# Independent Audit — 2026-09-29

**Record:** `2026/09/20/cauchy-trust-region-optimal-decrease-ratio--0eec6412acfe`  
**Title:** Sharp fraction-of-optimal decrease for the SPD Cauchy trust-region point  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `3561a9ff2f8b89dc7b4f9f91831162aaf3464310`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The proof is valid in both Cauchy regimes. When the Cauchy point is untruncated, comparison with the unconstrained Newton decrease gives 1/[(u^TBu)(u^TB^{-1}u)]. On the boundary, the desired domination is affine in normalized radius; its endpoints follow from K>=1 and weighted Cauchy–Schwarz plus AM–GM. Kantorovich yields 4kappa/(kappa+1)^2, and the two-eigenvalue equal-energy example attains equality once both unconstrained steps are feasible.
- **Originality — PASS:** Classical trust-region sources distinguish fraction-of-Cauchy from fraction-of-optimal decrease, and the unconstrained Kantorovich steepest-descent/Newton ratio is classical. Focused searches did not locate the filed radius-uniform inequality or the resulting sharp SPD conversion for every trust radius. The claim is therefore a plausible new bridge, with residual risk of an older equivalent lemma under different trust-region terminology.
- **Scientific value — PASS:** The theorem turns a standard inexpensive Cauchy benchmark into a sharp fraction-of-optimal certificate whenever the quadratic model is SPD, including a metric/preconditioned form. It also cleanly identifies why no positive conditioning-independent analogue survives for indefinite models.

## Independent findings
- Re-derived the affine endpoint inequality F(tau)>=0 on [0,1/q].
- Checked the fixed-(B,g) equality condition when both Newton and Cauchy unconstrained minimizers are feasible.
- Checked the Kantorovich equality family B=diag(mu,L) with equal squared gradient energy in the extreme eigenspaces.
- Checked the fraction-of-Cauchy sharpness construction using a point on the Cauchy segment with 2x-x^2=gamma.

## Independent checks
- Compared the statement with classical Cauchy-point and fraction-of-optimal terminology in Conn–Gould–Toint and Conn–Scheinberg–Vicente.
- Searched the exact condition-number factor together with trust-region/Cauchy/Kantorovich formulations; no radius-uniform equivalent theorem was located.
- Rechecked the metric change of variables and the indefinite diagonal counterexample.

## Evidence and literature
- https://doi.org/10.1137/1.9780898719857.ch7 — Conn, Gould and Toint, classical trust-region/Cauchy-point background.
- https://doi.org/10.1137/060673424 — Conn, Scheinberg and Vicente, explicit distinction between fraction-of-Cauchy and stronger fraction-of-optimal decrease conditions in general trust-region analysis.
- https://doi.org/10.1016/j.jmaa.2013.01.015 — A modern source recalling the classical vector Kantorovich inequality used for the sharp condition-number envelope.

## Limitations
- Originality is qualified by the breadth of older trust-region literature and possible synonymous formulations.
- The theorem concerns exact predicted reduction for finite-dimensional real SPD quadratics; it is not an actual-reduction, runtime, or floating-point-stability result.
- The quality factor can be very small for ill-conditioned B and no analogous positive universal bound holds for indefinite models.

The assigned source tree remains exactly `3561a9ff2f8b89dc7b4f9f91831162aaf3464310` at current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; it matches the assignment guard. GitHub was used only as read-only evidence and no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific contract.
