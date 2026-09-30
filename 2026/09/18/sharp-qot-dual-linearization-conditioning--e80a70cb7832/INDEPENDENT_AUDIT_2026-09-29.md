# Independent Audit — 2026-09-29

**Record:** `2026/09/18/sharp-qot-dual-linearization-conditioning--e80a70cb7832`  
**Title:** Sharp small-regularization conditioning of the QOT dual linearization  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `e79ad797f32e33a281daa80cf8eda2a7c05ec22d`  
**Disposition:** **PASSED**

## Independent checks

- Verified that H_oplus removes the (1,-1) gauge direction while retaining the common-constant stiff mode.
- Verified 1_A >= c ell^d k from k <= C ell^-d 1_A and the resulting lower support form.
- Verified that u=phi, v=-phi o S has equal zero means and O(ell) variation over the localized support.

## Three-axis assessment

- **Correctness — PASS**: The spectral scaling proof is internally consistent. Pulling the optimal density back by the Brenier map gives a doubly stochastic Markov kernel. The local overlap/Poincare input yields an order-ell^2 gap for KK*, hence an order-ell^2 lower bound for the density-weighted (u+b)^2 energy on the gauge-fixed space. The pointwise density ceiling converts this to an unweighted support energy of order ell^(d+2)=epsilon, while row/column section volumes give the order-ell^d upper support bound. Dividing by epsilon yields soft curvature O(1) and stiff curvature O(ell^-2), and the constant and transport-canceling Lipschitz modes match both spectral orders.
- **Originality — PASS**: The public Part I geometry paper provides the ell=epsilon^(1/(d+2)) support geometry and overlap/Poincare ingredients, and the earlier linear-convergence paper identifies the optimizer linearization, but targeted searches did not locate the sharp two-sided condition-number law or matching spectral-edge witnesses. The cited companion Part II remains nonpublic/uninspectable; no claim is made about its contents.
- **Scientific Value — PASS**: The result turns qualitative local contraction into a sharp stiffness law and determines the scalar-step local iteration exponent epsilon^(-2/(d+2)). This is a useful numerical-analysis consequence of the new geometry and clearly separates optimizer-local conditioning from the smaller step required for a global nonlinear theorem.

## Findings

- Current source tree exactly matches the assigned SHA.
- Independently rederived the mean/mean-zero energy decomposition and the use of ||K||_{L2_0}<1-c ell^2.
- Independently checked both spectral-edge witnesses and the scalar-step rate calculation.
- Searches found no public copy of the cited Geometry and Convergence of Quadratically Regularized Optimal Transport II.

## Sources compared

- Gonzalez-Sanz and Nutz, Geometry and Convergence of Quadratically Regularized Optimal Transport I: https://arxiv.org/abs/2609.20400 — Supplies the small-epsilon support scale and local/nonlocal geometric estimates used by the record.
- Gonzalez-Sanz, Nutz, Riveros Valdevenito, Linear Convergence of Gradient Descent for Quadratically Regularized Optimal Transport: https://arxiv.org/abs/2509.08547 — Supplies the optimizer linearization and qualitative contraction context.
- Gonzalez-Sanz, Nutz, Riveros Valdevenito, Polyak-Lojasiewicz Inequality for Quadratically Regularized Optimal Transport: https://arxiv.org/abs/2605.27175 — Related quantitative curvature work, but no matching sharp smooth-marginal conditioning law was located.

## Limitations

- The theorem is optimizer-local and does not establish global nonlinear convergence at the larger local step size.
- It is restricted to the smooth continuous quadratic-cost regime and sufficiently small epsilon.
- A cited 2026 companion working paper, Part II, was not publicly available for inspection; originality relative to inaccessible material is necessarily qualified.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
