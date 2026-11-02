# Thirty-three four-round theories of simply laced finite Dynkin diagrams

## Finding

Consider the finite simple undirected graphs underlying the simply laced Dynkin diagrams, regarded only as structures in the language of equality and adjacency. Write \(A_n\) for the path on \(n\geq1\) vertices, \(D_n\) for the three-arm tree with arm lengths \((1,1,n-3)\) for \(n\geq4\), and \(E_6,E_7,E_8\) for the three-arm trees with lengths \((1,2,2)\), \((1,2,3)\), and \((1,2,4)\). Arm lengths count edges from the unique trivalent vertex. All edges have their original unlabelled graph meaning: no root, ordering, color, edge label, or vertex constant belongs to the language.

For these graphs, equality of first-order sentences of quantifier rank at most four is *exactly* the following partition:

- \(A_1,A_2,\ldots,A_{15}\) each constitute a singleton equivalence class, while all \(A_n\), \(n\geq16\), form one further class.
- \(D_4,D_5,\ldots,D_{16}\) each constitute a singleton equivalence class, while all \(D_n\), \(n\geq17\), form one further class.
- \(E_6,E_7,E_8\) each constitute a singleton equivalence class.
- No class from one bullet coincides with any class from another bullet.

Thus there are exactly \(16+14+3=33\) classes. Every diagram is four-round equivalent to a diagram on at most \(17\) vertices, and this representative bound is sharp. In particular, the exceptional diagrams remain pairwise distinguishable at rank four, while the \(D\)-series stabilizes precisely at \(17\) vertices.

## Assumptions and scope

Graphs are finite, simple, undirected, and nonempty. A sentence's quantifier rank is its maximum number of nested first-order quantifiers. The relation \(G\equiv_4 H\) means that every sentence in the pure adjacency/equality language of rank at most four has the same truth value in \(G\) and \(H\). Repeated choices in the Ehrenfeucht–Fraïssé game are permitted and equality must be preserved. The classification is relative to the listed \(A,D,E\) diagrams, not to all finite graphs or to their associated Lie algebras.

## Proof

**1. Exhaustive finite lemma.** For a graph \(G\), an ordered tuple \(\bar v\), and an integer \(r\geq0\), define its complete finite-round signature recursively by
\[
\tau_0^G(\bar v)=\bigl((v_i=v_j,\ v_i\sim v_j): 1\leq j<i\leq|\bar v|\bigr),
\qquad
\tau_{r+1}^G(\bar v)=\{\tau_r^G(\bar v,w):w\in V(G)\}.
\]
The equality of these recursively formed objects (or of their injectively interned identifiers) is precisely the back-and-forth condition for all remaining moves. Induction on \(r\) shows that \(\tau_r^G(())=\tau_r^H(())\) if and only if Duplicator wins the \(r\)-round Ehrenfeucht–Fraïssé game on \(G,H\); this holds because every possible next vertex occurs in the set on *both* sides, and the base cases are exactly the complete atomic diagrams, including repeated vertices. There are no unexamined choices in this recursion.

The standalone program `checks/types.cpp` evaluates these signatures using all ordered tuples through length four, with duplicates, for \(A_1\) through \(A_{40}\), \(D_4\) through \(D_{40}\), and all three \(E\)-diagrams. Its exact finite output `checks/cpp_classes.txt` partitions these graphs into \(33\) classes: all \(A_1,\ldots,A_{15}\), \(D_4,\ldots,D_{16}\), and \(E_6,E_7,E_8\) have mutually distinct signatures, while \(A_{16},\ldots,A_{40}\) have one common signature and \(D_{17},\ldots,D_{40}\) have another distinct common signature. The separately written recursive Python implementation `checks/types.py` independently reproduces the entire partition restricted to \(A_1,\ldots,A_{22}\), \(D_4,\ldots,D_{22}\), and the exceptional diagrams. The exact finite calculation proves these finite statements, not an unbounded extrapolation.

**2. An all-order tail lemma.** Consider two linear paths whose two extremal vertices are treated as *virtually paired* at the outset, whether or not Spoiler ever selects them. With \(r\) moves still available, partition each path into gaps between consecutive selected interior vertices and the virtually paired extrema. Maintain that each pair of corresponding gaps has equal sizes if that size is less than \(s_r\), and otherwise both sizes are at least \(s_r\), where \(s_0=1\) and \(s_{r+1}=2s_r+1\). Thus \(s_r=2^{r+1}-1\).

