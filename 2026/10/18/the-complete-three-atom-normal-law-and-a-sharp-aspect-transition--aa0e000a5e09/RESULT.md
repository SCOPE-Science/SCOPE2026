# The complete three-atom normal law and a sharp aspect transition for parallelograms

## Finding

Let \(P\) be any nondegenerate Euclidean parallelogram. Choose adjacent edge lengths \(a\ge b>0\), let \(\alpha\in(0,\pi/2]\) be its smaller interior angle, and put \(q=a/b\ge1\) and \(c=\cos\alpha\in[0,1)\). Draw \(Y\) uniformly from the area of \(P\), and let \(N_P(Y)\) count distinct points \(z\in\partial P\) at which the line \(zY\) is perpendicular to some supporting line of \(P\) at \(z\). The point \(Y\) is assumed generic: the finitely many transition line segments are excluded, a probability-one condition.

Almost surely \(N_P(Y)\in\{4,6,8\}\). Its **complete distribution** is as follows. When \(cq\le1\), put \(k=c/q\), \(\ell=cq\). Then
\[
\Pr(N_P=8)=\frac{(1-k)(1-\ell)}{1-c^2},\qquad
\Pr(N_P=4)=\frac{c^2(2-k-\ell)}{1-c^2},\qquad
\Pr(N_P=6)=1-\Pr(N_P=4)-\Pr(N_P=8).
\]
When \(cq\ge1\), the law is
\[
\Pr(N_P=8)=0,\qquad
\Pr(N_P=6)=\frac{1-c^2}{cq},\qquad
\Pr(N_P=4)=1-\frac{1-c^2}{cq}.
\]
At the common boundary \(cq=1\), both formulas agree. The second display applies only when \(c>0\). At \(c=0\) (all rectangles) one has \(N_P=8\) almost surely.

For every fixed \(c\in(0,1)\), the critical aspect ratio \(q=1/c\) is characterized by the disappearance of the eight-normal event. At this critical ratio, \(\Pr(N_P=6)=1-c^2\) is the unique maximum over all \(q\ge1\), whereas \(\Pr(N_P=4)=c^2\) is the unique minimum. The probability of eight normals decreases strictly from \((1-c)/(1+c)\) at the rhombus \(q=1\) to zero at \(q=1/c\), and then remains zero. The mean decreases strictly with \(q\) for fixed \(c>0\), with the sharp rhombus maximum \(8-4c\) and limiting value \(4\) as \(q\to\infty\):
\[
\mathbb E N_P=
\begin{cases}
8-2c(q+q^{-1}),&1\le q\le1/c,\\
4+\dfrac{2(1-c^2)}{cq},&q\ge1/c.
\end{cases}
\]
For rectangles the mean is \(8\) regardless of side ratio.

For example, a rhombus with \(c=3/5\) has probabilities \(\Pr(N_P=4)=9/20\), \(\Pr(N_P=6)=3/10\), and \(\Pr(N_P=8)=1/4\). At the same angle and critical ratio \(q=5/3\) the probabilities are \(9/25,16/25,0\), respectively.

## Assumptions and scope

A normal is specified by its **base point** on the boundary, even at a nonsmooth corner. At a vertex, the line from the interior point is required to be perpendicular to *some* supporting line at that vertex. Opposite sides are not identified. Genericity excludes points where a side-foot lies exactly at a vertex or an inward-normal cone inequality becomes an equality. The conditions \(c\in[0,1)\) and \(q\ge1\) describe every nondegenerate parallelogram up to similarity and relabeling. The random point is uniform with respect to Euclidean area, not perimeter, not hyperplane measure, and not a fixed center.

## Proof

Choose the acute vertex as origin and express the parallelogram as \(P=\{xu+yv:0\le x,y\le1\}\), where \(\|u\|=a\), \(\|v\|=b\), and \(u\cdot v=ab c\). The area-uniform point is \(Y=xu+yv\) with independent uniform coordinates \(x,y\in(0,1)\). Set \(k=bc/a=c/q\), \(\ell=ac/b=cq\), so that \(k\ell=c^2<1\).

Orthogonal projection onto the four sides lands in their relative interiors precisely when the following four inequalities hold, respectively:
\[
A_1:\ x+ky<1,\quad A_2:\ x+ky>k,\quad
B_1:\ y+\ell x<1,\quad B_2:\ y+\ell x>\ell.
\]
These conditions are obtained directly by taking scalar products with \(u\) or \(v\). At each of the two acute vertices the inward supporting-normal cone always contains \(Y\) in its relative interior. At the other two vertices, the cone tests are \(A_1\wedge B_2\) and \(A_2\wedge B_1\). Therefore the total normal count at a generic point is
\[
N_P(Y)=2+\mathbf1_{A_1}+\mathbf1_{A_2}+\mathbf1_{B_1}+\mathbf1_{B_2}
+\mathbf1_{A_1\wedge B_2}+\mathbf1_{A_2\wedge B_1}.
\]

