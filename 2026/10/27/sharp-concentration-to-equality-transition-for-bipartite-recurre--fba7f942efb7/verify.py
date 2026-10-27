"""Exact finite-grid checks for the bipartite recurrent-booster allocation theorem.

The proof of the continuous optimization is analytic; these exact tests check
algebraic pieces and their asserted global boundary minimizers on rational grids.
Standard library only. Run: python verify.py
"""
from fractions import Fraction as Q

def susceptibility(x):
    x = Q(x)
    if x == 0:
        return Q(1)
    return 1 - x/2 if x <= 1 else 1/(2*x)

def optimal_product(B):
    B=Q(B)
    if B<=0:
        raise ValueError('positive total budget required')
    if B<2:
        return susceptibility(B)
    if B==2:
        return Q(1,4)
    return Q(1,B*B)

def verify():
    tests=0
    for den in [3,5,7,11,17,29]:
        for num in range(1, 7*den+1):
            B=Q(num,den)
            optimum=optimal_product(B)
            if B<2:
                assert susceptibility(B)*susceptibility(0)==optimum
            elif B==2:
                assert optimum==Q(1,4)
            else:
                assert susceptibility(B/2)**2==optimum
            tests+=1
            # A dense independent rational allocation grid, including all two-fold boundary points.
            for j in range(121):
                x=B*Q(j,120)
                y=B-x
                obj=susceptibility(x)*susceptibility(y)
                assert obj>=optimum,(B,x,obj,optimum)
                tests+=1
                if B==2:
                    assert obj==optimum
                    tests+=1
                elif B<2 and 0<j<120:
                    assert obj>optimum
                    tests+=1
                elif B>2 and j!=60:
                    assert obj>optimum
                    tests+=1
    # representative biological examples, one below and one above the transition
    assert optimal_product(1)==Q(1,2)
    assert susceptibility(Q(1,2))**2==Q(9,16)
    assert optimal_product(3)==Q(1,9)
    assert susceptibility(3)*susceptibility(0)==Q(1,6)
    tests+=4
    print('PASS:',tests,'exact rational checks')

if __name__=='__main__':
    verify()
