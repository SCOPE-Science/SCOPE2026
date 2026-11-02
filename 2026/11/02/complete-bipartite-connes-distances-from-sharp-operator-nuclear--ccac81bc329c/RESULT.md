# Complete-bipartite Connes distances from sharp operator–nuclear duality

## Finding
For an unweighted complete bipartite graph \(G=K_{p,q}\), where the integers \(p,q\ge 2\), equip the complex Hilbert space \(\ell_2(V(G))\) with the self-adjoint adjacency matrix \(D\). For distinct vertices, the Connes distance of the diagonal algebra is
\[
d_D(x,y)=\sup\{\lvert f(x)-f(y)\rvert:\ f:V(G)\to\mathbb R,\ \lVert[D,\operatorname{diag}f]\rVert_{2\to2}\le1\}.
\]
It is determined exactly by the two part sizes:
\[
d_D(x,y)=\begin{cases}
\sqrt{2/q},&x,y\text{ belong to the part of size }p,\\
\sqrt{2/p},&x,y\text{ belong to the part of size }q,\\
\dfrac{\sqrt{p-1}+\sqrt{q-1}}{\sqrt{pq}},&x,y\text{ belong to different parts}.
\end{cases}
\]
Always \(d_D(x,x)=0\). All three formulas have attaining real diagonal functions. They include previously accessible very-small-graph cases; the proposed extension is a uniform exact classification for arbitrary \(p,q\ge2\), especially \(p+q\ge5\).

## Assumptions and scope
All edges have weight one, with no loops. The operator norm is induced by the Euclidean Hilbert norms and **not** the graph shortest-path Lipschitz seminorm. Functions are real because self-adjoint diagonal elements suffice in Connes' spectral distance; no constraint other than the commutator norm is imposed. The matrices are finite dimensional. Permutations within either part preserve \(D\), reducing each of the three pair types to the first suitable vertices.

## Proof
**Block reduction.** Write a real vertex function as \(a\in\mathbb R^p\) on one part and \(b\in\mathbb R^q\) on the other, and let \({\bf1}_r\) be the all-ones vector of length \(r\). In the bipartite vertex order the commutator is skew-adjoint with off-diagonal block, up to sign,
\[
M=a{\bf1}_q^{T}-{\bf1}_p b^T.
\]
Consequently \(\|[D,\operatorname{diag}f]\|=\|M\|_{2\to2}\). Constants in \(a,b\) together do not affect the difference or this norm.

**Pairs in one part.** For two distinct vertices \(i,k\) in the first part,
\[
(e_i-e_k)^T M=(a_i-a_k){\bf1}_q^T,
\]
so by the Euclidean operator norm,
\[
|a_i-a_k|\sqrt q=\|(e_i-e_k)^T M\|_2\le\sqrt2\,\|M\|
\]
which yields \(|a_i-a_k|\le\sqrt{2/q}\,\|M\|\). The bound is attained by \(a=(e_i-e_k)/\sqrt{2q}\), \(b=0\), for which \(M=a{\bf1}_q^T\) has norm one. Interchanging the parts proves the second formula.

**A cross-part pair: lower witness.** By permutation invariance take the first vertex in each part. Set
\[
u_0={\bf1}_p/\sqrt p,\qquad u_1=(e_1-\mathbf1_p/p)/\sqrt{1-1/p},
\]
\[
v_0={\bf1}_q/\sqrt q,\qquad v_1=(e_1-\mathbf1_q/q)/\sqrt{1-1/q},
\]
and \(\alpha=\sqrt{p-1}\), \(\beta=\sqrt{q-1}\). Both pairs \((u_0,u_1)\), \((v_0,v_1)\) are orthonormal, with \(e_1=(u_0+\alpha u_1)/\sqrt p\) and \(e_1=(v_0+\beta v_1)/\sqrt q\) in their respective spaces. Choose \(a=u_1/\sqrt q\), \(b=-v_1/\sqrt p\). Then
\[
M=u_1v_0^T+u_0v_1^T,
\]
a rank-two partial isometry with \(\|M\|=1\), and
\[
a_1-b_1=\frac{\alpha+\beta}{\sqrt{pq}}.
\]
This supplies the asserted lower bound.

