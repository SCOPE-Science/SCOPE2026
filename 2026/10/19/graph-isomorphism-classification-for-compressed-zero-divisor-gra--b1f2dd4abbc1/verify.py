"""Exact finite-field and full-ring checks of projective compressed zero-divisor graphs."""
from itertools import product
from collections import Counter

class F:
    def __init__(self,q):
        assert q in (2,3,4,5,7)
        self.q=q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def mul(self,a,b):
        if self.q!=4:return a*b%self.q
        z=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1: z ^= (1<<(i+j))
        if z&8: z ^= 0b1110  # x^3 = x(x+1) = x^2+x
        if z&4: z ^= 0b111   # x^2=x+1
        return z
    def inv(self,a):
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)
    def zero(self):return 0

def bil(F,M,v,w):
    s=0
    for i,row in enumerate(M):
        for j,b in enumerate(row):s=F.add(s,F.mul(b,F.mul(v[i],w[j])))
    return s

def projective(F,d):
    ret=[]
    for v in product(range(F.q),repeat=d):
        if not any(v):continue
        a=next(x for x in v if x)
        t=tuple(F.mul(F.inv(a),x) for x in v)
        if t not in ret:ret.append(t)
    return ret

def graph(F,M):
    d=len(M);p=projective(F,d);N=len(p);Q=(F.q**(d-1)-1)//(F.q-1)
    I=sum(bil(F,M,v,v)==0 for v in p)
    adjacency=[set() for _ in range(N+1)]
    for a in range(N):
        adjacency[a].add(N);adjacency[N].add(a)
        for b in range(a+1,N):
            if bil(F,M,p[a],p[b])==0:
                adjacency[a].add(b);adjacency[b].add(a)
    expected=Counter({Q:I,Q+1:N-I})
    if I==0: expected=Counter({Q+1:N})
    if I==N: expected=Counter({Q:N})
    assert Counter(len(adjacency[i]) for i in range(N))==expected,(F.q,d,I,expected)
    assert len(adjacency[N])==N
    assert sum(map(len,adjacency))//2==N+(N*Q-I)//2
    if F.q%2==0:
        alt=all(M[i][i]==0 for i in range(d))
        assert I==(N if alt else Q),(F.q,d,I,Q,N)
    elif d%2:
        assert I==Q,(F.q,d,I,Q)
    else:
        assert abs(I-Q)==F.q**((d-2)//2),(F.q,d,I,Q)
    return adjacency,p,I

def direct_ann(F,M):
    d=len(M);z=(0,)*(d+1)
    rad=[v for v in product(range(F.q),repeat=d+1) if v!=z]
    sig={}
    for v in rad:
        sig[v]=tuple(i for i,w in enumerate(rad) if bil(F,M,v[:d],w[:d])==0)
    bysig={}
    for v,s in sig.items():bysig.setdefault(s,[]).append(v)
    verts=list(bysig.values()); adj=[set() for _ in verts]
    for i in range(len(verts)):
        for j in range(i+1,len(verts)):
            if bil(F,M,verts[i][0][:d],verts[j][0][:d])==0:
                adj[i].add(j);adj[j].add(i)
    pg,_,I=graph(F,M)
    assert len(verts)==len(pg)
    assert Counter(len(x) for x in pg)==Counter(len(x) for x in adj)
    assert sum(map(len,pg))==sum(map(len,adj))
    print('RING_OK',F.q,d,'classes',len(adj),'isotropic',I)

def fullring(elements,prod,zerop):
    nonzero=[x for x in elements if x!=zerop]
    units=[x for x in nonzero if any(prod(x,y)==one for y in elements)] # one defined below globally
    rad=[x for x in nonzero if x not in units]
    sig={x:tuple(i for i,y in enumerate(elements) if prod(x,y)==zerop) for x in rad}
    bysig={}
    for x,s in sig.items():bysig.setdefault(s,[]).append(x)
    cls=list(bysig.values()); G=[set() for _ in cls]
    for i in range(len(cls)):
        for j in range(i+1,len(cls)):
            if prod(cls[i][0],cls[j][0])==zerop:
                G[i].add(j);G[j].add(i)
    return sorted(map(len,G)),sum(map(len,G))//2

if __name__=='__main__':
    matrices={
        2:[[[0,1],[1,0]],[[1,0],[0,1]]],
        3:[[[1,0,0],[0,1,0],[0,0,1]]],
        4:[[[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]],[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]]
    }
    checks=0
    for q in [2,3,4,5,7]:
        Fq=F(q)
        for d,arr in matrices.items():
            for M in arr:
                graph(Fq,M); checks+=1
                if d<=3 and q<=5:direct_ann(Fq,M)
    # Concrete characteristic-two and characteristic-four, nonisomorphic local Gorenstein rings.
    elements=list(product(range(2), repeat=4))
    one=(1,0,0,0)
    def char2(x,y):
        a,b,c,d=x;A,B,C,D=y
        return ((a*A)%2,(a*B+b*A)%2,(a*C+c*A)%2,(a*D+d*A+b*C+c*B)%2)
    G1=fullring(elements,char2,(0,0,0,0))
    elements=list(product(range(4),repeat=2));one=(1,0)
    def char4(x,y):return ((x[0]*y[0])%4,(x[0]*y[1]+x[1]*y[0])%4)
    G2=fullring(elements,char4,(0,0))
    assert G1==G2==([1,1,1,3],3),(G1,G2)
    print('NONRIGID_OK char2/char4 identical K_1,3')
    print('VERIFY_OK',checks,'polar-field configurations plus direct annihilator computations')
