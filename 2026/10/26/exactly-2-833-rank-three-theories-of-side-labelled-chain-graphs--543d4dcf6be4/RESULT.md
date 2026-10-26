# Exactly 2,833 rank-three theories of side-labelled chain graphs, with a sharp 21-vertex kernel

## Finding

Let \(\mathcal C\) be the class of all finite (possibly empty) simple bipartite **chain graphs with a named bipartition**, regarded as first-order structures in the signature \(\{A,B,E\}\). The unary predicates \(A,B\) partition the domain, both parts are independent, and \(E\) is undirected, loopless adjacency. A graph is a chain graph when the neighbourhoods of vertices in either part are linearly ordered by inclusion; equivalently it has no induced pair of disjoint edges.

There are **exactly 2,833** equivalence classes in \(\mathcal C\) under agreement on all first-order sentences of quantifier rank at most three. Every class has a representative with at most **21 vertices**, and this is optimal: precisely **two** classes have minimum representative order 21. Minimal creation words witnessing these two classes are `001100110011011001100` and `110011001001100110011` under the conventions below. These bounds are within the named-bipartition chain-graph class, not within all graphs, and they include the empty structure as one of the 2,833 classes.

## Assumptions and scope

There are no parameters, no counting quantifiers, and no ordered relation beyond the two unary part predicates and adjacency. Quantifier rank is usual nesting depth, not the number of distinct variable symbols. The bipartition is fixed and named; the theorem does not assert the same 2,833 count for uncoloured chain graphs or for a signature naming a linear order.

For a word \(w\) over \(\{0,1\}\), define \(G(w)\) recursively from the empty graph: appending `0` inserts a vertex in \(A\) adjacent to no previously present vertex; appending `1` inserts a vertex in \(B\) adjacent to **every** previously present vertex in \(A\) and to no vertex of \(B\). Thus, for positions \(i<j\), adjacency occurs exactly when \(w_i=0\) and \(w_j=1\). Vertices of the same side never meet.

## Proof

**1. All chain graphs admit the word model.** For any chain graph \(G=(A,B,E)\), linearly order \(B\) as \(b_1,\ldots,b_t\) so that \(N(b_1)\subseteq\cdots\subseteq N(b_t)\). For each \(a\in A\), its set of neighbours in this ordering is a (possibly empty) suffix: once \(a\in N(b_j)\), nestedness forces \(a\in N(b_k)\) for all \(k>j\). Insert \(a\) just before the first neighbour \(b_j\), or after all \(B\) if it has none; insert each \(b_j\) in the given order. Ties can be broken arbitrarily. The resulting word uses one letter per vertex and realizes every edge and nonedge of \(G\). Conversely each word graph has nested neighbourhoods, since successive \(B\)-vertices see weakly increasing initial \(A\)-sets. This includes isolated vertices, empty sides, and the empty graph.

**2. An exact three-round logical invariant.** For a vertex \(a\), put
\[
D(a)=\bigl(\operatorname{side}(a),\{(\operatorname{side}(c),E(a,c)):c\ne a\}\bigr).
\]
For ordered distinct vertices \(a,b\), put
\[
P(a,b)=\bigl(\operatorname{side}(b),E(a,b),
\{(\operatorname{side}(c),E(a,c),E(b,c)):c\notin\{a,b\}\}\bigr).
\]
Define \(T(a)=(D(a),\{P(a,b):b\ne a\})\), and \(H(G)=\{T(a):a\in G\}\). The sets are sets of realizable patterns, not multisets. A complete zero-quantifier atomic type of a selected triple is exactly its equalities, unary colours, and pairwise adjacencies. The one-quantifier type of a selected ordered pair consists of its atomic diagram and the set of atomic diagrams obtained by choosing a third vertex. When the pair repeats the same vertex, this is exactly \(D(a)\); otherwise it is determined by the colours/edge of the pair and \(P(a,b)\). Thus the two-quantifier type of a selected vertex is exactly \(T(a)\), and the three-quantifier type of the empty tuple is exactly \(H(G)\). By the standard Hintikka/Ehrenfeucht–Fraïssé recursion,
\[
G\equiv_3 G'\quad\Longleftrightarrow\quad H(G)=H(G').
\]
The same proof covers the empty graph because the top-level set of vertex types is empty. No bound on the number of vertices is presumed in this equivalence.

