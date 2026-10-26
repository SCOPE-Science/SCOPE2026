# Sharp exponent threshold for a half-circle generalized sine-power covariance

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). Write \(\delta(x-y)\in[0,\pi]\) for the shorter angular distance between two points. For every real exponent \(\alpha>0\), define
\[
\psi_\alpha(\theta)=
\begin{cases}
1-\sin^\alpha\theta,&0\le\theta\le\pi/2,\\
0,&\pi/2<\theta\le\pi,
\end{cases}
\qquad K_\alpha(x,y)=\psi_\alpha(\delta(x-y)).
\]
Then \(K_\alpha\) is positive semidefinite for every finite configuration on the circle **if and only if**
\[
0<\alpha\le\alpha_*:=8-\sqrt{41}=1.596875762567\ldots.
\]
Every admitted kernel is strictly positive definite for finite sets of distinct points. For \(0<\alpha<\alpha_*\), every Fourier coefficient is strictly positive. At the critical exponent, the only vanishing Fourier coefficients occur at frequencies \(\pm5\). For \(\alpha_*<\alpha\le2\), frequency \(5\) has negative Fourier coefficient; for \(\alpha>2\), frequency \(4\) does.

## Assumptions and scope
The circle has circumference \(2\pi\) and is equipped with intrinsic (shortest-arc) distance; \(\alpha\) ranges over all positive real numbers. The support radius is exactly \(\pi/2\). The statement concerns kernel matrices \([K_\alpha(x_i,x_j)]\) for arbitrarily chosen finite points; strictness means positivity of \(\sum_{i,j}c_i\overline{c_j}K_\alpha(x_i,x_j)\) for pairwise distinct points and every nonzero complex coefficient vector. No statement is made for a different support radius or for spheres of dimension greater than one.

## Proof
For integers \(n\ge0\), let
\[
A_n(\alpha)=\int_0^{\pi/2}(1-\sin^\alpha t)\cos(nt)\,dt,
\qquad I_n(\alpha)=\int_0^{\pi/2}\sin^\alpha t\cos(nt)\,dt.
\]
The normalized complex Fourier coefficient of the even periodic function \(\psi_\alpha(\delta(t))\) at frequency \(n\) is \(A_{|n|}(\alpha)/\pi\). In particular \(A_0>0\), so Fourier positivity is equivalent to \(A_n\ge0\) for every positive integer \(n\).

**Recurrence.** Differentiating \(\sin^{\alpha+1}t\cos((n-1)t)\), using elementary product-to-sum identities, and integrating on \([0,\pi/2]\), gives, for every integer \(n\ge2\),
\[
(\alpha+n)I_n+(\alpha-n+2)I_{n-2}
=2\cos\left(\frac{(n-1)\pi}{2}\right).
\tag{1}
\]
The endpoint at zero vanishes because \(\alpha>0\); the endpoint at \(\pi/2\) is the cosine on the right.

**Even frequencies.** When \(n=2k\), the right side of (1) is zero, giving
\[
I_{2k}=\frac{2k-2-\alpha}{2k+\alpha}I_{2k-2},
\qquad I_2=-\frac{\alpha}{\alpha+2}I_0<0.
\]
For \(0<\alpha<2\), every subsequent multiplier, starting at \(k=2\), is positive, so \(I_{2k}<0\) for all \(k\ge1\). Since \(\int_0^{\pi/2}\cos(2kt)\,dt=0\), one has \(A_{2k}=-I_{2k}>0\). Conversely, if \(\alpha>2\), then
\[
A_4=-\frac{\alpha(\alpha-2)}{(\alpha+2)(\alpha+4)}I_0<0,
\]
which already rules out positive definiteness.

**Odd frequencies and the sharp obstruction.** For odd \(n\ge3\), set \(\varepsilon_n=\sin(n\pi/2)=(-1)^{(n-1)/2}\). Substituting \(A_n=\varepsilon_n/n-I_n\) into (1) yields
\[
(\alpha+n)A_n+(\alpha-n+2)A_{n-2}
=-\frac{2\alpha\varepsilon_n}{n(n-2)}.
\tag{2}
\]
The base integrals (or (2) beginning at \(A_1\)) give
\[
A_1=\frac{\alpha}{\alpha+1},\qquad
A_3=\frac{\alpha(5-\alpha)}{3(\alpha+1)(\alpha+3)},
\]
\[
A_5=\frac{\alpha(\alpha^2-16\alpha+23)}
{5(\alpha+1)(\alpha+3)(\alpha+5)}.
\tag{3}
\]
In \(0<\alpha\le2\), the expression in (3) is negative exactly when \(\alpha>8-\sqrt{41}\). Thus this index proves all remaining *necessity* assertions.

