# Independent Audit — Isolated points are exactly the boundary for point-mass isotropy restriction

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `e3a13775c5c3017a2a3069a5278eb364e5932755`  
**Audited current source tree:** `e3a13775c5c3017a2a3069a5278eb364e5932755`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the assigned source tree. GitHub was used only as read-only evidence, and the dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. In a Hausdorff ample groupoid, a singleton characteristic function belongs to the Steinberg algebra only if the singleton is open; conversely, if the unit x is open, intersecting a compact open bisection through an isotropy arrow with s^{-1}({x}) gives a compact open singleton. Thus the point-mass isotropy embedding exists exactly at isolated units. The support calculation then gives e_xAe_x=R[G_x^x] and Ae_x=RL_x. In the one-vertex two-loop graph the infinite-path space is Cantor, so x=a^∞ is not isolated and even the identity point mass is absent, invalidating the cited unrestricted point-mass formula. The finite-dimensional graded obstruction is also exact: a nonzero periodicity p gives an invertible homogeneous corner element of degree p, whose powers send a nonzero homogeneous vector into infinitely many distinct degrees.

## Originality — PASS

PASS, narrowly scoped. Standard Steinberg induction from isotropy through the source fiber is prior art, and open-singleton corner identifications are also known. The novelty credited here is only the source-specific correction to Nguyen's 2026 Kumjian–Pask restriction construction: identifying isolation as the exact boundary for the claimed point-mass embedding, supplying a minimal permitted counterexample, and deriving the finite-dimensional graded periodicity obstruction in that corrected setting. Targeted searches located the general older machinery but no prior public correction to this very recent proposition.

## Scientific value — PASS

PASS. The corrected hypothesis is foundational rather than cosmetic because the source's restriction-of-scalars construction is undefined at nonisolated boundary paths. The result both pinpoints the exact repair and separates it from the valid standard fiber-induction theory, while the graded obstruction clarifies an additional incompatibility between finite-dimensional graded fibers and nontrivial periodicity.

## Independent checks

- Proved both directions of the singleton/open-unit equivalence directly from local constancy and the étale bisection structure.
- Checked the corner and source-fiber identifications from support and finite compact support.
- Verified the one-vertex two-loop graph satisfies the source's row-finite/no-sources setting and has no isolated infinite paths.
- Reproved the finite-dimensional graded periodicity contradiction using an invertible homogeneous corner element.
- Compared with standard Steinberg isotropy induction in Nguyen–Nguyen and with known open-singleton corner literature.
- Checked the current public source description of arXiv:2609.20230, which treats restriction at a fixed infinite path, and found no public correction covering the submitted issue.
- Verified the assigned record was unchanged from the dispatcher source-check commit to current main and that the 2026-09-30 audit markers are absent.

## Limitations

- The result corrects the particular point-mass restriction construction; it does not challenge standard isotropy induction/restriction through groupoid source fibers.
- The isolated-singleton criterion is elementary and may be implicit in older Steinberg-algebra literature; originality is restricted to its application and consequences for the cited 2026 source.
- The full text of every historical induction paper was not exhaustively compared.

## Evidence and references

- https://arxiv.org/abs/2609.20230
- https://arxiv.org/abs/2006.09931
- https://arxiv.org/abs/2502.15574
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/isolated-point-boundary-kp-isotropy-restriction--6715bedaa3ac

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
