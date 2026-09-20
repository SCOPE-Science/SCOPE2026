# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The first claim is an identity. For the displayed shift
\[
s=-\widehat\lambda+\eta,
\]
the shifted minimum eigenvalue is
\[
\lambda_{\min}(Q+sI)
=
\eta-\bigl(\widehat\lambda-\lambda_{\min}(Q)\bigr).
\]
Thus a minimum Ritz estimate certifies positive definiteness only if its one-sided overestimate of \(\lambda_{\min}(Q)\) is smaller than the added margin.

The finite-depth counterexample was checked for the potentially delicate issue of Lanczos breakdown. At the limiting start \(v_0\), the \(m\)-column Krylov matrix has full rank because the benign eigenvalues are distinct and all benign start components are nonzero. Hence the \(m\)-dimensional Krylov projector is locally continuous under a small hidden-eigenvector perturbation. The compressed minimum eigenvalue is therefore continuous, yielding an open failure set rather than only a measure-zero orthogonality example.

For the certificate, the quadratic-form comparison
\[
x^TQx\ge |x|^TC(Q)|x|
\]
is exact term by term and gives \(\lambda_{\min}(Q)\ge\lambda_{\min}(C(Q))\). The weighted Gershgorin bound follows from diagonal similarity. With \(A=\mu I-C(Q)\ge0\), the inequality
\[
Ad_k\le U_kd_k
\]
implies
\[
A^2d_k\le U_kAd_k,
\]
so the upper Collatz ratios decrease and the lower eigenvalue bounds increase. Symmetry makes the reducible case a direct sum over support-graph components; positive diagonal makes each irreducible component primitive, so the power ratios converge to the Perron root. Collatz--Wielandt gives optimality among positive diagonal scalings.

The sign-switchable exactness statement is also exact: \(SQS=C(Q)\) with a signature matrix \(S\) is an orthogonal similarity. The verification artifact reproduces both an under-regularized finite-Lanczos example and monotone certified convergence on a sign-switchable example.

## Originality

**PASS, to the best of our knowledge.** Chen--Lu (arXiv:2609.19557v1) explicitly require \(Q+\gamma^{-1}I\succ0\), then state a practical formula using a Lanczos estimate plus the fixed margin \(\delta_\gamma\max\{1,\|Q\|_\infty\}\). The paper does not state a certified error bound for that estimate. Searches by the source title, the proximal-regularization formula, finite-Lanczos convexification, weighted Gershgorin scaling, comparison matrices, and equivalent smallest-eigenvalue formulations did not locate a prior correction of this rule.

The underlying matrix facts are classical and are excluded from the originality claim. In particular, Rayleigh--Ritz explains the direction of Ritz error; Gershgorin and positive diagonal scaling are standard; the comparison-matrix inequality belongs to classical Z-/H-matrix theory; and Perron--Frobenius/Collatz--Wielandt characterize the best scaling. Gershgorin-based Levenberg--Marquardt Hessian regularization is also implemented in acados. QPALM is an earlier proximal nonconvex-QP solver and explicitly treats the smallest eigenvalue when setting its proximal parameter.

The originality claim is only the PDNQP-specific package: (i) the exact interpretation of its fixed margin as an allowed one-sided Ritz error, (ii) an arbitrary-finite-depth open-set Lanczos failure family, and (iii) a monotone factorization-free certified replacement whose limiting bound and exact sign-switchable class are characterized.

The main residual originality risk is simultaneous work prompted by the very recent PDNQP preprint, or an implementation/revision not publicly linked or indexed at the time of review.

## Value

**PASS.** The spectral condition is not cosmetic: PDNQP uses it to make the inner QPs strongly convex and invokes it in the convergence assumptions. A deterministic safeguard that preserves sparse matrix-vector structure is therefore directly aligned with the solver's stated design goal. The proposed bound is available immediately from ordinary Gershgorin and can then be tightened monotonically, allowing a correctness/performance tradeoff without sparse factorization.

The result is also diagnostic: it distinguishes an eigenvalue approximation from a convexity certificate, quantifies exactly how much Ritz error the fixed margin can absorb, and identifies a structured matrix class where the sparse certificate becomes asymptotically exact.

## Limitations

The result does not establish a failure of the reported PDNQP benchmark runs. The arXiv v1 text says only that the smallest eigenvalue is estimated by Lanczos iterations; an implementation-specific estimator or unreported safeguard was not available for verification from the paper's linked materials. If the estimator is already a rigorous lower bound, the finite-Ritz objection is inapplicable.

The weighted comparison bound can be conservative when signs create favorable cancellation. Finite-precision certification needs rounding control or an added numerical allowance. The result addresses only the strong-convexity shift and does not re-prove the remaining convergence assumptions or analyze total GPU runtime.

## Sources inspected

- Chen and Lu, arXiv:2609.19557v1, including the full accessible HTML statement of the strong-convexity requirement, convergence assumptions, and Section 3.1.2 proximal-regularization formula.
- Hermans, Themelis, and Patrinos, arXiv:2010.02653 / Mathematical Programming Computation 14 (2022), for the predecessor proximal nonconvex-QP framework.
- Current QPALM public documentation describing its nonconvex minimum-eigenvalue setup.
- acados public documentation describing Gershgorin-based Levenberg--Marquardt Hessian regularization.
- Classical Gershgorin, Perron--Frobenius, Collatz--Wielandt, and comparison-matrix references.

No highly relevant inaccessible paper was identified whose available title or abstract specifically signals the PDNQP fixed-margin correction. The most material uninspected item is an implementation-specific PDNQP eigenvalue routine, because no public code link was present on the inspected arXiv record.
