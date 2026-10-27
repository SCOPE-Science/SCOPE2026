# Seven rank-four theories of connected half-graphs and a sharp fourteen-vertex kernel

## Finding
For every integer \(n\ge1\), let \(H_n\) be the finite simple graph with disjoint vertex sets \(A=\{a_0,\dots,a_{n-1}\}\) and \(B=\{b_0,\dots,b_{n-1}\}\), where
\[
 a_i\sim b_j\quad\Longleftrightarrow\quad i\le j,
\]
and there are no edges inside either vertex set. In ordinary first-order graph logic with equality and adjacency, for all \(n,m\ge1\),
\[
 H_n\equiv_4 H_m\quad\Longleftrightarrow\quad \min(n,7)=\min(m,7).
\]
Thus the connected half-graph family has exactly seven theories at quantifier rank four: six individual parameter values \(1,\ldots,6\), and one class containing every parameter \(n\ge7\). Every class has a representative on at most fourteen vertices, and fourteen is sharp within this family.

## Assumptions and scope
The relation \(\sim\) is undirected, symmetric, and irreflexive. There are no constants, unary colours, order symbols, counting quantifiers, or built-in bipartition labels in the stated graph language. \(H_n\) is connected and has \(2n\) vertices. The more common *strict* half-graph convention \(a_i\sim b_j\) iff \(i<j\) has isolated end vertices; deleting those endpoints from the strict half-graph of parameter \(n+1\) yields this connected version. First-order equivalence \(\equiv_q\) means agreement on all graph sentences of quantifier rank at most \(q\), equivalently a Duplicator win in the \(q\)-move Ehrenfeucht--Fraïssé game.

For a proof instrument only, write \(\widehat H_n\) for \(H_n\) expanded by one unary predicate \(P\) naming the \(A\)-side. The final assertion is in the *uncoloured* graph language; \(P\) is not included in that assertion.

## Proof
**Exact finite-type lemma.** Given a finite graph \(M\), optionally with a unary predicate, and an ordered tuple \(\bar u\), define its quantifier-free fingerprint \(\alpha_M(\bar u)\) to record all equalities, adjacency values, and optional unary values at positions in \(\bar u\). Define abstract types recursively by
\[
 \tau^M_0(\bar u)=\alpha_M(\bar u),\qquad
 \tau^M_{r+1}(\bar u)=\left(\alpha_M(\bar u),\;\big\{\tau^M_r(\bar u,v):v\in M\big\}\right).
\]
For tuples of the same arity, equality of these exact finite objects is equivalent to agreement on all first-order formulas of quantifier rank at most \(r\) with those free variables. Prove this by induction on \(r\): atoms are determined by the fingerprints, Boolean combinations do not add information, and an existential quantifier checks membership of a lower-rank successor type in the displayed set. Conversely, distinct successor-type sets are separated by an existentially quantified characteristic formula for the differing finite lower-rank type; the finite vocabulary and finite rank ensure that characteristic formulas can be built by induction. Universal quantification follows by negation. For the empty tuple these are exactly the rank-\(r\) sentence theories.

The standalone `verify.py` implements precisely this recursion, with canonical interning of its finite tree objects. Its exact calculation yields
\[
 \tau^{H_1}_4(()) ,\ldots,\tau^{H_6}_4(())
 \quad\text{all distinct from one another and from}\quad
 \tau^{H_7}_4(())=\tau^{H_8}_4(()).
\]
It also yields the *stronger labelled-language finite identity*
\[
 \tau^{\widehat H_8}_4(())=\tau^{\widehat H_9}_4(()).
\]
These are exhaustive finite calculations of all successor types on the displayed finite structures, not samples of sentences or tests based on graph invariants. They are the only non-symbolic premises of the theorem and are fully reproducible by the embedded program and recorded output.

**Composition lemma.** For graphs with the marked \(A\)-side, define \(X\odot Y\) on disjoint copies of \(X\) and \(Y\): retain all original edges; insert precisely those cross edges joining a \(P\)-vertex in the *left* factor \(X\) to a non-\(P\)-vertex in the *right* factor \(Y\). No other cross edges are inserted. If \(X\equiv_q X'\) and \(Y\equiv_q Y'\) in the unary-labelled graph language, then
\[
 X\odot Y\equiv_q X'\odot Y'.
\]
Indeed Duplicator plays the two component games in parallel, always answering in the corresponding factor. On every move the partial isomorphisms inside both components are preserved. Between factors, equality is always false, and adjacency is determined solely by factor order and the unary side labels, which those partial isomorphisms preserve. Thus their union remains a partial isomorphism after all \(q\) moves.

