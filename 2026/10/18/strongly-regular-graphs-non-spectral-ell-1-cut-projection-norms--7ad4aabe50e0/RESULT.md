# Strongly regular graphs: non-spectral \(\ell_1\) cut-projection norms

## Finding

For a connected noncomplete strongly regular graph \(G\) with parameters \((v,k,\lambda,\mu)\), the canonical orthogonal cut and cycle projections have endpoint norms determined by a small local *wing-edge count*. This count is not determined by the graph's three eigenvalues or its strongly regular parameters. Concretely, the classical cospectral pair consisting of the \(4\times4\) rook graph and the Shrikhande graph has distinct canonical projection norms:

\[\begin{aligned}
\|Q_R\|_{1\to1}=\|Q_R\|_{\infty\to\infty}&=\tfrac94,&
\|Q_S\|_{1\to1}=\|Q_S\|_{\infty\to\infty}&=\tfrac{19}{8},\\
\|C_R\|_{1\to1}=\|C_R\|_{\infty\to\infty}&=\tfrac{21}{8},&
\|C_S\|_{1\to1}=\|C_S\|_{\infty\to\infty}&=\tfrac{11}{4}.
\end{aligned}\]

Both gaps are exactly \(1/8\). These are norms of **the specified canonical orthogonal projections**, not claims that these operators are norm-minimizing among all projections onto their ranges.

## Assumptions and scope

Let \(G=(V,E)\) be a finite simple, connected, noncomplete strongly regular graph. Every vertex has degree \(k\); adjacent distinct vertices have \(\lambda\) common neighbors, and nonadjacent distinct vertices have \(\mu\) common neighbors. We assume the nontrivial strongly regular case \(2\le k<v-1\) and \(\mu>0\), which is automatic for the usual connected noncomplete strongly regular graphs.

Choose any orientation of the undirected edges. The vertex-edge incidence matrix \(B\) has column \(b_{xy}=\mathbf1_x-\mathbf1_y\) for an edge oriented from \(y\) to \(x\). Put \(L=BB^{\mathsf T}=kI-A\), with \(A\) the adjacency matrix; \(L^+\) is the Moore--Penrose inverse. The matrices \(Q=B^{\mathsf T}L^+B\) and \(C=I-Q\) are the mutually complementary Euclidean orthogonal projections onto \(\operatorname{ran}B^{\mathsf T}\) and \(\ker B\). Regard these same matrices as operators on real \(\ell_1(E)\) and \(\ell_\infty(E)\) with counting-measure norms.

For each edge \(e=xy\), define the exclusive neighbor sets
\[X_e=N(x)\setminus\bigl(N(y)\cup\{y\}\bigr),\qquad
Y_e=N(y)\setminus\bigl(N(x)\cup\{x\}\bigr),\]
with \(w_e=|E(G[X_e])|+|E(G[Y_e])|\). Write
\[h=k-\lambda+\mu-1,\quad D=kh+\mu,\quad
M=2k(h-1)+2(k-2)(k-\lambda)+4.\]
Then \(h\ge2\), \(D>2h>0\), and the universal endpoint laws are
\[\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=\frac{M-2\min_{e\in E}w_e}{D},}\]
\[\boxed{\|C\|_{1\to1}=\|C\|_{\infty\to\infty}=1+\|Q\|_{1\to1}-\frac{4h}{D}.}\]
The minimum runs over *all* graph edges, with no edge-transitivity assumption.

## Proof

**Step 1: an exact zero-sum Laplacian inverse.** The defining strong-regularity identity is
\[A^2=(k-\mu)I+(\lambda-\mu)A+\mu J.\]
For every vector \(d\) with zero coordinate sum, the term \(Jd\) vanishes. Direct multiplication shows
\[(kI-A)\bigl((h+1)I+A\bigr)d=(kh+\mu)d=Dd.\]
Moreover \(((h+1)I+A)d\) has zero coordinate sum. Since \(G\) is connected, the zero-sum solution is unique. Consequently, for any oriented edge \(e=xy\) with \(d=\mathbf1_x-\mathbf1_y\), the vertex potential of its unit-current electrical flow is
\[u=L^+d=\frac{((h+1)I+A)d}{D}.\]
With this orientation, its values are \(h/D\) at \(x\), \(-h/D\) at \(y\), \(1/D\) on \(X_e\), \(-1/D\) on \(Y_e\), and zero elsewhere. The sets \(X_e\) and \(Y_e\) are disjoint and each has exactly \(k-\lambda-1\) vertices. These five potential levels are ordered because \(h\ge2\).

**Step 2: total variation of the electrical flow.** If \(\partial U\) denotes the set of edges with exactly one end in \(U\), the discrete coarea formula for the five levels gives
\[\sum_{f\in E}|(B^{\mathsf T}u)_f|
=\frac{\,|\partial(\{x\}\cup X_e)|+|\partial(\{y\}\cup Y_e)|+2k(h-1)}{D}.\]
Indeed the levels from \(0\) to \(1/D\) contribute the two cuts of the positive and negative supports, and the remaining interval of length \((h-1)/D\) contributes the singleton cuts of \(x\) and \(y\). This formula works also for edges crossing a positive set and a negative set, because the coarea contributions add.

Since \(x\) is adjacent to every vertex of \(X_e\), and \(|\{x\}\cup X_e|=k-\lambda\), degree counting yields
\[|\partial(\{x\}\cup X_e)|=k(k-\lambda)-2(k-\lambda-1)-2|E(G[X_e])|
=(k-2)(k-\lambda)+2-2|E(G[X_e])|.\]
The analogous identity holds for \(y,Y_e\). Therefore the absolute sum of the column of \(Q\) indexed by \(e\) is exactly \((M-2w_e)/D\). The \(\ell_1\) operator norm is the largest absolute column sum; maximizing selects the smallest \(w_e\). Since \(Q\) is symmetric, its \(\ell_\infty\) norm is identical.

