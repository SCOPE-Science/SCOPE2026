#!/usr/bin/env python3
"""Independent exact finite-field verification of two-dimensional evolution idempotent counts.

This enumerates all invertible structure matrices and all algebra elements.
It also independently counts fixed-point configurations on the projective line.
No third-party packages are required.
"""
from collections import Counter
from fractions import Fraction


def finite_field(p, modulus=None):
    """Polynomial basis for F_(p^m), with monic irreducible modulus."""
    if modulus is None:
        m = 1
    else:
        m = len(modulus) - 1
        assert modulus[-1] == 1
    q = p ** m
    def decode(k):
        out = []
        for _ in range(m):
            out.append(k % p)
            k //= p
        return out
    def encode(a):
        return sum((v % p) * p**j for j,v in enumerate(a))
    elems = [decode(i) for i in range(q)]
    add = [[encode([x+y for x,y in zip(elems[a], elems[b])]) for b in range(q)] for a in range(q)]
    mul = []
    for a in range(q):
        row = []
        for b in range(q):
            c = [0]*(2*m-1)
            for i,x in enumerate(elems[a]):
                for j,y in enumerate(elems[b]):
                    c[i+j] = (c[i+j]+x*y)%p
            if modulus is not None:
                for d in range(2*m-2,m-1,-1):
                    t=c[d]
                    if t:
                        for j in range(m):
                            c[d-m+j] = (c[d-m+j]-t*modulus[j])%p
            row.append(encode(c[:m]))
        mul.append(row)
    neg = [encode([-x for x in elems[a]]) for a in range(q)]
    for a in range(1,q):
        assert any(mul[a][b] == 1 for b in range(1,q)), (p,modulus,a)
    return q, add, mul, neg


def expected(q):
    if q % 2 == 0:
        probs=(Fraction(1,3),Fraction(1,2),Fraction(0),Fraction(1,6))
    else:
        probs=(Fraction(1,3),Fraction(q*q+1,2*q*(q+1)),
               Fraction(q-1,q*(q+1)),Fraction(q*q-2*q+3,6*q*(q+1)))
    size=(q*q-1)*(q*q-q)
    return Counter({i:int(prob*size) for i,prob in enumerate(probs)})


def check(p,modulus=None):
    q, add, mul, neg = finite_field(p,modulus)
    sq = [mul[x][x] for x in range(q)]
    # Pair each nonzero coordinate vector with its coordinatewise square.
    points = [(x,y,sq[x],sq[y]) for x in range(q) for y in range(q) if x or y]
    counts=Counter()
    for a in range(q):
        for b in range(q):
            for c in range(q):
                for d in range(q):
                    if add[mul[a][d]][neg[mul[b][c]]] == 0:
                        continue
                    n=0
                    for x,y,x2,y2 in points:
                        if add[mul[a][x2]][mul[b][y2]]==x and add[mul[c][x2]][mul[d][y2]]==y:
                            n+=1
                    counts[n]+=1
    target=expected(q)
    assert counts==target,(q,counts,target)
    assert max(counts)<=3,(q,counts)
    # Independent projective-square fiber count: lines t in F_q plus infinity.
    image_fibers=Counter([sq[t] for t in range(q)]+['infinity'])
    weights=list(image_fibers.values())
    T2=sum(w*v for i,w in enumerate(weights) for j,v in enumerate(weights) if i!=j)
    T3=sum(u*v*w for i,u in enumerate(weights) for j,v in enumerate(weights) for k,w in enumerate(weights)
           if len({i,j,k})==3)
    G=q*(q*q-1)
    # Expected #nonzero idempotent factorial moments from algebra census.
    F2=Fraction(sum(n*(n-1)*ct for n,ct in counts.items()),sum(counts.values()))
    F3=Fraction(sum(n*(n-1)*(n-2)*ct for n,ct in counts.items()),sum(counts.values()))
    assert F2==Fraction(T2*(q-1),G), (q,F2,T2)
    assert F3==Fraction(T3,G), (q,F3,T3)
    print('q=%d, |GL_2|=%d, N=0,1,2,3 counts=%s, moments=%s,%s: PASS' %
          (q,sum(counts.values()),[counts[i] for i in range(4)],str(F2),str(F3)))


if __name__ == '__main__':
    for p,poly in [
        (2,None),(3,None),(5,None),(7,None),(11,None),
        (2,(1,1,1)),       # F4 = F2[t]/(t^2+t+1)
        (2,(1,1,0,1)),     # F8 = F2[t]/(t^3+t+1)
        (3,(1,0,1)),       # F9 = F3[t]/(t^2+1)
        (2,(1,1,0,0,1)),   # F16 = F2[t]/(t^4+t+1)
    ]:
        check(p,poly)
    print('VERIFY_OK')
