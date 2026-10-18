# Sharp cut and cycle complementability after deleting a perfect matching

## Finding

For each integer \(n\ge 3\), let \(G_n\) be the *crown graph*: the unit-edge complete bipartite graph on \(U=\{u_1,\ldots,u_n\}\) and \(V=\{v_1,\ldots,v_n\}\), with all \(n\) matching edges \(u_iv_i\) deleted. Orient its \(n(n-1)\) edges from \(U\) to \(V\). Let \(D:\mathbb R^{E(G_n)}\to\mathbb R^{2n}\) be the incidence matrix, let \(B_n=\operatorname{ran}D^{\mathsf T}\) be the real cut subspace, and let \(Z_n=\ker D\) be the real cycle-flow subspace. For a subspace \(Y\) of the edge space, define its relative projection constant
\[
\lambda_p(Y)=\inf\{\|T\|_{\ell_p(E)\to\ell_p(E)}:T^2=T,\ \operatorname{ran}T=Y\}.
\]
Then for **every** \(1\le p\le\infty\), the Euclidean orthogonal projections \(P_n\) onto \(B_n\) and \(Q_n=I-P_n\) onto \(Z_n\) individually attain their respective relative projection constants. Each is the unique projection onto its range commuting with simultaneous permutations of the paired indices. At the endpoint exponents the exact values are
\[
\boxed{\lambda_1(B_n)=\lambda_\infty(B_n)=3-\frac4n},\qquad
\boxed{\lambda_1(Z_n)=\lambda_\infty(Z_n)=\frac{2(2n^2-6n+3)}{n(n-1)}}.
\]
At \(p=2\) both constants equal one. Exact numerical norms for the other intermediate exponents are not asserted.

The first new family members are \(n\ge5\): the graphs at \(n=3\) and \(n=4\) are respectively the six-cycle and the three-dimensional cube, and their endpoint cases are consistency boundaries rather than novelty claims. For the crown family,
\[
\lambda_1(Z_n)-\lambda_1(B_n)=\frac{n^2-5n+2}{n(n-1)},
\]
so the cycle projection is the more expensive of the two precisely when \(n\ge5\). In contrast, the corresponding changeover in the undeleted \(K_{n,n}\) occurs already at \(n=4\). More precisely, deleting the perfect matching strictly lowers the best cut and cycle projection norms by the respective exact amounts
\[
\boxed{\frac2{n^2}\quad\text{and}\quad\frac{2(3n-2)}{n^2(n-1)}},
\]
for every \(n\ge3\). This supplies a sharp, dimension-dependent complementability response to a natural dense-graph edge deletion.

## Assumptions and scope

All vector spaces, projections, and operator norms are over the real scalars. The graph is simple, unweighted, and connected for \(n\ge3\). The edge spaces use the stated coordinate \(\ell_p\) norms, not a quotient norm. An alternative orientation changes coordinates by signs and does not change any stated operator norm. The claimed uniqueness applies to symmetry-equivariant projections; uniqueness among all unrestricted norm-minimizing projections is not asserted.

## Proof

**1. Equivariant projections are necessarily orthogonal.** Identify the oriented edge space with the arrays \(a_{ij}\), \(i\ne j\), and let the symmetric group \(S_n\) permute both indices simultaneously. Its action is an isometry on every coordinate \(\ell_p\). The cut space comprises the additive arrays \(a_{ij}=x_i+y_j\), and has the invariant decomposition into the constant arrays and the two copies of the centered standard representation \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\), represented by \(x_i\) and \(x_j\), respectively.

Here is an elementary uniqueness argument. Let \(F:H\to\mathbb R^{E(G_n)}\) be any \(S_n\)-equivariant linear map. For fixed distinct indices \(i,j\), the linear functional \(x\mapsto F(x)_{ij}\) is invariant under permutations fixing \(i\) and \(j\). Its coefficients at all remaining indices are equal; using \(\sum_k x_k=0\), it therefore has the form \(a x_i+b x_j\), where equivariance makes \(a,b\) independent of \(i,j\). Thus every such \(F\) has its range inside \(B_n\). An invariant vector in the entire edge space must be constant, hence also belongs to \(B_n\). It follows, by applying these observations to each of the three summands of \(B_n\), that every equivariant map \(B_n\to Z_n=B_n^\perp\) is zero. Taking Euclidean adjoints shows that every equivariant map \(Z_n\to B_n\) is zero as well.

Any projection onto \(B_n\) differs from its Euclidean orthogonal projection by a map \(Z_n\to B_n\); any projection onto \(Z_n\) differs from its Euclidean orthogonal projection by a map \(B_n\to Z_n\). Consequently the orthogonal projections are the **unique** \(S_n\)-equivariant projections onto their respective ranges. Averaging an arbitrary projection over \(S_n\) is still a projection onto the same range and cannot increase its norm in any coordinate \(\ell_p\). Therefore the orthogonal projections minimize the operator norm for every \(1\le p\le\infty\).

**2. Exact orthogonal cut projection.** Set \(L=DD^{\mathsf T}\). On a pair of vertex vectors \((x,y)\) its matrix is
\[
L=\begin{pmatrix}(n-1)I&-(J-I)\\-(J-I)&(n-1)I\end{pmatrix},
\]
where \(J\) denotes the all-ones matrix. The symmetric centered subspace \((x,x)\), the antisymmetric centered subspace \((x,-x)\), and the antisymmetric constant line have respective positive eigenvalues \(n\), \(n-2\), and \(2(n-1)\). The remaining constant line is the kernel. Thus \(P_n=D^{\mathsf T}L^+D\), where \(L^+\) is the Moore–Penrose inverse.

