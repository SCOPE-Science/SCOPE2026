# same-model review

## Verdict

**PASS (same-model review only).** The contribution is assessed separately as correct, original to the best of our knowledge, and useful. This is not independent validation or peer review.

Same-model review: passed. Independent audit: not yet performed.

## Correctness audit

The proof was checked at the following failure points.

1. **First integral / chemical potential.** The stationary advection-diffusion equation is exactly \(\nabla\cdot(U\nabla(d\log U+\alpha V))=0\). Positivity of \(U\), homogeneous Neumann data, and connectedness force \(d\log U+\alpha V\) to be constant. The case \(\alpha=0\) is handled separately.
2. **Map elimination.** At a positive steady state, \(g_2(U)>0\) gives \(K=h(U)=g_1(U)/g_2(U)\), and the elliptic smoothing equation becomes \(-R^2\Delta V+V=h(U)\).
3. **Centering identity.** With \(z=\log U\) and \(w=V-\bar V\), the first integral gives \(z-\bar z=-(\alpha/d)w\). Multiplication of the centered elliptic equation by \(w\) yields the exact energy-covariance identity used in the theorem; all signs were rechecked for both \(\alpha>0\) and \(\alpha<0\).
4. **Covariance sign and Lipschitz estimate.** The double-integral covariance formula makes monotonicity and the bound by \(L\|z-\bar z\|_2^2\) immediate. No pointwise ordering of the spatial profiles is assumed.
5. **Poincare constant.** The quantitative bound uses the first nonzero Neumann eigenvalue \(\lambda_1\). On \((0,\pi)\), \(\lambda_1=1\), matching the source paper's Fourier wavenumber normalization.
6. **Sharp example.** For \(h(u)=u/(1+u)\), \(u h'(u)=u/(1+u)^2\) has global maximum \(1/4\) at \(u=1\). With \(g_2=1\), the source formula \(\alpha_1=(1+R^2)d w_{k_*}/(u_*w_{u_*})\) gives \(\alpha_1=-4d(1+R^2)\) at \(u_*=1\), exactly matching the global criterion from the stable side.

### Correctness limitations

The theorem excludes positive classical stationary patterns only. It does not prove dynamic convergence or nonlinear asymptotic stability, and the strict quantitative inequality does not settle the equality case in general. The multidimensional extension is for the displayed local elliptic-smoothing system; the source paper proves exact equivalence with its original nonlocal model in the one-dimensional even-periodic setting.

## Originality audit

### Existing SCOPE records

No current SCOPE record was located that covers this logarithmic-slope/covariance obstruction or its sharp saturating-memory specialization. Existing nearby differential-equation records concern different mechanisms, including a growth-weighted mutation chemostat and a Riccati linearization result.

### External literature checked

- **Salmaniw--Liu--Shi--Wang (J. Nonlinear Sci. 2026; arXiv:2503.11550).** The full accessible article states the local Neumann equivalent system and, in the no-growth section, derives the critical strengths \(\alpha_n(R)\). It identifies \(n=1\) as the first critical mode and carries out local stability/bifurcation analysis. No global uniqueness theorem for arbitrary-amplitude positive steady states, covariance identity, or logarithmic-slope criterion was located.
- **Shi (DCDS 2026), DOI 10.3934/dcds.2026134.** This recent review surveys pattern formation driven by nonlocal advection and time delays, emphasizing stability and bifurcation mechanisms. No theorem located in the review gives the criterion \(|\alpha|\sup u|h'(u)|<d(1+R^2\lambda_1)\) for the present spatial-memory feedback.
- **Wang--Salmaniw (J. Math. Biol. 2023), DOI 10.1007/s00285-023-01905-9.** This review frames knowledge-based animal movement and spatial-memory PDEs as an area with many open analytical questions; no covering theorem for the present stationary obstruction was located.
- Synonymous searches were also made around nonconstant steady-state exclusion, chemotaxis/aggregation steady states, logarithmic chemical potentials, Poincare thresholds, and the logarithmic slope \(u h'(u)\). Related nonexistence results exist for other chemotaxis systems, but no located statement was found to imply the theorem for this coupled spatial-memory model.

No specific inaccessible paper emerged as a uniquely high-risk originality candidate. The main residual risk is the broad older chemotaxis and aggregation-diffusion literature, where analogous energy methods may exist in a different model or notation. The claim of originality is therefore deliberately limited to **to the best of our knowledge**.

## Value audit

The result upgrades a local bifurcation picture to a global finite-amplitude exclusion region and identifies an exact structural mechanism: diffusion plus elliptic memory smoothing competes against the logarithmic slope of the equilibrium map response. The saturating feedback example is especially informative because the global uniqueness boundary coincides exactly with the first local bifurcation threshold, eliminating detached or subcritical positive steady branches throughout the entire linearly stable side. The criterion also extends naturally from the source interval to bounded connected domains through the Neumann spectral gap.
