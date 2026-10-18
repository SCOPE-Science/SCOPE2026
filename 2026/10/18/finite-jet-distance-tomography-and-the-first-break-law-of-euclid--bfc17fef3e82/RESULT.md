# Finite-jet distance tomography and the first-break law of Euclidean orthotopes

## Finding

Let \(d\ge3\), let \(a_1,\ldots,a_d>0\), and let \(X,Y\) be independent, volume-uniform points in the Euclidean orthotope \(K=\prod_{i=1}^d[0,a_i]\). Write \(V=\prod_i a_i\), \(a_*=\min_i a_i\), and \(F(r)=\Pr(\|X-Y\|_2\le r)\). For \(0\le k\le d\), put
\[
 c_{d,k}=\frac{\pi^{(d-k)/2}}{\Gamma(1+(d+k)/2)},\qquad e_k=e_k(a_1^{-1},\ldots,a_d^{-1}),\qquad e_0=1.
\]
Then the *entire short-distance law* is the exact polynomial
\[
 F(r)=P(r):=\frac1V\sum_{k=0}^{d}(-1)^k c_{d,k}e_k r^{d+k},\qquad 0\le r\le a_*.
\]

**Finite-jet inverse and sharpness.** Denote the coefficient of \(r^{d+k}\) in this local polynomial by \(\beta_{d+k}\). Its first \(d\) nonzero coefficients \(\beta_d,\ldots,\beta_{2d-1}\) uniquely determine \(\{a_1,\ldots,a_d\}\) (including their absolute scale), and fewer than \(d\) such consecutive leading coefficients do not determine generic orthotopes. Explicitly,
\[
 V=\frac{c_{d,0}}{\beta_d},\quad e_k=\frac{(-1)^k c_{d,0}\beta_{d+k}}{c_{d,k}\beta_d}\ (1\le k\le d-1),\quad e_d=\frac{\beta_d}{c_{d,0}}.
\]
The reciprocal side lengths are the roots of
\[
 T^d-e_1T^{d-1}+e_2T^{d-2}-\cdots+(-1)^d e_d=0.
\]
A proposed set of first \(d\) coefficients is realized by a positive orthotope precisely when \(\beta_d>0\) and this polynomial has \(d\) positive real roots, counted with multiplicity. The otherwise free last coefficient is forced:
\[
 \beta_{2d}=(-1)^d c_{d,d}\left(\frac{\beta_d}{c_{d,0}}\right)^2.
\]
If dimension is not supplied, it is identified by \(\lim_{r\downarrow0}\log F(r)/\log r=d\).

