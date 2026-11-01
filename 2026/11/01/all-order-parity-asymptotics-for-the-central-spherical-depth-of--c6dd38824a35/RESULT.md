# All-order parity asymptotics for the central spherical depth of regular polygons

## Finding

Let \(P_n\subset\mathbb R^2\) be a nondegenerate regular \(n\)-gon, \(n\ge3\), centered at the origin. Let \(X,Y\) be independent points uniformly distributed with respect to area in \(P_n\), and let
\[
D_n=\Pr\{0\in B_{[X,Y]}\}=\Pr\{X\cdot Y\le0\},
\]
where \(B_{[X,Y]}\) is the disk with diameter \([X,Y]\). The probability is independent of the size and orientation of the polygon.

For every even \(n\), \(D_n=1/2\). For odd \(n\to\infty\),
\[
\boxed{D_n=\frac12-(-1)^{(n-1)/2}\left(\frac{5\pi^4}{192n^5}+\frac{7\pi^6}{720n^7}+O(n^{-9})\right).}
\]
More generally, for each integer \(M\ge0\) there are rational coefficients \(c_0,\ldots,c_M\), independent of \(n\), such that along the odd integers,
\[
D_n=\frac12-(-1)^{(n-1)/2}\left(\sum_{j=0}^{M}\frac{c_j\pi^{4+2j}}{n^{5+2j}}+O_M(n^{-7-2M})\right),
\qquad c_0=\frac5{192},\quad c_1=\frac7{720}.
\]
The coefficients admit an explicit recursive computation from the Taylor series of \(\sec^2\) and the Dirichlet beta values \(\beta(2j+1)\). In particular, the rate \(n^{-5}\) and its coefficient are exact. The mod-four sign pattern itself and the general Fourier representation of the probability were previously observed; they are not asserted to be new here.

## Assumptions and scope

The polygon is Euclidean, regular, and centered at its rotational center; area measure is normalized to total mass one. The random points are independent and sampled from its interior. For even \(n\), central symmetry gives the stated equality. Odd integers \(n\) are at least three. The asymptotics concern only \(n\to\infty\) through odd integers; the error constants need not be uniform over all \(n\ge3\). No conclusion is asserted for arbitrary nonregular polygons or for sample distributions other than uniform area.

Define \(a=\pi/n\) and, for positive integers \(k\),
\[
b_{k,n}=\frac1{2\tan a}\int_{-a}^a\sec^2t\cos(knt)\,dt.
\]
The integral gives a dimensionless, real Fourier coefficient of the probability distribution of a random direction from the center. For odd \(n\), the exact identity underlying the result is
\[
D_n-\frac12=-\frac{2(-1)^{(n-1)/2}}{\pi n}
\sum_{j=0}^{\infty}\frac{(-1)^j b_{2j+1,n}^{\,2}}{2j+1}.
\tag{1}
\]
The series is absolutely convergent. This identity is the specialization of the standard Fourier approach to spherical depth, not the novelty claim.

## Proof

**Step 1: angular density.** Normalize the inradius of \(P_n\) to one. If \(t\) is the angular displacement from the nearest outward facet normal, then \(|t|\le a\) and the radial boundary is \(\rho(t)=\sec t\). Polar integration shows that the direction of a uniform point has density proportional to \(\rho(t)^2=\sec^2t\). The mass in one period \([-a,a]\) is \(1/n\); normalized to one period, the density is \(g(t)=\sec^2t/(2\tan a)\). Consequently, the nonzero Fourier modes on the full circle occur only at frequencies \(kn\), with coefficients \(b_{k,n}\) above.

**Step 2: depth Fourier formula.** Thales' criterion is \(X\cdot Y\le0\), equivalent (outside a null set) to the difference of their directions lying between \(\pi/2\) and \(3\pi/2\). The difference-density Fourier coefficients are squared angular-density coefficients, so
\[
D_n=\frac12-\frac2{\pi n}
\sum_{\substack{k\ge1\\k\text{ odd}}}
\frac{\sin(kn\pi/2)}{k}\,b_{k,n}^{\,2}.
\tag{2}
\]
For odd \(n\), substituting \(\sin((2j+1)n\pi/2)=(-1)^{(n-1)/2+j}\) yields (1). For even \(n\), all such sine factors vanish. Two integrations by parts on each period give \(b_{k,n}=O_n(k^{-2})\), establishing absolute convergence.

