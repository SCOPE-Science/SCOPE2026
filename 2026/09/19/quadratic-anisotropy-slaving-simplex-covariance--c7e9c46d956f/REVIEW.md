# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The result is a refinement of the closed covariance system in arXiv:2609.16978v1. The proof uses four ingredients that are either exact or already established in the source: the preserved covariance eigenbasis, the exact pairwise eigenvalue-difference formula, exponential convergence to the isotropic covariance in the subcritical regime, and the exact mean-eigenvalue equation.

The new asymptotic step is checked as follows. Exponential convergence makes the deviation of the pairwise exponent integrand from its limit integrable, so every quantity `exp(alpha_perp t)(lambda_i-lambda_j)` has a finite limit; at least one limit is nonzero for anisotropic initial covariance. The centered elementary-symmetric expansion has no linear traceless term and has quadratic term `-C(d-2,n-2)||delta||^2/2`. Substitution into the exact mean equation gives a positive quadratic forcing coefficient. For 2 <= n < d,

\[
\alpha_\parallel-2\alpha_\perp
=4c_n\binom{d-2}{n-2}\lambda_*^{n-1}
\frac{d(n-2)+n}{n-1}>0,
\]

so the stable isotropic mode is faster than the quadratic forcing. Variation of constants therefore yields the stated `2 alpha_perp` mean correction and coefficient. Substitution of that coefficient back into the elementary-symmetric expansion gives the positive interaction-energy coefficient. No differentiation of an asymptotic equivalence or numerical extrapolation is used in the proof.

The compact verification artifact independently redoes the coefficient algebra, checks the centered polynomial expansion in finite dimensions, and numerically integrates a representative covariance ODE. The numerical check is supporting evidence only, not independent validation.

## Originality

**PASS, to the best of our knowledge, with a narrow claim.** The covariance representation of the simplex-volume functional, the finite-dimensional reduction, equilibrium classification, and sharp first-order exponential rates are prior results and are excluded from the novelty claim. General stable-manifold and mode-slaving ideas are also standard and are not claimed as new.

The source paper arXiv:2609.16978v1 was read at the theorem and proof level. In Proposition 5.2 and Corollary 5.1 it proves the centered remainder only as `O(D(t)^2)`, obtains a scalar forcing bounded by `O(exp(-2 alpha_perp t))`, and then records only the first-order covariance rate. It does not state the nonzero limiting anisotropy amplitude, the universal ratio between mean excess and squared anisotropy, the eventual positive sign of the mean excess, or the corresponding exact interaction-energy tail.

The authors' nondiffusive predecessor arXiv:2606.21918 was also inspected. It concerns rank collapse without diffusion and sharp rates in different spectral regimes; it does not contain the diffusive isotropic equilibrium or the quadratic trace-recoil law derived here.

External searches used the exact source identifier and title together with combinations of `anisotropy`, `mean covariance`, `trace`, `quadratic`, `second order`, `interaction energy`, `simplex volume`, and equivalent covariance-asymptotic terminology. No public source-specific correction, comment, or earlier statement of the coefficient formulas in this record was found. Repository searches by source identifier and claim terminology found no prior SCOPE record covering this contribution. The source is a very recent v1, so unindexed author notes or discussions remain a residual originality risk. A more general invariant-manifold theorem could imply existence of a quadratic slaving relation abstractly, but no located source supplies these simplex-specific coefficients, signs, or energy consequence.

No inaccessible paper was identified as a close source-specific candidate likely to overturn the originality assessment. The older generalized-variance literature establishes the covariance representation and related dispersion identities, not this diffusive long-time dynamical expansion.

## Value

**PASS.** The source already shows that anisotropic covariance relaxes more slowly than the isotropic linear mode. The new result explains what the fast scalar mode actually does under anisotropic forcing: it is slaved quadratically to the slow traceless mode, with a universal amplitude-free ratio. This produces a sign-definite consequence—eventual approach of the mean covariance from above—and an exact leading correction for the interaction energy. It also isolates a genuine distinction between pairwise interaction (`n=1`) and multipoint simplex interactions (`n>=2`).

## Limitations

The theorem is restricted to anisotropic initial covariance and 2 <= n < d. It is a covariance-level asymptotic statement; it does not determine the second-order asymptotics of the full measure in Wasserstein distance, where transport memory can introduce another decay mechanism. The critical case n=d and the isotropic invariant family require separate analyses. The originality assessment is to the best of our knowledge and is not independent validation.
