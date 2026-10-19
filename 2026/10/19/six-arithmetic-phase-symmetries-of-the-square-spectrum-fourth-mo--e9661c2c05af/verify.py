"""Reproduce finite arithmetic checks for an equality-phase theorem on square frequencies.

Run: python verify.py . Only the Python standard library is required.
The infinite-index recurrence and modular invariants are proved in RESULT.md;
this script is a finite independent regression check, not a substitute for proof.
"""
from collections import defaultdict
from fractions import Fraction
from cmath import exp
from math import pi


def feature(k):
    chi5 = 0 if k % 5 == 0 else (1 if k % 5 in (1, 4) else -1)
    return (1, k*k, int(k % 4 == 0), int(k % 4 == 2),
            int(k % 3 != 0), chi5)


def relations(n):
    pairs = defaultdict(list)
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            pairs[a*a + b*b].append((a,b))
    vectors = []
    for ps in pairs.values():
        a,b = ps[0]
        for c,d in ps[1:]:
            row = [0] * n
            row[a-1] += 1; row[b-1] += 1
            row[c-1] -= 1; row[d-1] -= 1
            vectors.append(row)
    return vectors, pairs


def rational_rank(rows):
    if not rows:
        return 0
    m = [[Fraction(x) for x in row] for row in rows]
    pivot_row = 0
    for col in range(len(m[0])):
        nz = next((i for i in range(pivot_row,len(m)) if m[i][col]),None)
        if nz is None:
            continue
        m[pivot_row],m[nz] = m[nz],m[pivot_row]
        den = m[pivot_row][col]
        m[pivot_row] = [x / den for x in m[pivot_row]]
        for i in range(pivot_row + 1,len(m)):
            mul = m[i][col]
            if mul:
                m[i] = [a - mul*b for a,b in zip(m[i],m[pivot_row])]
        pivot_row += 1
        if pivot_row == len(m):
            break
    return pivot_row


def det_bareiss(a):
    a = [list(row) for row in a]
    n = len(a)
    sign=1; prev=1
    for k in range(n-1):
        if not a[k][k]:
            j=next(j for j in range(k+1,n) if a[j][k]); a[k],a[j]=a[j],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                a[i][j]=(a[i][j]*p - a[i][k]*a[k][j])//prev
        for i in range(k+1,n):
            a[i][k]=0
        prev=p
    return sign*a[n-1][n-1]


def fourth_moment(n, weights, angles):
    cells=defaultdict(complex)
    for a in range(1,n+1):
        for b in range(1,n+1):
            cells[a*a+b*b] += weights[a-1]*weights[b-1]*exp(1j*(angles[a-1]+angles[b-1]))
    return sum(abs(z)**2 for z in cells.values())


assert det_bareiss([feature(k) for k in range(1,7)]) == 120
for n, expected in ((10,3),(11,5),(12,6),(18,12)):
    rows, _=relations(n)
    assert rational_rank(rows)==expected, (n,rational_rank(rows),expected)
    assert n-rational_rank(rows)==(7 if n==10 else 6), n
for n in (11,30,100):
    rows,pairs=relations(n)
    for row in rows:
        for col in range(6):
            assert sum(row[k-1]*feature(k)[col] for k in range(1,n+1)) == 0
    print(f"N={n}: {len(rows)} exact equal-sum relations; six invariants verified")
for k in range(12,2500):
    choices = [a for a in range(1,6) if a%5 == (3*k)%5]
    assert len(choices)==1
    a=choices[0]
    assert (3*k+4*a)%5==0 and (4*k-3*a)%5==0
    b=(3*k+4*a)//5; c=(4*k-3*a)//5
    assert 1<=a<k and 1<=b<k and 1<=c<k
    assert k*k+a*a==b*b+c*c
print('3-4-5 descent identities: k=12..2499 verified')
for n in (11,18):
    params = (0.12,-0.032,1.12,-1.23,0.55,0.71)
    weights = [(k+0.67)**(-.4) for k in range(1,n+1)]
    angles = [sum(p*x for p,x in zip(params,feature(k))) for k in range(1,n+1)]
    optimum = fourth_moment(n,weights,[0.0]*n)
    coherent = fourth_moment(n,weights,angles)
    assert abs(coherent-optimum) < 1e-7 * optimum
    changed=angles[:]
    changed[n-1] += 0.19
    assert fourth_moment(n,weights,changed) < optimum - 1e-7
    print(f'N={n}: coherent equality and strict phase perturbation verified')
print('PASS: integer determinants, ranks, modular invariants, descent, fourth moments')
