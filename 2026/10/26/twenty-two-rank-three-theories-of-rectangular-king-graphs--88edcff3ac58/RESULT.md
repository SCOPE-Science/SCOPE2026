# Twenty-two rank-three theories of rectangular king graphs

## Finding

Let \(P_m\) denote the undirected path on \(m\ge1\) vertices, and let \(K_{m,n}=P_m\boxtimes P_n\) be its strong product with \(P_n\). Thus vertices are cells \((i,j)\), and distinct cells are adjacent precisely when both coordinate differences have absolute value at most one (the legal moves of a chess king). Only graph adjacency and equality belong to the first-order signature; the coordinate axes, cells, and boundaries are not named.

For every pair of positive integers \(m,n\), write \(a=\min(m,n)\) and \(b=\max(m,n)\). Two such graphs satisfy exactly the same first-order sentences of quantifier rank at most three if and only if their parameter pairs occur in the same one of the following twenty-two classes:

| Class | Parameter regime for \((a,b)\) | Least-order representative |
|---|---|---|
| 1–6 | \((1,b)\), individually for \(b=1,2,3,4,5,6\) | respective \((1,b)\) |
| 7 | \(a=1,\ b\ge7\) | \((1,7)\) |
| 8–12 | \((2,b)\), individually for \(b=2,3,4,5,6\) | respective \((2,b)\) |
| 13 | \(a=2,\ b\ge7\) | \((2,7)\) |
| 14–17 | \((3,b)\), individually for \(b=3,4,5,6\) | respective \((3,b)\) |
| 18 | \(a=3,\ b\ge7\), **or** \(a=4,\ b\ge6\) | \((3,7)\) |
| 19 | \((a,b)=(4,4)\) | \((4,4)\) |
| 20 | \((a,b)=(4,5)\) | \((4,5)\) |
| 21 | \((a,b)=(5,5)\) | \((5,5)\) |
| 22 | \(a=5,\ b\ge6\), **or** \(a\ge6\) | \((5,6)\) |

Class numbers here group families by natural parameter regimes; `classification.json` gives all twenty-two individual classes with their twenty-eight canonical parameter pairs and least-order representatives.

In particular, \(K_{3,7}\equiv_3 K_{4,6}\), while \(K_{5,6}\equiv_3 K_{7,7}\). There are exactly twenty-two rank-three theories in the entire king-graph family, including fifteen represented by genuinely two-dimensional boards. Each equivalence class has a representative on at most \(30\) vertices; the unique class that requires \(30\) vertices is class 22, represented by \(K_{5,6}\). The bound is sharp **within this family**, not among arbitrary graphs.

## Assumptions and scope

All parameters are positive integers; the graphs are finite, nonempty, simple, undirected, and uncoloured. Equivalence \(\equiv_3\) means agreement on every first-order sentence of quantifier rank at most three, with unrestricted reuse of variables, Boolean operations and quantifier alternation, but with neither counting quantifiers nor named coordinates.

## Proof

**1. Exact bounded-rank recursion.** For a finite graph \(G\), let \(\operatorname{at}(v_1,\ldots,v_r)\) be the complete truth table of all equality and adjacency atoms on the displayed vertices, including repetitions. Define recursively
\[
\tau_0(\bar v)=\operatorname{at}(\bar v),\qquad
\tau_{s+1}(\bar v)=\big(\operatorname{at}(\bar v),\{\tau_s(\bar v,w):w\in V(G)\}\big).
\]
By induction on formula construction, two tuples have the same \(\tau_s\) exactly when they satisfy the same formulas of rank at most \(s\) in those free variables. In particular, the type \(\tau_3(())\) captures the entire rank-three theory. On loopless undirected graphs the recursion is computed exactly by listing all atomic diagrams of ordered triples (including repeated vertices), then sets of two-point one-extension types, then sets of one-point two-extension types. No larger tuples are required.

**2. Path stabilization at seven vertices.** Every two undirected paths of lengths at least seven are rank-three equivalent. Here is an elementary verification tailored to the above recursion. For two distinct selected vertices \(x,y\) of a path on at least seven vertices, the possible atomic patterns of a third vertex \(z\) are determined by equality, whether \(x,y\) are adjacent, whether their distance is two, and whether either \(x\) or \(y\) is an endpoint when their distance is at most two. Indeed, the common-neighbor pattern occurs exactly at distance two; a neighbor of \(x\) not adjacent to \(y\) exists at distance at least three, or at distance one or two when \(x\) is not an endpoint; and a vertex adjacent to neither exists for every pair, because the union of their closed neighborhoods contains at most six vertices. Interchanging \(x,y\) gives the remaining pattern. Equality cases are fixed by the two-point atomic diagram. Consequently a selected root \(x\) has one of four rank-two types, determined by its minimum distance to an endpoint, truncated at three. All four types occur in every path of length at least seven, and no additional type does. The path rank-three theory is therefore stable from seven onwards. This threshold also appears in Brown and Hoshino's full Ehrenfeucht–Fraïssé classification of paths.

