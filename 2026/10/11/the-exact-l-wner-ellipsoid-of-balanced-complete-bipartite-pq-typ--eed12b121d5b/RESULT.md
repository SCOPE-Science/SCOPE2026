# The exact Löwner ellipsoid of balanced complete-bipartite PQ-type adjacency polytopes

## Finding
For each integer \(m\ge2\), put \(n=2m\) and partition \([n]\) into two blocks of size \(m\). For their complete bipartite graph \(G=K_{m,m}\), consider the PQ-type adjacency polytope
\[
P_m=\operatorname{conv}\{(e_i,e_j):i=j\text{ or }\{i,j\}\in E(G)\}\subset\mathbb R^n\oplus\mathbb R^n.
\]
It has intrinsic dimension \(d=2(n-1)\). Its **unique minimum-volume enclosing ellipsoid** is the explicit ellipsoid below. In particular **every one of its \(n+2m^2\) vertices contacts that ellipsoid**, and no additional points of the polytope contact its boundary.

Set \(c_0=\mathbf1/n\), \(s=(\mathbf1_m,-\mathbf1_m)/\sqrt n\), \(H=I-\mathbf1\mathbf1^{\mathsf T}/n\), \(P_s=ss^{\mathsf T}\), and \(P_0=H-P_s\). For \((x,y)\) with coordinate sums one, define
\[
U=\frac{(x-c_0)+(y-c_0)}{\sqrt2},\quad V=\frac{(x-c_0)-(y-c_0)}{\sqrt2},\quad U_s=P_sU,\quad U_0=P_0U,\quad V_s=P_sV,\quad V_0=P_0V.
\]
Put
\[
t=\frac{2}{1+\sqrt{8n-7}},\qquad d=2(n-1).
\]
Then the enclosing ellipsoid, in the intrinsic affine space, is
\[
\boxed{\mathcal E_m=\left\{(x,y):\frac{\|U_s\|^2}{2t}+\frac{\|U_0\|^2}{1+t}+\frac{\|V_s\|^2}{2(1-t)}+\frac{\|V_0\|^2}{1-t}\le \frac dn\right\}.}
\]
The exact intrinsic Euclidean volume is
\[
\boxed{\operatorname{vol}_d(\mathcal E_m)=\kappa_d\left(\frac dn\right)^{d/2}\sqrt{4t(1-t)(1-t^2)^{n-2}},\qquad \kappa_d=\frac{\pi^{d/2}}{\Gamma(d/2+1)}.}
\]

## Assumptions and scope
The Euclidean metric is the one inherited from \(\mathbb R^{2n}\), **not** the lattice-normalized metric and not an arbitrary unimodular image of the body. The bipartition has equal part sizes, \(m\ge2\). The affine hull is given by the two unit coordinate-sum equations. The PQ polytope is defined by the displayed vertices, following Ohsugi--Tsuchiya [1]. Every displayed point is a vertex because it is a zero-one vertex of the ambient product of simplices; full intrinsic dimension follows from positive definiteness of the covariance computed below.

## Proof
Write \(v_{ij}=(e_i,e_j)\) for the displayed points, and \(z_{ij}=v_{ij}-(c_0,c_0)\). Assign contact-measure weights
\[
\mu(v_{ii})=\frac tn\quad(1\le i\le n),\qquad
\mu(v_{ij})=\frac{1-t}{nm}\quad(\{i,j\}\in E(G)).
\]
There are \(n\) diagonal points and \(nm=2m^2\) directed cross-edge points. Thus these positive weights total one. Their mean is \((c_0,c_0)\), because each coordinate index occurs with marginal probability \(t/n+(1-t)m/(nm)=1/n\).

Let \(A\) be the \(n\)-by-\(n\) adjacency matrix of \(K_{m,m}\), and \(J=\mathbf1\mathbf1^{\mathsf T}\). The covariance of the centered points in \((x,y)\) coordinates has diagonal blocks \(H/n\) and off-diagonal blocks
\[
\frac1n\left[tH+(1-t)\left(\frac Am-\frac Jn\right)\right].
\]
The orthogonal decomposition of \(H\) consists of the sign line \(\mathbb Rs\) and its \((n-2)\)-dimensional orthogonal complement. Since \(As=-ms\) and \(A\) vanishes on the latter complement, the covariance is block diagonal in the \(U,V\) coordinates, with operators
\[
C_U=\frac1n\bigl(2tP_s+(1+t)P_0\bigr),\qquad C_V=\frac1n\bigl(2(1-t)P_s+(1-t)P_0\bigr).
\]
All four eigenvalues are positive for \(0<t<1\). Therefore the covariance \(C\) is positive definite on the intrinsic \(d\)-space. The displayed ellipsoid is exactly \(\{z:z^{\mathsf T}C^{-1}z\le d\}\), centered at the mean.

