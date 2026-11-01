# Exact upper shadow-volume distribution and first transition of the regular 24-cell

## Finding

Let \(C\) be the regular four-dimensional 24-cell, with vertices
\[
\{\pm e_i:1\le i\le4\}\cup\{(\varepsilon_1,\ldots,\varepsilon_4)/2:\varepsilon_i\in\{-1,1\}\}.
\]
For Haar-uniform \(U\in S^3\), define the *brightness* \(B=\operatorname{vol}_3(C\mid U^\perp)\). Put
\[
b_{\max}=\frac{2\sqrt{14}}3,\qquad b_1=\sqrt6,\qquad b_2=\frac{2\sqrt{13}}3,\qquad
h=\sqrt{\frac{27}{28}},\quad q=\frac1{\sqrt{28}}.
\]
For \(0\le s\le1\) set
\[
P(s)=\frac{\arccos s-s\sqrt{1-s^2}}\pi,\qquad
Y(s)=h\sqrt{1-s^2}-qs.
\]
Define \(L(s)=0\) when \(s\ge h\), and otherwise, for \(\sqrt{13/14}\le s<h\),
\[
L(s)=\frac1\pi\left(\arcsin Y(s)-\frac{sY(s)}h\right).
\]
Then the **exact upper-tail law** is
\[
\boxed{\ \Pr(B\ge b)=192P(b/b_{\max})-384L(b/b_{\max})\quad(b_2\le b\le b_{\max}).\ }
\]
In particular, it is the single-cap expression \(192P(b/b_{\max})\) throughout \(b_1\le b\le b_{\max}\), and the first pairwise correction appears below \(b_1\). The first transition is sharp:
\[
\boxed{\ \Pr(B\ge b)-192P(b/b_{\max})
=-\frac{192\sqrt3}{\pi}(\sqrt6-b)^2+O((\sqrt6-b)^3)\quad(b\uparrow\sqrt6).\ }
\]
Thus the survival function is \(C^1\) but not \(C^2\) at \(b=b_1\). The exact interval contains about \(60.098\%\) of directions (at its lower endpoint).

## Assumptions and scope

All projection volumes are ordinary three-dimensional Euclidean volumes, and \(U\) is uniform on the oriented sphere \(S^3\); \(B(U)=B(-U)\). The normalization is that the 24-cell has volume two and each of its 24 octahedral facets has three-volume \(\sqrt2/3\). The formula is asserted only on the closed upper interval \([b_2,b_{\max}]\); the remaining lower tail is not classified. The endpoints are included because tangencies contribute zero spherical measure.

## Proof

**1. Brightness as an orbit support function.** The facet normals are \((\pm e_i\pm e_j)/\sqrt2\) for \(i<j\). Cauchy's formula and the common facet volume yield
\[
B(u)=\frac12\sum_F\operatorname{vol}_3(F)|u\cdot n_F|
=\frac13\sum_{i<j}(|u_i+u_j|+|u_i-u_j|)
=\frac23\sum_{i<j}\max(|u_i|,|u_j|).
\]
If \(a\ge b\ge c\ge d\ge0\) are the sorted absolute coordinates, this is \(2(3a+2b+c)/3\). Let \(\mathcal W\) be all distinct signed coordinate permutations of \((3,2,1,0)/\sqrt{14}\); there are \(4!2^3=192\) of them. Rearrangement of nonnegative coordinates and choice of signs prove the exact identity
\[
B(u)=\frac{2\sqrt{14}}3\max_{v\in\mathcal W}u\cdot v.
\]
Consequently, \(\{B(U)\ge b\}\) is the union of 192 equal spherical caps \(\{u\cdot v\ge s\}\), where \(s=b/b_{\max}\).

**2. The orbit's first two angular separations.** Scale the centers by \(\sqrt{14}\), obtaining signed permutations of \((3,2,1,0)\). They have squared norm 14. For distinct centers \(v,w\), the integer squared distance is at least 2, so \(v\cdot w\le13/14\). Equality requires an adjacent transposition of magnitudes \(3,2\), \(2,1\), or \(1,0\) (with either available sign on the formerly zero entry). Each center has exactly four such neighbors, giving \(192\cdot4/2=384\) unordered nearest pairs. All remaining pairs satisfy \(v\cdot w\le12/14\). A nearest edge reverses the permutation parity of the four absolute magnitudes, so the nearest-neighbor graph is bipartite and in particular contains no triangles. These conclusions can also be verified by exact finite integer enumeration in the accompanying script.

