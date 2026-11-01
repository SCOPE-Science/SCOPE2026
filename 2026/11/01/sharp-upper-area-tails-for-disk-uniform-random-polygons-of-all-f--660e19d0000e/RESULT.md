# Sharp upper-area tails for disk-uniform random polygons of all fixed orders at least four

## Finding

Fix an integer \(n\ge 4\). Let \(X_1,\ldots,X_n\) be independent, uniform-by-area points in the closed Euclidean unit disk, and let
\[
Z_n=\operatorname{Area}\bigl(\operatorname{conv}\{X_1,\ldots,X_n\}\bigr),
\qquad M_n=\frac n2\sin\frac{2\pi}{n}.
\]
Then, as \(\varepsilon\downarrow0\),
\[
\boxed{\Pr\{Z_n>M_n-\varepsilon\}
=C_n\,\varepsilon^{(3n-1)/2}
\bigl(1+O_n(\sqrt\varepsilon)\bigr),}
\]
where the explicit strictly positive coefficient is
\[
\boxed{C_n=\frac{2^n(n-1)!}{\sqrt n\,\pi^{(n-1)/2}
\bigl(\sin(2\pi/n)\bigr)^{(3n-1)/2}
\Gamma((3n+1)/2)}.}
\]
For comparison, the previously obtained random-triangle specialization is
\[
\Pr\left\{Z_3>\frac{3\sqrt3}{4}-\varepsilon\right\}
=\frac{32}{27\pi\sqrt3}\,\varepsilon^4\bigl(1+O(\sqrt\varepsilon)\bigr).
\]
The power \((3n-1)/2\) reflects \(n\) independently constrained inward radial displacements and \(n-1\) quadratically constrained angular degrees of freedom. The quantity \(Z_n\) is the area of the full convex hull, not the signed area of an arbitrarily ordered polygon.

## Assumptions and scope

The disk has radius one; scale by the square of the radius for any other fixed disk. The sample size \(n\ge4\) is a fixed integer, and the remainder constant may depend on \(n\). Points are independent and have normalized planar Lebesgue distribution, **not** arclength distribution on the circumference. The event is strict, but its boundary has probability zero. No joint limit with \(n\to\infty\) is asserted.

The classical extremal fact used below is that the maximum area of a convex polygon with at most \(n\) vertices contained in the disk is \(M_n\), attained only by an inscribed regular \(n\)-gon (up to rotation and vertex labels). With the degenerate value \(M_2:=0\), one has \(M_n>M_{n-1}\). A polygon attaining the upper endpoint therefore uses all \(n\) sample points as its vertices.

## Proof

**1. Localization at the regular polygons.** The function of the sample points given by their convex-hull area is continuous on the compact product of \(n\) closed disks. Its maximizers are precisely the regular inscribed \(n\)-gons. For the boundary conclusion, observe that at any maximizer every point must be an exposed polygon vertex because the best \((n-1)\)-gon has smaller area; moving any such vertex while keeping the others fixed changes the local area affinely with a nonzero gradient, so an interior vertex cannot maximize. The classical circumscribed-disk extremal inequality then forces equal angular gaps. Compactness implies that every sample with \(M_n-Z_n\) sufficiently small lies in a small neighborhood of this rotation/permutation family. Within this neighborhood the angularly ordered points are in strictly convex position and their convex-hull area is the usual shoelace area in circular order.

**2. Coordinates and their density.** Put \(\alpha=2\pi/n\), \(a=\sin\alpha>0\), and \(b=a/4\). Write the points in increasing polar-angle order, with radii \(r_i=1-u_i\), \(u_i\ge0\), and consecutive cyclic angular gaps
\[
\Delta_i=\alpha+\delta_i\quad (1\le i\le n),
\qquad \sum_{i=1}^{n}\delta_i=0.
\]
Use \(\delta_1,\ldots,\delta_{n-1}\) as the free coordinates and set \(\delta_n=-\sum_{i<n}\delta_i\). The radial joint density is \(\prod_i2(1-u_i)\). Since the ordered angular sample has density \(n!/(2\pi)^n\), integrating its smallest polar angle over the allowed interval of length \(\Delta_n\) gives the exact free-gap density
\[
f(\delta_1,\ldots,\delta_{n-1})
=\frac{n!}{(2\pi)^n}\left(\alpha-\sum_{i=1}^{n-1}\delta_i\right).
\]
In particular \(f(0)=(n-1)!/(2\pi)^{n-1}\). These densities already include all permutations and rotations of the maximizing family; no additional combinatorial multiplicity is needed.

**3. Mixed linear–quadratic deficit.** In the localized convex-position region,
\[
Z_n=\frac12\sum_{i=1}^{n}r_i r_{i+1}\sin\Delta_i,
\quad r_{n+1}=r_1.
\]
The first radial derivative at the regular polygon is \(a\), while the first angular variation vanishes because the gaps sum to \(2\pi\). Taylor expansion yields
\[
M_n-Z_n
=a\sum_{i=1}^{n}u_i+b\sum_{i=1}^{n}\delta_i^2
+O_n\!\left(\Bigl(\sum_i u_i\Bigr)^2
+\Bigl(\sum_i u_i\Bigr)\|\delta\|
+\|\delta\|^3\right).
\]
Both leading terms are nonnegative and coercive in their respective coordinates. By shrinking the neighborhood, the exact deficit is bounded above and below by fixed positive multiples of \(\sum u_i+\|\delta\|^2\). Consequently the event of deficit below \(\varepsilon\) has \(u_i=O_n(\varepsilon)\) and \(\delta_i=O_n(\sqrt\varepsilon)\). The displayed remainder is then uniformly \(O_n(\varepsilon^{3/2})\).

