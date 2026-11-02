"""Exhaustive independent factor-pattern test for cubic Möbius shift correlations.

Only ordinary finite-field arithmetic and root/multiplicity tests are used;
no cubic discriminant identities are assumed.
"""
from itertools import product


def make_field(p, modulus):
    # The modulus is the monic low-to-high coefficient tuple.
    m = len(modulus) - 1
    q = p ** m
    digs = [tuple((i // p**j) % p for j in range(m)) for i in range(q)]
    def enc(v):
        return sum((int(a) % p) * p**j for j, a in enumerate(v))
    add = [[enc([(u[j] + v[j]) % p for j in range(m)]) for v in digs] for u in digs]
    mul = []
    for u in digs:
        row = []
        for v in digs:
            a = [0]*(2*m-1)
            for i in range(m):
                for j in range(m):
                    a[i+j] += u[i]*v[j]
            for d in range(2*m-2, m-1, -1):
                coeff = a[d] % p
                for j in range(m):
                    a[d-m+j] -= coeff*modulus[j]
            row.append(enc(a[:m]))
        mul.append(row)
    return q, add, mul


def mu_profile(q, add, mul, p):
    # For cubic polynomials, any repeated irreducible factor is linear.
    # Squarefree cubics with 0, 1, 3 rational roots have signs -,+,-.
    triple = 3 % p
    double = 2 % p
    neg = [[next(k for k in range(q) if add[i][k] == 0) for i in range(q)]][0]
    signs = [[[0 for c in range(q)] for b in range(q)] for a in range(q)]
    for a in range(q):
        for b in range(q):
            counts = [0]*q
            multiple = [False]*q
            for x in range(q):
                x2 = mul[x][x]
                x3 = mul[x2][x]
                ax2 = mul[a][x2]
                bx = mul[b][x]
                c = neg[add[add[x3][ax2]][bx]]
                counts[c] += 1
                deriv = add[add[mul[triple][x2]][mul[double][mul[a][x]]]][b]
                if deriv == 0:
                    multiple[c] = True
            for c in range(q):
                if multiple[c]:
                    signs[a][b][c] = 0
                else:
                    assert counts[c] in (0,1,3), (p,q,a,b,c,counts[c])
                    signs[a][b][c] = 1 if counts[c] == 1 else -1
    return signs


def run():
    fields = [
        (3, (0,1)), (5,(0,1)), (7,(0,1)), (11,(0,1)),
        (13,(0,1)), (17,(0,1)), (23,(0,1)),
        (3,(1,0,1)),       # z^2+1
        (3,(1,2,0,1)),     # z^3+2z+1, irreducible
        (5,(2,0,1)),       # z^2+2
    ]
    cases = 0
    for p, poly in fields:
        q, add, mul = make_field(p,poly)
        profile = mu_profile(q,add,mul,p)
        corr = []
        for h in range(1,q):
            val = sum(profile[a][b][c]*profile[a][b][add[c][h]]
                      for a in range(q) for b in range(q) for c in range(q))
            corr.append(val)
            if q % 3 != 1:
                assert val == 0, (q,h,val)
            cases += 1
        if q == 7:
            assert corr[0] == -91 and corr[1] == 77
        print('FIELD', q, 'zero_all_nonzero_shifts', all(c == 0 for c in corr),
              'values', sorted(set(corr)))
    print('VERIFY_OK fields',len(fields),'shift_cases',cases)


if __name__ == '__main__':
    run()
