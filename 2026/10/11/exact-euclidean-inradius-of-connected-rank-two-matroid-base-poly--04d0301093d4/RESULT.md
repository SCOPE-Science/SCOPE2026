# Exact Euclidean inradius of connected rank-two matroid base polytopes
## Finding
Let \(M\) be a connected loopless rank-two matroid on a ground set of size \(n\). Its parallel classes are \(C_1,\ldots,C_s\), with \(s\ge3\), \(h_j=|C_j|\), and \(\sum_{j=1}^s h_j=n\). Write
\[
P(M)=\operatorname{conv}\{e_a+e_b:a,b\text{ belong to distinct parallel classes}\}.
\]
The polytope lies in the affine hyperplane \(H=\{x\in\mathbb R^n:\sum_i x_i=2\}\). Its Euclidean inradius, measured intrinsically in \(H\), is
\[
r(P(M))=\min\!\left\{\frac{2}{\sqrt{n(n-1)}},\ \frac{\sqrt n\,(s-2)}{\sum_{j=1}^s\sqrt{h_j(n-h_j)}},\ \min_{1\le j\le s}\frac{\sqrt n}{h_j\sqrt{n-1}+\sqrt{h_j(n-h_j)}}\right\}.
\]
Thus the metric invariant depends only on the parallel-class sizes. The three competing terms come respectively from all coordinate facets together, all class-sum facets together, and the compatibility of the lower coordinate clearances with one class-sum clearance.

## Assumptions and scope
The matroid is loopless, has rank two, and is connected. For rank two, connectedness is equivalent to having at least three parallel classes. Distances and balls are taken inside the affine hull \(H\), with the Euclidean metric inherited from \(\mathbb R^n\). This intrinsic convention is essential because the ambient \(n\)-dimensional inradius is zero.

For a point \(x\), write \(x(C_j)=\sum_{i\in C_j}x_i\). The exact description used below is
\[
P(M)=\{x\in H:x_i\ge0\text{ for every }i,\ x(C_j)\le1\text{ for }1\le j\le s\}.
\]
Indeed, every basis indicator satisfies these inequalities. Conversely, if \(x\) satisfies them, then the class totals \(t_j=x(C_j)\) lie in \([0,1]\) and sum to \(2\), hence \((t_1,\ldots,t_s)\) lies in the hypersimplex \(\Delta_{2,s}\), the convex hull of \(e_j+e_k\). A convex decomposition of the class totals can be refined inside each class pair by distributing mass according to the coordinate proportions of \(x\), yielding a convex decomposition into basis indicators.

## Proof
Let \(H_0=\{y:\sum_i y_i=0\}\) be the translation space of \(H\). The restriction of the coordinate functional \(x\mapsto x_i\) to \(H_0\) has norm
\[
A=\sqrt{\frac{n-1}{n}}.
\]
Therefore the intrinsic distance from \(c\in H\) to \(x_i=0\) is \(c_i/A\).

For a class \(C_j\), the projection of its indicator vector to \(H_0\) has norm
\[
B_j=\sqrt{\frac{h_j(n-h_j)}{n}},
\]
so the intrinsic distance from \(c\) to \(x(C_j)=1\) is \((1-c(C_j))/B_j\).

Consequently a radius-\(r\) ball centered at \(c\) lies in \(P(M)\) exactly when
\[
c_i\ge rA\quad\text{for all }i,
\qquad
c(C_j)\le1-rB_j\quad\text{for all }j.
\]
Summing the coordinate inequalities and using \(\sum_i c_i=2\) gives
\[
r\le \frac{2}{nA}=\frac{2}{\sqrt{n(n-1)}}.
\]
Summing the class inequalities gives
\[
r\le \frac{s-2}{\sum_j B_j}
=\frac{\sqrt n\,(s-2)}{\sum_j\sqrt{h_j(n-h_j)}}.
\]
Finally, within class \(C_j\), the coordinate inequalities imply \(c(C_j)\ge h_jrA\). Compatibility with the corresponding upper inequality requires
\[
h_jrA\le1-rB_j,
\]
that is
\[
r\le\frac{1}{h_jA+B_j}
=\frac{\sqrt n}{h_j\sqrt{n-1}+\sqrt{h_j(n-h_j)}}.
\]
These are necessary bounds.

They are also sufficient. Suppose \(r\) satisfies all three families of bounds. For every class define the interval
\[
I_j=[h_jrA,\,1-rB_j].
\]
The individual bounds make every \(I_j\) nonempty. The first aggregate bound gives \(\sum_j\inf I_j\le2\), while the second gives \(\sum_j\sup I_j\ge2\). Hence one can choose \(t_j\in I_j\) with \(\sum_jt_j=2\). Setting \(c_i=t_j/h_j\) for \(i\in C_j\) produces a center whose distance to every defining supporting hyperplane is at least \(r\). Taking \(r\) equal to the minimum of the necessary bounds proves the formula.

The same argument shows that, at the optimal radius \(r_*\), the complete Chebyshev-center set is
\[
\{c\in H:c_i\ge r_*A\text{ for all }i,\ c(C_j)\le1-r_*B_j\text{ for all }j\}.
\]

## Verification
The accompanying `verify.py` independently evaluates the interval feasibility problem for every integer partition of \(n\) with at least three parts through \(n=24\). It computes the closed formula at high precision and compares it with a binary search for the largest feasible radius using only the interval inequalities. It also constructs feasible class totals at the claimed optimum. This finite computation is a regression check, not a substitute for the proof for arbitrary \(n\).

## Relationship to prior work
Ferroni and Schröter identify loopless rank-two matroid base polytopes with edge polytopes of complete multipartite graphs and give an explicit face-number formula in terms of the part sizes. Their accessible full article focuses on face enumeration; document-wide searches for “inradius”, “Euclidean”, and “metric” return no occurrence. The earlier Ohsugi–Hibi work on the same complete-multipartite edge polytopes announces compressedness, toric initial ideals, face numbers, Ehrhart polynomials, and normalized volumes. None of the accessible statements supplies the intrinsic Euclidean inradius or its center set.

The present formula is not a face-count specialization: it uses the Euclidean norms of the projected facet normals and solves the simultaneous clearance problem among coordinate and class-sum inequalities.

## Limitations
The result covers connected loopless rank-two matroids only. The disconnected case with exactly two parallel classes is a product of simplices and is intentionally outside the statement. No claim is made for higher-rank matroids. The inradius is intrinsic to the affine hull. The literature comparison cannot exclude an unindexed statement in inaccessible material; in particular, the full Ohsugi–Hibi article was not available in the source inspected, so its abstract and bibliographic description were the material read.

## References
1. L. Ferroni and B. Schröter, *Face enumeration for split matroid polytopes*, arXiv:2310.05487, first posted 2023-10-09; Combinatorics, Probability and Computing 34 (2025), 528–544, DOI:10.1017/S0963548325000021.
2. H. Ohsugi and T. Hibi, *Compressed polytopes, initial ideals and complete multipartite graphs*, Illinois Journal of Mathematics 44 (2000), 391–406, DOI:10.1215/ijm/1255984847.
