"""Independent finite-field checks for square-zero elements in M_2(F_q[t]/t^n).
Execute with: python checker.py. No third-party packages required.
"""
from collections import Counter
from itertools import product
from fractions import Fraction


def rank_polynomial(n, q):
    if n < 1 or q < 2:
        raise ValueError('n >= 1 and q >= 2 required')
    c = (n+1)//2
    h = n//2
    C = (q*q - 1)*q**(2*n-2)
    P = Counter()
    for k in range(c):
        for j in range(k):
            P[n-j] += C * Fraction(q-1, q**(j+1))
        P[n-k] += C * Fraction(1, q**k)
    P[0] += 1
    R1 = (q-1)*(q+1)**2
    for m in range(1, h+1):
        scale = q**(4*(m-1))
        gl2 = q*(q-1)**2*(q+1)*scale
        P[2*m] += gl2
        for s in range(1, m):
            P[2*m-s] += R1*scale*Fraction(q-1, q**s)
        P[m] += R1*scale*Fraction(1, q**(m-1))
    assert all(x.denominator == 1 for x in P.values())
    P = Counter({r: int(count) for r, count in P.items()})
    total = c*(q*q-1)*q**(2*n-2) + q**(4*h)
    assert sum(P.values()) == total
    assert sum(P.values()) >= 1
    return P


def poly_mul(a,b,n,q):
    out=[0]*n
    for i, ai in enumerate(a):
        if ai:
            for j in range(n-i):
                out[i+j] = (out[i+j] + ai*b[j]) % q
    return tuple(out)


def poly_add(a,b,q):
    return tuple((x+y)%q for x,y in zip(a,b))


def matrix_rank(columns, q):
    basis = {}
    for col in columns:
        v = list(col)
        while True:
            lead = next((i for i, z in enumerate(v) if z), None)
            if lead is None:
                break
            if lead not in basis:
                inv = pow(v[lead], -1, q)
                basis[lead] = [(inv*z)%q for z in v]
                break
            b = basis[lead]
            c = v[lead]
            v = [(x-c*y)%q for x,y in zip(v,b)]
    return len(basis)


def brute(n,q):
    zero=(0,)*n
    one = (1,) + (0,)*(n-1)
    polys=list(product(range(q),repeat=n))
    # The four matrix entries are polynomials, not only their reductions.
    out=Counter()
    for a,b,c,d in product(polys,repeat=4):
        aa=poly_mul(a,a,n,q)
        bc=poly_mul(b,c,n,q)
        if any(poly_add(aa,bc,q)):continue
        ab=poly_mul(a,b,n,q)
        bd=poly_mul(b,d,n,q)
        if any(poly_add(ab,bd,q)):continue
        ca=poly_mul(c,a,n,q)
        dc=poly_mul(d,c,n,q)
        if any(poly_add(ca,dc,q)):continue
        cb=poly_mul(c,b,n,q)
        dd=poly_mul(d,d,n,q)
        if any(poly_add(cb,dd,q)):continue
        columns=[]
        for j in range(n):
            t=(0,)*j+(1,)+(0,)*(n-j-1)
            columns.append(poly_mul(a,t,n,q)+poly_mul(c,t,n,q))
        for j in range(n):
            t=(0,)*j+(1,)+(0,)*(n-j-1)
            columns.append(poly_mul(b,t,n,q)+poly_mul(d,t,n,q))
        out[matrix_rank(columns,q)]+=1
    return out


def main():
    for n,q in [(1,2),(2,2),(3,2),(4,2),(1,3),(2,3),(1,5),(2,5)]:
        predicted=rank_polynomial(n,q)
        observed=brute(n,q)
        assert predicted==observed, (n,q,dict(predicted),dict(observed))
        print(f'PASS n={n}, q={q}, count={sum(observed.values())}, rank_profile={sorted(observed.items())}')
    for q in [2,3,4,5,7,8,9,11]:
        for n in range(1,13):
            p=rank_polynomial(n,q)
            assert sum(p.values()) == (n+1)//2*(q*q-1)*q**(2*n-2)+q**(4*(n//2))
    print('ALL_EXACT_CHECKS_PASSED')

if __name__ == '__main__':
    main()
