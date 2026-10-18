# Heterogeneous clique bouquets: zero-forcing polynomial recognition and a universal random threshold

## Finding

Let \(G=K_1\vee(K_{r_1}\sqcup\cdots\sqcup K_{r_t})\), where \(t\ge1\) and each integer \(r_i\ge2\). The hub is adjacent to all peripheral vertices, and distinct peripheral cliques have no edges between them. Write \(s=\sum_{i=1}^t(r_i-1)\), \(C=\prod_{i=1}^tr_i\), and \(N=1+\sum_i r_i\).

**Theorem.** Every ordinary zero-forcing set meets each peripheral clique in at least \(r_i-1\) vertices and, in addition, either contains the hub or fully contains at least one peripheral clique. Conversely, every set meeting those conditions is zero forcing. Thus the complete size-generating polynomial is
\[\mathcal Z_G(z)=z^s\left((1+z)\prod_{i=1}^t(z+r_i)-C\right).\]
Its initial exponent and coefficient yield
\[Z(G)=s+1=N-t,\qquad z(G;Z(G))=C\left(1+\sum_{i=1}^t\frac1{r_i}\right).\]

**Recognition.** The ordinary zero-forcing polynomial determines the full multiset \(\{r_1,\ldots,r_t\}\) and therefore determines the graph up to isomorphism *within this class*. Explicitly, read \(s\) as the least exponent in \(\mathcal Z_G\) minus one. With \(H(z)=z^{-s}\mathcal Z_G(z)\), one has
\[\prod_{i=1}^t(z+r_i)=\frac{H(z)-H(-1)}{z+1}.\]
Its negative integer roots, with multiplicities, reconstruct the peripheral clique sizes. No recognition claim is made among arbitrary graphs outside this class.

**Random forcing.** If each vertex is initially blue independently with probability \(p\), the exact forcing-success probability is
\[P_G(p)=\prod_{i=1}^t\bigl[p^{r_i}+r_i p^{r_i-1}(1-p)\bigr]-(1-p)\prod_{i=1}^t r_i p^{r_i-1}(1-p).\]
For a sequence of size profiles indexed by \(m\), put \(L_m=\sum_i\binom{r_{m,i}}2\). Suppose \(L_m\to\infty\) and \(R_m=\max_i r_{m,i}=o(\sqrt{L_m})\). Then, for every fixed \(\lambda\ge0\) and \(p_m=1-\lambda/\sqrt{L_m}\),
\[P_{G_m}(p_m)\longrightarrow e^{-\lambda^2}.\]
The number of peripheral cliques containing at least two initially white vertices converges in distribution to a Poisson random variable of mean \(\lambda^2\). If \(p_{1/2,m}\) is the unique probability at which forcing success has probability \(1/2\), then
\[\sqrt{L_m}\,(1-p_{1/2,m})\longrightarrow\sqrt{\log2}.\]

## Assumptions and scope

Graphs are finite, simple, undirected, and labeled when counting subsets. The hub is a single vertex; all peripheral clique sizes are at least two. Zero forcing means the ordinary blue-vertex rule: a blue vertex with exactly one white neighbor may force that neighbor blue. The polynomial counts *all* successful initial subsets, not only minimum subsets. The asymptotic statement permits arbitrarily different peripheral clique sizes, subject to its stated maximal-size condition; it does not claim universality when a single clique dominates \(L_m\). The random model selects initially blue vertices independently and then applies the deterministic forcing rule.

## Proof

**Exact admissibility.** If at least two peripheral vertices in the same clique start white, their remaining blue neighbors are identical outside this pair: all other vertices in that clique and the hub. Neither white vertex can ever be the unique white neighbor of a blue vertex until one is forced, so neither can be the first of the pair to turn blue. The two-vertex white set is a permanent forcing obstruction, establishing necessity of at most one white vertex per clique.