**3. The two word operations respect the invariant.** If \(G\equiv_3 G'\), adding a fresh vertex of colour \(A\) with no edges, or a fresh vertex of colour \(B\) linked precisely to every old \(A\)-vertex, preserves three-round equivalence. Indeed, in a three-round Ehrenfeucht–Fraïssé game on the extended structures, reply to the new vertex by the new vertex, and for all old vertices follow a winning strategy on \(G,G'\). Cross-incidences with the new vertex depend only on the preserved unary colour, so the partial isomorphism is preserved. Repetitions of the new vertex are matched to repetitions. Hence each append operation induces a well-defined map on \(\equiv_3\) classes.

**4. An exhaustive finite closure certificate.** Starting at the empty word, breadth-first search over the two append operations, identifying two states exactly when their invariant \(H\) agrees, discovers 2,833 distinct states. `certificate.json` records one shortest representative word and both successor indices for every state. `verify.py` constructs graphs from each recorded word, reconstructs \(H\), checks all 2,833 signatures are different, checks all \(2\times2{,}833=5{,}666\) declared successor identities, and checks reachability and shortest distances from the empty state in the complete transition graph. Therefore the list is closed and exhaustive for words of **all finite lengths** by induction on length, not by extrapolation from a size-limited search. Step 1 transfers the classification to all graphs in \(\mathcal C\).

The verified breadth-first distances have maximum 21; exactly two states have distance 21 and their words are given in the Finding section. Because every graph on \(n\) vertices has a word of length \(n\), and the transition distance of a state is the minimum possible word length, no chain graph with fewer than 21 vertices can represent either extremal state. Conversely its exhibited length-21 word does so. This establishes sharpness.

## Verification

Run `python3 verify.py` alongside `certificate.json` with Python 3 and the standard library. The recorded `verification_output.txt` begins with `VERIFY_OK`, reports 2,833 states, 5,666 checked successor identities, and the full minimum-order histogram (orders zero through 21). It also checks all 2,047 binary input words of length at most 10 plus the 2,048 words of length 11 against the table; equivalently all words of length at most 11, and independently checks generic rank-three Hintikka recursions on 204 certificate representatives and on all input words of length at most six. The generic recursion uses atomic diagrams and quantifier extensions rather than the specialized bitmask encoding. These tests cross-check the finite certificate, while the mathematical induction in Step 3 justifies the extension to arbitrary sizes.

## Relationship to prior work

Finite-model-theoretic quantifier depth and Ehrenfeucht–Fraïssé games are treated by Pikhurko and Verbitsky (2010/2013); their survey supplies the general methodology but no exact chain-graph state count. Boyacı, Ekim, and Shalom (2015) treat the nested-neighbourhood structure of chain/co-chain graphs in optimization; their main theorems concern maximum cut. Alecu, Atminas, Lozin, and Malyshev (2022) describe chain and quasi-chain graph structure, including the \(2P_2\)-free characterization and bounded lettericity; they do not state the present rank-three classification or 21-vertex logical kernel. These were inspected in full-text HTML, including relevant theorems and arguments, not just abstracts.

A separate exact classification of ordinary uncoloured threshold graphs at rank three has 357 classes, but that graph class and signature are different. A separate result about a one-parameter family of connected half-graphs at rank four concerns uncoloured graphs rather than the entire chain-graph class with two named sides. Neither result implies the present count. Semigroup/word-composition theorems may imply general finiteness or algorithmic computability but not this numeric value without a substantive state calculation.

## Limitations

The theorem is for *finite* chain graphs with **named** bipartition and plain first-order logic. It makes no assertion about counting logic, uncoloured graphs, quasi-chain graphs, or quantifier rank four. The 2,833 figure and sharp bound rely on the attached finite closure calculation and must be replayed to check numerical integrity. The computation alone is not a substitute for the three-round logical invariant and append-congruence proof. Literature searches and relevant full-text comparisons do not establish global novelty against unindexed publications or inaccessible historical material; independent external mathematical audit has not been performed.

## References

1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first submitted 2010-03-25, especially the definitions of quantifier depth and Section 3 on Ehrenfeucht games. https://arxiv.org/html/1003.4865
2. A. Boyacı, T. Ekim, and M. Shalom, *The Maximum Cut Problem in Co-bipartite Chain Graphs*, arXiv:1504.03666v1, submitted 2015-04-14, especially Section 1 on bipartite chain graphs. https://arxiv.org/html/1504.03666v1
3. B. Alecu, A. Atminas, V. Lozin, and D. Malyshev, *Combinatorics and Algorithms for Quasi-Chain Graphs*, Algorithmica 85 (2023), first published online 2022-08-08, especially Sections 1–2 on nested neighbourhoods and forbidden induced subgraphs. https://doi.org/10.1007/s00453-022-01019-6
