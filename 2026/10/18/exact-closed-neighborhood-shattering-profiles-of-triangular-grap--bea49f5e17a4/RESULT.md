# Exact closed-neighborhood shattering profiles of triangular graphs

## Finding

Let \(n\ge 2\), and let the triangular graph \(T_n=J(n,2)=L(K_n)\) have as vertices the two-element subsets of \([n]\). Its radius-one *closed* neighborhoods form the set system
\[
\mathcal N_n=\{N_{T_n}[f]:f\in\tbinom{[n]}2\},\qquad
N_{T_n}[f]=\{e\in\tbinom{[n]}2:e\cap f\ne\varnothing\}.
\]
A set \(A\subseteq\binom{[n]}2\) is **shattered** if every subset of \(A\) is of the form \(A\cap N_{T_n}[f]\) for some two-element set \(f\subseteq[n]\). View \(A\) as the edge set of a simple graph \(H_A\) on its nonisolated endpoints, and write \(v(A)=|V(H_A)|\).

**Complete structural classification.** A nonempty \(A\) is shattered exactly when \(n\ge v(A)+2\) and \(H_A\) is one of these six types, with isolated vertices omitted:

1. one edge;
2. a two-edge path;
3. two disjoint edges;
4. a three-edge star;
5. a two-edge path disjoint from a single edge;
6. two disjoint two-edge paths.

No shattered set has more than four elements. Writing \(s_j(n)\) for the number of shattered \(j\)-sets, the complete profile is
\[
\begin{aligned}
s_0(n)&=1,\\
s_1(n)&=\mathbf 1_{n\ge4}\binom n2,\\
s_2(n)&=3\mathbf1_{n\ge5}\binom n3+3\mathbf1_{n\ge6}\binom n4,\\
s_3(n)&=4\mathbf1_{n\ge6}\binom n4+30\mathbf1_{n\ge7}\binom n5,\\
s_4(n)&=90\mathbf1_{n\ge8}\binom n6,\\
s_j(n)&=0\quad(j\ge5).
\end{aligned}
\]
Here \(\mathbf1_{n\ge r}\) equals one when \(n\ge r\) and zero otherwise. Therefore the *shattering polynomial* is exactly \(\sum_{j=0}^4s_j(n)t^j\), and
\[
\operatorname{VCdim}(T_n,\mathcal N_n)=
\begin{cases}
0&n=2,3,\\
1&n=4,\\
2&n=5,\\
3&n=6,7,\\
4&n\ge8.
\end{cases}
\]
The distinction between closed and open neighborhoods is mathematically consequential: the open-neighborhood edge relation already has VC dimension four on \(J(7,2)\) by Adler–Benediktsson–Macpherson (Theorem 3.7), whereas the closed-neighborhood system here first reaches four at \(n=8\).

## Assumptions and scope

The underlying graph is the ordinary finite simple complete graph \(K_n\). Its line graph \(T_n\) uses intersection of distinct edges as adjacency; the neighborhoods in this statement *include* the center edge. Shattering is by *all* such closed neighborhoods, not the corresponding open neighborhoods, neighborhoods in an induced subgraph, or sets centered at arbitrary vertex subsets. Counts are for unlabelled selected edge *sets on the labelled ground set* \([n]\), without dividing by graph automorphisms. There is no stochastic hypothesis. The primary classification is in the model theory of finite graph structures, for the quantifier-free relation \(E(x,y)\lor(x=y)\).

## Proof

**Trace lemma.** For any vertex \(u\) of \([n]\), write \(\operatorname{st}_A(u)=\{e\in A:u\in e\}\). For any two distinct ground vertices \(u,v\), the closed-neighborhood trace is
\[
A\cap N_{T_n}[\{u,v\}]=\operatorname{st}_A(u)\cup\operatorname{st}_A(v).
\]
If \(A\ne\varnothing\) is shattered, the empty trace requires a center \(\{u,v\}\) with neither vertex in \(V(H_A)\), so \(n\ge v(A)+2\). Conversely, if this inequality holds, two unused vertices allow empty traces and one unused vertex pads any desired single star. It follows that \(A\) is shattered if and only if (a) \(n\ge v(A)+2\) and (b) **every subset of its edges is a union of at most two vertex stars in \(H_A\)**.

**Necessity of star components.** Fix an edge \(e=\{a,b\}\in A\). Since the singleton trace \(\{e\}\) occurs, at least one center endpoint incident to \(e\) has a nonempty star contained in \(\{e\}\). Thus \(a\) or \(b\) has degree exactly one in \(H_A\). Every edge of \(H_A\) therefore touches a degree-one vertex. Every nontrivial connected component must be a star: otherwise two vertices of degree at least two are connected by a path whose initial or final internal edge has two nonleaf endpoints (equivalently, delete the leaves and observe that there can be no remaining edge). Hence \(H_A\) is a star forest.

**Restriction on stars.** If a component is a star with at least four edges, choosing exactly three edges of that component produces a trace requiring three distinct leaves: its center cannot be used, because it brings along an unwanted fourth edge. This contradicts the two-star trace lemma. Thus every star component has at most three edges.

