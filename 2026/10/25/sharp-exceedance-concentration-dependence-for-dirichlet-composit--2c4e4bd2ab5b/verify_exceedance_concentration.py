"""Independent finite exact-rational checks for Dirichlet exceedance-concentration identities.

No numerical quadrature is used: all beta-tail moments in these checks
are expanded into rational polynomial integrals. The analytic theorem for
all real Dirichlet parameters and power exponents is proved in RESULT.md.
"""
from fractions import Fraction as F
from math import comb, factorial


def rising(z, q):
    y = F(1)
    for h in range(q):
        y *= z+h
    return y


def beta_int(u, v):
    return F(factorial(u-1)*factorial(v-1), factorial(u+v-1))


def beta_tail_raw(u, v, t):
    return sum((F((-1)**j * comb(v-1, j), u+j) *
                (1 - t**(u+j)) for j in range(v)), F(0))


def exact_cov(alpha, i, q, t):
    A = sum(alpha)
    a = alpha[i]
    b = A-a
    c = sum(rising(x,q) for j,x in enumerate(alpha) if j != i) / rising(b,q)
    eq = sum(rising(x,q) for x in alpha) / rising(A,q)
    norm = beta_int(a,b)
    probability = beta_tail_raw(a,b,t) / norm
    joint = (beta_tail_raw(a+q,b,t)+c*beta_tail_raw(a,b+q,t))/norm
    return joint - eq * probability


def predicted_cov2(alpha, i, t):
    A = sum(alpha)
    a = alpha[i]
    b = A-a
    c = sum(F(x*(x+1)) for j,x in enumerate(alpha) if j != i) / F(b*(b+1))
    theta = (c*(a+2*b+1) - (a+1)) / (A*(1+c))
    f = t**(a-1)*(1-t)**(b-1) / beta_int(a,b)
    return t*(1-t)*f*(1+c)/(A+1)*(t-theta), theta


def main():
    examples = ((1,1), (1,1,1), (7,1,1), (8,1,1),
                (10,1,1), (2,1,1), (2,3,1,4), (3,2,2,5), (1,1,1,1,1))
    tvals = (F(1,17),F(1,5),F(1,3),F(1,2),F(4,5),F(16,17))
    checks = 0
    for al in examples:
        for i in range(len(al)):
            for t in tvals:
                actual = exact_cov(al,i,2,t)
                pred, theta = predicted_cov2(al,i,t)
                assert actual == pred, (al,i,t,actual,pred)
                if theta <= 0:
                    assert actual > 0
                elif t < theta:
                    assert actual < 0
                elif t > theta:
                    assert actual > 0
                else:
                    assert actual == 0
                checks += 1
    assert predicted_cov2((7,1,1),0,F(1,2))[1] == 0
    assert predicted_cov2((8,1,1),0,F(1,2))[1] < 0
    assert predicted_cov2((1,1,1),0,F(1,2))[1] == F(2,5)
    for m in range(2,9):
        for a in range(1,5):
            al=(a,)*m
            theta=predicted_cov2(al,0,F(1,2))[1]
            assert theta == F(a+1,m*a+2)
            for t in tvals:
                exact = sum((exact_cov(al,i,2,t) for i in range(m)),F(0))
                expected = m*predicted_cov2(al,0,t)[0]
                assert exact == expected
                checks += 1
    # Higher Renyi powers: direct integration and analytic endpoint classification.
    for al in examples:
        A=sum(al)
        for i,a in enumerate(al):
            b=A-a
            for q in (3,4,5):
                c=sum(rising(x,q) for j,x in enumerate(al) if j!=i)/rising(b,q)
                eq=sum(rising(x,q) for x in al)/rising(A,q)
                for t in tvals:
                    actual=exact_cov(al,i,q,t)
                    if c<=eq:
                        assert actual>0
                    checks += 1
    print(f'PASS: {checks} exact rational beta-tail/covariance comparisons')
    print('PASS: symmetric q=2 transition and asymmetric n=3 boundary cases')
    print('PASS: sample higher-power q=3,4,5 positive-regime checks')

if __name__=='__main__':
    main()