We now verify containment by calculating every vertex's inverse-covariance norm. For \(v_{ii}\), its \(U\)-projection has squared norms \(2/n\) on the sign line and \(2(n-2)/n\) on its complement, while \(V=0\). Consequently
\[
Q_{\rm diag}=\frac1n\left(\frac1t+\frac{2(n-2)}{1+t}\right).
\]
For an oriented edge \(v_{ij}\) joining the opposite bipartition classes, \(U_s=0\), \(\|U_0\|^2=(n-2)/n\), \(\|V_s\|^2=2/n\), and \(\|V_0\|^2=(n-2)/n\). Thus
\[
Q_{\rm edge}=\frac1n\left(\frac{n-2}{1+t}+\frac{n-1}{1-t}\right).
\]
The equality \(Q_{\rm diag}=Q_{\rm edge}\) is equivalent to \(1-t-2(n-1)t^2=0\), whose unique solution in \((0,1)\) is \(t=2/(1+\sqrt{8n-7})\). For this choice, all contact norms coincide. Their weighted mean is
\[
\sum_{ij}\mu(v_{ij})z_{ij}^{\mathsf T}C^{-1}z_{ij}
=\operatorname{tr}(C^{-1}C)=d,
\]
so each norm is exactly \(d\). Hence every generating vertex lies on the proposed ellipsoid, and its convex hull is contained in that ellipsoid. Since a positive-definite quadratic form is strictly convex, a nontrivial convex combination of distinct vertices has strictly smaller quadratic form; there are no additional contacts.

To prove global volume optimality, let a competing containing ellipsoid be \(\{z:(z-a)^{\mathsf T}S^{-1}(z-a)\le1\}\), where \(S\) is any positive-definite shape matrix on the intrinsic \(d\)-space, with no symmetry assumptions. Averaging its vertex inequalities with \(\mu\) gives
\[
\operatorname{tr}(S^{-1}C)+a^{\mathsf T}S^{-1}a\le1.
\]
By arithmetic--geometric mean on the eigenvalues of \(C^{1/2}S^{-1}C^{1/2}\),
\[
\left(\frac{\det C}{\det S}\right)^{1/d}
\le\frac1d\operatorname{tr}(S^{-1}C)\le\frac1d.
\]
Therefore \(\det S\ge d^d\det C\); equality requires \(a=0\) and \(S=dC\), by the equality cases in the inequalities. This proves **uniqueness** even against off-center and nonsymmetric competitors. Taking square roots of the product of the four eigenvalue blocks of \(dC\) yields the volume formula, completing the proof.

## Verification
The accompanying `verification/verify.py` constructs the vertex set and contact weights independently, expands the full covariance matrix exactly, checks the four orthogonal eigenblocks, verifies the two symbolic contact-norm formulas, and reconstructs every contact equality for the parameters \(m=2,3,4,5\). It passed at those four parameters using exact SymPy algebra. The symbolic all-dimensional proof above is the justification for arbitrary \(m\), not that finite check. Run `python verification/verify.py` with Python 3 and SymPy installed.

## Relationship to prior work
Ohsugi and Tsuchiya [1] define PQ-type adjacency polytopes, relate them to bipartite root polytopes, and compute \(h^*\)-polynomials and normalized volumes for join graphs including complete bipartite graphs (especially their Section 4 and Example 4.5). These combinatorial/lattice quantities do not determine a minimum-volume ellipsoid for the **specified Euclidean embedding**, and their formulas contain no such shape or contact design. Rietsch and Williams [2] study root-polytope, flow-polytope and order-polytope correspondences and face structure; their integral equivalences do not preserve Euclidean Löwner ellipsoids. General Löwner optimality and covariance methods are classical; the contribution here is their explicit, sharp specialization to this PQ family, including all contact points and an algebraic parameter.

## Limitations
The theorem concerns balanced complete-bipartite graphs and does not assert a formula for unbalanced graphs or arbitrary joins. Its ellipsoid is metric-dependent and is not invariant under a nonorthogonal lattice change of coordinates. The originality comparison is not an exhaustive theorem-proving search: related optimal-design or graph-root-polytope literature may contain an equivalent statement. Independent mathematical audit has not been performed.

## References
[1] H. Ohsugi and A. Tsuchiya, *PQ-type adjacency polytopes of join graphs*, arXiv:2103.15045v1 (first posted 2021-03-28), Sections 1 and 4. https://arxiv.org/abs/2103.15045

[2] K. Rietsch and L. Williams, *Root polytopes, flow polytopes, and order polytopes*, arXiv:2406.15803v1 (first posted 2024-06-22). https://arxiv.org/abs/2406.15803
