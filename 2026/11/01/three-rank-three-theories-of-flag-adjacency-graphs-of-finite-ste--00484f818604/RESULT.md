# Three rank-three theories of flag-adjacency graphs of finite Steiner \(2\)-designs

## Finding
Let \(\mathcal D\) be any finite simple \(2\)-\((v,k,1)\) block design with \(2\le k<v\): its points form a set of size \(v\), every block has size \(k\), and each pair of distinct points occurs in exactly one block. A **flag** is an incident pair \((p,B)\) with \(p\in B\). Define the **flag-adjacency graph** \(F(\mathcal D)\) to have the flags as vertices, with two *distinct* flags adjacent exactly when they share their point or their block. Equivalently, \(F(\mathcal D)\) is the ordinary line graph of the point–block Levi incidence graph; this differs from other constructions sometimes called flag graphs.

In first-order graph logic with equality and one undirected adjacency relation, write \(G\equiv_3H\) for agreement on every sentence of quantifier rank at most \(3\). Then **exactly three** rank-three theories occur in the entire family:

| Class | Necessary and sufficient design parameters | Smallest example | Flag vertices |
| --- | --- | --- | ---: |
| I | \(k=2,\ v=3\) | The complete pair design on three points | \(6\) |
| II | \(k=2,\ v\ge4\) | The complete pair design on four points | \(12\) |
| III | \(3\le k<v\) | The Fano-plane design \(2\)-\((7,3,1)\) | \(21\) |

Graphs belonging to the same row are rank-three equivalent, **regardless of design isomorphism type, number of points, or block size within the row**. Different rows are not rank-three equivalent. Thus \(21\) is the sharp uniform number of flag vertices needed to represent all rank-three theories within this family.

Moreover, if \(J(7,3)\) denotes the Johnson graph on the three-element subsets of a seven-element set, adjacent when they intersect in two elements, then every flag-adjacency graph in class III satisfies
\[
F(\mathcal D)\equiv_3 J(7,3).
\]
This cross-family equivalence has **exact separating quantifier rank four**: the Johnson graph contains an induced three-leaf claw, whereas every flag-adjacency graph is a line graph and hence claw-free.

## Assumptions and scope
All structures are finite, nonempty and simple. There are no named points, named blocks, point/block sorts, constants, or incidence predicates in the logical language: only flags are vertices and only flag adjacency and equality are available. Quantifier rank counts nested quantifiers, not the total number of variables or the length of a formula. Block size \(k=2\) is deliberately included as the complete pair design. The requirement \(v>k\) excludes one-block degeneracies. No assumption of a Desarguesian plane, resolvability, flag transitivity, or any symmetry group is made.

Let \(r\) be the number of blocks through each point. Counting the other points through one fixed point gives
\[
 r(k-1)=v-1.
\]
For \(k\ge3\), choose a block \(B\) and a point outside it. The distinct blocks joining this point to each member of \(B\) show \(r\ge k\). These elementary facts hold for every design in the stated class.

## Proof
**A. One-vertex extension invariant for a three-round game.** For any ordered pair \((x,y)\) in an undirected graph, record whether the pair is equal, adjacent, or distinct and nonadjacent. Additionally record every realizable atomic pattern of a third vertex \(z\), comprising \(z=x\), \(z=y\), \(z\sim x\), and \(z\sim y\). Suppose that in each of two graphs the *set* of pair records available from a first vertex is independent of that first vertex, and these sets agree between the graphs. Duplicator wins the three-round Ehrenfeucht–Fraïssé game: after the first selection, choose any first vertex; after a second selection, match its pair record; after a third selection, realize the matching extension pattern. All equality and adjacency atoms of the three selected vertices then agree. The argument is symmetric as to which graph Spoiler selects from. Therefore the two graphs are \(\equiv_3\). Conversely, whenever the available pair records differ for all possible first vertices, Spoiler can force a difference within three rounds by choosing the offending second vertex and then an unmatched third-vertex pattern. We apply this elementary invariant explicitly, not as an unverified assumption of vertex transitivity.