For *sufficiency*, fix \(0<\alpha\le\alpha_*<2\). The base values satisfy \(A_1>0\), \(A_3>0\), and \(A_5\ge0\). Suppose \(m\ge5\) is odd, \(m\equiv1\pmod4\), and \(A_m\ge0\). Two applications of (2) give
\[
A_{m+2}=\frac{(m-\alpha)A_m+2\alpha/[m(m+2)]}{m+2+\alpha}
\ge\frac{2\alpha}{m(m+2)(m+2+\alpha)}>0,
\]
\[
A_{m+4}=\frac{(m+2-\alpha)A_{m+2}-2\alpha/[(m+2)(m+4)]}{m+4+\alpha}
\ge \frac{2\alpha(4-2\alpha)}{m(m+2+\alpha)(m+4)(m+4+\alpha)}>0.
\]
The final inequality uses the exact identity
\[
\frac{m+2-\alpha}{m(m+2+\alpha)}-\frac1{m+4}
=\frac{(m+2)(4-2\alpha)}{m(m+2+\alpha)(m+4)}.
\]
Induction from \(m=5\) proves that every odd \(A_n\) with \(n\ge7\) is strictly positive. Coupled with the even case and the positive base coefficients, this proves Fourier nonnegativity throughout the stated parameter interval.

The compact-group Fourier characterization (Bochner's criterion) gives positive semidefiniteness. Moreover, all Fourier coefficients for \(n\ge6\) are strictly positive, including at \(\alpha=\alpha_*\). If a Gram quadratic form vanishes for distinct points \(z_j=e^{ix_j}\), then \(\sum_jc_jz_j^n=0\) for all \(n\ge6\). Taking any consecutive block of as many frequencies as points and factoring the corresponding Vandermonde matrix forces every \(c_j=0\). Thus every admitted kernel is strictly positive definite, even though the fifth harmonic vanishes at the endpoint.

## Verification
The standalone `CHECK.py` verifies the exact rational formulas for \(A_3\) and \(A_5\), the factorization underlying the induction, and the critical root. It independently compares 384 recurrence-derived coefficients with direct numerical quadrature for six representative exponent values (largest absolute discrepancy below \(4.8\times10^{-14}\)). It also constructs a 32-site finite cyclic Gram witness at \(\alpha=1.7\), with a negative frequency-five eigenvalue approximately \(-0.0510351363091\). These finite checks support, but do not replace, the all-frequency proof above. Run `python CHECK.py` with Python, SymPy, NumPy, and SciPy.

## Relationship to prior work
This is the support-radius \(c=\pi/2\), circle-dimension \(d=1\) case of the generalized sine-power family presented as Problem 10 in Gneiting's 2011 preprint, which asks for admissible smoothness and support parameters. The explicit critical radical and complete all-frequency sign classification are not stated there. Earlier spherical Pólya criteria provide sufficient positivity under convexity assumptions but do not reach exponents strictly greater than one for this particular truncated profile. General strict positive-definiteness criteria for circles and products of circles concern the Fourier support rather than this family's exact parameter threshold. Search comparisons did not identify an already stated equivalent result; that is not a proof of global novelty.

## Limitations
The sharp result is restricted to the circle and the natural support radius \(\pi/2\). It does not solve the full two-parameter, higher-dimensional generalized sine-power problem, classify other cutoffs, or produce probabilistic sample-path properties. The novelty assessment is based on bounded accessible literature and indexed-result searches; independent mathematical validation has not been performed.

## References
1. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077v1 (first posted 2011-11-30), especially Problem 10 and equation (45).
2. R. K. Beatson, F. zu Castell, Y. Xu, *A Pólya criterion for (strict) positive definiteness on the sphere*, arXiv:1110.2437 (2011).
3. J. C. Guella, V. A. Menegatto, A. P. Peron, *Strictly positive definite kernels on a product of circles*, arXiv:1505.01169 (2015).
4. T. Gneiting, *Simple tests for the validity of correlation function models on the circle*, Statistics & Probability Letters 39 (1998), 119–122, doi:10.1016/S0167-7152(98)00042-X (abstract checked; full text not inspected).
