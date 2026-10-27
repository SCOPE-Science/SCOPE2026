# Sharp signed-cosine taper threshold on \(SO(3)\) and a Euclidean positivity separation

## Finding
Let \(\alpha(R)\in[0,\pi]\) denote the principal rotation angle of \(R\in SO(3)\). For each real \(b\), set
\[
\Phi_b(R)=\left(1-\frac{\alpha(R)}{\pi}\right)^2\bigl(1+b\cos\alpha(R)\bigr),
\qquad K_b(R,S)=\Phi_b(R^{-1}S).
\]
The following conditions are equivalent:

1. \(K_b\) is positive semidefinite on every finite subset of \(SO(3)\).
2. \(b\ge-8/23\).

Every admissible \(K_b\), including \(b=-8/23\), is strictly positive definite on every finite set of distinct rotations. At \(b=-8/23\) the central Fourier coefficient vanishes precisely in irreducible degree \(\ell=2\), whose matrix-coefficient isotypic space has dimension \(25\); all other irreducible degrees have strictly positive coefficients. For \(b<-8/23\) the degree-two coefficient is negative.

This exact admissibility is not a consequence of an ambient Euclidean radial covariance restriction: the radial extension of the boundary profile, defined by \(\Phi_{-8/23}(r)\) for \(0\le r\le\pi\) and zero for \(r>\pi\), has three-dimensional Euclidean Fourier transform
\[
\widehat{\Phi}_{-8/23}(\xi)=-\frac{361}{3726}<0
\quad\text{when }\|\xi\|_2=3,
\]
with the Fourier convention \(\widehat f(\xi)=\int_{\mathbb R^3}f(x)e^{-i\xi\cdot x}\,dx\).

## Assumptions and scope
The group \(SO(3)\) has normalized Haar measure. The intrinsic distance is \(d(R,S)=\alpha(R^{-1}S)\), with maximal angle \(\pi\). The parameter \(b\) ranges over **all** real numbers; no extra positivity assumption on the pointwise profile is imposed. Positive semidefiniteness means that \(\sum_{j,k}c_j\overline{c_k}K_b(R_j,R_k)\ge0\) for every finite tuple of rotations and complex coefficients. Strict positive definiteness uses pairwise distinct rotations and a nonzero coefficient vector. The Euclidean extension is an auxiliary comparison, not the metric used in the main theorem.

## Proof
**1. Central Fourier reduction.** The irreducible characters of \(SO(3)\) are
\[
\chi_\ell(\theta)=\frac{\sin((\ell+1/2)\theta)}{\sin(\theta/2)},\qquad \ell=0,1,2,\ldots,
\]
with dimension \(2\ell+1\). A normalized Haar-distributed rotation has angle density \(\frac{2}{\pi}\sin^2(\theta/2)\) on \([0,\pi]\). For a continuous central function \(u(\theta)\), the scalar Fourier transform on degree \(\ell\) equals
\[
\widehat u(\ell)=\frac{1}{\pi(2\ell+1)}\int_0^\pi u(\theta)
\bigl(\cos(\ell\theta)-\cos((\ell+1)\theta)\bigr)\,d\theta.
\]
By the compact-group Bochner theorem, positivity of all these scalar coefficients is necessary and sufficient for positive definiteness.

**2. Exact cosine coefficients.** Put \(g(\theta)=(1-\theta/\pi)^2\) and define
\[
F_k=\int_0^\pi g(\theta)\cos(k\theta)\,d\theta,
\quad H_k=\int_0^\pi g(\theta)\cos\theta\cos(k\theta)\,d\theta.
\]
Integration by parts gives \(F_0=\pi/3\) and \(F_k=2/(\pi k^2)\) for integers \(k\ge1\). The product-to-sum identity gives \(H_0=F_1\) and \(H_k=(F_{k-1}+F_{k+1})/2\) for \(k\ge1\). Writing \(A_\ell=F_\ell-F_{\ell+1}\) and \(B_\ell=H_\ell-H_{\ell+1}\), the sign of the degree-\(\ell\) Fourier block is exactly the sign of \(A_\ell+bB_\ell\).

