# The regular octahedron's full-normal locus has one-quarter volume

## Finding

Let
\[
O=\{x\in\mathbb R^3:\|x\|_1\le 1\}
\]
be the standard regular octahedron, and let
\[
\Sigma_3=\{x\in\mathbb R^3:\|x\|_1+\|x\|_\infty\le 1\}.
\]
A point \(y\in\operatorname{int}O\) has a distinct normal based in the relative interior of every face of \(O\) if and only if \(y\in\operatorname{int}\Sigma_3\). Since \(O\) has six vertices, twelve edges, and eight facets, these points have exactly \(26\) distinct normals. Moreover,
\[
\operatorname{Vol}(\Sigma_3)=\frac13,\qquad
\operatorname{Vol}(O)=\frac43,
\]
so a point sampled uniformly by volume from \(O\) has all \(26\) normals with probability exactly \(1/4\).

## Assumptions and scope

Normals are Euclidean normals to support planes, counted by their distinct boundary base points. The body is the standard Euclidean realization \(O=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}\); no affine invariance is asserted. The volume probability is for normalized three-dimensional Lebesgue measure. Points on active-region boundaries are treated separately because a facet normal and an edge normal can then share a base point.

## Proof

For \(s=(s_1,s_2,s_3)\in\{\pm1\}^3\), the facet \(F_s\) is the triangle in the plane \(s\cdot x=1\), with vertices \(s_i e_i\). The orthogonal projection of \(y\) onto this plane is
\[
z=y+\frac{1-s\cdot y}{3}s.
\]
Its barycentric coordinate at vertex \(s_i e_i\) is
\[
\lambda_i=s_i y_i+\frac{1-s\cdot y}{3},\qquad
3\lambda_i=1+2s_i y_i-s_jy_j-s_ky_k.
\]
Thus every facet contributes a normal with base in its relative interior precisely when all these expressions are positive. Requiring nonnegativity for every sign vector and every \(i\) is equivalent to
\[
1-\|y\|_1-|y_i|\ge0\quad(i=1,2,3),
\]
that is, \(\|y\|_1+\|y\|_\infty\le1\). Strict inequality gives relative-interior facet bases; equality forces at least one facet projection onto an edge.

For an edge with endpoints \(s_i e_i\) and \(s_j e_j\), let \(k\) be the remaining coordinate. Its inner normal cone consists of vectors \(c\) with \(s_i c_i=s_j c_j=-t\le0\) and \(|c_k|\le t\). Writing \(y=z+c\), where \(z\) is the orthogonal foot on the edge, gives
\[
s_i y_i+s_j y_j=1-2t,\qquad |y_k|\le t.
\]
For \(y\in\operatorname{int}O\), the foot lies strictly between the endpoints, since \(|y_i|+|y_j|<1\). Hence the edge contributes a normal exactly when
\[
s_i y_i+s_j y_j+2|y_k|\le1.
\]
Requiring this for every edge and every pair of endpoint signs is again equivalent to \(\|y\|_1+|y_k|\le1\) for each \(k\), or \(y\in\Sigma_3\). In the interior of \(\Sigma_3\), all twelve edge bases lie in relative interiors of their edges.

Every vertex contributes a normal for every \(y\in\operatorname{int}O\): at vertex \(s_i e_i\), the vector from \(y\) to that vertex lies in its normal cone because \(1-s_i y_i\ge1-|y_i|>|y_j|+|y_k|\). Therefore points in \(\operatorname{int}\Sigma_3\) have six vertex, twelve edge, and eight facet normals, all with distinct bases. If \(y\notin\Sigma_3\), some facet projection is outside that facet, so fewer than 26 normals occur. If \(y\in\partial\Sigma_3\), at least one facet projection lies on an edge, causing the corresponding face and edge bases to coincide; it therefore does not have 26 distinct bases. This proves the locus characterization and the maximum count.

It remains to compute the volume. Signed coordinate permutations divide \(\Sigma_3\) into 48 congruent chambers. In one chamber, write \(0\le z\le y\le x\); the defining inequality is \(2x+y+z\le1\). Its volume is
\[
\begin{aligned}
V_0&=\int_0^{1/4}\int_z^{(1-z)/3}
\int_y^{(1-y-z)/2} dx\,dy\,dz\\
&=\int_0^{1/4}\left(\frac1{12}-\frac{2z}{3}+\frac{4z^2}{3}\right)dz
=\frac1{144}.
\end{aligned}
\]
Consequently \(\operatorname{Vol}(\Sigma_3)=48V_0=1/3\). The standard octahedron has volume \(2^3/3!=4/3\), so the required fraction is \((1/3)/(4/3)=1/4\).

## Verification

The geometric argument reduces the face and edge active-region conditions to the same explicit norm inequality. The accompanying `verify.py` evaluates the chamber integral and volume ratio using exact rational arithmetic. The script checks the arithmetic only; it is supplementary to, not a substitute for, the proof above. The claim concerns the locus of maximum normal count, not the full distribution of smaller counts.

## Relationship to prior work

Nasonov, Panina, and Siersma develop active regions for faces of convex polytopes, relate normals to critical points of squared distance, and discuss the average number of normals as a shape indicator. Their paper supplies the framework used here, but the inspected definitions, general bounds, and tetrahedral results do not give the regular octahedron's full-normal locus or its volume fraction. The result identifies that locus with the polyhedral set \(\Sigma_3\), rather than claiming the set itself is a new convex body.

## Limitations

No classification is claimed for stretched octahedra, arbitrary cross-polytopes, or other norms. The probability is a volume fraction for the standard Euclidean octahedron. The distribution of the number of normals outside \(\operatorname{int}\Sigma_3\) is not determined. Bibliographic priority is not exhaustively established, and no independent audit has been performed.

## References

1. I. Nasonov, G. Panina, and D. Siersma, “Concurrent normals problem for convex polytopes and Euclidean distance degree,” arXiv:2406.01773, first submitted 2024-06-03; *Acta Mathematica Hungarica* 174 (2024), 522–538. https://arxiv.org/abs/2406.01773. DOI: 10.1007/s10474-024-01483-2.
