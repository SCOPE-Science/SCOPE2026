"""Independent finite checks for X^2=0 in 2x2 finite chain-ring matrices.

Run: python verify.py. This program tests explicit finite cases; proof for all
finite commutative chain rings is mathematical and not delegated to testing.
"""
from collections import Counter


def field(q):
    if q == 4:
        # F_4 = F_2[u]/(u^2+u+1), represented by two-bit polynomials.
        def add(a, b): return a ^ b
        def mul(a, b):
            v = 0
            for i in range(2):
                for j in range(2):
                    if (a >> i) & (b >> j) & 1:
                        v ^= 1 << (i+j)
            if v & 8: v ^= 0b1110  # u^3 = u*(u+1) = 1
            if v & 4: v ^= 0b111   # u^2 = u+1
            return v
        return add, mul
    assert q in (2, 3, 5)
    return lambda a,b: (a+b)%q, lambda a,b: (a*b)%q


def chain_ring(q, d, kind):
    size = q ** d
    if kind == 'integer':
        assert q in (2, 3, 5)
        add = [[(a+b)%size for b in range(size)] for a in range(size)]
        mul = [[(a*b)%size for b in range(size)] for a in range(size)]
        valuation = [next((i for i in range(d) if a % (q**(i+1)) != 0), d) for a in range(size)]
    else:
        assert kind == 'polynomial'
        fadd, fmul = field(q)
        coef = [tuple(a//(q**i)%q for i in range(d)) for a in range(size)]
        add = [[0]*size for _ in range(size)]
        mul = [[0]*size for _ in range(size)]
        for a in range(size):
            for b in range(size):
                ca,cb=coef[a],coef[b]
                add[a][b] = sum(fadd(ca[i],cb[i])*q**i for i in range(d))
                prod = [0]*d
                for i in range(d):
                    for j in range(d-i):
                        prod[i+j]=fadd(prod[i+j],fmul(ca[i],cb[j]))
                mul[a][b]=sum(prod[i]*q**i for i in range(d))
        valuation=[next((i for i,v in enumerate(row) if v),d) for row in coef]
    return add,mul,valuation


def verify(q,d,kind):
    add,mul,val=chain_ring(q,d,kind)
    size=q**d
    sq=[mul[a][a] for a in range(size)]
    count=Counter()
    for a in range(size):
        for b in range(size):
            for c in range(size):
                bc=mul[b][c]
                if add[sq[a]][bc]:continue
                for e in range(size):
                    if add[sq[e]][bc]:continue
                    tr=add[a][e]
                    if mul[b][tr] or mul[c][tr]:continue
                    count[min(val[a],val[b],val[c],val[e])]+=1
    shallow=(d+1)//2
    expected_each=(q*q-1)*q**(2*d-2)
    assert all(count[s]==expected_each for s in range(shallow)),(q,d,kind,count)
    deep=sum(k for s,k in count.items() if s>=shallow)
    assert deep==q**(4*(d//2)),(q,d,kind,count)
    total=sum(count.values())
    assert total==shallow*expected_each+deep
    print(f'{kind:10s} q={q} length={d} total={total} shells={dict(sorted(count.items()))}')


if __name__ == '__main__':
    for q,d in ((2,1),(3,1),(4,1),(5,1),(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(2,4)):
        verify(q,d,'polynomial')
    for q,d in ((2,1),(3,1),(5,1),(2,2),(3,2),(5,2),(2,3),(3,3),(2,4)):
        verify(q,d,'integer')
    print('VERIFY_OK: 20 finite configurations')
