#!/usr/bin/env python3
"""Exact rational checks for fourth-order Gauss diffusion on weighted stars.

Requires SymPy 1.12 or newer. These finite checks corroborate the separate
analytical proof; they are not a substitute for its all-weight quantifiers.
"""
import sympy as S


def star_laplacian(weights):
    n = len(weights) + 1
    L = S.zeros(n)
    for i, w in enumerate(weights, 1):
        L[0, 0] += w
        L[0, i] = L[i, 0] = -w
        L[i, i] = w
    return L


def pade_step(L, h):
    I = S.eye(L.rows)
    L2 = L * L
    numerator = 12 * I - 6 * h * L + h * h * L2
    denominator = 12 * I + 6 * h * L + h * h * L2
    return numerator * denominator.inv()


def phi(weights, h, i):
    wi = weights[i]
    return 1 + sum((h*h*w*(w-wi))/(h*h*w*w+6*h*w+12) for w in weights)


def center_formula(weights, h, i):
    s = (3+S.I*S.sqrt(3))/h
    om = 1 + sum(w/(s+w) for w in weights)
    f = weights[i]/((s+weights[i])*om)
    # |f|^2= f*conjugate(f), no floating-point evaluation.
    return S.simplify(12*f*S.conjugate(f)*phi(weights,h,i)/(h*weights[i]))


def leaf_formula(weights, h, i, j):
    s = (3+S.I*S.sqrt(3))/h
    om = 1 + sum(w/(s+w) for w in weights)
    f = weights[i]*weights[j]/((s+weights[i])*(s+weights[j])*om)
    return S.simplify(-12*S.im(S.expand_complex(f))/(h*(S.sqrt(3)/h)))


def test():
    z=S.symbols('z',positive=True)
    assert S.factor((z*z-6*z+12)/(z*z+6*z+12) - (1-12*z/(z*z+6*z+12))) == 0
    h=S.symbols('h',positive=True)
    w=S.symbols('w',positive=True)
    d=w*w*h*h+6*h*w+12
    assert S.factor(S.diff(h*h/d,h)-(6*h*h*w+24*h)/d**2)==0
    # Exact value of the four-vertex boundary with weights 2,2,4.
    ws=[S.Rational(2),S.Rational(2),S.Rational(4)]
    assert S.simplify(phi(ws,h,2) + (h*h-3*h-3)/(h*h+3*h+3)) == 0
    H=(3+S.sqrt(21))/2
    assert S.simplify(phi(ws,H,2))==0
    assert 4*sum(1/x for x in ws)==5
    # Equality/no-finite-failure four-vertex boundary with weights 2,2,3.
    we=[S.Rational(2),S.Rational(2),S.Rational(3)]
    assert max(we)*sum(1/x for x in we) == len(we)+1
    matrix_count=0
    entry_count=0
    sign_count=0
    examples=[
        [1,1],[1,2],[1,3],[2,2],[1,1,1],[2,2,3],[2,2,4],
        [1,2,4],[1,1,1,1],[1,1,1,3],[1,2,3,4],
        [1,1,1,1,1],[2,3,3,4,5],[1,2,3,4,5,6]
    ]
    # Additional generated cases are reproducible; all weights strictly positive.
    for m in range(2,7):
        for k in range(1,4):
            examples.append([1+(k*i+i*i)%5 for i in range(m)])
    for values in examples:
        weights=list(map(S.Rational,values))
        n=len(weights)+1
        L=star_laplacian(weights)
        assert L == L.T and all(sum(L[i,j] for j in range(n))==0 for i in range(n))
        for hh in (S.Rational(1,2),S.Rational(3),S.Rational(9)):
            M=pade_step(L,hh)
            matrix_count+=1
            assert M == M.T
            assert all(sum(M[i,j] for j in range(n))==1 for i in range(n))
            for i in range(len(weights)):
                if values in ([2,2,4],[2,2,3]) and hh==3:
                    c=center_formula(weights,hh,i)
                    assert S.simplify(M[0,i+1]-c) == 0
                assert (M[0,i+1]>=0)==(phi(weights,hh,i)>=0)
                sign_count+=1
                entry_count+=1
            for i in range(len(weights)):
                for j in range(i+1,len(weights)):
                    if values in ([2,2,4],[2,2,3]) and hh==3:
                        c=leaf_formula(weights,hh,i,j)
                        assert S.simplify(M[i+1,j+1]-c)==0
                    if min(phi(weights,hh,k) for k in range(len(weights)))>=0:
                        assert M[i+1,j+1]>0
                    entry_count+=1
            assert all(M[i,i]>0 for i in range(n))
        # Under the classification, every noncritical center entry has
        # a larger sign factor; check this entirely with exact arithmetic.
        wmax=max(weights)
        for hh in (S.Rational(1,3),S.Rational(10),S.Rational(1000)):
            vals=[phi(weights,hh,i) for i in range(len(weights))]
            assert min(vals)==min(vals[i] for i,v in enumerate(weights) if v==wmax)
    print('VERIFY_OK: scalar Padé/derivative identities; exact four-site crossover;',
          matrix_count,'exact weighted-star matrices;',entry_count,
          'exact off-diagonal entries evaluated;',sign_count,'exact hub-entry sign tests')


if __name__ == '__main__':
    test()
