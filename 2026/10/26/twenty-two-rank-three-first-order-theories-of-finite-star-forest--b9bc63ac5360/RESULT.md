# Twenty-two rank-three first-order theories of finite star forests

## Finding

Every nonempty finite star forest belongs to one of exactly **22** equivalence classes for first-order sentences of quantifier rank at most three, in the language containing equality and a single symmetric irreflexive adjacency relation. Every class has a representative with at most **nine** vertices, and nine is the smallest possible uniform bound.

Writing \(S_t=K_{1,t}\), with \(S_0\) an isolated vertex and \(S_1\) an isolated edge, the unique rank-three class requiring nine vertices is represented by \(S_2\sqcup S_2\sqcup S_2\). This is a complete statement about arbitrary finite star forests, not merely a sample of small ones.

## Assumptions and scope

A *star forest* is a finite simple undirected graph in which every connected component is \(S_t\) for some integer \(t\ge0\). The graph is nonempty. Structures have **no built-in ordering, named vertices, colours, counting quantifiers, or extra predicates**. For graphs \(G,H\), write \(G\equiv_3 H\) when they satisfy the same first-order sentences of quantifier rank at most three. Repeated selections of a vertex are allowed in the corresponding three-round Ehrenfeucht–Fraïssé game.

Define a canonical forest
\[
F(c_0,c_1,c_2,c_3)=\bigsqcup_{j=0}^3 c_j S_j,
\qquad c_j\in\{0,1,2,3\},\quad\sum_j c_j>0.
\]
There are precisely \(4^4-1=255\) canonical parameter vectors. The four coordinates count isolated vertices, edges, two-leaf stars, and stars with at least three leaves after truncation.

## Proof

**1. Infinite-to-finite reduction.** In a three-round graph game between individual stars \(S_s\) and \(S_t\) with \(s,t\ge3\), Duplicator matches the centre with the centre and injectively matches selected leaves. At most three distinct leaves can be selected, so this preserves every equality and adjacency atom after all three rounds. Thus all \(S_t\) with \(t\ge3\) are rank-three equivalent. Components of the types \(S_0,S_1,S_2\) are retained exactly.

Consider two disjoint unions whose numbers of components of each of these four types agree after truncation at three. Duplicator reserves a one-to-one correspondence for each type whenever fewer than three such components exist, and otherwise matches each newly visited component with a fresh component of the same type. At most three components are ever visited. For each visited pair of components the local three-move strategy is used; choosing a vertex of a previously visited component never changes its matching. The global partial map is a partial isomorphism because edges occur only within components. Therefore every nonempty finite star forest is rank-three equivalent to exactly some \(F(c_0,c_1,c_2,c_3)\) in the stated 255-element collection. This reduction does **not** assume that 255 different logical theories occur.

**2. Exact three-rank invariant.** For any finite graph \(G\) and vertices \(a,b,z\), let \(\tau_G(a,b,z)\) be the six truth values of the three equality atoms and the three adjacency atoms on the ordered tuple \((a,b,z)\). Set
\[
P_G(a,b)=\{\tau_G(a,b,z):z\in V(G)\},\qquad
Q_G(a)=\{P_G(a,b):b\in V(G)\},\qquad
T(G)=\{Q_G(a):a\in V(G)\}.
\]
The usual backward induction for the first-order quantifier-rank game shows
\[
G\equiv_3 H\quad\Longleftrightarrow\quad T(G)=T(H).
\]
Indeed, equal atomic three-tuple types are the rank-zero game positions; the sets \(P_G\) record exactly every possible extension in one move from a marked pair, the sets \(Q_G\) do so from a marked vertex, and \(T(G)\) does so from the empty tuple. Using sets (rather than multisets) is essential: ordinary first-order logic cannot count multiplicities without spending further quantifiers. This equivalence gives an **exact, finite, reproducible decision procedure**, not a heuristic fingerprint.

**3. Exhaustive but bounded final step.** The included `verify_rank3.py` constructs the 255 canonical graphs as adjacency bitsets, computes \(T(G)\) directly from all choices of \(a,b,z\), and groups graphs by equality of this exact invariant. The resulting `rank3_manifest.csv` explicitly assigns each canonical vector to its class. The computation yields precisely 22 distinct values of \(T\). Its minimal-order representatives are the following vectors, ordered by increasing minimum order and then lexicographically:

\[
\begin{gathered}
(1,0,0,0),(0,1,0,0),(2,0,0,0),(0,0,1,0),\\
(1,1,0,0),(3,0,0,0),(0,0,0,1),(0,2,0,0),\\
(1,0,1,0),(2,1,0,0),(0,1,1,0),(1,2,0,0),\\
(2,0,1,0),(0,0,2,0),(0,3,0,0),(1,1,1,0),\\
(2,2,0,0),(0,2,1,0),(1,0,2,0),(2,1,1,0),\\
(2,0,2,0),(0,0,3,0).
\end{gathered}
\]
All these graphs have at most nine vertices. The final vector represents \(3S_2\) and has nine vertices. The same exact invariant proves that no canonical vector of fewer than nine vertices belongs to that class. By step 1, a hypothetical smaller, noncanonical star-forest representative could be truncated to a canonical representative without increasing its number of vertices. Hence no smaller representative exists: nine is sharp. These computations are exhaustive over the proven finite reduction, not an inference from testing star forests up to a size cutoff.

## Verification

Run `python3 verify_rank3.py --crosscheck` in the folder containing the attached program. This regenerates `rank3_manifest.csv` and reports exactly `canonical_profiles=255 rank3_theories=22 sharp_kernel_order=9`. It also solves the three-move Spoiler–Duplicator game by an independently implemented minimax recursion for all \(\binom{22}{2}=231\) pairs of class representatives, confirming each pair is inequivalent, together with four selected within-class/cross-class comparisons. The manifest holds all 255 canonical assignments; the program includes no external dependencies. The full unbounded statement additionally requires the symbolic component reduction of step 1.

## Relationship to prior work

The equivalence between quantifier rank and Ehrenfeucht–Fraïssé games is classical; the exact rank-three type construction is a concrete use of that theorem. Immerman's *Descriptive Complexity* (1999), Chapter 6, presents the games and formula-rank correspondence, while Libkin's *Elements of Finite Model Theory* (2004) surveys these methods. Algor and Alon (1989) treat star forests as fundamental graph objects in star arboricity; their invariant differs from first-order logical rank. The 22-type census and sharp nine-vertex kernel are not implied just by the general existence of finitely many rank-three types. No assertion of uniqueness in the wider literature follows merely from the searches reported separately.

## Limitations

The result concerns only nonempty finite star forests and quantifier rank three in the pure graph language. It does not classify arbitrary forests, all finite graphs, higher quantifier ranks, counting logic, or graph-isomorphism classes. The computational table is finite and exact, but the extension to arbitrarily large star forests relies on the proven three-round component reduction. The principal remaining originality risk is an equivalent calculation in unindexed literature or folklore.

## References

1. N. Immerman, *Descriptive Complexity*, Springer (1999), Chapter 6, “Ehrenfeucht–Fraïssé Games.” Author-hosted chapter: https://people.cs.umass.edu/~immerman/book/ch6.pdf .
2. L. Libkin, *Elements of Finite Model Theory*, Springer (2004), ISBN 9783540212027. https://doi.org/10.1007/978-3-662-07003-1 .
3. I. Algor and N. Alon, “The star arboricity of graphs,” *Discrete Mathematics* 75 (1989), 11–22. https://doi.org/10.1016/0012-365X(89)90073-3 .
