# Block-path connected-block polytopes have parity-split inradii and large incenter loci

## Finding
For every integer \(n\ge2\), let
\[
Q_n=\operatorname{conv}\left(\{\mathbf0\}\cup
\left\{\mathbf1_{[i,j]}:1\le i\le j\le n\right\}\right)\subset\mathbb R^n,
\]
where \(\mathbf1_{[i,j]}\) has entries equal to one on the consecutive interval \([i,j]\) and zero elsewhere. This is the connected-block polytope of a graph whose \(n\) blocks form a path; in particular, for an ordinary path graph, the coordinates index its edges. All distances are standard Euclidean distances in \(\mathbb R^n\).

**Theorem.** The radius of a largest Euclidean ball contained in \(Q_n\) is
\[
\boxed{\rho_n=\begin{cases}
\displaystyle\frac1{1+\sqrt{n-1}},&n\text{ even},\\[5pt]
\displaystyle\frac2{2+\sqrt n+\sqrt{n-2}},&n\text{ odd}.
\end{cases}}
\tag{1}
\]
For \(n\ge3\), the complete set of centers of these maximum inscribed balls is a polytope of affine dimension exactly
\[
\boxed{n-3.}\tag{2}
\]
For \(n=2\), the body is the unit square and its incenter is uniquely \((1/2,1/2)\).

Here is an explicit full description of the incenter polytope. Let \(\mathcal F_n\) denote the set of \(\{-1,0,1\}\)-vectors whose nonzero coordinates, read from left to right, form an alternating sequence starting and ending in \(+1\). Their number of nonzero coordinates \(\ell(\alpha)\) is necessarily odd. Define two distinguished facet normals:

If \(n\ge4\) is even, set
\[
a=(1,-1,1,-1,\ldots,1,0),\qquad
b=(0,1,-1,1,\ldots,-1,1).
\tag{3}
\]
Their supports each have size \(n-1\). If \(n\ge3\) is odd, set
\[
a=(1,-1,1,-1,\ldots,-1,1),\qquad
b=(0,1,-1,1,\ldots,-1,1,0).
\tag{4}
\]
Their supports have sizes \(n\) and \(n-2\). In both cases \(a+b=e_1+e_n\). Then the complete incenter set is
\[
\boxed{\begin{aligned}
\mathcal I_n=\bigl\{c\in\mathbb R^n:\;&c_1=c_n=\rho_n,\\
&\langle a,c\rangle=1-\rho_n\|a\|_2,\\
&c_i\ge\rho_n\quad(1\le i\le n),\\
&\langle\alpha,c\rangle+\rho_n\sqrt{\ell(\alpha)}\le1
\quad(\alpha\in\mathcal F_n)\bigr\}.
\end{aligned}}
\tag{5}
\]
The two endpoint equalities and the additional equality involving \(a\) are linearly independent for every \(n\ge3\). The remaining constraints do not further reduce the affine hull, giving (2). Thus in dimension \(n\ge4\) the incenter is **not unique**, even though the radius is unique.

## Assumptions and scope
The body includes the zero vector as a vertex and is not the convex hull of only the **nonzero** interval vectors. The distinction matters for its facet description and Euclidean inradius. The primary connected-block source identifies exactly this body for a block path and proves a complete facet description in the full graph family (Theorem 5.11). The same work identifies the \(h^*\)-polynomial of \(Q_n\) with the \((n+1)\)-st Narayana polynomial (Theorem 7.6). The present result concerns Euclidean metric geometry, not Ehrhart coefficients.

A unimodular change of coordinates sends \(Q_n\) to a positive type-\(A\) root polytope, but this transformation is not generally an isometry: inradius computed in root coordinates cannot simply be carried over without transforming the metric.

## Proof
**Step 1: the exact facet normals.** Theorem 5.11 of Bruckamp–Chimani–Juhnke gives the inequalities \(x_i\ge0\) and the independent-block inequalities as a complete, irredundant facet system. For a block path, the positive blocks in an independent-block inequality appear at distinct indices \(p_1<\cdots<p_k\), no two consecutive. The definition requires nonpositive integer coefficients between the first and last positive block, with total sum \(-(k-1)\); the inequality for each consecutive pair of positives requires a sum at most \(-1\) in that intervening gap. Since the \(k-1\) gaps are disjoint, each has exactly one coefficient \(-1\), and all other coefficients are zero. Thus the nonzeros alternate
\[
+1,-1,+1,-1,\ldots,-1,+1.
\]
Conversely, each such alternating-sign pattern defines a valid independent-block inequality: every interval between a subset of its positive entries contains at least the requisite number of negative entries. It follows that the complete facet description is
\[
\boxed{Q_n=\{x\in\mathbb R^n:x_i\ge0\ (1\le i\le n),\quad
\langle\alpha,x\rangle\le1\ (\alpha\in\mathcal F_n)\}.}
\tag{6}
\]
The facet normals in \(\mathcal F_n\) have Euclidean norm \(\sqrt{\ell(\alpha)}\), where \(\ell(\alpha)\) is their odd number of nonzeros.

