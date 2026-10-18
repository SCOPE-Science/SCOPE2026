#!/usr/bin/env python3
"""Four-chart Groebner check of every binary bidegree-(2,2) equation.
Requires sympy; contains no imports from the independent finite-field checker.
"""
from collections import Counter
from sympy import Poly, groebner, symbols
x,y=symbols('x y')
MON=[(i,j) for i in range(3) for j in range(3)]

def chart_poly(m,ax,ay):
    return Poly(sum((x**(i if ax==0 else 2-i))*(y**(j if ay==0 else 2-j))
                    for k,(i,j) in enumerate(MON) if (m>>k)&1), x,y,modulus=2)

def smooth(m):
    for a in (0,1):
        for b in (0,1):
            f=chart_poly(m,a,b)
            G=groebner([f.as_expr(),f.diff(x).as_expr(),f.diff(y).as_expr()],x,y,modulus=2)
            if len(G.polys)!=1 or G.polys[0].total_degree()!=0 or G.polys[0].LC()%2==0:
                return False
    return True

def main():
    sm={m for m in range(1,512) if smooth(m)}
    print('GROEBNER_SMOOTH_COUNT',len(sm))
    print('SMOOTH_MASKS',','.join(map(str,sorted(sm))))
    assert len(sm)==144
    print('GROEBNER_OK')
if __name__=='__main__':main()
