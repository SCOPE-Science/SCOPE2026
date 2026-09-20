# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The central identity is immediate from scalar spectral shifting:
\[
\lambda_{\min}(Q+(-\theta+\delta\beta)I)
=\delta\beta-(\theta-\lambda_{\min}(Q)).
\]
For an indefinite \(Q\), this also makes positivity of the proximal denominator automatic whenever the shifted Hessian is positive definite.

The finite-budget family was checked algebraically. At the displayed start, the Krylov matrix on the positive invariant block is a diagonally scaled Vandermonde matrix with distinct nodes, hence has full rank. The resulting smallest Ritz value is exactly \(\delta/(m+1)\), and the shifted minimum remains strictly negative. The open-set statement follows from persistence of full column rank and continuity of the compressed symmetric eigenvalue under perturbation of the start.

The universal threshold proof uses only
\(\|Q\|_2\le\|Q\|_\infty\le\beta\) for symmetric \(Q\) and the Rayleigh--Ritz enclosure. The two \(2\times2\) witnesses show necessity through the endpoint \(\delta=2\), where the best uniform conclusion is semidefiniteness, not positive definiteness.

The Gershgorin repair is standard and valid:
\(\ell_G\le\lambda_{\min}(Q)\) implies
\[
\lambda_{\min}(Q+\{\max(0,-\ell_G)+\eta\beta\}I)\ge\eta\beta.
\]
Exact rational execution of the public verification script agrees with all displayed finite examples.

## Originality

**PASS, to the best of our knowledge.** The classical fact that finite-step Lanczos/Ritz approximations can misconverge to a non-extreme eigenvalue is not claimed as new. Van Dorsselaer--Hochstenbach--van der Vorst explicitly document this issue and develop probabilistic extreme-eigenvalue bounds.

The September 2026 PDNQP paper is more specific: its base convergence result assumes \(Q+\gamma^{-1}I\succ0\), while its practical Eq. (11) uses a Lanczos estimate plus a fixed \(10^{-2}\max\{1,\|Q\|_\infty\}\) margin and states that this choice convexifies the inner problem. Searches by paper title, arXiv identifier, proximal convexification, Lanczos/Ritz terminology, and equivalent spectral-shift formulations found no public correction or prior derivation of the exact error-budget criterion, the all-finite-budget open-set family, or the sharp \(\delta>2\) norm-only threshold for this rule.

QPALM is the closest directly relevant predecessor. It explicitly treats minimum-eigenvalue estimation as part of choosing a proximal penalty and labels its LO(B)PCG output a lower bound. This record therefore does not claim that using a certified spectral lower bound for proximal convexification is new; the contribution is the certification gap and its sharp quantitative characterization for the newly stated PDNQP rule.

No public PDNQP implementation repository was identified, so an implementation may contain an undocumented certified lower-bound correction or safeguard. That possibility limits the implementation-level claim but does not alter the mathematical counterexample to the published rule as written.

## Value

**PASS.** Strong convexity of every inner QP is the interface connecting PDNQP's practical solver to both its accelerated primal--dual inner method and the imported QPALM outer convergence theory. The result identifies the exact quantity that must be controlled, proves that any fixed finite ordinary Lanczos budget can miss it on a positive-measure set of starts, and gives both a sharp worst-case safety threshold and a cheap certified repair. This is a concrete correctness boundary rather than a small constant improvement.

## Scope and limitations

The finding is about exact arithmetic and the standard Rayleigh--Ritz interpretation of a finite Lanczos estimate. It neither asserts failure of the published benchmark runs nor proves divergence of the whole PDNQP algorithm when the inner Hessian is indefinite. The sharp \(\delta>2\) threshold is for a restricted information model; tighter certified eigenvalue lower bounds can and should do better.
