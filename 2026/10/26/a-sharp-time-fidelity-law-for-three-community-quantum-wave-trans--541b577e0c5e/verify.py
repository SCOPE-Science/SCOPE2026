"""Independent numerical checks for the three-site wave-transfer rate.

Execute with Python 3, numpy and mpmath. The proof is analytic; this program
checks the matrix reduction, exact Pell identities and high-precision limits.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 100
COUNT = 0

def check(condition, what):
    global COUNT
    if not bool(condition):
        raise AssertionError(what)
    COUNT += 1


def amplitude(s):
    return mp.mpf(1) / 3 - mp.cos(s) / 2 + mp.cos(mp.sqrt(3) * s) / 6


def infidelity(s):
    a = amplitude(s)
    return (1-a) * (1+a)


L = np.array([[1.,-1.,0.],[-1.,2.,-1.],[0.,-1.,1.]])
e, V = np.linalg.eigh(L)
for expected, actual in zip([0., 1., 3.],e):
    check(abs(actual-expected) < 2e-14, "Laplacian spectrum")
for s in np.linspace(0., 123.456, 57):
    cosine_matrix = (V * np.cos(s * np.sqrt(np.clip(e,0,None)))) @ V.T
    a = 1./3 - .5*math.cos(s) + math.cos(math.sqrt(3.)*s)/6
    check(abs(cosine_matrix[0,2]-a) < 1e-12, "spectral amplitude")
    check(abs(cosine_matrix[2,0]-a) < 1e-12, "symmetric endpoint amplitude")

# The exact Cauchy completion of squares is independent of number theory:
# (e1^2/2 + e2^2/6) - (e2 - sqrt(3)*e1)^2/12
#   = (sqrt(3)*e1+e2)^2/12 >= 0.
for j in range(150):
    e1=mp.sin(mp.mpf(j+1)*mp.mpf('0.713'))
    e2=mp.cos(mp.mpf(j+2)*mp.mpf('0.319'))
    left=e1*e1/2+e2*e2/6
    lower=(e2-mp.sqrt(3)*e1)**2/12
    residue=(mp.sqrt(3)*e1+e2)**2/12
    check(abs(left-lower-residue)<mp.mpf('1e-90'), "square completion")

p,q=2,1
C=mp.pi**4/144
for j in range(7):
    check(p % 2 == 0 and q % 2 == 1, "Pell parity")
    check(p*p-3*q*q == 1, "Pell norm")
    z=mp.mpf(p)+mp.sqrt(3)*q
    d=1/z
    s=mp.pi*z/(2*mp.sqrt(3))
    e1=s-mp.pi*q
    e2=mp.sqrt(3)*s-mp.pi*p
    check(abs(e1-mp.pi*d/(2*mp.sqrt(3)))<mp.mpf('1e-85'), "first optimized phase")
    check(abs(e2+mp.pi*d/2)<mp.mpf('1e-85'), "second optimized phase")
    deficit=infidelity(s)
    leading=mp.pi**2*d*d/12
    check(deficit>0, "strictly imperfect transfer")
    check(abs(deficit-leading) < 2*d**4, "Pell asymptotic remainder")
    if j>=2:
        check(abs(s*s*deficit-C) < mp.mpf('1.0')/z**2,"sharp asymptotic constant")
    # Test the unshifted resonance used in early Pell constructions.
    raw=mp.pi*q
    rawdef=infidelity(raw)
    if j>=2:
        check(abs(raw*raw*rawdef-2*C) < mp.mpf('5.0')/z**2,"factor-two time optimization")
    # p+q sqrt(3) multiplied by (2+sqrt(3))^2=7+4 sqrt(3)
    p,q=7*p+12*q,4*p+7*q

print("PASS:",COUNT,"finite independent checks")
print("liminf s^2 (1-P):",mp.nstr(C,30))
print("for equal arc mass 12 and one bridge each:",mp.nstr(12*C,30))
