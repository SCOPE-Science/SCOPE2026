"""Exact coefficient and Frobenius-block checks in characteristic five.
Requires sympy. This script checks identities; the proof explains their geometric use.
"""
import sympy as s

x, a = s.symbols('x a')

def mod(e):
    return sum((int(c) % 5)*a**power[0] for power,c in s.Poly(s.expand(e), a).terms())

def coeff_matrix(degree, f):
    # For gcd(3,degree)=1, basis x^i dx/y^j, 0<=i<floor((j*degree-1)/3).
    d1=(degree-1)//3
    d2=(2*degree-1)//3
    A=s.zeros(d2,d1) # 1 -> 2 from f^3
    B=s.zeros(d1,d2) # 2 -> 1 from f
    for j,(source,output,power,M) in enumerate(((d1,d2,3,A),(d2,d1,1,B))):
        polynomial=s.Poly(s.expand(f**power),x)
        for i in range(source):
            for z in range(output):
                M[z,i]=mod(polynomial.nth(5*z+4-i)) if 5*z+4-i >= 0 else 0
    return A,B

A,B=coeff_matrix(8,x**8+a*x**6+1)
expected_A=s.Matrix([[0,0],[0,3],[a,0],[0,a**3],[1,0]])
expected_B=s.Matrix([[0,0,0,0,1],[0,1,0,a,0]])
assert A==expected_A,(A,expected_A)
assert B==expected_B,(B,expected_B)
T=(B.applyfunc(lambda z:mod(z**5))*A).applyfunc(mod)
assert T==s.diag(1,mod(3+a**8)),T
assert int(A.extract([1,4],[0,1]).det())%5 == 2
assert int(B.extract([0,1],[1,4]).det())%5 == 4

AQ,BQ=coeff_matrix(4,x**4+a*x**3+1)
assert AQ==s.Matrix([[3],[a**3]]),AQ
assert BQ==s.Matrix([[1,a]]),BQ
TQ=(BQ.applyfunc(lambda z:mod(z**5))*AQ).applyfunc(mod)
assert TQ==s.Matrix([[mod(a**8+3)]]),TQ
assert mod(3+a**8)==mod(a**8-2)
assert s.gcd(s.Poly(a**4-3,a,modulus=5),s.Poly(a**8-2,a,modulus=5)).degree()==0
assert s.Poly(a**8-2,a,modulus=5).is_irreducible
assert s.Poly(a**4-3,a,modulus=5).is_irreducible
# Geometric smoothness: at nonzero critical x, x^2=3a, f(x)=1+3a^4.
assert mod(1+3*a**4)==mod(3*(a**4-3))
print('SYMBOLIC_GENUS7_PRYM_OK')
print('Cartier source/output block sizes (j=1 to 2, j=2 to 1):',A.shape,B.shape)
print('Twisted two-step blocks:',T,TQ)
print('Exceptional x^8-2 irreducible, smoothness x^4-3 disjoint')
