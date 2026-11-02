"""Exact rational checks for finite two-type seasonal transmission matrices."""
from fractions import Fraction as F
from itertools import permutations
import random


def mul(A, B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0],
             A[0][0]*B[0][1]+A[0][1]*B[1][1]),
            (A[1][0]*B[0][0]+A[1][1]*B[1][0],
             A[1][0]*B[0][1]+A[1][1]*B[1][1]))


def prod(ms):
    A=((F(1),F(0)),(F(0),F(1)))
    for M in ms: A=mul(A,M)
    return A


def tr(A):return A[0][0]+A[1][1]

def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def matrix(s,b,c):return ((s,b),(c,s))


def check():
    rng=random.Random(20261028)
    checked=0
    for _ in range(240):
        s=F(rng.randint(1,8),10)
        b=[F(rng.randint(1,12),rng.randint(2,12)) for i in range(4)]
        c=[F(rng.randint(1,12),rng.randint(2,12)) for i in range(4)]
        E=[matrix(s,b[i],c[i]) for i in range(4)]
        base=2*s**4+s*s*sum(b[i]*c[j]+c[i]*b[j] for i in range(4) for j in range(i+1,4))
        for p in permutations(range(4)):
            trace=tr(prod([E[i] for i in p]))
            pair=b[p[0]]*b[p[2]]*c[p[1]]*c[p[3]]+c[p[0]]*c[p[2]]*b[p[1]]*b[p[3]]
            assert trace==base+pair
            checked+=1
        for k in (1,2,3):
            traces={tr(prod([E[i] for i in p])) for p in permutations(range(k))}
            determinants={det(prod([E[i] for i in p])) for p in permutations(range(k))}
            assert len(traces)==1 and len(determinants)==1
            checked+=2
    s=F(1,2)
    b=[F(23,128),F(23,48),F(69,64),F(23,12)]
    c=[F(23,128),F(23,96),F(23,64),F(23,48)]
    E=[matrix(s,b[i],c[i]) for i in range(4)]
    classes={}
    for p in permutations(range(4)):
        A=prod([E[i] for i in p]); classes.setdefault(tr(A),[]).append(p)
    expected=[(F(18587429,18874368),8), (F(37454699,37748736),8), (F(19147111,18874368),8)]
    assert sorted((value,len(ps)) for value,ps in classes.items())==expected
    common_det=F(160560615985,59373627899904)
    assert all(det(prod([E[i] for i in p]))==common_det for p in permutations(range(4)))
    assert [1-val+common_det for val,_ in expected]==[
        F(1063192662577,59373627899904),
        F(623040827953,59373627899904),
        -F(697414675919,59373627899904)]
    assert 0<common_det<1
    checked+=27
    print('EXACT_CHECKS_PASSED', checked)
    print('THREE_TRACE_CLASSES', expected)
    print('COMMON_DETERMINANT', common_det)

if __name__=='__main__':check()
