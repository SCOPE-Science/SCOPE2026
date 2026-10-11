# A rationally certified width-two Fourier zero-free strip for three-dimensional bipyramids

## Finding
For \(\alpha>0\), consider the centrally symmetric three-dimensional convex bipyramid
\[
\Omega_\alpha=\{(x,y)\in\mathbb R\times\mathbb R^2:|x|+\alpha\|y\|_2\le1\}.
\]
For the Fourier convention \(\widehat{\chi_K}(\xi)=\int_K e^{-i\langle\xi,z\rangle}\,dz\), let \(\kappa(K)\) be the infimum of Euclidean norms of real Fourier zeros, with the infimum of an empty set interpreted as infinity.

**Theorem.** For every \(\alpha>0\), every real Fourier zero of \(\chi_{\Omega_\alpha}\) has norm **strictly greater** than \(2\alpha\). Equivalently,
\[
\boxed{\kappa(\Omega_\alpha)>2\alpha.}
\]
If \(\Omega_\alpha^*\) is the Euclidean ball with the same volume, then
\[
\boxed{\kappa(\Omega_\alpha)>\kappa(\Omega_\alpha^*)\quad\text{for every }\alpha\ge23.}
\]
The inequality is a sufficient explicit certificate in this shape family; neither the zero-free width \(2\) nor the parameter threshold \(23\) is asserted optimal.

## Assumptions and scope
The body is exactly the solid of revolution defined above; \(\alpha\) is any positive real number. This concerns its real Fourier transform and Euclidean distance to its zero set, not complex Fourier zeros or arbitrary three-dimensional symmetric convex bodies. The source motivation was first publicly posted September 9, 2026 (arXiv:2609.10517v1). The main theorem's primary subject is convex geometry (MSC 52A40).

