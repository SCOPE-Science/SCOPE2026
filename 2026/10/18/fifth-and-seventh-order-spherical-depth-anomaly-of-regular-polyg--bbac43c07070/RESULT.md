# Fifth- and seventh-order spherical-depth anomaly of regular polygons

## Finding
Let \(P_n\subset\mathbb R^2\) be a nondegenerate regular \(n\)-gon, \(n\ge3\), centered at the origin. Choose \(X,Y\) independently from normalized planar area measure on \(P_n\), and put
\[
D_n=\Pr\bigl(0\in\operatorname{disk}_{XY}\bigr)
=\Pr(X\cdot Y\le0),
\]
where \(\operatorname{disk}_{XY}\) is the closed disk with diameter \(XY\). Along odd integers \(n\to\infty\),
\[
\boxed{D_n-\tfrac12=(-1)^{(n+1)/2}\left(\frac{5\pi^4}{192n^5}+\frac{7\pi^6}{720n^7}+O(n^{-9})\right).}
\]
The constants are exact, and in particular the \(n^{-5}\) convergence exponent and its coefficient are sharp. For every even \(n\), \(D_n=1/2\) exactly by central symmetry. The already-known qualitative modulo-four sign rule for odd \(n\) is recalled for context, not asserted as an independent new discovery.

## Assumptions and scope
The probability refers to two independent **area-uniform interior points**, not two uniformly distributed vertex indices; the center is the dihedral center. Scaling and rotating the polygon do not change \(D_n\). The expansion holds along odd integers as \(n\to\infty\); the error constant is absolute for sufficiently large odd \(n\). No all-\(n\) finite error bound with the displayed two coefficients is claimed. The conventional notation \(O(n^{-9})\) means a uniform bounded remainder times \(n^{-9}\).

## Proof
**1. Exact directional law.** Set \(\alpha=\pi/n\) and let \(r\) be the apothem. In the angular sector \(-\alpha\le t\le\alpha\) about a side's outward normal, the radial boundary is \(r\sec t\). Since the polygon area is \(nr^2\tan\alpha\), the density of the angle \(\Theta=\arg X\) is
\[
f_n(\theta)=\frac{\sec^2t}{2n\tan\alpha},\qquad
 t\equiv\theta\pmod{2\alpha},\quad -\alpha\le t\le\alpha.
\]
This follows directly from integrating the planar area element \(s\,ds\,d\theta\) along the radius. It agrees with the known polygonal cone-measure transfer principle. It is a probability density, since the integral of \(\sec^2t\) on one sector is \(2\tan\alpha\).

**2. Exact spectral identity.** Write \(\widehat f_n(\ell)=\mathbb E(e^{i\ell\Theta})\). Rotational symmetry gives \(\widehat f_n(\ell)=0\) unless \(n\mid\ell\). For integer \(j\),
\[
A_{n,j}:=\widehat f_n(jn)
=\frac1{\tan(\pi/n)}\int_0^{\pi/n}\sec^2 t\cos(jnt)\,dt.
\]
These coefficients are real. For the angular difference \(\Delta=\arg X-\arg Y\), the Fourier coefficients of its law equal \(|\widehat f_n(\ell)|^2\). The angular indicator of \(\cos\Delta\le0\) has Fourier series (in the integrated sense)
\[
{\bf1}_{\{\cos t\le0\}}=\frac12-\frac2\pi
\sum_{\substack{\ell\ge1\\\ell\ \mathrm{odd}}}
\frac{(-1)^{(\ell-1)/2}}\ell\cos(\ell t).
\]
There is no atom at its discontinuities, and the resulting correlation series is absolutely convergent (indeed the coefficients below have quadratic decay). Therefore, when \(n\) is odd,
\[
D_n-\frac12=-\frac2{\pi n}\sum_{\substack{j\ge1\\j\ \mathrm{odd}}}
\frac{(-1)^{(jn-1)/2}}j A_{n,j}^2. \tag{1}
\]
When \(n\) is even, all odd angular harmonics vanish, so \(D_n=1/2\) exactly.

