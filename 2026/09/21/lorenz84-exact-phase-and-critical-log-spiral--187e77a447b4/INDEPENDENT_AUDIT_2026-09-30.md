# Independent audit — 2026-09-30

**Record:** `2026/09/21/lorenz84-exact-phase-and-critical-log-spiral--187e77a447b4`  
**Audited source tree:** `4a7c0d4baea431c6183fd926cd1d096a426d7bbe`  
**Disposition:** passed

## Correctness — PASS

PASS. Writing w=y+iz gives w'=((x-1)+ibx)w, so R'=2(x-1)R and theta'=bx; integration immediately yields the exact logarithmic phase-amplitude identity. For constant F>1, the stated reduced Lyapunov function has derivative -a(x-1)^2 and is proper on R>0, and its zero-dissipation invariant set is exactly (x-1,R)=(0,a(F-1)), so LaSalle gives global convergence off the invariant axis. At F=1, W=(s^2+R)/2 has derivative -as^2; after convergence to the origin, s must become negative. With h=-s and p=h/R, p'+(a-2h)p=1 implies p->1/a, hence (1/R)'=2p gives tR->a/2 and th->1/2. Substitution in the exact phase law gives the stated t^{-1/2} amplitude and logarithmic phase lag. Boundary case R=0 is explicitly excluded from phase statements and is handled separately.

## Originality — PASS

PASS, with explicit historical-source qualification. Broer--Simó--Vitolo (2002) is the closest prior source: accessible bibliographic material confirms its symmetric reduction and seasonal-forcing/bifurcation focus, while targeted searches did not locate the exact logarithmic phase-amplitude reconstruction, explicit global isochrons, or the F=1 sharp logarithmic spiral. After open-access/preprint attempts did not yield the complete paper, authorized institutional retrieval of DOI 10.1088/0951-7715/15/4/312 returned no verified PDF, so I do not claim to have independently inspected its printed reconstruction equation. The record itself appropriately credits the reduced equations and global reduced attraction as prior. Older Lorenz-84 papers/theses remain a residual priority risk, but no inspected source covers the theorem package.

## Scientific value — PASS

PASS. The result extracts an exact phase coordinate from a standard climate model, supplies a closed-form global asymptotic-phase/isochron description above threshold, and quantifies the nonhyperbolic threshold by both amplitude and phase. The identity is elementary once found, but the combination of exact reconstruction, global basin geometry, and sharp critical asymptotics is scientifically useful and corrects a potentially misleading reconstruction in the cited literature without claiming the known reduced dynamics as new.

## Independent checks

- Re-derived the complex-coordinate equation and integrated its real and imaginary logarithmic derivatives.
- Rechecked properness and the LaSalle invariant sets for F>1 and F=1.
- Reconstructed the p=h/R comparison argument yielding tR->a/2 and t(x-1)->-1/2.
- Searched exact/synonymous phase, isochron, and critical-law terms; attempted authorized full-text retrieval of the 2002 paper after OA/preprint routes failed.

## Literature evidence

- https://doi.org/10.1088/0951-7715/15/4/312 — Broer, Simó and Vitolo (2002), closest prior Lorenz-84 reduction/bifurcation source; authorized retrieval found no verified PDF in this audit.
- https://doi.org/10.3934/dcds.2014.34.3901 — Anguiano and Caraballo (2014), nonautonomous Lorenz-84 attractor analysis; accessible abstract does not state the filed phase law.
- https://doi.org/10.1155/2014/296279 — Wang, Yu and Wen (2014), later Lorenz-84 dynamical analysis.

## Limitations

- The theorem requires zero asymmetric forcing G=0; the global isochron result additionally assumes constant F>1 and the critical asymptotics assume F=1.
- Phase is undefined on the invariant axis R=0.
- The complete 2002 Broer--Simó--Vitolo text and some older theses were not independently inspectable, leaving residual originality risk.

No GitHub write was performed by the audit chat. The guarded publication plan stages only this audit evidence and the independent-audit verification channel.
