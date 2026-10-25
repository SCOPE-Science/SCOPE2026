# Conditional area law for random cyclic quadrilaterals at a fixed diagonal angle

## Finding

Let four points be independent and uniformly distributed by arclength on the unit circle, and let \(Q\) be their convex quadrilateral. Write \(K=\operatorname{area}(Q)\), and let \(\Delta\in(0,\pi/2)\) be the smaller angle between its two diagonals. The **complete conditional law of \(K\) given \(\Delta=t\)**, for every fixed \(0<t<\pi/2\), is the law of
\[
K_t=\sin t\,\bigl(\cos U-\cos V\bigr),
\qquad U\sim\operatorname{Unif}(0,t),\quad V\sim\operatorname{Unif}(t,2\pi-t),
\]
where \(U,V\) are independent. In particular, its support is exactly \([0,2\sin t]\) and its conditional cumulative distribution function is the following explicit one-dimensional integral. Set \(c=\cos t\) and
\[
H_t(v)=\begin{cases}
0,&v\le-1,\\
(\pi-\arccos v)/(\pi-t),&-1<v<c,\\
1,&v\ge c.
\end{cases}
\]
For \(0<k<2\sin t\),
\[
\boxed{\Pr(K\le k\mid\Delta=t)
=1-\frac1t\int_0^t H_t\!\left(\cos u-\frac{k}{\sin t}\right)du.}
\]
The conditional distribution is continuous, with conditional mean and variance
\[
\boxed{\mathbb E[K\mid\Delta=t]=\frac{\pi\sin^2t}{t(\pi-t)},}
\]
\[
\boxed{\operatorname{Var}(K\mid\Delta=t)=
\sin^2t\left[1+\frac{\sin(2t)}4\left(\frac1t-\frac1{\pi-t}\right)
-\sin^2t\left(\frac1{t^2}+\frac1{(\pi-t)^2}\right)\right].}
\]
As \(\varepsilon\downarrow0\), for each fixed \(t\in(0,\pi/2)\),
\[
\boxed{\Pr(K>2\sin t-\varepsilon\mid\Delta=t)
\sim \frac{\pi}{2t(\pi-t)\sin t}\,\varepsilon.}
\]
The value at \(t=\pi/2\) follows by continuity for the chosen regular conditional version. The angle's marginal density, \(12t(\pi-t)/\pi^3\) for \(0<t<\pi/2\), is prior knowledge, **not claimed as novel**. As consistency checks and consequences, the area moments are
\[
\mathbb E[K]=\frac3\pi,\qquad
\mathbb E[K^2]=\frac12+\frac{105}{16\pi^2},\qquad
\operatorname{Var}(K)=\frac12-\frac{39}{16\pi^2}.
\]
The claim of independent interest is the complete area distribution **conditional on the crossing angle**, together with its explicit conditional moments and its sharp conditional upper tail. The unconditional near-maximal-area exponent is already implied by existing inscribed-polygon area results and is not claimed here.

## Assumptions and scope

The sampling law is the product of four normalized arclength measures on the Euclidean unit circle. The points are distinct almost surely, and their cyclic order defines a strictly convex quadrilateral. Diagonals join opposite points in cyclic order. \(\Delta\) is the **unoriented acute angle** between the two diagonal lines. Conditional distributions at individual values of a continuous random variable mean the explicit continuous regular conditional version constructed below, not conditioning on a positive-probability event. The endpoints \(t=0\) and \(t=\pi/2\) have zero probability; the latter is defined by continuous extension if desired.

## Proof

1. Pick one of the four independent points as a *distinguished* point and rotate it to polar angle zero; list the other three counterclockwise. Let \(g_1,g_2,g_3,g_4>0\) be the successive circular angular gaps, summing to \(2\pi\). Because the three other polar angles are independent uniform angles relative to the distinguished point, \((g_1,g_2,g_3,g_4)/(2\pi)\sim\operatorname{Dirichlet}(1,1,1,1)\). Distinguishing a sampled vertex rather than always choosing the smallest absolute polar angle is essential here.

