# Fractional clique-cover norms and the sharp two-threshold for graph-generated Banach spaces

## Finding
For an arbitrary nonempty set \(V\) and a simple graph \(G\) on \(V\), define \(X_G\) by completing finitely supported real vectors for the clique norm
\[
\|x\|_G=\sup\left\{\sum_{v\in C}|x_v|:C\subseteq V\text{ is a finite clique of }G\right\}.
\]
Write \(H=\overline G\) for the complementary graph. The canonical coordinate identity \(J_G:X_G\to\ell_1(V)\) is bounded if and only if the fractional chromatic numbers of the finite induced subgraphs of \(H\) are uniformly bounded. In that case it is an onto isomorphism and
\[
\boxed{\|J_G\|=\sup_{E\subseteq V\text{ finite}}\chi_f(H[E]),\qquad \|J_G^{-1}\|=1.}
\]
The following is a sharp rigidity-versus-realization distinction. One has \(\|J_G\|\le2\) if and only if \(H\) is bipartite; in that case \(G\) admits a partition into at most two cliques, and its canonical norm is \(1\) if \(H\) is edgeless and \(2\) otherwise. Conversely, for every real \(c>2\) there exists a graph \(G_c\) on \(\omega_1\) such that \(J_{G_c}\) is an onto isomorphism with \(\|J_{G_c}\|=c\) and \(\|J_{G_c}^{-1}\|=1\), but \(G_c\) cannot be covered by finitely many cliques; in fact \(\chi(\overline{G_c})=\aleph_0\).

More generally, for hereditary families \(\mathcal F,\mathcal H\subseteq[V]^{<\omega}\) containing all singletons, the exact norm of the coordinate identity, whenever bounded, is the supremum of the finite fractional \(\mathcal F\)-cover numbers of members of \(\mathcal H\), defined precisely below.

## Assumptions and scope
All spaces are real. For an arbitrary set \(V\), let \([V]^{<\omega}\) denote its finite subsets. Let \(\mathcal F\) and \(\mathcal H\) be hereditary subfamilies containing each singleton. For finite \(E\subseteq V\), define
\[
\tau_{\mathcal F}^*(E)=\min\left\{\sum_{F\in\mathcal F,\,F\subseteq E}\lambda_F:\ \lambda_F\ge0,\quad \sum_{F\ni v}\lambda_F\ge1\ (v\in E)\right\},
\]
with \(\tau_{\mathcal F}^*(\varnothing)=0\). Singletons ensure feasibility; all programs have finitely many variables. Let \(X_{\mathcal F}\) and \(X_{\mathcal H}\) be completions of \(c_{00}(V)\) in the corresponding set-sum norms. The coordinate identity initially means the literal identity on \(c_{00}(V)\); no assertion concerns an arbitrary isomorphism or the Banach–Mazur distance. In the graph specialization, \(\mathcal F\) is the family of finite cliques of \(G\), and \(\mathcal H=[V]^{<\omega}\). Fractional chromatic number \(\chi_f(Q)\) of a finite graph \(Q\) is the linear-program optimum for covering every vertex by nonnegative weights on independent sets.

## Proof
**1. The hereditary-family identity formula.** On \(c_{00}(V)\), the norm of the coordinate identity from \(\|\cdot\|_{\mathcal F}\) to \(\|\cdot\|_{\mathcal H}\) equals
\[
\sup_{E\in\mathcal H}\ \sup_{\substack{w_v\ge0\ (v\in E)\\ \sum_{v\in F}w_v\le1\ (F\in\mathcal F,\,F\subseteq E)}}\sum_{v\in E}w_v.
\]
To see this, interchange the supremum over vectors and the supremum over \(E\in\mathcal H\). For a fixed \(E\), setting coefficients outside \(E\) to zero changes neither the target sum nor the validity of the source constraints. As \(\mathcal F\) is hereditary, every source constraint meeting \(E\) reduces to a constraint indexed by \(F\cap E\in\mathcal F\). Taking absolute values removes signs. The displayed finite maximization is the linear-program dual of the minimization defining \(\tau_{\mathcal F}^*(E)\). Both are feasible and bounded, by the singleton constraints, so finite-dimensional strong LP duality gives
\[
\boxed{\|J_{\mathcal F\to\mathcal H}\|=\sup_{E\in\mathcal H}\tau_{\mathcal F}^*(E)}
\]
where infinite supremum means that no bounded extension exists.

