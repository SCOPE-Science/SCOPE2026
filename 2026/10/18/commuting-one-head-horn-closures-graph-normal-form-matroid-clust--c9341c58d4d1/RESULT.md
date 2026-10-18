# Commuting one-head Horn closures: graph normal form, matroid clusters, and submodular matchings

## Finding

**Graph--Horn classification.** For every integer \(n\ge 1\), fix a labelled finite set \(V\) of \(n\) propositional variables. Choose exactly one definite Horn rule \(A_v\longrightarrow v\) for every \(v\in V\), with \(A_v\subseteq V\setminus\{v\}\). The associated elementary operator on \(\mathcal P(V)\) is
\[
c_v(X)=\begin{cases}X\cup\{v\},&A_v\subseteq X,\\X,&A_v\not\subseteq X.\end{cases}
\]
The following assertions hold.

1. The \(n\) operators commute pairwise if and only if the premise relation is symmetric: \(u\in A_v\Longleftrightarrow v\in A_u\) for every pair of distinct variables. Thus the commuting systems are uniquely encoded by simple undirected graphs \(G=(V,E)\), with \(A_v=N_G(v)\). There are exactly \(2^{\binom n2}\) such labelled systems, and the combined closure maps are distinct. Every order of applying each elementary operator once gives the same closure
\[
C_G(X)=X\cup\{v\in V:N_G(v)\subseteq X\}.
\]
2. The fixed sets are exactly
\[
\operatorname{Fix}(C_G)=\{X\subseteq V:G[V\setminus X]\text{ has no isolated vertices}\},
\]
where the empty induced graph is deemed to have no isolated vertices. In particular these sets are intersection-closed.
3. \(C_G\) is a matroid closure (satisfies Steinitz exchange) if and only if every component of \(G\) is a clique, including singleton cliques. Each clique component of size \(b\) contributes the uniform matroid \(U_{b-1,b}\), so these systems are in bijection with partitions of \(V\): there are exactly \(B_n\), the \(n\)-th Bell number. Their fixed-set cardinality polynomial is
\[
\sum_{X\in\operatorname{Fix}(C_G)}t^{|X|}=\prod_{K\in\operatorname{Comp}(G)}\big((1+t)^{|K|}-|K|t^{|K|-1}\big).
\]
4. Set \(f_G(X)=0\) for fixed sets and \(f_G(X)=1\) otherwise. The Boolean function \(f_G\) is submodular in the \(\{0,1\}\)-valued lattice sense,
\[
f_G(X\cap Y)\vee f_G(X\cup Y)\le f_G(X)\vee f_G(Y),
\]
if and only if \(G\) is a matching plus isolated vertices. Exactly
\[
I_n=\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n!}{2^j j!(n-2j)!}
\]
labelled commuting systems satisfy this condition, with exponential generating function \(\exp(z+z^2/2)\). For a graph with \(r\) isolated vertices and \(m\) edge components, its fixed-set polynomial is \(t^r(1+t^2)^m\).

The Bell, involution/matching, and graph counts are familiar enumerations; the claimed result is their simultaneous characterization *inside the class of commuting one-head Horn update systems*, including the exact graph representation, order-independence and two independent closure-property thresholds.

## Assumptions and scope

The underlying domain is a finite labelled nonempty Boolean set lattice \(\mathcal P(V)\); each variable has exactly one implication with that variable as a single head, and its premise excludes the head. Empty premises are allowed. Rule activation is ordinary definite Horn forward chaining: \(A_v\to v\) adds \(v\) when \(A_v\subseteq X\). The relation \(u\in A_v\) is tested syntactically on the chosen rule family; no extra rules or additional inferred implications are assumed. A *cluster graph* is a disjoint union of complete graphs. A *matching graph* has maximum degree at most one. Matroid closure means extensive, increasing, idempotent and satisfying the usual exchange axiom: \(y\in C(X\cup\{x\})\setminus C(X)\Rightarrow x\in C(X\cup\{y\})\).

## Proof

**Lemma 1 (two-rule commutation).** For distinct \(u,v\), the operators \(c_u,c_v\) commute on all subsets if and only if \((u\in A_v)\Leftrightarrow(v\in A_u)\). If both cross-memberships are absent, no rule can change the other one's premise, so they commute. If both are present and a rule is not already enabled, the other rule cannot be the sole cause of its activation: to produce \(u\) one must already have \(v\), and conversely. Thus either both addable heads were already enabled on the starting set or the two updates are independent. For necessity, suppose \(u\in A_v\) but \(v\notin A_u\). Set \(X=(A_v\setminus\{u\})\cup A_u\). Neither head belongs to \(X\), \(c_u\) adds \(u\), and this newly enables \(c_v\). In the reverse order \(c_v\) adds nothing, so the two compositions differ on \(X\). The opposite asymmetry is symmetric. This proves the equivalence.

Under pairwise commutation, symmetry of adjacency constructs exactly one undirected simple graph. The \(n\) operators are closure operators individually; their commuting composition is again extensive, increasing and idempotent. More strongly, its explicit formula follows because if a missing head \(v\) is not initially enabled, it has an initially missing neighbor \(u\); both missing adjacent heads block each other throughout any update sequence. Thus no formerly disabled rule becomes enabled. Conversely all initially enabled heads are inserted in one pass. The minimal enabling subset for insertion of each missing \(v\) is \(N_G(v)\), which is recoverable from the combined closure; this proves injectivity of the graph-to-closure correspondence and \(2^{\binom n2}\) exact enumeration.