For clarity, the equality of the number of side normals and vertex normals also follows independently from the circular critical-point argument. Restricted to each open side, squared Euclidean distance to \(Y\) is strictly convex, so an interior stationary point is a local minimum. At a vertex, a local minimum cannot occur: writing the vector toward \(Y\) as a positive combination of the two adjacent outgoing side vectors, it cannot have nonpositive scalar product with both, because its scalar product with itself is positive. Generic extrema on the polygonal circle therefore alternate between side minima and vertex maxima. There are exactly two automatic acute-vertex maxima, at most four side minima, and no other types. Hence the number of normals is twice the number of side-foot indicators and belongs to \(\{4,6,8\}\).

Eight normals occur exactly when all four side-foot indicators hold. Writing \(s=x+ky\), \(t=y+\ell x\), this is \(k<s<1\) and \(\ell<t<1\). If \(\ell\ge1\) the region is empty. If \(k,\ell\le1\), the linear change of variables has determinant \(1-k\ell>0\). The preimage of the rectangle \((k,1)\times(\ell,1)\) lies inside the unit square: the four preimage corners are \((0,1)\), \((1,0)\), \((k(1-\ell)/(1-k\ell),\ell(1-k)/(1-k\ell))\), and \(((1-k)/(1-k\ell),(1-\ell)/(1-k\ell))\). Therefore its area is \((1-k)(1-\ell)/(1-k\ell)\), yielding the eight-normal probability.

For any \(z\ge0\), the probability \(F(z)=\Pr(X>zY)\) for independent uniform \(X,Y\in(0,1)\) is
\[
F(z)=\begin{cases}1-z/2,&0\le z\le1,\\1/(2z),&z\ge1.\end{cases}
\]
Each of the two \(u\)-parallel sides has foot probability \(F(k)\), and each of the two \(v\)-parallel sides has foot probability \(F(\ell)\). By the alternating-extrema identity,
\[
\mathbb EN_P=4(F(k)+F(\ell)).
\]
Now write \(p_j=\Pr(N_P=j)\) for \(j\in\{4,6,8\}\). Since \(p_4+p_6+p_8=1\) and \(\mathbb EN_P=6+2(p_8-p_4)\), the already computed eight-normal probability and mean determine \(p_4\) and \(p_6\). Substitution yields exactly the two displayed laws, including agreement at \(\ell=1\).

For fixed \(c>0\), differentiation in the first regime gives \(p_8'=-c(1-q^{-2})/(1-c^2)\), \(p_4'=-c^3(1-q^{-2})/(1-c^2)\), and \(p_6'=c(1+c^2)(1-q^{-2})/(1-c^2)\). These are strictly signed for \(1<q<1/c\). In the second regime \(p_6=(1-c^2)/(cq)\) decreases strictly, and \(p_4=1-p_6\) increases strictly. This proves the three extremal claims. The mean decreases strictly for \(q>1\) by the displayed piecewise formula. The rectangular case follows by putting \(c=0\) in the first regime.

## Verification

A standalone Python 3 script, `check_normals.py`, constructs each of the sixteen sign chambers by exact rational half-plane clipping. It independently computes the area of every chamber using exact rational shoelace arithmetic, assigns a normal count from side and vertex scalar-product tests, and compares all three resulting rational probabilities with the formulas above. It passed \(87\) parameter cases, including critical-boundary cases, together with four exact phase-extremum tests. A further independent Euclidean-coordinate computation enumerated side feet and vertex support cones at \(1{,}250\) deterministic random interior points over five shapes; all comparisons passed. Run `python3 check_normals.py`. These finite checks are reproducibility safeguards; the proof above establishes the formula for all admissible real parameters.

## Relationship to prior work

Hann (1993) and Hug (1995) develop general bounds and Euler-type identities for normals of convex bodies. Domokos and Lángi (first public preprint 2014) state the classical bound \(n(K)\le8\) for centrally symmetric planar convex bodies and discuss the general equality mechanism. Nasonov, Panina and Siersma (2024 preprint) discuss active regions, Morse-theoretic normal counts, and averages, but their planar explicit proposition concerns triangles. The present claim is the complete parallelogram-specific probability law, including its exact aspect threshold and extremizers; it does **not** claim the already-known general \(8\) bound, Euler identities, or polygonal Morse principles as new. Direct historical coverage cannot be completely excluded because the full texts of the older Hann and Hug papers were not available in this examination.

## Limitations

No assertion is made for general convex quadrilaterals, non-Euclidean norms, nonuniform area distributions, or nongeneric transition points. Results are exact for every nondegenerate parallelogram but involve no independent audit and do not establish definitive historical priority. The threshold is a shape-specific probability transition rather than a statement about smooth perturbations or higher-dimensional normal counts.

## References

- G. Domokos and Z. Lángi, *On the average number of normals through points of a convex body*, arXiv:1406.0813, first posted 2014-06-03, https://arxiv.org/abs/1406.0813 .
- I. Nasonov, G. Panina, and D. Siersma, *Concurrent normals problem for convex polytopes and Euclidean distance degree*, arXiv:2406.01773, first posted 2024-06-03, https://arxiv.org/abs/2406.01773 .
- K. Hann, *The average number of normals through a point in a convex body and a related Euler-type identity*, Geom. Dedicata 48 (1993), 27–55, doi:10.1007/BF01265675 (full text not inspected).
- D. Hug, *On the mean number of normals through a point in the interior of a convex body*, Geom. Dedicata 55 (1995), 319–340, doi:10.1007/BF01266322 (full text not inspected).