**2. Fractional chromatic specialization and surjectivity.** For \(\mathcal F=\mathcal C(G)\), the sets in \(\mathcal F\cap\mathcal P(E)\) are exactly the independent sets of \(H[E]\); therefore \(\tau_{\mathcal F}^*(E)=\chi_f(H[E])\). This proves the asserted exact operator norm. Conversely the canonical inclusion \(I:\ell_1(V)\to X_G\) always has norm exactly \(1\): every clique sum is bounded by the total absolute sum, and a singleton unit vector witnesses equality. If \(J_G\) is bounded, \(J_GI\) and \(IJ_G\) equal the identities on dense finitely supported subspaces, so they are the identities everywhere. Hence \(J_G\) is onto and has inverse norm \(1\).

**3. The sharp threshold \(2\).** If \(H\) is bipartite, each finite induced subgraph admits a proper two-coloring; hence \(\chi_f(H[E])\le2\) and \(\|J_G\|\le2\). If \(H\) contains any edge, its induced two-vertex subgraph has fractional chromatic number \(2\), so \(\|J_G\|=2\); otherwise \(G\) is complete and \(\|J_G\|=1\). Conversely, suppose \(H\) contains an odd cycle on \(2m+1\) distinct vertices. Every independent set of that cycle has at most \(m\) vertices. Assigning dual LP weight \(1/m\) to each cycle vertex gives \(\chi_f(H[E])\ge(2m+1)/m=2+1/m>2\) for its vertex set \(E\), even when additional chords are present. Thus \(\|J_G\|\le2\) forbids odd cycles. A graph has no odd cycle exactly when it is bipartite, for arbitrary vertex cardinality (color each connected component by path parity). A bipartition of \(H\) partitions \(G\)'s vertices into at most two nonempty cliques.

**4. Arbitrarily small excess with unbounded integral clique cover.** Fix any real \(c>2\). For every integer \(k\ge1\) set \(n_k=\lfloor ck\rfloor\ge2k\) and \(W_k=\binom{[n_k]}{k}\), the finite set of all \(k\)-subsets of \([n_k]\). Take pairwise disjoint blocks \(B_{k,\xi}\cong W_k\) for \(k\ge1\) and \(\xi<\omega_1\); their union \(V\) has cardinality \(\omega_1\). Define \(G_c\) so that distinct vertices in a common block are adjacent precisely when their corresponding \(k\)-subsets intersect, while every two vertices from different blocks are adjacent. Thus the complement \(H_c\) is the disjoint union of the Kneser graphs \(KG(n_k,k)\), repeated \(\omega_1\) times.

For any finitely supported vector \(x\), complete joining makes the norm additive across its finitely many active blocks:
\[
\|x\|_{G_c}=\sum_{(k,\xi)}\|x|_{B_{k,\xi}}\|_{G_c|B_{k,\xi}}.
\]
For one block, select \(r\) uniformly from \([n_k]\). The star \(\{A\in W_k:r\in A\}\) is a clique; averaging its absolute coefficient sum over \(r\) gives \((k/n_k)\|x\|_1\). Consequently \(\|x\|_1\le (n_k/k)\|x\|_{G_c}\) in that block. The bound is exact for the vector with coefficient \(1\) at every \(A\in W_k\): by the Erdős–Ko–Rado theorem, the largest intersecting family has \(\binom{n_k-1}{k-1}\) elements, so the norm ratio is
\[
\frac{\binom{n_k}{k}}{\binom{n_k-1}{k-1}}=\frac{n_k}{k}.
\]
Summing across the blocks gives \(\|J_{G_c}\|=\sup_{k\ge1}(n_k/k)=c\). The inclusion inverse still has norm \(1\). Finally the Lovász–Kneser theorem yields
\[
\chi(KG(n_k,k))=n_k-2k+2\longrightarrow\infty.
\]
As the complement is a disjoint union of finite components, it admits a countable proper coloring but no finite coloring: \(\chi(H_c)=\aleph_0\). Hence a finite cover of \(V\) by \(G_c\)-cliques is impossible. The graph is nonseparable in the Banach sense because \(X_{G_c}\) is canonically isomorphic to \(\ell_1(\omega_1)\). This completes the proof.

