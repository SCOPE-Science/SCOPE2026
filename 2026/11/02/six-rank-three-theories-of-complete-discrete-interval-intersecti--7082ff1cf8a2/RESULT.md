# Six rank-three theories of complete discrete-interval intersection graphs

## Finding
For every integer \(n\ge1\), let \(G_n\) be the simple undirected graph whose vertices are the nonempty intervals \([i,j]\) of the chain \([n]=\{1,\ldots,n\}\), with an edge between two **distinct** intervals precisely when they intersect. In the first-order signature consisting only of equality and a symmetric irreflexive adjacency relation \(E\), the complete quantifier-rank-three classification is

\[
G_m\equiv_3G_n\quad\Longleftrightarrow\quad \min(m,6)=\min(n,6)
\qquad(m,n\ge1).
\]

In particular there are exactly six rank-three theories among these graphs. Their smallest representatives are \(G_1,\ldots,G_6\), with respectively \(1,3,6,10,15,21\) vertices. Every graph in the family has a rank-three equivalent representative on at most \(21\) vertices; this bound is sharp **within this family**. By contrast, at quantifier rank two there are only two theories: \(G_1\) and the class of all \(G_n\) with \(n\ge2\).

## Assumptions and scope
The family includes *all* nonempty contiguous subsets of the finite chain, including singleton intervals and the whole chain. Adjacency does not include loops. The structures have no named endpoints, containment relation, length predicate, or built-in order. The parameter \(n\) ranges over positive integers without any additional restriction. The notation \(G_m\equiv_qG_n\) means agreement on all first-order sentences of quantifier rank at most \(q\) in the stated language.

## Proof
**1. Exact finite type recursion.** For any nonempty finite simple graph \(H\), any ordered tuple \(\bar a\) of vertices, and integer \(r\ge0\), define \(T_0^H(\bar a)\) to be its *complete atomic diagram*, recording every equality and every ordered adjacency atom on entries of \(\bar a\). Define recursively

\[
T_{r+1}^H(\bar a)=\big\{T_r^H(\bar a,b):b\in V(H)\big\}.
\]

These are exact first-order types for this purpose: an induction on \(r\) shows that two tuples have identical \(T_r\) if and only if their expansions have the same first-order formulas of quantifier rank at most \(r\). The forward direction uses agreement of existential extensions and Boolean combinations; the converse constructs distinguishing Hintikka formulas, and reconstructs the atomic diagram by projection from any extension because the structures are nonempty. In particular \(T_3^H(())\) determines precisely the rank-three theory. This recurrence includes repeated choices of vertices, so equality information is not lost.

For an ordered triple \((u,v,w)\), its atomic diagram is exactly the six Boolean values

\[
(u=v,\ u=w,\ v=w,\ E(u,v),\ E(u,w),\ E(v,w)).
\]

The C++ verifier encodes that diagram by a six-bit integer, uses a 64-bit set mask for all triple diagrams achievable from each ordered pair, then takes canonical sets of these pair masks for each first vertex, followed by the canonical set of one-vertex profiles for the whole graph. This implements the displayed recurrence *exactly*, not by sampling.

Exhaustive computation for all \(1\le n\le26\) yields the following result; the last column counts distinct rank-two types with one free vertex:

| Parameter | Rank-three equivalence class | Distinct one-vertex rank-two types |
|---|---|---|
| \(1\) | 1 | 1 |
| \(2\) | 2 | 2 |
| \(3\) | 3 | 4 |
| \(4\) | 4 | 6 |
| \(5\) | 5 | 8 |
| \(6,\ldots,26\) | 6 | 9 |

The graph types of \(G_1,\ldots,G_6\) are pairwise distinct; every graph from \(G_6\) through \(G_{26}\) has literally the same canonical rank-three type. More concretely, the rank-two singleton profile of interval \([3,4]\) in \(G_6\) is absent from every vertex of \(G_5\), while all eight profiles of \(G_5\) persist in \(G_6\). Hence the distinction at the sharp boundary is witnessed by a rank-three sentence, not by comparing sizes. The independent Python program builds the recursive types directly as nested immutable sets for \(1\le n\le12\) and corroborates these conclusions.

**2. Infinite-tail lemma.** Let \(L_n\) denote the order on \([n]\). Put \(t_0=0\), and for \(r\ge1\) set

\[
t_r=3t_{r-1}+2=3^r-1.
\]