**3. Product preservation.** If \(A\equiv_3 A'\) and \(B\equiv_3 B'\), then \(A\boxtimes B\equiv_3 A'\boxtimes B'\). In a three-round Ehrenfeucht–Fraïssé game, use one Duplicator strategy for each factor and answer a product move by pairing the two coordinate replies. Partial equality and adjacency tables are preserved in each factor. The strong-product adjacency is the conjunction of the two coordinate conditions “equal or adjacent,” excluding equality of both full vertices; hence it too is preserved. Therefore
\[
K_{m,n}\equiv_3 K_{\min(m,7),\min(n,7)}.
\]
After interchanging factors as needed, only the twenty-eight pairs \(1\le m\le n\le7\) remain.

**4. Exhaustive finite classification.** Apply the recurrence in step 1 to these twenty-eight explicitly constructed graphs (at most forty-nine vertices each). The provided `king_rank3_verifier.py` implements the complete ordered-triple recurrence and an independent equivalent implementation via four possible adjacency masks for a third vertex relative to each ordered pair. Both yield precisely the same partition into twenty-two classes, recorded completely in `classification.json`. The two non-singleton canonical classes are
\[
\{(3,7),(4,6),(4,7)\},\qquad
\{(5,6),(5,7),(6,6),(6,7),(7,7)\};
\]
all other twenty canonical pairs occupy singleton classes. No simulation of unbounded graphs is used here: step 3 proves the infinite-to-finite reduction.

**5. Sharpness.** For each of the twenty-two classes, inspect the least product \(mn\) among its canonical pairs. The maximum of these minima is \(5\cdot6=30\), attained only by the last class. Any graph with a side length greater than seven has the same theory as its coordinatewise seven-truncation and cannot provide a smaller representative of that class. Thus the universal thirty-vertex bound is sharp within the family.

## Verification

Run `python3 king_rank3_verifier.py` in a directory containing the supplied script. It uses only the Python standard library, reproduces the complete twenty-eight-case table, independently compares two exact recursions, tests seventy-eight pairs of sizes up to twelve, checks path stabilization on sizes seven through thirty, and emits `classification.json`. The included `verification_output.txt` records `VERIFY_OK` and the sharp bound. The numerical checks beyond the canonical range are corroboration; the proof for arbitrarily large parameters is in steps 2 and 3.

## Relationship to prior work

Brown and Hoshino determine the Ehrenfeucht–Fraïssé equivalence of individual paths and cycles and establish the path threshold needed here. That threshold alone says nothing about how **strong-product adjacency** combines the two factors or which distinct board shapes collapse. The standard king-graph literature describes the graph family and conventional invariants but does not, in the inspected material, give these logical classes. Results for Cartesian grids concern edge-only (rook-move) adjacency, so their exact class partitions do not imply this one for diagonal-inclusive king graphs. The new contribution is the complete twenty-two-class strong-product calculation, its nontrivial cross-shape equivalences, and the sharp thirty-vertex bound.

## Limitations

The result concerns only ordinary rank-three first-order logic on these unmarked finite king graphs; it does not cover higher quantifier rank, counting logic, or graphs with named coordinates, endpoints, or a distinguished corner. Independent validation has not been performed. Exact duplication by unindexed specialist literature remains a residual novelty risk. The finite classification relies on the complete reproducible computation specified above; its hand-checkable type recurrence and independently formulated bit-mask test are included.

## References

1. Jason I. Brown and Richard Hoshino, “The Ehrenfeucht–Fraïssé Game for Paths and Cycles,” *Ars Combinatoria* **83** (2007), 193–212, published 30 April 2007. Full text: https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf .
2. Eric W. Weisstein, “King Graph,” *MathWorld*, https://mathworld.wolfram.com/KingGraph.html .
3. Oleg Pikhurko and Oleg Verbitsky, “Logical Complexity of Graphs: A Survey,” arXiv:1003.4865 (2010), https://arxiv.org/abs/1003.4865 .
