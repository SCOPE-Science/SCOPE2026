# A dimension-stable inball and codimension-four incenter family for Catalan matroid polytopes

## Finding

Let \(n\ge 2\) be an integer. Form the **Catalan matroid base polytope** \(P_n\subset\mathbb R^{2n}\) by taking the convex hull of indicator vectors of the up-step positions of all Dyck paths with \(n\) up-steps and \(n\) down-steps. Give its affine hull the metric inherited from the standard Euclidean inner product. Put
\[
m=2n-2,\qquad a_m=\sqrt{\frac{m-1}{m}},\qquad c_m=\sqrt{\frac{m-2}{2m}}.
\]
The exact intrinsic Euclidean inradius is
\[
\boxed{r(P_n)=\frac{1}{2(a_m+c_m)}.}
\]
It decreases strictly as \(n\) increases and has the positive limit
\[
\boxed{\lim_{n\to\infty}r(P_n)=1-\frac1{\sqrt2}.}
\]
For \(n=2\) and \(n=3\), the largest inscribed ball has a unique center. For every \(n\ge4\), the complete set of centers of largest balls is a polytope of affine dimension
\[
\boxed{2n-7=\dim(P_n)-4.}
\]
The entire incenter set is described explicitly below. Thus this family has an inradius bounded away from zero despite its growing intrinsic dimension, and all but four affine center coordinates remain free subject to explicit linear constraints.

## Assumptions and scope

A Dyck path is a word of length \(2n\) in up and down steps with \(n\) of each, and with at least as many up as down steps in every prefix. For a Dyck path \(D\), its indicator vector \(x(D)\in\{0,1\}^{2n}\) has entry \(1\) exactly at its up-step positions. Let \(P_n=\operatorname{conv}\{x(D)\}\). Every such vector has \(x_1=1\), \(x_{2n}=0\), and coordinate sum \(n\).

Use the isometric intrinsic coordinates
\[
y_i=x_{i+1}\quad(1\le i\le m),\qquad H_m=\left\{y\in\mathbb R^m:\sum_{i=1}^{m}y_i=\frac m2\right\}.
\]
For \(1\le k\le n-2\), set \(b_{k,m}=\sqrt{2k(m-2k)/m}\). For \(n\ge3\), define \(r=r(P_n)\), \(h=c_mr=\frac12-a_mr\), and \(z_i=y_i-\frac12\).

The exact incenter set for \(n\ge3\) consists of points in \(H_m\) satisfying
\[
\begin{gathered}
z_1=z_2=h,\qquad z_{m-1}=z_m=-h,\\
-h\le z_i\le h\quad(3\le i\le m-2),\qquad \sum_{i=3}^{m-2}z_i=0,\\
\sum_{i=3}^{2k}z_i\ge r b_{k,m}-2h\qquad(2\le k\le n-3).
\end{gathered}
\]
When an index range is empty, its condition is vacuous. For \(n=3\) the four displayed fixed coordinates specify a unique point; for \(n=2\) the unique center is \(y=(1/2,1/2)\) and the inradius is \(1/\sqrt2\). For \(n\ge4\), the other coordinates describe a full-dimensional polytope within the hyperplane of their zero sum.

No affine change of coordinates is used to measure distance: inradius and incenter dimension are for the **original** incidence-vector realization with the ambient Euclidean metric restricted to its affine hull.

## Proof

**1. Exact inequality model and affine dimension.** As the first up step and last down step are mandatory, eliminate the fixed first and last coordinates. A \(0\)-\(1\) vector \(y\in\{0,1\}^{m}\) arises precisely when its sum is \(m/2\) and the even-prefix ballot constraints hold. Its convex hull is
\[
Q_m=\left\{y\in H_m:0\le y_i\le1\ (1\le i\le m),\quad
\sum_{i=1}^{2k}y_i\ge k\ (1\le k\le n-2)\right\}.
\]
Indeed, the odd-position Dyck restrictions become these even-prefix inequalities, and the intervening Dyck restrictions follow from their predecessors and coordinate nonnegativity. To see that the displayed continuous system is the convex hull, introduce partial sums \(s_j=\sum_{i=1}^{j}y_i\), with \(s_0=0\) and \(s_m=m/2\). The conditions become the integer difference inequalities \(0\le s_j-s_{j-1}\le1\) and \(s_{2k}\ge k\). Their matrix on the free partial sums is a directed-network incidence matrix (with some rows deleted or signed), and is totally unimodular. Therefore all vertices have integral \(s_j\), hence \(y_i\in\{0,1\}\); they are exactly the Dyck vectors. This also agrees with the established facet/halfspace description of lattice path matroid polytopes [1,2]. Choosing small positive first-half deviations and opposite last-half deviations from \(1/2\) gives a strict feasible point of all the inequalities relative to \(H_m\); thus \(\dim P_n=m-1=2n-3\).

**2. Intrinsic normal lengths.** The orthogonal projection of the standard coordinate normal \(e_i\) onto the tangent subspace \(\mathbf1^\perp\) of \(H_m\) has norm \(a_m\). The projection of the prefix normal \(e_1+\cdots+e_{2k}\) has norm \(b_{k,m}\). Hence a closed Euclidean ball of radius \(r\) centered at \(y\in H_m\) lies in \(Q_m\) if and only if
\[
r a_m\le y_i\le1-r a_m\quad(1\le i\le m),\qquad
\sum_{i=1}^{2k}y_i\ge k+r b_{k,m}\quad(1\le k\le n-2).
\]
This equivalence applies to the complete halfspace model, whether or not any particular displayed inequality is redundant as a facet inequality.