This invariant is preserved by each legal move. For a point selected in a small gap, match its exact offset; for a point in a large gap, match its exact offset from the nearer boundary if that offset is less than \(s_{r-1}\), and otherwise choose a point leaving at least \(s_{r-1}\) unused vertices on each side. The recurrence guarantees that the latter point exists. If both offsets were small, the gap would be too short to be large. Previously selected vertices are always answered by their existing partners. At \(r=0\), the invariant states exactly that corresponding gaps are simultaneously empty or nonempty; therefore consecutive selected path vertices are adjacent on one side if and only if their partners are adjacent. The strategy also preserves equality.

At rank four \(s_4=31\). Therefore two paths each containing at least \(31\) interior vertices between their virtually paired ends are four-round equivalent in the adjacency language. In particular all \(A_n\) with \(n\geq33\) are equivalent.

For \(D_n\), take the spine from the unique trivalent vertex to the endpoint of its long arm. There are \(n-2\) spine vertices, with \(n-4\) vertices interior to its two ends, plus two additional pendant vertices adjacent only to the trivalent endpoint. Pair those two pendant vertices beforehand as well. Spoiler's choice of either pendant vertex is answered by its fixed mate; all moves on the spine follow the gap strategy. This preserves adjacency with the two pendants because they meet only the virtually paired trivalent endpoint. Hence all \(D_n\) with \(n\geq35\) are four-round equivalent.

**3. Completion and sharpness.** The finite lemma includes \(A_{16}\equiv_4 A_{35}\) and \(D_{17}\equiv_4 D_{35}\). Step 2, transitivity, and the finite lemma now yield the stated classification for *all* indices without restriction. The finite lemma also establishes every required distinction, so neither stabilization threshold can be lowered. Its \(D_{17}\) class has no smaller \(A,D,E\) representative, proving the sharp \(17\)-vertex bound inside this family.

## Verification

Run `python3 checks/reproduce.py` from the package directory. This compiles the standalone C++17 program, computes the complete finite partition through parameter \(40\), and independently runs the pure-Python recursion through parameter \(22\), then checks the resulting partitions against the formula above. The actual successful reproduction is recorded in `checks/reproduction.txt`; raw partition outputs appear in `checks/cpp_classes.txt` and `checks/python_classes.txt`. The programs determine the full rank-four types, not just sampled formulas or induced-subgraph profiles. Step 2, rather than any finite computation, is responsible for the infinite range.

## Relationship to prior work

Brown and Hoshino (2007) give the exact Ehrenfeucht–Fraïssé classifications for finite paths and cycles. Their path theorem already supplies the \(A\)-series rank-four threshold \(16\); this part of the present classification is explicitly not claimed as a new discovery. The new family-level comparison concerns the branching \(D\)-series, the three exceptional \(E\)-diagrams, and the complete cross-series partition. Bohman, Frieze, Łuczak, Pikhurko, Smyth, Spencer and Verbitsky (2007) give general and asymptotic logical-definability bounds for trees, but their main results do not specify the precise four-round \(D/E\) partition. No exact equivalent of the combined \(33\)-class theorem was located in the stated literature and repository searches; a complete historical-priority claim is not made.

## Limitations

The classification is limited to quantifier rank four and the *unlabeled adjacency* reducts of the simply laced finite Dynkin diagrams. It does not describe their richer Coxeter or Cartan signatures, graph families outside \(A,D,E\), or equivalence at higher ranks. The finite lemma is a reproducible exhaustive computation; its outputs are not a formal proof independently of the provided source and the recurrence justified above. General historical priority, including possible specialized unpublished treatments of trivalent trees, is not established. Independent external mathematical audit has not been performed.

## References

1. J. Brown and R. Hoshino, *The Ehrenfeucht-Fraïssé Game for Paths and Cycles*, Ars Combinatoria **83** (2007), 193–212, published April 30, 2007. https://combinatorialpress.com/ars-articles/volume-083-ars-articles/the-ehrenfeucht-fraisse-game-for-paths-and-cycles/ (open full text: https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf).
2. T. Bohman, A. Frieze, T. Łuczak, O. Pikhurko, C. Smyth, J. Spencer and O. Verbitsky, *First-Order Definability of Trees and Sparse Random Graphs*, Combinatorics, Probability and Computing **16** (2007), 375–400; first online January 23, 2007. https://doi.org/10.1017/S0963548306008376 (lawful open full text: https://edoc.hu-berlin.de/bitstreams/442d2d36-b746-4235-9404-aef14a9e24b3/download).