For the edge coordinate \(e_{12}\), define
\[
s_k=\frac{\mathbf1_{k=1}-\mathbf1_{k=2}}{2n},\qquad
c_k=\frac{(\mathbf1_{k=1}+\mathbf1_{k=2})/2-1/n}{n-2},\qquad
g=\frac{1}{2n(n-1)}.
\]
Applying the three displayed inverse eigenvalues to the incidence vector of \(e_{12}\) gives the vertex potential \((s+c+g\mathbf1,\ s-c-g\mathbf1)\). Hence the coefficient of \(P_ne_{12}\) on the edge \((k,l)\), where \(k\ne l\), is
\[
(P_ne_{12})_{kl}=s_k-s_l+c_k+c_l+2g.
\]
The resulting complete coefficient partition is

| Edge type | Number | Coefficient |
| --- | ---: | ---: |
| \((1,2)\) | \(1\) | \((2n-1)/(n(n-1))\) |
| \((2,1)\) | \(1\) | \(1/(n(n-1))\) |
| \((1,l),\ l\notin\{1,2\}\), or \((k,2),\ k\notin\{1,2\}\) | \(2(n-2)\) | \((n^2-3n+1)/(n(n-1)(n-2))\) |
| \((2,l),\ l\notin\{1,2\}\), or \((k,1),\ k\notin\{1,2\}\) | \(2(n-2)\) | \(-1/(n(n-1)(n-2))\) |
| \((k,l),\ k,l\notin\{1,2\},\ k\ne l\) | \((n-2)(n-3)\) | \(-1/((n-1)(n-2))\) |

For every integer \(n\ge3\), \(n^2-3n+1>0\). Summing the absolute values of this partition yields exactly \(3-4/n\). Because the paired-index action is transitive on all edges, this equals the \(\ell_1\)-operator norm of \(P_n\), not just one column norm.

**3. Exact cycle norm and endpoint duality.** The entry \((P_ne_{12})_{12}=(2n-1)/(n(n-1))\) is strictly between zero and one. Every other coefficient of \(Q_ne_{12}=e_{12}-P_ne_{12}\) is the negative of its corresponding cut coefficient. Therefore
\[
\|Q_ne_{12}\|_1=1+\|P_ne_{12}\|_1-2(P_ne_{12})_{12}
=\frac{2(2n^2-6n+3)}{n(n-1)}.
\]
Transitivity again makes this the full operator norm. Both projectors are symmetric real matrices, so \(\|P_n\|_{\infty\to\infty}=\|P_n\|_{1\to1}\), and the same holds for \(Q_n\). The minimization in Step 1 proves all four endpoint projection-constant equalities.

**4. Comparison with the intact complete bipartite graph.** For \(K_{n,n}\), the orthogonal cut projection of a matrix subtracts its grand average from the sum of its row and column averages. Its endpoint cut norm is \(3-4/n+2/n^2\); the complementary cycle norm is \(4(n-1)^2/n^2\). Symmetry over separate row and column permutations proves that these are also the minimum projection norms. Subtracting the crown values gives the two strictly positive deletion gaps in the finding. The crown difference has numerator \(n^2-5n+2\), which is negative at \(n=3,4\) and positive at all integers \(n\ge5\). The intact difference has numerator \(n^2-4n+2\), negative at \(n=3\) and positive at all integers \(n\ge4\). This proves the sharp one-step shift of the dominant-projection threshold.

## Verification

The accompanying `crown_verify.py` program uses exact rational arithmetic to check the complete formula in dimensions \(n=3,\ldots,9\): every input-edge column has zero residual divergence, the cut projection fixes every row and column cut, it is symmetric, and all its column norms and the deletion/crossover identities equal the stated rational expressions. An independent NumPy program, `crown_pinv_check.py`, constructs the incidence matrix and computes \(D^{\mathsf T}(DD^{\mathsf T})^+D\) directly for \(n=3,\ldots,10\). Its largest observed absolute discrepancy, including projector identities and incidence tests, was below \(9\times10^{-15}\). These finite checks support, but do not replace, the all-dimensional proof above.

## Relationship to prior work

Dilworth, Kutzarova, and Ostrovskii developed the use of graph cycle spaces, incidence quotients and invariant projections in finite Lipschitz-free geometry; their work on invariant projections gives a general uniqueness criterion and analyzes discrete tori and Hamming graphs. The present calculation applies that setting to the matching-deleted complete bipartite family and proves a representation-free uniqueness lemma, explicit endpoint norms, and a sharp deletion-induced switch of which complementary projection is more expensive. The six-cycle and the three-cube are known small cases; neither is presented as the new result. A previously studied balanced complete-multipartite family excludes the bipartite matching deletion, and a previously studied matching-deleted bipartite family classified facets rather than best projection norms. The intact complete bipartite comparison is included only as the boundary baseline.

## Limitations

The formulas describe real coordinate edge spaces and the canonical cut/cycle embedding, not absolute projection constants in every super-space. Exact intermediate-exponent norms are not determined. Unique symmetry-equivariant minimizers do not imply uniqueness among all unrestricted minimizers. Although no exact matching-deleted formula was identified in the inspected mathematical sources, exhaustive bibliographic uniqueness is not claimed.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (first publicly posted 2018-07-10), https://arxiv.org/abs/1807.03814.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first publicly posted 2023-05-21), https://arxiv.org/abs/2305.12582.
