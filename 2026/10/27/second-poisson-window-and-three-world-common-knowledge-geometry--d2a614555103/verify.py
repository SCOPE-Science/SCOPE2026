"""Exact finite checks for independently restricted uniform partitions."""
from functools import lru_cache
from math import comb, factorial

@lru_cache(None)
def parts(n):
    if n == 0:
        return ((),)
    out=[]
    for p in parts(n-1):
        out.append(p + ((n-1,),))
        for j in range(len(p)):
            q=list(p);q[j]=q[j]+(n-1,);out.append(tuple(q))
    return tuple(out)

def bell(n):return len(parts(n))

def restrict(p,m):
    return tuple(x for block in p if (x:=tuple(v for v in block if v<m)))

def R(n,m,b):
    return sum(comb(n-m,j)*b**j*bell(n-m-j) for j in range(n-m+1))

def x(p,m):
    return sum(comb(sum(v<m for v in block),2) for block in p)

for n in range(1,9):
    for m in range(n+1):
        frequencies={}
        for p in parts(n):
            q=tuple(sorted(restrict(p,m)))
            frequencies[q]=frequencies.get(q,0)+1
        for q in parts(m):
            q=tuple(sorted(q))
            assert frequencies[q]==R(n,m,len(q)), (n,m,q,frequencies[q],R(n,m,len(q)))
        lhs=sum(x(p,m) for p in parts(n))
        rhs=comb(m,2)*bell(n-1)
        assert lhs==rhs,(n,m,lhs,rhs)
        lhs2=sum(x(p,m)*(x(p,m)-1) for p in parts(n))
        rhs2=comb(comb(m,2),2)*2*bell(n-2) if n>=2 else 0
        assert lhs2==rhs2, (n,m,lhs2,rhs2)
    print('PARTITION_PATTERN_AND_FACTORIAL_MOMENTS_OK',n,bell(n))

# Two agents: all pairs of four-world partitions, independently uniform.
for m in range(1,5):
    n=4
    cnt=0
    for p in parts(n):
        if x(p,m):continue
        for q in parts(n):
            if x(q,m)==0:cnt+=1
    expected=sum(1 for p in parts(n) if x(p,m)==0)**2
    assert cnt==expected
    print('TWO_AGENT_DISCRETE_UPDATE_OK',n,m,cnt, bell(n)**2)
for n in range(2,9):
    for m in range(1,n+1):
        for k in range(2,min(m,5)+1):
            observed=sum(sum(sum(v<m for v in block)==k for block in p) for p in parts(n))
            single_prob_numerator=sum((-1)**h*comb(m-k,h)*bell(n-k-h+1) for h in range(m-k+1))
            predicted=comb(m,k)*single_prob_numerator
            assert observed==predicted,(n,m,k,observed,predicted)
    print('EXACT_K_CELL_SPECTRUM_OK',n)
print('FINITE_S5_UPDATE_CERTIFICATES_OK')

# Independent two-agent ordered-wedge and monochromatic-triple expectations.
def tags(p,n):
    t=[0]*n
    for j,b in enumerate(p):
        for v in b:t[v]=j
    return t
for n in range(3,7):
    P=[tags(p,n) for p in parts(n)]
    for m in range(3,min(n,5)+1):
        triple=sum(sum(PA[i]==PA[j]==PA[k] for i in range(m) for j in range(i+1,m) for k in range(j+1,m)) for PA in P)
        assert triple==comb(m,3)*bell(n-2)
        wedge=0
        for PA in P:
            for PB in P:
                wedge+=sum(PA[u]==PA[v] and PB[u]==PB[w] for u in range(m) for v in range(m) for w in range(m) if len({u,v,w})==3)
        assert wedge==m*(m-1)*(m-2)*bell(n-1)**2,(n,m,wedge)
        print('MIXED_WEDGE_AND_TRIPLE_MOMENTS_OK',n,m,triple,wedge)
print('SECOND_WINDOW_PATTERNS_OK')
