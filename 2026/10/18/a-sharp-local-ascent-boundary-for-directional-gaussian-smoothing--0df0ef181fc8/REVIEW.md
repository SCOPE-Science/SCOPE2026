# Scientific review

## Correctness — PASS

The one-coordinate Gaussian derivative has the normalization \(F_i(z)=\mathbb E\partial_i f(z+\sigma Z e_i)\), so its Jacobian at the minimizer is exactly \(J=\delta I+a u^{\mathsf T}\), with \(a_i=u_i\mathbb E g''(\sigma u_iZ)\). Direct diagonalization of its symmetric rank-two part gives least eigenvalue \(\delta-\delta_*\). The isotropic second-order expansion of the original objective (using \(g''(0)=0\)) converts any negative symmetric direction into strict *finite-step* increase for every fixed \(h>0\). The stated example is globally \(\delta\)-strongly convex and smooth; exact inequalities \(c_1>1/3\), \(c_2<1/10\) prove the rational witness negative without numerical assumptions. The standalone verifier passed 63 integral, differentiation, eigenvalue and step checks; no finite test is presented as proof of a quantified infinite statement.

## Originality — PASS, residual risk recorded

The three primary works examined are arXiv:2002.03001 (operator, strongly convex convergence-to-neighborhood analysis), arXiv:2011.02009 (adaptive line search), and arXiv:2302.06404 (error-based convergence-to-neighborhood theorem). Their inspected material supplies the DGS definition but no local ascent threshold or analytical counterexample to every positive fixed stepsize near the unique minimum. General convergence-to-neighborhood bounds do not imply one-step monotonicity, so they neither cover nor contradict the finding. Targeted semantic searches for the source IDs, DGS, nonconservative smoothing, ascent and coordinate Gaussian convolution found no directly covering statement. A mathematically equivalent formulation in unexamined derivative-free optimization literature remains possible, and search absence is not a proof of novelty.

## Value — PASS

The natural practical question is whether globally smooth strong convexity makes the **exact** nonlocal DGS direction safe for fixed-step descent. The result gives an answer of a stronger form than a single failing step: a sharp general ridge-family boundary plus a concrete globally regular two-dimensional example where **every** positive fixed step increases the objective from some points arbitrarily close to its minimizer. It separates intrinsic directional-kernel geometry from numerical quadrature error and explains why a method may require descent safeguards even on strongly convex losses. The equality case and behavior of line searches or adaptive directions are not established.

## Closest work and boundaries

The 2020 DGS article's Appendix D proves error-controlled convergence toward a neighborhood, the 2023 analysis bounds the discrepancy from the true gradient, and the adaptive variant performs a line search. None is claimed erroneous, and a neighborhood guarantee can coexist with local objective increases. The result concerns the exact common-radius coordinate operator, not all Gaussian-smoothed optimizers or all practical implementations.

Self-review: passed. Independent audit: not yet performed.
