# Independent Audit — 2026-09-29

**Record:** `2026/09/20/centered-maximal-near-eigenfunction-rigidity--38695a6091d8`  
**Title:** Quantitative near-eigenfunction rigidity for the sharp centered maximal inequality  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `4cacaca44b7325950f578995d47beb693a18a3b2`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The exact one-sided rising-sun identity gives ||M_±f||_p^p=p'∫f(M_±f)^{p-1}. A centered near-extremizer forces both one-sided norms within O(delta) of p'; normalizing and applying Lp uniform convexity then gives the claimed delta^{1/max(2,p)} near-eigenfunction estimate. Pointwise domination and (A-B)^p<=A^p-B^p transfer control to the centered and restricted-radii operators. Exact saturation yields a t^{-p} distribution tail and hence excludes nonzero Lp extremizers. The compactness consequence follows from norm invariance and Lipschitz continuity of M_c.
- **Originality — PASS:** Madrid’s 2026 preprint establishes the newly sharp centered norm p', constructs extremizing sequences, and proves the same norm for geometrically restricted centered radii. Accessible current descriptions do not state nonattainment or quantitative simultaneous one-sided/centered near-eigenfunction rigidity, and focused searches did not locate such a follow-up. Older eigenfunction/nonattainment work concerns the uncentered operator with a different sharp constant.
- **Scientific value — PASS:** The result adds a stability/equality theory to a newly solved sharp-constant problem: every centered near-extremizer must exhibit the same operator profile, exact attainment is impossible, and strong precompactness modulo translations/dilations is ruled out. That is a meaningful structural complement to existence of extremizing sequences.

## Independent findings
- Checked the normalization of the exact one-sided identity and the step from near one-sided norm saturation to near equality in Hölder.
- Checked the exponent comparison: the centered gap contributes delta^{1/p}, which is no worse than delta^{1/max(2,p)} in the small-deficit regime.
- Re-derived the distribution-function ODE from M_+f=p'f and confirmed logarithmic divergence of the p-moment.
- Checked the dyadic-radii transfer and the symmetry-based noncompactness argument.

## Independent checks
- Compared with current public descriptions of arXiv:2609.12440 and searched for centered maximal nonattainment/near-eigenfunction/stability follow-ups.
- Separated the older uncentered eigenfunction literature from the centered sharp-constant problem.
- Reconstructed each inequality in the stability chain without relying on the repository’s same-model verdict.

## Evidence and literature
- https://arxiv.org/abs/2609.12440 — Madrid (2026), sharp centered Lp norm and extremizing sequences; direct source motivating the stability analysis.
- https://doi.org/10.4064/CM118-2-2 — Colzani and Pérez Lázaro (2010), eigenfunctions/nonattainment for the one-dimensional uncentered maximal operator.
- https://doi.org/10.1112/S0024609396002081 — Grafakos and Montgomery-Smith (1997), sharp uncentered maximal-function constant.
- https://doi.org/10.1007/BF02589410 — Hanner (1956), uniform convexity input.

## Limitations
- The stability exponent is not proved optimal and there is no spatial/multiscale classification of all extremizing sequences.
- The result is one-dimensional and the restricted-radii operator is Madrid’s centered geometric family, not the usual dyadic-grid maximal operator.
- Because the sharp centered theorem is very recent, a contemporaneous unindexed refinement remains a residual originality risk.

The assigned source tree remains exactly `4cacaca44b7325950f578995d47beb693a18a3b2` at current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; it matches the assignment guard. GitHub was used only as read-only evidence and no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific contract.