**3. Upper bound and construction.** Suppose \(n\ge3\). The first prefix inequality and the first two coordinate upper bounds force
\[
1+r b_{1,m}\le y_1+y_2\le2(1-r a_m),
\]
so \(r\le1/(2a_m+b_{1,m})=1/[2(a_m+c_m)]\), because \(b_{1,m}=2c_m\). For \(n=2\), the coordinate bounds and the sum-one equation give the same bound with \(c_m=0\).

For the reverse inequality take \(r=1/[2(a_m+c_m)]\) and \(h=c_mr\). Set \(z_i=h\) for \(i\le m/2\) and \(z_i=-h\) for \(i>m/2\), and take \(y_i=1/2+z_i\). The coordinate bounds hold at equality because \(h=1/2-a_mr\), and the sum is \(m/2\). For any even prefix of length \(\ell=2k\), its excess over \(k\) is
\[
\sum_{i=1}^{\ell}z_i=h\min(\ell,m-\ell).
\]
Writing \(t=\min(\ell,m-\ell)\ge2\), we have
\[
\frac{b_{k,m}}{\min(\ell,m-\ell)}
=\sqrt{\frac{m-t}{mt}}
\le\sqrt{\frac{m-2}{2m}}=c_m.
\]
Thus every inward-shifted prefix inequality holds. This proves the exact radius for all \(n\ge2\).

**4. Every incenter and its dimension.** For \(n\ge3\), equality in the first-prefix upper-bound argument forces \(y_1=y_2=1-r a_m\), equivalently \(z_1=z_2=h\). The last prefix, at length \(m-2\), combined with \(\sum z_i=0\) and the two last coordinate lower bounds, forces \(z_{m-1}=z_m=-h\). The remaining constraints are precisely the ones stated in the theorem. Conversely, any point satisfying that list obeys every radius-\(r\) halfspace condition, so is an incenter.

For \(n\ge4\), the \(m-4\) middle deviations have one independent zero-sum equality, giving an upper bound \(m-5\) on the incenter dimension. This bound is attained: start from the step-sign configuration in step 3. For every *nonendpoint* prefix, its distance inequality is strict, because in the displayed bound the inequality is strict when \(2<\min(\ell,m-\ell)\). Keep the first and last two deviations fixed and multiply all middle deviations by a scalar slightly below \(1\). Their sum remains zero, their coordinate bounds become strict, and all nonendpoint prefix bounds remain strict by continuity. The resulting point lies in the relative interior of an \((m-5)\)-dimensional affine patch. Hence the incenter dimension is \(m-5=2n-7\). When \(n=3\), all four deviations are fixed, so the center is unique; the \(n=2\) segment also has a unique midpoint.

**5. Limit and monotonicity.** Both \(a_m=\sqrt{1-1/m}\) and \(c_m=\sqrt{1/2-1/m}\) increase strictly with the even integer \(m\ge2\). The inradius therefore decreases strictly. Their limits are \(1\) and \(1/\sqrt2\), giving \(r\to1/(2+\sqrt2)=1-1/\sqrt2\).

## Verification

The companion standalone script `verify.py` implements the exact halfspace model and the induced-normal Euclidean-radius linear program. It compares the linear-programming optimum to the theorem for every \(3\le n\le34\), tests explicit feasible centers, and independently enumerates Dyck up-step vectors for \(3\le n\le8\) to check the ballot description and Catalan vertex counts. It requires Python 3 with NumPy and SciPy. These finite checks are supporting evidence; the argument above proves the all-\(n\) statement.

## Relationship to prior work

Bidkhori [1] gave facet and inequality descriptions and the intrinsic dimension of Catalan/lattice-path matroid polytopes. Knauer, Martínez-Sandoval, and Ramírez Alfonsín [2] studied integer points, Ehrhart theory and affine distributive realizations; those affine maps need not preserve Euclidean inradii. Engström, Sanyal and Stump [3] studied their standard complexes. Chen, Li and Yao [4] studied valuative invariants, including volume and Ehrhart data, but the metric inradius is not a valuative invariant covered by those formulas. None of these inspected results states the sharp Euclidean inradius together with its full incenter-locus dimension. The novelty assertion is conditional on the inspected literature and searches, not a claim that all historical formulations have been excluded.

## Limitations

The result concerns the standard incidence-vector embedding and not arbitrary affine realizations of the same matroid polytope. It treats ordinary Catalan matroids, not general \((a,b)\)-Catalan or arbitrary lattice path matroids. It gives the radius and affine dimension of the entire center set, but no formula for its face numbers or Euclidean volume. No independent mathematical audit or global historical-priority certification is asserted.

## References

[1] H. Bidkhori, *Lattice Path Matroid Polytopes*, first arXiv version 22 December 2012, arXiv:1212.5705, especially Lemmas 3.8--3.10. https://arxiv.org/abs/1212.5705

[2] K. Knauer, L. Martínez-Sandoval and J. L. Ramírez Alfonsín, *On lattice path matroid polytopes: integer points and Ehrhart polynomial*, arXiv:1701.05529, first submitted 19 January 2017. https://arxiv.org/abs/1701.05529

[3] A. Engström, R. Sanyal and C. Stump, *Standard Complexes of Matroids and Lattice Paths*, Vietnam J. Math. 50 (2022), 763--779, DOI:10.1007/s10013-021-00546-z.

[4] Y. Chen, Y. Li and M. Yao, *Valuative Invariants of Catalan Matroids*, arXiv:2503.19621, first submitted 25 March 2025.