## Verification
Every use of optimization in the general formula is a **finite** primal–dual pair; no compactness or infinite-dimensional LP duality is assumed. For a block with \(k=2\) and \(n_k=5\), there are \(\binom52=10\) vertices and the maximal intersecting family has \(\binom41=4\) members, giving the exact norm ratio \(10/4=5/2\). This finite witness is illustrative, not a proof for all blocks. The infinite-dimensional statements follow instead from the finite-support norm identity, density in the completions, the uniform star averaging, the named Erdős–Ko–Rado and Lovász–Kneser theorems, and the explicit cardinality of the block system. The two named graph theorems are invoked as published results, not claimed to have been reproved here.

## Relationship to prior work
Borodulin-Nadzieja, Marsy and Ryduchowski (arXiv:2610.01919v1) supply the nonseparable graph-generated Banach-space framework and characterize embeddings of long sequence spaces by different combinatorial and measure-theoretic criteria. The present statement concerns the **bounded canonical coordinate identity** and its exact norm, rather than existence of an arbitrary subspace copy.

Borodulin-Nadzieja, Farkas, Jachimek and Pelczar-Barwacz (arXiv:2404.01733v1), Example 4.7, already construct integer-parameter star-generated hereditary families with bounded \(\ell_1\) distortion and growing finite star-cover requirements. That strong precursor is credited. Its families are not the full clique families of the intersection graphs. The exact fractional-chromatic identity, universal two-threshold, arbitrary real parameters above it, and an uncountable graph whose **full** clique family still has unbounded integral covering number are not statements of that example. The perfect-graph duality theorem in arXiv:2605.14072v1 concerns a different extreme-point criterion and does not supply these quantitative nonperfect-graph identities. Standard fractional coloring, Erdős–Ko–Rado, and Lovász–Kneser theorems are explicitly used and not presented as novel.

## Limitations
The isomorphism and distortion are strictly **coordinate-canonical**: the result does not determine the Banach–Mazur distance over all possible linear isomorphisms, nor characterize arbitrary subspaces of \(X_G\). The construction relies on classical Kneser-graph coloring theorems. No claim is made about norm attainment of the canonical identity, embeddings between complexified spaces, set-theoretic forcing, or the chromatic number for graph families outside the displayed construction. The originality assessment is restricted to the primary literature and database actually inspected; an unindexed equivalent application of fractional graph coloring remains a residual risk.

## References
1. P. Borodulin-Nadzieja, M. Marsy and K. Ryduchowski, *Non-separable combinatorial Banach spaces*, arXiv:2610.01919v1 (public October 1, 2026), Sections 1, 4, 5 and 6; primary MSC2020 46B45.
2. P. Borodulin-Nadzieja, B. Farkas, S. Jachimek and A. Pelczar-Barwacz, *The Zoo of combinatorial Banach spaces*, arXiv:2404.01733v1, Example 4.7.
3. P. Borodulin-Nadzieja, B. Farkas and A. Pelczar-Barwacz, *Geometric duality, perfect graphs, and the Sierpiński space*, arXiv:2605.14072v1, Section 4.
4. *Critical Subgraphs of Schrijver Graphs for the Fractional Chromatic Number*, *Graphs and Combinatorics* (2024), DOI:10.1007/s00373-024-02782-9, Section 2, Theorems 1 and 2 and Corollary 3 (statements of the Lovász–Kneser and Erdős–Ko–Rado results).
