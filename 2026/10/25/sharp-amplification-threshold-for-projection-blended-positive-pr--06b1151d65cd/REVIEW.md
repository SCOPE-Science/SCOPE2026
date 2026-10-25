# Scientific review

**Correctness — PASS.** The exact centered-ball inequality \(\|(F-qI/2)u\|_2\le(q/2)\|u\|_2\) follows from \(F^2\preceq qF\), and similarly for \(G\). Orthogonality of \(Pu\) and \((I-P)u\) gives the universal upper bound. Two rank-one projectors attain the constant in dimension two; a strictly positive-definite perturbation crosses the threshold. An exact-rational same-ODE backward-Euler example has strictly positive Euclidean norm excess while similar to a Hermitian matrix with eigenvalues in \((0,1)\). The standalone checker corroborates arithmetic; analytical derivations establish the universal statement.

**Originality — PASS, with risks.** The blended map itself is explicit prior work of Tan et al., with a historical antecedent in Gander and Petcu. Tan et al.'s nonlinear iteration-dependent bounds and Jin–Lin–Zhou's scalar spectral parareal factors do not state or dominate the sharp arbitrary-projection PSD norm envelope. Claim-level mathematical record searches for the equivalent map, positivity, exact constant, and backward-Euler resolvents found noncovering records. The full historical Gander–Petcu paper was not inspected, and unindexed generic operator inequalities could overlap: these are residual risks, not assertions of conclusive absence.

**Mathematical value — PASS.** Strict spectral contraction of both solvers is not sufficient to prevent one-step norm growth after splitting across an arbitrary projection; the exact universal damping threshold and a rigorously nondivergent, same-ODE example explain the distinction for stability-oriented method design. This is a sharp structural property, not an arbitrary scalar exercise.

The result is a local linear operator-norm theorem. It does not invalidate finite-step exactness or guarantee full parareal divergence, and does not solve nonlinear or history-dependent stability.

Self-review: passed. Independent audit: not yet performed.
