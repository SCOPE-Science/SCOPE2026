# Mathematical review: degenerate diffusive-boundary Hopf unfolding

## Correctness — PASS

The branch exists and is smooth by Pelz–Scheel, Theorem 1.4. At the stated critical cubic coefficient, its published third-order formula gives precisely \(m_2=0\), \(w_2=-7/6-3g/4\). A mode-by-mode recurrence through fifth order follows from the exact Dirichlet-to-Neumann multiplier \(\sqrt{ij\omega}\), with a constant far-field mode and zero first-harmonic corrections. The fourth-order multiplier expansion includes the \(\sqrt2\sqrt i\,w_2^2/8\) term. The coefficient of \(R^4\) is enclosed using integer-directed interval arithmetic: \(0.70584603791928416421<K<0.70584603791928416422\). Rescaling gives \(K\beta^4/\alpha^{7/2}\). The code checks the finite algebraic stage; analytic existence and smoothness are imported explicitly from the source.

## Originality — PASS under inspected evidence

The motivating paper computes the quadratic unfolding and the critical value where it vanishes, while its orbital-stability theorem is stated only for strict nonzero signs. The fifth-order coefficient and fourth-root law at equality are not specified in its inspected full text. Scientific searches for fifth-order degenerate Hopf coefficients in this particular diffusion-mediated boundary model and published-results searches did not reveal equivalent coverage. An August 2026 continuation treats a two-boundary configuration and its abstract does not supply this single-boundary coefficient. A broader historical or later computation may exist; that priority risk remains.

## Value — PASS

This is the natural missing endpoint between supercritical and subcritical Hopf branches in a diffusion-coupled scalar boundary model. The sign resolves which side of the bifurcation parameter contains small cycles exactly at the cubic degeneracy. The quartic parameter scaling and its explicit coefficient are quantitative information unattainable from the source's cubic-order result. No stability classification or global cycle census is asserted.

## Closest literature and limits

Pelz–Scheel (arXiv:2604.01135v1), Theorem 1.4, Corollary 3.3 and Section 4 provide branch existence, nondegenerate coefficients and stability outside the critical surface. The later Pelz paper (arXiv:2608.08537v1) concerns two dynamic boundaries; only its abstract was accessible. The finite algebraic checker cannot prove the cited infinite-dimensional existence theorem or orbital stability.

Self-review: passed. Independent audit: not yet performed.
