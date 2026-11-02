"""Independent finite-field enumeration of idempotent algebra endomorphisms and commuting components of K<x,y>/(x²,y²,xy-lambda*yx)."""
from itertools import product
from collections import Counter, deque


def field(q):
    if q == 4:
        add=lambda a,b:a^b
        def mul(a,b):
            r=0
            for i in range(2):
                if (a>>i)&1:
                    for j in range(2):
                        if (b>>j)&1:r^=1<<(i+j)
            if r&8:r^=0b1100 # x^3 = x^2+x; x^3+x^2+x =0; reduction via x²=x+1, x³=1
            if r&4:r^=0b111
            return r
        # direct test multiplication in GF4 under X^2+X+1
        assert mul(2,2)==3 and mul(2,3)==1
        return add,mul,lambda a:1 if a else None,lambda a: {1:1,2:3,3:2}.get(a)
    add=lambda a,b:(a+b)%q
    mul=lambda a,b:(a*b)%q
    return add,mul,lambda a:1 if a else None,lambda a:pow(a,q-2,q) if a else None

def experiment(q,lam):
    add,mul,_,inv=field(q)
    zero=(0,0,0,0)
    x=(0,1,0,0);y=(0,0,1,0);z=(0,0,0,1)
    c=inv(lam)
    def addv(u,v):return tuple(add(a,b) for a,b in zip(u,v))
    def scalar(a,v):return tuple(mul(a,b) for b in v)
    def prod(u,v):
        # normalized 1,x,y,xy basis; x*y=z, y*x=lam^-1 z
        o=[0]*4
        for i in range(4):
            for j in range(4):
                a=mul(u[i],v[j])
                if not a:continue
                if i==0:k=j;coef=1
                elif j==0:k=i;coef=1
                elif (i,j)==(1,2):k=3;coef=1
                elif (i,j)==(2,1):k=3;coef=c
                else:continue
                o[k]=add(o[k],mul(a,coef))
        return tuple(o)
    assert prod(x,y)==z and prod(y,x)==scalar(c,z)
    def square_zero(v):return prod(v,v)==zero
    def valid(u,v):return square_zero(u) and square_zero(v) and prod(u,v)==scalar(lam,prod(v,u))
    def apply(A,w):
        u,v=A
        return addv(addv(scalar(w[1],u),scalar(w[2],v)),scalar(w[3],prod(u,v)))
    def comp(A,B):return (apply(A,B[0]),apply(A,B[1]))
    idemps=[];end_count=0;aut_count=0
    for a,b,c0,d,e,f in product(range(q),repeat=6):
        u=(0,a,b,c0);v=(0,d,e,f)
        if not valid(u,v):continue
        end_count+=1
        if add(mul(a,e), mul(b,d) if q==4 or q==2 else (-mul(b,d))%q) != 0: aut_count+=1
        pair=(u,v)
        if comp(pair,pair)==pair:
            idemps.append(pair)
    isext=lam==(-1)%q if q!=4 else lam==1
    iscomm=lam==1 and not isext
    exp_end=q**6 if isext else (q*q*(2*q-1)**2 if iscomm else q**3*(3*q-2))
    exp_aut=q*q*(q*q-1)*(q*q-q) if isext else ((2 if iscomm else 1)*q*q*(q-1)**2)
    assert (end_count,aut_count)==(exp_end,exp_aut),(q,lam,end_count,exp_end,aut_count,exp_aut)
    predicted=q*q*(q+1)+2 if isext else 2*q*q+2
    assert len(idemps)==predicted,(q,lam,len(idemps),predicted)
    augment=(zero,zero)
    identity=(x,y)
    assert augment in idemps and identity in idemps
    vertices=[a for a in idemps if a not in (augment,identity)]
    adjacency=[set() for _ in vertices]
    for i,A in enumerate(vertices):
        for j in range(i+1,len(vertices)):
            B=vertices[j]
            if comp(A,B)==comp(B,A):
                adjacency[i].add(j);adjacency[j].add(i)
    parts=[]
    seen=set()
    for i in range(len(vertices)):
        if i in seen:continue
        todo=[i];seen.add(i);cc=[]
        while todo:
            h=todo.pop();cc.append(h)
            for v in adjacency[h]:
                if v not in seen:seen.add(v);todo.append(v)
        parts.append(cc)
    sizes=Counter(map(len,parts))
    exp_sizes=Counter({2*q:q*(q+1)//2}) if isext else Counter({2*q:1,1:2*q*(q-1)})
    assert sizes==exp_sizes,(q,lam,sizes,exp_sizes)
    for cc in parts:
        if len(cc)>1:
            assert all(len(adjacency[v])==q for v in cc)
            assert sum(len(adjacency[v]) for v in cc)//2==q*q
            assert not any((a in adjacency[b]) and (b in adjacency[c0]) and (a in adjacency[c0]) for a in cc for b in adjacency[a] for c0 in adjacency[b] if c0!=a)
    pairs=sum(len(s) for s in adjacency)//2
    exp_pairs=q**3*(q+1)//2 if isext else q*q
    assert pairs==exp_pairs,(q,lam,pairs,exp_pairs)
    print(f'CHECK_OK q={q} lambda={lam} exterior={isext} endomorphisms={end_count} automorphisms={aut_count} idempotents={len(idemps)} edges={pairs} components={dict(sizes)}')

for q in (2,3,4,5):
    for lam in range(1,q):
        experiment(q,lam)
print('VERIFY_OK')
