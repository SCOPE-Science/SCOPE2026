# Sharp cycle and cut projection norms for triangular Johnson graphs

## Finding

For each integer \(n\ge5\), let \(G_n=J(n,2)=L(K_n)\) be the graph whose vertices are the two-element subsets of \(\{1,\ldots,n\}\), two vertices being adjacent when they intersect in one element. Choose any orientation of its edges, and let \(D:\mathbb R^{E(G_n)}\to\mathbb R^{V(G_n)}\) be the signed incidence map. Put \(B_n=\operatorname{ran}D^{\mathsf T}\) (the real cut/gradient space) and \(Z_n=\ker D\) (the real cycle/flow space). For a subspace \(Y\) of the edge space, define the **relative projection constant**
\[
\lambda_p(Y)=\inf\{\|P\|_{\ell_p(E(G_n))\to\ell_p(E(G_n))}:P^2=P,\ \operatorname{ran}P=Y\}.
\]
Then
\[
\boxed{\lambda_1(B_n)=\lambda_\infty(B_n)=\frac{(n-2)(3n-1)}{n(n-1)}}
\qquad\text{and}\qquad
\boxed{\lambda_1(Z_n)=\lambda_\infty(Z_n)=\frac{2(2n-5)}{n-1}}.
\]
For every \(1\le p\le\infty\), the Euclidean orthogonal projections onto \(B_n\) and \(Z_n\) **separately minimize** the \(\ell_p\)-operator norm among all linear projections onto their ranges. They are the respective unique \(S_n\)-equivariant projections (uniqueness among arbitrary minimizers is not asserted). Both endpoint constants increase strictly with \(n\), tending respectively to \(3\) and \(4\). In the first genuinely new case, \(n=5\), they are \(21/10\) and \(5/2\).

## Assumptions and scope

All vector spaces, operators, and projection constants here are **real**. Each graph is finite, simple, connected, and unweighted; the ambient \(\ell_p\) norm gives every oriented graph edge weight one. Edge orientation changes the embedding only by a signed coordinate isometry, and hence cannot affect the constants. There are \(\binom n2\) graph vertices and \(\frac{n(n-1)(n-2)}2\) edges; \(\dim B_n=\binom n2-1\) and \(\dim Z_n=\frac{n(n-1)(n-2)}2-\binom n2+1\). The theorem is asserted for every integer \(n\ge5\); the \(n=4\) boundary is already represented by the complete tripartite graph \(K_{2,2,2}\) and is not claimed as new.

## Proof

**1. Laplacian and orthogonal cut projector.** Write \(N=\binom n2\). Let \(U\) be the unsigned \(N\times n\) point-pair incidence matrix, with \(U_{X,i}=1\) when \(i\in X\). Put \(T=UU^{\mathsf T}\). Its entries are \(T_{X,Y}=|X\cap Y|\), and direct counting gives
\[
U^{\mathsf T}U=(n-2)I_n+\mathbf1_n\mathbf1_n^{\mathsf T},\qquad L:=DD^{\mathsf T}=2(n-1)I_N-T.
\]
The constant vectors form \(\ker L\). On \(U(\mathbf1_n^\perp)\), the eigenvalues of \(T\) and \(L\) are \(n-2\) and \(n\). On \(\ker U^{\mathsf T}\), they are \(0\) and \(2(n-1)\). These two invariant subspaces span \(\mathbf1_N^\perp\), since \(U\) has full column rank for \(n\ge3\). Consequently the Moore--Penrose inverse of \(L\), when applied to any mean-zero vector, is
\[
L^+x=\frac{x}{2(n-1)}+\frac{Tx}{2n(n-1)}.
\]
In particular, the Euclidean orthogonal cut projection and its cycle complement are
\[
Q=D^{\mathsf T}L^+D
 =D^{\mathsf T}\left(\frac{I_N}{2(n-1)}+\frac{T}{2n(n-1)}\right)D,
\qquad P=I-Q.
\]

**2. Uniqueness of invariant projections and global minimality.** The permutations of \(\{1,\ldots,n\}\) act transitively on oriented edges by signed coordinate permutations; the action is isometric on every real \(\ell_p(E(G_n))\). Let \(A:\ell_2^{E(G_n)}\to B_n\) be **any equivariant linear map** (not necessarily a projection). Fix the oriented edge \(e\) with incidence column \(De=\delta_{\{1,2\}}-\delta_{\{1,3\}}\), and represent \(Ae=D^{\mathsf T}g_e\) using the unique potential \(g_e\) with mean zero. Invariance under permutations of \(4,\ldots,n\) and antisymmetry under the transposition \((2\ 3)\), which reverses \(e\), force
\[
g_e=a(\delta_{\{1,2\}}-\delta_{\{1,3\}})
  +b\sum_{j=4}^n(\delta_{\{2,j\}}-\delta_{\{3,j\}}).
\]
Since \(TDe=\delta_{\{1,2\}}-\delta_{\{1,3\}}+
\sum_{j=4}^n(\delta_{\{2,j\}}-\delta_{\{3,j\}})\), this is equivalently \(g_e=((a-b)I_N+bT)De\). Transitivity over all oriented edges then yields
\[
A=D^{\mathsf T}((a-b)I_N+bT)D.
\]
The matrix \(A\) is therefore symmetric, **without assuming that it is a projection**. In particular, every equivariant projection onto \(B_n\) is symmetric and so equals the Euclidean orthogonal projector \(Q\). For the cycle-space assertion, let \(R\) be an equivariant projection onto \(Z_n\) and set \(S=(R-P)^{\mathsf T}\). Since \(R-P\) maps into \(Z_n\) and vanishes on \(Z_n\), the equivariant operator \(S\) has range in \(B_n=Z_n^\perp\) and vanishes on \(B_n\). By the preceding classification, \(S\) is symmetric; a symmetric operator with range in \(B_n\) that vanishes on \(B_n\) is zero. Thus \(R=P\), proving uniqueness of the equivariant cycle projection as well.

