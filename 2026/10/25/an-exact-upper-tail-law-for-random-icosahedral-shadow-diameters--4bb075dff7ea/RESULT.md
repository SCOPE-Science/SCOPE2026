# An exact upper-tail law for random icosahedral shadow diameters

## Finding

Let \(\varphi=(1+\sqrt5)/2\), \(R=\sqrt{1+\varphi^2}\), and let \(I\subset\mathbb R^3\) be the regular icosahedron with vertices
\[
(0,\pm1,\pm\varphi),\qquad(\pm1,\pm\varphi,0),\qquad(\pm\varphi,0,\pm1).
\]
For a uniform unit normal \(U\in S^2\), write \(D(U)\) for the Euclidean diameter of the orthogonal projection of \(I\) onto \(U^\perp\). Put
\[
t_*=\sqrt{\frac{1-2/\sqrt5}{3}},\qquad
J_k(t)=t\arcsin\frac{kt}{\sqrt{1-t^2}}+
\arctan\frac{\sqrt{1-(1+k^2)t^2}}{k}-\arctan\frac1k.
\]
Then for every \(0\le t\le t_*\), with both square roots taken nonnegative,
\[
\boxed{\Pr\left(D(U)>2R\sqrt{1-t^2}\right)=6t-\frac{30}{\pi}\left(J_\varphi(t)+J_{1/\varphi}(t)\right).}
\]
At the left endpoint the probability is zero; the strict inequality at intermediate thresholds is immaterial because the distribution has no atoms there. The cutoff \(t_*\) is sharp as the first occurrence of an orientation belonging to three distinct vertex-equator bands. The exact branch extends to a probability of approximately \(0.7441273066\) at its cutoff, so it covers a substantial part of the distribution, not only an infinitesimal asymptotic neighborhood.

In particular, as \(t\downarrow0\),
\[
\Pr\left(D(U)>2R\sqrt{1-t^2}\right)
=6t-\frac{15\sqrt5}{\pi}t^2-\frac{25\sqrt5}{4\pi}t^4+O(t^6).
\]
Writing \(z=\varepsilon/R\), the corresponding near-maximal-diameter probability is
\[
\Pr(D(U)>2R-\varepsilon)
=6\sqrt z-\frac{15\sqrt5}{\pi}z-\frac34 z^{3/2}
-\frac{5\sqrt5}{2\pi}z^2+O(z^{5/2}).
\]

## Assumptions and scope

The icosahedron is fixed, with its edge length \(2\), circumradius \(R\), and exactly twelve vertices. The plane passes through the origin; its unoriented normal is Haar-uniform, equivalently \(U\) is uniform on the unit sphere. The result applies only to the explicit branch \(0\le t\le t_*\). No statement about the full lower-diameter branch is asserted. All probabilities are with respect to the viewing orientation, not random points inside the solid.

## Proof

**1. Projected diameter and six equators.** Choose the six representatives
\[
a_i\in\frac1R\{(0,1,\varphi),(0,-1,\varphi),(1,\varphi,0),(-1,\varphi,0),(\varphi,0,1),(\varphi,0,-1)\}.
\]
The vertex set equals \(\{\pm Ra_i:1\le i\le6\}\). For every origin-symmetric compact convex set \(C\), its diameter is twice its maximum norm: the triangle inequality gives the upper bound and an antipodal pair attains it. Orthogonal projection preserves central symmetry. Because the squared projected norm of vertex \(Ra_i\) is \(R^2(1-(U\cdot a_i)^2)\), it follows exactly that
\[
D(U)=2R\sqrt{1-m(U)^2},\qquad m(U)=\min_{1\le i\le6}|U\cdot a_i|.
\]
Thus the asserted event is the union of six spherical bands \(B_i(t)=\{|U\cdot a_i|<t\}\). Each has probability \(t\), since \(U\cdot a_i\) is uniform on \([-1,1]\).

**2. The exact first triple-overlap threshold.** Direct dot products give \(|a_i\cdot a_j|=c=1/\sqrt5\) for all distinct \(i,j\). None of the twenty triples is linearly dependent. Ten triple Gram matrices have positive off-diagonal sign product and ten have negative product. Changing axis signs puts them, respectively, into the forms \((1-c)\mathrm{Id}+c\mathbf1\mathbf1^\mathsf T\) and \((1+c)\mathrm{Id}-c\mathbf1\mathbf1^\mathsf T\).

