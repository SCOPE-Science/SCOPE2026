# Exact John ellipsoids and an order-six roundness transition for complete-graph spanning-tree polytopes

## Finding
For every integer \(n\ge4\), let \(E=E(K_n)\) be the \(m=\binom n2\) edges of the complete graph and let
\[
P_n=\operatorname{conv}\{\mathbf1_T:T\subseteq E\text{ is a spanning tree}\}\subset\{x\in\mathbb R^E:\mathbf1_E^{\mathsf T}x=n-1\}.
\]
Use the intrinsic Euclidean metric of this affine hull, and set \(c=(2/n)\mathbf1_E\). Let \(B\) be the unsigned vertex-edge incidence matrix. On \(H_0=\{y:\mathbf1_E^{\mathsf T}y=0\}\), define the orthogonal projectors
\[
\Pi_U=\frac1{n-2}B^{\mathsf T}\left(I_n-\frac1n\mathbf1_n\mathbf1_n^{\mathsf T}\right)B,
\qquad
\Pi_W=I_{H_0}-\Pi_U.
\]
Their ranks are respectively \(n-1\) and \(n(n-3)/2\). The **unique maximum-volume inscribed ellipsoid** of \(P_n\) is
\[
\boxed{J(P_n)=\left\{c+y:y\in H_0,\quad
\frac{\|\Pi_Uy\|_2^2}{a_n}+\frac{\|\Pi_Wy\|_2^2}{b_n}\le1\right\},}
\]
where the squared principal semiaxes are exactly
\[
\boxed{(a_n,b_n)=
\begin{cases}
\left(\dfrac{n-2}{n(n-1)},\dfrac{2}{n(n-3)}\right),&n\in\{4,5\},\\[5pt]
\left(\dfrac{4(n-1)}{n(n-2)(n+1)},\dfrac{4(n-1)}{n(n-2)(n+1)}\right),&n\ge6.
\end{cases}}
\]
Thus \(J(P_n)\) is strictly anisotropic in dimensions corresponding to \(n=4,5\) and is **exactly a Euclidean ball for all \(n\ge6\)**. Its intrinsic volume is
\[
\operatorname{vol}_{m-1}J(P_n)=\frac{\pi^{(m-1)/2}}{\Gamma(1+(m-1)/2)}\,
 a_n^{(n-1)/2}b_n^{n(n-3)/4}.
\]
Every coordinate facet \(x_e=0\) touches the John ellipsoid. When \(n=4\), all \(16\) facets touch: the \(6\) coordinate facets, \(6\) two-vertex induced-edge facets \(x_e=1\), and \(4\) co-singleton facets. When \(n=5\), precisely the \(10\) coordinate facets and \(5\) co-singleton facets touch. When \(n\ge6\), **only the \(m\) coordinate facets touch**.

A positive John decomposition certifying global optimality uses the same weight on each coordinate contact and (when present) on each co-singleton contact:
\[
\boxed{
\begin{array}{c|cc}
n&\text{each coordinate contact}&\text{each co-singleton contact}\\\hline
4&1/2&1/2\\
5&4/5&1/5\\
\ge6&(m-1)/m&0
\end{array}}
\]
These contact weights satisfy both zero-first-moment and identity-second-moment conditions in the full intrinsic affine hull, ruling out **all** off-center or non-invariant competing ellipsoids.

For completeness, the \(n=3\) polytope is an equilateral triangle whose unique John ellipsoid is the inscribed Euclidean circle of squared radius \(1/6\), centered at \((2/3)\mathbf1_E\), contacting its three upper coordinate facets.

## Assumptions and scope
All graphs are simple, undirected and complete. The metric is that induced by \(\mathbb R^E\) on the fixed-edge-sum affine hull, not by deleting an edge coordinate. Both \(\Pi_U\) and \(\Pi_W\) are orthogonal projections on \(H_0\), not on all of \(\mathbb R^E\). The numbers \(a_n,b_n\) are squared Euclidean semiaxes. Contacts refer to actual supporting facets (not all redundant subset inequalities). The assertion for \(n=3\) is a separate planar boundary case. No assumption about a prescribed ellipsoid center or shape is imposed in the optimality claim.

