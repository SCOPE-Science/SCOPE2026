# Review: Hermite–Hellmann–Feynman extrapolation for constrained eigenvalue penalties

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** In an orthogonal range/null-space basis, the penalized eigenvalue equation has the Schur form
\[
D-\lambda I-E^T(B+\rho C-\lambda I)^{-1}E.
\]
With \(t=1/\rho\), the inverse admits a convergent local matrix power series. At a simple eigenvalue \(\lambda_*\) of \(D\), the determinant has nonzero derivative with respect to \(\lambda\), so the analytic implicit-function theorem gives an analytic branch \(F(t)=f(1/t)\) through \(F(0)=\lambda_*\). Expanding the Schur complement and applying standard simple symmetric-eigenvalue perturbation gives the stated coefficients \(-w^TGw\) and
\[
w^TJw-\sum_{j\ne *}|w_j^TGw|^2/(\lambda_j-\lambda_*).
\]

Hellmann–Feynman gives \(f'(\rho)=\|Ax_\rho\|_2^2\), hence \(F'(1/\rho)=-\rho^2f'(\rho)\). The standard Hermite remainder at zero then contains \(\prod_j t_j^2\), proving \(O(\rho^{-2q})\) for fixed distinct scale factors. Direct polynomial cancellation verifies the explicit two-level formula. The uniqueness statement is limited to coefficient-blind linear estimators and follows from nonsingularity of the confluent Vandermonde system for exactness on degrees \(0,\ldots,2q-1\).

The verification artifact checks the block coefficient formulas and the explicit two-level identity on a concrete symmetric example. The scaled fourth-order error approaches a nonzero constant over the displayed asymptotic range, showing that the fourth-order term need not vanish on constrained-eigenvalue penalty paths.

## Originality

**PASS, to the best of our knowledge.** The motivating source arXiv:2609.18538 was inspected for the exact penalty representation, finite-recovery criterion, first-order asymptotic expansion, Hellmann–Feynman sensitivity, value-only two-level Richardson correction, and one-level sensitivity correction. Those contributions are explicitly treated as prior. The present claim is restricted to the analytic inverse-penalty branch in the simple case, the explicit second coefficient, the general q-level Hermite–Hellmann–Feynman order-doubling rule, the closed two-level fourth-order formula, and its coefficient-blind linear polynomial-exactness characterization.

Hermite interpolation, Richardson extrapolation, simple-eigenvalue perturbation theory, and the Hellmann–Feynman theorem are classical and are not novelty claims. Searches covering `constrained eigenvalue` or `constrained Rayleigh quotient` together with `penalty`, `Hellmann-Feynman`, `Hermite extrapolation`, `derivative-assisted Richardson`, `confluent Richardson`, and synonymous inverse-penalty formulations did not identify a prior source stating the present combination. The SCOPE archive was also searched by source identifier, projected-Hessian terminology, penalty extrapolation, and derivative/Hermite formulations; no overlapping accepted record was found.

The older Ilanko–Williams paper (DOI 10.1002/nme.2247) is a plausible residual source because it studies eigenvalue convergence under large positive and negative penalty parameters in structural systems. Its accessible abstract establishes bracketing and convergence but does not expose the detailed higher-order asymptotics, and the full text was not inspected here. That leaves a residual originality risk for specialized structural-penalty asymptotics. The Zhou–Bai–Li constrained Rayleigh quotient paper (DOI 10.4208/csiam-am.2021.nla.01) was checked at the abstract/formulation level; it focuses on equivalent constrained formulations and Krylov algorithms rather than this penalty-path derivative extrapolation. The motivating preprint is also very recent, so contemporaneous or not-yet-indexed follow-up remains possible.

## Value

**PASS.** The source's first-order penalty law explains why large penalties are needed when finite exactness fails. The present extrapolation uses derivative information already supplied by a computed penalized eigenpair to remove twice as many inverse-power terms per penalty level as value-only polynomial extrapolation. In particular, two penalty eigenpair solves support a fourth-order scalar estimate rather than the source's two-level second-order value estimate. When the surviving coefficients are nonzero, this reduces the asymptotic penalty scale needed for target scalar error from \(\Theta(\epsilon^{-1/2})\) for the two-level value-only correction to \(\Theta(\epsilon^{-1/4})\) for the two-level Hermite-HF correction. This can be useful when very large penalties degrade the numerical separation of constrained and range modes, although no computational-complexity or conditioning theorem is asserted.

## Limitations

The proof requires a simple constrained eigenvalue and sufficiently large positive penalty in the non-finitely-exact regime. Multiple or crossing eigenvalue branches are outside the theorem. The estimator is asymptotic, not a certified upper/lower bound, and derivative terms multiplied by the penalty can amplify finite eigensolve error. No backward-stability analysis, adaptive penalty-selection theory, or end-to-end complexity result is provided. The maximum-eigenvalue path is analogous after a sign change but is not developed. The optimality statement concerns coefficient-blind linear extrapolators for arbitrary analytic inverse-power expansions and does not exclude nonlinear or structure-specific estimators.
