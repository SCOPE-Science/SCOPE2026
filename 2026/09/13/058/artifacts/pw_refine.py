"""Refine the 2-atom PW candidate: solve cof+det constraints EXACTLY and minimize energy.
Use deterministic local optimization from the found seed with exact penalty->0.
Then attempt analytic understanding: is the candidate genuinely below E*=0.03012?
Seed: t=0.2686, X=(0.9763,1.1303,1.1359), Y=(1.1984,1.1418,1.1398).
Check: mean should be exact by construction. cof/det mismatch ~1e-6 (pen). Refine.
Method: coordinate descent on (t,X) with Y from mean constraint, penalty weight ramp.
"""
import math

alpha = 1.25
lam = ((1 + alpha**3) / 2) ** (1/3)
DET0 = lam**3
C0 = lam*lam

def Wd(x, y, z):
    a = (x-1)**2+(y-1)**2+(z-1)**2
    b = (x-alpha)**2+(y-alpha)**2+(z-alpha)**2
    return a if a < b else b

t = 0.26855383198909866
X = [0.9762585837399508, 1.1303388095793911, 1.1358942320079732]

def full(t, X):
    Y = [(lam - t*x)/(1-t) for x in X]
    (x1,x2,x3) = X; (y1,y2,y3) = Y
    mc = (t*x2*x3+(1-t)*y2*y3, t*x3*x1+(1-t)*y3*y1, t*x1*x2+(1-t)*y1*y2)
    md = t*x1*x2*x3+(1-t)*y1*y2*y3
    e = t*Wd(*X)+(1-t)*Wd(*Y)
    pen = sum((v-C0)**2 for v in mc)+(md-DET0)**2
    return e, pen, Y, mc, md

def obj(t, X, mu):
    (e, pen, Y, mc, md) = full(t, X)
    if any(v < 0.15 or v > 2.6 for v in Y):
        return (1e9, e, pen, Y)
    return (e + mu*pen, e, pen, Y)

for mu in (10**3, 10**4, 10**5, 10**6, 10**7):
    step = 0.002
    cur = obj(t, X, mu)[0]
    for _ in range(4000):
        improved = False
        for k in range(4):
            for sgn in (-1, 1):
                tt, XX = t, list(X)
                if k == 0: tt += sgn*step*0.25
                else: XX[k-1] += sgn*step
                if tt < 0.05 or tt > 0.95: continue
                v = obj(tt, XX, mu)[0]
                if v < cur - 1e-15:
                    cur = v; t, X = tt, XX; improved = True
        if not improved:
            step *= 0.5
            if step < 1e-9: break
    (e, pen, Y, mc, md) = full(t, X)
    print("mu=%.0e E=%.10f pen=%.3e t=%.8f X=%s Y=%s" % (mu, e, pen, t, X, Y))
    print("   cof=%s det=%.10f targets C0=%.10f DET0=%.10f" % (mc, md, C0, DET0))