**A cross-part pair: sharp nuclear dual.** Define the real matrix
\[
Y=\frac{u_0v_0^T+\beta u_0v_1^T+\alpha u_1v_0^T+u_1v_1^T}{\sqrt{pq}}.
\]
Directly, \(Y{\bf1}_q=e_1\) and \(Y^T{\bf1}_p=e_1\). For every matrix \(M=a{\bf1}_q^T-{\bf1}_pb^T\), its Frobenius pairing therefore satisfies
\[
\langle Y,M\rangle_F=a_1-b_1.
\]
The only nonzero singular values of \(Y\) are those of the two-by-two matrix
\[
\frac1{\sqrt{pq}}\begin{pmatrix}1&\beta\\\alpha&1\end{pmatrix}.
\]
For any real two-by-two matrix, the square of its nuclear norm is its squared Frobenius norm plus twice the absolute determinant. Since \(\alpha\beta\ge1\), this gives
\[
\|Y\|_*^2=\frac{2+\alpha^2+\beta^2+2(\alpha\beta-1)}{pq}
=\frac{(\alpha+\beta)^2}{pq}.
\]
Schatten operator/nuclear Hölder duality yields
\[
|a_1-b_1|=|\langle Y,M\rangle_F|\le\|Y\|_*\|M\|=\frac{\sqrt{p-1}+\sqrt{q-1}}{\sqrt{pq}}\|M\|.
\]
This coincides with the exhibited norm-one lower witness and completes all cases.

## Verification
The accompanying standalone `verify.py` uses Python 3 and NumPy. Executing `python3 verify.py` checks the norm-one primal extremizers, dual marginal constraints, nuclear norm and equality pairing for every integer pair \(2\le p,q\le15\), together with randomized inequalities. These tests are diagnostic; the preceding proof is exact for all integers \(p,q\ge2\) and uses no computational extrapolation.

## Relationship to prior work
Clare, Li, Poon and Swartz [1], publicly available September 6, 2024, treat the graph adjacency-Dirac metric using Birkhoff–James orthogonality, with complete characterization for **paths**; their definitions and the path analysis provide the closest motivating framework but not the present arbitrary-size biclique formula. Besnard [2] gives graph-distance comparisons, pruning principles and general bounds without the sharp three pair-type biclique classification. Iochum, Krajewski and Martinetti [3] establish the original finite-space framework and small-order calculations; their results overlap a finite corner, not the uniform general-size classification. In contrast to the ordinary shortest-path metric or the norm of a Lipschitz-free transportation space, the norm in this theorem is that of an adjacency-matrix **commutator**. The proof is a direct operator-nuclear dual norm computation on an additive matrix subspace.

## Limitations
Only unweighted, complete bipartite adjacency-Dirac spectral triples are treated. The formulas are not asserted for weighted edges, arbitrary bipartite graphs, other graph Dirac constructions, or general states beyond vertex evaluations. Prior full-text comparisons and targeted mathematical searches did not find this uniform formula, but search absence does not establish uniqueness; an equivalent derivation may occur in differently indexed graph, spectral-triple or matrix-norm literature. No independent scientific assessment has been carried out.

## References
[1] P. Clare, C.-K. Li, E. Poon and E. Swartz, *Noncommutative distances on graphs: An explicit approach via Birkhoff-James orthogonality*, arXiv:2409.04146v1 (September 6, 2024), https://arxiv.org/abs/2409.04146.

[2] F. Besnard, *Estimating noncommutative distances on graphs*, arXiv:2105.09056v1 (May 19, 2021), https://arxiv.org/abs/2105.09056.

[3] B. Iochum, T. Krajewski and P. Martinetti, *Distances in Finite Spaces from Noncommutative Geometry*, arXiv:hep-th/9912217v1 (December 22, 1999), https://arxiv.org/abs/hep-th/9912217.
