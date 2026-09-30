# Independent audit — 2026-09-29

**Record:** `2026/09/17/analytic-rigidity-of-milman-polar-sum-equation--8d105c333ef0`  
**Audited source tree:** `8ff6c3e59193804489a25c67f5e675e97ba0eb67`  
**Repository:** `SCOPE-Science/SCOPE2026` at checked commit `253a0fe5d0217455660a277f9adb940030e567ad`  
**Overall independent-audit verdict:** **PASS**

## Correctness — PASS

The reduction of K+T=K^circ+T^circ to equality of F_K=h_K-1/rho_K is correct after putting L=T^circ.  Segal's alternating-direction lemma plus the record's quantitative increment estimate forces consecutive angular gaps to zero, so an alternating subsequence has a common limiting direction at which the two support functions agree and both support-to-radial maps fix the direction.  The polar second-jet calculation q''(0)=-b/[a(a+b)] is correct and makes F'' strictly increasing in b.  If the first unequal support jet has order m>=3, the nondegenerate polar maximizer moves only O(alpha^{m-1}); stationarity makes that displacement higher order, while the direct reciprocal-support term changes the coefficient by the negative factor -a^{m-2}/R^m.  Equality F_K=F_L is then impossible at finite order.  Hence a smooth nontrivial pair must have a flat contact, and real analyticity forces global equality.

## Originality — PASS

The September 2026 Segal preprint gives rigidity for polytopes and counterexamples for general convex bodies; the inspected statements do not provide a positive-curvature analytic rigidity theorem or the infinite-order-contact obstruction.  Targeted searches did not locate an earlier theorem matching this regularity regime.  Because the motivating preprint is very recent, concurrent or poorly indexed work remains a residual priority risk.

## Scientific value — PASS

The result identifies a natural rigid class between the known polytope theorem and general counterexamples, while the smooth flat-contact statement gives a structural obstruction stronger than the analytic corollary and materially constrains possible smooth counterexamples.

## Sources used in the independent comparison

- https://arxiv.org/abs/2609.12685 — Segal preprint motivating the equation; proves the polytope positive result and general negative result used as the comparison baseline.

## Limitations and residual uncertainty

- The theorem is planar and assumes strictly positive curvature.
- It does not rule out non-analytic C-infinity positive-curvature counterexamples with infinite-order contact, nor higher-dimensional failures.
- Originality is necessarily qualified because the motivating preprint is only weeks old.

This independent audit is scoped to correctness, originality, and scientific value.  Repository material was used as evidence only; no GitHub modification was made during the audit.