**Lemma 2 (closed complements).** A set \(X\) is fixed precisely when every vertex \(v\notin X\) has at least one neighbor missing from \(X\). With \(S=V\setminus X\), this says every vertex of the induced graph \(G[S]\) has positive degree, including the vacuous case \(S=\varnothing\). The family is intersection-closed since it consists of fixed points of a closure operator (or directly because all heads of a Horn theory are satisfied).

**Lemma 3 (matroid boundary).** Suppose exchange holds. For any edge \(\{u,v\}\), let \(X=N_G(u)\setminus\{v\}\). This set excludes both heads. Then \(u\notin C_G(X)\), but \(u\in C_G(X\cup\{v\})\). Exchange forces \(v\in C_G(X\cup\{u\})\), so \(N_G(v)\setminus\{u\}\subseteq N_G(u)\setminus\{v\}\). Interchanging \(u,v\) gives equality: every adjacent pair has identical neighborhoods outside the pair. Consequently adjacency is transitive along length-two paths, so every connected component is a clique. Conversely if \(G\) is a disjoint union of cliques, the rule for each vertex of a clique \(K\) fires only when all *other* vertices of \(K\) are present. The closure on this block is exactly the uniform-matroid closure of \(U_{|K|-1,|K|}\), with singleton blocks interpreted as loops. The global closure is their direct sum, hence a matroid closure. Components correspond exactly to a set partition of \(V\), giving \(B_n\). Within each block every subset is fixed except the \(|K|\) subsets with exactly one missing vertex; taking products gives the stated polynomial.

**Lemma 4 (Boolean submodular boundary).** Since fixed points of \(C_G\) are intersection-closed, the displayed Boolean submodularity inequality for the failure indicator \(f_G\) is equivalent to the fixed-point family being also union-closed. If \(v\) has distinct neighbors \(u,w\), both \(V\setminus\{u,v\}\) and \(V\setminus\{v,w\}\) are fixed by Lemma 2, but their union \(V\setminus\{v\}\) is not. Thus union closure requires every vertex degree at most one. Conversely in a matching graph, a complement with no isolated vertices consists of whole edges and no isolated vertices, so the fixed sets are exactly unions of whole edge components together with all isolated vertices. Their union and intersection are again fixed. The polynomial is therefore \(t^r(1+t^2)^m\). A matching with \(j\) edges is a choice of \(2j\) labelled vertices and a pairing, giving \(n!/(2^j j!(n-2j)!)\), and summation establishes the count and generating function.

These four lemmas establish all assertions for every integer \(n\ge1\). No conclusion is extrapolated from finite samples.

## Verification

The accompanying standalone `verify.py` (Python 3.9 or later, standard library only) directly checks every ordered pair of elementary rules and enumerates every rule family for \(1\le n\le4\), reproducing the commutation/symmetric-premise equivalence. It enumerates every labelled graph through \(n=5\), tests both orders of single-pass execution and fixed-complement semantics, exhaustively evaluates the exchange axiom and union closure, and matches the graph, Bell, and matching counts. It returns `VERIFY_OK`. The independent graph counts are \((1,2,8,64,1024)\); matroid counts \((1,2,5,15,52)\); Boolean submodular counts \((1,2,4,10,26)\) for \(n=1,\ldots,5\). These computations test the theorem but are not the proof of its universal quantifier.

Run: `python3 verify.py` in a directory containing this document and the script. The script also checks an auxiliary random-graph fixed-point expectation formula; that experiment is not required for the theorem.

## Relationship to prior work

Bérczi, Boros and Makino (2023) study Horn closure operators, hypergraph Horn functions and the matroid exchange connection; these provide the correct broader setting but do not state the pairwise commutation graph normal form or the two graph-class thresholds for the one-head commuting-update problem. Lozin and Zamaraev (2023) characterize Boolean-submodular Horn functions through general implicant conditions, providing a route to broader coverage of the union-closure half; their results do not supply the per-head commutation classification or its matroid/Boolean-submodular graph trichotomy. Eiter, Ibaraki and Makino (1999) study bidual Horn conditions, a different closure requirement; we do not identify bidual Horn with Boolean submodularity. Bell numbers, the matching involution numbers, cluster graphs, and uniform matroids are standard, and none is itself claimed as novel.

## Limitations

The conclusion concerns exactly one distinct-head definite Horn clause per vertex with premises excluding that vertex. Additional clauses per head, multihead rules, or arbitrary Horn theories need not obey the graph description. The exact counts are for *labelled* variables (not graph isomorphism classes). The novelty search cannot exclude an unindexed reformulation in database dependency theory, closure-system theory, or rewrite-system critical-pair theory. General Boolean-submodular and matroid characterizations may imply individual boundary tests after translating the present family; the distinguishing contribution is the integrated exact normal form and classification. The software exhausts only the stated finite ranges; the proof carries the arbitrary-size assertion.

## References

- Bérczi, K., Boros, E., Makino, K., *Hypergraph Horn Functions*. arXiv:2301.05461, first public version 13 January 2023; https://arxiv.org/abs/2301.05461. Primary text and matroid-exchange material examined.
- Lozin, V., Zamaraev, V., *Union-closed sets and Horn Boolean functions*. Journal of Combinatorial Theory, Series A, published online 11 October 2023; open full text https://wrap.warwick.ac.uk/id/eprint/180696/.
- Eiter, T., Ibaraki, T., Makino, K., *Bidual Horn Functions and Extensions* (1999); author-hosted full text https://www.kr.tuwien.ac.at/staff/eiter/et-archive/files/da4123.pdf. Used for terminology and comparison only.
