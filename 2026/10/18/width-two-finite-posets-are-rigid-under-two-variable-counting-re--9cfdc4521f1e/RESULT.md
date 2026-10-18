# Width-two finite posets are rigid under two-variable counting refinement

## Finding

**Theorem.** Let \((P,<)\) be a nonempty finite strict partial order of width at most two. Run directed one-dimensional counting refinement from one colour, distinguishing the relations \(x<y\), \(y<x\), and incomparability. Its stable colour-class sizes and all interclass comparison counts uniquely determine \(P\) up to isomorphism **among arbitrary finite strict posets**, without assuming that the competing poset also has width at most two. Consequently, \(P\) has a characteristic sentence in two-variable first-order logic with counting, \(C^2\), of quantifier rank at most \(|P|+1\) relative to the class of finite strict posets.

Every stable refinement class is exactly an automorphism orbit and has size one or two. Form a graph \(F_P\) on the size-two stable classes, putting an edge between two classes when their order relation is a directed perfect matching, rather than a complete directed bipartite relation. Then \(F_P\) is chordal. If it has \(c\) connected components, including isolated vertices, then

\[\operatorname{Aut}(P)\cong(C_2)^c.\]

When there are no size-two classes, \(c=0\) and the automorphism group is trivial. The conclusions also hold when the poset carries any finite set of named unary predicates and refinement starts from their atomic colours; automorphisms then preserve those predicates.

## Assumptions and scope

A strict partial order is an irreflexive, transitive binary relation, hence asymmetric. Its width is the maximum size of an antichain. All structures are finite and nonempty. The language has the binary order relation and, optionally, finitely many fixed unary relations; **transitivity is a semantic promise on competing structures**, not a property asserted to be definable in \(C^2\).

Let \(\gamma_0(x)\) be the initial unary colour (uniform if no unary symbols are present). Define iteratively

\[\gamma_{r+1}(x)=\bigl(\gamma_r(x),\ (N^<_{r,a}(x))_a,\ (N^>_{r,a}(x))_a\bigr),\]

where \(N^<_{r,a}(x)=|\{y:y<x,\ \gamma_r(y)=a\}|\) and \(N^>_{r,a}(x)=|\{y:x<y,\ \gamma_r(y)=a\}|\). The indexing \(a\) ranges over the finite colours present at round \(r\). These are canonical type labels, not arbitrary integers chosen independently for each structure. The stable profile consists of all stable class cardinalities and the number of strict predecessors and strict successors in every other stable class of a vertex in a given class. The third relation, incomparability, is recoverable from these counts and the class sizes.

## Proof

**1. Stable classes are antichains.** In a stable class \(A\), each vertex has the same number of strict predecessors belonging to \(A\). As the induced finite partial order on \(A\) has a minimal element, this number must be zero for all vertices of \(A\). Thus \(A\) is an antichain. The width hypothesis shows that every stable class of \(P\) has one or two elements. Any strict poset \(Q\) with the same stable profile has the same class sizes, and the same argument makes each of its classes an antichain.

**2. Comparisons between two doubletons.** Write \(A=\{a_0,a_1\}\) and \(B=\{b_0,b_1\}\) for distinct size-two stable classes. In \(P\), four pairwise incomparable vertices are impossible, so at least one cross-comparison exists. Equitability gives constant numbers \(u\) and \(v\) of vertices of \(B\) respectively above and below each vertex of \(A\); the analogous counts are constant across \(B\). If both \(u\) and \(v\) were nonzero, they would each equal one and orient the four edges of \(K_{2,2}\) with indegree and outdegree one at each vertex; this creates a directed four-cycle, impossible in a poset. Therefore all cross-comparisons have one direction. Regularity and the two-point class sizes force them to be either all four comparisons or exactly two comparisons forming a perfect matching. The same is true for \(Q\), since the entire comparison profile is the same.

**3. A linear order on doubleton classes.** Declare \(A\prec B\) if some vertex of \(A\) lies below a vertex of \(B\). Step 2 makes this a strict total orientation of the distinct doubleton classes. It is transitive: if \(A\prec B\prec C\), every element of \(A\) has an upper neighbour in \(B\), and every element of \(B\) has an upper neighbour in \(C\); transitivity of the original order supplies a comparison from \(A\) to \(C\). Hence enumerate the doubletons \(A_1\prec\cdots\prec A_s\). The stable profile determines this order and, for every \(i<j\), whether \(A_i<A_j\) is complete or a perfect matching.

**4. Intervening matching lemma.** Suppose \(i<j<k\) and \(A_i<A_k\) is a perfect matching. Then both \(A_i<A_j\) and \(A_j<A_k\) must be perfect matchings. Indeed, if \(A_i<A_j\) were complete, every \(a\in A_i\) would lie below any \(c\in A_k\): choose a vertex of \(A_j\) below \(c\) and apply transitivity. If \(A_j<A_k\) were complete, choose a vertex of \(A_j\) above \(a\) instead. Either possibility contradicts the matching from \(A_i\) to \(A_k\). Moreover the matching \(A_i\to A_k\) is the **composition** of the matchings \(A_i\to A_j\) and \(A_j\to A_k\), since the latter composition is contained in the former by transitivity and both are bijections of two-element sets.

**5. Unique reconstruction.** Compare \(P\) with any finite strict poset \(Q\) having the same stable profile and identify corresponding singleton classes. Every comparison incident with a singleton is all-or-none on a doubleton, since the two elements of that doubleton have identical counts into the singleton class. These comparisons are determined by the profile.

