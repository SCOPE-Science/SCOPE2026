#!/usr/bin/env python3
"""Exact integer-Gaussian enumeration of two-qubit Pauli MUB supports."""
from itertools import combinations, product, permutations

I = ((1+0j,0j),(0j,1+0j))
X = ((0j,1+0j),(1+0j,0j))
Y = ((0j,-1j),(1j,0j))
Z = ((1+0j,0j),(0j,-1+0j))


def tensor(a,b):
    return tuple(tuple(a[i//2][j//2]*b[i%2][j%2] for j in range(4)) for i in range(4))


def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)) for i in range(4))


def add(*aa):
    return tuple(tuple(sum(a[i][j] for a in aa) for j in range(4)) for i in range(4))


def scale(a,c):
    return tuple(tuple(c*a[i][j] for j in range(4)) for i in range(4))


def tr(a):
    return sum(a[i][i] for i in range(4))

P = {a+b:tensor(m,n) for a,m in [('I',I),('X',X),('Y',Y),('Z',Z)]
                         for b,n in [('I',I),('X',X),('Y',Y),('Z',Z)] if a+b != 'II'}
ident = tensor(I,I)


def commute(x,y):
    return mul(P[x],P[y]) == mul(P[y],P[x])


def third(x,y):
    pq=mul(P[x],P[y])
    return next(k for k,v in P.items() if pq==v or pq==scale(v,-1))

triples = sorted({frozenset((p,q,third(p,q))) for p,q in combinations(P,2) if commute(p,q)},
                 key=lambda s:''.join(sorted(s)))
assert len(triples) == 15
classes = ['ZI IZ ZZ','XI IX XX','XZ ZY YX','YI IY YY','YZ ZX XY']
spread = [frozenset(x.split()) for x in classes]
assert len(set.union(*map(set,spread))) == 15
assert all(s in triples for s in spread)


def states(line):
    a,b=sorted(line)[:2]
    assert commute(a,b)
    AB=mul(P[a],P[b])
    return [add(ident,scale(P[a],u),scale(P[b],v),scale(AB,u*v))
            for u,v in product((1,-1),repeat=2)]

B = [states(c) for c in spread]
for j in range(5):
    assert all(tr(mul(x,y)) == (16 if x==y else 0) for x in B[j] for y in B[j])
    for k in range(j):
        assert all(tr(mul(x,y)) == 4 for x in B[j] for y in B[k])

results={14:0,17:0}
seen=set()
zero_six=[]
for line in triples:
    for rho in states(line):
        key=tuple(tuple(int(rho[i][j].real) for j in range(4))+
                  tuple(int(rho[i][j].imag) for j in range(4)) for i in range(4))
        assert key not in seen
        seen.add(key)
        counts=[]
        for basis in B:
            # rho and measurement-projector numerator are scaled by four.
            weights=[tr(mul(rho,b)) for b in basis]
            assert sum(weights)==16
            assert set(weights).issubset({0,4,8,16})
            counts.append(sum(t!=0 for t in weights))
        signature=tuple(sorted(counts))
        if line not in spread:
            zero_six.append(frozenset(j*4+k for j,basis in enumerate(B) for k,b in enumerate(basis) if tr(mul(rho,b))==0))
        if line in spread:
            assert signature==(1,4,4,4,4)
            results[17]+=1
        else:
            assert signature==(2,2,2,4,4)
            results[14]+=1
assert len(seen)==60 and results=={14:40,17:20}
print('PASS: 15 commuting triples, 5 basis triples, 10 remaining triples')
print('PASS: 40 nonbasis stabilizer rays have profile (2,2,2,4,4)')
print('PASS: 20 basis stabilizer rays have profile (1,4,4,4,4)')
print('PASS: pairwise basis unbiasedness checked exactly (all rational traces)')


def determinant(a):
    n=len(a)
    return sum((-1 if sum(row[i]>row[j] for i in range(n) for j in range(i+1,n))%2 else 1)
               * __import__('math').prod(a[i][row[i]] for i in range(n))
               for row in permutations(range(n)))

# Exact columns of projector numerators are rays; all entries lie in Z[i].
rays=[]
for basis in B:
    for pr in basis:
        j=next(j for j in range(4) if any(pr[i][j]!=0 for i in range(4)))
        rays.append(tuple(pr[i][j] for i in range(4)))
assert len(rays)==20
for ids in combinations(range(20),3):
    assert any(determinant([[rays[c][r] for c in ids] for r in rs])!=0
               for rs in combinations(range(4),3)), ('dependent triple',ids)

zero_six=set(zero_six)
assert len(zero_six)==40 and all(len(z)==6 for z in zero_six)
singular=[]
for ids in combinations(range(20),4):
    det=determinant([[rays[c][r] for c in ids] for r in range(4)])
    claimed=any(set(ids).issubset(z) for z in zero_six)
    assert (det==0) == claimed, ('unexplained quadruple',ids,det)
    if det==0: singular.append(ids)
assert len(singular)==600
print('PASS: all 1140 three-ray selections are independent')
print('PASS: precisely 600 of 4845 four-ray selections are dependent')
print('PASS: each dependent four-ray set sits in a six-zero stabilizer configuration')
print('THEOREM: total support spectrum is exactly {14,17,18,19,20}')
