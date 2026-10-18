"""Exact geometric smoothness census for bidegree-(2,3) binary curves.
Usage: python verify_geometry.py smooth_masks.txt
Requires sympy. Four standard affine charts cover P1 x P1.
"""
import sys
from pathlib import Path
import sympy as sp
x,y=sp.symbols('x y')

def geometrically_smooth(mask):
    for ax in (0,1):
        for ay in (0,1):
            f=sum((x**(i if ax==0 else 2-i)) * (y**(j if ay==0 else 3-j))
                  for i in range(3) for j in range(4) if mask & (1<<(4*i+j)))
            f=sp.Poly(f,x,y,modulus=2).as_expr()
            gb=sp.groebner((f,sp.diff(f,x),sp.diff(f,y)),x,y,modulus=2)
            if not (len(gb.polys)==1 and gb.polys[0].as_expr()==1):
                return False
    return True

if __name__=='__main__':
    result=[a for a in range(1,4096) if geometrically_smooth(a)]
    assert len(result)==1116, len(result)
    assert {386,1566,2597,1948,2983,3131,3513} <= set(result)
    Path(sys.argv[1] if len(sys.argv)>1 else 'smooth_masks.txt').write_text(''.join(f'{i}\n' for i in result),encoding='ascii')
    print(f'geometric_smoothness: 4095 checked, 1116 smooth; example 7 smooth: PASS')