Next identify the ordered doubleton classes in \(P\) and \(Q\) inductively. On \(A_1\), choose either bijection. Suppose classes before \(A_k\) are aligned. If \(A_k\) is connected by no matching to an earlier class, choose either bijection on \(A_k\). Otherwise let \(i<k\) be the least earlier class matched to \(A_k\) and choose the unique bijection on \(A_k\) respecting that matching. For every other earlier matched class \(A_j\), with \(i<j<k\), the intervening matching lemma makes \(A_i\to A_j\) a matching and forces the \(A_i\to A_k\) matching to be its composition with \(A_j\to A_k\), both in \(P\) and \(Q\). The chosen bijection therefore respects all such matchings. Complete comparisons impose no restriction. Induction gives an order isomorphism \(P\cong Q\).

**6. Chordality and automorphisms.** In the matching graph \(F_P\), if \(i<j<k\) and \(i\) is adjacent to \(k\), the intervening matching lemma makes \(i\) adjacent to \(j\) and \(j\) adjacent to \(k\). Thus the later neighbours of every vertex form a clique, so the order \(1,\ldots,s\) is a perfect elimination ordering and \(F_P\) is chordal. An automorphism fixes each stable colour class setwise. On each doubleton it either flips or fixes the two vertices, and a matching edge forces equal flip decisions at its endpoints. Conversely simultaneous flips in any entire connected component of \(F_P\) preserve every matching, every complete doubleton comparison, and all singleton comparisons. All choices on distinct components are independent. Hence \(\operatorname{Aut}(P)\cong(C_2)^{c(F_P)}\), and each doubleton is an automorphism orbit. Singletons are, trivially, also orbits.

**7. Characteristic \(C^2\) sentence and rank.** Every round-\(r\) colour can be described by a one-free-variable \(C^2\) formula of quantifier rank at most \(r\), by inductively counting predecessors and successors of earlier colours. A partition on \(n=|P|\) vertices can strictly split at most \(n-1\) times, so it stabilizes by round \(t\le n-1\). Conjoin exact cardinality formulas for all round-\(t\) classes and, for every class pair, universal formulas specifying the exact predecessor and successor counts into the other class. These conditions have quantifier rank at most \(t+2\le n+1\); they force the stable comparison profile used in steps 1–6. By unique reconstruction, any finite strict poset satisfying this sentence is isomorphic to \(P\). Unary predicates are handled by their initial colours.

## Verification

The complete, infinite-size theorem is proved above; the finite computations below are consistency checks, not a replacement for the proof. `verify_small_posets.py` exhaustively generates every strict partial order compatible with the natural numerical order for \(n\le6\), tests width, groups structures by directed counting-refinement fingerprints, and checks isomorphism of every competitor sharing a fingerprint with a width-two structure. It reports 4,824 such transitively closed labelled orders at \(n=6\), of which 497 have width at most two, with no counterexample through six points.

`verify_matching_skeletons.py` independently checks every complete-or-matching orientation template for up to five ordered doubleton classes, verifying that all transitive templates with the same unsigned profile differ only by independent classwise flips. Its five-class level tests 381 transitive templates across 42 comparison profiles. `verify_stabilizers.py` generates 800 reproducible width-two posets on 3 to 12 points and verifies the predicted automorphism-group orders directly. Program sources and actual output logs are included alongside this document. Each checker uses only the standard Python library.

## Relationship to prior work

Colour refinement and its correspondence with two-variable counting logic are classical; see Arvind–Köbler–Rattan–Verbitsky (arXiv:1502.01255) and the earlier Immerman–Lander result they cite. Kiefer–Schweitzer–Selman (arXiv:1503.08792) classify arbitrary finite relational structures that are identified by \(C^2\). Their unrestricted relational class is different from the class of **strict posets** in this theorem: transitively closed orders constrain matching alignments that would be free in general binary relations. Their classification does not explicitly state a width-two-poset reconstruction theorem, and the present proof uses the poset promise essentially. Gajarský and collaborators (arXiv:1504.04115) study first-order model-checking algorithms for posets of bounded width, rather than identification by two-variable counting logic.

The proof is a self-contained width-two specialization based on transitivity, not a claim to have established the general theory of counting logic. No matching statement was located in the inspected sources or targeted research searches. Earlier specialized work may still exist.

## Limitations

The theorem **does not** identify width-two posets among arbitrary directed graphs: transitivity is essential. For example, the strict order of two disjoint three-element chains and the six-point acyclic relation obtained by crossing only the bottom-to-top comparisons have the same colour-refinement profile, but the latter is not transitive. The width assumption is also essential to the reconstruction argument: stable classes of size three need not reduce interclass relations to a choice between complete bipartite order and a perfect matching. No assertion is made here that width three is impossible, or that the stated logical-rank bound is optimal. The small-poset and template enumerations cannot by themselves certify the theorem for arbitrary size. No independent external scientific audit has been performed.

## References

1. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, first public arXiv posting 2015-02-04, arXiv:1502.01255.
2. S. Kiefer, P. Schweitzer, and E. Selman, *Graphs Identified by Logics with Counting*, first public arXiv posting 2015-03-30, arXiv:1503.08792.
3. J. Gajarský, P. Hliněný, D. Lokshtanov, J. Obdržálek, S. Ordyniak, M. S. Ramanujan, and S. Saurabh, *FO Model Checking on Posets of Bounded Width*, first public arXiv posting 2015-04-16, arXiv:1504.04115.
