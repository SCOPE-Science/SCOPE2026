from fractions import Fraction as F
from math import isqrt

def ln_interval(x, terms=12):
    assert F(0) < x <= F(1)
    k = 0
    while x < 1:
        x *= 2
        k += 1
    if x == 2:
        x /= 2
        k -= 1
    z = (x - 1) / (x + 1)
    def calc(z):
        power = z
        s = F(0)
        for j in range(terms):
            s += 2*power/(2*j+1)
            power *= z*z
        rem = 2*power/((2*terms+1)*(1-z*z))
        return s,s+rem
    l2,u2=calc(F(1,3))
    l,u=calc(z)
    return l-k*u2, u-k*l2

def h_interval(x):
    assert F(0)<x<=F(1,2)
    l1,u1=ln_interval(x)
    l2,u2=ln_interval(1-x)
    return -x*u1-(1-x)*u2, -x*l1-(1-x)*l2

def H_from_sqrt(num,den):
    s=10**10
    j=isqrt(num*s*s)//den
    assert (j*den)**2 <= num*s*s < ((j+1)*den)**2
    a=(F(1)-(F(j+1,s)))/2
    b=(F(1)-F(j,s))/2
    assert 0<a<=b<=F(1,2)
    return h_interval(a)[0],h_interval(b)[1]

inputI=H_from_sqrt(241,17)
outputA=H_from_sqrt(285097,659)
cond=H_from_sqrt(2739985,1769)
q=F(1769,2636)
diff_lower=outputA[0]-q*cond[1]-inputI[1]
diff_upper=outputA[1]-q*cond[0]-inputI[0]
assert diff_lower > F(1,30), 'missing certified violation'
assert diff_upper < F(1,20), 'upper enclosure invalid'
print('VERIFY_OK lower_in_nats_approx=',float(diff_lower),'upper=',float(diff_upper),
      'certificate=exact_Fraction_atanh_remainders')

# Independent rational-matrix reconstruction of the candidate and dual-basis map.
def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def transp(a):
    return [[a[j][i] for j in range(2)] for i in range(2)]
def add(a,b):
    return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
def scale(x,a):
    return [[x*a[i][j] for j in range(2)] for i in range(2)]
def outer(a):
    return [[a[i]*a[j] for j in range(2)] for i in range(2)]
def tr(a):
    return a[0][0]+a[1][1]
def det(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def discriminant(a):
    return tr(a)**2-4*det(a)

v0=[F(1),F(0)]
v1=[F(4,5),F(3,5)]
u=[F(15,17),F(8,17)]
K0=[[F(1),F(-4,3)],[F(0),F(0)]]
K1=[[F(0),F(4,3)],[F(0),F(1)]]
# The dual vectors are (1,-4/3) and (0,5/3).
assert sum(v0[i]*v1[i] for i in range(2))==F(4,5)
assert [sum(K0[i][j]*v0[j] for j in range(2)) for i in range(2)]==v0
assert [sum(K1[i][j]*v0[j] for j in range(2)) for i in range(2)]==[F(0),F(0)]
assert [sum(K0[i][j]*v1[j] for j in range(2)) for i in range(2)]==[F(0),F(0)]
assert [sum(K1[i][j]*v1[j] for j in range(2)) for i in range(2)]==v1
sigma=add(mm(mm(K0,outer(u)),transp(K0)),mm(mm(K1,outer(u)),transp(K1)))
assert sigma==[[F(1193,2601),F(256,867)],[F(256,867),F(64,289)]]
assert tr(sigma)==F(1769,2601)
rhoA=add(scale(F(1,4),outer(v0)),scale(F(3,4),outer(u)))
assert rhoA==[[F(241,289),F(90,289)],[F(90,289),F(48,289)]]
Z=F(1,4)+F(3,4)*tr(sigma)
assert Z==F(659,867)
rhoAprime=scale(1/Z,add(scale(F(1,4),outer(v0)),scale(F(3,4),sigma)))
assert rhoAprime==[[F(515,659),F(192,659)],[F(192,659),F(144,659)]]
sigma1=scale(1/tr(sigma),sigma)
assert sigma1==[[F(1193,1769),F(768,1769)],[F(768,1769),F(576,1769)]]
assert discriminant(rhoA)==F(241,289)
assert discriminant(rhoAprime)==F(285097,659**2)
assert discriminant(sigma1)==F(2739985,1769**2)
kk=add(mm(transp(K0),K0),mm(transp(K1),K1))
assert kk==[[F(1),F(-4,3)],[F(-4,3),F(41,9)]]
assert tr(kk)==F(50,9) and det(kk)==F(25,9)
assert (F(5)*F(5,9)==det(kk)) # spectral norm^2 is five.
print('VERIFY_OK matrices=exact biorthogonality=passed success_trace=659/867 certificate=passed')