At the two lowest degrees,
\[
\begin{array}{ll}
A_0=\pi/3-2/\pi,&B_0=7/(4\pi)-\pi/6,\\
A_1=3/(2\pi),&B_1=\pi/6-31/(36\pi).
\end{array}
\]
Each \(B_\ell\) is strictly positive: the displayed values are positive for \(\ell=0,1\), and for \(\ell\ge2\),
\[
A_\ell=\frac2\pi\left(\frac1{\ell^2}-\frac1{(\ell+1)^2}\right),\quad
B_\ell=\frac1\pi\left(\frac1{(\ell-1)^2}+\frac1{(\ell+1)^2}
-\frac1{\ell^2}-\frac1{(\ell+2)^2}\right)>0.
\]
For all integers \(\ell\ge2\), the exact ratio simplifies to
\[
\frac{A_\ell}{B_\ell}
=\frac{(\ell-1)^2(\ell+2)^2}{\ell^4+2\ell^3+3\ell^2+2\ell-2}.
\]
A polynomial factorization, with every denominator factor positive, shows
\[
\pi\left(23A_\ell-8B_\ell\right)
=\frac{6(\ell-2)(\ell+3)(2\ell+1)(5\ell^2+5\ell-6)}
{\ell^2(\ell-1)^2(\ell+1)^2(\ell+2)^2}\ge0,
\]
and equality holds only for \(\ell=2\). At the two remaining degrees, direct substitution gives
\[
A_0-\tfrac8{23}B_0=\frac{3(3\pi^2-20)}{23\pi}>0,\qquad
A_1-\tfrac8{23}B_1=\frac{745-24\pi^2}{414\pi}>0.
\]
Consequently \(A_\ell+bB_\ell\ge0\) for every degree if and only if \(b\ge-8/23\), and exactly the degree-two coefficient vanishes at equality. Since \(2\ell+1=5\) in that degree, its entire Peter--Weyl matrix-coefficient sector has dimension \(5^2=25\).

**3. Strictness despite one missing sector.** In the admissible interior, every irreducible scalar Fourier coefficient is positive. At the endpoint, only the degree-two coefficient is zero. If a finite complex measure \(\mu=\sum_jc_j\delta_{R_j}\) has zero quadratic energy, its Fourier transform must vanish in every degree other than possibly two. Peter--Weyl uniqueness then identifies \(\mu\) with a finite matrix-coefficient polynomial times Haar measure. Such an absolutely continuous measure cannot equal a nonzero finite atomic measure because Haar measure is nonatomic. Thus \(\mu=0\), and pairwise distinct support forces all \(c_j=0\). Strict positive definiteness follows.

**4. Ambient Euclidean obstruction.** For the boundary parameter, extend the radial profile by zero outside radius \(\pi\). The radial Fourier formula at frequency radius \(k>0\) reads
\[
\widehat f(k)=\frac{4\pi}{k}\int_0^\pi r\left(1-\frac r\pi\right)^2
\left(1-\frac8{23}\cos r\right)\sin(kr)\,dr.
\]
Termwise elementary integration at \(k=3\) yields \(-361/3726\). A negative Fourier value contradicts Euclidean Bochner positivity.

## Verification
The standalone file `check_rotation_taper.py` uses exact symbolic algebra to check the rational ratio, the factored infinite-degree inequality, the two exceptional degrees and the Euclidean Fourier witness. It also performs 18 independent numerical integrations against the normalized \(SO(3)\) characters, comparing with the analytic coefficients to 30-digit working precision; the largest observed absolute residual was below \(5\times10^{-31}\). Execute with Python 3 and installed `sympy` and `mpmath`: `python check_rotation_taper.py`. Numerical tests are not an infinite-degree proof; the factored identity and compact-group Bochner theorem provide that proof.

## Relationship to prior work
Erb and Filbir develop the Peter--Weyl framework for positive-definite central functions on \(SO(3)\), including Poisson-type, polynomial-character, and diffusion examples. Their general characterization is used here, but their exhibited families do not provide the exact signed-cosine quadratic-taper cutoff. Gneiting develops the classical Askey truncated-power covariance framework on spheres. Lu proves positive definiteness and strictness for unmodulated truncated powers on spheres and real projective spaces. Neither result states the signed cosine modulation threshold, the missing degree-two matrix sector, or the Euclidean non-transfer witness. Earlier work on exponentially damped cosine kernels on circles and three-spheres concerns different underlying spaces and profiles, so its parameter boundaries do not imply this cutoff.

## Limitations
The classification concerns one intrinsic-distance kernel family on \(SO(3)\), not arbitrary projective spaces, dimensions, or higher-frequency multipliers. The boundary kernel is strictly positive definite on finite distinct configurations, but its Fourier transform is **not** strictly positive in every irreducible degree. The Euclidean comparison shows non-transfer only at the specified boundary parameter and frequency; it does not characterize Euclidean admissibility for other parameters. Literature comparisons are bounded, and independent mathematical audit remains outstanding.

## References
1. W. Erb and F. Filbir, *Approximation by positive definite functions on compact groups*, Numerical Functional Analysis and Optimization 29 (2008), 1082--1107. DOI: 10.1080/01630560802484310. Author preprint: https://math.hawaii.edu/~erb/images/pp07-23.pdf (Sections 2 and 4).
2. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, Bernoulli 19 (2013), 1327--1349. Original arXiv posting 2011-11-30, arXiv:1111.7077, https://arxiv.org/abs/1111.7077.
3. T. Lu, *Strictly positive definite functions on spheres*, Journal of Approximation Theory 306 (2025), 106120. DOI: 10.1016/j.jat.2024.106120. Author-available full text: https://www.math.wichita.edu/~lu/resume/power.pdf (Sections 2 and 3).