**4. Evaluation of the limiting cap volume.** Set \(m=n-1\) and \(d=(\delta_1,\ldots,\delta_m)^T\). The angular quadratic form is
\[
Q(d)=b\,d^T(I_m+\mathbf 1\mathbf 1^T)d,
\qquad \det\bigl(b(I_m+\mathbf1\mathbf1^T)\bigr)=n b^m.
\]
For \(0\le Q(d)<t\), the volume of the allowed positive radial simplex
\(a\sum_i u_i<t-Q(d)\) equals \((t-Q(d))^n/(n!a^n)\). Diagonalizing the positive definite angular form gives
\[
\int_{\mathbb R^m}(t-Q(d))_+^n\,\mathrm d d
=\frac{\pi^{m/2}\Gamma(n+1)}{\sqrt n\,b^{m/2}\Gamma(n+1+m/2)}\,
 t^{n+m/2}.
\]
This is the standard beta-ball integral, justified for every \(n\ge4\).

Multiplying by the angular density \(f(0)\), the radial density \(2^n\), and the radial-simplex factor \(1/(n!a^n)\) produces
\[
\frac{2^n(n-1)!}{\sqrt n\,\pi^{(n-1)/2}a^{(3n-1)/2}\Gamma((3n+1)/2)}
\,t^{(3n-1)/2}=C_n t^{(3n-1)/2}.
\]

**5. Controlled remainder.** On the localized event, the true deficit differs from its mixed linear–quadratic model by at most \(K_n\varepsilon^{3/2}\). The true event can therefore be sandwiched between model caps with thresholds \(\varepsilon(1-K'_n\sqrt\varepsilon)\) and \(\varepsilon(1+K'_n\sqrt\varepsilon)\), for sufficiently small \(\varepsilon\). The product sampling density differs uniformly from its value at the maximizer by \(O_n(\sqrt\varepsilon)\). Since the model cap volume scales exactly as the threshold to \((3n-1)/2\), both comparisons yield the stated relative \(O_n(\sqrt\varepsilon)\) remainder. The complement of the localization neighborhoods contributes zero for all sufficiently small \(\varepsilon\). This proves the theorem.

## Verification

The standalone file `verify_polygon_tail.py` checks the Gram-form determinant and inverse for dimensions \(n=3,\ldots,15\), the exact first and second Taylor coefficients for \(n=3,4,6\), and the normalization against the published boundary-sampling constant. It also runs a seeded importance-sampling consistency test for \(n=3,4,5,6\). At \(\varepsilon=0.001\) the near-cap ratios were respectively \(0.99656,0.99938,0.99764,0.99469\).

The independent `test_enlarged.py` checks a larger mixed cap and estimates the whole near-maximal event; for \(n=3,4\) at \(\varepsilon=0.001\) the ratios to the asserted leading law were \(1.00140\) and \(0.99985\), with Monte Carlo standard errors below \(0.0013\). These finite stochastic checks test calculations but are not proofs; the proof is Steps 1–5.

For an additional analytical consistency test, the boundary-only version of Step 4 yields the leading constant \((n!)/K_{2n}\), with \(K_{2n}\) as in the 2013 circle-sampling theorem by Koroleva and Nikitin. The interior law has an additional \(n\) radial powers and a different gamma factor.

## Relationship to prior work

Koroleva and Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons* (first public preprint January 7, 2013), establish the angular near-maximum area law for \(n\) points **sampled from the circumference** and corresponding extreme-value limits for subsets of large boundary samples. Their Section 2.2 and Lemma 2.3 supply the boundary comparison. They do not address independent **area-uniform interior** points or the mixed radial/angular exponent and leading coefficient above.

Marckert, *Probability that n random points in a disk are in convex position* (2014), treats the probability of convex position and exact vertex-count distributions, not the area endpoint. Paouris and Pivovarov (2013) study small-volume probabilities and general distributional estimates for different random convex sets, rather than the present sharp **upper** endpoint of a fixed-size disk sample. The classical triangle's mean area \(35/(48\pi)\) and related general integrals do not determine this endpoint law. The new theorem is the full family for every fixed \(n\ge4\), not a single numerical exercise. An earlier near-maximal disk-triangle calculation already yields the \(n=3\) upper-tail constant shown above, which is included solely as a consistency check and is not claimed as new.

## Limitations

No closed formula is asserted for the entire distribution of \(Z_n\). The estimate is for each fixed \(n\) and is not uniform in \(n\). The argument exploits the disk's unique (modulo rotation) maximizing regular polygon and the boundary density of area-uniform sampling; it is not asserted for other convex bodies or sampling densities. The result does not prove a Weibull law for maxima over overlapping \(n\)-tuples in a much larger sample, where dependence requires separate analysis. Literature searches cannot establish absolute historical priority; the closest available complete primary text concerns boundary sampling.

## References

1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360, first posted 2013-01-07, especially Section 2.2 and Lemma 2.3. https://arxiv.org/abs/1301.1360
2. Jean-François Marckert, *Probability that n random points in a disk are in convex position*, arXiv:1402.3512, first posted 2014-02-14, especially the introduction and Theorem 1. https://arxiv.org/abs/1402.3512
3. Grigoris Paouris and Peter Pivovarov, *Small-Ball Probabilities for the Volume of Random Convex Sets*, Discrete & Computational Geometry 49 (2013), 601–646, doi:10.1007/s00454-013-9492-2. https://doi.org/10.1007/s00454-013-9492-2
4. Eric W. Weisstein, *Disk Triangle Picking*, MathWorld, accessed 2026-10-30. https://mathworld.wolfram.com/DiskTrianglePicking.html
