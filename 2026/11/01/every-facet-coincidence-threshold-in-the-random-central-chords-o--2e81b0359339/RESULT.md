# Every facet-coincidence threshold in the random central chords of a Euclidean hypercube

## Finding
For each integer \(d\ge2\), uniformly orient a line through the origin of the Euclidean cube \(Q_d=[-1,1]^d\), and let \(2T_d\) be the length of its intersection with the cube. The full distribution of \(T_d\) is a finite sum of explicit Dirichlet integrals. At every critical radius \(\sqrt{k}\), \(k=1,\ldots,d\), there is a sharp, nonzero contact-onset coefficient with exponent \((d+k-2)/2\). At every internal radius \(\sqrt{k}\), \(1\le k<d\), this determines the exact differentiability of the distribution function; at \(\sqrt d\) it determines the entire upper endpoint tail.

Put
\[
\alpha_{d,k}=\frac{d+k-2}{2},\qquad
B_{d,k}=\frac{2^{\alpha_{d,k}} k^{(k-d+2)/4}\Gamma(d/2)}{\pi^{k/2}\Gamma((d+k)/2)}.
\]
All these constants are strictly positive. If \(A_{d,k}(t)\) denotes the probability that the **first \(k\) squared coordinates** of a uniform unit vector are each at least \(t^{-2}\), then
\[
A_{d,k}(\sqrt k+\varepsilon)
=B_{d,k}\varepsilon^{\alpha_{d,k}}(1+o(1))\quad(\varepsilon\downarrow0).
\]
Write \(F_d(t)=\Pr(T_d\le t)\). At each internal threshold \(\sqrt{k}\), the newly activated term in \(F_d\) is
\[
(-1)^{k+1}\binom dk B_{d,k}(t-\sqrt{k})_+^{\alpha_{d,k}}
  +o((t-\sqrt{k})_+^{\alpha_{d,k}}).
\]
Precisely, \(F_d\) is \(C^{\lceil\alpha_{d,k}\rceil-1}\) but not \(C^{\lceil\alpha_{d,k}\rceil}\) at \(t=\sqrt{k}\), where for \(k=1\) the function is extended by zero below one. At the last threshold,
\[
1-F_d(\sqrt d-\varepsilon)
=B_{d,d}\varepsilon^{d-1}(1+o(1));
\]
therefore the complete CDF, extended by one above \(\sqrt d\), is \(C^{d-2}\) but not \(C^{d-1}\) there.

## Assumptions and scope
The dimension is an arbitrary fixed integer \(d\ge2\). The orientation \(U\) is Haar-uniform on \(S^{d-1}\), equivalently the unoriented line \(\mathbb R U\) is invariant under rotations of direction. No random translation of that line is made. The **central chord** is \(Q_d\cap\mathbb R U\). Its half-length is
\[
T_d=\frac{1}{\max_{1\le i\le d}|U_i|}\in[1,\sqrt d].
\]
All probabilities refer only to directional Haar measure, not volume-uniform points, invariant-line measures on all affine lines, or the directional projection width \(\sum_i|U_i|\). The exact distribution below is valid for all real \(t\): \(F_d(t)=0\) for \(t\le1\) and \(F_d(t)=1\) for \(t\ge\sqrt d\).

For \(1\le k\le d\), set
\[
A_{d,k}(t)=\Pr\{U_1^2\ge t^{-2},\ldots,U_k^2\ge t^{-2}\}
\]
for \(t>0\), and set \(A_{d,k}(t)=0\) for \(t\le0\). When \(t\le\sqrt k\), these events have probability zero.

