#!/usr/bin/env python3
"""Exact characteristic-number and Hodge-genus checks for a Grassmannian sixfold.
Run: python3 verify.py (Python 3 standard library)."""
from fractions import Fraction as Q
from math import comb
from itertools import combinations

# A polynomial in the Chern roots x,y is a finite dictionary (power_x,power_y) -> Q.
def add(*polys):
    result = {}
    for poly in polys:
        for key, coeff in poly.items():
            result[key] = result.get(key, Q(0)) + coeff
    return {key: coeff for key, coeff in result.items() if coeff}

def scale(poly, factor):
    return {key: coeff * factor for key, coeff in poly.items() if coeff * factor}

def mul(a, b):
    result = {}
    for (i, j), c in a.items():
        for (k, l), d in b.items():
            key = (i+k, j+l)
            result[key] = result.get(key, Q(0)) + c*d
    return {key: value for key, value in result.items() if value}

def power(a, n):
    result = {(0,0):Q(1)}
    for _ in range(n):
        result = mul(result, a)
    return result

X, Y = {(1,0):Q(1)}, {(0,1):Q(1)}
H = add(X,Y)
DIFF = add(X,scale(Y,-1))

# In Gr(2,10), the Schubert coefficient rule is
# integral(f) = [x^9*y^8]((x-y)*f), with f homogeneous of degree 16.
def integrate(poly):
    p = mul(DIFF,poly)
    assert all(i+j==17 for i,j in p)
    return p.get((9,8),Q(0))

# c(TX) = (1+x)^10 (1+y)^10 / ((1-(x-y)^2)(1+x+y)^10).
# Its homogeneous degree-k part, expressed by exact finite binomial sums:
C=[]
for k in range(7):
    terms=[]
    for a in range(k//2+1):
        for b in range(k-2*a+1):
            for c in range(k-2*a-b+1):
                e=k-2*a-b-c
                coeff=Q(comb(10,b)*comb(10,c)*(-1)**e*comb(9+e,e))
                term=mul(mul(mul(power(X,b),power(Y,c)),power(DIFF,2*a)),power(H,e))
                terms.append(scale(term,coeff))
    C.append(add(*terms))
assert C[1]=={}

expected={
    'degree':1430, 'c2H4':4004, 'c3H3':-4290,
    'c4H2':9350,'c5H':-15180,'c6':24920,
    'c2cube':32480,'c2c4':26720,'c3sq':13200,'c2sqH2':11330,'c2c3H':-12210,
}
cases=[('degree',{},6),('c2H4',{2:1},4),('c3H3',{3:1},3),
       ('c4H2',{4:1},2),('c5H',{5:1},1),('c6',{6:1},0),
       ('c2cube',{2:3},0),('c2c4',{2:1,4:1},0),
       ('c3sq',{3:2},0),('c2sqH2',{2:2},2),('c2c3H',{2:1,3:1},1)]
for name,cclasses,extra_h in cases:
    integrand=power(H,10+extra_h)
    for i,multiplicity in cclasses.items():
        integrand=mul(integrand,power(C[i],multiplicity))
    assert integrate(integrand)==expected[name],name

# Independent check: localization at all C(10,2)=45 torus-fixed points.
# The tangent weights at span(e_i,e_j) are w_k-w_i and w_k-w_j (k != i,j).
loc={name:Q(0) for name,_,_ in cases}
weights=list(range(10))
for i,j in combinations(range(10),2):
    h=-(weights[i]+weights[j])
    tangent=[weights[k]-weights[i] for k in range(10) if k not in (i,j)]
    tangent += [weights[k]-weights[j] for k in range(10) if k not in (i,j)]
    euler=1
    for t in tangent: euler*=t
    numerator=[1]+[0]*6
    for t in tangent:
        for d in range(6,0,-1): numerator[d]+=t*numerator[d-1]
    ceq=[sum(numerator[d-r]*(-1)**r*comb(9+r,r)*h**r
             for r in range(d+1)) for d in range(7)]
    for name,cclasses,extra_h in cases:
        value=h**(10+extra_h)
        for d,multiplicity in cclasses.items(): value*=ceq[d]**multiplicity
        loc[name]+=Q(value,euler)
assert loc==expected,(loc,expected)

# A genus computation independent of the above Chern polynomial:
# TX = 10S* - End(S) - 10O(H) as a K-class, with formal roots x,y of S*.
# With a=z/(1+z), the degree-k coefficient in
# log(t*(1+z*exp(-t))/(1-exp(-t))) - log(1+z) is B_k(a).
# Because the first Newton power sum of TX is zero, only partitions of 6
# into pieces at least 2 contribute to the degree-six Hirzebruch class.
power_sums={k:add(scale(power(X,k),10),scale(power(Y,k),10),
                  scale(power(DIFF,k),-1),
                  scale(power(DIFF,k),-(-1)**k),
                  scale(power(H,k),-10)) for k in range(1,7)}
assert power_sums[1]=={}

def B(k,a):
    if k==2: return -(12*a*a-12*a+1)/24
    if k==3: return -a*(a-1)*(2*a-1)/6
    if k==4: return -(720*a**4-1440*a**3+840*a*a-120*a-1)/2880
    if k==6: return -(30240*a**6-90720*a**5+98280*a**4-45360*a**3+7812*a*a-252*a+1)/181440
    raise ValueError(k)

# Coefficients of chi_z(X) in ascending powers of z.
expected_chiy=[2,-252,5204,-14004,5204,-252,2]
for z in range(7):
    a=Q(z,1+z)
    P=add(scale(power_sums[6], B(6,a)),
          scale(mul(power_sums[2],power_sums[4]), B(2,a)*B(4,a)),
          scale(power(power_sums[3],2), B(3,a)**2/2),
          scale(power(power_sums[2],3), B(2,a)**3/6))
    value=(1+z)**6 * integrate(mul(power(H,10),P))
    target=sum(coef*z**i for i,coef in enumerate(expected_chiy))
    assert value==target,(z,value,target)

# Multiplication by (1+z)^6 clears the denominators in these B-polynomials,
# so both expressions are polynomials of degree at most six in z.  Seven exact
# values establish the full chi_y identity, not a mere numerical fit.
assert sum(v*(-1)**i for i,v in enumerate(expected_chiy))==24920
assert sum(expected_chiy)==-4096
assert expected_chiy[1]==-(1+251)
assert expected_chiy[2]==2+5202
assert expected_chiy[3]==-14004
assert 2*(1+251+5202)+14004==24912
assert 24912+8==24920

# From Hirzebruch--Riemann--Roch for c1=0:
# chi(O(mH)) = H6*m6/720 + c2H4*m4/288
#             + (3*c2^2 H2 - c4 H2)*m2/1440 + chi(O).
def hilbert(m):
    return (Q(1430,720)*m**6 + Q(4004,288)*m**4
            + Q(3*11330-9350,1440)*m**2+2)
assert [hilbert(i) for i in (0,1,2,3,4)]==[2,35,420,2730,11970]
print('VERIFY_OK fixed_points=45 degree=1430 euler=24920 middle_betti=24912')
print('chern_numbers',expected)
print('chi_y_coefficients',expected_chiy)
print('middle_hodge', [1,251,5202,14004,5202,251,1])
