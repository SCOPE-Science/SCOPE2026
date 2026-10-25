#!/usr/bin/env python3
"""Optional independent symbolic smoothness check; requires SymPy.
Run from this directory: python crosscheck_sympy.py
"""
from sympy import Poly, groebner, symbols
from gf2_ideal import smooth
x,y=symbols('x y')
chart_terms=[[(i if not u else 2-i,j if not v else 3-j) for i in range(3) for j in range(4)] for u in (0,1) for v in (0,1)]
def sympy_smooth(mask):
    for chart in chart_terms:
        F=Poly.from_dict({exp:1 for k,exp in enumerate(chart) if (mask>>k)&1},(x,y),modulus=2)
        if F.is_zero:return False
        G=groebner([F,F.diff(x),F.diff(y)],x,y,modulus=2)
        if not (len(G.polys)==1 and G.polys[0].is_one): return False
    return True
if __name__=='__main__':
    matches=sum(smooth(i)==sympy_smooth(i) for i in range(1,4096))
    assert matches==4095
    print('Independent SymPy and GF(2) Buchberger smoothness flags agree:',matches)
