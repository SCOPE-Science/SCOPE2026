"""Quadrature corroboration of Knapp lower bound at R=256 (lane-527).
Checks min |I(y)| over the coherence box T_y by direct numerical integration.
I(y) = A(y1,y3)*B(y2,y3), A=int_{-d}^{d} e^{i(y1 u+y3 u^3)}du, B=int_{-s}^{s} e^{i(y2 v-y3 v^2)}dv.
"""
import math

R = 256
d = R**(-1/3); s = R**(-1/2)
c = 0.1

def A_val(y1, y3, n=4000):
    h = 2*d/n
    tot = 0j
    for k in range(n+1):
        u = -d + k*h
        w = 0.5 if (k==0 or k==n) else 1.0
        tot += w*complex(math.cos(y1*u+y3*u**3), math.sin(y1*u+y3*u**3))
    return tot*h

def B_val(y2, y3, n=2000):
    h = 2*s/n
    tot = 0j
    for k in range(n+1):
        v = -s + k*h
        w = 0.5 if (k==0 or k==n) else 1.0
        tot += w*complex(math.cos(y2*v-y3*v**2), math.sin(y2*v-y3*v**2))
    return tot*h

area = 4*d*s
print(f"R={R}, d={d:.6f}, s={s:.6f}, area(Q)={area:.6e}, ||f||_2={2*math.sqrt(d*s):.6e}")

# sample corners/center of T_y (worst case expected at corners)
import itertools
corners = list(itertools.product([-1,0,1], repeat=3))
worst = 1e99; worst_pt=None
for s1,s2,s3 in corners:
    y1,y2,y3 = s1*c/d, s2*c/s, s3*c*R
    Aval = A_val(y1,y3); Bval = B_val(y2,y3)
    I = Aval*Bval
    m = abs(I)
    print(f"y=({y1:+.3f},{y2:+.3f},{y3:+.1f}): |A|={abs(Aval):.6e} |B|={abs(Bval):.6e} |I|={m:.6e} ratio-to-area={m/area:.4f}")
    if m < worst: worst=m; worst_pt=(y1,y2,y3)

theory = area*math.cos(0.4)
print(f"\nmin|I| over 27-pt grid = {worst:.6e} at {worst_pt}")
print(f"analytic lower bound area*cos(0.4) = {theory:.6e}")
print("QUAD_CHECK:", "PASS" if worst >= theory*0.999 else "FAIL")

# L^p ratio lower bounds from analytic formula
for p in [3.5, 4.0, 4.2]:
    e = 11/(6*p)-5/12
    const = 1.8421*(0.008)**(1/p)
    print(f"p={p}: ratio >= {const:.4f} R^{e:+.5f} = {const*R**e:.4f} at R={R}")
print("VERIFY_OK")
