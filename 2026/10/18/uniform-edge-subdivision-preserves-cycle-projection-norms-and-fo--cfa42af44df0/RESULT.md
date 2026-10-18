# Uniform edge subdivision preserves cycle-projection norms and forces cut dominance

## Finding

Let \(G=(V,E)\) be any finite connected simple undirected graph with at least one edge. Fix arbitrary edge orientations and regard the cycle-flow space \(Z(G)\) as a subspace of the real coordinate edge space \(\ell_2(E)\). Write \(C_G\) for the orthogonal projection onto \(Z(G)\), and \(Q_G=I-C_G\) for the orthogonal cut-space projection. All operator norms below are the induced real \(\ell_1\)-norms, equally the induced \(\ell_\infty\)-norms because these projection matrices are symmetric.

Replace each edge \(e\) by a simple oriented path of \(r_e\ge1\) unit edges, with distinct new interior vertices; call the resulting graph \(G_{\mathbf r}\). Choose any matrix \(B\) whose columns form a basis of \(Z(G)\), put \(R=\operatorname{diag}(r_e)\), and define
\[
H=B(B^{\mathsf T}RB)^{-1}B^{\mathsf T},\qquad
A_e=\sum_{f\in E}r_f|H_{fe}|.
\]
When \(G\) is a tree, set \(H=0\); the statements below then remain valid.

**Nonuniform subdivision law.** The orthogonal cycle projection of \(G_{\mathbf r}\), on subdivided edge coordinates \((e,i)\), has entries
\[
(C_{G_{\mathbf r}})_{(f,j),(e,i)}=H_{fe}.
\]
Consequently,
\[
\boxed{\ \|C_{G_{\mathbf r}}\|_{1\to1}=\max_{e\in E} A_e,\quad
\|Q_{G_{\mathbf r}}\|_{1\to1}=\max_{e\in E}(1+A_e-2H_{ee}).\ }
\]
For every original edge \(e\), \(0\le r_eH_{ee}<1\). Thus if **every original edge is subdivided at least once**, meaning \(r_e\ge2\) for all \(e\), then each corresponding cut-projection column has strictly larger absolute sum than its cycle-projection column, and
\[
\boxed{\ \|Q_{G_{\mathbf r}}\|_{1\to1}>\|C_{G_{\mathbf r}}\|_{1\to1}.\ }
\]

**Uniform subdivision law.** If every length equals the same integer \(r\ge1\), put \(c_e=\sum_f |(C_G)_{fe}|\) and \(d_e=(C_G)_{ee}\). Then
\[
\boxed{\ \|C_{G_r}\|_{1\to1}=\|C_G\|_{1\to1},\qquad
\|Q_{G_r}\|_{1\to1}=\max_{e\in E}\left(1+c_e-\frac{2d_e}{r}\right).\ }
\]
The second expression is nondecreasing in \(r\), with
\[
\lim_{r\to\infty}\|Q_{G_r}\|_{1\to1}=1+\|C_G\|_{1\to1},\qquad
0\le 1+\|C_G\|_{1\to1}-\|Q_{G_r}\|_{1\to1}\le\frac2r.
\]

The threshold \(r=2\) is sharp as a graph-independent assertion: for the unsplit complete graph \(K_5\),
\[
\|Q_{K_5}\|_{1\to1}=\frac85<\frac95=\|C_{K_5}\|_{1\to1},
\]
whereas after subdividing every edge once,
\[
\|Q_{(K_5)_2}\|_{1\to1}=\frac{11}5>\frac95=\|C_{(K_5)_2}\|_{1\to1}.
\]
No claim is made that the orthogonal projections are minimum-norm among all projections onto the relevant subspaces.

## Assumptions and scope

The graph is finite, connected, simple, loopless and has at least one edge. All edge spaces and projections are real, and new paths have positive integer lengths. Every new interior vertex lies on exactly one path and has degree two. Coordinates are oriented consistently along each path, so a circulation has a constant signed flow on all edges of a path. These norms are operator norms of the specified Euclidean orthogonal projections, not intrinsic minimum complementability constants. The formula for a tree is interpreted with an empty cycle basis and a zero cycle projection. The same answers apply to \(\ell_\infty\) by symmetry.

## Proof

**Step 1 (the cycle-space lift).** Orient each original edge \(e\), and orient all \(r_e\) edges of its replacement path consistently. Define the replication map \(U:\mathbb R^E\to\mathbb R^{E(G_{\mathbf r})}\) by \((Uz)_{(e,i)}=z_e\). Conservation at each new degree-two vertex forces any circulation to have equal values along its path. Conversely, the remaining conservation equations at original vertices are exactly those of \(G\). Therefore
\[
Z(G_{\mathbf r})=U Z(G),\qquad U^{\mathsf T}U=R.
\]

**Step 2 (exact projector).** If the cycle rank is positive, the full-column-rank matrix \(UB\) spans the subdivided cycle space. The standard orthogonal-projector formula yields
\[
C_{G_{\mathbf r}}=UB\left(B^{\mathsf T}U^{\mathsf T}UB\right)^{-1}B^{\mathsf T}U^{\mathsf T}=UHU^{\mathsf T}.
\]
Its \(((f,j),(e,i))\) entry is \(H_{fe}\), independently of the path positions. If the cycle rank is zero, both sides are zero.

