#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 60

# Example 1 from the motivating source.
m = mp.mpf("0.6")
r = mp.mpf("1")
a = mp.mpf("3")
k = mp.mpf("0.08")
b = mp.mpf("0.2")
p = mp.mpf("0.5")
d = mp.mpf("1")
c = mp.mpf("2")
e = mp.mpf("1.1")

K = a/b
C = (e*K**p)**(1/(r-m))
assert K == 15
assert abs(C-mp.mpf("37.462416393001334")) < mp.mpf("1e-12")

def equations(u,v,q):
    F = a*u/(1+k*v)-b*u*u-c*u**p*v**m
    G = -d*v-q*v**r+e*u**p*v**m
    return F,G

def jacobian(u,v,q):
    Fu = a/(1+k*v)-2*b*u-c*p*u**(p-1)*v**m
    Fv = -a*k*u/(1+k*v)**2-c*m*u**p*v**(m-1)
    Gu = e*p*u**(p-1)*v**m
    Gv = -d-q*r*v**(r-1)+e*m*u**p*v**(m-1)
    # Reconstructed equilibrium identities.
    Fu_eq = -b*u+c*(1-p)*u**(p-1)*v**m
    Gv_eq = -(1-m)*d-(r-m)*q*v**(r-1)
    assert abs(Fu-Fu_eq) < mp.mpf("1e-35")
    assert abs(Gv-Gv_eq) < mp.mpf("1e-35")
    return Fu,Fv,Gu,Gv

previous_ratio = mp.mpf("0")
for q_text in ("10","100","1000"):
    q = mp.mpf(q_text)
    v0 = (e*K**p/q)**(1/(r-m))
    u0 = K*(1-mp.mpf("0.05"))
    u,v = mp.findroot(lambda U,V: equations(U,V,q), (u0,v0))
    F,G = equations(u,v,q)
    assert abs(F) < mp.mpf("1e-35")
    assert abs(G) < mp.mpf("1e-35")
    assert 0 < u < K and v > 0
    Fu,Fv,Gu,Gv = jacobian(u,v,q)
    tr = Fu+Gv
    det = Fu*Gv-Fv*Gu
    assert tr < 0
    assert det > 0
    ratio = q*v**(r-m)/(e*K**p)
    assert ratio > previous_ratio
    previous_ratio = ratio
    print("q", q_text, "u", mp.nstr(u,20), "v", mp.nstr(v,20),
          "ratio", mp.nstr(ratio,20), "trace", mp.nstr(tr,20), "det", mp.nstr(det,20))

assert previous_ratio > mp.mpf("0.998")
print("VERIFY_OK")
print("K", mp.nstr(K,20))
print("asymptotic_coefficient", mp.nstr(C,20))
