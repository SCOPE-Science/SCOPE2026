# Seven rank-four theories of finite half-graphs

## Finding
For every integer \(n\ge1\), let \(H_n\) be the undirected simple graph with vertex set \(\{a_1,\ldots,a_n,b_1,\ldots,b_n\}\) and edges \(\{a_i,b_j\}\) exactly when \(i\le j\). Use ordinary first-order logic with only equality and undirected adjacency (no distinguished bipartition, order, or constants). Then, for all positive integers \(m,n\),
\[
 H_m\equiv_4 H_n\quad\Longleftrightarrow\quad\min\{m,7\}=\min\{n,7\}.
\]
Thus there are exactly seven quantifier-rank-four theories in this family: one for each \(1\le n\le6\), and one shared by every \(n\ge7\). The smallest representative of the last class *within this family* has fourteen vertices; no claim is made about minimum representatives among arbitrary graphs.

Moreover, the four-vertex atomic diagrams already stabilize at \(n=4\): any tuple of at most four selected vertices uses at most four distinct underlying indices, which can be order-compressed into \(\{1,2,3,4\}\) without changing its induced adjacency/equality pattern. Hence all \(H_n\) with \(n\ge4\) agree on purely existential or purely universal graph sentences using at most four quantifiers, even though full rank-four logic distinguishes \(H_4,H_5,H_6,H_7\). The finer separation necessarily uses quantifier alternation.

The lower-rank partitions provide context: rank one has one class; rank two separates \(n=1\) from \(n\ge2\); rank three has the classes \(n=1\), \(n=2\), and \(n\ge3\). In contrast, rank four distinguishes each of the first six consecutive parameter values before stabilizing at seven.

## Assumptions and scope
All graphs are finite, nonempty, simple, undirected and uncoloured. Every \(n\) is a positive integer. \(G\equiv_q K\) means agreement on *all* first-order sentences with quantifier rank at most \(q\), including those with alternating quantifiers. This is not an assertion about counting logic, infinite half-graphs, monadic second-order logic, or a language that names the two sides.

## Proof
**1. Infinite tail via a linear-order transfer.** Let \(L_n\) be the strict linear order of length \(n\). The graph \(H_n\) has a quantifier-free two-copy description: its vertices are \((i,\mathsf A)\) and \((i,\mathsf B)\), for \(i\in L_n\). Distinct vertices are adjacent if and only if their tags differ and the \(\mathsf A\)-index is less than or equal to the \(\mathsf B\)-index. If Duplicator wins the \(q\)-round Ehrenfeucht–Fraïssé game on \(L_m,L_n\), she wins the corresponding game on \(H_m,H_n\) by retaining each chosen vertex's tag and responding to its index by the order-game strategy. Repeated index choices across the two tags are handled by the order-game equality condition. The resulting map preserves vertex equality and graph adjacency. Hence \(L_m\equiv_q L_n\) implies \(H_m\equiv_q H_n\).

The standard interval-splitting induction for finite linear orders says that \(L_m\equiv_q L_n\) whenever both lengths are at least \(2^q-1\). Briefly, after an ordered selection the unchosen intervals are maintained as either equal in length below \(2^r-1\) or both of length at least \(2^r-1\), with \(r\) moves left. Any chosen point splitting a large interval can be answered so that both resulting subinterval pairs are either small and equal or sufficiently large at threshold \(2^{r-1}-1\); small intervals can be matched exactly. Induction proves the claim. For \(q=4\), therefore, \(H_n\equiv_4H_{15}\) for every \(n\ge15\).

**2. Exact finite boundary by a terminating type recurrence.** For each graph \(G\) and ordered \(k\)-tuple \(\bar v\), define the atomic diagram \(T_4(G,\bar v)\), when \(k=4\), by recording equality and adjacency for every pair of tuple positions. For \(k=3,2,1,0\), recursively set
\[
 T_k(G,\bar v)=\{T_{k+1}(G,\bar v,w):w\in V(G)\}.
\]
All tuples, including those with repeated vertices, are included. An induction on the remaining quantifiers shows that the same \(T_k\) is obtained precisely when two tuples satisfy the same first-order formulas of quantifier rank at most \(4-k\). In the induction, existential quantification tests membership of a child type in the displayed set; negation and Boolean operations add no information. Therefore two graphs agree at rank four if and only if their empty-tuple \(T_0\) values agree.