**Step 2: a global upper bound.** Suppose the closed Euclidean ball of center \(c\in Q_n\) and radius \(\rho\ge0\) lies inside \(Q_n\). Its lower-coordinate facet clearances give
\[
c_i\ge\rho\quad(1\le i\le n).
\tag{7}
\]
The two selected independent-block facets in (3) or (4) give
\[
\langle a,c\rangle+\rho\|a\|_2\le1,\qquad
\langle b,c\rangle+\rho\|b\|_2\le1.
\tag{8}
\]
Using \(a+b=e_1+e_n\) and \(c_1+c_n\ge2\rho\), add (8) to obtain
\[
2\ge\rho(2+\|a\|_2+\|b\|_2).
\tag{9}
\]
For even \(n\), \(\|a\|_2=\|b\|_2=\sqrt{n-1}\); for odd \(n\), these norms are \(\sqrt n\) and \(\sqrt{n-2}\). Equation (9) is exactly the upper bound (1). Equality for any optimal \(c\) forces
\[
c_1=c_n=\rho_n,\qquad
\langle a,c\rangle=1-\rho_n\|a\|_2,\qquad
\langle b,c\rangle=1-\rho_n\|b\|_2.
\tag{10}
\]
The last equality follows automatically from the preceding equalities and \(a+b=e_1+e_n\).

**Step 3: achieving the bound for even dimensions.** For even \(n\ge2\), take
\[
c^0=\rho_n\mathbf1.
\tag{11}
\]
Every alternating-sign facet normal \(\alpha\) has coordinate sum one, so
\[
\langle\alpha,c^0\rangle+\rho_n\|\alpha\|_2
=\rho_n\bigl(1+\sqrt{\ell(\alpha)}\bigr)
\le\rho_n(1+\sqrt{n-1})=1.
\tag{12}
\]
Every lower-coordinate clearance is also exactly \(\rho_n\), so this ball is feasible and (1) is sharp. The case \(n=2\) is the unit square.

**Step 4: achieving the bound for odd dimensions.** Write \(n=2m+1\ge3\), put
\[
\delta_n=\frac{(\sqrt n-\sqrt{n-2})\rho_n}{n-1},
\tag{13}
\]
and define
\[
c_i^0=\begin{cases}
\rho_n,&i\text{ odd},\\
\rho_n+\delta_n,&i\text{ even}.
\end{cases}
\tag{14}
\]
Then the \(a\)- and \(b\)-facets are both exactly tangent:
\[
\langle a,c^0\rangle+\rho_n\sqrt n
=\langle b,c^0\rangle+\rho_n\sqrt{n-2}=1.
\tag{15}
\]
For any other \(\alpha\in\mathcal F_n\), the number of its nonzero entries is an odd \(\ell\le n-2\). Since its coordinate sum is one,
\[
\langle\alpha,c^0\rangle
=\rho_n+\delta_n\sum_{i\text{ even}}\alpha_i
\le\rho_n+m\delta_n.
\tag{16}
\]
Consequently
\[
\langle\alpha,c^0\rangle+\rho_n\sqrt\ell
\le\rho_n+m\delta_n+\rho_n\sqrt{n-2}=1.
\tag{17}
\]
The lower-coordinate clearances are at least \(\rho_n\). Therefore the odd-dimensional upper bound is attained as well.

**Step 5: the complete incenter locus and its dimension.** The full facet system (6) gives the necessary-and-sufficient clearance inequalities in (5). The equalities in (10) are forced by the globally sharp bound; hence (5) is the complete incenter set. The two endpoint coordinate constraints and the \(a\)-constraint are independent for \(n\ge3\), so
\[
\dim\operatorname{aff}\mathcal I_n\le n-3.
\tag{18}
\]
We prove equality by exhibiting a feasible center with **all inequalities except those forced by (10) strictly slack**.

For even \(n\ge4\), start from (11) and increase each interior coordinate \(2,\ldots,n-1\) by the same sufficiently small \(\varepsilon>0\). The endpoint equalities stay fixed. For \(a\) and \(b\), the sums of their interior coefficients are zero, so (10) remains tight. A facet normal of maximal possible support size \(n-1\) omitted at an **interior** index has interior coefficient sum \(-1\), so its formerly tight inequality becomes strict. The only maximal-support facets omitted at endpoints are precisely \(a\) and \(b\). Shorter-support facets had strictly positive clearance slack at (11) and remain strict for small \(\varepsilon\). Interior coordinate facets also become strict.

