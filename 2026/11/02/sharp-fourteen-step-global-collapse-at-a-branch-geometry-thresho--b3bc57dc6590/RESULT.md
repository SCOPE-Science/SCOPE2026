# Sharp fourteen-step global collapse at a branch-geometry threshold

## Finding
For the continuous piecewise-affine planar map
\[
 F(x,y)=\left(|x|-y-1,\ x-|y|+\frac14\right),
\]
write \(p=(-1/4,-1/2)\). Then
\[
 \boxed{F^{14}(\mathbb R^2)=\{p\},\qquad F^{13}(\mathbb R^2)\ne\{p\}.}
\]
The point \(p\) is fixed. In particular, the smallest positive integer \(N\) such that \(F^N\) is constant on the entire unbounded plane is \(N=14\). This is an exact finite-time statement, not a limiting-attraction estimate.

## Assumptions and scope
All initial conditions \((x,y)\in\mathbb R^2\) are included, including points on the two coordinate axes. The coefficients are exactly \(a=-1\), \(b=1/4\) in the planar family \(F_{a,b}(x,y)=(|x|-y+a,\ x-|y|+b)\). No floating-point comparisons enter the argument. The parameter \(b=1/4\) is a branch-geometry threshold distinguished in the source's treatment of transitions between quadrant itineraries (proof of Proposition 17 and Proposition 19).

## Proof
**Step 1 (the homogeneous part vanishes after five iterates).** Put \(H(x,y)=(|x|-y,x-|y|)\), and let the quadrants be interpreted with weak inequalities on their shared axes. For \(x,y\ge0\), the first image is \((t,t)\), where \(t=x-y\). If \(t\ge0\), the next image is zero. If \(t<0\), the successive images after \(H(x,y)\) are \((-2t,2t)\), \((-4t,0)\), \((-4t,-4t)\) and zero. For \(x,y\le0\), write \(s=-x-y\ge0\); the successive images are \((s,-s)\), \((2s,0)\), \((2s,2s)\) and zero. For \(x\ge0\ge y\), the first image is \((x-y,x+y)\). If \(x+y\ge0\), its next image is \((-2y,-2y)\), then zero. If \(x+y<0\), its next images are \((-2y,2x)\), \((-2x-2y,-2x-2y)\), and zero. For \(x\le0\le y\), the first image is \((-x-y,x-y)\). When \(-x-y\le0\), the next images are \((2y,-2y)\), \((4y,0)\), \((4y,4y)\), and zero. Otherwise they are \((-2x,-2y)\), \((-2x+2y,-2x-2y)\), \((4y,4y)\), and zero. Thus \(H^5\equiv0\) on \(\mathbb R^2\), including all boundary cases.

Since \(F=H+c\) with \(c=(-1,1/4)\), and \(H\) is \(2\)-Lipschitz in the supremum norm, comparison with \(H^5\) gives
\[
 \|F^5(z)\|_\infty\le\sum_{j=0}^4 2^j\|c\|_\infty=31
 \quad(z\in\mathbb R^2).
\]
The boundedness of the entire fifth image is needed below when image polygons arise from unbounded initial cells.

**Step 2 (finite exact description of the fifth image).** A sign itinerary of length \(5\) is a word in the four possible sign pairs \((\pm,\pm)\) at the successive inputs. Its closed itinerary cell is defined by at most \(10\) affine weak inequalities in the initial \((x,y)\). On each cell, \(F^5(z)=Az+v\) for an integer matrix \(A\) and a rational vector \(v\). The cells cover the entire plane, with overlaps only at sign boundaries where the affine formulas agree.

Each nonempty itinerary cell lies in one closed initial quadrant, so its recession cone contains no line. It is therefore a pointed polyhedron with vertices; every vertex is obtained by intersecting two independent active boundary lines and checking all inequalities. Because the affine image of each cell is contained in the bounded set \(F^5(\mathbb R^2)\), its linear part annihilates every recession direction. Minkowski--Weyl decomposition then shows that the *entire image of this unbounded cell* is the convex hull of the affine images of its finitely many vertices. No finite truncation of the initial plane is used.