The full-edge trace \(A\) requires at most two stars and therefore at most two nontrivial components. If there are two components and one has three edges, the set comprising exactly two edges from that component and one edge from the other needs at least three selected vertices: two leaves of the three-star, and one vertex from the second component. This is again impossible. Therefore either there is one star with one, two, or three edges, or there are two stars each having one or two edges. These are precisely the six listed types.

**Sufficiency.** In a single star with at most three edges, every proper subset is the union of at most two leaf stars, and the whole set is one center star. In two star components, each of size at most two, the selected edges from each component are either empty, a single leaf star, or the full center star. Thus every selected subset uses at most one vertex star per component, hence at most two total. With two unused ambient vertices, the trace lemma realizes all subsets by genuine centers from \(\binom{[n]}2\). This proves the classification, including all small-parameter boundaries and the global size-four bound.

**Counting.** A single edge has \(\binom n2\) placements. A two-edge path has \(3\binom n3\), while two disjoint edges have \(3\binom n4\). A three-edge star has \(4\binom n4\); a two-edge path plus a disjoint edge has \(3\binom n3\binom{n-3}2=30\binom n5\). Finally, two disjoint two-edge paths use six vertices, which can be divided into two unordered three-vertex blocks in \(\binom63/2=10\) ways, followed by three choices of center in each block, giving \(90\binom n6\). The constraint of two unused vertices applies to each placement and gives precisely the indicated thresholds. All other coefficients vanish by the classification.

For \(n=2,3\), every closed ball includes all vertices of \(T_n\), so no nonempty set is shattered. For larger \(n\), the thresholds of the six types directly imply the stated VC-dimension formula. The boundary \(n=7\) versus \(n=8\) follows because a shattered four-set must have two disjoint two-edge paths on six ground vertices *and* two unused ground vertices. All claims follow.

## Verification

The standalone file `verify_shattering.py` enumerates all two-element centers and their actual closed-neighborhood traces. Independently of the proof's star-union argument, it tests every candidate set of sizes zero through five for \(2\le n\le9\), and sizes zero through four for \(n=10\), comparing direct trace realization with the six isomorphism types and all coefficient formulas. To reproduce from a directory containing that file, execute `python verify_shattering.py`. The run checked 763,914 candidate subsets without an assertion failure. In particular, the exhaustive size-five checks over all selected five-edge sets for \(n\le9\) corroborate the claimed ceiling; the *proof*, not the finite enumeration, covers all \(n\).

## Relationship to prior work

Adler, Benediktsson, and Macpherson (arXiv:2007.16042, first public 2020-07-31; journal version 2022), Theorems 3.6–3.7 and Figure 4, prove the sharp **open-neighborhood** VC-dimension four for Johnson graphs, including the four-point example in \(J(7,2)\). Their abstract observes boundedness of the closed-neighborhood variant. Their Johnson-graph section studies the open edge relation rather than the six-type classification and all closed-neighborhood shattering coefficients obtained here. This result must not be described as a new open-neighborhood bound.

Bousquet et al. (arXiv:1407.5833, first public 2014-07-22) define graph VC dimension via closed neighborhoods and establish general connections with identifying codes. Their main statements concern hereditary graph classes, bounds and approximation, not exact profiles for triangular graphs. Coudert et al. (arXiv:2405.07588, first public 2024-05-13) give general practical algorithms and bounds for graph VC dimension, rather than this structural closed-neighborhood classification.

The general combinatorics of VC shattering, and the equivalence \(J(n,2)=L(K_n)\), are established facts. The present claim is the specific six-type theorem, complete coefficient enumeration, and the exact shift in the threshold at which the closed-neighborhood VC dimension becomes four. Searches under line-graph, triangular-graph, two-star trace, shattering-polynomial and radius-one Johnson-ball formulations did not identify a covering statement. That negative search result is not a proof of publication priority.

## Limitations

The theorem concerns only rank-two Johnson graphs \(J(n,2)\) and genuine **closed** radius-one neighborhoods. It does not classify all higher-rank Johnson graphs, open-neighborhood traces, or arbitrary line graphs. The manuscript gives an ordinary mathematical proof and finite corroborating calculations, not a formal proof certificate or independent external audit. An equivalent classification under alternate graph-theoretic terminology could remain in the literature; the priority assessment is limited to inspected sources.

## References

1. I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, v1 2020-07-31. https://arxiv.org/abs/2007.16042 . Relevant primary text: Theorems 3.6–3.7, Figure 4, and the abstract's closed-neighborhood qualification.
2. N. Bousquet, A. Lagoutte, Z. Li, A. Parreau, S. Thomassé, *Identifying codes in hereditary classes of graphs and VC-dimension*, arXiv:1407.5833, 2014-07-22. https://arxiv.org/abs/1407.5833 . Relevant primary text: Introduction and Section 1.2.
3. D. Coudert, M. Csikós, G. Ducoffe, L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588, 2024-05-13. https://arxiv.org/abs/2405.07588 . Relevant primary text: Sections 1–2.