For odd \(n=2m+1\ge5\), the center (14) already makes all upper independent-block facets other than \(a,b\) strictly slack. Indeed, equality in (17) requires both \(\ell=n-2\) and that every one of the \(m\) even coordinate coefficients equal \(+1\); the unique alternating-sign normal with these properties is \(b\). Now increase each interior odd coordinate by \(\varepsilon>0\) and increase each even coordinate by \(\frac{m-1}{m}\varepsilon\). There are \(m-1\) interior odd positions and \(m\) even positions, so these variations preserve both \(\langle a,c\rangle\) and \(\langle b,c\rangle\). For sufficiently small \(\varepsilon\), all other upper facets remain strict and all interior lower-coordinate facets become strict.

Thus, in either parity, the feasible center set has a relative interior point in the affine subspace specified by the three independent equations in (10), proving
\[
\dim\operatorname{aff}\mathcal I_n=n-3.
\]
For \(n=3\), those equations already specify a single point, so the dimension statement also holds. This completes the proof.

## Verification
The theorem and equality cases are symbolic and apply to every integer \(n\ge2\). The accompanying `verify.py` enumerates the entire alternating-sign facet system through \(n=14\), independently solves the exact facet-clearance linear program numerically in each dimension, tests the displayed closed-form centers, and checks that explicit interior perturbations have exactly three linearly independent active facet normal directions for \(4\le n\le14\). For dimensions \(2\le n\le6\), it additionally enumerates all interval-indicator vertices and compares the predicted facets against every supporting hyperplane returned by an independent convex-hull calculation. Finite checks corroborate, but do not replace, the arbitrary-dimensional proof.

## Relationship to prior work
Bruckamp, Chimani, and Juhnke establish the complete facet system for connected-block polytopes; in the block-path case they also derive Narayana \(h^*\)-data through a unimodular equivalence with a positive root polytope. They do not give the Euclidean inradius or classify its centers.

Didi Biha, Kerivin, and Ng give an earlier polyhedral characterization of connected-subgraph polytopes on trees; on a path their connected-edge-set formulation specializes to the same interval-indicator body including zero, but their work addresses optimization and facet descriptions rather than Euclidean inscribed balls.

Beck, De Silva, Dorfsman-Hopkins, Pruitt, and Ruiz examine interval-vector polytopes and their Catalan/Ehrhart structure. Their specifically named complete interval-vector polytope is generated by all **nonzero** interval vectors; the zero-inclusive body here is distinct, and their inspected text does not contain inradius or Euclidean-center computations.

The new result describes a genuine metric invariant for the standard interval-incidence coordinates; unimodular equivalence to root polytopes, though valuable in lattice geometry, does not preserve the Euclidean inradius. The parity split and the dimension \(n-3\) of the full incenter locus do not follow from the known Ehrhart or facet enumeration statements without the additional sharp facet-clearance analysis above.

## Limitations
The result concerns the standard unweighted, zero-inclusive interval-incidence realization. General connected-block graphs, weighted or affine-distorted realizations, inscribed ellipsoids, and other Euclidean metrics are not covered. The full incenter polytope is given by an exact facet description, but its own vertex count and combinatorial type are not claimed. Since its proof uses elementary operations once the nonstandard complete facet description is known, independently rediscovered metric formulations under root-polytope or interval-vector terminology remain possible.

## References
1. Justus Bruckamp, Markus Chimani, Martina Juhnke, *On the Connected Blocks Polytope*, arXiv:2304.06318, first public version 2023-04-13; *Discrete & Computational Geometry* 73 (2025), 946–972, DOI 10.1007/s00454-024-00675-5, especially Definition 5.2, Theorem 5.11, and Theorem 7.6.
2. Mohamed Didi Biha, Hervé L. M. Kerivin, Peh H. Ng, *Polyhedral study of the connected subgraph problem*, *Discrete Mathematics* 338 (2015), 80–92, DOI 10.1016/j.disc.2014.08.026, especially Theorem 6 for trees.
3. Matthias Beck, Jessica De Silva, Gabriel Dorfsman-Hopkins, Joseph Pruitt, Amanda Ruiz, *The combinatorics of interval-vector polytopes*, *Electronic Journal of Combinatorics* 20 (2013), #P22, arXiv:1211.2039, especially Sections 1 and 3.
