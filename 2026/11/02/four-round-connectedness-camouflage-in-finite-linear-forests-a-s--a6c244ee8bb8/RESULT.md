# Four-round connectedness camouflage in finite linear forests: a sharp 29-vertex threshold

## Finding
Let \(P_n\) denote the undirected simple path on \(n\ge1\) vertices. Work in ordinary first-order logic with equality and one binary undirected adjacency predicate; write \(G\equiv_4H\) when the graphs agree on all sentences of quantifier rank at most four.

**Two-component classification.** For all positive integers \(a,b,c\),
\[
P_a\sqcup P_b\equiv_4P_c
\quad\Longleftrightarrow\quad
\min(a,b)\ge14,\quad\max(a,b)\ge15,\quad c\ge16.
\]
Here \(\sqcup\) is disjoint union. Thus every disjoint union of two paths with component orders at least \(14\) and \(15\) is four-round equivalent to each sufficiently long connected path, and no other two-component linear forest has that property.

**Sharp size and uniqueness.** Among *all* disconnected finite linear forests, allowing arbitrarily many nonempty path components, the smallest order of a graph equivalent through rank four to any connected path is \(29\). Up to graph isomorphism its unique minimum witness is \(P_{14}\sqcup P_{15}\), equivalent to \(P_{16}\). No disconnected linear forest with fewer than \(29\) vertices is equivalent through rank four to any connected path.

## Assumptions and scope
Graphs are finite, simple, undirected and nonempty, with no vertex labels, added constants, counting quantifiers, path order or endpoint predicates. A linear forest is a disjoint union of undirected paths, including single-vertex paths. The integer in \(P_n\) counts vertices, not edges. The quantifier rank is the maximum depth of nested first-order quantifiers (not the number of variables or the number of symbols). The two-component equivalence includes any \(a,b,c\ge1\); the minimum result permits any number \(\ge2\) of components.

## Proof
**1. Published connected-path stabilization.** Brown and Hoshino [1, Theorem 3.10] prove that for all positive integers \(m,n\), in precisely this graph language,
\[
P_m\equiv_4 P_n\quad\Longleftrightarrow\quad m=n\text{ or }(m\ge16\text{ and }n\ge16).
\]
This is an infinite theorem, not a consequence of the finite computations below.

**2. Disjoint-union congruence.** For arbitrary finite graphs \(A,B,C\) and any finite rank \(r\), if \(A\equiv_rB\) then \(A\sqcup C\equiv_r B\sqcup C\). In the \(r\)-round Ehrenfeucht–Fraïssé game, Duplicator uses the winning strategy on the \(A/B\) pair for moves there and copies Spoiler's choices identically on the two copies of \(C\). These strategies preserve equalities and adjacencies within their respective components; across components both graphs have no edges. The strategy therefore preserves the partial isomorphism after every move. In particular every \(P_n\) with \(n\ge16\) can be replaced by \(P_{16}\) *inside a disjoint union* without changing its rank-four theory.

**3. Exact finite-type recurrence.** For a graph \(G\), a tuple \(\bar v\) of length \(k\), and remaining quantifier rank \(r\), let \(T^G_0(\bar v)\) be its complete atomic equality-and-adjacency pattern (including repeated entries). Recursively define
\[
T^G_{r+1}(\bar v)
=\bigl(T^G_0(\bar v),\;\{T^G_r(\bar v,w):w\in V(G)\}\bigr).
\]
For tuples of the same length in graphs, equality of these finite codes is exactly agreement on formulas of quantifier rank at most \(r+1\) with those free variables. This follows by induction: Boolean combinations use the atomic pattern; existential formulas correspond to membership among the one-vertex extension codes, and universal formulas to complements. In particular \(G\equiv_4H\) exactly when their empty-tuple codes \(T^G_4(())\) and \(T^H_4(())\) agree. The code may canonically replace each extension multiset by a set, since ordinary existential quantifiers do not count witnesses; equality of repeated tuple entries is retained by the atomic pattern. The C++ verifier implements this recursion by interning exact byte strings, comparing full strings after hashing (hence no probabilistic hash equality).

**4. Finite exhaustion and boundary identities.** Every linear forest with no isolated vertex and at most \(29\) vertices is enumerated once by a nondecreasing partition of its total order into parts of size at least two. The C++ program `verify_exhaustive.cpp` computes and compares its rank-four type to the types of \(P_2,\ldots,P_{35}\). All connected paths of length \(\ge16\) have the type of \(P_{16}\) by step 1, so the list covers *all* connected-path types. There are exactly \(3,690\) disconnected no-isolate linear forests with at most \(28\) vertices, and none matches. Among the \(846\) disconnected no-isolate forests on \(29\) vertices, precisely one matches: \(P_{14}\sqcup P_{15}\); its matching path class consists exactly of \(P_n\) with \(n\ge16\). The standalone `census.csv` gives the exact per-order partition counts and matches.