## Proof
Write \(s=\|\eta\|_2/\alpha\) and \(u\in\mathbb R\) for axial and transverse Fourier parameters. Integrating circular cross sections gives
\[
\widehat{\chi_{\Omega_\alpha}}(u,\eta)=\alpha^{-2}F(u,s),\quad
F(u,s)=2\int_0^1 f_s(x)\cos(ux)\,dx,
\]
where, for \(s>0\),
\[
f_s(x)=\frac{2\pi}{s}(1-x)J_1(s(1-x)),\qquad
f_0(x)=\pi(1-x)^2.
\]
Here \(J_0,J_1\) are ordinary Bessel functions. Put \(g(z)=J_0(z)-zJ_1(z)\). The identity \((zJ_1(z))'=zJ_0(z)\) yields \(f_s''(x)=2\pi g(s(1-x))\), including \(s=0\) by continuity. Since \(f_s(1)=f_s'(1)=0\), two integrations by parts and \((tJ_0(st))'=g(st)\) give, for \(u\ne0\),
\[
\frac{u^2F(u,s)}{4\pi}=H(u,s):=
\int_0^1g(s(1-x))\bigl(1-\cos(ux)\bigr)\,dx. \tag{1}
\]
For \(0<z\le2\), the alternating Bessel series imply \(J_0(z)>0\) and \(J_1(z)>0\); indeed \(J_0(z)\ge1-z^2/4\) with strictness at \(z=2\), and \(J_1(z)\ge z/2-z^3/16>0\). Consequently
\[
g'(z)=-J_1(z)-zJ_0(z)<0\quad(0<z\le2).
\]
Thus \(H(u,s)\ge H(u,2)\) for every real \(u\ne0\) and \(0\le s\le2\), because the factor \(1-\cos(ux)\) is nonnegative. It suffices to prove \(H(u,2)>0\) for every \(u>0\). Write \(q(x)=g(2(1-x))\). The bounds \(0<J_0(z)\le1\), \(0\le J_1(z)\le z/2\) on \([0,2]\) imply \(\|q\|_\infty\le3\). Moreover \(q\) is increasing, \(q(1)=1\), and the alternating expansion of \(g(2t)\) gives
\[
\int_0^1q(x)x^2\,dx
=\sum_{j=0}^\infty\frac{(-1)^j\,2}{(j!)^2(2j+2)(2j+3)}
\ge\frac13-\frac1{10}=\frac7{30}. \tag{2}
\]
The alternating terms after the first decrease in magnitude.

**Small axial frequencies.** For \(0<u\le1\), Taylor's inequality \(1-\cos y\ge y^2/2-y^4/24\), applied with the signed kernel through the absolute remainder, gives
\[
H(u,2)\ge\frac{u^2}{2}\frac7{30}-\frac{u^4}{24}\frac35
\ge\frac{11}{120}u^2>0. \tag{3}
\]

**Large axial frequencies.** The alternating series give \(g(2)>-1\) (already the first four terms sum to \(-17/18\)) and
\[
\int_0^1q(x)\,dx=J_0(2)>\frac{11}{50}
\]
(the first four terms of \(J_0(2)\) sum to \(2/9\)). Integration by parts, using monotonicity, gives
\[
\left|\int_0^1q(x)\cos(ux)\,dx\right|
\le\frac{q(1)+\int_0^1q'(x)\,dx}{u}
=\frac{2-g(2)}{u}<\frac3u.
\]
Hence for \(u\ge14\),
\[
H(u,2)>\frac{11}{50}-\frac3{14}=\frac1{175}>0. \tag{4}
\]

**Remaining axial frequencies.** On \(1\le u\le14\), expand
\[
g(2t)=\sum_{j\ge0}\frac{(-1)^j(2j+1)t^{2j}}{(j!)^2},
\quad1-\cos(ux)=\sum_{k\ge1}\frac{(-1)^{k+1}(ux)^{2k}}{(2k)!}.
\]
Let \(P(u)\) be the integrated product of the first \(11\) terms of the former (\(0\le j\le10\)) and the first \(40\) terms of the latter (\(1\le k\le40\)):
\[
P(u)=\sum_{k=1}^{40}\sum_{j=0}^{10}
\frac{(-1)^{j+k+1}(2j+1)(2j)!\,u^{2k}}
{(j!)^2(2j+2k+1)!}. \tag{5}
\]
The alternating Bessel remainder and Taylor's theorem, using \(\sum_{j=0}^{10}(2j+1)/(j!)^2<6\), imply uniformly on this interval
\[
|H(u,2)-P(u)|\le E
:=\frac{46}{(11!)^2}+\frac{6\,14^{81}}{81!}<10^{-10}. \tag{6}
\]
The standalone exact-rational certificate `checks/bicone_certificate.py` evaluates (5) at the \(261\) rational nodes \(u_i=1+i/20\) for \(0\le i\le260\) and proves, **with exact rational comparisons**, that \(P(u_i)>1/20\) at every node. Since
\[
|\partial_uH(u,2)|\le\int_0^1|q(x)|x\,dx\le\frac32,
\]
every point of \([1,14]\) lies within \(1/40\) of a node, and therefore
\[
H(u,2)>\frac1{20}-\frac3{80}-10^{-10}>0. \tag{7}
\]
Equations (3), (4), (7) cover every \(u>0\); evenness covers \(u<0\). For \(u=0\), the original positive-integrand expression for \(F(0,s)\) shows \(F(0,s)>0\) for \(0\le s\le2\), since \(J_1(z)>0\) on \((0,2]\). Thus the Fourier transform has no zero with \(s\le2\), and all zeros satisfy \(\|\eta\|_2>2\alpha\). By the nonemptiness theorem for Fourier zeros of balanced positive-measure sets (reference 1, Proposition 1.1) and continuity of the Fourier transform, the real zero set is nonempty and closed, so its distance from the origin is attained. Hence the minimum norm is strictly greater than \(2\alpha\), proving the first assertion.

The volume is \(|\Omega_\alpha|=2\pi/(3\alpha^2)\), so the equal-volume ball has radius \((2\alpha^2)^{-1/3}\) and its first real Fourier zero is
\[
\kappa(\Omega_\alpha^*)=j_{3/2,1}(2\alpha^2)^{1/3}.
\]
For completeness, \(j_{3/2,1}<9/2\): the first positive root of \(\sin z-z\cos z=0\) lies in \((\pi,3\pi/2)\); at \(z_0=9/2\) put \(y=3\pi/2-z_0\). The elementary bounds \(3<\pi<22/7\) imply \(0<y<3/14\), so \(\tan y\le y/(1-y^2/2)\le84/383<2/9=1/z_0\). Thus \(\sin z_0-z_0\cos z_0<0\), and the first root is below \(z_0\). Whenever \(\alpha>729/32\), in particular whenever \(\alpha\ge23\), cubing shows
\[
\kappa(\Omega_\alpha^*)<\frac92(2\alpha^2)^{1/3}<2\alpha<\kappa(\Omega_\alpha).
\]

## Verification
Run `python checks/bicone_certificate.py` using Python's standard library. It constructs (5) with `fractions.Fraction` only, checks all \(261\) grid nodes and the rational tail/interpolation estimates, and prints `BICONE_ZERO_FREE_S2_OK`. No floating-point comparisons are used to establish positivity. The grid is **not** treated as exhaustive without the analytic derivative bound and error estimate. The analytic steps outside the finite certificate are explicitly given above.

## Relationship to prior work
Gómez-Serrano, Levitin, Platt and Polterovich (arXiv:2609.10517v1, Section 2) proved the existence of a positive, not explicitly quantified, all-axial-frequency zero-free transverse strip for these bipyramids and exhibited a numerical case with \(\alpha=100\). A separately published note entitled *A Pólya–Bessel zero-free strip for Fourier bipyramids* (September 2026, archival identifier `72c1da0f9bb0`) proved the explicit strip with transverse width \(r_3\approx1.2557837118\), yielding a sufficient parameter cutoff about \(91.625\). That convexity-of-kernel argument does not imply a strip of width \(2\): the kernel's second derivative already changes sign before \(2\). The present result instead proves positivity of the **integrated** oscillatory kernel beyond the convexity range, increasing the certified strip to \(2\) and reducing the explicit sufficient parameter to \(23\). It does not imply the sharp transverse-zero threshold or an optimal counterexample.

## Limitations
The result concerns only the stated three-dimensional bipyramids. The width \(2\) and parameter \(23\) are sufficient, not optimal. The technique does not determine any Fourier zero's location, nor does it disprove ball extremality in dimension two. The novelty comparison covers inspected primary sources and searched public records, not inaccessible or unpublished parallel work. The scientific assessment is not an independent validation.

## References
1. J. Gómez-Serrano, M. Levitin, D. Platt, I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517v1 (first posted September 9, 2026), https://arxiv.org/abs/2609.10517.
2. *A Pólya–Bessel zero-free strip for Fourier bipyramids*, public mathematical note (September 2026), archival identifier `72c1da0f9bb0`.
3. NIST Digital Library of Mathematical Functions, §10.2 and §10.6, for the Bessel series and recurrences, https://dlmf.nist.gov/10.2 and https://dlmf.nist.gov/10.6.
