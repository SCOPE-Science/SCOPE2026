# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** Substitution of the separable quadratic into the published predictor--feedback--corrector updates gives the stated two-dimensional linear recurrence. The determinant identity is an exact cancellation. For kappa_x=1, the characteristic discriminant was reduced symbolically to a degree-nine polynomial on s=1/sqrt(kappa) in (0,1]; an exact Bernstein-basis reconstruction has ten strictly positive coefficients for the negative of that polynomial, proving the discriminant is strictly negative throughout the claimed interval. The spectral-radius formula follows from conjugate roots and det(M)=alpha A. Independent direct eigenvalue evaluations reproduce the formula and the asymptotic constants. The sinusoidal last-iterate formula follows from the second-order recurrence and its initial values.

Adversarial checks included the kappa=1 endpoint, large-kappa limits, the defective limiting matrix, and direct recurrence simulation. The fixed-kappa_x extension was rederived with a three-coordinate uncoupled quadratic whose full-gradient Lipschitz constant is exactly L=1 and whose primal strong-convexity constant is exactly 1/kappa_x.

## Originality

**PASS, to the best of our knowledge.** The motivating source, arXiv:2609.20327v1, was inspected at the theorem, algorithm, parameter, and numerical-experiment levels. It gives a Lyapunov contraction and last-iterate complexity bound but does not state a quadratic spectral-radius analysis, an underdamped/near-Jordan description, the exact constants above, or the first-sign-reversal law.

Searches by source identifier, title, algorithm description, quadratic/spectral terminology, and equivalent underdamped language found no public correction or analysis containing these source-specific formulas. No overlapping SCOPE record was located under the source identifier or the relevant claim family.

Generic quadratic spectral analysis and underdamped acceleration are prior art and are expressly excluded from the novelty claim. Related accelerated-minimax literature establishes rate-optimality for other algorithms and structures, but no inspected source implied the displayed matrix and constants for this newly introduced feedback recursion.

A relevant residual-risk source is Yoon--Ryu, *Accelerated Minimax Algorithms Flock Together* (SIAM J. Optim. 35(1), 2025, DOI 10.1137/22M1504597). Its abstract and bibliographic material were inspected, but the complete article text was not. It could contain a sufficiently general acceleration mechanism that subsumes part of the qualitative interpretation; because it predates arXiv:2609.20327, it cannot explicitly contain the source-specific recurrence unless the new method is shown to reduce to an older template. The newly submitted preprint itself also creates a contemporaneous-follow-up risk.

## Value

**PASS.** The result distinguishes two issues that the source theorem leaves combined. First, the square-root condition-number dependence is not merely a Lyapunov-proof artifact: it appears in the exact spectral radius of the prescribed algorithm on an elementary separable family. Second, the additional logarithmic condition-number factor in the theorem is not intrinsic on that family; a direct last-iterate envelope has a condition-number-independent prefactor. The exact phase constant further explains why finite trajectories can cross the saddle well before their spectral envelope has strongly decayed.

## Limitations

The construction is separable and source-specific. It is not an oracle lower bound, does not show that coupled problems behave identically, and does not optimize the published parameters. The all-kappa discriminant certificate is for kappa_x=1; arbitrary fixed kappa_x is treated asymptotically. The sign-reversal law concerns trajectory geometry rather than a stopping guarantee.
