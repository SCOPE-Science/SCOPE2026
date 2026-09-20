# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The main identity is an exact two-dimensional calculation. Exact first-step line search makes the Dai--Yuan coefficient equal to Fletcher--Reeves and makes the next direction A-conjugate to the first. In the orthonormal basis formed by the first direction and its complement, the source AOS matrix reduces to an explicit 2 by 2 matrix. Evaluating the true and model curvatures on the unique A-conjugate direction gives the exact ratio
\[
r=\frac{\mu L}{\mu^2\cos^2\theta+L^2\sin^2\theta}.
\]
Since exact two-dimensional CG would terminate on that line, the objective ratio is exactly \((r-1)^2\). The explicit condition-number family was also checked by symbolic algebra; the verification script is included.

The proof was stress-tested against eigenvector limits. If either mode vanishes, the first exact step already solves the one-mode problem, which is why the theorem excludes those endpoints and the range of r is open. The damping statement correctly uses the open range: gamma=2/kappa still gives strict decrease for every non-eigenvector orientation, while any larger positive gamma permits an orientation with gamma r>2.

## Originality

**PASS, to the best of our knowledge.** The primary 2026 source defines CG_AOS with the same AOS matrix and Dai--Yuan direction, provides numerical experiments, and explicitly leaves theoretical convergence and convergence-rate analysis open. Searches were made for CG_AOS, approximately optimal stepsizes combined with conjugate-gradient convergence/nonmonotonicity/overshoot, Dai--Yuan with approximately optimal stepsizes, and inexact-line-search CG on quadratics. No source was located that states the exact two-mode distortion formula, the sharp (kappa-1)^2 transient amplification, the explicit f_2/f_0 ~ kappa/4 family, or the sharp gamma <= 2/kappa two-mode damping threshold for this CG_AOS step.

The closest identified prior work is Ni and Liu (2024), DOI 10.1080/01630563.2024.2333255. Its abstract was inspected, but the full text was not accessible in the sources checked. The abstract describes a different Dai--Liao method: approximately optimal stepsize ideas are used to choose Dai--Liao conjugacy parameters, and global convergence is proved under stated conditions. Because the full theorem statements were not inspected, this paper is the main residual originality risk. The algorithm described by the available abstract is different from the 2026 CG_AOS method analyzed here.

Classical Dai--Yuan and other nonlinear-CG convergence papers were also checked at the statement/abstract level. Their global results impose Wolfe, Goldstein, or related line-search conditions and do not imply the exact AOS curvature-distortion formulas above.

## Value

**PASS.** The source paper presents CG_AOS as a new adaptive inexact-step framework and explicitly asks for convergence theory. A sharp two-mode calculation shows why standard monotone/Wolfe-style arguments cannot be assumed automatically: even after a favorable exact initialization, the first AOS step may increase the objective, and the excursion can scale without bound with conditioning relative to the starting objective. The accompanying sharp scalar damping threshold gives a concrete robust modification in the two-mode case. The result therefore supplies both an obstruction and a precise local repair target for future convergence analysis.

## Scope and limitations

This is an exact-arithmetic quadratic result, not a proof of CG_AOS divergence. It analyzes the first AOS step after exact initialization and a two-eigenmode invariant subspace. The scalar safeguard uses the condition number and is not claimed to be globally sharp in dimensions above two. The 2024 Ni--Liu full text remains uninspected and is explicitly retained as an originality uncertainty.
