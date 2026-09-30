# Independent Audit — Torsion levels in small horo-convex hyperbolic domains expand faster than horospheres

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `b9911ba6b6014dfe77d055ea164d7ad0fa76f30d`  
**Audited current source tree:** `b9911ba6b6014dfe77d055ea164d7ad0fa76f30d`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path is unchanged from the dispatcher's source-check commit, so the audited tree is the assigned source tree. GitHub was used read-only. The dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. Zhang–Zhou's full text proves the stronger tensor inequality Lambda=Hess(v)-|grad v|g>0 for v=-sqrt(u) under the same small-diameter strictly horo-convex hypotheses. This immediately gives Hess(v)>0, a unique nondegenerate critical minimum, and II_level(X,X)=Hess(v)(X,X)/|grad v|>|X|^2. The hyperbolic Gauss equation then gives positive intrinsic sectional curvature for n>=3. Along the level-flow Y=grad v/|grad v|^2, a transported tangent vector W satisfies d/dt log|W|=Hess(v)(W,W)/(|grad v|^2|W|^2)>1/|grad v|, while d/dt log|grad v|=Hess(v)(nu,nu)/|grad v|^2>1/|grad v|. Integration gives the claimed length, gradient and Jacobian expansion. Every flow arc is at least the ambient distance between levels, yielding the pullback-metric and area inequalities. The Morse/flow argument gives the spherical foliation.

## Originality — PASSED

PASS, narrowly scoped. The source full text states strict convexity of -sqrt(u) as its main theorem and explicitly proves the stronger tensor positivity Lambda>0 as the mechanism. It does not state the submitted torsion-level horo-convexity, global spherical foliation, or pointwise exponential level-flow/Jacobian comparison. The two-dimensional uniqueness/nondegeneracy of the torsion maximum is prior work and receives no novelty credit. The originality here is therefore only the geometric extraction and quantitative flow consequences of the new tensor estimate.

## Scientific value — PASSED

PASS. Although the derivation is short once Lambda>0 is available, the result translates an analytic constant-rank estimate into a concrete geometric comparison with horospherical normal flow, including pointwise metric and area expansion and all-dimensional strict horo-convexity of torsion superlevels. These consequences are reusable and materially sharpen the geometric interpretation of the source theorem.

## Independent checks

- After ordinary open full-text retrieval was insufficient, read Zhang–Zhou's lawful full text via authorized institutional retrieval; the introduction explicitly defines Lambda=Hess(v)-|grad v|g and states the proof establishes Lambda>0.
- Re-derived the level second fundamental form and hyperbolic Gauss-equation consequences.
- Re-derived both differential expansion identities along Y=grad v/|grad v|^2 and the Jacobian estimate.
- Checked the nondegenerate-minimum/Morse-flow argument giving a nested S^{n-1} foliation.
- Checked that ambient level separation is bounded by every connecting flow-arc length, producing the uniform e^{delta} comparison.
- Verified no files under the assigned record changed between the dispatcher source-check commit and current main, and verified both dated independent-audit files and FAILED_ATTEMPT.md are absent.

## Limitations

- The result inherits the source's strict horo-convexity and diameter bound and does not show these assumptions are necessary.
- The key tensor inequality is Zhang–Zhou's prior result; the audit credits only its geometric consequences.
- The expansion is for the canonical gradient level-flow and does not provide a dimension-only quantitative margin beyond the strict factor.

## Evidence and references

- https://arxiv.org/abs/2609.02516
- https://doi.org/10.1007/s00208-023-02722-7
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/torsion-level-horospherical-expansion--b7c156417bf2

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