**Step 3: the cycle projector.** The diagonal entry of \(Q\) at every edge is the effective resistance across that edge, equal here to
\[Q_{ee}=u(x)-u(y)=\frac{2h}{D}.\]
Because \(D-2h=(k-2)h+\mu>0\), this diagonal is strictly between zero and one. The column of \(C=I-Q\) has diagonal magnitude \(1-2h/D\) and all off-diagonal magnitudes equal to those of the corresponding \(Q\) column. Hence for each \(e\),
\[\sum_f|C_{fe}|=1+\sum_f|Q_{fe}|-\frac{4h}{D}.\]
Taking maxima yields the displayed cycle norm, and symmetry gives the \(\ell_\infty\) identity.

**Step 4: two cospectral graphs, one local difference.** Define the rook graph \(R\) on \(\{0,1,2,3\}^2\), joining two distinct pairs when they agree in exactly one coordinate. Define the Shrikhande graph \(S\) on \(\mathbb Z_4^2\), joining points whose difference lies in
\[\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\pmod4.\]
Direct neighbor counting gives parameters \((v,k,\lambda,\mu)=(16,6,2,2)\) for both. Their adjacency spectra are therefore \(6\) once, \(2\) six times, and \(-2\) nine times; in particular the Laplacian spectra agree. Here \(h=5\), \(D=32\), and \(M=84\).

For an edge \((0,0)(0,1)\) of \(R\), each exclusive-neighbor set consists of the three remaining vertices in a fixed column; each induces a triangle, so \(w_e=3+3=6\). Row/column permutations and coordinate interchange act transitively on edges, giving \(w_e=6\) everywhere.

For an edge \((0,0)(1,0)\) of \(S\), the two exclusive neighbor sets are respectively
\[X_e=\{(0,1),(3,0),(3,3)\},\qquad Y_e=\{(1,3),(2,0),(2,1)\}.\]
Each induces exactly two edges (a length-two path), giving \(w_e=2+2=4\). Translations together with the maps \((a,b)\mapsto(a-b,a)\) and \((a,b)\mapsto(-a,-b)\), which preserve the six-generator connection set, act transitively on edges, so \(w_e=4\) everywhere. Substitution in the universal laws gives
\[\begin{aligned}
\|Q_R\|_{1\to1}&=(84-12)/32=\tfrac94,&
\|Q_S\|_{1\to1}&=(84-8)/32=\tfrac{19}{8},\\
\|C_R\|_{1\to1}&=1+\tfrac94-\tfrac{20}{32}=\tfrac{21}{8},&
\|C_S\|_{1\to1}&=1+\tfrac{19}{8}-\tfrac{20}{32}=\tfrac{11}{4}.
\end{aligned}\]
Both gaps are \(1/8\), as asserted. \(\square\)

## Verification

Run `python3 verify.py` in a directory containing this document and the standalone verifier. It uses only the Python standard library and exact integer/rational arithmetic. For each of six strongly regular graphs (a five-cycle, Petersen graph, triangular graph \(T_5\), \(K_{3,3}\), rook graph \(R\), and Shrikhande graph \(S\)), it verifies regularity parameters exhaustively, checks the proposed zero-sum Laplacian inverse for **every oriented edge**, checks the exact wing-count column formula and cycle complement formula for every column, and reports the maximal rational endpoint norms. The two sixteen-vertex graphs each have 48 edge columns, and the checker tests all 48 rather than sampled columns. It prints `ALL_EXACT_CHECKS_PASS` at successful completion.

An additional direct symbolic matrix computation used an exact \(16\times16\) rational inverse of \(L+J/16\) to construct the two \(48\times48\) projection matrices, checked their ranks and idempotence, and independently reproduced all four rational norms. The general all-parameter proof is the preceding algebra and coarea argument, not finite testing.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii (2023) develop the relation between graph cycle/cut spaces, transportation cost spaces, and invariant norm-minimizing projections; their main explicit families are tori and Hamming graphs, and their Hamming-graph section includes \(R\) as a special graph. The present conclusion is about the **specified canonical orthogonal** projector on arbitrary connected strongly regular graphs and an exact failure of spectral determination; neither a new construction of the projector nor minimum-norm optimality is claimed.

Gurel-Gurevich, Nachmias and Sachdeva (2026) establish general \(O(\log v)\) localization bounds for absolute transfer-current matrices, including averaged edge-current bounds. Those bounds neither give the local wing-edge identity nor decide the difference between \(R\) and \(S\). Standard spectral descriptions of strongly regular graphs imply cospectrality of \(R\) and \(S\), but quadratic spectral information alone does not determine the absolute column sums of the transfer-current projection.

## Limitations

The norms are those of the Euclidean orthogonal cut and cycle projectors regarded on \(\ell_1\) or \(\ell_\infty\), **not** relative projection constants minimized over all projections, and no assertion about intermediate \(\ell_p\) norms is made. The explicit non-spectral gap is for one natural cospectral pair, not a classification of all cospectral strongly regular graphs. The literature comparison does not rule out an equivalent result in obscure or unindexed electrical-network literature. No independent scientific validation has been performed.

## References

1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first posted 21 May 2023), especially Sections 1.1, 1.4, 2.1 and 2.6. https://arxiv.org/abs/2305.12582
2. O. Gurel-Gurevich, A. Nachmias and S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130 (first posted 22 May 2026), especially Theorems 1.1--1.4 and Section 2. https://arxiv.org/abs/2605.24130
