from fractions import Fraction
from math import sqrt


def sum_i_2i_minus1(n):
    return sum(Fraction(i*(2*i-1), 1) for i in range(1, n))


def conditional_mean(n, m):
    m = Fraction(m)
    # Conditional on M=m, the lower n-1 order statistics are m times
    # the order statistics of n-1 iid uniforms; E[U_(i)|M=m]=i*m/n.
    sq = m*m * Fraction(n+2, 3)
    weighted = m * (sum_i_2i_minus1(n) / n + (2*n-1))
    const = Fraction(n, 3)
    return sq - weighted/Fraction(n, 1) + const


def conditional_closed(n, m):
    m = Fraction(m)
    return (Fraction(n+2, 3)*m*m
            - Fraction((n+1)*(4*n-1), 6*n)*m
            + Fraction(n, 3))


def moment_M(n, k):
    return Fraction(n, n+k)


def covariance(n):
    A = Fraction(n+2, 3)
    B = Fraction((n+1)*(4*n-1), 6*n)
    C = Fraction(n, 3)
    emw = A*moment_M(n,3) - B*moment_M(n,2) + C*moment_M(n,1)
    em = moment_M(n,1)
    ew = Fraction(1,6)
    return emw-em*ew


def covariance_closed(n):
    return -Fraction(n-1, 2*(n+1)*(n+2)*(n+3))


def poly_mul(p, q):
    out={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            out[(i+k,j+l)] = out.get((i+k,j+l), Fraction(0)) + a*b
    return out


def triangle_integral(p):
    # 0 <= u <= v <= 1
    s=Fraction(0)
    for (i,j),a in p.items():
        s += a * Fraction(1, (i+1)*(i+j+2))
    return s


def unit_integral(p):
    return sum(a*Fraction(1,i+1) for i,a in p.items())

# d(u)=h(u,u)=1/3+u^2-u.
d={0:Fraction(1,3),1:Fraction(-1),2:Fraction(1)}
d2={}
for i,a in d.items():
    for j,b in d.items():
        d2[i+j]=d2.get(i+j,Fraction(0))+a*b
Ed=unit_integral(d)
Vd=unit_integral(d2)-Ed*Ed
assert Ed==Fraction(1,6)
assert Vd==Fraction(1,180)

# On u<=v, h(u,v)=1/3+u^2/2+v^2/2-v.
h={(0,0):Fraction(1,3),(2,0):Fraction(1,2),(0,2):Fraction(1,2),(0,1):Fraction(-1)}
Eh2=2*triangle_integral(poly_mul(h,h))
assert Eh2==Fraction(1,90)

checks=0
for n in range(2,81):
    for k in range(1,20):
        m=Fraction(k,20)
        assert conditional_mean(n,m)==conditional_closed(n,m)
        checks+=1
    assert covariance(n)==covariance_closed(n)
    varw=Fraction(4*n-3,180*n)
    varw_kernel=(Fraction(n,1)*Vd + Fraction(2*n*(n-1),1)*Eh2)/Fraction(n*n,1)
    assert varw==varw_kernel
    varm=Fraction(n,(n+1)**2*(n+2))
    corr=float(covariance_closed(n))/sqrt(float(varm*varw))
    corr_closed=-3*sqrt(5)*(n-1)/((n+3)*sqrt((n+2)*(4*n-3)))
    assert abs(corr-corr_closed)<1e-14
    mstar=Fraction((n+1)*(4*n-1),4*n*(n+2))
    assert 0<mstar<1

# Direct exact check of E[W]=1/6 from the conditional regression.
for n in range(2,201):
    A=Fraction(n+2,3)
    B=Fraction((n+1)*(4*n-1),6*n)
    C=Fraction(n,3)
    ew=A*moment_M(n,2)-B*moment_M(n,1)+C
    assert ew==Fraction(1,6)

print(f'VERIFY_OK conditional={checks} covariance=79 kernel=79 mean=199')
