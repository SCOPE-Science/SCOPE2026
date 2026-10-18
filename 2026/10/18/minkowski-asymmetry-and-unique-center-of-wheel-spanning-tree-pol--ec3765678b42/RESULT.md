# Minkowski asymmetry and unique center of wheel spanning-tree polytopes

## Finding

For every integer \(n\ge4\), let \(W_n=K_1\vee C_n\) be the simple wheel with one hub, \(n\) rim vertices, \(n\) spokes, and \(n\) rim edges. The spanning-tree (graphic-matroid base) polytope is
\[
P_n=\operatorname{conv}\{\mathbf1_T:T\subseteq E(W_n)\text{ is a spanning tree}\}\subset\mathbb R^{2n}.
\]
The exact Minkowski asymmetry, measured within the affine hull of \(P_n\), is
\[
\boxed{s(P_n)=\frac{2n}{n-1}}.
\]
The **unique** minimizing Minkowski center \(c_n\) has constant coordinates on the two natural edge orbits:
\[
\boxed{c_n(p_i)=\frac{n+1}{3n-1},\qquad c_n(r_i)=\frac{2(n-1)}{3n-1}\quad (i\in\mathbb Z/n\mathbb Z).}
\]
Here \(p_i\) joins the hub to rim vertex \(i\) and \(r_i\) joins vertices \(i\) and \(i+1\). This is an infinite-family classification, not an extrapolation from sampled wheels. In particular \(s(P_n)\) decreases strictly toward \(2\).

## Assumptions and scope

The wheel is the **simple** join \(K_1\vee C_n\) with \(n\ge4\). The excluded case \(n=3\) is the complete graph on four vertices, a different natural family. The definition of Minkowski asymmetry is
\[
s(K)=\inf_{c\in\operatorname{aff}K}\{s\ge1:\;-(K-c)\subseteq s(K-c)\}.
\]
The polytope is bounded and has relative interior in the affine hyperplane \(\sum_{e\in E}x_e=n\), since the connected graphic matroid of the wheel has rank \(n\) on \(2n\) edges. Its relative dimension is \(2n-1\).

For every edge subset \(A\), write \(x(A)=\sum_{e\in A}x_e\). Set \(\lambda=s+1\). Reflected containment is equivalent to \(\lambda c-v\in sP_n\) for every spanning-tree incidence vector \(v\).

## Proof

**1. Two support families force the lower bound.** Let \(R=\{r_i\}_{i=0}^{n-1}\). Its spanning-tree support range is \([0,n-1]\): the spoke star attains the minimum, and a rim path plus one spoke attains the maximum. For any admissible center \(c\), reflected containment applied to \(x(R)\) gives
\[
\lambda c(R)\le s(n-1).\tag{1}
\]
For each \(i\), let \(A_i=\{p_i,p_{i+1},r_i\}\), the hub triangle's three edges. Its support range over spanning trees is \([0,2]\). The minimum follows because deleting these three edges leaves a connected spanning subgraph when \(n\ge4\); the maximum is the rank of the triangle. Therefore
\[
\lambda c(A_i)\le2s=2\lambda-2.\tag{2}
\]
Summing (2) over all \(i\) counts each spoke twice and each rim edge once. Since \(c(E)=n\), the left side equals \(\lambda(2n-c(R))\). Hence \(\lambda c(R)\ge2n\). Combined with (1), this yields \(2n\le s(n-1)\), so \(s\ge2n/(n-1)\).

**2. Explicit global attainment by a spanning-tree certificate.** Set
\[
s_* =\frac{2n}{n-1},\qquad
\lambda_*=\frac{3n-1}{n-1},\qquad
c_*(p_i)=\frac{n+1}{3n-1},\qquad
c_*(r_i)=\frac{2(n-1)}{3n-1}.
\]
The coordinates are positive and \(c_*(E)=n\). Put \(z=\lambda_*c_*\), so \(z(p_i)=(n+1)/(n-1)\) and \(z(r_i)=2\). For each spanning tree \(T\), define \(y_T=(z-\mathbf1_T)/s_*\). Its coordinates are nonnegative because \(z(p_i)>1\) and \(z(r_i)>1\), and \(y_T(E)=n\).

The standard spanning-tree polytope criterion states that \(y\in P_n\) if and only if \(y\ge0\), \(y(E)=n\), and \(y(E(S))\le|S|-1\) for every nonempty proper vertex subset \(S\), where \(E(S)\) denotes the edges with both endpoints in \(S\).

If \(S\) contains no hub and \(k=|S|<n\), it induces at most \(k-1\) rim edges; their total \(z\)-weight is at most \(2(k-1)\le s_*(k-1)\). When \(S\) contains all \(n\) rim vertices but not the hub, its induced \(z\)-weight is \(2n=s_*(n-1)\). In either case, subtracting \(\mathbf1_T(E(S))\ge0\) establishes the desired inequality for \(y_T\).

