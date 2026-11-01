# Finite-scale saturation of translate depth for every polyhedral testing body

## Finding
Let \(K\subset\mathbb R^d\), \(d\ge2\), be a full-dimensional bounded convex polytope, with irredundant unit outward facet normals \(u_1,\ldots,u_m\). Let \(\mu\) be any Borel probability distribution supported in a Euclidean ball \(B_R\). For a testing body \(tK\), define its translate depth at \(y\) by
\[
\mathsf d_{tK}(y;\mu)=1-\sup_{z:\,y\notin tK+z}\mu(tK+z).
\]
Choose \(p_i\) in the relative interior of facet \(i\), and write
\[
K=\{x:\langle u_j,x\rangle\le b_j,\;1\le j\le m\},\qquad
\delta_{ij}=b_j-\langle u_j,p_i\rangle>0\quad(i\ne j).
\]
Then for **all** \(y\in\mathbb R^d\), **all** compactly supported \(\mu\) as above (including atomic laws), and **all** \(t>0\) with \(t\ge t_0\), with
\[
t_0=\max_{i\ne j}\frac{2R}{\delta_{ij}},
\]
one has the exact finite-scale identity
\[
\boxed{\mathsf d_{tK}(y;\mu)=\min_{1\le i\le m}\mu\{x:\langle u_i,x\rangle\ge\langle u_i,y\rangle\}.}
\]
If the support ball is centered at a point other than the origin, simultaneously translate the distribution and the query point to the origin before using the displayed cutoff; its numerical value remains the same. Thus every depth region above the cutoff is the intersection of at most \(m\) one-dimensional projection quantile halfspaces, and is independent of \(t\).

The saturation may occur at a genuinely positive scale. For \(K=[-1,1]^2\), \(\mu\) uniform on the same square, and \(y=0\), the complete pre-saturation profile is
\[
\boxed{\mathsf d_{tK}(0;\mu)=
\begin{cases}
1-t^2,&0<t\le1/2,\\
1-t/2,&1/2\le t\le1,\\
1/2,&t\ge1.
\end{cases}}
\]
Its exact first saturation time at this query point is \(t=1\). The general cutoff \(t_0\) is an explicit sufficient bound, not asserted to be globally sharp.

## Assumptions and scope
The polytope is bounded, full-dimensional, and described by its genuine facets, rather than redundant halfspaces. The distribution is an arbitrary Borel probability measure with support contained in a closed Euclidean ball of radius \(R\ge0\). No density, non-atomicity, generic position, or hyperplane-null hypothesis is required. The testing parameter satisfies \(t>0\), including the case \(R=0\), where the formula holds for every \(t>0\). All depth infima and suprema use translates missing the query point as a point of a closed set.

## Proof
Translate the ambient coordinates so that \(\mu(B_R)=1\) for \(B_R\) centered at the origin. Denote the right-side minimum by \(H(y)\). If a translate \(tK+z\) misses \(y\), at least one of its facet inequalities is violated at \(y\). Thus for some \(i\),
\[
tK+z\subseteq\{x:\langle u_i,x\rangle\le c_i\},\qquad c_i<\langle u_i,y\rangle,
\]
where the strict comparison to the query coordinate follows because every point of the closed translate satisfies \(\langle u_i,x\rangle\le c_i\), and \(c_i<\langle u_i,y\rangle\). Consequently
\[
\sup_{z:\,y\notin tK+z}\mu(tK+z)
\le\max_i\mu\{x:\langle u_i,x\rangle<\langle u_i,y\rangle\}=1-H(y).
\]
For the converse, fix facet \(i\) and any \(c\in[-R,R]\). Consider the explicit translate
\[
Q_{i,c,t}=t(K-p_i)+cu_i.
\]
Its \(i\)th facet inequality is \(\langle u_i,x\rangle\le c\). For \(j\ne i\), its \(j\)th facet inequality is
\[
\langle u_j,x\rangle\le t\delta_{ij}+c\langle u_j,u_i\rangle.
\]
If \(t\ge t_0\), this right side is at least \(2R-R=R\), so all these other inequalities hold throughout \(B_R\). Therefore
\[
Q_{i,c,t}\cap B_R=B_R\cap\{x:\langle u_i,x\rangle\le c\}.
\]
If \(c<\langle u_i,y\rangle\), this translate misses \(y\), and its probability equals \(\mu\{\langle u_i,X\rangle\le c\}\). Taking the supremum over such \(c\in[-R,R]\) gives \(\mu\{\langle u_i,X\rangle<\langle u_i,y\rangle\}\): below \(-R\) that value is zero, above \(R\) it is one, and within the interval the equality follows from continuity of measures from below. Maximizing over the finitely many facet indices gives the reverse inequality. This proves exact equality simultaneously for every query point. The case \(R=0\) is obtained by the same geometric construction with \(c=0\) when the strict inequality holds, and by an elementary zero-mass bound in the remaining cases.

For the square example, every axis-aligned square missing the origin must lie strictly on one side of one coordinate hyperplane. By symmetry choose the positive first-coordinate side. Its overlap with \([-1,1]^2\) has maximum area
\[
\min(2t,1)\min(2t,2).
\]
Indeed both factors are independent one-dimensional interval-overlap maxima; arbitrarily small shifts remove any unwanted boundary contact with the origin. Dividing by the ambient area four gives the maximal missed-query translate mass, and elementary evaluation of the two minima yields the stated three-branch depth law. In particular the value is strictly above \(1/2\) for every \(0<t<1\), proving the exact onset.

## Verification
The standalone Python 3 program `verify.py` uses exact rational arithmetic. It checks the facet-translate construction on the square and a right triangle, across rational sample points and offsets, and checks the three-branch square formula for rational testing scales. The actual check returned `VERIFY_OK: 1805 exact rational construction and square-profile comparisons`. These finite checks are supplementary; the proof of the all-dimension, all-measure statement is the facet-slack argument above.

## Relationship to prior work
Molchanov and Nagy, *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*, first posted October 19, 2026 (arXiv:2610.26108v1), define this translate depth in their equation (2.2), prove a general tangent-cone **limit** under a boundary-null assumption in Theorem 5.2, and give an isolated square example with eventual stabilization at one query point in Example 5.11. The present result proves exact **uniform-in-query finite-time saturation for every polytope and every compactly supported law**, without any boundary-null assumption, and supplies an explicit geometric cutoff and an independent sharp scale-onset example. The general asymptotic convergence assertion is not equivalent to finite stabilization; its proof does not state a uniform finite threshold. Ordinary finite-direction Tukey depth is an antecedent to the limiting expression, not to the finite-scale identity.

## Limitations
The cutoff depends on a choice of relative-interior facet points and may not be minimal. The theorem does not extend by this proof to noncompactly supported distributions or nonpolyhedral testing bodies. No characterization of all bodies admitting finite stabilization is asserted. The square exact-onset example is specific to the stated measure and query point. Historical priority beyond the inspected literature and accessible mathematical-record searches is not independently certified.

## References
1. I. Molchanov and S. Nagy, *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*, arXiv:2610.26108v1, October 19, 2026, Sections 2.2, 5.1–5.2, Example 5.11. https://arxiv.org/html/2610.26108v1
2. J. A. Cuesta-Albertos and A. Nieto-Reyes, *The random Tukey depth*, arXiv:0707.0167, 2007. The abstract was consulted for context on finite-direction projections; it does not establish a translate-body stabilization theorem.
