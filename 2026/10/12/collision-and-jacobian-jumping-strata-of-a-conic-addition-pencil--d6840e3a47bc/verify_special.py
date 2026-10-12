"""Exact ranks at the conic-contact parameter t=2*i, over Q(i).

Run `python verify_special.py 4` and `python verify_special.py 5` in
separate processes to avoid a computer-algebra cache accumulation.
Requires SymPy 1.14 or later and the sibling file verify.py.
"""
import sys
import sympy as s
from verify import jacobian_matrix, rank_over, t

def run(r):
    assert r in (4,5)
    A=jacobian_matrix(r).subs(t,2*s.I)
    rank=rank_over(A,s.QQ.algebraic_field(s.I))
    assert rank=={4:42,5:54}[r], (r,rank)
    print('VERIFY_SPECIAL_OK degree=%d rank=%d' % (r,rank))
if __name__=='__main__':
    assert len(sys.argv)==2
    run(int(sys.argv[1]))
