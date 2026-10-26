"""Independent finite-field enumeration for cycle graphical-group abelian subgroups.
Only prime fields are needed for these exhaustive checks; theorem covers every finite field.
"""
from collections import Counter
from itertools import product
from math import comb

def gl2(q):
    return (q*q-1)*(q*q-q)

def predicted(n,q):
    # Coefficient arrays, independent transfer-polynomial path.
    z=q+1
    Q=q-1
    # evaluate sum over supports directly; each component chooses a line
    ans=Counter()
    for mask in range(1<<n):
        s=mask.bit_count()
        if s==0: continue
        visited=0; c=0
        for i in range(n):
            if not (mask>>i)&1 or (visited>>i)&1: continue
            c+=1
            frontier=[i]
            visited|=1<<i
            while frontier:
                j=frontier.pop()
                for v in ((j-1)%n,(j+1)%n):
                    if (mask>>v)&1 and not (visited>>v)&1:
                        visited|=1<<v; frontier.append(v)
        ans[s]+=Q**s*(z**c-z)
    assert all(x % gl2(q)==0 for x in ans.values())
    return Counter({s:v//gl2(q) for s,v in ans.items() if v})

def transfer(n,q):
    # polynomial arithmetic independent of the graph support enumeration.
    def add(a,b):
        return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b))) ]
    def mul_x(a): return [0]+[v*(q-1) for v in a]
    def mul_1w(a): return add(a,mul_x(a))
    t0=[2];t1=[1,q-1]
    for _ in range(2,n+1):
        t0,t1=t1,add(mul_1w(t1),[0]+[v*q for v in mul_x(t0)[1:]])
    # correction term q w^n - (q+1)(1+w)^n + q
    corr=[- (q+1)*comb(n,j)*(q-1)**j for j in range(n+1)]
    corr[0]+=q
    corr[n]+=q*(q-1)**n
    sums=add(t1,corr)
    assert all(v%gl2(q)==0 for v in sums)
    return Counter({i:v//gl2(q) for i,v in enumerate(sums) if v})

def brute(n,q):
    # Iterate ordered pairs (u,v) of basis row vectors, entirely independently.
    # Each rank-two subspace is represented by |GL_2(q)| ordered pairs.
    res=Counter()
    for a in product(range(q),repeat=n):
        for b in product(range(q),repeat=n):
            support=[j for j in range(n) if a[j] or b[j]]
            if not any((a[j]*b[k]-a[k]*b[j])%q for j in range(n) for k in range(j+1,n)):
                continue
            if any((a[j]*b[(j+1)%n]-a[(j+1)%n]*b[j])%q for j in range(n)):
                continue
            res[len(support)]+=1
    assert all(v%gl2(q)==0 for v in res.values())
    return Counter({i:v//gl2(q) for i,v in res.items()})

def verify():
    cases=[(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,4),(3,5),(5,3),(5,4)]
    for q,n in cases:
        exp=predicted(n,q); got=brute(n,q); tr=transfer(n,q)
        assert exp==got==tr, (q,n,exp,got,tr)
        print(f'CHECK q={q} n={n} planes={sum(got.values())} support={dict(sorted(got.items()))}')
    # Larger exact transfer-versus-support comparison without enumerating bases.
    for q in (2,3,4,5,7,9):
        for n in range(3,13):
            assert predicted(n,q)==transfer(n,q), (q,n)
    print('VERIFY_OK')

if __name__=='__main__':
    verify()