We use the known graphic-matroid spanning-tree halfspace description
\[
P_n=\{x:\mathbf1_E^{\mathsf T}x=n-1,\quad x_e\ge0\ (e\in E),\quad
x(E(S))\le |S|-1\ (2\le |S|\le n-1)\}.
\tag{1}
\]
Here \(E(S)\) denotes the edges with both endpoints in \(S\). This classical polyhedral description and John's general contact criterion are prior results, not claimed as new theorems.

## Proof
**1. Symmetry and two orthogonal invariant subspaces.** The symmetric group on vertices permutes unordered edges transitively, and it preserves both \(P_n\) and its intrinsic Euclidean metric. The unique maximum-volume inscribed ellipsoid is therefore invariant. The only invariant center in the affine hull is \(c=(2/n)\mathbf1_E\). An invariant quadratic form on unordered edges has entries depending only on whether two edges are identical, adjacent, or disjoint; the resulting commutant is three-dimensional. Removing the trivial constant-edge direction leaves two orthogonal invariant eigenspaces of dimensions \(n-1\) and \(n(n-3)/2\). Directly, for the unsigned incidence matrix \(B\),
\[
 BB^{\mathsf T}=(n-2)I_n+\mathbf1_n\mathbf1_n^{\mathsf T}.
\]
Hence the displayed formula for \(\Pi_U\) is symmetric and idempotent on \(H_0\), with rank \(n-1\); \(\Pi_W=I_{H_0}-\Pi_U\) is its orthogonal complement. The center-fixed invariant ellipsoid consequently has shape operator \(Q=a\Pi_U+b\Pi_W\) for some \(a,b>0\). The later explicit John certificate also proves unrestricted global optimality, independently of this invariant reduction.

**2. Exact containment constraints.** For a nonzero linear inequality with normal \(v\) and slack \(h\) at \(c\), the ellipsoid \(c+Q^{1/2}B_2^{m-1}\) lies inside its halfspace exactly when \(v^{\mathsf T}Qv\le h^2\) (the constant component of \(v\) is immaterial). For every edge-coordinate inequality \(x_e\ge0\), the slack is \(2/n\), and
\[
\|\Pi_Ue_e\|_2^2=\frac2n,
\qquad\|\Pi_We_e\|_2^2=\frac{n-3}{n-1}.
\]
Thus the coordinate bound is
\[
\frac2n a+\frac{n-3}{n-1}b\le\frac4{n^2}.
\tag{2}
\]
For a subset \(S\) of size \(s\), \(2\le s\le n-1\), the upper inequality in (1) has slack
\[
 g_s=(s-1)-\frac2n\binom s2=\frac{(s-1)(n-s)}n.
\]
The squared projected-normal components of \(v_S=\mathbf1_{E(S)}\) are
\[
\alpha_s=\|\Pi_Uv_S\|_2^2=\frac{s(n-s)(s-1)^2}{n(n-2)},
\qquad
\beta_s=\|\Pi_Wv_S\|_2^2
=\binom s2\left(1-\frac{\binom s2}{\binom n2}\right)-\alpha_s.
\tag{3}
\]
To verify (3), the \(n\) entries of \(Bv_S\) equal \(s-1\) on \(S\) and zero outside it. Orthogonally removing their mean and dividing squared length by \(n-2\) gives \(\alpha_s\); subtracting this from the squared norm of the edge-sum projection gives \(\beta_s\). Therefore the exact remaining containment inequalities are
\[
\alpha_s a+\beta_s b\le g_s^2\quad(2\le s\le n-1).
\tag{4}
\]
In particular, at \(s=n-1\), \(\beta_{n-1}=0\), and (4) simplifies to
\[
 a\le A_n:=\frac{n-2}{n(n-1)}.
\tag{5}
\]