## Proof
**1. Distribution and exact integration.** Each coordinate has the standard Gaussian representation \(U_i=G_i/(\sum_jG_j^2)^{1/2}\), where \(G_i\) are independent standard normal variables. Consequently \(Z_i=U_i^2\) has the Dirichlet density with all parameters \(1/2\) on the simplex \(\sum_i Z_i=1\). Since \(T_d\le t\) means at least one \(Z_i\ge t^{-2}\), inclusion–exclusion gives the exact identity
\[
F_d(t)=\sum_{k=1}^d(-1)^{k+1}\binom dk A_{d,k}(t),\qquad t>0.
\]
For \(k<d\) let \(\beta=(d-k)/2>0\), \(a=t^{-2}\), and \(\delta=1-ka\). On \(t>\sqrt k\), integrate out the remaining \(d-k\) squared coordinates. Their sum has Dirichlet parameter \(\beta\); thus
\[
A_{d,k}(t)=\frac{\Gamma(d/2)}{\pi^{k/2}\Gamma(\beta)}
\int_{\substack{x_i\ge0\\\sum_{i=1}^k x_i\le\delta}}
(\delta-\sum_i x_i)^{\beta-1}\prod_{i=1}^k(a+x_i)^{-1/2}\,dx_1\cdots dx_k.
\tag{1}
\]
For \(k=d\), integrate directly on the simplex, taking \(x_d=\delta-\sum_{i<d}x_i\), to obtain
\[
A_{d,d}(t)=\frac{\Gamma(d/2)}{\pi^{d/2}}
\int_{\substack{x_i\ge0\\\sum_{i=1}^{d-1}x_i\le\delta}}
\prod_{i=1}^{d}(a+x_i)^{-1/2}\,dx_1\cdots dx_{d-1}.
\tag{2}
\]
Both domains are finite simplices and their integrands are integrable. These are the promised exact finite-dimensional integrals for the CDF.

**2. Thresholds and leading constants.** No \(k\) coordinates can simultaneously satisfy \(Z_i>1/k\), because \(\sum Z_i=1\). Hence \(A_{d,k}(t)=0\) for \(t\le\sqrt k\); for \(t>\sqrt k\) its integration simplex has positive volume, so \(A_{d,k}(t)>0\). Put \(t=\sqrt k+\varepsilon\). Then
\[
\delta=1-\frac{k}{t^2}=\frac{2\varepsilon}{\sqrt k}+O(\varepsilon^2),\qquad a\longrightarrow\frac1k.
\]
For \(k<d\), substitute \(x_i=\delta y_i\) in (1). After extracting \(\delta^{k+\beta-1}\), the remaining integral tends by dominated convergence to
\[
k^{k/2}\int_{\substack{y_i\ge0\\\sum_i y_i\le1}}(1-\sum_i y_i)^{\beta-1}dy
=k^{k/2}\frac{\Gamma(\beta)}{\Gamma(k+\beta)}.
\]
Domination holds since \(a\) stays bounded away from zero; the beta singularity at \(\sum y_i=1\) is integrable for \(\beta>0\). Here \(k+\beta=(d+k)/2\), yielding
\[
A_{d,k}(\sqrt k+\varepsilon)
\sim\frac{\Gamma(d/2)}{\pi^{k/2}\Gamma((d+k)/2)}k^{k/2}
\left(\frac2{\sqrt k}\right)^{(d+k-2)/2}
\varepsilon^{(d+k-2)/2}=B_{d,k}\varepsilon^{\alpha_{d,k}}.
\]
For \(k=d\), the integrand in (2) tends uniformly to \(d^{d/2}\), while the \((d-1)\)-simplex has volume \(\delta^{d-1}/(d-1)!\). This gives the same coefficient \(B_{d,d}\) and exponent \(d-1\).

**3. Exact interior differentiability.** For a fixed internal threshold \(t_0=\sqrt k\), all terms \(A_{d,j}\) with \(j>k\) vanish on a neighborhood of \(t_0\); for \(j<k\), their integrals (1) with \(a>0\), \(\delta>0\) can be mapped to a fixed simplex and depend real-analytically on \(t\) near \(t_0\). Hence the first term that switches on at \(t_0\) is \((-1)^{k+1}\binom dk A_{d,k}\). The same fixed-simplex substitution shows more precisely that \(A_{d,k}(t)=\delta^{\alpha_{d,k}}H(t)\) for \(t>t_0\), with \(H\) real analytic through \(t_0\) and \(H(t_0)>0\). This is also true for \(k=d\) by (2). Thus the finite left/right mismatch has the regularity of \((t-t_0)_+^{\alpha_{d,k}}\): exactly \(C^{\lceil\alpha_{d,k}\rceil-1}\) and no higher integer differentiability.

**4. Upper endpoint.** Put \(t=\sqrt d-\varepsilon\) with \(\varepsilon>0\). The event \(T_d>t\) is \(Z_i<t^{-2}\) for every \(i\), i.e. the complement of the union appearing in the CDF. Set \(a=t^{-2}\) and \(\eta=da-1\). Writing \(y_i=a-Z_i\ge0\), one has \(\sum_i y_i=\eta=2\varepsilon/\sqrt d+O(\varepsilon^2)\). The Dirichlet density tends to \(\Gamma(d/2)d^{d/2}/\pi^{d/2}\) at the unique point \(Z_i=1/d\), and the \((d-1)\)-simplex volume is \(\eta^{d-1}/(d-1)!\). This gives \(1-F_d(t)\sim B_{d,d}\varepsilon^{d-1}\). Mapping to the fixed simplex makes the multiplicative factor analytic and positive, proving exactly \(C^{d-2}\) but not \(C^{d-1}\) at \(\sqrt d\).

