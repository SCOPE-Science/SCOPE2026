"""Exact combinatorial verifier for total domination in K_m tensor K_n.

All arithmetic is integral. The exhaustive test checks the original
vertex-neighborhood definition, not the proof's column classification.
"""
from math import comb


def add_scaled_power(a, scale, power, base=1):
    for j in range(power + 1):
        a[j] += scale * comb(power, j) * (base ** j)


def coefficients(m, n):
    if min(m, n) < 2:
        return [0] * (m*n+1)
    a = [0] * (m*n+1)
    add_scaled_power(a, 1, m*n)
    add_scaled_power(a, -m*n, m+n-1)
    add_scaled_power(a, m*(n-1), n)
    add_scaled_power(a, n*(m-1), m)
    a[0] -= (m-1)*(n-1)
    a[2] += m*(m-1)*n*(n-1)//2
    return a


def by_column_cases(m, n):
    # Directly assemble the three disjoint column-type cases from the proof.
    from math import comb
    L = m*n+1
    a=[0]*L
    def mul(x,y):
        z=[0]*L
        for i,v in enumerate(x):
            if v:
                for j,w in enumerate(y[:L-i]):
                    z[i+j]+=v*w
        return z
    def power(x,k):
        y=[1]+[0]*(L-1)
        for _ in range(k): y=mul(y,x)
        return y
    one_col=[comb(m,k) for k in range(m+1)]
    singular=[1,m]+[0]*(m-1)
    strong=[0,0]+[comb(m,k) for k in range(2,m+1)]
    for i,v in enumerate(power(one_col,n)):a[i]+=v
    for i,v in enumerate(power(singular,n)):a[i]-=v
    q=mul(strong,power(singular,n-1))
    for i,v in enumerate(q):a[i]-=n*v
    # One strong column: all remaining columns singleton-or-empty,
    # minus assignments supported on zero or just one row label.
    eligible=power(singular,n-1)
    p=power([1,1]+[0]*(m-1),n-1)
    eligible=[x-m*y for x,y in zip(eligible,p)]
    eligible[0]+=m-1
    for i,v in enumerate(mul(strong,eligible)):a[i]+=n*v
    # No strong column: t named columns with row labels that do
    # not concentrate on t or t-1 positions in a single row.
    for t in range(3,n+1):
        a[t]+=comb(n,t)*(m**t-m-t*m*(m-1))
    return a


def direct(m, n):
    masks = []
    for i in range(m):
        for j in range(n):
            masks.append(sum(1 << (p*n+q)
                             for p in range(m) if p != i
                             for q in range(n) if q != j))
    a = [0]*(m*n+1)
    for S in range(1 << (m*n)):
        if all(S & mask for mask in masks):
            a[S.bit_count()] += 1
    return a


def minima(m,n):
    a = coefficients(m,n)
    for k, v in enumerate(a):
        if v:
            return k, v
    return None


def run():
    checked=0
    enumerated=0
    for m in range(2,7):
        for n in range(m,10):
            if m*n > 18: continue
            x=coefficients(m,n)
            y=direct(m,n)
            assert x==y,(m,n,x,y)
            assert x==coefficients(n,m)
            target=(4,comb(n,2)**2) if m==2 else (3,6*comb(m,3)*comb(n,3))
            assert minima(m,n)==target,(m,n,minima(m,n),target)
            checked+=1
            enumerated+=2**(m*n)
    for m in range(2,31):
        for n in range(2,31):
            x=coefficients(m,n)
            assert x==coefficients(n,m)
            assert x==by_column_cases(m,n),(m,n)
            assert min(x)>=0,(m,n)
            assert sum(x)>0
            target=(4,comb(max(m,n),2)**2) if min(m,n)==2 else (3,6*comb(m,3)*comb(n,3))
            assert minima(m,n)==target,(m,n,minima(m,n),target)
    print(f'PASS: {checked} parameter pairs; {enumerated} labeled subsets independently enumerated')
    print('PASS: three-case column algebra, coefficient symmetry, nonnegativity and minimum-set formulas for 841 parameter pairs')
    for m,n in [(2,2),(2,3),(3,3),(3,4),(4,4)]:
        print(f'K_{m} tensor K_{n}: minimum/number={minima(m,n)}; coeffs={coefficients(m,n)}')

if __name__=='__main__': run()