The standalone exact-rational checker enumerates all four sign choices at each depth; the numbers of nonempty closed itinerary cells after depths \(1,2,3,4,5\) are, respectively, \(4,13,25,45,75\). At depth \(5\), their affine images reduce to exactly \(30\) distinct convex polygons or degeneracies, with \(13\) distinct total vertices. Consequently their union is exactly \(F^5(\mathbb R^2)\).

**Step 3 (exact image propagation).** For any convex polygon, line segment or singleton, intersect it with each of the four closed quadrants and apply the corresponding affine branch of \(F\). Taking the convex hull of the transformed vertices is an *exact* image on that branch. Therefore iterating this construction on the union of the \(30\) fifth-image polytopes computes the full plane's subsequent images without discretizing the initial conditions. With duplicate polytopes removed, the numbers of distinct image polytopes at times \(5\) through \(14\) are
\[
 30,\ 25,\ 20,\ 15,\ 12,\ 10,\ 8,\ 6,\ 3,\ 1.
\]
The corresponding counts of all distinct vertices are
\[
 13,\ 11,\ 9,\ 8,\ 7,\ 6,\ 5,\ 4,\ 2,\ 1.
\]
At time \(14\), the sole polytope is the singleton \(\{(-1/4,-1/2)\}\). Hence \(F^{14}(\mathbb R^2)=\{p\}\).

**Step 4 (sharpness).** Exact evaluation of the orbit beginning at \((-3,1/4)\) yields
\[
 F^{13}(-3,1/4)=(-3/4,0),\qquad F^{14}(-3,1/4)=p.
\]
Since \((-3/4,0)\ne p\), the globally constant iterate cannot be \(13\) or any smaller integer. Indeed, if an earlier iterate were constant, all later iterates would be constant, whereas \(F^{13}\) is not. This proves optimality.

## Verification
Run \(\texttt{python3 CHECK.py}\) using Python's standard library. The checker uses \(\texttt{fractions.Fraction}\) for every coordinate, intersection, sign test and convex hull; it requires no external package. It rederives all depth-five feasible cells from affine sign inequalities and then computes the exact forward images through time \(14\). It checks all cell/polytope/vertex counts and the explicit sharpness witness. The analytic homogeneous-nilpotence and recession-cone arguments above justify why this finite enumeration covers the entire unbounded plane. No sample of initial conditions substitutes for exhaustive coverage.

## Relationship to prior work
Cima, Gasull, Mañosa and Mañosas introduced and systematically studied this family. Their Corollary 20 proves \(F_{-1,b}^{22}(\mathbb R^2)=\{(-b,2b-1)\}\) for every \(3/16\le b\le4/15\). In proving Proposition 19 they distinguish \(b\le1/4\) from \(b>1/4\), making \(b=1/4\) a meaningful branch-geometry boundary. The statement at exponent \(22\) does not imply that the globally constant iterate already occurs at \(14\), nor that no iterate before \(14\) is constant. The present exact first-collapse calculation is a sharply different quantitative invariant. The authors' subsequent work concentrates on entropy and invariant-graph dynamics in other parameter ranges.

## Limitations
The exact exponent \(14\) is established only at \(a=-1\), \(b=1/4\), not for all parameters in the finite-collapse interval. No assertion is made about the complete parameter-dependent function of first-collapse times, perturbed coefficients, stochastic dynamics or entropy. Although the arithmetic proof is self-contained, this finding has not been independently audited and a mathematically exhaustive priority assessment across every older source is not claimed.

## References
1. A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052v1 (first posted 2024-10-01); published in *Qualitative Theory of Dynamical Systems* 24, article 70 (2025), doi:10.1007/s12346-025-01221-1. In particular, Propositions 17--19 and Corollary 20.
2. A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Further results for a family of continuous piecewise linear planar maps*, arXiv:2503.02411v1 (2025).
