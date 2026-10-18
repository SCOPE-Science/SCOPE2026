#!/usr/bin/env python3
"""Independent finite checks for commuting tuples in length-m chain rings.

Uses direct pairwise 2x2 determinant tests, not the proof's valuation strata.
No external packages required.
"""
from itertools import product


def field_add(a, b, q):
    return (a ^ b) if q == 4 else ((a + b) % q)


def field_mul(a, b, q):
    if q != 4:
        return (a * b) % q
    # F_4 = F_2[u]/(u^2+u+1); field elements are binary coefficients.
    z = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & (b >> j) & 1:
                z ^= (1 << (i + j))
    if z & 8:
        z ^= 0b1110
    if z & 4:
        z ^= 0b111
    return z


def ring_ops(q, m, model):
    if model == 'integers':
        assert q in (2, 3)
        order = q ** m
        return order, lambda a,b:(a+b)%order, lambda a,b:(a*b)%order
    assert model == 'polynomial'
    order = q ** m
    digits = [tuple((i // (q ** j)) % q for j in range(m)) for i in range(order)]
    def encode(a):
        return sum(x*q**i for i, x in enumerate(a))
    adds = [[0]*order for _ in range(order)]
    muls = [[0]*order for _ in range(order)]
    for a in range(order):
        for b in range(order):
            da,db=digits[a],digits[b]
            adds[a][b] = encode([field_add(da[j],db[j],q) for j in range(m)])
            c = [0]*m
            for j in range(m):
                for i in range(j+1):
                    c[j]=field_add(c[j],field_mul(da[i],db[j-i],q),q)
            muls[a][b]=encode(c)
    return order, lambda a,b:adds[a][b], lambda a,b:muls[a][b]


def direct_count(q, m, r, model):
    size, add, mul = ring_ops(q,m,model)
    negatives = [next(b for b in range(size) if add(a,b)==0) for a in range(size)]
    vectors=list(product(range(size),repeat=2))
    count=0
    for row in product(vectors,repeat=r):
        ok=True
        for i in range(r):
            for j in range(i+1,r):
                if add(mul(row[i][0],row[j][1]), negatives[mul(row[i][1],row[j][0])]) != 0:
                    ok=False
                    break
            if not ok:
                break
        if ok:
            count+=1
    return count


def predicted(q,m,r):
    a=sum(q**j for j in range(m+1))
    return a*q**(m*r)-(a-1)*q**((m-1)*r)


def main():
    cases = [
        (2,1,2,'integers'), (2,1,3,'polynomial'),
        (2,2,2,'integers'), (2,2,3,'integers'),
        (2,3,2,'integers'), (2,3,3,'polynomial'),
        (3,1,3,'integers'), (3,2,2,'integers'),
        (3,2,2,'polynomial'),
        (4,1,2,'polynomial'), (4,2,2,'polynomial'),
        (2,4,2,'integers'),
    ]
    for q,m,r,model in cases:
        actual=direct_count(q,m,r,model)
        want=predicted(q,m,r)
        assert actual==want,(q,m,r,model,actual,want)
        print(f'PASS q={q} m={m} r={r} model={model} N={actual}')
    print(f'VERIFY_OK_HEISENBERG_CHAIN {len(cases)} cases')


if __name__ == '__main__':
    main()
