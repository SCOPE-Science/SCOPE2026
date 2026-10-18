"""Reproduce the exact algebraic multiplier identities and sample the stability regions.
Uses only the Python standard library; statements for all parameters are proved in RESULT.md.
"""
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 65
D = Decimal
ONE = D(1)
TWO = D(2)
FOUR = D(4)


def mul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in (0, 1)) for j in (0, 1)] for i in (0, 1)]


def cosh(x):
    return (x.exp() + (-x).exp()) / TWO


def acosh(x):
    if x < ONE:
        raise ValueError('outside real acosh domain')
    return (x + (x*x - ONE).sqrt()).ln()


def exponent_from_product(a,b,c,q,T):
    B = b*q*T
    C = c*(ONE-q)*T
    first = [[ONE,B],[D(0),ONE]]
    second = [[ONE,D(0)],[-C,ONE]]
    Q = mul(second,first)
    tr = Q[0][0]+Q[1][1]
    det = Q[0][0]*Q[1][1]-Q[0][1]*Q[1][0]
    assert abs(det-ONE)<D('1e-45')
    dis = tr*tr-FOUR*det
    if dis <= 0:
        rho = ONE
    else:
        rad = dis.sqrt()
        rho=max(abs((tr+rad)/TWO),abs((tr-rad)/TWO))
    return rho.ln()/T - a, Q


def exponent_formula(a,b,c,q,T):
    z=(b*c*q*(ONE-q)).sqrt()*T
    return -a+(TWO*acosh(z/TWO)/T if z>TWO else D(0))


def instability_test(a,b,c,q,T):
    return b*c*q*(ONE-q)*T*T>FOUR*cosh(a*T/TWO)**2


def bisect(f,lo,hi,iterations=240):
    vlo=f(lo)
    vhi=f(hi)
    assert vlo*vhi<0,(vlo,vhi)
    for _ in range(iterations):
        mid=(lo+hi)/TWO
        vm=f(mid)
        if vm==0:
            return mid
        if vm*vlo<0:hi,vhi=mid,vm
        else:lo,vlo=mid,vm
    return (lo+hi)/TWO


def main():
    count=0
    for p in (1,2,3,5,7):
        for r in (1,3,4,6,10):
            B=Fraction(p,7)
            C=Fraction(r,5)
            first=[[Fraction(1),B],[Fraction(0),Fraction(1)]]
            second=[[Fraction(1),Fraction(0)],[-C,Fraction(1)]]
            Q=mul(second,first)
            assert Q==[[Fraction(1),B],[-C,Fraction(1)-B*C]]
            assert Q[0][0]+Q[1][1]==2-B*C
            assert Q[0][0]*Q[1][1]-Q[0][1]*Q[1][0]==1
            count+=1
    # Independent eigenvalue discriminant versus closed-form hyperbolic expression
    sample_count=0
    for ia in (1,2,3,5):
      for ib in (1,2,4,9):
       for ic in (1,3,5,11):
        for iq in (1,2,3,5,7):
         for it in (1,2,5,11,23):
          a=D(ia)/D(4)
          b=D(ib)
          c=D(ic)
          q=D(iq)/D(10)
          T=D(it)/D(5)
          v,_=exponent_from_product(a,b,c,q,T)
          w=exponent_formula(a,b,c,q,T)
          assert abs(v-w)<D('1e-42'),(a,b,c,q,T,v,w)
          flag=instability_test(a,b,c,q,T)
          assert (w>0)==flag,(a,b,c,q,T,w,flag)
          sample_count+=1
    wstar=bisect(lambda w:w*(w.exp()-(-w).exp())/(w.exp()+(-w).exp())-ONE,D('1.1'),D('1.3'))
    H=wstar/cosh(wstar)
    qcrit=H/TWO
    assert D('.331')<qcrit<D('.332')
    # A concrete coexistence equilibrium is stable for short and long seasons,
    # but unstable at intermediate season durations.
    a,b,c,q=D(1),D(4),D(4),D('0.5')
    indicators=[]
    for T in (D('0.4'),D(2),D(8)):
        val,_=exponent_from_product(a,b,c,q,T)
        indicators.append((T,val))
    assert indicators[0][1]<0 and indicators[1][1]>0 and indicators[2][1]<0
    f=lambda T:(T-cosh(T/TWO))
    Tlo=bisect(f,D(1),D(2))
    Thi=bisect(f,D(4),D(5))
    assert D('1.17')<Tlo<D('1.19')
    assert D('4.25')<Thi<D('4.26')
    # At fixed period T=2, the duration share must fall inside one symmetric interval.
    T=D(2)
    edge=(ONE-(D(16)*cosh(a*T/TWO)**2/(b*c*T*T))).sqrt()
    qlo=(ONE-edge)/TWO
    qhi=(ONE+edge)/TWO
    assert D('.181')<qlo<D('.183') and D('.817')<qhi<D('.819')
    for qi in (D('.1'),D('.18'),D('.3'),D('.5'),D('.75'),D('.82'),D('.9')):
        assert instability_test(a,b,c,qi,T)==(qlo<qi<qhi)
    print('rational_shear_identities:',count,'cases PASS')
    print('independent_eigenvalue_checks:',sample_count,'cases PASS')
    print('universal_wstar:',wstar)
    print('critical_a_over_sqrt_bc_at_balanced_duty:',qcrit)
    print('sample_period_crossings:',Tlo,Thi)
    print('fixed_period_duty_crossings:',qlo,qhi)
    print('sample_exponents:',indicators)
    print('checks: PASS')

if __name__ == '__main__':
    main()
