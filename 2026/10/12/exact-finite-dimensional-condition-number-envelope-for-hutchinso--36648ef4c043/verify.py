from fractions import Fraction
from math import floor, ceil

def V(n,k,r):
    return 2*(Fraction(n,1)+r*(k*k-1))/(Fraction(n,1)+r*(k-1))**2 - Fraction(2,n)

def test_grid():
    ks=[Fraction(6,5),Fraction(3,2),Fraction(2,1),Fraction(5,2),Fraction(3,1),Fraction(5,1),Fraction(10,1),Fraction(25,2)]
    for n in range(2,31):
        for k in ks:
            vals=[V(n,k,r) for r in range(n+1)]
            brute=max(vals)
            x=Fraction(n,1)/(k+1)
            lo=x.numerator//x.denominator
            hi=lo if x.denominator==1 else lo+1
            cand=max(V(n,k,max(0,min(n,lo))),V(n,k,max(0,min(n,hi))))
            assert brute==cand,(n,k,brute,cand)
            cont=(k-1)**2/Fraction(2*k*n,1)
            assert brute<=cont,(n,k,brute,cont)
            assert brute<=2*Fraction(n-1,n)

def witness():
    # A=I+J/2, n=4.  diag=3/2, offdiag=1/2, spectrum {3,1,1,1}.
    n=4
    trace=Fraction(6,1)
    frob2=4*Fraction(9,4)+12*Fraction(1,4)
    diag2=4*Fraction(9,4)
    var=2*(frob2-diag2)
    rel=var/(trace*trace)
    assert frob2==12
    assert var==6
    assert rel==Fraction(1,6)
    assert rel==V(4,Fraction(3,1),1)
    assert V(4,Fraction(3,1),1)==max(V(4,Fraction(3,1),r) for r in range(5))

def derivative_factor():
    # Symbolic numerator after differentiation of Q/S^2 in r:
    # -(k-1)^2*((k+1)r-n).  Test its sign pattern exactly on a grid.
    for n in range(2,20):
        for k in [Fraction(3,2),Fraction(2),Fraction(3),Fraction(7)]:
            for r in range(n+1):
                num=-(k-1)**2*((k+1)*r-n)
                if Fraction(r,1)<Fraction(n,1)/(k+1): assert num>0
                elif Fraction(r,1)>Fraction(n,1)/(k+1): assert num<0
                else: assert num==0

if __name__=='__main__':
    test_grid(); witness(); derivative_factor(); print('VERIFY_OK')