Two spherical caps of threshold \(s\ge0\) intersect in positive measure only if \(s<\sqrt{(1+v\cdot w)/2}\). Accordingly, at \(s\ge h=\sqrt{27/28}\) no pair intersects except on a null set. For \(\sqrt{13/14}\le s<h\), precisely the 384 nearest pairs may overlap, and triple overlaps have zero measure: otherwise the three centers would form a nearest-neighbor triangle. Therefore inclusion–exclusion stops after pair terms, with the claimed coefficients 192 and 384.

**3. Spherical cap and lens integrals.** For \(U\) uniform on \(S^3\), one scalar coordinate has density \(2\sqrt{1-t^2}/\pi\). Hence each cap has measure \(P(s)\). For a nearest pair, choose orthonormal bisector coordinates \(x,y\) such that its centers have coordinate vectors \((h,q)\) and \((h,-q)\). The projection of \(U\) to the \((x,y)\)-disk is uniform there with density \(1/\pi\). Both cap inequalities become \(hx\ge s+q|y|\). Its integration range is \(0\le |y|\le Y(s)\), where \(\sqrt{1-Y(s)^2}=(s+qY(s))/h\). Thus the pair intersection is
\[
\frac2\pi\int_0^{Y(s)}\left(\sqrt{1-y^2}-\frac{s+qy}h\right)dy
=\frac1\pi\left(\arcsin Y(s)-\frac{sY(s)}h\right)=L(s).
\]
This establishes the exact survival law, including both boundary values.

**4. Quadratic onset.** As \(s\uparrow h\), a Taylor expansion of the preceding integral at the first cap tangency gives
\[
L(s)=\frac{(h-s)^2}{\pi hq}+O((h-s)^3).
\]
Indeed \(Y(s)= (h-s)/q+O((h-s)^2)\), and the thickness \(\sqrt{1-y^2}-(s+qy)/h\) is affine to leading order on that shrinking interval. Substitution \(s=b/b_{\max}\) gives
\[
\frac{384}{\pi hq b_{\max}^{2}}=\frac{192\sqrt3}\pi.
\]
The cap function \(P\) is smooth near \(s=h\), so the nonzero quadratic jump establishes the stated \(C^1\)-but-not-\(C^2\) regularity.

## Verification

The standalone standard-library script `verify.py` enumerates all 192 signed-permutation directions using exact integers, checks that there are 384 nearest pairs, degree four and no nearest-neighbor triangles, and verifies all other pair separations. It independently compares the cap-pair lens with numerical disk integrals at six thresholds, evaluates the quadratic coefficient, and tests the predicted upper-tail probability against 240,000 seeded Gaussian-sphere directions at five thresholds. Run `python verify.py`. Its final line reads `VERIFY_OK`. Numerical samples are diagnostic; the exact proof is the cap geometry and integral calculation above.

## Relationship to prior work

Novaga–Song's October 2026 isoperimetric theorem fixes the 24-cell vertex realization and octahedral facet areas; it does not give a random brightness law. A prior exact 24-cell brightness-profile result determines \(B(u)=2(3a+2b+c)/3\), its minimum, maximum, and precisely 192 maximizing directions. This **known directional profile is used** rather than claimed as new. Our claim is the evaluated pushforward distribution, its exact first overlap regime, and its sharp quadratic singularity from 384 adjacent maxima. Standard Cauchy projection and spherical cap identities are likewise not novel. Nearby published random-width formulas for cubes and octahedra concern other polytopes and a different projection invariant.

## Limitations

The result does not classify the distribution below \(2\sqrt{13}/3\), where non-nearest pairs and higher overlaps can contribute. The complete brightness function and extrema were known, so no independent discovery is claimed for that ingredient. The exact probability formula is derived by nontrivial cap-orbit geometry but may have an older equivalent presentation using Weyl-orbit probability or spherical tessellations; searches cannot establish absolute historical priority. There has been no independent audit.

## References

1. M. Novaga and L. Song, *The isoperimetric problem for four-dimensional parallelohedra*, arXiv:2610.01653v1 (October 1, 2026), especially Lemma 2.3; https://arxiv.org/abs/2610.01653.
2. *The regular 24-cell has exactly 24 least-bright and 192 most-bright projection directions*, public mathematical research record, October 2026; https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-regular-24-cell-has-exactly-24-least-bright-and-192-most-bri--c9973824dcf5.
3. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd expanded ed., Cambridge University Press, 2014; Cauchy's projection formula.