**B. Common-neighbour geometry.** Write \(x=(p,B)\), \(y=(q,C)\). When \(x\ne y\) are adjacent, either \(p=q\) and \(B\ne C\), in which case their common neighbours are exactly the \(r-2\) other flags through \(p\), or \(B=C\) and \(p\ne q\), in which case their common neighbours are exactly the \(k-2\) other flags on \(B\). When \(p\ne q\) and \(B\ne C\), the pair is nonadjacent and has a common neighbour precisely if \(p\in C\) or \(q\in B\); either alternative gives one common neighbour. Both alternatives cannot hold simultaneously, because then distinct blocks \(B\) and \(C\) would both contain the pair \(\{p,q\}\), contrary to the design axiom. Thus the common-neighbour counts for nonadjacent pairs are \(0\) or \(1\).

For every initial flag \((p,B)\), both kinds of nonadjacent pair occur. To obtain one with a common neighbour, choose \(q\in B\setminus\{p\}\) and any \(C\ne B\) containing \(q\); the pair \((p,B),(q,C)\) is nonadjacent but has the common neighbour \((q,B)\). To obtain one without any common neighbour, choose \(q\notin B\) and one of its blocks \(C\) not containing \(p\); such a block exists because \(r\ge2\) and only one block contains \(p\) and \(q\). Then \((p,B),(q,C)\) is nonadjacent with no common neighbour.

**C. Availability of all other third-vertex patterns.** Every flag has graph degree \(r+k-2\). Adjacent distinct flags always have witnesses adjacent to the first but not the second, and conversely: for flags sharing a point choose another point on the first block; for flags sharing a block choose another block through the first point. For nonadjacent pairs, at most one common neighbour exists by part B, whereas each endpoint has at least two neighbours, so both exclusive-neighbour patterns exist. The \((0,0)\) pattern (a third vertex distinct from both and adjacent to neither) is available for every pair whenever the number of flags exceeds twice the maximum closed-neighbourhood size:
\[
vr>2(r+k-1).
\]
For \(k\ge3\), we have \(r\ge k\), \(v=(k-1)r+1\ge7\), and hence \(vr\ge7r>4r-2\ge2(r+k-1)\). For \(k=2\) and \(v\ge4\), \(r=v-1\) and \(vr=v(v-1)>2v=2(r+k-1)\). These inequalities establish the \((0,0)\) pattern uniformly across both larger classes, including equal-pair extensions where appropriate.

For \(k=2,v=3\), the flag-adjacency graph is the six-cycle. Its nonadjacent antipodal pairs lack a distinct third vertex adjacent to neither, while its distance-two nonadjacent pairs admit every \((0,0),(0,1),(1,0),(1,1)\) pattern. Adjacent pairs have no common neighbour and do admit \((0,0),(0,1),(1,0)\). This six-vertex case is checked directly; its two-point records are independent of the chosen first vertex by cyclic symmetry.

**D. Exact profile classification.** For \(k\ge3\), both \(r,k\ge3\); all adjacent pairs have a third common neighbour, all four third-vertex adjacency patterns \((0,0),(0,1),(1,0),(1,1)\) are realized for such pairs, and for nonadjacent pairs there are exactly the two record types distinguished by the availability of \((1,1)\). This set of records is independent of \(v,k\) and of the choice of first flag. For \(k=2,v\ge4\), all the same types occur, but there is an **additional adjacent-pair type without a common neighbour**, arising from two flags of a two-point block. For \(k=2,v=3\), the point degree is only \(2\), so no adjacent pair has a common neighbour and the opposite-pair \((0,0)\) exception occurs. Part A therefore proves equivalence for each of the three rows.

The rows are pairwise distinct at rank three. The sentence
\[
\exists x\,\exists y\,\exists z\ (x\sim y\land y\sim z\land z\sim x)
\]
is false exactly in class I (the six-cycle). The rank-three sentence
\[
\exists x\,\exists y\bigl(x\sim y\land\forall z\,\neg(z\sim x\land z\sim y)\bigr)
\]
holds in classes I and II but fails in class III, since every edge of a class-III flag graph belongs to a triangle. Together these sentences distinguish all three rows.

