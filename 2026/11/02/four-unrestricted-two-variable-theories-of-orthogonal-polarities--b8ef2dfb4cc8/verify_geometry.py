"""Finite-field coordinate verifier for loop-retaining projective orthogonality."""
from collections import Counter

PRIME={2:2,3:3,4:2,5:5,7:7,8:2,9:3,11:11,13:13,16:2,25:5}
BIT_POLY={2:0b11,4:0b111,8:0b1011,16:0b10011}

def arithmetic(q):
    p=PRIME[q]
    if p==2:
        mod=BIT_POLY[q]
        def plus(a,b): return a^b
        def times(a,b):
            v=0
            while b:
                if b&1:v^=a
                b>>=1
                a<<=1
                if a&q:a^=mod
            return v
    elif q==p:
        def plus(a,b):return (a+b)%p
        def times(a,b):return (a*b)%p
    else:
        assert q==p*p
        c={9:2,25:3}[q]
        def plus(a,b):
            a0,a1=a%p,a//p;b0,b1=b%p,b//p
            return (a0+b0)%p+p*((a1+b1)%p)
        def times(a,b):
            a0,a1=a%p,a//p;b0,b1=b%p,b//p
            return (a0*b0+c*a1*b1)%p+p*((a0*b1+a1*b0)%p)
    for x in range(1,q):assert any(times(x,y)==1 for y in range(1,q))
    return plus,times

def graph(q):
    plus,times=arithmetic(q)
    verts=[(1,a,b) for a in range(q) for b in range(q)] + [(0,1,a) for a in range(q)]+[(0,0,1)]
    n=len(verts)
    assert n==q*q+q+1
    adj=[[False]*n for i in range(n)]
    for i,x in enumerate(verts):
        for j,y in enumerate(verts):
            z=plus(plus(times(x[0],y[0]),times(x[1],y[1])),times(x[2],y[2]))
            adj[i][j]=(z==0)
    assert all(adj[i][j]==adj[j][i] for i in range(n) for j in range(n))
    return verts,adj

def types(q,adj):
    n=len(adj); ab=[adj[i][i] for i in range(n)]
    if q%2:
        tt=['A' if ab[i] else 'E' if any(adj[i][j] and ab[j] for j in range(n)) else 'I' for i in range(n)]
        expected={'A':q+1,'E':q*(q+1)//2,'I':q*(q-1)//2}
    else:
        tt=['A' if ab[i] else 'C' if all(not adj[i][j] or ab[j] for j in range(n)) else 'N' for i in range(n)]
        expected={'A':q+1,'C':1,'N':q*q-1}
    assert Counter(tt)==expected,(q,Counter(tt),expected)
    return tt

def expected(q,T):
    if q%2:
        if T=='A':return {'A':0,'E':q,'I':0}
        if T=='E':return {'A':2,'E':(q-1)//2,'I':(q-1)//2}
        if T=='I':return {'A':0,'E':(q+1)//2,'I':(q+1)//2}
    else:
        if T=='A':return {'A':0,'C':1,'N':q-1}
        if T=='C':return {'A':q+1,'C':0,'N':0}
        if T=='N':return {'A':1,'C':0,'N':q}
    raise ValueError((q,T))

def verify(q):
    verts,adj=graph(q);typ=types(q,adj);n=len(typ)
    counts=Counter(typ)
    for i,T in enumerate(typ):
        d={S:sum(adj[i][j] for j in range(n) if j!=i and typ[j]==S) for S in counts}
        want=expected(q,T)
        assert d==want,(q,i,T,d,want)
    # each pair has exactly one common neighbor, including loops
    for i in range(n):
        for j in range(i+1,n):
            common=sum(adj[i][k] and adj[j][k] for k in range(n))
            assert common==1,(q,i,j,common)
    return n,counts

if __name__=='__main__':
    for q in PRIME:
        n,c=verify(q)
        print('GEOMETRY_OK',q,'vertices',n,'types',','.join(f'{t}:{c[t]}' for t in sorted(c)))
    print('GEOMETRY_ALL_PASS')
