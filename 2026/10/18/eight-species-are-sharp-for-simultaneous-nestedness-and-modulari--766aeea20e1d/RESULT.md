# Eight species are sharp for simultaneous nestedness and modularity improvement under a degree-preserving swap

## Finding

**Theorem.** Let \(G\) be a finite, connected, simple bipartite interaction graph, with nonempty, distinguished guilds of sizes \(p\) and \(a\). For each graph define its nested overlap and decreasing fill (NODF) score \(\mathcal N(G)\), normalized to the interval \([0,1]\), and its maximum Newman–Girvan modularity \(Q^*(G)\), both specified below. A *checkerboard swap* exchanges the diagonal entries \((1,0;0,1)\) and \((0,1;1,0)\) in a two-by-two submatrix of the bipartite incidence matrix, so it preserves every labeled species degree. Require that the graph after the swap is also connected.

If \(p+a\le7\), no checkerboard swap can strictly increase both \(\mathcal N\) and \(Q^*\). This bound is sharp: a connected graph with \(p=3\), \(a=5\), and eight edges admits a single degree-preserving swap for which both values strictly increase. In a row-by-column representation, a witness is

\[
 B=\begin{pmatrix}
0&1&1&1&1\\
1&0&1&0&0\\
1&1&0&0&0
\end{pmatrix},\qquad
 B'=\begin{pmatrix}
1&1&1&0&1\\
0&0&1&1&0\\
1&1&0&0&0
\end{pmatrix}.
\]

The swap exchanges the two occupied positions \((1,4)\) and \((2,1)\) with the two unoccupied positions \((1,1)\) and \((2,4)\) (one-based labels). Both degree vectors are exactly \((4,2,2)\) on the row side and \((2,2,2,1,1)\) on the column side, and both graphs are connected and unicyclic. The scores are

