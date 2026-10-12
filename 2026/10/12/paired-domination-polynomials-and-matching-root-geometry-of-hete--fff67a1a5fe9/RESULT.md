# Paired-domination polynomials and matching-root geometry of heterogeneous leaf coronas

## Finding
Let \(G=(V,E)\) be any finite simple graph with \(n=|V|\ge1\), and let \(r_v\) be a positive integer for each \(v\in V\). Form \(H\) by adjoining \(r_v\) private degree-one leaves adjacent to each \(v\). The paired-domination polynomial \(D_{\mathrm{pr}}(H;x)\) counts vertex subsets that dominate \(H\) and whose induced subgraph admits a perfect matching, by subset size.

A set \(U\subseteq V\) is *perfectly matchable* if \(G[U]\) has a perfect matching, counting the empty set as perfectly matchable. Then
\[
\boxed{D_{\mathrm{pr}}(H;x)=\sum_{\substack{U\subseteq V\\G[U]\text{ has a perfect matching}}} x^{2n-|U|}\prod_{v\in V\setminus U}r_v.}
\]
Every paired-dominating set is uniquely represented by such a \(U\) together with one choice of a private leaf at each \(v\in V\setminus U\). Equivalently, for uniform \(r_v=r\), if \(p(G;t)=\sum_{k\ge0}p_{2k}(G)t^k\) counts perfectly matchable \(2k\)-vertex subsets once each, then
\[
D_{\mathrm{pr}}(H;x)=r^n x^{2n}p\!\left(G;\frac{1}{r x^2}\right).
\]

**Root-location consequence.** If \(G\) contains no even cycle, then every nonzero complex zero of \(D_{\mathrm{pr}}(H;x)\) lies on the imaginary axis, for every choice of the positive integers \(r_v\). In fact, with \(\nu(G)\) the maximum matching size, there are positive real numbers \(\lambda_1,\ldots,\lambda_{\nu(G)}\), counted with multiplicity, such that
\[
D_{\mathrm{pr}}(H;x)=\left(\prod_{v\in V}r_v\right)
 x^{2n-2\nu(G)}\prod_{j=1}^{\nu(G)}(x^2+\lambda_j).
\]
Hence \(\gamma_{\mathrm{pr}}(H)=2n-2\nu(G)\), and the multiplicity of zero as a polynomial root is exactly this minimum cardinality.

## Assumptions and scope
All graphs are finite, simple, and undirected. The base graph may be disconnected or have isolated vertices. All leaf multiplicities satisfy \(r_v\in\{1,2,\ldots\}\); the attached vertices are pairwise distinct and have degree one. A perfect matching of an empty induced graph is the empty matching. A paired-dominating set is counted once, even if its induced subgraph has several perfect matchings; this convention is essential.

For an ordinary base matching \(M\subseteq E\), write \(V(M)\) for its set of endpoints. The root-location assertion is one-directional: absence of even cycles is a sufficient condition, not claimed necessary. A graph with only odd cycles and bridges is included. The polynomial identity itself holds for every base graph, with or without even cycles.

## Proof
**Step 1: all base vertices must be selected.** Let \(S\) dominate \(H\) and suppose \(H[S]\) has a perfect matching. Fix a base vertex \(v\) and any one of its private leaves \(\ell\). If \(v\notin S\) and \(\ell\notin S\), then \(\ell\) is not dominated. If \(v\notin S\) and \(\ell\in S\), then \(\ell\) is isolated in \(H[S]\), contrary to the perfect matching. Thus \(V\subseteq S\).

**Step 2: at most one private leaf may be selected at each base vertex.** In any perfect matching of \(H[S]\), each selected private leaf at \(v\) must be matched to \(v\). Distinct leaves cannot share a matching partner. Hence each \(v\) contributes either zero or exactly one selected leaf.

**Step 3: the exact bijection.** Let \(U\subseteq V\) be the base vertices whose private leaves are not selected. Every \(v\notin U\) is matched to its selected private leaf in any perfect matching of \(H[S]\). The remaining selected vertices are precisely \(U\), and their matching edges lie entirely in \(G[U]\). Therefore \(G[U]\) must have a perfect matching. Conversely, take any perfectly matchable \(U\), choose one among the \(r_v\) private leaves at every \(v\notin U\), and take \(S\) to consist of all of \(V\) and these chosen leaves. Every unselected leaf is dominated by its base vertex. A perfect matching of \(G[U]\), together with the selected pendant edges at \(V\setminus U\), covers \(S\). The choices are uniquely recoverable from \(S\).

There are \(\prod_{v\notin U}r_v\) leaf-choice possibilities, each with \(|S|=n+(n-|U|)=2n-|U|\), which proves the sum. If all multiplicities equal \(r\), grouping perfectly matchable subsets by \(|U|=2k\) gives the displayed substitution formula. A maximum matching of \(G\) has \(\nu(G)\) edges, so a largest perfectly matchable set has size \(2\nu(G)\), proving the asserted minimum cardinality and its zero multiplicity.

