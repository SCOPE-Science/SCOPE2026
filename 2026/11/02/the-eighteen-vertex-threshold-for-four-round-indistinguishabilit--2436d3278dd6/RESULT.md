# The eighteen-vertex threshold for four-round indistinguishability of connectedness in cycle unions

## Finding
Let \(C_n\) be the simple undirected cycle with \(n\ge3\) vertices. Write \(G\equiv_4 H\) when \(G\) and \(H\) satisfy exactly the same first-order graph sentences of quantifier rank at most four, in the equality-and-adjacency language, without counting or component predicates.

**Theorem.** (i) Every finite disjoint union of at least two cycles, each of length at least nine, satisfies
\[
\bigsqcup_{i=1}^{s}C_{n_i}\equiv_4 C_{11}\qquad(s\ge2,\ n_i\ge9).
\]
(ii) Among all disconnected finite simple two-regular graphs that are \(\equiv_4\)-equivalent to *some connected cycle*, the minimum number of vertices is exactly eighteen. It is attained by
\[
C_9\sqcup C_9\equiv_4 C_{11}.
\]
In particular, a graph with only eighteen vertices can be disconnected yet have the same four-round first-order theory as a connected cycle, and no disconnected two-regular graph on fewer vertices has this property.

## Assumptions and scope
All graphs are finite, nonempty, loopless, simple, undirected, and are interpreted in first-order logic with equality and a binary adjacency relation. A finite two-regular graph is a disjoint union of cycles of lengths at least three. Equivalence is for arbitrary first-order formulas *as sentences* with nesting depth at most four; this is not an assertion about counting logic, arbitrary additional named vertices, or isomorphism. No connectedness predicate is added.

## Proof
**1. Connected-cycle tail.** Brown and Hoshino, Theorem 4.9, prove that for \(n,m\ge3\),
\[
C_n\equiv_4 C_m\ \Longleftrightarrow\ n=m\ \text{or}\ (n\ge11\text{ and }m\ge11).
\]
Thus \(C_3,\ldots,C_{11}\) represent the nine distinct rank-four theories of individual finite cycles. This published theorem is used as a lemma, not asserted as a new result.

**2. Disjoint-union compatibility.** If \(A\equiv_4 B\), then \(A\sqcup D\equiv_4 B\sqcup D\) for any graph \(D\). In the four-round Ehrenfeucht–Fraïssé game, Duplicator follows her winning strategy between \(A,B\) for vertices selected from the corresponding components, and copies moves identically in the common component \(D\). Because there are no edges between these components, the combined partial map preserves equality and adjacency. This proves the compatibility for finite disjoint unions, without any assumption on their orders.

**3. Six exact base identities.** Define the rank-four extension signature of a finite graph \(G\). For each ordered tuple \(\bar v\) of selected vertices, \(T_0^G(\bar v)\) is its complete equality/adjacency atomic pattern, and, recursively,
\[
T_{r+1}^G(\bar v)=\bigl(T_0^G(\bar v),\{T_r^G(\bar v,w):w\in V(G)\}\bigr).
\]
Induction on \(r\) shows that two tuples have the same signature precisely when they agree on all first-order formulas of quantifier rank at most \(r\), with the tuple as parameters. The induction covers negation and arbitrary Boolean combinations because the set of extension types records every possible witness type, while repeated witnesses are included. Hence \(T_4^G(())\) is a complete rank-four sentence invariant.

The standalone finite-type programs evaluate all four-vertex atomic patterns and all possible quantified extensions, with no sampling or heuristic pruning. They establish the following six exact equalities:
\[
C_a\sqcup C_b\equiv_4 C_{11}\quad\text{for } (a,b)\in
\{(9,9),(9,10),(9,11),(10,10),(10,11),(11,11)\}.
\]
A separate direct adversarial game solver independently establishes the first equality with \(C_{11}\), by exhaustive minimax on all possible remaining moves and replies (with the first chosen vertices normalized by vertex transitivity). The two signature implementations are independent Python and C++ code.

