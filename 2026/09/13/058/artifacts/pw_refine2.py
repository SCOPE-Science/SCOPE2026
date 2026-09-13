"""Targeted PW attack: split along e3 instead of e1 (relaxed hints show z-split leaves
(1.139,1.138,1.2246)/(1.136,1.140,0.9221) with E~0.0306, pen 1e-7). By symmetry e3-split =
e1-split (same E*). The relaxed E=0.0295/pen=3e-6 with x-split (0.94..)/(1.243..): pen-dominated?
E+MU*pen = 0.0295+20000*3.3e-6 = 0.0295+0.0666 -> not actually good. The pen~1e-7 ones:
0.0306+0.0022=0.0328 > E*. So NOTHING feasible below E* found; all sub-E* relaxed are pen-dominated.
Refine the two near-feasible z-split seeds with MU ramp to check if they converge to E* (like e1 case).
Seed A: ws=[0.716,0.284], X1=(1.1399,1.1384,1.2246), X2=(1.1358,1.1396,0.9221).
General 2-atom refine: vars (t,X), Y from mean; penalty ramp. Also try 3-atom seeds.
"""
import math

alpha = 1.25
lam = ((1 + alpha**3) / 2) ** (1/3)
DET0 = lam**3
C0 = lam*lam
Estar = 0.030120427271912907

def Wd(x, y, z):
    a = (x-1)**2+(y-1)**2+(z-1)**2
    b = (x-alpha)**2+(y-alpha)**2+(z-alpha)**2
    return a if a < b else b

def full(t, X):
    Y = [(lam - t*x)/(1-t) for x in X]
    (x1,x2,x3) = X; (y1,y2,y3) = Y
    mc = (t*x2*x3+(1-t)*y2*y3, t*x3*x1+(1-t)*y3*y1, t*x1*x2+(1-t)*y1*y2)
    md = t*x1*x2*x3+(1-t)*y1*y2*y3
    e = t*Wd(*X)+(1-t)*Wd(*Y)
    pen = sum((v-C0)**2 for v in mc)+(md-DET0)**2
    return e, pen, Y

def refine(t, X, mus=(1e3, 1e4, 1e5, 1e6, 1e7, 1e8)):
    for mu in mus:
        step = 0.002
        def obj(tt, XX):
            Y = [(lam - tt*x)/(1-tt) for x in XX]
            if any(v < 0.15 or v > 2.6 for v in Y): return 1e9
            (e, pen, _) = full(tt, XX)
            return e + mu*pen
        cur = obj(t, X)
        for _ in range(3000):
            improved = False
            for k in range(4):
                for sgn in (-1, 1):
                    tt, XX = t, list(X)
                    if k == 0: tt += sgn*step*0.25
                    else: XX[k-1] += sgn*step
                    if tt < 0.05 or tt > 0.95: continue
                    v = obj(tt, XX)
                    if v < cur - 1e-15:
                        cur = v; t, X = tt, XX; improved = True
            if not improved:
                step *= 0.5
                if step < 1e-10: break
    (e, pen, Y) = full(t, X)
    return e, pen, t, X, Y

seeds = [
    (0.716, (1.1399, 1.1384, 1.2246)),
    (0.449, (1.1379, 1.1402, 1.0336)),
    (0.30, (0.98, 1.13, 1.14)),
    (0.50, (1.00, 1.00, 1.30)),
    (0.50, (1.30, 1.30, 0.80)),
]
for (t, X) in seeds:
    (e, pen, tt, XX, Y) = refine(t, list(X))
    print("seed t=%.3f X=%s -> E=%.10f pen=%.2e t=%.6f X=%s Y=%s" % (t, X, e, pen, tt, [round(v,6) for v in XX], [round(v,6) for v in Y]))
print("Estar=%.10f" % Estar)