**Sharp first departure.** Let \(m=\#\{i:a_i=a_*\}\), and let \(\kappa_j=\pi^{j/2}/\Gamma(1+j/2)\) denote the volume of the unit Euclidean \(j\)-ball. For \(\varepsilon\downarrow0\),
\[
 F(a_*+\varepsilon)-P(a_*+\varepsilon)
 =\frac{8m\kappa_{d-1}(2a_*)^{(d-1)/2}}{a_*V(d+1)(d+3)}\,\varepsilon^{(d+3)/2}
 +O_K\left(\varepsilon^{(d+4)/2}\right).
\]
The displayed leading constant is strictly positive. Therefore \([0,a_*]\) is exactly the maximal initial radius interval on which the stated polynomial agrees with the distance distribution; the first breakpoint is the shortest side, with onset exponent \((d+3)/2\) and multiplicity-sensitive coefficient.

## Assumptions and scope

The side lengths are arbitrary positive real numbers, including repetitions. The random points are independent and uniform with respect to volume, and the distance is Euclidean. Orthogonal rigid motions and coordinate permutations do not change the observable. No assumption of distinct edges is required for reconstruction or the breakpoint formula; distinctness is invoked only when demonstrating the sharp generic lower bound on the number of coefficients. All coefficients and limits are *population-level* mathematical quantities, not finite-sample estimates.

## Proof

**1. Difference density and polynomiality.** In coordinate \(i\), the difference of two independent uniforms on \([0,a_i]\) has density \((a_i-|z_i|)_+/a_i^2\). Independence gives the difference-vector density
\[
 f_{X-Y}(z)=\frac1V\prod_{i=1}^d\left(1-\frac{|z_i|}{a_i}\right)_+.
\]
For \(0\le r\le a_*\), all coordinates of \(z\in B_d(r)\) satisfy \(|z_i|\le a_i\); the positive parts can be dropped. Expand the product over subsets \(I\subseteq\{1,\ldots,d\}\), integrate over the radius-\(r\) ball, and group subsets by cardinality. The ball monomial identity is
\[
 \int_{B_d(r)}\prod_{i\in I}|z_i|\,dz
 =\frac{\pi^{(d-|I|)/2}}{\Gamma(1+(d+|I|)/2)}r^{d+|I|}.
\]
This follows by expressing the ball integral using Gaussian integrals and radial scaling (or by repeated beta integrals). The subset sum is precisely the elementary symmetric polynomial \(e_{|I|}\) in reciprocal side lengths, proving the exact formula and its coefficient normalization.

**2. Reconstruction, feasibility, and optimal coefficient count.** Since \(c_{d,0}=\kappa_d>0\), the leading coefficient gives \(V\). Each subsequent coefficient through \(\beta_{2d-1}\) gives one successive elementary symmetric polynomial \(e_1,\ldots,e_{d-1}\); the product identity gives \(e_d=1/V\). Vieta's formulas therefore identify the multiset of positive reciprocal side lengths. Conversely any reconstructed positive-root multiset defines an orthotope having exactly those coefficients, proving the realizability criterion. The stated constraint on \(\beta_{2d}\) follows by substitution.

To prove sharpness, choose any \(d\) pairwise distinct positive reciprocal lengths \(s_1,\ldots,s_d\). Holding \(e_1,\ldots,e_{d-2},e_d\) fixed, perturb the remaining coefficient \(e_{d-1}\) slightly in the monic polynomial with these \(s_i\) as roots. Every sufficiently small real perturbation still has \(d\) distinct positive real roots, by continuity of simple real roots. It changes the orthotope without changing \(\beta_d,\ldots,\beta_{2d-2}\), the first \(d-1\) local coefficients. Therefore any shorter leading jet generically fails to distinguish shapes. The leading power of \(F(r)\) is \(d\), proving the dimension limit.

**3. Exact first-break asymptotics.** Extend the *untruncated* polynomial integrand \(V^{-1}\prod_i(1-|z_i|/a_i)\) to all balls; its integral is \(P(r)\) for every \(r>0\). Choose \(\eta>0\) small enough that when \(a_*<r<a_*+\eta\), (i) only coordinates with side length \(a_*\) can exceed their side limits, and (ii) two such coordinates cannot simultaneously exceed \(a_*\) inside \(B_d(r)\). The second condition follows from \(r<\sqrt2a_*\). Thus the difference \(F(r)-P(r)\) is the sum of the positive corrections on the disjoint caps \(\{|z_i|>a_*\}\) for the \(m\) shortest coordinates.

For one such coordinate, put \(r=a_*+\varepsilon\) and \(|z_i|=a_*+s\), with \(0<s<\varepsilon\). The transverse \((d-1)\)-ball has radius \(\sqrt{(\varepsilon-s)(2a_*+\varepsilon+s)}\). Uniformly on the cap the remaining product is \(1+O_K(\sqrt\varepsilon)\), because every remaining transverse coordinate is \(O(\sqrt\varepsilon)\). Accounting for the two signs of \(z_i\), the cap correction is
\[
 \frac{2\kappa_{d-1}}{a_*V}\int_0^\varepsilon s\bigl[(\varepsilon-s)(2a_*+\varepsilon+s)\bigr]^{(d-1)/2}\bigl[1+O_K(\sqrt\varepsilon)\bigr]\,ds.
\]
Replacing the second factor in brackets by \(2a_*\) causes only a relative \(O_K(\varepsilon)\) error. The remaining beta integral satisfies
\[
 \int_0^\varepsilon s(\varepsilon-s)^{(d-1)/2}\,ds
 =\frac{4\varepsilon^{(d+3)/2}}{(d+1)(d+3)}.
\]
Summing the \(m\) congruent leading cap contributions proves the displayed onset and remainder. Their positivity proves genuine departure immediately above \(a_*\), hence the asserted sharp radius boundary. All statements are valid for arbitrary \(d\ge3\).

**4. Explicit three-dimensional reconstruction.** For side lengths \((1,2,3)\), the exact local CDF is
\[
 F(r)=\frac{2\pi}{9}r^3-\frac{11\pi}{72}r^4+\frac4{45}r^5-\frac1{216}r^6,\quad 0\le r\le1.
\]
The coefficients of \(r^3,r^4,r^5\) give \(V=6\), \(e_1=11/6\), \(e_2=1\); volume gives \(e_3=1/6\). The reciprocal-root polynomial is \((T-1)(T-1/2)(T-1/3)\). The forced \(r^6\) coefficient is \(-1/216\). The first-break correction has exponent \(3\) and coefficient \(2\pi/(3V)=\pi/9\).

## Verification

The included standalone `check.py` independently checks the exact coefficient/root reconstruction in dimensions two through five, numerical quadrature of the planar difference-vector density, first-break coefficient ratios from cap integrals in dimensions two through four (including multiple shortest sides), and simulated independent point pairs in dimensions three and four. Executing `python check.py` should print `ORTHOTOPE_LOCAL_DISTANCE_OK`. Numerical experiments corroborate but do not replace the all-dimensional arguments above.

## Relationship to prior work

Classical work on random distances in rectangles, including Ghosh (1951) and Marsaglia–Narasimhan–Zaman (1990), supplies planar forward distance distributions. Bäsel's 2012 full-text treatment also derives planar distributions using chord-length methods. Mathai–Moschopoulos–Pederzoli (1999) treat random distances in cubes, a much more symmetric setting. Pure–Durrani–Tong–Pan (2019) provide a planar polygonal forward-distribution framework. The general covariogram identity relates pair-distance probabilities to radial covariogram integrals, including the general 2026 treatment by Wang. None of the inspected relevant passages asserts the present arbitrary-dimensional orthotope finite-jet inverse with sharp generic coefficient count and multiplicity-sensitive first-break asymptotic. The planar special case and the general convolution identity are existing mathematics, not claimed as new. The full original 1990 and 1999 articles were not accessible for page-by-page inspection; priority is therefore provisional.

## Limitations

The result identifies orthotopes *within the orthotope model*; it does not assert that an arbitrary convex body with the same local distance law must be an orthotope. Exact derivatives/coefficients are required, and no finite-sample estimation bound or noise robustness theorem is proved. A constant-width or nonorthogonal parallelotope has a different covariogram and is not covered. The parent probability law is invariant under translation, rigid motion, and side permutation. As with any theorem derived from classical covariogram identities, equivalent formulas under alternative terminology remain a historical-priority risk. No independent validation is asserted.

## References

1. U. Bäsel, *The distribution function of the distance between two random points in a right-angled triangle* (arXiv:1208.6228, first submitted 2012-08-30). https://arxiv.org/abs/1208.6228
2. G. Marsaglia, B. Narasimhan, and A. Zaman, *The distance between random points in rectangles*, Communications in Statistics—Theory and Methods 19 (1990), 4199–4212. https://doi.org/10.1080/03610929008830437
3. A. M. Mathai, P. Moschopoulos, and G. Pederzoli, *Distance between random points in a cube*, Statistica 59 (1999), 61–81. https://doi.org/10.6092/issn.1973-2201/1104
4. R. Pure, S. Durrani, F. Tong, and J. Pan, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons* (arXiv:1903.07757, 2019). https://arxiv.org/abs/1903.07757
5. S. Wang, *A Brunn–Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies* (arXiv:2610.01916, 2026), particularly the introductory small-range expansion and the covariogram identity. https://arxiv.org/abs/2610.01916