**3. The round feasibility transition.** If only the coordinate bound (2) is imposed, maximize the log of the determinant of \(Q\), namely
\[
(n-1)\log a+\frac{n(n-3)}2\log b.
\]
Its unique solution has \(a=b=r_0^2\), where
\[
 r_0^2=\frac{4(n-1)}{n(n-2)(n+1)}.
\tag{6}
\]
The squared intrinsic distance of \(c\) from a subset supporting hyperplane of cardinality \(s\) is
\[
 d_s^2=\frac{g_s^2}{\alpha_s+\beta_s}
=\frac{2(s-1)(n-s)(n-1)}{n\,s\,(n+s-1)}.
\tag{7}
\]
As a real function on \([2,n-1]\), the factor \(f(s)=(s-1)(n-s)/(s(n+s-1))\) increases and then decreases: its logarithmic derivative is
\[
\frac1{s(s-1)}-\frac{2n-1}{(n-s)(n+s-1)},
\]
whose first term strictly decreases and whose second positive term strictly increases. Consequently, the smallest \(d_s^2\) is attained at one of the two endpoints. For \(n\ge4\),
\[
 d_2^2=\frac{(n-2)(n-1)}{n(n+1)}
\ge d_{n-1}^2=\frac{n-2}{n(n-1)}.
\]
Comparing (6) and (5) gives
\[
 r_0^2\le A_n\quad\Longleftrightarrow\quad n^2-7n+8\ge0,
\]
which holds for integer \(n\ge6\) and fails for \(n=4,5\). Thus for every \(n\ge6\), the round ellipsoid is feasible for *all* subset constraints, and every non-coordinate facet has strictly greater slack than the round radius.

**4. The anisotropic small-order solutions.** For \(n=4,5\), retain only the coordinate constraint (2) and co-singleton cap (5). Strict log concavity and the fact that the unrestricted coordinate-only optimizer has \(a=r_0^2>A_n\) force \(a=A_n\). The coordinate inequality binds and then forces
\[
 b=\frac{2}{n(n-3)}.
\]
All other inequalities (4) are feasible: for \(n=4\) the remaining \(s=2\) bound is an equality, and for \(n=5\) the remaining \(s=2,3\) bounds are strict, as follows by direct substitution in (3)–(4). Since this point maximizes a relaxation and belongs to the original feasible set, it is the unique invariant optimum. Together with Step 3, this proves the displayed semiaxis formulas and the complete list of tangent facet orbits.

**5. Explicit unrestricted John certificates.** Write \(p_e=\Pi_{H_0}e_e\) and \(q_v=\Pi_{H_0}\mathbf1_{E([n]\setminus\{v\})}\). The contact normals after mapping the candidate ellipsoid to the unit ball are respectively
\[
 u_e=-Q^{1/2}p_e/(2/n),
\qquad
 v_v=Q^{1/2}q_v/((n-2)/n).
\]
At the indicated contacts these are unit vectors. The two contact orbits satisfy
\[
 \sum_e p_e=0,\quad \sum_v q_v=0,
\qquad
 \sum_e p_ep_e^{\mathsf T}=I_{H_0},\quad
 \sum_v q_vq_v^{\mathsf T}=(n-2)\Pi_U.
\tag{8}
\]
The last identity follows by expanding the co-singleton incidence normals via the centered unsigned incidence matrix. For \(n\in\{4,5\}\), assign each \(u_e\) weight \(w_e=4/(n^2 b)\) and each \(v_v\) weight
\[
 w_v=\frac{(n-2)^2}{n^2}\frac{1-a/b}{(n-2)a};
\]
these simplify to the displayed positive numerical weights. For \(n\ge6\), assign each \(u_e\) weight \(w_e=4/(n^2r_0^2)=(m-1)/m\), using no \(v_v\). All weights are positive on the contacts included. Equation (8) implies directly
\[
 \sum_i w_i u_i=0,
\qquad
 \sum_i w_i u_iu_i^{\mathsf T}=I_{H_0}.
\]
The sum of weights equals \(m-1\) by taking traces. John's contact theorem now proves global optimality among *all* ellipsoids, including asymmetric shapes and displaced centers. Uniqueness of the maximum-volume ellipsoid completes the main proof.