If \(m,n\ge t_q\), Duplicator can handle \(q\) rounds in which each Spoiler move selects **up to two points at once** from one of the linear orders, maintaining all equality and strict-order relations between selected points. Indeed, with \(r\) moves left, require each corresponding gap between previously selected points (including exterior gaps) either to contain equal numbers of unselected points below \(t_r\), or to contain at least \(t_r\) points in both orders. If a move places \(s\le2\) new points in one gap, the gap splits into at most three subgaps. A gap containing fewer than \(t_r\) points is replicated exactly. For a large gap, the source subgaps cannot all be smaller than \(t_{r-1}\): if they were, the old gap would contain at most \(3(t_{r-1}-1)+2<t_r\) points. Match each small subgap exactly; give every large one at least \(t_{r-1}\) points, distributing any surplus to a large subgap. The total minimum required in the target is at most \(3t_{r-1}+2=t_r\). Thus the invariant descends to \(r-1\), and at \(r=0\) all selected endpoint order relations are preserved.

Each interval is specified by its two endpoints, with both endpoints allowed to coincide. Therefore Duplicator applies the two-point order strategy to the endpoints of each selected interval. Preserved endpoint order and equality imply preserved equality of selected intervals and preserved adjacency, since

\[
E([i,j],[k,\ell])\quad\Longleftrightarrow\quad
([i,j]\ne[k,\ell])\ \land\ i\le\ell\ \land\ k\le j.
\]

Consequently \(G_m\equiv_qG_n\) whenever \(m,n\ge3^q-1\). In particular, all \(G_n\) for \(n\ge26\) have the same rank-three theory.

**3. Complete classification.** Step 1 identifies the six pairwise different types through parameter \(26\), and shows that \(G_6\equiv_3G_{26}\). Step 2 shows that every larger \(G_n\) is equivalent to \(G_{26}\). Transitivity gives the displayed equivalence for every positive pair \((m,n)\). The representative bound is sharp since no graph with parameter below \(6\) has the common tail theory.

## Verification
All computation is integer-exact, with no statistical assumptions or external mathematical packages. From the directory containing the companion files, execute `sh reproduce.sh`. This compiles `interval_types.cpp` with a C++17 compiler and compares its complete output with `interval_types_output.txt`; it separately runs `independent_types.py` and `witness.py`, checking their outputs against the included files. The C++ run exhausts parameters \(1\) through \(26\); the Python definition-level recursion independently covers parameters \(1\) through \(12\); the witness script isolates the new rank-two singleton profile at \(n=6\). The infinite-tail lemma is proved above, rather than inferred from computations.

## Relationship to prior work
Ganian, Hliněný, Kráľ, Obdržálek, Schwartz and Teska establish general first-order model-checking results for interval graphs using Ehrenfeucht–Fraïssé game trees; their 2013 preprint and 2015 journal version do not state the exact six-class classification of the *complete discrete interval family* or its sharp rank-three cutoff. McKee and McMorris describe the standard path/subpath representation of interval graphs, rather than a bounded-rank classification. These sources supply the natural combinatorial setting and logical method, but do not imply the specific numerical threshold merely by specializing their published theorems. The relation studied here is *intersection*, not interval containment; results in the containment signature cannot be transferred at fixed quantifier rank without a rank-preserving interpretation.

## Limitations
The result concerns only the complete family of all discrete closed intervals of one finite chain, with pure simple-graph adjacency, at quantifier rank three. No assertion is made for higher quantifier ranks, arbitrary interval graph subfamilies, or expanded interval signatures. The finite boundary is supported by executable exhaustive enumeration, with an independent smaller-range implementation; independent expert mathematical validation has not been carried out. Literature searches and primary-source inspection are not an exhaustive historical-priority guarantee.

## References
1. R. Ganian, P. Hliněný, D. Kráľ, J. Obdržálek, J. Schwartz and J. Teska, *FO Model Checking of Interval Graphs*, arXiv:1302.6043, first public version 25 February 2013; *Logical Methods in Computer Science* 11(4:11) (2015). https://arxiv.org/abs/1302.6043
2. T. A. McKee and F. R. McMorris, *Topics in Intersection Graph Theory*, Chapter 3, *Interval Graphs*, SIAM edition, DOI:10.1137/1.9780898719802.ch3. https://epubs.siam.org/doi/10.1137/1.9780898719802.ch3
