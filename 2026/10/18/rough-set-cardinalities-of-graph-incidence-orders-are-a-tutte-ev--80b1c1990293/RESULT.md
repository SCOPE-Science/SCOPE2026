# Rough-set cardinalities of graph-incidence orders are a Tutte evaluation

## Finding

**Theorem (height-two counting and graph correspondence).** Let \(P=A\sqcup B\) be a finite poset with all elements of \(A\) minimal and all elements of \(B\) maximal, and with strict comparabilities only of the form \(a<b\), \(a\in A\), \(b\in B\). Set \(N(a)=\{b\in B:a<b\}\). For each \(S\subseteq P\), let \[L_P(S)=\{x\in P:\uparrow x\subseteq S\},\qquad U_P(S)=\{x\in P:\uparrow x\cap S\ne\varnothing\}.\] Here \(\uparrow x=\{y:x\le y\}\) includes \(x\). Define \(R(P)=|\{(L_P(S),U_P(S)):S\subseteq P\}|\). Then

\[
R(P)=\sum_{T\subseteq B}2^{m(T)},\qquad
m(T)=\bigl|\{a\in A:N(a)\subseteq T\ \text{or}\ N(a)\cap T=\varnothing\}\bigr|.
\]

An element with \(N(a)=\varnothing\) contributes to \(m(T)\) for every \(T\). This identity also holds when \(A\) or \(B\) is empty, with the empty sum and empty product conventions.

Let \(G=(V,E)\) be any finite simple undirected graph. Its **dual incidence poset** \(P_G\) has a maximal element for each \(v\in V\) and a minimal element for each \(e=\{u,v\}\in E\), with \(e<u,e<v\). Then

\[
\boxed{R(P_G)=\sum_{T\subseteq V}2^{|E(G[T])|+|E(G[V\setminus T])|}
=\sum_{F\subseteq E}2^{k(V,F)}
=2^{k(G)}T_G(3,2).}
\]

Here \(k(G)\) denotes the number of connected components, including isolated vertices, and \(T_G(x,y)\) is the standard graphic Tutte polynomial. The spin sum is the partition function of the two-state ferromagnetic Potts model at random-cluster edge weight one. The identities also extend to finite multigraphs if every edge occurrence is given its own incidence point; loops have just one upper endpoint.

**Corollaries.** If \(e\) is an edge with distinct endpoints, then \(R(G)=R(G-e)+R(G/e)\), with contraction interpreted as a multigraph. For a loop, \(R(G)=2R(G-e)\). Adding an isolated vertex doubles \(R\). Consequently, for trees with \(n\ge1\) vertices, \(R=2\cdot 3^{n-1}\); for simple cycles with \(n\ge3\), \(R=3^n+1\); and for \(K_n\), \[R(K_n)=\sum_{j=0}^{n}\binom nj2^{\binom j2+\binom{n-j}2}.\] In particular \(R(K_2)=6\), \(R(K_3)=28\), \(R(K_4)=216\), \(R(K_5)=3008\).