Assume at most one white vertex per peripheral clique. If the hub is blue, each missing peripheral vertex is the only white neighbor of any initially blue vertex in its clique. There is at least one blue vertex in each clique because \(r_i\ge2\). Such vertices force every peripheral omission. If the hub is white but some peripheral clique is entirely blue, any vertex of that clique forces the hub; the previous argument completes the forcing. If the hub is white and every peripheral clique has exactly one white vertex, no initially blue vertex has exactly one white neighbor (each has its clique's white vertex and the hub); the process cannot start. This proves both necessity and sufficiency.

**Polynomial and minimum count.** A peripheral clique of size \(r_i\) with at most one vertex omitted contributes \(z^{r_i}+r_i z^{r_i-1}=z^{r_i-1}(z+r_i)\); the condition that every peripheral clique omit exactly one vertex contributes \(\prod_i r_i z^{r_i-1}=Cz^s\). Sets including the hub are enumerated by \(z\prod_i z^{r_i-1}(z+r_i)\). Sets omitting the hub are enumerated by the peripheral product minus the all-one-omission term. Adding gives the asserted polynomial. Its term of degree \(s\) cancels exactly and its degree-\(s+1\) coefficient is \(C+C\sum_i 1/r_i>0\), proving the exact minimum and minimum-set count, including \(t=1\).

**Recognition.** The polynomial has valuation \(s+1\) and hence determines \(s\). Let \(Q(z)=\prod_i(z+r_i)\); then \(H(z)=(z+1)Q(z)-Q(0)\). Evaluating at \(z=-1\) yields \(H(-1)=-Q(0)\), and rearrangement gives \(Q(z)=(H(z)-H(-1))/(z+1)\). Since \(Q\) factors as monic linear factors with negative integer roots, its multiset of roots uniquely determines \(\{r_i\}\). This is also constructive for profiles with repeated sizes.

**Critical window.** Let \(\varepsilon=1-p\), \(a_i=p^{r_i}+r_i p^{r_i-1}\varepsilon\), and \(b_i=r_i p^{r_i-1}\varepsilon\). The exact admissibility condition gives \(P_G(p)=\prod_i a_i-\varepsilon\prod_i b_i\). Here \(a_i\) is the probability that peripheral clique \(i\) initially contains at most one white vertex. For \(\varepsilon_m=\lambda/\sqrt{L_m}\), the uniform condition \(\max_i r_{m,i}\varepsilon_m=o(1)\) yields
\[1-a_i=\binom{r_i}{2}\varepsilon_m^2+O(r_i^3\varepsilon_m^3).\]
The sum of the leading terms equals \(\lambda^2\), while the total remainder is bounded by a constant times \(R_m L_m\varepsilon_m^3=o(1)\). Also \(\max_i(1-a_i)=O(R_m^2\varepsilon_m^2)=o(1)\), so \(\sum_i(1-a_i)^2=o(1)\). Taking logarithms gives \(\prod_i a_i\to e^{-\lambda^2}\). Meanwhile \(0\le b_i\le r_i\varepsilon_m=o(1)\), so \(\varepsilon_m\prod_i b_i\to0\). For \(\lambda=0\), this conclusion is immediate.

Let \(Y_m\) count peripheral cliques with two or more initially white vertices. The cliques are independent and have failure probabilities \(d_i=1-a_i\). For each fixed \(u\in[0,1]\),
\[\mathbb E[u^{Y_m}]=\prod_i(1-(1-u)d_i)\longrightarrow e^{\lambda^2(u-1)},\]
the probability generating function of Poisson\((\lambda^2)\); hence \(Y_m\) has the claimed distributional limit. Finally \(P_G(p)\) is continuous and strictly increasing on \((0,1)\) (it counts an increasing nontrivial property of independently retained vertices), so its median is unique. Bracketing \(\lambda=\sqrt{\log2}\) by nearby constants and using the pointwise limit proves the stated median-threshold asymptotic.

## Verification

`verify_clique_bouquets.py` is standalone Python using only the standard library. It independently builds graph neighborhoods and simulates ordinary forcing for every initial subset of 38 profiles consisting of up to three peripheral cliques of sizes two through four and at most twelve total vertices. It tests the structural if-and-only-if condition, every polynomial coefficient, and exact recovery of the peripheral product polynomial by the displayed recognition formula. The checker enumerated 37,336 candidate subsets and also calculated numerical finite-size values in three fixed-clique families; `verification_output.txt` records its actual output. The analytic proof, not finite enumeration, establishes the all-size and asymptotic statements.

## Relationship to prior work

Boyer et al. (2018, arXiv:1801.08910) define and investigate zero-forcing polynomials; their main graph formulas include complete graphs, complete multipartite graphs, paths, cycles, wheels and threshold graphs. Curtis et al. (2022, arXiv:2208.12899) introduce random-initial-set zero-forcing thresholds and study several graph families including paths, cycles and wheels. Neither inspected paper states the heterogeneous clique-bouquet recognition formula or the heterogeneous critical-window law. A previously indexed result, “Zero forcing polynomial of friendship graphs” (published-finding corpus identifier ending `b77605779c1b`), **already covers the special case when every peripheral clique has size two**: its polynomial agrees exactly with the specialization of the present formula. This known special case is not asserted as new. Skew zero forcing uses a different forcing rule and does not by itself imply the ordinary-forcing recognition or random-threshold claims. Scalar zero-forcing numbers for broader block graphs are also studied in later literature; recovering the scalar number alone is not claimed as original.

## Limitations

Novelty and priority remain subject to potentially unindexed or inaccessible equivalent research, particularly all-set forcing formulas on block graphs; the accessible indexed friendship result establishes prior coverage of one important special case. The proof does not apply to one-vertex peripheral parts and does not establish a limiting law without the maximal-clique-size condition. The graph-recognition assertion is restricted to the specified family, not arbitrary graphs. Finite checks do not certify the infinite proof. Independent scientific audit has not been performed.

## References

1. Bryan Curtis, Luyining Gan, Jamie Haddock, Rachel Lawrence, Sam Spiro, *Zero Forcing with Random Sets*, arXiv:2208.12899v1, publicly submitted 27 August 2022, https://arxiv.org/abs/2208.12899.
2. Kirk Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910v1, publicly submitted 26 January 2018, https://arxiv.org/abs/1801.08910.
3. *Zero forcing polynomial of friendship graphs*, prior indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-zero-forcing-polynomial-of-friendship-graphs--b77605779c1b.