For a triple of axes let \(A\) be the invertible matrix having those axes as rows. Its first simultaneous-band threshold is
\[
\min_{\|u\|_2=1}\|Au\|_\infty
=\left(\max_{\sigma\in\{-1,1\}^3}\|A^{-1}\sigma\|_2\right)^{-1}.
\]
Indeed, the maximum of the convex norm of \(A^{-1}x\) over the cube is attained at a vertex; normalization proves equality. For the positive-product Gram form this threshold equals
\[
\sqrt{\frac{(1-c)(1+2c)}{3+5c}}=\frac1{\sqrt5};
\]
for the negative-product form the threshold is \(\sqrt{(1-2c)/3}=t_*\). Since \(t_*<1/\sqrt5\), no point lies in any three bands for \(t<t_*\). At \(t=t_*\) a triple first touches; that touching has zero spherical area, and for \(t>t_*\) triple intersections of positive area occur. Therefore inclusion-exclusion stops exactly at pair intersections throughout the stated interval.

**3. Common pair-band intersection.** The probability \(H(t)=\Pr(B_i(t)\cap B_j(t))\) is identical for each of the fifteen pairs because every absolute axis inner product is \(c\). Put \(s=\sqrt{1-c^2}=2/\sqrt5\). Conditional on \(U\cdot a_i=t\), the other scalar product has the form \(ct+s\sqrt{1-t^2}\cos\theta\), with \(\theta\) uniform on the circle. For \(0<t\le t_*\), the relevant endpoints lie in \((-1,1)\). Differentiating the two moving band boundaries gives
\[
H'(t)=\frac2\pi\left[\arcsin\frac{(1+c)t}{s\sqrt{1-t^2}}
+\arcsin\frac{(1-c)t}{s\sqrt{1-t^2}}\right].
\]
Here \((1+c)/s=\varphi\), \((1-c)/s=1/\varphi\), and \(H(0)=0\). Direct differentiation of the displayed definition of \(J_k\) gives
\[
J_k'(t)=\arcsin\frac{kt}{\sqrt{1-t^2}},\quad J_k(0)=0,
\]
so \(H(t)=2\big(J_\varphi(t)+J_{1/\varphi}(t)\big)/\pi\).

**4. Inclusion-exclusion and expansions.** With no positive-area triple intersection, the union probability is \(6t-15H(t)\), proving the formula. Expanding the inverse sine inside the integral yields
\[
J_\varphi(t)+J_{1/\varphi}(t)
=\frac{\sqrt5}{2}t^2+\frac{5\sqrt5}{24}t^4+O(t^6),
\]
using \(\varphi+1/\varphi=\sqrt5\) and \(\varphi^3+\varphi^{-3}=2\sqrt5\). Substitution gives the stated expansion in \(t\). Finally \(t=\sqrt{z-z^2/4}\) when the diameter threshold is \(2R-\varepsilon\), which gives the displayed expansion in \(z\). Every step takes place in an explicit open interval where the inverse trigonometric expressions are real and analytic; the expansions have rigorous Taylor remainders.

## Verification

Run `python verify.py` with Python, NumPy, and SciPy. The script independently checks all fifteen equiangular dot products, the twenty three-axis Gram classes and their exact target thresholds numerically, the primitive against independent numerical quadrature, the expansion, and the diameter identity by brute-force all-pairs distances among the twelve projected vertices. A seeded Haar-normal experiment with 1,200,000 orientations compares three interior thresholds with the exact law; its sampling errors agree with binomial standard errors. These finite computations corroborate but are not substitutes for the analytic steps above.

## Relationship to prior work

Kabluchko–Litvak–Zaporozhets (2015, arXiv:1511.08479) derive moments and high-dimensional limit theorems for one-dimensional random widths of regular polytopes. Finch (2011, arXiv:1110.0671) studies corresponding one-dimensional width distributions for the tetrahedron and cube. Neither studied quantity is the diameter of the *two-dimensional* orthogonal shadow of the regular icosahedron, and their formulas do not imply the six-band finite-interval law here. The classical six-great-circle icosahedral arrangement is geometric background, not claimed as new: the new statistic is the Haar area of its thickened equator union through the sharp first triple-overlap transition. Historical priority has not been independently certified.

## Limitations

The formula is not a global distribution: it applies only from the maximal diameter down to the explicit first triple-overlap cutoff. The threshold formula relies on all six vertex axes having equal length and pairwise absolute scalar product \(1/\sqrt5\); it does not extend unchanged to general deformed icosahedra or arbitrary projection measures. Numerical tests do not certify infinitely many orientations, and no independent external mathematical audit has been conducted.

## References

1. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479, first posted 26 November 2015, https://arxiv.org/html/1511.08479v3.
2. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first posted 4 October 2011, https://arxiv.org/html/1110.0671v2.
3. E. Popko, *Divided Spheres: Geodesics and the Orderly Subdivision of the Sphere*, CRC Press, 2012, discussion of the six icosahedral great circles; this book was identified bibliographically but its relevant full chapter was not inspected.