2. The direction of the chord joining angular positions \(\alpha\) and \(\beta\) is \((\alpha+\beta)/2+\pi/2\) modulo \(\pi\). Hence one oriented representative of the diagonal crossing angle is
\[T=(g_1+g_3)/2\in(0,\pi),\qquad \Delta=\min(T,\pi-T).\]
The Dirichlet aggregation and beta-gamma factorization show \(T/\pi\sim\operatorname{Beta}(2,2)\). Given \(T=t\), the two relative splits are independent uniforms, so there exist independent \(U\sim\operatorname{Unif}(0,t)\) and \(B\sim\operatorname{Unif}(0,\pi-t)\) with
\[g_1=2U,\quad g_3=2(t-U),\quad g_2=2B,\quad g_4=2(\pi-t-B).\]
Cycling the distinguished vertex by one position exchanges \(T\) and \(\pi-T\) but leaves \(K\) unchanged. Consequently the conditional area law at \(T=t\) equals that at \(T=\pi-t\), and it suffices to take \(t=\Delta\in(0,\pi/2)\).

3. The lengths of the two diagonals are \(2\sin(U+B)\) and \(2\sin(t-U+B)\); both arguments lie in \((0,\pi)\). The formula \(K=\tfrac12 d_1d_2\sin t\), followed by \(2\sin a\sin b=\cos(a-b)-\cos(a+b)\), yields
\[
K=\sin t\left[\cos(2U-t)-\cos(t+2B)\right].
\]
Since \(2U-t\) is uniform on \((-t,t)\), cosine symmetry replaces it by \(U'\sim\operatorname{Unif}(0,t)\); independently \(V=t+2B\sim\operatorname{Unif}(t,2\pi-t)\). Thus \(K=\sin t(\cos U'-\cos V)\) in conditional distribution. For these ranges \(\cos U'\in[\cos t,1]\) and \(\cos V\in[-1,\cos t]\); both have positive interior densities. This proves the exact support, positivity and continuity of the conditional law.

4. The variable \(Y=\cos V\) has cumulative distribution \(H_t\) as displayed. For \(z=k/\sin t\), conditioning on \(U'\) gives
\[
\Pr(K\le k\mid\Delta=t)
=\frac1t\int_0^t\Pr\bigl(Y\ge\cos u-z\bigr)du
=1-\frac1t\int_0^t H_t(\cos u-z)du.
\]
There are no equality atoms. Endpoint CDF values are zero and one by the support.

5. Independence gives
\[\mathbb E\cos U'=\frac{\sin t}{t},\quad
\mathbb E\cos V=-\frac{\sin t}{\pi-t},\]
\[\mathbb E\cos^2U'=\frac12+\frac{\sin2t}{4t},\quad
\mathbb E\cos^2V=\frac12-\frac{\sin2t}{4(\pi-t)}.\]
Taking first and second moments of their independent difference proves the conditional mean and variance.

6. At the conditional upper endpoint, write \(U'=u\) and \(V=\pi+v\). The deficit is
\[
2\sin t-K=\sin t\left[(1-\cos u)+(1+\cos(\pi+v))\right]
=\frac{\sin t}{2}(u^2+v^2)+O_t((u^2+v^2)^2).
\]
Near \((u,v)=(0,0)\), the joint density is \(1/[2t(\pi-t)]\) on the half-plane \(u\ge0\). Comparing the event with half-disks of squared radius \(2\varepsilon/\sin t\) gives the claimed sharp linear coefficient \(\pi/[2t(\pi-t)\sin t]\). This local argument is valid for every fixed interior angle \(t\).

7. The known beta marginal implies density \(f_\Delta(t)=12t(\pi-t)/\pi^3\), and by symmetry the oriented representative has density \(f_T(t)=6t(\pi-t)/\pi^3\) on \((0,\pi)\). Integrating the conditional moments gives
\[\mathbb E K=\frac6{\pi^2}\int_0^\pi\sin^2 t\,dt=\frac3\pi.\]
For the second moment, multiplying its conditional expression by \(f_T\) reduces the integral to
\[
\frac6{\pi^3}\int_0^\pi\sin^2t\left[t(\pi-t)+\frac{\pi-2t}{4}\sin2t+2\sin^2t\right]dt.
\]
The three contributions inside the integral are respectively \(\pi^3/12+\pi/4\), \(3\pi/32\), and \(3\pi/4\), hence \(\mathbb E K^2=1/2+105/(16\pi^2)\). Subtracting \((3/\pi)^2\) gives the variance. These unconditional identities are consistency checks, not the originality basis.

## Verification

`verify.py` reconstructs each quadrilateral from independent Cartesian circle coordinates, computes its area by the shoelace formula, and computes the *acute* diagonal angle from dot and determinant. It checks the conditional mean/variance in five narrow angular bins using 450,000 random quadrilaterals. Independently of Cartesian vertices, it samples the two cosine variables for four fixed angle values, checks the CDF against numerical one-dimensional quadrature at four area fractions, and checks unconditional moments and the already-known angular marginal. Run `python verify.py` with Python 3, NumPy and SciPy. Randomized tolerances are intentionally much looser than ordinary sampling uncertainty; no finite Monte Carlo sample constitutes a proof of the formula.

## Relationship to prior work

Koroleva–Nikitin (2013), Section 2.2 and Lemma 2.3, treat the unconditional near-maximum **area** of inscribed random polygons and their extreme-value consequences, including the four-vertex specialization; the present result does not claim their near-maximal area tail as new. Barahona Torres–Manrique-Mirón–Treviño-Aguilar (2019), Theorem 2.1, study an **angle** formed by a chord from two points sampled in the *disk* and an independently chosen horizontal chord; their sine density and sampling assumptions do not imply this conditional quadrilateral area law. Bortolotto–Souza (2025), Theorem 1, give the distribution of the radial location of the crossing of lines through independently sampled *circle-boundary* pairs. That radial marginal is not an area conditional on a diagonal angle and does not determine it. The previously available exact **angle-only** law for crossing diagonals of regular polygon vertices and its continuous beta-density limit is also expressly prior: an angle marginal cannot imply the family of conditional area distributions or their conditional variance. Related deterministic cyclic-quadrilateral area/side-variance bounds govern different parameters and are not stochastic angle-conditioned laws.

## Limitations

This theorem holds for four independent arclength-uniform boundary points of a Euclidean circle. It is not a statement about disk-interior sampling, random lines from motion-invariant measures, ellipse arclength sampling, independent randomly paired non-crossing chords, or regular finite vertex sets. The one-dimensional CDF integral is an exact numerical representation, not an assertion of an elementary primitive. No novelty is claimed for Dirichlet gap distributions, the diagonal-angle marginal, deterministic diagonal area formulas, or the unconditional near-maximum area exponent. Historical novelty is provisional pending independent exhaustive literature review, especially older random-chord sources not available in full.

## References

1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360v1, 7 January 2013, especially Section 2.2, Theorem 2, Lemma 2.3. https://arxiv.org/abs/1301.1360
2. J. I. H. Barahona Torres, P. C. Manrique-Mirón, and E. Treviño-Aguilar, *Angle distribution of two random chords in the disc: A sine law*, arXiv:1911.05576 (first publicly posted 13 November 2019), especially Section 2. https://arxiv.org/abs/1911.05576
3. C. Bortolotto and V. Souza, *Intersections of random chords of a circle*, arXiv:2504.12866v1, 17 April 2025, especially Theorem 1 and Section 1.2. https://arxiv.org/abs/2504.12866
4. R. E. Morton, *The expected number and angle of intersections between random curves in a plane*, Journal of Applied Probability 3 (1966), 559–562, DOI:10.2307/3212140. A different invariant random-intersections setting; cited for historical context only.