**5. Elementary three-dimensional form.** For \(d=3\), one squared-coordinate exceedance satisfies \(A_{3,1}(t)=1-1/t\), \(1\le t\le\sqrt3\). Define \(b=1/t\) and, for \(\sqrt2<t<\sqrt3\),
\[
J(t)=\frac4\pi\left[\arctan\sqrt{1-2b^2}-b\arccos\!\left(\frac{b}{\sqrt{1-b^2}}\right)\right].
\]
Conditioning on the first spherical coordinate shows \(A_{3,2}(t)=J(t)\): the first coordinate is uniform on \([-1,1]\), and, given it, the remaining direction is uniform on a circle, leading to the elementary integral \((2/\pi)\int_b^{\sqrt{1-b^2}}\arccos(b/\sqrt{1-x^2})\,dx\). Integrating by parts evaluates it as \(J\). Inclusion–exclusion then gives
\[
F_3(t)=\begin{cases}
0,&t\le1,\\
3(1-1/t),&1<t\le\sqrt2,\\
3(1-1/t)-3J(t),&\sqrt2<t<\sqrt3,\\
1,&t\ge\sqrt3.
\end{cases}
\]
At the first interior threshold \(B_{3,2}=2^{7/4}\Gamma(3/2)/(\pi\Gamma(5/2))\) as specified by the general formula, and at the endpoint \(B_{3,3}=\sqrt3/\pi\). The branch formula is a separate check of the onset theorem.

## Verification
The supplied `central_chord_checker.py` independently generates Haar-uniform Gaussian directions in dimensions two and three, checks the exact explicit CDF at eleven interior thresholds in each dimension, compares the three-dimensional two-face probability with an independent one-dimensional conditional integral, and checks contact-asymptotic coefficients in dimensions three and four using separate quadratures. It runs 69 consistency checks with a fixed random seed. Its finite simulations and quadratures corroborate but do not establish the universal statement; the analytical proof above establishes the exact CDF, thresholds, coefficients and differentiability for all integers \(d\ge2\). Reproduce with `python central_chord_checker.py` using numpy and scipy.

## Relationship to prior work
Finch's *Width Distributions for Convex Regular Polyhedra* (arXiv:1110.0671, 2011) treats uniform-direction **projection widths** of a cube, using its support function. The central chord here uses the **radial function** \(1/\|U\|_\infty\), which is a different random variable and is not given by Finch's width moments. Ciccariello's 2014 paper (arXiv:1401.7950) studies isotropic chord-length densities through a solid and analyzes an octahedron; its sampling is not restricted to centroid-passing lines. General spherical Gaussian/Dirichlet coordinate methods underlie the derivation and are not novel. Coleman (1981) examines three kinds of random intercepts through three-dimensional boxes, while Steinerberger (2011) studies random chords in high-dimensional cubes; their complete texts were not accessible, so detailed historical overlap for their exact sampling measures remains a residual priority risk. The precise all-dimensional threshold and differentiability hierarchy derived here was not identified in the inspected literature. No assertion of exhaustive historical priority is made.

## Limitations
This theorem is for the centered cube and uniform directions through its center. It does not apply without change to isotropic affine random lines, position-biased probes, arbitrary boxes or non-Euclidean direction laws. The general CDF is expressed by finite Dirichlet integrals, not an elementary closed form in every dimension. The proof does not assert new spherical-coordinate distributions or elementary support bounds, and historical originality remains qualified by incomplete access to two plausible earlier works.

## References
1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671v1, first public 2011-10-04, https://arxiv.org/abs/1110.0671.
2. S. Ciccariello, *The chord-length probability density of the regular octahedron*, arXiv:1401.7950v1, first public 2014-01-30, https://arxiv.org/abs/1401.7950.
3. R. Coleman, *Intercept lengths of random probes through boxes*, Journal of Applied Probability 18 (1981), 276–282, DOI 10.2307/3213189. Abstract available; full text not inspected.
4. S. Steinerberger, *Extremal uniform distribution and random chord lengths*, Acta Math. Hungar. 130 (2011), 321–339, DOI 10.1007/s10474-010-0067-x. Abstract available; full text not inspected.
