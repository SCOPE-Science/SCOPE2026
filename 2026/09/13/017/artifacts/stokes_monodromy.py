"""Loop monodromy at x=0 (self-contained fixed-step RK4, mpmath arbitrary precision).

M(x) = [[a,1],[1,-a]], a = 2x+1/(2x)+1/x^2.
Formal monodromy at 0 is scalar -I (system exponents +-1/2); rank-1 Stokes
relation M_0 = -S_2 S_1 gives tr(M_0)+2 = -(s1*s2): nonzero => at least one
Stokes multiplier != 0. Loop |x|=r avoids both singularities.
det(M_0)=1 self-check; radius/mesh independence check included.
"""
import json
from mpmath import mp, mpc, exp, pi

mp.dps = 50

def monodromy(r, N):
    h = 2*pi/N
    V = [mpc(1), mpc(0), mpc(0), mpc(1)]
    def F(th, V):
        z = r*exp(mpc(0, 1)*th)
        dz = mpc(0, 1)*z
        a = 2*z + 1/(2*z) + 1/z**2
        return [dz*(a*V[0]+V[2]), dz*(a*V[1]+V[3]),
                dz*(V[0]-a*V[2]), dz*(V[1]-a*V[3])]
    th = mp.mpf(0)
    for _ in range(N):
        k1 = F(th, V)
        V2 = [V[i]+(h/2)*k1[i] for i in range(4)]
        k2 = F(th+h/2, V2)
        V3 = [V[i]+(h/2)*k2[i] for i in range(4)]
        k3 = F(th+h/2, V3)
        V4 = [V[i]+h*k3[i] for i in range(4)]
        k4 = F(th+h, V4)
        V = [V[i]+(h/6)*(k1[i]+2*k2[i]+2*k3[i]+k4[i]) for i in range(4)]
        th += h
    tr = V[0]+V[3]; det = V[0]*V[3]-V[1]*V[2]
    return {"r": str(r), "N": N, "trace": str(tr), "det": str(det),
            "tr_plus_2": str(tr+2), "stokes_product": str(-(tr+2)),
            "abs_tr_plus_2": str(abs(tr+2))}

runs = [monodromy(mp.mpf(r), N)
        for r, N in [(mp.mpf('0.5'), 2000), (mp.mpf('0.5'), 4000),
                     (mp.mpf('1.0'), 4000), (mp.mpf('0.25'), 4000)]]
out = {"dps": mp.dps, "runs": runs}
print(json.dumps(out, indent=2))
with open("output/artifacts/stokes_monodromy.json", "w") as fh:
    json.dump(out, fh, indent=2)
