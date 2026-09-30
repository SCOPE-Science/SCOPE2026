# Independent audit — 2026-09-30

**Record:** `2026/09/20/rabinovich-fabrikant-recurrence-sign-selection--047ddc1ae9fc`  
**Audited source tree:** `b98e54f94a82f6c89ed8ba7fdd048c4554394763`  
**Disposition:** passed

## Correctness — PASS

PASS. I independently differentiated W=x^2+y^2+4z and obtained Wdot=2 gamma(x^2+y^2)-8 alpha z, and on z=0 obtained qdot=2 gamma q. The exact log|z| identity plus Poincare recurrence and Birkhoff genericity gives integral xy=-alpha without assuming log|z| integrable. Invariance of W then gives the displayed mean-height and anisotropy laws. The gamma=0 planar polar reduction gives theta'=1-r^2 cos^2(theta), hence precisely the circles 0<r<1 with period 2 pi/sqrt(1-r^2). For gamma<0,z>=0, W is positive and satisfies Wdot<=-min(2|gamma|,2 alpha)W; applying this to complete bounded trajectories also proves the claimed compact-invariant-set exclusion. I separately checked that equality in the periodic mean-height inequality forces x+y identically zero and then an equilibrium, so the strict statement is valid.

## Originality — PASS

PASS, narrowly and to the best of current evidence. The 1979 Rabinovich--Fabrikant paper explicitly contains the conservative energy x^2+y^2+4z and the invariant plane z=0; those are correctly excluded from the novelty claim. The inspected later RF literature focuses on equilibria, invariant manifolds, bifurcation/attractor numerics, averaging constructions of periodic orbits, and negative-parameter scans. I did not find the compact-ergodic identities integral xy=-alpha and integral z=gamma/2+(gamma/(4alpha)) integral(x+y)^2, their half-space recurrence selection, the exact gamma=0 periodic classification, or the gamma<0 physical-half-space collapse theorem. Older or poorly indexed literature in the original wave variables remains a residual risk, so this is not an exhaustive novelty guarantee.

## Scientific value — PASS

PASS. Exact invariant-measure constraints that apply simultaneously to periodic, quasiperiodic, and chaotic recurrent states are more informative than a parameter scan; the sign-selection law forbids entire classes of recurrent states, the gamma=0 slice is fully classified at periodic-orbit level, and the gamma<0 theorem supplies a simple global exclusion region.

## Independent checks

- Symbolically re-differentiated W, q on z=0, and x+y on y=-x.
- Reconstructed the ergodic recurrence/logarithm argument and the generator identity.
- Integrated the gamma=0 angular equation exactly and checked the r=1 and r>1 stopping points.
- Rechecked the complete-trajectory argument behind the global compact-invariant-set exclusion.

## Literature evidence

- https://www.jetp.ras.ru/cgi-bin/dn/e_050_02_0311.pdf — Rabinovich and Fabrikant (1979), primary model source; explicitly gives the conservative energy and invariant plane.
- https://doi.org/10.1142/S0218127416500383 — Danca, Feckan, Kuznetsov and Chen (2016), later RF invariant-manifold/attractor analysis.
- https://doi.org/10.18500/0869-6632-003015 — Turukina (2022), negative-dissipation numerical/bifurcation study.

## Limitations

- The invariant-measure theorem assumes compact support and is stated ergodic-componentwise.
- The exponential global theorem is restricted to alpha>0, gamma<0 and z>=0.
- Originality remains subject to older or non-indexed RF literature using different variables/terminology.

No GitHub write was performed by the audit chat. This file is staged by the guarded `scope-audit-change-set-v1` plan only.
