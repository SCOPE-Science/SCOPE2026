---
audit_date: 2026-10-01
status: repaired
---

# Scientific audit

## Final claim

Under the smooth uniformly convex quadratic-cost hypotheses of González-Sanz and Nutz, let \(\ell=\varepsilon^{1/(d+2)}\). For all sufficiently small \(\varepsilon\), a fixed positive-slack core has coercivity of order \(\varepsilon\); consequently the quadratically regularized transport dual is uniformly strongly concave on an \(L^\infty\) direct-sum neighborhood of radius \(\Theta(\ell^2)\), has local \(L^2\)-gradient Lipschitz scale \(O(\ell^{-2})\), and satisfies an \(\varepsilon\)-uniform local Polyak--Łojasiewicz inequality and quadratic growth there. The previously claimed optimizer Hessian condition-number asymptotics are removed because that spectral statement was already publicly covered by an earlier result.

## Correctness — PASS

The repaired claim was reconstructed without using the removed spectral theorem. The geometry input gives positive-slack row and column sections of radius \(\Theta(\ell)\), section masses \(\Theta(\ell^d)\), and overlap for nearby rows. Minimizing over the opposite endpoint converts the core quadratic form to a finite-range variance form; the finite-range Poincaré scale is \(\ell^{d+2}=\varepsilon\). The normalized core marginals have densities bounded above and below, so the mean direct-sum component is controlled at the same scale. Hence the core form is at least \(c\varepsilon\|u\oplus v\|_2^2\). If \(\|h-h_\varepsilon\|_\infty\le\rho\ell^2\) with \(\rho\) below the core slack threshold, that same core remains active along every segment in the neighborhood; integrating the almost-everywhere second derivative yields uniform strong concavity. The active sections remain \(O(\ell^d)\), giving local smoothness \(O(\ell^{-2})\). Strong concavity then gives the stated PL and quadratic-growth bounds.

**Checked sources.** Assigned RESULT.md at source tree 749133b8ff5640d2c3a1749e67ac771f5d0b96af; González-Sanz and Nutz, Geometry and Convergence of Quadratically Regularized Optimal Transport I, arXiv:2609.20400; González-Sanz, Nutz and Riveros Valdevenito, Polyak--Łojasiewicz Inequality for Quadratically Regularized Optimal Transport, arXiv:2605.27175; González-Sanz, Nutz and Riveros Valdevenito, Linear Convergence of Gradient Descent for Quadratically Regularized Optimal Transport, arXiv:2509.08547

**Residual risks.** Full arXiv HTML for the three recent primary papers was unavailable through the web route in this run, so the exact geometry-lemma wording was cross-checked against the frozen assigned proof and the accessible abstracts rather than re-extracted from the PDFs.

## Originality — PASS

The original package mixed a genuinely additional robust-neighborhood theorem with a spectral-conditioning statement already covered by an earlier public result. The repaired claim removes that covered part. Searches located no earlier theorem asserting the fixed positive-slack core coercivity together with \(\Theta(\varepsilon^{2/(d+2)})\)-radius uniform strong concavity and the resulting uniform local PL bound.

### Equivalent formulations

The repaired statement is not equivalent to the already-covered optimizer Hessian theorem: it requires one fixed positive-slack core to remain active throughout a natural-scale neighborhood and therefore controls nonlinear dual curvature away from the optimizer.

### Broader coverage

Neither broad result mechanically gives persistence of a common active core throughout the claimed \(L^\infty\) ball; that persistence is the extra structural step.

### Exact database or table

No numerical database or table controls this infinite-dimensional analytic claim; the exact-database check is therefore a search for theorem-level duplicate records.

### Claim versus prior implication

The prior spectral result does not imply the repaired claim because optimizer active-set coercivity alone does not persist after perturbing the potentials; the positive-slack core argument is essential.

**Checked sources.** https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-sharp-qot-dual-linearization-conditioning--e80a70cb7832; https://arxiv.org/abs/2609.20400; https://arxiv.org/abs/2605.27175; https://arxiv.org/abs/2509.08547

**Residual risks.** The unavailable contemporaneous Part II working paper is a genuine residual overlap risk, but no public text was located and it does not override the resolved prior coverage of the spectral component. Parallel very recent work may not yet be indexed.

## Scientific value — PASS

After removing the covered spectral statement, the surviving theorem still identifies a natural \(\Theta(\varepsilon^{2/(d+2)})\) potential neighborhood on which the dual has an \(\varepsilon\)-uniform curvature modulus. This is a motivated nonlinear optimization consequence of the new support geometry: it upgrades a local PL picture with deteriorating constants and supplies a robust region in which standard first-order analysis applies.

**Residual risks.** The theorem remains local and does not establish that an algorithm enters the neighborhood.

## Limitations

- The result requires the smooth positive-density uniformly convex continuous quadratic-cost setting and sufficiently small \(\varepsilon\).
- The neighborhood is local in the direct-sum \(L^\infty\) norm; no global basin-entry or invariance theorem is claimed.
- The contemporaneous working paper titled Geometry and Convergence of Quadratically Regularized Optimal Transport II was cited by the source geometry paper but no public full text was located, so some overlap risk remains.

## Disposition

REPAIRED. Acceptance requires all three scientific axes to pass.
