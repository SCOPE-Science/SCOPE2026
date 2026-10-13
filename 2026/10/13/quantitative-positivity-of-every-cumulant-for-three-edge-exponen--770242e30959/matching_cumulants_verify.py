"""Exact-arithmetic regression checks for three-edge exponential-matching cumulants.

This checker tests finite instances of an analytically proved theorem. It is not
an exhaustive check of all integer side lengths or all cumulant orders.
"""
from fractions import Fraction as F


checks = 0


def verify(test):
    global checks
    checks += 1
    assert test, f"Check {checks} failed"


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def factors(vals):
    result = [1]
    for v in vals:
        result = multiply(result, v)
    return result


def a_star(k):
    return F(2, 3) ** k - F(k + 3, 3 * 2**k)


def reciprocal_product_coeffs(params, upto):
    coeffs = [F(1)] + [F(0)] * upto
    for param in params:
        new = [F(0)] * (upto + 1)
        for j in range(upto + 1):
            for i in range(j + 1):
                new[j] += coeffs[i] * param ** (j - i)
        coeffs = new
    return coeffs


def h_coeffs(m, n, upto):
    alpha, beta, gamma = F(2, 3), F(m, 3*(m-1)), F(n, 3*(n-1))
    delta = F(1, 9*(m-1)*(n-1))
    reciprocal = reciprocal_product_coeffs((alpha,beta,gamma), upto - 2)
    return [F(0), F(0)] + [delta*v for v in reciprocal]


def logarithmic_defect_derivatives(h, upto):
    c = [F(0)] * (upto + 1)
    for p in range(2, upto + 1):
        c[p] = p*h[p] + sum((h[k]*c[p-k] for k in range(2,p-1)), F(0))
    return c


for m in range(3, 17):
    for n in range(3, 17):
        mn = m*n
        pj = factors([[mn,-2],[(m-1)*n,-1],[m*(n-1),-1]])
        p = [m*m*n*n*(m-1)*(n-1), -mn*(4*mn-3*m-3*n+2),
             5*mn-2*m-2*n-1, -2]
        verify(pj == [p[0],p[1],p[2]+1,p[3]])
        verify(F(1, 9*(m-1)*(n-1)) <= F(1,36))
        verify(F(m,3*(m-1)) <= F(1,2))
        verify(F(n,3*(n-1)) <= F(1,2))
        q = factors([[mn,-3],[(m-1)*n,-2],[m*(n-1),-2],
                     [(m-2)*n,-1],[(m-1)*(n-1),-1],[m*(n-2),-1]])
        exact_mean = sum((F(1,(m-i)*(n-j)) for i in range(3) 
                          for j in range(3-i)), F(0))
        verify(F(p[1],p[0]) - F(q[1],q[0]) == exact_mean)

# Independent cross multiplication against the displayed exact 3-by-3 MGF.
m=n=3
pj=factors([[9,-2],[6,-1],[6,-1]])
p=[pj[0],pj[1],pj[2]-1,pj[3]]
q=factors([[9,-3],[6,-2],[6,-2],[3,-1],[4,-1],[3,-1]])
reference_num=[972,-540,96,-6]
reference_den=factors([[4,-1]] + [[3,-1]]*5)
verify([36*v for v in multiply(p,reference_den)]==multiply(reference_num,q))

for k in range(0, 210):
    a=a_star(k)
    verify(a >= 0)
    if k >= 2:
        verify(k*a <= F(1,3))

for m in range(3, 13):
    for n in range(3, 13):
        upto=25
        r=F(m*n,3)
        h=h_coeffs(m,n,upto)
        c=logarithmic_defect_derivatives(h,upto)
        den=[F(m*n,3), F((m-1)*n,2), F(m*(n-1),2),
             F((m-2)*n), F((m-1)*(n-1)), F(m*(n-2))]
        num=[F(m*n,2), F((m-1)*n), F(m*(n-1))]
        for order in range(1,upto+1):
            logj_derivative=sum(((r/u)**order for u in den),F(0)) \
                -sum(((r/u)**order for u in num),F(0))
            verify(logj_derivative >= 1)
            verify(logj_derivative - c[order] >= F(1,2))
            if order >=2:
                verify(h[order] <= a_star(order))
                verify(c[order] <= F(1,2))

universal=[F(0),F(0)]+[a_star(k) for k in range(2,301)]
cu=logarithmic_defect_derivatives(universal,300)
for p in range(2,301):
    verify(cu[p] <= F(1,2))
verify(F(1,36)/((1-F(2,3))*(1-F(1,2))**2)==F(1,3))
verify(F(8)*(F(2,3)**8)<F(1,3))
print(f"PASS {checks} exact rational and polynomial checks")
