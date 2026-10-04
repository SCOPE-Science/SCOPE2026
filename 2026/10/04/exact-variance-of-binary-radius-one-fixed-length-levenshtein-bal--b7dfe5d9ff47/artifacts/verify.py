from itertools import product
from fractions import Fraction


def delete_insert_ball(x):
    n=len(x)
    out=set()
    for d in range(n):
        z=x[:d]+x[d+1:]
        for ins in range(n):
            for b in (0,1):
                out.add(z[:ins]+(b,)+z[ins:])
    return out


def claimed_variance(n):
    return (Fraction(n**3-9*n**2+48*n-120,4)
            + Fraction(n*n+3*n+17,2**(n-1))
            - Fraction(1,4**(n-1)))


def claimed_mean(n):
    return Fraction(n*(n-1),2)+3-Fraction(1,2**(n-1))


def direct_check(max_n=10):
    words=0
    for n in range(1,max_n+1):
        vals=[]
        for x in product((0,1), repeat=n):
            vals.append(len(delete_insert_ball(x)))
            words += 1
        N=len(vals)
        mu=Fraction(sum(vals),N)
        var=sum((Fraction(v)-mu)**2 for v in vals)/N
        assert mu==claimed_mean(n),(n,mu,claimed_mean(n))
        assert var==claimed_variance(n),(n,var,claimed_variance(n))
    return words


def recurrence_check(max_m=200):
    # Moments of trailing zero-run R and Q=sum over zero runs binom(length,2).
    ER=ER2=EQ=EQR=EQ2=Fraction(0)
    for m in range(0,max_m+1):
        if m>=0:
            q_formula=Fraction(m,2)-1+Fraction(1,2**m)
            qr_formula=Fraction(m,2)+2-Fraction(m*m+2*m+2,2**m)
            q2_formula=Fraction(m*m+13*m-76,4)+Fraction(2*m*m+10*m+19,2**m)
            assert EQ==q_formula,(m,EQ,q_formula)
            assert EQR==qr_formula,(m,EQR,qr_formula)
            assert EQ2==q2_formula,(m,EQ2,q2_formula)
        if m==max_m: break
        old_ER,old_ER2,old_EQ,old_EQR,old_EQ2=ER,ER2,EQ,EQR,EQ2
        ER=(old_ER+1)/2
        ER2=(old_ER2+2*old_ER+1)/2
        EQ=old_EQ+old_ER/2
        EQR=(old_EQR+old_EQ+old_ER2+old_ER)/2
        EQ2=old_EQ2+old_EQR+old_ER2/2

    # Independently sum the exact covariance and assemble the variance formula.
    for m in range(0,max_m+1):
        cov=Fraction(0)
        for ell in range(2,m+1):
            cov -= Fraction((m-ell+1)*ell,2**(ell+1))
        var_q=Fraction(17*m,4)-20+Fraction(2*m*m+9*m+21,2**m)-Fraction(1,4**m)
        var_b=Fraction(m**3,4)+var_q+2*m*cov
        assert var_b==claimed_variance(m+1),(m,var_b,claimed_variance(m+1))


if __name__=='__main__':
    words=direct_check(10)
    recurrence_check(200)
    print(f'VERIFY_OK direct_binary_words={words} n<=10 recurrence_m<=200')
