"""Independent standard-library binomial verification of the four Cartier blocks.
Run: python3 verify_binomial_11.py. All coefficients are modulo 11.
"""
from math import comb
p=11

def poly_add(a,b):
    c={}
    for k in set(a)|set(b):
        v=(a.get(k,0)+b.get(k,0))%p
        if v: c[k]=v
    return c

def poly_mul(a,b):
    c={}
    for i,ai in a.items():
        for j,bj in b.items():
            v=(c.get(i+j,0)+ai*bj)%p
            if v:c[i+j]=v
            elif i+j in c:del c[i+j]
    return c

def pow_poly(a,n):
    r={0:1}
    for _ in range(n):r=poly_mul(r,a)
    return r

def coeff_direct(q,r,e,k):
    # x^r (x-t)^e [x(x-1)(x-t)^2]^q.
    # Expand only the two binomials in x; return a dict t_degree -> F11 coefficient.
    out={}
    total=k-q-r
    for u in range(q+1):
        v=total-u
        if not 0<=v<=2*q+e:continue
        d=2*q+e-v
        coef=comb(q,u)*(-1)**(q-u)*comb(2*q+e,v)*(-1)**d
        out[d]=(out.get(d,0)+coef)%p
    return {k:v for k,v in out.items() if v}

t={1:1};one={0:1};minusone={0:10}
Q={0:1,1:10,2:1}
# Independent target polynomials, built in the coefficient ring F11[t].
P_minus1=poly_add(t,{0:10})
P_m3=poly_add(t,{0:8})
P_plus5=poly_add(t,{0:5})
A=poly_mul({2:6},poly_mul(pow_poly(P_minus1,2),Q))
B=poly_mul({0:4},Q)
a=poly_mul({4:6},{2:1,1:8,0:8})
b=poly_mul({5:3},{1:1,0:9})
c=poly_mul({0:5},P_plus5)
d=poly_mul({0:4},{2:1,1:1,0:7})
for q,r,e,scalars in [
 (4,0,0,[(10,A)]),
 (6,0,1,[(10,poly_mul({11:10},B)),(21,B),(32,{})]),
 (8,0,1,[(10,poly_mul({11:10},a)),(21,poly_add(a,poly_mul({11:10},c))),(32,c)]),
 (8,1,1,[(10,poly_mul({11:10},b)),(21,poly_add(b,poly_mul({11:10},d))),(32,d)]),
]:
  for k,expected in scalars:
    actual=coeff_direct(q,r,e,k)
    assert actual==expected, (q,r,e,k,actual,expected)
print('BINOMIAL_OK: eleven independent F11[t] coefficients match all four Cartier block identities')
# Show rank-two determinant of the 2x2 block, with no symbolic algebra package.
det=poly_add(poly_mul(a,d),poly_mul({0:10},poly_mul(b,c)))
expected=poly_mul({4:2},pow_poly(P_minus1,4))
assert det==expected,(det,expected)
assert poly_mul(poly_mul(A,B),det)==poly_mul(poly_mul({6:4},pow_poly(P_minus1,6)),pow_poly(Q,2))
print('BINOMIAL_DETERMINANT_OK: block det=2*t^4*(t-1)^4 and total Hasse determinant=4*t^6*(t-1)^6*Q^2')