**Counting-complexity consequence (using established theorems).** The function \(G\mapsto R(P_G)\) belongs to \(\#\mathrm P\): a witness consists of a two-coloring of \(V\) and a selected set of monochromatic edges. It is \(\#\mathrm P\)-hard under polynomial-time Turing reductions because \(R(P_G)=2^{k(G)}T_G(3,2)\), and the fixed-point Tutte evaluation \((3,2)\) lies in the hard region of the Jaeger–Vertigan–Welsh classification. For planar \(G\), the same counting problem is polynomial-time computable by the zero-field planar Ising/Pfaffian algorithm; the graph-size distinction does not require a new complexity theorem.

## Assumptions and scope

The poset is finite, reflexive and antisymmetric, with order orientation specified above. Approximations use **upward** principal neighborhoods (and therefore need not match a paper using downward neighborhoods without order duality). \(R(P)\) counts **distinct ordered approximation pairs**, not the number of subsets that generate them and not just the number of upper or lower approximation sets. The graph correspondence counts labeled incidence points for the edges, but only the number of distinct rough pairs, not graph labelings. Every assertion uses exact integer cardinalities. The two-state model has no external magnetic field and equal spin weights. The planar algorithm is an exact rational/integer computation, not approximate sampling.

## Proof

Fix \(T=S\cap B\). Each maximal element \(b\in B\) has \(\uparrow b=\{b\}\), so its lower and upper approximation indicators both equal \(1_{b\in T}\). Consequently a rough pair uniquely determines \(T\), and contributions from different \(T\) cannot collide.

For a minimal point \(a\), write \(h=N(a)\) and \(s=1_{a\in S}\). Then \(\uparrow a=\{a\}\cup h\), so the lower indicator is \(s\wedge[ h\subseteq T]\), and the upper indicator is \(s\vee[ h\cap T\ne\varnothing]\). If \(h\subseteq T\) and \(h\ne\varnothing\), the two possible values as \(s\) changes are \((0,1)\) and \((1,1)\). If \(h\cap T=\varnothing\) and \(h\ne\varnothing\), they are \((0,0)\) and \((0,1)\). If \(h\) meets both \(T\) and its complement, the only possibility is \((0,1)\), regardless of \(s\). For \(h=\varnothing\), the two possible values are \((0,0)\) and \((1,1)\). Thus a minimal point contributes two distinct local rough statuses exactly when all its upper neighbors have the same binary color, counting an empty neighborhood as monochromatic. Values at different minimal points can be chosen independently by choosing their individual membership bits; statuses for different such choices are distinct. This proves the general product/sum formula.

For \(P_G\), a minimal point has the two endpoints of its edge as neighbors. For a fixed \(T\subseteq V\), such a point is monochromatic exactly when both endpoints lie in \(T\) or both lie in \(V\setminus T\). The exponent is therefore \(|E(G[T])|+|E(G[V\setminus T])|\), proving the first graph formula. For each two-coloring \(\sigma:V\to\{0,1\}\), the factor contributed by \(e=uv\) is \(2^{[\sigma(u)=\sigma(v)]}=1+[\sigma(u)=\sigma(v)]\). Expanding the product over edges gives

\[
R(P_G)=\sum_{F\subseteq E}\sum_{\sigma:V\to\{0,1\}}
\prod_{uv\in F}[\sigma(u)=\sigma(v)]
=\sum_{F\subseteq E}2^{k(V,F)},
\]

since \(\sigma\) must be constant on the connected components of \((V,F)\). The subset expansion of the Tutte polynomial reads

\[
T_G(x,y)=\sum_{F\subseteq E}(x-1)^{k(V,F)-k(G)}(y-1)^{|F|-|V|+k(V,F)}.
\]

Substitution \((x,y)=(3,2)\) proves the third equality. The deletion–contraction recurrence follows by partitioning \(F\subseteq E\) according to the presence or absence of the selected edge; a loop creates an independent factor two. The tree formula follows by using \(k(V,F)=n-|F|\) for every edge subset of a tree. For a cycle \(C_n\), every proper edge subset is a forest, while the full edge set has one component: \(\sum_{j=0}^{n-1}\binom nj2^{n-j}+2=3^n+1\). For a complete graph, a two-coloring with \(j\) points of color one has \(\binom j2+\binom{n-j}2\) monochromatic edges, and there are \(\binom nj\) such colorings.

Finally, a nondeterministic counting machine can guess a vertex coloring and then an edge subset, accepting exactly when each chosen edge is monochromatic. This yields one accepting branch per allowed pair and proves membership in \(\#\mathrm P\). The hardness and planar tractability statements are direct, identified applications of existing fixed-point Tutte and planar Ising classifications; they are not derived from the finite experiments below.

## Verification

The standalone `verify.py` uses only the Python standard library and exact integers. It directly enumerates all subsets of each finite height-two incidence model, computes both approximations, and deduplicates resulting ordered pairs. Independently it evaluates the monochromatic-neighborhood sum. For graph examples it separately sums connected-component weights over edge subsets and checks deletion–contraction. Run `python3 verify.py` in the same directory.

The executed checks covered 689 height-two neighborhood families (37,477 direct subset cases), every one of the 76 simple graphs on at most four vertices, 108 multigraph/loop deletion–contraction cases, and the tree, cycle, and complete-graph formulas through eight vertices. All passed. These finite checks **do not** establish the all-graph statements or complexity results; those follow from the proof and cited prior theorems.

## Relationship to prior work

Järvinen and Radeleczki (2020) characterize three-valued core/support representations of quasiorder rough sets; their introduction records an earlier representation of quasiorder rough pairs as constrained pairs of approximations. Their result supports the definitions and structural framework, but the inspected introduction, preliminaries, and representation discussion do not explicitly identify graph-incidence cardinality with the two-state Potts partition function or give the resulting planar/unrestricted complexity split. Their later work (2023) focuses on pseudo-Kleene algebra structure rather than this graph cardinality specialization. The Fortuin–Kasteleyn expansion, Tutte polynomial, fixed-point complexity classification, and planar zero-field Ising algorithms are established results. The contribution here is the specific all-height-two counting formula, its exact graph-incidence reduction to these established invariants, and the induced sharp computational contrast for **rough-set cardinality**. The statement is not a new theorem about the Tutte polynomial itself.

## Limitations

The fully explicit cardinality product holds for height-two orders with the stated orientation. General quasiorders with longer chains can have nonlocal constraints and are not covered. The graph construction is specialized to edge-neighborhood incidence, not every arbitrary rough-set information system. The complexity statements use polynomial-time Turing reductions and exact planar zero-field models, not a claim about approximation hardness or arbitrary weighted fields. An implicit equivalent graph specialization in earlier rough-set lattice literature cannot be ruled out without broader expert bibliographic review; independent validation and publication-priority certification have not been performed.

## References

1. J. Järvinen and S. Radeleczki, *Defining rough sets as core–support pairs of three-valued functions*, first publicly posted 2020-11-06, arXiv:2011.03461. https://arxiv.org/abs/2011.03461
2. J. Järvinen and S. Radeleczki, *Pseudo-Kleene algebras determined by rough sets*, arXiv:2304.05641 (2023). https://arxiv.org/abs/2304.05641
3. F. Jaeger, D. L. Vertigan and D. J. A. Welsh, *On the computational complexity of the Jones and Tutte polynomials*, Mathematical Proceedings of the Cambridge Philosophical Society (1990), DOI:10.1017/S0305004100068936. https://doi.org/10.1017/S0305004100068936
4. D. Vertigan, *The computational complexity of Tutte invariants for planar graphs*, SIAM Journal on Computing (2005), DOI:10.1137/S0097539704446797. https://doi.org/10.1137/S0097539704446797