**6. Remaining claims.** The three contact-orbit possibilities and their multiplicities are exactly those found in Steps 3–4 and the known facet description (1). The volume formula follows by multiplying the \(m-1\) principal semiaxes with their rank multiplicities. For \(n=3\), the polytope is the convex hull of the three two-edge incidence vectors, a regular triangle in its affine plane; the distance of its barycenter to an upper-coordinate side is \(1/\sqrt6\), completing the boundary case.

## Verification
The accompanying standard-library Python program `verify.py` uses exact rational arithmetic. It checks **44,252** subset-facet orbit inequalities over the integers \(4\le n\le299\), including every equality case and its strict complement; verifies the contact weight identities for **296** orders \(4\le n\le299\); and independently constructs actual incidence-based projection matrices and cut-normal quadratic forms for \(4\le n\le8\). Run `python verify.py` from the extracted package directory. Its successful terminal marker is `EXACT_VERIFICATION_OK`. These checks are *finite corroboration*, not a proof of all orders: the all-order claims follow from Steps 1–6 above.

## Relationship to prior work
The classical graphic-matroid and spanning-tree descriptions, as treated by Chaourar [1] and Pineda-Villavicencio–Schröter [2], provide (1) and the relevant polyhedral framework. These pre-existing facets and symmetry facts are not claimed as new. General maximum-volume ellipsoid conditions, as surveyed or extended by Ivanov–Naszódi [3], provide the universal contact criterion. Existing work on Löwner–John ellipsoids of the **metric polytope** [4] addresses a distinct family defined by triangle metric inequalities, not a spanning-tree incidence polytope.

Related known results determine the **largest Euclidean ball** of general connected matroid base polytopes and Minkowski asymmetry centers for complete-graph spanning-tree polytopes; those do not determine a potentially anisotropic maximum-**volume** ellipsoid, its two eigenspaces, or the positive facet-contact design. Another exact John-ellipsoid theorem for square fixed-cardinality partial-assignment polytopes uses analogous permutation-invariant optimization but applies to a different collection of vertices and row/column capacity facets; neither claim implies the present tree-polytope transition. Available mathematical-record and primary-paper comparisons did not locate the present all-order John theorem. Failed searches are not a uniqueness or priority proof.

## Limitations
This is an exact claim only for complete graphs with unweighted Euclidean edge-coordinate metric, not arbitrary graphic matroids or edge-weighted incidence realizations. The centered largest Euclidean ball is not identical to a volume-maximizing ellipsoid in the anisotropic cases. The general finite computation does not constitute an infinite proof, and no independent audit or literature-priority certification has been performed. Equivalent historical results under optimal-design, graphic matroid, or ellipsoid terminology remain a bibliographic risk.

## References
1. Brahim Chaourar, *The facets of the spanning trees polytope*, arXiv:1903.07292, first public version 2019-03-18, https://arxiv.org/abs/1903.07292.
2. Guillermo Pineda-Villavicencio and Benjamin Schröter, *Reconstructibility of matroid polytopes*, arXiv:2010.10227, first public version 2020-10-20, https://arxiv.org/abs/2010.10227.
3. Gergely Ivanov and Márton Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions*, arXiv:2212.11781 (2022), https://arxiv.org/abs/2212.11781.
4. Vladimir Gartsman and Nathan Linial, *On the Löwner-John Ellipsoids of the Metric Polytope*, arXiv:2305.02113 (2023), https://arxiv.org/abs/2305.02113.
