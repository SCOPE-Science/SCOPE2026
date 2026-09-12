import sys
sys.path = [p for p in sys.path if p not in ('/tmp','')]
import mpmath as mp
mp.mp.dps = 60

def compute(d):
    d = mp.mpf(d)
    e1 = -(mp.mpf(10)+d**2)/2
    def s_abs(E):
        R = (E**2-9)*(E**2-1)*(E**2-d**2)
        return mp.sqrt(abs(R))
    # gap (d,1): y real = sqrt(R), R>0
    # dp numerator E^2+b: condition int_d^1 (E^2+b)/s = 0
    f0 = lambda E: 1/s_abs(E)
    f2 = lambda E: E**2/s_abs(E)
    f4 = lambda E: E**4/s_abs(E)
    I0 = mp.quad(f0, [d, 1])
    I2 = mp.quad(f2, [d, 1])
    I4 = mp.quad(f4, [d, 1])
    b = -I2/I0
    # dOm numerator E^4+e1 E^2+p1: int (E^4+e1E^2+p1)/s=0
    p1 = -(I4+e1*I2)/I0
    return b, e1, p1, I0, I2, I4

for d in [0.05,0.1,0.2,0.3,0.5,0.7,0.9,0.95,0.99]:
    b,e1,p1,I0,I2,I4 = compute(d)
    V = lambda s: (s**2+e1*s+p1)/(s+b)
    v9, v1, vd = V(9), V(1), V(d**2)
    print(f"d={d} b={float(b):.8f} e1={float(e1):.6f} p1={float(p1):.8f}")
    print(f"   V(3)={float(v9):.8f} V(1)={float(v1):.8f} V(d)={float(vd):.8f}  diffs: {float(v9-v1):.5f} {float(v9-vd):.5f} {float(v1-vd):.5f}")
