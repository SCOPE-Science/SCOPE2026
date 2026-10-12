# Exact rank-two random-removal operator and sharp spectral-progress constant

## Finding

Let \(X\succeq0\) be a real symmetric matrix of rank exactly two, with its two positive eigenvalues \(0<a\le b\), and let \(u\) be uniform on the unit circle of \(\operatorname{Im}X\). The maximal feasible coefficient for subtracting \(uu^{\mathsf T}\) is
\[
\gamma(u)=\bigl(u^{\mathsf T}X^\dagger u\bigr)^{-1},
\]
where \(X^\dagger\) is the Moore–Penrose inverse. The **entire mean removed matrix**, not merely the mean coefficient, has the exact formula
\[
\mathbb E\bigl[\gamma(u)uu^{\mathsf T}\bigr]
=\frac{\sqrt{ab}}{\sqrt a+\sqrt b}\,X^{1/2}.
\tag{1}
\]
Here the square root is the positive-semidefinite square root and the formula is interpreted as zero on the orthogonal complement of \(\operatorname{Im}X\). In particular, for every positive-semidefinite matrix \(Q\) of the same ambient size,
\[
\mathbb E\bigl[\gamma(u)u^{\mathsf T}Qu\bigr]
\ge \frac{1}{1+\sqrt{b/a}}\,\operatorname{tr}(QX).
\tag{2}
\]
The coefficient \(1/(1+\sqrt{b/a})\) is the **largest possible uniform coefficient** in (2) for the given spectrum: equality holds for \(Q\) the orthogonal projector onto a \(b\)-eigenvector. It equals \(1/2\) in the isotropic case \(a=b\) and is asymptotic to \(\sqrt{a/b}\) as \(a/b\downarrow0\).

For comparison, the separate elementary estimates \(\gamma(u)\ge a\), \(\mathbb E[uu^{\mathsf T}]=\Pi/2\), and \(X\preceq b\Pi\) (\(\Pi\) the range projector) yield only \(a/(2b)\) instead of the sharp coefficient. Their ratio is \(2(b/a)/(1+\sqrt{b/a})\), which grows without bound with spectral conditioning. This comparison pertains to the **joint** stochastic weight and direction; it does not assert a new convergence rate for a full Frank–Wolfe algorithm.

## Assumptions and scope

The ambient dimension is any finite \(n\ge2\). The matrix \(X\in\mathbb S_+^n\) has rank precisely two, eigenvalues \(a,b\) with \(0<a\le b\), and arbitrary trace (unit trace is a special case). The random vector \(u\) is chosen with normalized rotationally invariant arc-length measure on the unit circle in \(\operatorname{Im}X\), independently of \(Q\). The test \(Q\) ranges over all \(n\times n\) symmetric positive-semidefinite matrices, including singular projectors. No convergence algorithm, minimizer, differentiable objective, or distribution on other spheres is assumed.

By the rank-one subtraction criterion, \(X-tuu^{\mathsf T}\succeq0\) for \(t\ge0\) if and only if \(t\le\gamma(u)\); at the maximal value the rank drops from two to one. This is the maximal-removal operation appearing in rank-one pairwise spectrahedral steps.

## Proof

Write \(X=aee^{\mathsf T}+bff^{\mathsf T}\) with \(e,f\) orthonormal. Parameterize \(u=e\cos\theta+f\sin\theta\), \(\theta\) uniform on \([0,2\pi)\), and put \(C=1/a\), \(D=1/b\). Then
\[
\gamma(u)=\frac{1}{C\cos^2\theta+D\sin^2\theta}.
\]
Elementary symmetry makes the off-diagonal expectation \(\mathbb E[\gamma\sin\theta\cos\theta]\) vanish. The scalar integral
\[
I(C,D)=\frac{1}{2\pi}\int_0^{2\pi}
\frac{d\theta}{C\cos^2\theta+D\sin^2\theta}
=\frac{1}{\sqrt{CD}}
\tag{3}
\]
follows by fourfold quadrant symmetry and the substitution \(t=\tan\theta\): on a quadrant the integral becomes \(\int_0^\infty dt/(C+Dt^2)=\pi/(2\sqrt{CD})\).

Define \(U=\mathbb E[\gamma\cos^2\theta]\) and \(V=\mathbb E[\gamma\sin^2\theta]\). The exact relations \(U+V=I(C,D)\) and \(CU+DV=1\) give, if \(C\ne D\),
\[
U=\frac{1}{\sqrt C(\sqrt C+\sqrt D)},\qquad
V=\frac{1}{\sqrt D(\sqrt C+\sqrt D)}.
\tag{4}
\]
For \(C=D\), each is \(1/(2C)\) by circle symmetry, agreeing with (4). Substituting \(C=1/a\), \(D=1/b\) into (4) yields
\[
U=\frac{a\sqrt b}{\sqrt a+\sqrt b},\qquad
V=\frac{b\sqrt a}{\sqrt a+\sqrt b}.
\]
Hence \(\mathbb E[\gamma uu^{\mathsf T}]=Uee^{\mathsf T}+Vff^{\mathsf T}\), precisely (1).

