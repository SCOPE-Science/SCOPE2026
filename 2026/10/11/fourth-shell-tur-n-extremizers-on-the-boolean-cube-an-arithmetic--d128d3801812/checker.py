"""Exact finite checks for the Boolean fourth-shell Turan theorem.

Reproduces Krawtchouk eigenvalues, minimizer arithmetic, slice harmonic
multipliers, and an explicit nonradial feasible extremizer.
Uses only the Python standard library.
"""
from math import comb
from fractions import Fraction
from itertools import combinations


def kraw(d, r, k):
    return sum((-1)**j * comb(k,j) * comb(d-k,r-j)
               for j in range(r+1) if j<=k and r-j<=d-k)


def k4_closed(d,k):
    t=d-2*k
    v=t**4-(6*d-8)*t*t+3*d*(d-2)
    assert v%24==0
    return v//24


def eig(d,k,j):
    return (-2)**j * kraw(d-2*j,4-j,k-j)


def eig_closed(d,k,j):
    t=d-2*k
    return (k4_closed(d,k), -t*(t*t-3*d+8)//3,
            2*(t*t-d+4), -8*t,16)[j]


def minima(d):
    vals=[k4_closed(d,k) for k in range(d+1)]
    m=min(vals)
    return m,[k for k,v in enumerate(vals) if v==m]


def test_minima():
    tests=0
    resonances=[]
    for d in range(13,1001):
        m,ks=minima(d)
        assert m<0
        assert all(4<=k<=d-4 for k in ks)
        eigzeros={j for j in range(1,5) if all(eig_closed(d,k,j)==0 for k in ks)}
        expected=(len(ks)==2 and eig_closed(d,ks[0],1)==0)
        assert eigzeros==({1} if expected else set()),(d,ks,eigzeros)
        td=3*d-8
        square=int(td**.5)
        expected2=(square*square==td and square>=7 and square%3!=0)
        assert expected==expected2,(d,ks,expected,expected2)
        if expected:resonances.append((d,square,ks,m))
        tests+=1
    assert resonances[:5]==[(19,7,[6,13],-76),
                            (24,8,[8,16],-126),
                            (36,10,[13,23],-297),
                            (43,11,[16,27],-430),
                            (59,13,[23,36],-826)]
    print('DIMENSIONS',tests,'FIRST_RESONANCES',resonances[:6]);return tests


def test_harmonic_actions():
    tests=0
    for d in [10,11,12,13]:
        for j in range(5):
            pairs=[(2*t,2*t+1) for t in range(j)]
            for k in sorted(set([4,5,d-5,d-4])):
                if k<4 or k>d-4:continue
                scalar=eig_closed(d,k,j)
                assert scalar==eig(d,k,j),(d,k,j)
                for Y in combinations(range(d),k):
                    bits=sum(1<<i for i in Y)
                    rhs=scalar
                    for u,v in pairs:
                        rhs*=((bits>>u)&1)-((bits>>v)&1)
                    if rhs==0:
                        # algebraic anti-pair symmetry makes vanishing automatic
                        continue
                    lhs=0
                    for S in combinations(range(d),4):
                        sc=1
                        for u,v in pairs:
                            sc*=(int(u in S)-int(v in S))
                        if sc:
                            lhs+=((-1)**len(set(S)&set(Y)))*sc
                    assert lhs==rhs,(d,k,j,Y,lhs,rhs)
                    tests+=1
    print('HARMONIC_ACTIONS',tests);return tests


def test_feasible():
    d=19
    m,ks=minima(d)
    a=Fraction(-1,m)
    m1=max(abs(eig_closed(d,k,1)) for k in range(d+1))
    eps=Fraction(1, 4*(1+m1)*abs(m))
    w=[eps,-eps]+[Fraction(0)]*(d-2)
    assert sum(w)==0
    four=0
    for k in range(d+1):
        base=1+a*k4_closed(d,k)
        one=eig_closed(d,k,1)
        for b0 in [0,1]:
            for b1 in [0,1]:
                if b0+b1<=k and k-b0-b1<=d-2:
                    F=base+one*eps*(b0-b1)
                    assert F>=0,(k,b0,b1,F)
                    four+=1
        if k in ks:assert base==0 and one==0
    assert eps>0
    print('EXPLICIT_FEASIBLE_D19',str(eps),'FOURIER_CHECKS',four)
    return four


def main():
    t=0
    for d in range(8,101):
        for k in range(d+1):
            assert kraw(d,4,k)==k4_closed(d,k)
            t+=1
    print('KRAWTCHOUK',t)
    test_minima()
    test_harmonic_actions()
    test_feasible()
    print('CHECK_PASS')
if __name__=='__main__': main()
