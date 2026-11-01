# Scientific assessment

## Correctness — PASS

The gamma beta integral gives the exact normalized monomial weights \(b_n=\sqrt{(n+1)/(n+\alpha+2)}\). The numerical radius equals the largest eigenvalue of the explicit symmetric tridiagonal compression by unitary rotation symmetry. Equation (1) of RESULT.md is an exact sum-of-squares identity; it supplies both the hard top-degree boundary condition and a coercive linear potential in the degree deficit. The upper variational bound is attained asymptotically by sampled smooth test functions. The lower bound follows by global discrete interpolation, tightness, compactness and weak lower semicontinuity. The resulting Dirichlet Airy eigenvalue and normalized eigenfunction establish the full asymptotic claim. The package checker passed 1922 finite supplementary assertions, but those tests are not a substitute for the variational proof.

## Originality — PASS, subject to historical priority

The closest weighted Bergman Toeplitz/Jacobi results of Simanek (arXiv:2001.07823) and Le–Simanek (arXiv:2003.07330) determine hyponormality thresholds for infinite weighted shifts plus diagonal Toeplitz operators. The Gorkin–Partington restricted shifts are Hardy model-space compressions, not weighted Bergman polynomial compressions. Lukic's eventually monotone Jacobi results concern infinite Jacobi spectral measures and edge-density asymptotics rather than a growing finite-section numerical radius. Sen et al. (arXiv:2502.02833) study full-space Toeplitz and composition operators. A related public Airy-edge result for geometrically damped periodic weighted shifts has a different parameter and coefficient geometry. No checked statement directly contains the displayed \(N^{-4/3}\) coefficient and the normalized degree-layer profile. A general finite-Jacobi turning-point theorem may nevertheless imply this result and remains an identified historical-priority risk.

## Mathematical value — PASS

Finite-degree polynomial compression is a natural approximation of a bounded analytic Bergman multiplier. The leading distance from unit numerical radius is of order \(N^{-1}\), but the next sharp term is governed by a boundary-layer Airy operator, and optimal polynomials concentrate on a nontrivial \(N^{2/3}\) degree scale. The exact coefficient and eigenvector limit answer a natural asymptotic extremal problem in analytic function spaces. At the adjacent Hardy endpoint, the behavior instead has order \(N^{-2}\), showing a genuine structural change rather than a routine finite calculation.

## Scope and limits

The theorem is for fixed \(\alpha>-1\) and the specific standard radial weights; no uniform \(\alpha\)-dependent error term or higher-eigenvalue result is claimed. Numerical tests check exact finite identities and convergence trends but not infinite quantifiers. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