To prove (2), observe that the generalized eigenvalues of the pair \((\mathbb E[\gamma uu^{\mathsf T}],X)\) on \(\operatorname{Im}X\) are
\[
\frac{U}{a}=\frac{\sqrt b}{\sqrt a+\sqrt b},\qquad
\frac{V}{b}=\frac{\sqrt a}{\sqrt a+\sqrt b}.
\]
The smaller one is \(c=\sqrt a/(\sqrt a+\sqrt b)=1/(1+\sqrt{b/a})\). Therefore \(\mathbb E[\gamma uu^{\mathsf T}]-cX\succeq0\), also on the kernel of \(X\). Taking its trace against \(Q\succeq0\) proves (2). With \(Q=ff^{\mathsf T}\), equality holds. When \(a=b\), equality holds for every \(Q\). This proves the optimality assertion for all parameter boundaries allowed in the theorem.

The rank-one subtraction criterion used above follows without additional hypotheses by expressing \(X-tuu^{\mathsf T}=X^{1/2}(\Pi-tvv^{\mathsf T})X^{1/2}\), where \(v=X^{\dagger/2}u\in\operatorname{Im}X\). The central factor is positive semidefinite exactly when \(t\|v\|^2\le1\). At equality its range loses one dimension.

## Verification

The companion `verify_rank_two.py` performs 990 exact rational checks with eigenvalues whose square roots have rational ratios. It compares both eigenvalues of the mean-removal operator with the claimed formula, checks the sharp PSD coefficient and its spectral equality witness, and verifies the precise factor against the separate-estimate baseline. Six separate periodic-quadrature checks evaluate the angular integrals at isotropic and highly anisotropic spectral configurations and also check singularity/positivity of the maximal rank-one removal in sampled directions. Running `python verify_rank_two.py` produced `VERIFY_OK: 990 exact spectral-rational cases, six quadrature checks`.

The identity and inequality are proved for all admissible \(a,b,Q\) analytically; the finite checker is corroboration, not an exhaustive proof.

## Relationship to prior work

The maximal coefficient \(\gamma(u)=(u^{\mathsf T}X^\dagger u)^{-1}\) and the uniform-on-support random vector are taken from Garber's pairwise spectrahedral Frank–Wolfe construction (arXiv:2503.01441; DOI:10.1007/s10107-026-02343-3), which proves feasibility and uses pointwise spectral lower bounds and unweighted second moments in its convergence proof. The new fact concerns the **joint** matrix expectation with that maximal coefficient and its exact spectral comparison, rather than the already known feasibility criterion, an unweighted spherical second-moment identity, or the algorithm's global convergence theorem.

The standard scalar two-dimensional trigonometric integral (3) is explicitly recognized as a proof ingredient. General spherical quadratic-form moment formulas, including NIST DLMF §19.31, concern related integrals; the reviewed formulas do not themselves give the rank-two algorithmic mean-removal operator and the optimal positive-semidefinite comparison (2). The subsequent deterministic algorithm of Garber (arXiv:2608.09569) has a different update mechanism. Prior literature on in-face Frank–Wolfe updates also motivates rank-one modifications but does not, on the inspected material, establish the same stochastic certificate.

## Limitations

The exact mean operator requires rank **two** and uniform directions; it is not asserted in higher rank, for nonuniform sampling, or for approximate pseudoinverses. The condition-number comparison is sharp only for the specified stochastic removal operation. The proof gives no unconditional improvement to an algorithmic convergence rate or iteration complexity. Existing general spherical-integral literature may contain an equivalent operator identity under different terminology; the literature comparison is necessarily bounded and cannot exclude all unindexed results.

## References

1. D. Garber, *A Randomized Linearly Convergent Frank–Wolfe-type Method for Smooth Convex Minimization over the Spectrahedron*, arXiv:2503.01441 (first posted 2025-03-03); *Mathematical Programming* (2026), DOI:10.1007/s10107-026-02343-3, especially Algorithm 1 and Lemmas 2, 4, 5.
2. D. Garber, *Linear Convergence of a Frank-Wolfe-type Method over the Spectrahedron without Strict Complementarity*, arXiv:2608.09569 (2026), distinct deterministic follow-up.
3. NIST Digital Library of Mathematical Functions, §19.31, *Probability Distributions* (quadratic-form integrals; related general analytic background).
4. R. M. Freund, P. Grigas, and R. Mazumder, *An Extended Frank–Wolfe Method with “In-Face” Directions, and Its Application to Low-Rank Matrix Completion*, *SIAM Journal on Optimization* 27 (2017), DOI:10.1137/15M104726X.
