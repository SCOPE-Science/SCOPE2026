# Review status

Independent audit completed on 2026-10-01 (UTC).

Disposition: **PASSED**.

## Correctness — PASS

With an energy-orthonormal pair \((\phi_1,\phi_2)\), the two unit tests are \(z_1=\phi_2\) and \(z_2=(\varepsilon\phi_1+\phi_2)/\sqrt{1+\varepsilon^2}\). Direct least squares gives \(\xi=(J^Tb)/(J^TJ)=1/\varepsilon\), decreases the measurement loss to \(1\), but changes the physical error norm from \(1\) to \(\sqrt{1+\varepsilon^{-2}}\). Diagonalizing the Gram matrix yields exactly \(\xi=\tfrac12(\sqrt\kappa-1/\sqrt\kappa)\) and amplification \(\tfrac12(\sqrt\kappa+1/\sqrt\kappa)\). A fresh independent numerical reconstruction at five \(\varepsilon\)-values reproduced these identities and zero Gram-weighted correction; the proof itself is algebraic, not empirical.

## Originality — PASS

RVPINNs already establish that classical variational residual losses depend on the chosen basis and that inverse-Gram discrete-dual-norm weighting removes that coordinate dependence; those general facts are excluded from the claim. The audited result is narrower and source-specific: even after individual energy normalization and with the test span fixed, the particular Euclidean weak Gauss--Newton step can increase the physical energy error without bound, with an exact condition-number law. Resultary returned no earlier published SCOPE statement of this fixed-span unit-normalized one-step obstruction. The motivating 2026 Gauss--Newton preprint was available only at abstract level, so later/full-text overlap remains a residual risk.

## Scientific value — PASS

This is a motivated counterexample/boundary for a new weak Gauss--Newton formulation: it shows that the seemingly natural safeguard of unit-normalizing tests does not control the algorithmic metric, and it quantifies the exact dependence on frame conditioning. It is not merely a restatement of the known Gram-inverse remedy.

## Residual originality risks

- The full current arXiv:2609.20641 text was not retrievable through the available open route; a revision could discuss conditioning more explicitly.