Independent bottom-up type refinement in `verify_boundary.py` checks the crucial positive finite base cases
\[
(14,15),\ (14,16),\ (15,15),\ (15,16),\ (16,16)
\]
(all rank-four equivalent to \(P_{16}\)) and checks the contrasting pairs \((13,16),(14,14),(12,18)\) and the distinction \(P_{15}\not\equiv_4P_{16}\). These are genuine exhaustive finite-type checks, not numerical sampling.

**5. Infinite two-component characterization.** Suppose \(a,b,c\ge1\), and order the two components so \(a\le b\). If \(a\ge14,b\ge15\), replace each component with order at least \(16\) by \(P_{16}\) using step 2. The resulting unordered component-size pair belongs to the five positive base cases in step 4. If \(c\ge16\), step 1 gives \(P_c\equiv_4P_{16}\); transitivity proves the forward implication of the claimed conditions.

Conversely, if \(a=1\) or \(b=1\), the disjoint union has an isolated vertex and at least two vertices. No connected path \(P_c\) has the same rank-two theory: \(P_1\) has only one vertex, while every \(P_c\) with \(c\ge2\) has no isolated vertices. Otherwise both parts have size at least two. If \(a\le13\), replace \(b\ge16\) by \(16\) if necessary: the resulting disconnected forest has at most \(29\) vertices and is not the unique matching pair in step 4. If \(a=b=14\), the forest has \(28\) vertices and fails the census comparison. Thus no excluded two-component parameter pair can match *any* connected path. For positive cases, the finite type computation shows equivalence only to the stabilized connected-path class, forcing \(c\ge16\). This proves the exact criterion.

**6. The minimum over any number of components.** If any component has one vertex, the rank-two isolated-vertex argument applies. Otherwise all parts have size at least two, and all disconnected forests of order \(\le29\), regardless of component count, occur in the exhaustive nondecreasing-partition enumeration of step 4. That proves both the lower bound and uniqueness of the \(29\)-vertex witness. Larger forests are not required for this minimum assertion. QED.

## Verification
Run `bash REPRODUCE.sh` in a directory containing the supplied standalone files. The exhaustive C++ program compiles with an ordinary C++17 compiler, uses no external libraries, enumerates \(4,536\) disconnected no-isolate forest isomorphism types through \(29\) vertices, and reports the unique matching pair. `verify_boundary.py` independently constructs the same rank-four invariants bottom-up, recomputing its own atomic patterns rather than calling the C++ code. Recorded stdout/stderr and the per-order table are embedded; both programs were executed from the packaged source paths. The finite recurrence proves what the computations calculate, while step 1 supplies the only infinite path-classification premise.

## Relationship to prior work
Brown and Hoshino [1] classify the four-round game when *both graphs are single paths* (and separately both cycles). Their stated scope and concluding discussion do not include a path compared with a disconnected union of paths. The present classification uses their stabilized single-path theory but supplies new finite boundary identities and the first sharp disconnected-linear-forest witness. Pikhurko and Verbitsky [2] survey logical complexity and Ehrenfeucht–Fraïssé methods, not this particular extremal finite threshold. The standard logical inability to express connectedness on arbitrary finite graphs [2] gives no precise minimum witness for this restricted class and quantifier rank. An older Brown–Woodrow technical report [3] is a historical-priority risk: a complete full-text comparison was unavailable.

## Limitations
This is a rank-four result in pure adjacency logic; it does not assert equivalence under counting, endpoint predicates, graph connectivity predicates, or higher quantifier ranks. The two-component classification is complete, while for arbitrary many components only the sharp minimum and uniqueness are claimed. The finite-exhaustion step relies on a supplied, inspectable computation, not a short closed-form handwritten separation formula for every smaller forest. Independent external review and exhaustive historical-priority assessment remain unperformed.

## References
[1] J. Brown and R. Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles*, Ars Combinatoria 83 (2007), 193–212, published 2007-04-30. https://combinatorialpress.com/ars-articles/volume-083-ars-articles/the-ehrenfeucht-fraisse-game-for-paths-and-cycles/ ; full text: https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf .

[2] O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (initially 2010), https://arxiv.org/abs/1003.4865 .

[3] J. I. Brown and R. E. Woodrow, *Ehrenfeucht games and graphs*, University of Calgary Technical Report (1984), cited as reference [2] of [1]; full text not verified accessible.
