"""Exact-fraction checks for a period-three census in a piecewise-affine planar map.

Requires Python 3 standard library only. These are finite checks of the proof's
algebraic identities; universal statements are proved in the accompanying text.
"""
from fractions import Fraction as Q
from itertools import product

I = ((Q(1), Q(0)), (Q(0), Q(1)))

def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))

def mv(a, z):
    return tuple(sum(a[i][k] * z[k] for k in range(2)) for i in range(2))

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def mat(l, s, d, q):
    return (((l, Q(1)), (-d, Q(0))),
            ((-s, Q(1)), (q, Q(0))))

def symbolic(d, q, l, s):
    k = (d+l)*(s-1)-(1-d)*(1+q)
    b = d*q+d+l*q+l*s+s-1
    c = d*d+d*l-d+l*l+l+1
    h = q*q+q*s+q+s*s-s+1
    dl = d*d*q-d*l+d*s-l*l*s+l*q-1
    dr = d*q*q-d*s-l*q-l*s*s+q*s+1
    return k,b,c,h,dl,dr

def F(z, l, s, d, q):
    x, y = z
    return (l*x+y+1, -d*x) if x <= 0 else (-s*x+y+1, q*x)

n = 0
for di, qi, li, delta in product((1,2,3,5,7), (1,2,4,6,8), (1,3,5), (-1,0,1)):
    d, q = Q(di, 9), Q(qi, 9)
    l = 1+d+Q(li, 7)
    s0 = 1 + (1-d)*(1+q)/(d+l)
    s = s0+Q(delta, 4)
    if s <= 1-q:
        continue
    k,b,c,h,dl,dr = symbolic(d,q,l,s)
    assert b>0 and c>0 and h>0
    assert (k > 0) == (delta > 0)
    assert (k == 0) == (delta == 0)
    left, right = mat(l,s,d,q)
    for word, denom, xxx in [
        ('LLR',dl,(b,k,-c)), ('LRR',dr,(h,-k,-b))
    ]:
        matrices = {'L':left,'R':right}
        mon = I
        for w in word:
            mon = mm(matrices[w],mon)
        tr = mon[0][0]+mon[1][1]
        det = mon[0][0]*mon[1][1]-mon[0][1]*mon[1][0]
        if word=='LLR':
            assert tr == -d*l+d*s-l*l*s+l*q
            assert det == -d*d*q
        else:
            assert tr == d*s+l*q+l*s*s-q*s
            assert det == d*q*q
        assert denom == tr-det-1 if word=='LLR' else denom == 1-tr+det
        if denom == 0:
            continue
        x0,x1,x2 = (x/denom for x in xxx)
        z0=(x0,q*x2)
        z1=F(z0,l,s,d,q)
        z2=F(z1,l,s,d,q)
        z3=F(z2,l,s,d,q)
        if delta >= 0:
            assert z3 == z0, (word,delta,z3,z0)
            assert (z0[0],z1[0],z2[0]) == (x0,x1,x2)
            if delta > 0:
                assert tuple('L' if x<0 else 'R' for x in (x0,x1,x2)) == tuple(word)
            else:
                assert x1 == 0 and x0<0 and x2>0
            if delta>0 and word=='LLR':
                assert 1+tr+det < 0 and -1 < det < 0
            if delta>0 and word=='LRR':
                assert 1-tr+det < 0 and 0 < det < 1 and tr>0
        n+=1
print('PASS: {} exact candidate formulas / monodromies checked'.format(n))