Given any projection onto either space, averaging its conjugates over the finite group \(S_n\) produces another projection with the same range and operator norm no larger in **every** \(\ell_p\). The unique equivariant projections are \(Q\) and \(P\); therefore they are globally norm-minimizing for all \(1\le p\le\infty\). This establishes minimality, not just the norm of a preferred projector.

**3. Exact endpoint column sums.** Choose \(e\) as in Step 2 and put
\[
\alpha=\frac{n+1}{2n(n-1)},\qquad \beta=\frac1{2n(n-1)}.
\]
The potential \(g=L^+De\) takes value \(+\alpha\) at \(\{1,2\}\), \(-\alpha\) at \(\{1,3\}\), \(+\beta\) at every \(\{2,j\}\) with \(j\ge4\), \(-\beta\) at every \(\{3,j\}\) with \(j\ge4\), and zero elsewhere. Each entry of \(Qe=D^{\mathsf T}g\) is a difference of two adjacent potential values. The nonzero absolute differences fall into five exhaustive classes:

- the edge between the \(+\alpha\) and \(-\alpha\) sites: one edge of difference \(2\alpha\);
- edges from either \(\alpha\)-site to a zero site: \(2(n-2)\) edges of difference \(\alpha\);
- edges from an \(\alpha\)-site to a same-sign \(\beta\)-site: \(2(n-3)\) edges of difference \(\alpha-\beta\);
- edges between paired \(+\beta\) and \(-\beta\) sites: \(n-3\) edges of difference \(2\beta\);
- edges from a \(\beta\)-site to a zero site: \(2(n-3)(n-2)\) edges of difference \(\beta\).

All remaining adjacent pairs have equal potential. Hence every edge column of \(Q\) has absolute sum
\[
\begin{aligned}
\|Qe\|_1
 &=2(n-1)\alpha+2(n-3)(\alpha-\beta)+2(n-3)(n-1)\beta\\
 &=\frac{(n-2)(3n-1)}{n(n-1)}.
\end{aligned}
\]
The diagonal coefficient is \(Q_{e,e}=2\alpha=(n+1)/(n(n-1))\in(0,1)\). Therefore the column sum of \(P=I-Q\) is
\[
\|Pe\|_1=(1-2\alpha)+(\|Qe\|_1-2\alpha)
 =\frac{2(2n-5)}{n-1}.
\]
The group is edge-transitive, so these are the induced \(\ell_1\) operator norms. Both \(Q\) and \(P\) are symmetric matrices, whence their induced \(\ell_\infty\) norms equal their \(\ell_1\) norms. Global minimality follows from Step 2. Finally, rewriting the constants as \(3-(4n-2)/(n(n-1))\) and \(4-6/(n-1)\) proves strict monotonicity and the limits.

## Verification

Run `python verify.py` using Python 3 and its standard library. It constructs each graph for \(4\le n\le8\), checks every edge column with exact rational arithmetic, and independently checks the projection identity on all graph gradients. For \(4\le n\le7\) it also constructs the *grounded graph Laplacian*, inverts it by rational Gauss--Jordan elimination, and compares every entry of its transfer-current projection with the formula above. On the packaged source this gives **24,980 passing assertions**. Independent unrestricted linear-programming calculations (finite-dimensional numerical optimization) additionally agreed for \(n=4,5,6\). These finite computations are cross-checks; the proof for all \(n\ge5\) is analytic in the preceding section.

## Relationship to prior work

Dilworth, Kutzarova, and Ostrovskii [1] formulate invariant cycle projections and the representation-theoretic criterion for their uniqueness, and analyze discrete tori and Hamming graphs. Their relevant sections do not calculate cycle or cut projection constants for \(J(n,2)\); neither their general uniqueness criterion nor their Hamming formulas immediately supplies the explicit values here. Their earlier work [2] concerns diamond and Laakso graphs. The Johnson graph is the triangular graph \(L(K_n)\), as described in [3], and should not be confused with the Hamming graph \(L(K_{q,q})\).

The special boundary \(J(4,2)\cong K_{2,2,2}\) is covered by existing balanced complete multipartite results and is deliberately excluded from the new range; similarly \(J(3,2)\cong K_3\) is covered by complete-graph results. For \(n\ge5\), disjointness of two-subsets is not an equivalence relation, so these graphs are not complete multipartite graphs. The core additional content is the independent invariant-projection rigidity argument on the triangular graph family and the exact transfer-current column census.

## Limitations

No formula for the optimal operator norm at intermediate exponents \(p\notin\{1,2,\infty\}\) is claimed, although the minimizing projector is identified. No uniqueness is claimed among all norm-minimizing projections. No statement is made for weighted graphs, complex edge spaces, or higher-rank Johnson graphs \(J(n,k)\) with \(k\ge3\). The calculations are reproducibility checks, not exhaustive searches over graph sizes. Literature comparisons cannot rule out an equivalent result under a different name or in unindexed sources; an independently performed scientific audit is not available.

## References

[1] Stephen J. Dilworth, Denka Kutzarova, Mikhail I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (first public preprint 2023-05-21), https://arxiv.org/abs/2305.12582 . In particular Sections 1.5, 2.1, 2.6, 2.7 and Theorems 5, 43, 45.

[2] Stephen J. Dilworth, Denka Kutzarova, Mikhail I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, arXiv:2007.07949 (first public preprint 2020-07-15), https://arxiv.org/abs/2007.07949 .

[3] *Triangular Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/TriangularGraph.html (notation \(T_n=L(K_n)=J(n,2)\)).