**E. Sharp representatives and cross-family boundary.** The number of flags is \(vr\). In class I it is \(6\); in class II it is \(v(v-1)\), minimized at \(v=4\), giving \(12\). In class III, \(k\ge3\), \(r\ge k\), \(v\ge k(k-1)+1\), so \(vr\ge k(k(k-1)+1)\ge21\). Equality is realized by the Fano plane. Thus the sharp uniform representative bound is \(21\).

The Johnson graph \(J(7,3)\) has \(35\) vertices and degree \(12\). Its pair-extension records are identical with class III: adjacent pairs have common neighbours; nonadjacent pairs at Johnson distance two have common neighbours, those at distance three do not; both kinds occur from any first vertex. For every pair the \((0,0)\) pattern occurs because \(35>2(12+1)\), and each nonadjacent pair has at most four common neighbours, leaving exclusive neighbours. Adjacent pairs also have exclusive neighbours (their common-neighbour count is \(5<12\)). By part A, \(J(7,3)\equiv_3F(\mathcal D)\) for every class-III design.

For the sharp four-round separation, the Johnson subsets \(\{1,2,3\}\), \(\{2,3,4\}\), \(\{1,3,5\}\), \(\{1,2,6\}\) form an induced claw centered at the first set. This is expressed by a first-order sentence of quantifier rank four: there is a vertex with three pairwise nonadjacent neighbours. No line graph has an induced claw, because any three edges meeting one fixed edge at least twice share one endpoint. Therefore the least quantifier rank separating \(J(7,3)\) from any class-III flag graph is precisely \(4\).

## Verification
Two standalone, differently implemented finite checks accompany this result. `verify_designs.py` constructs complete pair systems on three, four and five points; affine planes of orders two, three and five; projective planes of orders two, three and five; the point–line design of binary projective three-space; and \(J(7,3)\). It checks the block-design axioms and enumerates all equality/adjacency third-vertex extension patterns from every ordered pair, comparing their first-vertex profiles. `verify_ef3.py` independently builds exact quantifier-rank-three types bottom-up, from all atomic diagrams of ordered triples to rank-one ordered-pair types, rank-two singleton types and rank-three empty-tuple types. Outputs are in `verify_designs.out` and `verify_ef3.out`.

Both checks pass and verify the three classes and Johnson coincidence on the finite tested examples. The all-parameter and non-Desarguesian statements are justified by parts A–E, not by extrapolation from any finite computational range. All programs use Python's standard library only.

## Relationship to prior work
Verbitsky's 2004 paper develops Ehrenfeucht–Fraïssé graph methods for definability of graphs with separators, not flag-adjacency graphs of Steiner designs. De Winter–Lazebnik–Verstraëte's 2008 work analyzes extremal cycle counts of the Levi graphs of projective planes and explains these incidence graphs, but does not prove a first-order classification of their line graphs in the inspected material. Existing logical results for point-only collinearity relations of Steiner designs, for projective-plane Levi graphs, for Johnson graphs and for line graphs of Hamming products do not imply the present result: the universe of flags and its graph-adjacency relation differ from their signatures and objects. A prior Johnson rank-three theorem supplies the Johnson comparison class; its independent classification is not claimed as a new contribution here. The novel content is the complete three-class classification of **all** flag-adjacency graphs of finite \(2\)-designs, the sharp representative bound and the cross-family first-order equivalence with its exact rank-four separation.

## Limitations
This theorem concerns ordinary adjacency and equality at rank three, with one additional rank-four *separator* only. It does not classify all rank-four theories of design flag graphs, arbitrary incidence systems or other meanings of the term "flag graph." The finite programs are corroborative and do not certify the general theorem. The originality assessment is based on the available literature and prior scientific comparisons; historical priority and correctness have not received independent external audit.

## References
1. O. Verbitsky, *The First Order Definability of Graphs with Separators via the Ehrenfeucht Game*, arXiv:math/0401361v1, first publicly posted 2004-01-26. https://arxiv.org/abs/math/0401361.
2. S. De Winter, F. Lazebnik and J. Verstraëte, *An Extremal Characterization of Projective Planes*, Electronic Journal of Combinatorics **15** (2008), R143, publicly published 2008-11-30, DOI:10.37236/867. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v15i1r143.
