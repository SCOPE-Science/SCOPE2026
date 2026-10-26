"""Direct finite-field checks of restricted power heights in sl2 truncated currents.

Usage: python3 verify.py
Only prime fields are needed for the exhaustive small checks; the proof covers prime powers.
"""
from itertools import product
from collections import Counter

def predicted(q, m, k):
    if k == 0:
        return 1
    # All tested coefficient fields are prime fields, so q is the characteristic.
    a = q ** k
    cut = (m + a - 1) // a
    ans = q ** (3 * (m-cut))
    for v in range(cut):
        h = (2*(m-a*v) + a-2) // (a-1)
        r = m-v
        assert 1 <= h <= r
        ans += (q*q-1) * q**(3*r-h-2)
    return ans

def poly_mul(a,b,p):
    m = len(a)
    c=[0]*m
    for i in range(m):
        if a[i]:
            for j in range(m-i):
                c[i+j] = (c[i+j]+a[i]*b[j])%p
    return tuple(c)

def matmul(A,B,p):
    return tuple(tuple(tuple((poly_mul(A[i][0],B[0][j],p)[h] + poly_mul(A[i][1],B[1][j],p)[h])%p for h in range(len(A[0][0]))) for j in range(2)) for i in range(2))

def zero(A):
    return all(a==0 for row in A for ent in row for a in ent)

def actual_counts(p,m):
    zero_poly=(0,)*m
    hist=Counter()
    for c,a,b in product(product(range(p),repeat=m),repeat=3):
        negc=tuple((-u)%p for u in c)
        X=((c,a),(b,negc))
        if zero(X):
            hist[0]+=1
            continue
        Y=X
        for k in range(1,12):
            # Compute Y**p (not using the Cayley-Hamilton identity).
            Z=Y
            for _ in range(p-1):
                Z=matmul(Z,Y,p)
            Y=Z
            if zero(Y):
                hist[k]+=1
                break
        else:
            hist[-1]+=1
    return hist

def main():
    cases=[(3,1),(3,2),(3,3),(5,1),(5,2),(7,1)]
    for p,m in cases:
        hist=actual_counts(p,m)
        assert sum(hist.values())==p**(3*m)
        assert hist[-1]==p**(3*m)-p**(3*m-1)
        for k in range(0,6):
            got=sum(v for j,v in hist.items() if 0<=j<=k)
            want=predicted(p,m,k)
            assert got==want, (p,m,k,got,want)
        print('CHECK',p,m,'height histogram',dict(sorted(hist.items())))
    print('VERIFY_OK')

if __name__=='__main__': main()
