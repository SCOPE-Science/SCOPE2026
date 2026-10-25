# Optimal outer-independent two-rainbow labelings of star coronas

## Finding

Let \(G\) be a finite simple graph with \(n\ge 1\) vertices. For an integer \(k\ge 2\), write \(W_k(G)=G\odot\overline{K_k}\): attach \(k\) distinct private leaves to every vertex of \(G\). An **outer-independent two-rainbow dominating function** is a map \(f:V(W_k(G))\to\{\varnothing,\{1\},\{2\},\{1,2\}\}\) such that the vertices labeled \(\varnothing\) form an independent set and every such vertex has both colors in the union of its neighbors' labels. Its weight is \(w(f)=\sum_v|f(v)|\).

**Theorem (optimal-labeling phase transition).** For every such \(G\) and \(k\ge 2\), the minimum weight is \(2n\). Let \(Z\) be the set of isolated vertices of \(G\), let \(G^\circ=G-Z\), and put \(i=|Z|\). Define the independence polynomial \(I_F(t)=\sum_{J\subseteq V(F),\ J\text{ independent}}t^{|J|}\). The polynomial enumerating minimum functions by the number of **original** vertices labeled empty is

\[
Q_{G,k}(t)=\sum_{\substack{f\text{ outer-independent two-rainbow}\\w(f)=2n}}t^{|\{v\in V(G):f(v)=\varnothing\}|}
=\begin{cases}(1+2t)^i I_{G^\circ}(4t),&k=2,\\1,&k\ge3.\end{cases}
\]

