#!/usr/bin/env python3
"""Independent finite-case verification for biclique continuous-map rank enumerators.

Run: python3 verify.py
Only Python's standard library is needed. Exhaustive tests are finite checks;
the general theorem follows from the separately stated proof.
"""
from itertools import product
from collections import Counter
from math import comb, factorial


def fall(s, j):
    if j < 0 or s < j:
        return 0
    ans = 1
    for t in range(j):
        ans *= s-t
    return ans


def theory(m, n):
    # H, Q, and E coefficient arrays, including rank zero.
    H = Counter({0:1}); Q = Counter(); E = Counter({0:1})
    for k in range(1, max(m, n)+1):
        image_sets = (comb(m,k) if k<=m else 0)+(comb(n,k) if k<=n else 0)
        T = sum(comb(k,c)*fall(m,c)*fall(n,c)*fall(m+n-2*c,k-c)
                for c in range(min(m,n,k)+1))
        F = sum(factorial(k)//(factorial(a)*factorial(b)*factorial(k-a-b))
                *fall(m,k-b)*fall(n,k-a)
                for a in range(1,k) for b in range(1,k-a+1))
        H[k] += image_sets*T
        Q[k] += image_sets*F
        if k<=m:
            E[k] += comb(m,k)*sum(comb(k,c)*fall(n,c) for c in range(min(k,n)+1))
        if k<=n:
            E[k] += comb(n,k)*sum(comb(k,c)*fall(m,c) for c in range(min(k,m)+1))
    for a in range(1,m+1):
        for b in range(1,n+1):
            k=a+b
            w=comb(m,a)*comb(n,b)
            H[k]+=w*(fall(m,a)*fall(n,b)+fall(n,a)*fall(m,b))
            E[k]+=w
    return H, Q, E


def continuous(f,m,n):
    N = m+n
    cells = [(i,) for i in range(N)] + [(i,j) for i in range(m) for j in range(m,N)]
    for simplex in cells:
        pre = [v for v,x in enumerate(f) if x in simplex]
        if len(pre)>2:
            return False
        if len(pre)==2 and (pre[0]<m)==(pre[1]<m):
            return False
    return True


def has_continuous_section(f,m,n):
    N=m+n
    fibers={y:[x for x,a in enumerate(f) if a==y]
            for y in sorted(set(f)) if y>=0}
    if not fibers:
        return True
    for representatives in product(*fibers.values()):
        section=[-1]*N
        for y,rep in zip(fibers, representatives):
            section[y]=rep
        if continuous(section,m,n):
            return True
    return False


def exhaustive(m,n):
    N=m+n
    H=Counter();Q=Counter();E=Counter()
    monoid=[]
    for f in product(range(-1,N), repeat=N):
        if not continuous(f,m,n):
            continue
        monoid.append(f)
        rank=len(set(f)-{-1})
        H[rank]+=1
        if not has_continuous_section(f,m,n):
            Q[rank]+=1
        if all(f[x]==x for x in f if x>=0):
            E[rank]+=1
    th,tq,te=theory(m,n)
    for computed, predicted,label in [(H,th,'total'),(Q,tq,'nonregular'),(E,te,'idempotent')]:
        assert computed==Counter({k:v for k,v in predicted.items() if v}), (m,n,label,computed,predicted)
    # Truly independent full-semigroup witnesses in small order:
    if N<=4:
        for f in monoid:
            section=has_continuous_section(f,m,n)
            found=False
            for g in monoid:
                # composition from left to right: f g f = f
                if all(f[g[f[x]]]==f[x] if x>=0 and f[x]>=0 and g[f[x]]>=0
                       else x<0 for x in range(N) if f[x]>=0):
                    found=True
                    break
            assert found==section,(m,n,f)
    return len(monoid),sum(Q.values()),sum(E.values()),dict(sorted(Q.items()))


def main():
    for m,n in [(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(3,3)]:
        total,nonregular,idempotents,qpoly=exhaustive(m,n)
        print(f'K_{{{m},{n}}}: total={total} nonregular={nonregular} '
              f'idempotents={idempotents} Q={qpoly}',flush=True)
    print('VERIFY_OK',flush=True)


if __name__=='__main__':
    main()