If \(S\) contains the hub and \(k\) rim vertices, then \(0\le k<n\), because \(S\) is proper. The case \(k=0\) is immediate. For \(k>0\), the selected rim vertices split into \(q\ge1\) maximal cyclic runs of lengths \(\ell_1,\ldots,\ell_q\). The induced edge set has exactly \(k\) spokes and \(k-q\) rim edges. When all these induced edges are removed from \(W_n\), the \(L=\sum_{j=1}^q\max(\ell_j-2,0)\) interior vertices of the runs become isolated, while all other vertices remain in one connected component. Every spanning tree consequently uses at least \(L\) induced edges. Thus
\[
\begin{aligned}
z(E(S)) - \mathbf1_T(E(S))
&\le \frac{n+1}{n-1}k+2(k-q)-L\\
&=\lambda_*k-(2q+L)\\
&\le (\lambda_*-1)k=s_*k,
\end{aligned}
\]
because \(\ell_j\le2+\max(\ell_j-2,0)\), and therefore \(k\le2q+L\). This proves every required spanning-tree inequality. Consequently \(y_T\in P_n\) for every \(T\). The identity \(\lambda_*c_*-\mathbf1_T=s_*y_T\) verifies reflected containment at \(s_*\), proving the claimed asymmetry.

**3. Equality forces a unique center.** Suppose \(c\) attains \(s_*\). At the lower-bound equality, (1) and the sum of (2) are both tight: \(\lambda_*c(R)=2n\). Because every inequality (2) has the correct orientation and their sum is tight, each is individually tight, yielding
\[
\lambda_*[c(p_i)+c(p_{i+1})+c(r_i)]=2\lambda_*-2.\tag{3}
\]
Consider \(B_i=\{p_i,p_{i+1},p_{i+2},r_i,r_{i+1}\}\), the edges induced by the hub and three consecutive rim vertices. Its support range is \([1,3]\). Its maximum is the number of vertices minus one; for the minimum, deleting \(B_i\) isolates the middle rim vertex and leaves all other vertices connected, so exactly one edge of \(B_i\) is necessary and sufficient to complete a spanning tree. Thus reflected containment gives
\[
\lambda_*c(B_i)\le3s_*+1=3\lambda_*-2.\tag{4}
\]
On summing (4), each spoke occurs three times and each rim edge twice. Therefore its total left-hand side is \(\lambda_*(3n-c(R))=3n\lambda_*-2n\), which equals the sum of the right-hand sides \(n(3\lambda_*-2)\). Every (4) is tight. Subtract (3) from tight (4) at the same index to obtain \(c(p_{i+2})+c(r_{i+1})=1\), for each \(i\). It follows that \(c(r_i)=1-c(p_{i+1})\). Substitution into (3) gives \(c(p_i)=1-2/\lambda_*=(n+1)/(3n-1)\) for all \(i\); hence \(c(r_i)=2/\lambda_*=2(n-1)/(3n-1)\). Thus \(c=c_*\), proving uniqueness without assuming symmetry of a minimizer.

## Verification

Run the accompanying standard-library program `wheel_asymmetry_verify.py` with `python3 wheel_asymmetry_verify.py`. It exhaustively enumerates the spanning trees for \(4\le n\le8\), checks the reflected candidate \(y_T\) against every induced-vertex-set inequality in exact integer arithmetic, checks the support extrema used in the lower bound and uniqueness argument, and checks the center normalization.

The completed execution verified \(3{,}532\) distinct spanning trees and \(1{,}390{,}868\) induced-set inequalities: respectively \(45,121,320,841,2205\) trees at rim sizes \(4,5,6,7,8\). Finite computation corroborates but does not replace the analytic all-\(n\) proof.

## Relationship to prior work

Backman and Liu [1] study general matroid base polytopes and prove existence of regular unimodular triangulations; their principal theorems concern triangulation and integer lattice geometry, not reflection asymmetry or minimizing centers. Chaourar [2] derives facets of spanning-tree polytopes by graphic/matroid connectivity; these descriptions support the context of the present vertex-set inequalities but do not give the wheel-specific exact asymmetry or center rigidity. The classical spanning-tree description due to Edmonds [3] is used as an established membership characterization, rather than treated as new.

Distinct previously published calculations for other graph classes do not imply the result merely by substituting the number of vertices; the wheel has two edge orbits and mixed triangle/cycle constraints. The wheel statement is not claimed to be a general theorem for all graphic matroids.

## Limitations

Only simple wheels with at least four rim vertices are classified. No closed formula for arbitrary planar or graphic matroid base polytopes is proved. The mathematical proof is self-contained modulo the standard spanning-tree polytope membership theorem. Priority assessment remains non-exhaustive: an earlier equivalent theorem using matroid-duality or symmetry terminology could exist. No independent validation or external mathematical audit has been performed.

## References

1. Spencer Backman and Gaku Liu, *A Regular Unimodular Triangulation of the Matroid Base Polytope*, arXiv:2309.10229 (first posted 19 September 2023), https://arxiv.org/abs/2309.10229.
2. Brahim Chaourar, *The facets of the spanning trees polytope*, arXiv:1903.07292 (first posted 18 March 2019), https://arxiv.org/abs/1903.07292.
3. J. Edmonds, *Matroids and the greedy algorithm*, Mathematical Programming 1 (1971), 127–136; standard spanning-tree polytope rank/vertex-set characterization.
