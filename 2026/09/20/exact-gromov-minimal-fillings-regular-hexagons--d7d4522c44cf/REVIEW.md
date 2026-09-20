# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof was checked at four separate levels.

First, the two proposed upper-bound trees were checked edge by edge. For the caterpillar tree the weights
\[
\frac{a+b-c}{2},\quad
\frac{a-b+c}{2},\quad
\frac{c-a}{2},\quad
\frac{3b-2c}{2},\quad
c-b
\]
are all nonnegative under the concavity consequences
\[
a\le b\le c,\qquad c\le a+b,\qquad 3b\ge2c.
\]
Its fifteen leaf-pair path lengths reduce to
\[
a,\ b,\ c,\ 2b-c,\ 2c-b,\ 3c-2b,
\]
and the remaining filling inequalities follow from \(2b\ge a+c\) and \(c\ge b\ge a\). The total weight simplifies to \(a+2b\). The three-cherry tree has six leaf edges of weight \(a/2\) and three central edges of weight \((c-a)/2\); it majorizes all boundary distances and has total weight \(3(a+c)/2\).

Second, the lower bound uses two standard results from Ivanov--Tuzhilin: a minimal filling can be taken with binary-tree type, and every compatible tour of a filling tree gives a half-perimeter lower bound. The only new finite step is the six-leaf tour lemma. The included verifier independently generates all \(105=(2\cdot6-5)!!\) labeled unrooted binary trees, all 60 cyclic orders modulo rotation and reversal, checks tour compatibility by edge splits, and confirms that every tree has a tour in one of the six asserted gap-count classes. It also reduces the list to 17 dihedral orbits and prints an explicit witness for every orbit.

Third, the six resulting half-perimeters were compared symbolically with the two candidate upper bounds. The four required differences are
\[
c-a,\qquad \frac{c-a}{2},\qquad c-b,\qquad b-a,
\]
so every binary tree receives the required lower bound.

Fourth, the Euclidean, spherical, and hyperbolic chord profiles were differentiated directly. Their second derivatives have the claimed nonpositive signs, and their first derivatives are nonnegative on \([0,\pi]\). Therefore the abstract concave-profile theorem applies to the stated constant-curvature regular hexagons.

No step uses numerical evidence in place of the general proof; the finite enumeration certifies only the explicitly finite tree lemma.

## Originality

**PASS, to the best of our knowledge.**

The 2012 Ivanov--Tuzhilin paper is the closest old source. It proves the binary-tree and tour machinery used here, gives an exact formula for convex five-point sets, and then states only an upper estimate for regular \(n\)-gons (Assertion 11.5, attributed to E. E. Zaval'nyuk). For \(n=6\), that estimate equals \(1+2\sqrt3\) under unit circumradius normalization. The new contribution is the matching lower bound and the two-branch closed form for the wider concave cyclic six-point family, which in turn gives spherical and hyperbolic regular-hexagon formulas.

Edelsbrunner--Ivanov--Karasev explicitly asked for minimal fillings of regular polygons in Euclidean, spherical, and Lobachevskii geometry. The present record is deliberately narrower: it determines the exact minimum weight for \(n=6\) and constructs minimizers, but does not claim to classify every minimizer or solve all \(n\).

Eremin's 2013 theorem supplies a general minimax characterization of minimal-filling weight for arbitrary finite metrics. That general result is not being claimed as new. Searches were made under *minimal filling*, *one-dimensional Gromov filling*, *regular polygon*, *regular hexagon*, *six-point cyclic metric*, *tour half-perimeter*, and equivalent formula searches involving \(a+2b\) and \(3(a+c)/2\). No located source states the closed form proved here.

The most important residual risk is A. O. Ivanov and A. A. Tuzhilin, *Minimal Fillings of Finite Metric Spaces and Convex Polyhedra*, arXiv:2607.27211 (2026). Its abstract was inspected and describes a general convex-polyhedral formulation for parametric generalized fillings. The full text was not inspected in the sources available for this review. Because such a framework could contain or mechanically imply a worked six-point evaluation, it is a material priority risk even though the abstract and targeted searches did not expose the regular-hexagon formula.

A separate body of literature studies Steiner minimal networks for regular hexagons in a fixed ambient plane. That is a different optimization problem: one-dimensional Gromov minimal fillings optimize over weighted filling trees that majorize the boundary metric, not only embedded Steiner networks in the original ambient surface.

## Value

**PASS.**

The result turns an old regular-polygon upper estimate into an exact Euclidean value at the first even case beyond the square, and at the same time produces a curvature-uniform formula for a larger symmetric six-point metric family. The proof identifies a simple two-topology competition:
\[
a+2b\quad\text{versus}\quad \frac32(a+c),
\]
with the lower bound reduced to a complete finite tour statement on six-leaf binary trees. The spherical and hyperbolic formulas address the same three constant-curvature settings singled out in the older open-problem list.

## Limitations

- The abstract six-point theorem assumes a nondecreasing concave chord profile.
- The spherical corollary is restricted to \(0<R<\pi/2\).
- The minimum weight is determined, but all minimizing tree types are not classified.
- The six-leaf combinatorial lemma is certified by exhaustive standard-library code rather than a handwritten classification proof.
- Originality is to the best of our knowledge; arXiv:2607.27211 remains the principal uninspected full-text risk.

## Sources checked

- H. Edelsbrunner, A. Ivanov, R. Karasev, *Current Open Problems in Discrete and Computational Geometry* (2012), especially the regular-polygon minimal-filling problem.  
  https://doi.org/10.18255/1818-1015-2012-5-5-17
- A. O. Ivanov, A. A. Tuzhilin, *One-dimensional Gromov minimal filling problem* (2012), especially the binary-tree reduction, tour lower bounds, convex-polygon section, and Assertion 11.5.  
  https://doi.org/10.1070/SM2012v203n05ABEH004239  
  https://arxiv.org/abs/1101.0106
- A. Yu. Eremin, *A formula for the weight of a minimal filling of a finite metric space* (2013).  
  https://doi.org/10.1070/SM2013v204n09ABEH004340
- A. O. Ivanov, A. A. Tuzhilin, *Minimal fillings of finite metric spaces: The state of the art* (Contemporary Mathematics 625).
- A. O. Ivanov, A. A. Tuzhilin, *Minimal Fillings of Finite Metric Spaces and Convex Polyhedra* (2026); abstract inspected, full text not inspected.  
  https://arxiv.org/abs/2607.27211