**Step 4: weighted matching form when there is no even cycle.** The symmetric difference of two distinct perfect matchings on the same vertex set contains an even alternating cycle. Thus, if \(G\) has no even cycle, every perfectly matchable set has exactly one perfect matching and conversely every matching produces a distinct endpoint set. With \(R=\prod_{v\in V}r_v\) and positive edge weights \(w_{uv}=1/(r_u r_v)\), the sum becomes
\[
D_{\mathrm{pr}}(H;x)=R x^{2n}
\sum_{M\text{ matching in }G}
\left(\prod_{uv\in M}w_{uv}\right)x^{-2|M|}.
\]
The weighted matching generating polynomial \(m_w(t)=\sum_M(\prod_{e\in M}w_e)t^{|M|}\) has degree \(\nu(G)\), constant term \(1\), and only strictly negative real zeros, by the weighted Heilmann–Lieb matching-polynomial theorem. It factors as \(\prod_{j=1}^{\nu(G)}(1+\lambda_j t)\) for positive real \(\lambda_j\). Substituting \(t=x^{-2}\) and clearing denominators produces the product formula and proves the imaginary-axis root statement. When \(\nu(G)=0\), the product is empty and there are no nonzero roots.

## Verification
The included `verify.py` uses no external packages. It constructs each decorated graph explicitly and independently enumerates all selected subsets; domination is checked against its adjacency lists, and existence of a perfect matching is decided by a recursive Boolean search. These direct counts are compared with the perfectly matchable-subset weighted formula.

A successful run checked 2,174 graph-and-multiplicity instances and 3,401,516 candidate subsets. The fully exhaustive families are every labeled base graph on at most four vertices with each multiplicity equal to one or two, and all labeled base graphs on five vertices with one leaf per base vertex. The remaining five- and six-vertex heterogeneous examples are a fixed sample, not an exhaustive census. The script also contrasts the one perfect vertex support of a four-cycle with its two perfect matchings; these must not be conflated. The finite checks corroborate, but do not prove, the all-graph identity or the root statement; the proof is above.

To reproduce, save the included `verify.py` and run `python verify.py` in Python 3.9 or later. Its standard output is included as `VERIFIER_OUTPUT.txt`.

## Relationship to prior work
Haynes and Slater (1998) introduced paired domination and recorded the minimum-cardinality formula for a single-leaf corona; that scalar equality is prior work, not a new claim here. Ohsugi and Tsuchiya (arXiv:2103.15045v1, 28 March 2021) studied perfectly matchable set polynomials in connection with adjacency polytopes. Davis and Kohl (arXiv:2207.14759v1, 29 July 2022), especially Lemma 3.2, identified exactly when that polynomial equals the ordinary matching enumerator. Heilmann and Lieb's classical theorem gives real-rootedness for weighted matching polynomials.

The result above links those previously separate objects by a bijection for **every** base graph and **heterogeneous** private-leaf multiplicities, thereby producing the complete paired-domination enumerator and a uniform, multiplicity-dependent imaginary-axis root property. The previously established scalar minimum formula, perfectly matchable set polynomials, path and cycle coefficient tables, and Heilmann–Lieb theorem are explicitly credited rather than claimed as new.

## Limitations
The imaginary-axis conclusion is only asserted under the no-even-cycle hypothesis; the general coefficient identity needs no such condition. Counting matching *edges* instead of perfectly matchable vertex *supports* overcounts whenever two perfect matchings use the same vertex set, as happens for a four-cycle. No new complexity bound, universal root-location theorem for arbitrary graphs, or converse to the root theorem is claimed. The relationship may have an unindexed or implicit earlier derivation, particularly in specialized paired-domination polynomial literature; one 2016 article could be examined only through its publicly accessible abstract. Scientific review is not independent validation.

## References
1. T. W. Haynes and P. J. Slater, *Paired-domination in graphs*, Networks 32 (1998), 199–206, DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.
2. H. Ohsugi and A. Tsuchiya, *PQ-type adjacency polytopes of join graphs*, arXiv:2103.15045v1 (28 March 2021), https://arxiv.org/html/2103.15045v1 .
3. R. Davis and F. Kohl, *Perfectly Matchable Set Polynomials and h*-polynomials for Stable Set Polytopes of Complements of Graphs*, arXiv:2207.14759v1 (29 July 2022), https://arxiv.org/html/2207.14759v1 .
4. O. J. Heilmann and E. H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics 25 (1972), 190–232.
5. A. Alwardi, S. R. Nayaka, and Puttaswamy, *Introduction to Paired Domination Polynomial of a Graph*, ICMAGT 2016 (abstract publicly accessible), https://www.researchgate.net/publication/325108045_Introduction_to_Paired_Domination_Polynomial_of_a_Graph .