The standalone `finite_types.py` is a literal exhaustive implementation of this recurrence, sharing type identifiers across all graphs. It constructs the ternary pair-diagram of each four-tuple from the explicit adjacency formula \(i\le j\), then takes distinct-child-type sets successively for triples, pairs, singletons, and the empty tuple. It checks *every* vertex tuple, with no sampling. For \(n=1,\ldots,15\), the resulting identifiers, assigned on first occurrence in increasing \(n\), are exactly
\[
 (0,1,2,3,4,5,6,6,6,6,6,6,6,6,6).
\]
The integer identifiers are only encodings of exact structural types; their equality and inequality are the checked mathematical facts. The exhaustive finite range combines with the preceding tail lemma to prove the claimed classification for every positive integer.

**3. Independent boundary verification.** The independent program `ef_game.py` does not construct first-order types. It instead solves the alternating four-round Spoiler–Duplicator game by memoized minimax, testing all legal new selections on either graph and all partial-isomorphism-preserving responses. It verifies Spoiler wins on \((H_4,H_5)\), \((H_5,H_6)\), and \((H_6,H_7)\), while Duplicator wins on \((H_7,H_8)\). Because repeated selections can always be matched to their already corresponding vertices, skipping them does not change who wins. This independently checks the sensitive stabilization boundary.

## Verification
Run `python3 finite_types.py` and `python3 ef_game.py` from the directory containing those two files, using Python 3 and no nonstandard packages. Their actual successful outputs are bundled in `finite_types_output.txt` and `ef_game_output.txt`. The first program includes the exhaustive finite \(1\le n\le15\) certificate and cross-checks quantifier ranks one to three. The second program independently evaluates four boundary games. In particular, it explored 138098 memoized states for \((H_6,H_7)\) and 574599 for \((H_7,H_8)\). The infinite-tail step is proved mathematically, not inferred from these tests.

## Relationship to prior work
The finite half-graph is the canonical combinatorial pattern of the order property in stability theory. Malliaris–Shelah's *Regularity lemmas for stable graphs* (2011, arXiv:1102.3904) uses half-graphs to formulate the non-order-property assumption and proves regularity theorems for graphs excluding sufficiently large half-graphs; its main assertions concern partitions and uniformity, not the exact first-order type partition of \(H_n\) itself. The paper uses a variant indexed by \(i<j\); our connected convention uses \(i\le j\), and the distinction is substantive at small sizes.

Pikhurko–Verbitsky's *Logical complexity of graphs: a survey* (first arXiv version 2010, arXiv:1003.4865), Section 2.2, gives the general finite-rank tuple-type recurrence and its correctness. That general recurrence is used here; the graph-specific numerical stabilization at seven, the seven classes, and their sharp smallest family representative require the additional computation and finite-order transfer above. The exact finite-order theorem is classical, and not claimed as new. Searches for the rank-four half-graph classification and equivalent chain/Ferrers-graph terminology did not identify a published covering statement. This is limited priority evidence, not a proof of absence.

## Limitations
The sharp fourteen-vertex representative statement is **within the family of half-graphs only**. The theorem covers exactly quantifier rank four in the uncoloured adjacency language, with contextual ranks one through three. It does not imply all-rank stabilization, definability in richer logics, or a bound on the model-theoretic order property itself. Independent mathematical review and exhaustive historical-priority verification have not been performed. The numerical type computation is finite and reproducible but is not a formal proof-assistant certificate; its mathematical meaning relies on the proved recurrence.

## References
1. M. Malliaris and S. Shelah, *Regularity lemmas for stable graphs*, arXiv:1102.3904 (first publicly posted 2011-02-18), especially Introduction, Definition 1.2 and Theorem 5.18. https://arxiv.org/abs/1102.3904
2. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (first publicly posted 2010-03-25), especially §§2.2 and 3. https://arxiv.org/abs/1003.4865
