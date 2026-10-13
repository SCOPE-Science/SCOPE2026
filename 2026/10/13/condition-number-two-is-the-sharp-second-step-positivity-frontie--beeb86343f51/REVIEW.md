# Self-review

## Correctness
PASS. The second exact GMRES iterate on a diagonal SPD problem has the form
\[
x_2=ab-cAb.
\]
Residual orthogonality gives two exact moment equations. Solving them yields \(c>0\), while
\[
\frac ac
\]
is exactly a positive weighted average of pair sums
\[
\lambda_i+\lambda_j.
\]
Therefore
\[
\frac ac\ge2\mu,
\]
so every coordinate of \(x_2\) is nonnegative whenever \(L\le2\mu\).

For every \(\kappa>2\), the displayed three-eigenvalue family and explicit bound on the third right-hand-side weight make \(a/c<\kappa\), forcing the top-eigenvalue coordinate negative. One- and two-point active spectra terminate exactly by step two, so the edge cases and minimal dimension are accounted for.

The embedded verifier independently replays the pairwise identities and the exact \(\kappa=3\) witness using rational arithmetic.

## Originality
PASS. Classical sources establish GMRES residual-polynomial minimization, harmonic Ritz roots, and explicit residual-polynomial coefficients. The inspected literature does not state a componentwise second-iterate positivity threshold, and targeted searches using both GMRES and MINRES terminology found no implication-equivalent condition-number frontier.

The closest prior phenomena concern residual norms, harmonic Ritz values, or isolated sign-loss examples. They do not imply the universal safe region \(\kappa\le2\) together with a three-dimensional counterexample for every \(\kappa>2\).

Residual risk remains that older pseudo-Ritz or orthogonal-polynomial literature records the same pair-sum consequence under different terminology.

## Value
PASS. The theorem gives a sharp, dimension-free safety condition for orthant preservation at the first nontrivial residual-minimizing step on diagonal SPD systems. It distinguishes residual monotonicity from physically meaningful sign preservation and identifies the minimal spectral complexity needed for failure.

The weighted pair-sum representation is structural and reusable: it explains both the safe side and the exact onset of possible negativity rather than merely supplying a counterexample.

## Closest literature and limitations
The closest published sources are the classical harmonic-Ritz interpretation of GMRES residual polynomials, explicit normal-matrix residual formulas, and later early-iteration coefficient formulas. None of the inspected statements covers the componentwise threshold.

The theorem is limited to exact arithmetic, the second iterate, diagonal SPD matrices, and nonnegative right-hand sides. Later iterates, arbitrary SPD coordinate bases, general Stieltjes matrices, preconditioning, restarting, and finite precision remain outside the claim.

Self-review: passed. Independent audit: not yet performed.