Consequently, if \(G\) has no isolated vertices, the number of minimum functions on \(W_2(G)\) is exactly \(I_G(4)\); on \(W_k(G)\) with \(k\ge3\) the minimum function is unique. Moreover, **exact counting of minimum outer-independent two-rainbow dominating functions is \(\#\mathrm P\)-complete under polynomial-time Turing reductions**, even when inputs are bipartite two-leaf coronas \(W_2(G)\) of bipartite graphs \(G\) without isolated vertices. The complexity statement concerns exact enumeration; the minimum weight itself is explicitly known.

## Assumptions and scope

Graphs are finite, simple, undirected, and have named (distinguishable) vertices and private leaves. The parameter \(k\) is a positive integer at least two. No connectivity or positive minimum-degree hypothesis is imposed on \(G\). Two labelings that exchange colors globally or permute leaves are counted separately unless they agree at every named vertex. A minimum labeling means a function of least weight among all functions satisfying **both** outer-independence and rainbow domination.

## Proof

For an original vertex \(v\) let \(B_v\) denote \(v\) together with its \(k\) private leaves. If \(f(v)=\varnothing\), outer-independence forces every private leaf to have a nonempty label; hence \(w(f|_{B_v})\ge k\). If \(f(v)\) is a singleton, a private leaf cannot be empty, since that leaf has only \(v\) as neighbor and would see only one color. Thus \(w(f|_{B_v})\ge k+1\). If \(f(v)=\{1,2\}\), the block weight is at least two. These disjoint blocks partition the vertex set, so \(w(f)\ge2n\). Setting every original vertex to \(\{1,2\}\) and every leaf to \(\varnothing\) is valid, proving equality.

For \(k\ge3\), equality in any block is possible only when the original vertex has label \(\{1,2\}\) and all its private leaves are empty. These prescriptions are globally valid and uniquely determine the optimum, proving \(Q_{G,k}(t)=1\).

For \(k=2\), equality in each block forces exactly one of two types: type A has original vertex labeled \(\{1,2\}\) and both leaves empty; type B has original vertex empty and both leaves labeled singletons. A singleton-labeled original vertex costs at least three and cannot occur at the optimum. Write \(J\) for the set of original vertices of type B. Since their labels are empty, \(J\) is independent in \(G\). For every \(v\in J\) with positive degree, every original neighbor is of type A (and hence carries both colors). Therefore **each of the four ordered singleton pairs** on its two leaves satisfies rainbow domination at \(v\). For an isolated \(v\in J\), there are exactly **two** permissible ordered pairs, namely opposite singleton colors. Every type-A leaf is itself dominated by the double-labeled original vertex. No additional empty-empty edge exists: \(J\) is independent, and empty private leaves occur only at type-A originals. Thus these conditions are also sufficient.

Conversely, choosing any independent \(J\subseteq V(G)\), giving every vertex outside \(J\) type A, and choosing the indicated singleton leaf pairs at vertices of \(J\), produces a valid function of weight \(2n\). This establishes a bijection. Decomposing \(J\) into its isolated and nonisolated original vertices gives

\[
Q_{G,2}(t)=\sum_{J\text{ independent}}2^{|J\cap Z|}4^{|J\setminus Z|}t^{|J|}
=(1+2t)^i I_{G^\circ}(4t).
\]

It remains to establish the exact-counting consequence. Membership in \(\#\mathrm P\) follows because, given a two-leaf corona, a candidate labeling can be guessed and its weight, empty-set independence, and two-color neighbor coverage checked in polynomial time; the proven optimum weight is \(2n\). For hardness, counting independent sets in bipartite graphs is \(\#\mathrm P\)-complete (equivalently, counting their vertex covers; Provan and Ball). Isolated vertices can be removed from an independent-set instance and their known factor \(2^i\) restored, so the source problem remains hard on bipartite graphs without isolated vertices.

For such a source graph \(G\) with \(n\) vertices, replace each original vertex by \(r\) mutually nonadjacent clones and each original edge by all \(r^2\) cross-edges between its endpoint clone classes, obtaining \(G^{(r)}\). It remains bipartite and has no isolated vertices. An independent set of \(G^{(r)}\) meets clone classes only over an independent set of \(G\); each selected class has \(r\) clones and contributes \((1+4)^r-1=5^r-1\) after weighting each selected clone by four. Hence

\[
I_{G^{(r)}}(4)=I_G(5^r-1).
\]

An oracle counting minimum functions of \(W_2(G^{(r)})\) therefore supplies \(I_G(5^r-1)\). Taking \(r=1,\ldots,n+1\) yields \(n+1\) distinct evaluations of the polynomial \(I_G(x)\) of degree at most \(n\). Exact rational interpolation in polynomial bit complexity recovers \(I_G(1)\), the number of independent sets of \(G\). Each queried graph has polynomial order and size. This proves \(\#\mathrm P\)-hardness under polynomial-time Turing reductions, including the bipartite restriction, and completes the proof.

## Verification

The accompanying Python standard-library verifier independently builds the corona adjacency lists and checks labelings from the **original definition**, without using the case classification as its validity test. All labelings are exhaustively searched for every labeled base graph on one, two, or three vertices at \(k=2\); for five representative four-vertex bases, **every** labeling of weight \(2n\) is searched. Further tests search all weight-\(2n\) labelings for every base graph of one through three vertices at \(k=3\) and of one through two vertices at \(k=4\). The resulting profiles agree with the theorem in all 30 cases. Three independent checks of the clone-graph identity for a three-vertex path pass. The program prints `VERIFICATION_OK` if all assertions succeed. The infinite statements and complexity reduction are proved above; finite checks are corroboration, not substitutes for proof.

## Relationship to prior work

Samadi and Soltankhah's first-public 2022 preprint (arXiv:2208.02340, Theorem 3.4 in the 2023 revision) already gives the scalar minimum \(\gamma_{oir2}(G\odot H)\) for coronas with nonisolated base graphs. In particular, its formula gives \(\gamma_{oir2}(G\odot\overline{K_2})=2|V(G)|\). The minimum itself is **not** claimed as new. Cabrera-Martínez's 2022 results cover coronas with both factors having no isolated vertices; that hypothesis excludes \(\overline{K_2}\). The additional results here are the exact enumeration and bijection for **every** base graph (including isolated vertices), the leaf-multiplicity transition, and the resulting specialized exact-counting complexity classification. The enumerator is not fixed by the known scalar minimum: both a three-vertex path and triangle have optimum weight six, but their numbers of minimum functions are respectively \(29\) and \(13\).

The graph independence polynomial and \(\#\mathrm P\)-completeness of counting independent sets are established prior notions and are used as ingredients, not claimed as independently discovered here. Results for independent (rather than **outer-independent**) rainbow domination constrain the opposite label class and do not directly enumerate these functions.

## Limitations

This result enumerates **minimum-weight** functions, not all admissible outer-independent two-rainbow functions. For \(k=1\), different phenomena occur and no classification is claimed here. The counting-hardness proof supplies a polynomial-time **Turing** reduction, not a parsimonious many-one reduction or a bounded-degree hardness theorem. This proof and computation have not undergone independent external validation. Priority may be affected by hard-to-index or otherwise inaccessible literature, particularly complete versions of earlier corona-product papers; the accessible primary comparison supports but cannot guarantee global novelty.

## References

1. B. Samadi and N. Soltankhah, *Further results on outer independent 2-rainbow dominating functions of graphs*, arXiv:2208.02340, first posted 2022-08-03; revision of 2023-01-29, particularly Section 3.2, Theorem 3.4. https://arxiv.org/abs/2208.02340
2. A. Cabrera-Martínez, *A Note on Outer-Independent 2-Rainbow Domination in Graphs*, Mathematics 10 (2022), 2287, published 2022-06-30. DOI: 10.3390/math10132287.
3. Q. Kang, V. Samodivkin, Z. Shao, S. M. Sheikholeslami, and M. Soroudi, *Outer-independent k-rainbow domination*, Journal of Taibah University for Science 13 (2019), 883–891.
4. J. S. Provan and M. O. Ball, *The Complexity of Counting Cuts and of Computing the Probability that a Graph is Connected*, SIAM Journal on Computing 12 (1983), 777–788. DOI: 10.1137/0212053.
