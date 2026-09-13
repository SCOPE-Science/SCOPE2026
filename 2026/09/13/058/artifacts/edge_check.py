"""Rigorous edge-case completion for the 2-atom diagonal classification.
True line kink: W1(x)=W2(x) at xk (NOT (1+a)/2 since K1!=Ka). Compute xk exactly,
then minimize E over kink edges and confirm margin above E*."""
import math

alpha = 1.25
lam = ((1 + alpha**3) / 2) ** (1/3)
e1 = lam - 1
ea = lam - alpha
K1 = 2 * e1**2
Ka = 2 * ea**2
# kink: 2(a-1)x = (a^2-1)+(Ka-K1)
xk = ((alpha**2 - 1) + (Ka - K1)) / (2 * (alpha - 1))
print("true kink xk=%.15f" % xk)
Wk = (xk - 1)**2 + K1
print("Wline(xk)=%.15f (check well2: %.15f)" % (Wk, (xk - alpha)**2 + Ka))
A_ = lam - 1.25
c1 = 0.5 * A_ + 2 * e1**2 - 2 * ea**2
ts = -c1 / 0.125
Estar = 0.0625 * ts**2 + c1 * ts + A_**2 + 2 * ea**2
ax = lam - (1 - ts) * 0.25
bx = lam + ts * 0.25
print("Estar=%.15f t*=%.15f a*=%.15f b*=%.15f" % (Estar, ts, ax, bx))
print("a*<xk<b*: %s (margins %.4f, %.4f)" % (ax < xk < bx, xk - ax, bx - xk))

def Wline(x):
    return min((x - 1)**2 + K1, (x - alpha)**2 + Ka)

# Edge X: x=xk fixed, t in [0,1): y=(lam-t*xk)/(1-t) (>lam>xk so well-a branch)
def edgeX(t):
    y = (lam - t * xk) / (1 - t)
    return t * Wk + (1 - t) * ((y - alpha)**2 + Ka)
# dense scan + local refine
N = 20000
bt = min((edgeX(i / N), i / N) for i in range(N))
print("edgeX coarse min: E=%.12f at t=%.6f" % bt)
t = bt[1]
step = 1.0 / N
for _ in range(200):
    improved = False
    for sgn in (-1, 1):
        tt = t + sgn * step
        if 0 <= tt < 1 and edgeX(tt) < edgeX(t) - 1e-15:
            t = tt
            improved = True
    if not improved:
        step *= 0.5
        if step < 1e-13:
            break
print("edgeX refined min: E=%.15f at t=%.12f" % (edgeX(t), t))
print("margin over Estar: %.10f" % (edgeX(t) - Estar))
# Edge Y (case 1,2): y=xk -> x=(lam-(1-t)xk)/t > xk: infeasible (shown analytically); verify numeric
print("edgeY feasibility check: x(t)-xk =", [( (lam - (1 - t) * xk) / t - xk, t) for t in (0.1, 0.5, 0.9)])
# Case (2,1) interior stationary value (swap symmetry): t2=1-ts
t2 = 1 - ts
x2 = lam + t2 * 0.25  # x-y=+0.25, x=lam+(1-t2)*0.25? verify: x=lam+(1-t)*0.25 with t=t2
y2 = lam - (1 - t2) * 0.0  # placeholder
# direct: x2-y2=0.25, t2*x2+(1-t2)*y2=lam -> x2=lam+(1-t2)*0.25, y2=lam-t2*0.25
x2 = lam + (1 - t2) * 0.25
y2 = lam - t2 * 0.25
E2 = t2 * ((x2 - alpha)**2 + Ka) + (1 - t2) * ((y2 - 1)**2 + K1)
print("case(2,1) stationary: t=%.12f x=%.12f y=%.12f E=%.15f diff=%.3e" % (t2, x2, y2, E2, E2 - Estar))
print("x2>=xk, y2<=xk:", x2 >= xk, y2 <= xk)
# Case (2,2) Jensen floor:
W0 = 3 * ea**2
print("W0=%.15f margin over Estar: %.10f" % (W0, W0 - Estar))
# Case (1,1) infeasible: both<=xk<xk... mean lam>xk: confirmed since xk=%.6f<lam=%.6f" % (xk, lam))