**Step 3 (strict diagonal inequality).** The matrix \(R^{1/2}HR^{1/2}\) is the Euclidean orthogonal projection onto \(R^{1/2}Z(G)\). Consequently \(0\le r_e H_{ee}\le1\). Equality to one would force the coordinate vector supported only on \(e\) to lie in \(R^{1/2}Z(G)\), and hence force a nonzero circulation supported on one loopless edge of \(G\); this is impossible. Thus \(0\le r_eH_{ee}<1\) for every \(e\), including bridge edges where equality to zero is allowed.

**Step 4 (absolute column sums).** Consider any one subdivided edge \((e,i)\). Its cycle-projection column consists of \(r_f\) copies of \(H_{fe}\) for each original edge \(f\). Its absolute sum is exactly \(A_e\). For the cut projection \(Q=I-C\), the diagonal entry is \(1-H_{ee}>0\), and all other entries on the same original path are \(-H_{ee}\le0\). Entries on other paths are \(-H_{fe}\). Since \(H_{ee}\ge0\), the cut-projection absolute column sum is
\[
(1-H_{ee})+(r_e-1)H_{ee}+\sum_{f\ne e}r_f|H_{fe}|=1+A_e-2H_{ee}.
\]
The induced \(\ell_1\)-norm of a finite matrix is its maximum absolute column sum. The matrices here are symmetric, so their maximum absolute row sums, hence induced \(\ell_\infty\)-norms, agree. If every \(r_e\ge2\), Step 3 gives \(H_{ee}<1/r_e\le1/2\), making the cut sum strictly exceed the cycle sum in *each* column. Taking the column attaining the cycle norm proves strict dominance of the cut norm.

**Step 5 (uniform lengths).** If \(R=rI\), then
\[
H=\frac1r B(B^{\mathsf T}B)^{-1}B^{\mathsf T}=\frac1r C_G.
\]
The formula of Step 4 reduces to the stated two uniform norms, and every cycle column sum is unchanged. Since each \(d_e\in[0,1)\), each cut column expression is nondecreasing as a function of \(r\). Write \(M=\max_e c_e\). The upper estimate \(\|Q_{G_r}\|\le1+M\) is immediate; choosing any \(e\) with \(c_e=M\) yields \(\|Q_{G_r}\|\ge1+M-2d_e/r\ge1+M-2/r\). This establishes the limit and the error bound.

**Step 6 (sharpness of requiring subdivision).** Let \(G=K_5\). Writing \(D\) for the oriented vertex-edge incidence matrix, the unit-edge effective-resistance identity gives the cut projection \(Q_G=D^{\mathsf T}(DD^{\mathsf T})^+D\), whose diagonal equals \(2/5\). For a fixed edge there are six edges sharing exactly one endpoint; their off-diagonal cut-projector entries have absolute value \(1/5\); all other off-diagonal entries vanish. The corresponding cut column sum is \(2/5+6/5=8/5\). The cycle projector \(C_G=I-Q_G\) has diagonal \(3/5\) and the same six off-diagonal absolute values, giving \(3/5+6/5=9/5\). The uniform formula at \(r=2\) gives the subdivided cut norm \(1+9/5-3/5=11/5\), while the cycle norm remains \(9/5\). This proves the asserted reversal and shows that \(r\ge2\) cannot be relaxed to \(r\ge1\) uniformly over graphs.

## Verification

The accompanying standalone Python checker uses exact rational arithmetic and separately constructs the orthogonal projector of each subdivided graph by a reduced incidence-Laplacian inverse. Separately, it computes the weighted original-graph expression for \(H\), checking all matrix entries and both column-norm identities. It covers the complete graphs \(K_4,K_5\), a six-cycle, a three-branch theta graph, a two-triangle graph with a bridge, a tree, and \(K_{3,3}\), with uniform, fully nonuniform, and mixed path lengths. All 35 graph/length configurations and 10,264 full projection entries passed, including exact verification of the reversal at \(K_5\). The code proves only these finite checks; the universal and limiting statements follow from Steps 1–6.

Run with Python 3.10 or newer: `python verify_subdivision.py`.

## Relationship to prior work

The 2023 work of Dilworth, Kutzarova and Ostrovskii develops invariant and orthogonal projections onto graph cycle spaces and obtains results for discrete tori and Hamming graphs; its original preprint carries primary MSC 46B04. Their 2020 work analyzes recursively edge-replaced diamond and Laakso graphs by cycle-space methods. Both provide directly relevant motivation and standard definitions. The present result instead concerns arbitrary finite connected graphs undergoing simple series subdivision of edges, and determines an exact transformation law for both canonical endpoint projection norms, including a universal reversal of cut/cycle dominance. This statement has not been identified in the examined primary texts or the completed research-record comparisons. Standard electrical-network series reduction alone does not specify these induced \(\ell_1\) projector norms, because they depend on *absolute sums of every expanded edge-column*.

## Limitations

All norms are for the **canonical orthogonal projections**; minimum projection norms over unrestricted complementary maps are not evaluated. The theorem is finite-dimensional; no assertion about a fixed infinite graph or an infinite subdivision limit in a common ambient space is made. The positive-integer restriction models subdivision into unit edges, not arbitrary positive continuous lengths. Exact finite verification supports, but is not a proof of, the all-graph statement. An independently established literature equivalence could supersede the originality assessment.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first publicly posted 2023-05-21), especially Sections 1.1, 1.4–1.6, 2.1, and 2.7. https://arxiv.org/abs/2305.12582
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, arXiv:2007.07949 (first publicly posted 2020-07-15), especially Sections 1 and 4–5. https://arxiv.org/abs/2007.07949