\[
\mathcal N(B)=\frac5{13},\quad \mathcal N(B')=\frac{11}{26},\quad
\mathcal N(B')-\mathcal N(B)=\frac1{26}>0,
\]
\[
 Q^*(B)=\frac9{32},\quad Q^*(B')=\frac{39}{128},\quad
 Q^*(B')-Q^*(B)=\frac3{128}>0.
\]

This is a minimum-size statement only for the explicitly defined metrics, connectedness condition, and one-step degree-preserving swap; no conclusion is claimed for alternate modularity conventions or nestedness indices.

## Assumptions and scope

An interaction graph has no loops, parallel edges, or within-guild edges. Its \(p\times a\) incidence matrix has entries zero or one. For each row \(i\), write \(R_i\) for its set of neighboring columns; for each column \(j\), write \(C_j\) for its set of neighboring rows. Put \(d_i=|R_i|\) and \(e_j=|C_j|\). Since the graph is connected, all these degrees are positive.

For distinct nonempty finite sets \(U,V\), define the pairwise NODF contribution

\[
 F(U,V)=\begin{cases}
0,&|U|=|V|,\\
\displaystyle \frac{|U\cap V|}{\min(|U|,|V|)},&|U|\ne|V|.
\end{cases}
\]

The precise NODF normalization used here is

\[
\mathcal N(G)=\frac{\sum_{i<k}F(R_i,R_k)+\sum_{j<\ell}F(C_j,C_\ell)}{\binom p2+\binom a2},
\]

provided the denominator is positive, as it is whenever a two-by-two swap is possible. This is the usual NODF value divided by \(100\); row and column pairs of equal degree contribute zero. The definition does not depend on the ordering of vertices within either guild.

For \(m=|E(G)|\ge1\), let \(\mathcal P\) range over all set partitions of the full vertex set, without restricting whether a block includes vertices of both guilds. The Newman–Girvan modularity of \(\mathcal P\) is

\[
 Q_G(\mathcal P)=\sum_{S\in\mathcal P}\left(\frac{\ell_G(S)}m-\left(\frac{\operatorname{vol}_G(S)}{2m}\right)^2\right),
 \qquad Q^*(G)=\max_{\mathcal P} Q_G(\mathcal P),
\]

where \(\ell_G(S)\) is the number of edges with both endpoints in \(S\), and \(\operatorname{vol}_G(S)\) is the sum of degrees of vertices in \(S\). This is unipartite Newman–Girvan modularity evaluated on a bipartite graph, as in Fortuna et al. (2010), **not** Barber's alternative bipartite modularity.

## Proof

**1. The only relevant sizes below eight.** A swap requires two vertices on each side. If either guild has at most two vertices, \(\mathcal N\) is invariant under every degree-preserving swap: with two rows, their intersection equals the number of columns of degree two, which is fixed by the column degree vector. Any pair of columns of unequal degrees has degrees one and two; its overlap contribution is exactly one, also fixed. Equal-degree pairs contribute zero. The case of one row has no swap. Hence both quantities cannot strictly increase when \(\min(p,a)\le2\), regardless of total size. Up to guild interchange, the only cases left when \(p+a\le7\) are \((p,a)=(3,3)\) and \((3,4)\).

**2. Finite classification of the remaining cases.** Exhaustive exact enumeration, implemented in `verify.py`, runs over all \(2^{pa}\) labeled binary matrices for these two sizes, retaining precisely those with connected bipartite graphs. It visits every pair of row indices and pair of column indices and checks the two valid diagonal checkerboard patterns. It retains the swapped graph only if that graph is connected. It evaluates \(\mathcal N\) by rational arithmetic and \(Q^*\) by exact integer partition optimization, described next.

There are \(205\) connected labeled matrices at \((3,3)\) and \(216\) directed valid connected swaps; at \((3,4)\) the corresponding counts are \(1795\) and \(4320\). At both sizes the number of directed swaps with strict increases in **both** scores is zero. At \((3,4)\), \(576\) directed swaps change both scores strictly, always in opposite directions. These are exhaustive outcomes, not statistical samples. Together with step 1, this proves the lower bound.

For clarity, here is why modularity is optimized over **all** partitions rather than only sampled partitions. For each nonempty vertex subset \(S\), define the integer

\[
 w_G(S)=4m\,\ell_G(S)-\operatorname{vol}_G(S)^2.
\]

If \(D(\varnothing)=0\) and \(v\) is any fixed vertex of \(T\), set

\[
 D(T)=\max_{\substack{S\subseteq T\\v\in S}}
 \bigl(w_G(S)+D(T\setminus S)\bigr).
\]

Every partition has exactly one block containing \(v\), so induction on \(|T|\) proves this recurrence considers every partition, with

\[
 Q^*(G)=\frac{D(V(G))}{4m^2}.
\]

The verification program checks all subsets and all possible blocks containing the least-index vertex. Its connectedness test is a graph search; the complete matrix loop and all candidate two-by-two swaps form an exhaustive proof for the stated finite sizes.

**3. Sharpness at eight species.** Both displayed eight-vertex matrices are connected and have eight edges. Pairwise NODF contributions sum to \(5\) for \(B\) and \(11/2\) for \(B'\); the common pair-count denominator is \(\binom32+\binom52=13\). The exact partition recurrence yields \(D(V)=72\) and \(78\), respectively, with common denominator \(4m^2=256\), proving the displayed values. For an independent finite check of the two optima, `verify.py` also evaluates all \(4140\) set partitions of eight labeled vertices for each matrix; this agrees with the dynamic program.

One maximizing partition for \(B\) groups vertices \(\{r_1,c_4,c_5\}\), \(\{r_2,c_1,c_3\}\), and \(\{r_3,c_2\}\). One for \(B'\) groups \(\{r_1,r_3,c_1,c_2,c_5\}\) and \(\{r_2,c_3,c_4\}\). Their integer modularity numerators are, respectively, \(72\) and \(78\). The strict inequalities prove sharpness.

## Verification

Run `python verify.py` with the Python standard library (version 3.9 or newer). It checks all connected labeled graphs and all connected-output checkerboard swaps at total sizes three through seven, independently computes the normalized NODF fractions and maximum modularities, and checks the explicit eight-vertex witness. All quantities are exact rationals or integers; no floating-point tolerances are used. A separate enumeration of all set partitions of the eight witness vertices independently checks the modularity dynamic program. The finite state spaces and the partition recurrence prove exhaustiveness over the specified range. Results do not rely on simulation, random sampling, or unreported external data.

## Relationship to prior work

Almeida-Neto et al. (2008) introduced NODF as a metric of overlap and decreasing fill, with fixed-degree randomizations. Fortuna et al. (2010) directly studied nestedness and Newman–Girvan modularity together and explicitly used degree-preserving two-by-two swaps; their conclusion concerns empirical-network and null-model correlations with connectance, rather than the first connected bipartite graph size for simultaneous strict local improvement of both exact metrics. Joppa et al. (2011) examined contributions of individual incidence-matrix cells to NODF, rather than joint optimal modularity. Leung and Weitz (2015) studied how network growth produces nested and modular structures, using Barber's bipartite modularity; their generative results do not imply the stated exact connected fixed-degree threshold. Recent generative-null-model comparisons (de los Ríos et al., 2026) likewise do not present a finite minimality classification.

The contribution is **not** the pre-existing general observation that nestedness and modularity can coexist or correlate positively. It is the explicit sharp \(8\)-species *single degree-preserving switch* threshold for the **specified pair** of standard metrics, with exact partition optimization and complete exclusion at smaller sizes.

## Limitations

This is a structural theorem for binary undirected interaction matrices, not a claim about ecological stability, species extinction, or causal effects of real network rewiring. The two metrics are sensitive to their definitions, especially the unipartite versus bipartite modularity distinction. The finite classification addresses total vertex number at most eight for the asserted threshold; it does not classify all larger matrices or all degree-sequence fibers. It does not establish how frequently the co-improvement occurs in empirical communities. Unexamined equivalent formulations under other network-analysis terminology remain a bibliographic risk.

## References

1. Almeida-Neto, M., Guimarães, P., Guimarães, P. R., Loyola, R. D., and Ulrich, W. (2008), “A consistent metric for nestedness analysis in ecological systems: reconciling concept and measurement,” *Oikos* 117, 1227–1239. DOI: 10.1111/j.0030-1299.2008.16644.x. Original NODF definition.
2. Fortuna, M. A. et al. (2010), “Nestedness versus modularity in ecological networks: two sides of the same coin?”, *Journal of Animal Ecology* 79, 811–817. DOI: 10.1111/j.1365-2656.2010.01688.x. Original full text: https://stoufferlab.org/pdfs/Fortuna-2010-J.Anim.Ecol.-79-811.pdf.
3. Joppa, L. N., Montoya, J. M., Solé, R., Sanderson, J., and Pimm, S. L. (2011), “The influence of single elements on nested community structure,” *Methods in Ecology and Evolution*. DOI: 10.1111/j.2041-210X.2011.00101.x.
4. Leung, C. Y. and Weitz, J. S. (2015), “Conflicting attachment and the growth of bipartite networks,” arXiv:1511.04025 (first public preprint, 2015-11-12), https://arxiv.org/abs/1511.04025.
5. de los Ríos, H., Palazzi, M. J., Lampo, A., Solé-Ribalta, A., and Borge-Holthoefer, J. (2026), “Bipartite structural evaluation: Extended network generation model and corrected randomization techniques,” *Physical Review Research* 8, 013036. DOI: 10.1103/7t51-c6tx.
