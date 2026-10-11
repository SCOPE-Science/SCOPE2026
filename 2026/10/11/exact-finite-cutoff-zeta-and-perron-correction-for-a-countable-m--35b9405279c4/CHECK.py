"""Finite arithmetic diagnostics for the finite-cutoff map theorem.
Run: python CHECK.py (Python 3 standard library only).
Finite tests do not establish the asymptotic theorem.
"""
from decimal import Decimal, getcontext
from fractions import Fraction


def groups(r):
    return [4] + [3 * 4 ** (j - 1) for j in range(2, r + 1)]


def quotient(r):
    mm = groups(r)
    return [[mm[k] if k <= j else (1 if k == j + 1 else 0)
             for k in range(r)] for j in range(r)]


def full_matrix(r):
    n = 4 ** r
    return [[int(j < min(4 ** ell + 1, n)) for j in range(n)]
            for i in range(1, n + 1)
            for ell in [1 if i <= 4 else next(k for k in range(2, r + 1) if i <= 4 ** k)]]


def matmul(a, b):
    n = len(a)
    p = len(b)
    q = len(b[0])
    out = [[0]*q for _ in range(n)]
    for i in range(n):
        for k in range(p):
            if a[i][k]:
                aik = a[i][k]
                for j in range(q):
                    out[i][j] += aik * b[k][j]
    return out


def traces(a, upto):
    n = len(a)
    power = [[int(i == j) for j in range(n)] for i in range(n)]
    ans = []
    for _ in range(upto):
        power = matmul(power, a)
        ans.append(sum(power[i][i] for i in range(n)))
    return ans


def coeffs_from_traces(ts):
    c = [Fraction(1)]
    for j in range(1, len(ts)+1):
        c.append(-sum(c[j-k]*ts[k-1] for k in range(1,j+1))/j)
    return c


def perron(r):
    getcontext().prec = 65
    cc = quotient(r)
    x = [Decimal(1)] * r
    for _ in range(150):
        y = [sum(Decimal(c) * x[j] for j, c in enumerate(row)) for row in cc]
        lam = y[-1]
        x = [entry/lam for entry in y]
    assert max(abs(sum(Decimal(c)*x[j] for j,c in enumerate(row))-lam*x[i]) for i,row in enumerate(cc)) < Decimal('1e-45')
    return lam


def run():
    checks = 0
    for r in range(1, 4):
        n = 4**r
        a = full_matrix(r)
        c = quotient(r)
        assert len(a)==n and len(c)==r
        upto = 7 if r<=2 else 4
        ta, tc = traces(a, upto), traces(c, upto)
        for k,(v,w) in enumerate(zip(ta,tc), start=1):
            assert v==w, ('trace mismatch',r,k,v,w)
            checks+=1
        assert ta[0] == n
        checks+=1
        if r >=2:
            assert ta[1] == Fraction(3*n*n,5)+Fraction(n,2)+Fraction(32,5)
            checks+=1
    for r in range(1,7):
        c=quotient(r)
        coeff=coeffs_from_traces(traces(c,r))
        assert all(x.denominator==1 for x in coeff)
        checks+=1
    assert coeffs_from_traces(traces(quotient(2),2)) == [1,-16,44]
    checks+=1
    bound=Decimal(0)
    for r in range(4,12):
        m=Decimal(3*4**(r-1))
        lam=perron(r)
        delta=lam-m
        assert Decimal(0)<delta<Decimal('0.5')
        error=(delta-Decimal(1)/3+Decimal(4)/(135*m))*m*m
        assert abs(error)<Decimal(1), ('asymptotic residual unexpectedly large',r,str(error))
        bound=max(bound,abs(error))
        checks+=2
        print('r=',r,'m=',int(m),'lambda-m=',str(delta)[:28], 'scaled_remainder=',str(error)[:28])
    print('CHECK_OK',checks,'exact matrix/trace/determinant and high-precision asymptotic diagnostics; bounded second-order residual',str(bound))

if __name__=='__main__':
    run()
