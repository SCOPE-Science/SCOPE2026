# One-way 3-chain SEIR: source-endemic boundary classification with upstream autonomy and downstream driving

## Context

Multi-patch SEIR theory is most complete for irreducible (strongly connected) movement, where a scalar R0 governs a fully interior endemic equilibrium. Reducible movement, in which infection flows one way, produces boundary equilibria with some patches driven rather than self-sustained. This record resolves the admitted target for the 3-patch one-way chain 1->2->3: the ordered source-endemic boundary classification with upstream autonomy and downstream driving made explicit.

## Definitions

Patches j = 1,2,3 with compartments (S_j,E_j,I_j,R_j) >= 0 and mass-action incidence:

dS_j/dt = Lambda_j + phi^S_j - c^S_j S_j - beta_j S_j I_j
dE_j/dt = beta_j S_j I_j + phi^E_j - a_j E_j
dI_j/dt = sigma_j E_j + phi^I_j - b_j I_j
dR_j/dt = gamma_j I_j + phi^R_j - d^R_j R_j

Lambda_j > 0, d_j > 0, beta_j > 0, sigma_j > 0, gamma_j >= 0. One-way chain: per-class movement m^X_{jk} = 0 unless (j,k) in {(1,2),(2,3)}; inflows phi^X_1 = 0, phi^X_2 = m^X_{12} X_1, phi^X_3 = m^X_{23} X_2; outflows c^S_j = d_j + sum_k m^S_{jk}, a_j = sigma_j + d_j + sum_k m^E_{jk}, b_j = gamma_j + d_j + sum_k m^I_{jk}. R-equations are driven by (S,E,I) with strictly negative diagonal, so local asymptotic stability (LAS) of an (S,E,I) fixed point implies LAS in 12 dimensions.

Disease-free equilibrium (DFE): S^0_1 = Lambda_1/c^S_1, S^0_2 = (Lambda_2 + m^S_{12} S^0_1)/c^S_2, S^0_3 = (Lambda_3 + m^S_{23} S^0_2)/c^S_3, all E = I = R = 0. Next-generation patch numbers R0^(j) = beta_j S^0_j sigma_j/(a_j b_j).

## Result

Unique DFE; block lower-triangular next-generation matrix K with isolated diagonal blocks and rho(K) = max_j R0^(j). The DFE is LAS iff max_j R0^(j) < 1 and unstable iff max_j R0^(j) > 1. When R0^(1) > 1 with R0^(2), R0^(3) <= 1: there exists exactly one equilibrium with E1+I1 > 0, namely the patch-1 closed-form endemic point continued downstream by one quadratic per patch; it is LAS; and no equilibrium with E1+I1 = 0 < E2+I2+E3+I3 exists (hence none is stable). Strict downstream positivity E2+I2, E3+I3 > 0 holds iff each downstream link carries infected movement (m^E + m^I > 0); with zero infected movement the unique equilibrium has zero downstream infectives.

## Proof / evidence

DFE by forward substitution. With infected ordering (E1,I1,E2,I2,E3,I3), F = diag(F_11,F_22,F_33) and V block lower-triangular with diagonal V_jj; V is a nonsingular M-matrix, so K = F V^{-1} is block lower-triangular with K_jj = F_jj V_jj^{-1} and spectrum the union of diagonal-block spectra. DFE stability follows blockwise from van den Driessche-Watmough Theorem 2. Patch 1 is exactly autonomous with S1* = S^0_1/R0^(1), I1* = c^S_1(R0^(1)-1)/beta_1, E1* = b_1 I1*/sigma_1. For patch j given upstream equilibrium, T_j = Lambda_j + m^S S*_{j-1}, Phi^E_j, Phi^I_j, D_j = a_j Phi^I_j + sigma_j Phi^E_j >= 0 yield A_j I_j^2 + B_j I_j + C_j = 0 with A_j = a_j b_j beta_j > 0, C_j = -c^S_j D_j <= 0, hence exactly one admissible root I_j >= 0, forcing S_j, E_j, R_j. Monotone depletion S*_{j-1} <= S^0_{j-1} gives effective Rtilde_j <= R0^(j), so under R0^(2),R0^(3) <= 1 no self-sustained second root is positive. Root positivity is equivalent to D_j > 0. No-source-free nonexistence follows by induction: E1 = I1 = 0 forces patch 1 at DFE, D_2 = 0, then I_2 = E_2 = 0 and likewise patch 3. The full (S,E,I) Jacobian is block lower-triangular; each 3x3 diagonal block satisfies Routh-Hurwitz (a2 = (c+bI)(a+bb)+D/I > 0, a3 = a bb b I + cD/I > 0, a1a2 > a3, plus the I = 0 / Rtilde < 1 edge), so the source-endemic point is LAS. Numerics (numpy only): driven case R0 ~ (3.00,0.50,0.95) gives all-patch positive E,I, residual ~5e-16, endemic max Re ~ -0.078, DFE max Re ~ +0.34; all-R0<1 case DFE max Re ~ -0.011; zero-infected-movement case keeps uniqueness/LAS (max Re ~ -0.022) with downstream E = I = 0; 24 seeded damped-Newton runs converge only to the DFE and the constructed point.

## Limitations

Mass-action incidence with strictly positive recruitment and death; standard downstream-driven R-equations; local (not global) asymptotic stability; random Newton scans are uniqueness evidence within the sampled class, not a global proof.

## Reproducibility

Run output/artifacts/verify_chain.py (numpy only) to regenerate output/artifacts/verify_results.json with scenarios A (driven), B (stable DFE), C (zero infected driving).

## References

P. van den Driessche and J. Watmough, Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission, Math. Biosci. 180 (2002); L. Meng and W. Zhu, Generalized SEIR epidemic model for COVID-19 in a multipatch environment, Discr. Dyn. Nat. Soc. 2021 (nearest general n-patch scope, not covering); Q. Cui, Z. Qiu and L. Ding, An SIR epidemic model with vaccination in a patchy environment, Math. Biosci. Eng. 14 (2017) (nearest n=2 SIR boundary scope, not covering); Y. Li, Z. Shuai and P. van den Driessche-type irreducible multi-group theory (hypothesis-excluded by reducibility).