**Infinite-tail step.** Direct inspection of the defining inequality proves an isomorphism of labelled graphs
\[
 \widehat H_{n+k}\cong\widehat H_n\odot\widehat H_k
 \qquad(n,k\ge1).
\]
(The early \(A\)-vertices are adjacent to all later \(B\)-vertices; the later \(A\)-vertices are adjacent to no early \(B\)-vertices.) By the exact finite identity \(\widehat H_8\equiv_4\widehat H_9\) and composition, for every \(k\ge1\),
\[
 \widehat H_{8+k}\equiv_4\widehat H_{9+k}.
\]
Forgetting \(P\) preserves equivalence of graph sentences, so \(H_s\equiv_4 H_{s+1}\) for every \(s\ge8\). The separate exact uncoloured identity \(H_7\equiv_4 H_8\) joins the first step of this chain. Transitivity gives \(H_n\equiv_4 H_m\) for all \(n,m\ge7\). Conversely the six distinct finite types for \(H_1,\ldots,H_6\), and their distinction from \(H_7\), prove that no other pair can be equivalent. This proves the classification and the sharp bound \(2\cdot7=14\) for a smallest representative of the saturated class.

## Verification
Run `python3 verify.py` using an ordinary Python 3 interpreter. The script constructs each \(H_n\) from the given inequalities and computes rank types recursively without quantifier heuristics. It verifies all pairwise inequivalences among \(H_1,\ldots,H_7\), the rank-four identity for uncoloured \(H_7,H_8\), and the rank-four identity for labelled \(\widehat H_8,\widehat H_9\). Additionally, it confirms labelled \(\widehat H_7\not\equiv_4\widehat H_8\), and reports lower-rank sanity checks. `verify_output.txt` records the actual output, ending in `PASS`. Exhaustion here concerns only the finite base identities; the composition lemma, not extrapolation from small graphs, proves the infinite tail. Re-running the script is a direct check of the essential finite premises, not an independent formal certification of the written symbolic argument.

## Relationship to prior work
Malliaris and Shelah make half-graphs the central obstruction witnessing the finite order property for graphs and use their absence to prove regularity statements. Their half-graph convention can be converted to the connected convention used here by removing isolated end vertices. Their regularity and stability conclusions neither classify ordinary first-order rank-four equivalence among these particular finite graphs nor supply the sharp fourteen-vertex kernel. Pikhurko and Verbitsky survey logical depth and Ehrenfeucht--Fraïssé methods for graph definability, including structured graph families; the rank-four connected half-graph equivalence profile is a different, family-specific statement. Existing exact results on finite directed paths, one-red linear orders, and complete multipartite graphs concern different signatures or non-half-graph structures, and do not imply the displayed equivalence after quantifier-free interpretation. The proof's side-labelled composition is stronger than the uncoloured conclusion and isolates the edge-concatenation geometry that makes the infinite threshold rigorous.

## Limitations
The theorem is restricted to the connected half-graphs in the specified undirected simple graph language and specifically to quantifier rank four. It does not assert a uniform formula for arbitrary quantifier ranks, arbitrary chain graphs or mixed sums. The finite base identities are checked through reproducible exact exhaustive recursion rather than a separate hand-written game strategy for each of their pairs; the unbounded part has a symbolic game proof. Unindexed literature or an equivalent folklore result may still contain the same rank-four classification.

## References
1. M. Malliaris and S. Shelah, “Regularity lemmas for stable graphs,” arXiv:1102.3904 (first public version 18 February 2011), later *Transactions of the American Mathematical Society* 366 (2014), 1551–1585. https://arxiv.org/abs/1102.3904
2. Oleg Pikhurko and Oleg Verbitsky, “Logical complexity of graphs: a survey,” arXiv:1003.4865 (first public version 25 March 2010). https://arxiv.org/abs/1003.4865
