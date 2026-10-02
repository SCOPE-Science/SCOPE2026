# Independent scientific review — 2026-10-01

## Final claim

For symmetric Lorenz-84 with \(G=0\), the eddy phase satisfies the exact phase-amplitude law \(\theta(t)-\theta(0)=bt+(b/2)\log(R(t)/R(0))\). In the autonomous case \(F>1\) this yields explicit global isochrons on \(R>0\); at the critical value \(F=1\), every off-axis orbit has \(tR(t)\to a/2\), \(t(x(t)-1)\to-1/2\), and a logarithmic phase lag with the stated coefficient.

## Correctness — PASS

Writing \(w=y+iz\) gives \(\dot w=((x-1)+ibx)w\), hence \(\dot R=2(x-1)R\) and the phase-amplitude identity by direct integration. For constant \(F>1\), the reduced system in \(s=x-1\) and \(R\) has a coercive relative-entropy Lyapunov function whose derivative is \(-as^2\), so on \(R>0\) LaSalle gives global convergence to \((0,a(F-1))\); subtracting the logarithmic amplitude term produces the exact phase coordinate. At \(F=1\), \(W=(s^2+R)/2\) has derivative \(-as^2\); after setting \(h=-s\), the ratio \(p=h/R\) satisfies \(p' +(a-2h)p=1\), giving \(p\to1/a\), then \((1/R)'\to2/a\) and the stated sharp amplitude and phase asymptotics. The invariant axis \(R=0\) is correctly excluded from phase claims.

**Risk:** The theorem is confined to \(G=0\); it does not assert global phase coordinates for asymmetric forcing.

## Originality — PASS

The full Broer–Simó–Vitolo primary paper was inspected at the reduced-system and reconstruction pages. It defines \(r=y^2+z^2\), proves the autonomous \(F>1\) reduced global attractor, and prints a reconstruction of \(y,z\) in its equation (10); it does not state the audited logarithmic phase-amplitude invariant, global isochrons, or the \(F=1\) sharp algebraic/logarithmic asymptotics. A Resultary search found a distinct earlier Lorenz-84 stationary eddy-memory result, not this phase theorem.

**Risk:** Older Lorenz-84 theses and early papers were not exhaustively inspected, so priority risk remains.

## Value — PASS

The exact phase coordinate and critical logarithmic spiral sharpen the qualitative Hopf/reduced-attractor picture of a classic atmospheric model. The result gives explicit global isochrons and leading critical constants rather than a routine local calculation.

**Risk:** The contribution is special to the symmetric \(G=0\) reduction and does not address the generic forced model.

## Overall disposition

**PASSED**