**Step 3: a uniform large-\(n\) coefficient expansion.** Change variables \(t=az\), writing \(b=\pi k\). As \(n\to\infty\),
\[
\sec^2(az)=1+a^2z^2+\frac23a^4z^4+O(a^6z^6),\quad
\frac a{\tan a}=1-\frac{a^2}{3}+O(a^4).
\]
For every integer \(k\ge1\), integration by parts gives
\[
\int_0^1z^2\cos(bz)\,dz=\frac{2(-1)^k}{b^2},\qquad
\int_0^1z^4\cos(bz)\,dz=(-1)^k\left(\frac4{b^2}-\frac{24}{b^4}\right).
\]
The constant term integrates to zero. Substitution and collection of powers give
\[
\boxed{b_{k,n}=(-1)^k\left[\frac2{k^2n^2}
+\frac1{n^4}\left(\frac{2\pi^2}{k^2}-\frac{16}{k^4}\right)\right]
+O\!\left(\frac1{k^2n^6}\right).}
\tag{3}
\]
The remainder is uniform for \(k\ge1\) as \(n\to\infty\): after subtracting the fourth-order Taylor polynomial, its rescaled even remainder has values and first two derivatives of order \(O(a^6)\) on \([-1,1]\); two integrations by parts with vanishing endpoint sine terms bound its cosine coefficient by \(O(a^6/k^2)\). Multiplication by \(a/\tan a\) preserves the bound.

**Step 4: summation.** For odd \(k\), squaring (3) yields uniformly
\[
b_{k,n}^{\,2}=\frac4{k^4n^4}
+\frac1{n^6}\left(\frac{8\pi^2}{k^4}-\frac{64}{k^6}\right)
+O\!\left(\frac1{k^4n^8}\right).
\]
Define \(\beta(s)=\sum_{j\ge0}(-1)^j/(2j+1)^s\). Inserting this expansion into (1) gives
\[
D_n-\frac12=-(-1)^{(n-1)/2}\left[
\frac{8\beta(5)}{\pi n^5}
+\frac{16\pi\beta(5)-128\beta(7)/\pi}{n^7}
+O(n^{-9})\right].
\]
The classical exact evaluations \(\beta(5)=5\pi^5/1536\) and \(\beta(7)=61\pi^7/184320\) yield the displayed coefficients \(5\pi^4/192\) and \(7\pi^6/720\).

**Step 5: all-orders structure.** The even analytic expansion of \(\sec^2(az)\) on \(|z|\le1\), together with the even analytic series of \(a/\tan a\), supplies a uniform-in-\(k\) asymptotic expansion of \(b_{k,n}\) in even powers of \(n^{-1}\). Every coefficient is \((-1)^k\) times a finite rational linear combination of monomials \(\pi^{2r}k^{-2s}\), with \(s\ge1\). For any prescribed order, twice integrating by parts in the remainder gives a bound \(O_M(k^{-2}n^{-2M-4})\). Squaring, dividing by \(k\), and summing produces only convergent beta values at positive odd integers at least five. These beta values are rational multiples of corresponding odd powers of \(\pi\), which proves the asserted full odd-power expansion with rational coefficients and the stated remainder. This is an asymptotic series, not a claim of convergence for fixed \(n\).

## Verification

The standalone file `verify.py` evaluates the exact Fourier formula with independently computed quadrature coefficients and also calculates the probability from a discretized angular autocorrelation. It compares the two at several odd orders; checks the equilateral special case \(1/3+\log(3)/6\); and displays the fifth- and seventh-order scaled errors. These finite tests are independent consistency checks, not a proof of the asymptotic expansion. The analytic proof above provides its uniform error control.

## Relationship to prior work

Rabinowitz, *The Probability That the Incenter of a Triangle Lies in a Random Diameter Disk* (arXiv:2608.27491, first public date 2026-08-26), gives the general angular cone-measure transfer and the exact equilateral value, and treats arbitrary triangles rather than the large-order regular-polygon regime.

The October 2025 Mathematics Stack Exchange discussion *What planar convex shape maximizes the probability that a random circle contains the centre?* (question 5101873) already contains the radial double integral, its Fourier representation for regular polygons, and the mod-four sign observation. This work does not claim any of those known assertions as new. The new assertion is the all-order, uniform-asymptotic expansion and the explicit first two sharp nonzero coefficients with remainder orders; the derivation requires uniform control of the Fourier index when expanding the angular density.

Bremner and Shahsavarifar, *An Optimal Algorithm for Computing the Spherical Depth of Points in the Plane* (arXiv:1702.07399), studies finite-sample computation and does not address the large-side-number population asymptotics here.

## Limitations

The precise historical priority of the higher-order asymptotic coefficients is not independently certified. A prior exact Fourier formula already determines \(D_n\) in principle, so the contribution is asymptotic analysis of that formula, not a new integral representation or a new sign theorem. Uniform estimates are proved only in the large-odd-order regime. No claim about extremality among all convex bodies is made. The computational checks do not establish infinite statements, and no independent audit has been performed.

## References

1. S. Rabinowitz, *The Probability That the Incenter of a Triangle Lies in a Random Diameter Disk*, arXiv:2608.27491 (2026), https://arxiv.org/abs/2608.27491.
2. *What planar convex shape maximizes the probability that a random circle contains the centre?*, Mathematics Stack Exchange, question 5101873 (2025), https://math.stackexchange.com/questions/5101873/what-planar-convex-shape-maximizes-the-probability-that-a-random-circle-contains.
3. Bremner and Shahsavarifar, *An Optimal Algorithm for Computing the Spherical Depth of Points in the Plane*, arXiv:1702.07399 (2017), https://arxiv.org/abs/1702.07399.