For any \(a,b\ge9\), the connected-cycle tail and Step 2 allow every length at least eleven to be replaced by eleven before applying the six identities. Hence \(C_a\sqcup C_b\equiv_4 C_{11}\). For \(s>2\), combine two components and replace their union by \(C_{11}\), then repeat; this proves (i).

**4. Sharp lower bound.** For any disconnected two-regular graph with fewer than eighteen vertices, its multiset of cycle lengths is an integer partition of some \(n\in\{6,\ldots,17\}\), into at least two parts all at least three. Exactly 105 such partitions exist, with counts for \(n=6,\ldots,17\), respectively,
\[
1,1,2,3,4,5,8,9,12,16,20,24.
\]
For every one of these 105 graphs the finite-type recursion in Step 3 computes the rank-four sentence type. Exhaustive comparison with \(C_3,\ldots,C_{11}\) gives **no match**. By Step 1 those nine graphs exhaust the connected-cycle theories, including all cycles longer than eleven. Hence none of the 105 disconnected graphs is rank-four equivalent to any connected cycle. The equality in (ii) follows from the \(18\)-vertex witness in Step 3.

## Verification
Run `python3 verify_rank4_connectedness.py` (Python 3, standard library only), compile and execute `verify_rank4_connectedness.cpp` with a C++17 compiler, and run `python3 ef_game_independent.py`. Each program reconstructs its graphs and does not read prior run records or external datasets. The Python census and C++ census both exhaust all cycle partitions below eighteen, check all nine connected representatives, and reproduce the six two-cycle identities. The independent game solver directly verifies \(C_9\sqcup C_9\equiv_4 C_{11}\).

Finite enumeration is exhaustive only over the specified 105 small disconnected graphs and six base pairs. The infinite step relies separately on the cited Brown–Hoshino connected-cycle theorem and the proved disjoint-union compatibility; no finite experiment is extrapolated to unbounded cycle lengths or numbers of components.

## Relationship to prior work
Brown–Hoshino (2007), Theorem 4.9, solves the comparison of **two connected cycles** at arbitrary fixed rank and provides the threshold eleven used here. The new question concerns arbitrary **disconnected unions of cycles** versus connected cycles; the sharp eighteen-vertex obstruction and six two-component identities are not contained in their connected-cycle statement. Their Conclusions explicitly distinguish further graph families from the completed single-cycle case.

Pikhurko–Verbitsky's survey gives the standard bounded-rank Ehrenfeucht framework and notes that connectedness is not first-order expressible on arbitrary finite graphs. It does not supply the optimal four-round finite witness within the two-regular family. Prior work on rank-three two-regular graphs addresses a different quantifier depth and neither implies the rank-four witness nor the optimal cutoff. Earlier uninspected graph-game technical reports are a residual historical-priority risk.

## Limitations
This result is restricted to quantifier rank four and pure adjacency/equality. It does not classify the rank-four theories of **all** disjoint cycle unions, nor claim that any cycle of length eight or smaller cannot occur in a large structure equivalent to \(C_{11}\). The minimality statement concerns the disconnected graph's vertex count (not the sum of the two compared orders). The lower-bound finite census and six identities are checkable exact computations, not an independent formal proof assistant certification. Independent mathematical audit and exhaustive historical-priority review remain unperformed.

## References
1. J. Brown and R. Hoshino, “The Ehrenfeucht–Fraïssé Game for Paths and Cycles,” *Ars Combinatoria* **83** (2007), 193–212, Theorem 4.9 and Conclusions; published April 30, 2007. Open article and PDF: https://combinatorialpress.com/ars-articles/volume-083-ars-articles/the-ehrenfeucht-fraisse-game-for-paths-and-cycles/ .
2. O. Pikhurko and O. Verbitsky, “Logical complexity of graphs: a survey,” arXiv:1003.4865 (2010), Sections 1 and 3. https://arxiv.org/abs/1003.4865 .