**3. Uniform harmonic expansion.** Substitute \(u=nt\) to obtain
\[
A_{n,j}=\frac1{n\tan(\pi/n)}\int_0^\pi \sec^2(u/n)\cos(ju)\,du.
\]
For fixed \(n\ge5\), the integrand is smooth on this interval. The Taylor formulae, with remainders uniform on \(0\le u\le\pi\), are
\[
\sec^2(u/n)=1+\frac{u^2}{n^2}+\frac{2u^4}{3n^4}+R_n(u),
\qquad
\frac1{n\tan(\pi/n)}=\frac1\pi\left(1-\frac{\pi^2}{3n^2}+O(n^{-4})\right).
\]
The remainder \(R_n\) and its first two \(u\)-derivatives admit bounds of respective orders \(n^{-6}\), \(n^{-6}\), \(n^{-6}\) on \([0,\pi]\). Twice integrating its cosine integral by parts (with the first boundary sine terms zero) yields \(\int_0^\pi R_n(u)\cos(ju)\,du=O(j^{-2}n^{-6})\), uniformly in integers \(j\ge1\). The analogous expansion of the prefactor is also uniform after integrating twice. For nonzero integer \(j\),
\[
\int_0^\pi\cos(ju)\,du=0,\quad
\int_0^\pi u^2\cos(ju)\,du=\frac{2\pi(-1)^j}{j^2},
\]
\[
\int_0^\pi u^4\cos(ju)\,du=(-1)^j\left(\frac{4\pi^3}{j^2}-\frac{24\pi}{j^4}\right).
\]
Consequently, uniformly for all positive integers \(j\) and all sufficiently large \(n\),
\[
A_{n,j}=(-1)^j\left[\frac{2}{j^2n^2}
+\frac1{n^4}\left(\frac{2\pi^2}{j^2}-\frac{16}{j^4}\right)
+O\left(\frac1{j^2n^6}\right)\right]. \tag{2}
\]
Squaring gives a uniform-in-\(j\) estimate
\[
A_{n,j}^2=\frac4{j^4n^4}
+\frac1{n^6}\left(\frac{8\pi^2}{j^4}-\frac{64}{j^6}\right)
+O\left(\frac1{j^4n^8}\right). \tag{3}
\]
The \(j^{-5}\)-summability after multiplying by \(1/j\) in (1) justifies termwise summation of (3) and gives a total error \(O(n^{-9})\).

**4. Evaluation of the constants.** For odd \(j,n\),
\[
(-1)^{(jn-1)/2}=(-1)^{(n-1)/2}(-1)^{(j-1)/2}.
\]
Define the Dirichlet beta values
\[
\beta(s)=\sum_{j\ge1,\ j\ \mathrm{odd}}\frac{(-1)^{(j-1)/2}}{j^s}.
\]
Combining (1) and (3) yields
\[
D_n-\frac12=(-1)^{(n+1)/2}
\left[\frac{8\beta(5)}{\pi n^5}
+\frac{16\pi\beta(5)-128\beta(7)/\pi}{n^7}
+O(n^{-9})\right].
\]
The classical exact evaluations \(\beta(5)=5\pi^5/1536\) and \(\beta(7)=61\pi^7/184320\) turn the two coefficients into \(5\pi^4/192\) and \(7\pi^6/720\), respectively. This proves the claimed sharp expansion. Since \(5\pi^4/192>0\), there can be no better decay exponent than five along either odd congruence class.

## Verification
The standalone `check_depth_asymptotic.py` numerically evaluates the exact Fourier integral, independently computes the probability by circular FFT convolution on 262144 angular grid points, tests the equilateral-triangle value \(1/3+(\log3)/6\), and checks the two-term approximation and individual harmonic expansions on finite samples. It returned `VERIFY_OK independent_FFT_checks=10 coefficients=9 triangle_baseline=1`. In particular, for \(n=5,7,9,11\), the Fourier evaluations of \(D_n\) are approximately \(0.499054315985\), \(0.500162939595\), \(0.499955019327\), and \(0.500016241476\). Finite numerical experiments do not prove the uniform remainder or the infinite-series identity; those follow from the preceding analytic argument.

## Relationship to prior work
The concept of spherical depth was introduced by Elmore, Hettmansperger and Xuan (2006), and Bremner and Shahsavarifar (2017) gave an optimal planar computational algorithm. Rabinowitz (2026, arXiv:2608.27491) supplies the triangle-incenter formula and the general polygonal directional cone-measure transfer. A 2025 Mathematics Stack Exchange discussion, question 5101873, **already records** the regular-polygon Fourier formulation, the qualitative modulo-four sign distinction, and an argument for the equilateral triangle's maximality among regular polygons. None of those facts is claimed as new here. The narrower new quantitative assertion is the explicitly evaluated fifth- and seventh-order spherical-depth asymptotic and its uniform \(O(n^{-9})\) remainder. Relevant available indexed geometric research records concern different chord, normal or area invariants rather than this spherical-depth expansion.

## Limitations
This is a deterministic asymptotic statement about the distributional spherical depth at the center of regular polygons. It neither determines the maximizing body among arbitrary convex sets nor gives a closed elementary expression for every finite odd \(n\). The known Fourier identity alone is not a novelty claim. An unindexed independent asymptotic computation could predate the present formula. 

## References
1. S. Rabinowitz, *The Probability That the Incenter of a Triangle Lies in a Random Diameter Disk*, arXiv:2608.27491, initially posted 2026-08-26. https://arxiv.org/abs/2608.27491
2. D. Bremner and R. Shahsavarifar, *An Optimal Algorithm for Computing the Spherical Depth of Points in the Plane*, arXiv:1702.07399, initial posting 2017-02-23. https://arxiv.org/abs/1702.07399
3. *What planar convex shape maximizes the probability that a random circle contains the centre?*, Mathematics Stack Exchange, question 5101873, initial discussion 2025-10-14; relevant regular-polygon and Fourier answers from 2025-10-17. https://math.stackexchange.com/questions/5101873/
4. R. T. Elmore, T. P. Hettmansperger and F. Xuan, *Spherical data depth and a multivariate median*, DIMACS Series 72 (2006), pp. 87–101. https://datacolorado.com/publication/dimacs-06/
