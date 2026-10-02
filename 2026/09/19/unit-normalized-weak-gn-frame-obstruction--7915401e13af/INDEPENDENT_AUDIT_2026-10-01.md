# Independent mathematical audit — 2026-10-01

**Record:** SCOPE-20260919-7915401e13af — Unit-normalized weak Gauss–Newton can amplify energy error without bound
**Disposition:** PASSED

## Final claim assessed

In the weak Gauss--Newton measurement geometry, individual unit-energy normalization does not control the Euclidean least-squares metric: a fixed two-dimensional test span admits unit tests producing a correction \(1/\varepsilon\) and energy-error amplification \(\sqrt{1+\varepsilon^{-2}}\); the amplification has the stated exact Gram-condition-number law, while inverse-Gram weighting recovers the invariant energy projection.

## Correctness — PASS

With an energy-orthonormal pair \((\phi_1,\phi_2)\), the two unit tests are \(z_1=\phi_2\) and \(z_2=(\varepsilon\phi_1+\phi_2)/\sqrt{1+\varepsilon^2}\). Direct least squares gives \(\xi=(J^Tb)/(J^TJ)=1/\varepsilon\), decreases the measurement loss to \(1\), but changes the physical error norm from \(1\) to \(\sqrt{1+\varepsilon^{-2}}\). Diagonalizing the Gram matrix yields exactly \(\xi=\tfrac12(\sqrt\kappa-1/\sqrt\kappa)\) and amplification \(\tfrac12(\sqrt\kappa+1/\sqrt\kappa)\). A fresh independent numerical reconstruction at five \(\varepsilon\)-values reproduced these identities and zero Gram-weighted correction; the proof itself is algebraic, not empirical.

## Originality — PASS

RVPINNs already establish that classical variational residual losses depend on the chosen basis and that inverse-Gram discrete-dual-norm weighting removes that coordinate dependence; those general facts are excluded from the claim. The audited result is narrower and source-specific: even after individual energy normalization and with the test span fixed, the particular Euclidean weak Gauss--Newton step can increase the physical energy error without bound, with an exact condition-number law. Resultary returned no earlier published SCOPE statement of this fixed-span unit-normalized one-step obstruction. The motivating 2026 Gauss--Newton preprint was available only at abstract level, so later/full-text overlap remains a residual risk.

## Scientific value — PASS

This is a motivated counterexample/boundary for a new weak Gauss--Newton formulation: it shows that the seemingly natural safeguard of unit-normalizing tests does not control the algorithmic metric, and it quantifies the exact dependence on frame conditioning. It is not merely a restatement of the known Gram-inverse remedy.

## Originality comparison details

### Equivalent formulations

The standard frame-operator and dual-norm formulations were treated as equivalent background, while the claimed new object is the Gauss--Newton update/error amplification.

Searches:
- Resultary semantic search: weak Gauss Newton unit normalized test functions frame conditioning fixed span unbounded energy error Gram inverse Petrov Galerkin
- RVPINN full-text search for basis dependence, Gram inverse, discrete dual norm

Evidence:
- RVPINN full text explicitly states basis dependence of the classical loss and gives the loss \(\mathcal R^T G^{-1}\mathcal R\); the audited theorem instead fixes unit norms and the span and quantifies one-step Gauss--Newton energy amplification.

### Broader coverage

The prior robust-loss theory covers the remedy and broad mechanism but does not, in the inspected material, dominate the exact one-step counterexample.

Searches:
- Rojas et al., arXiv:2308.16910 full text
- Schwencke--Maier arXiv:2609.20641 abstract
- Resultary query listed above

Evidence:
- RVPINN lines on the classical loss say its stability depends on the basis and that inverse-Gram weighting yields a basis-independent dual norm; no inspected theorem gives the unit-normalized fixed-span \(1/\varepsilon\) Gauss--Newton error blow-up.
- The 2026 source abstract makes test choice an explicit design choice but does not state this obstruction.

### Exact database or table

This is an analytic counterexample rather than a tabulated invariant; database search was used only to locate prior published formulations.

Searches:
- Resultary query listed above

Evidence:
- The audited record was the only direct match among returned published findings; nearby hits concerned different optimization algorithms.

### Claim versus prior implication

The exact counterexample is not a literal corollary of the inspected RVPINN theorem statements without the additional construction.

Searches:
- direct implication comparison with arXiv:2308.16910 equations for classical and inverse-Gram losses

Evidence:
- Basis dependence under arbitrary rescaling does not by itself force unbounded physical-error amplification when every test is individually normalized and the span is fixed. The explicit nearly parallel frame and Gauss--Newton tangent geometry provide that stronger statement.

## Source inspections

### Robust Variational Physics-Informed Neural Networks

- Identifier: arXiv:2308.16910
- Trigger: Closest prior for basis dependence and Gram-inverse remedy
- Material read: Full accessible HTML: introduction and Sections 2--3 through the classical loss, basis-dependence discussion, Riesz representative, Gram system, and \(\mathcal R^T G^{-1}\mathcal R\) formula
- Method: Full-text web inspection
- Assessment: PARTIAL_COVERAGE
- Evidence: Covers basis dependence and the inverse-Gram discrete dual norm, not the audited unit-normalized fixed-span Gauss--Newton amplification law.

### Beyond PINNs: A Unified Gauss--Newton and Petrov--Galerkin Framework for Neural and Hybrid PDE Solvers

- Identifier: arXiv:2609.20641
- Trigger: Exact motivating method
- Material read: Primary abstract; full arXiv page could not be fetched
- Method: Open arXiv/web inspection
- Assessment: UNRESOLVED_FULLTEXT_RISK
- Evidence: Abstract confirms finite linear measurements, test-function representation, Petrov--Galerkin Gauss--Newton, and weak elliptic formulations.

## Limitations and residual risks

- The theorem is a worst-case fixed-span counterexample, not a claim that the motivating experiments fail.
- The full current motivating preprint was not retrievable through the available open route; later/full-text discussion of conditioning remains a residual originality risk.
