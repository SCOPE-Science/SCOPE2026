# Seven exact four-round theories of three-subset Kneser graphs

## Finding
For each integer \(n\ge6\), write \(K_n=KG(n,3)\) for the graph whose vertices are the three-element subsets of \(\{1,\ldots,n\}\), with adjacency defined by disjointness. In the first-order signature consisting solely of equality and an irreflexive, symmetric binary edge predicate, the complete rank-four equivalence criterion is
\[
K_n\equiv_4 K_m\quad\Longleftrightarrow\quad (n=m\le11)\ \lor\ (n,m\ge12).
\]
In particular, there are exactly seven rank-four theories in this infinite family, with smallest representatives \(K_6,K_7,K_8,K_9,K_{10},K_{11},K_{12}\). The largest of these representatives has \(\binom{12}{3}=220\) vertices, and this upper bound cannot be lowered within the family.

## Assumptions and scope
All graph vertices are *three-subsets* of the underlying ground set; underlying elements are **not** named or quantified in the first-order language. No counting, fixed constants, hyperedge relations, or intersection-size predicates are available. Quantifier rank counts nesting depth and permits arbitrary finite Boolean combinations. Both repeated and distinct graph vertices are allowed in plays and in the finite certificate. The claim concerns precisely the family \(KG(n,3)\), \(n\ge6\); it does not classify general Kneser graphs or arbitrary graphs.

## Proof
**The uniform tail.** In a four-round Ehrenfeucht–Fraïssé game between \(K_n\) and \(K_m\), with \(n,m\ge12\), maintain after at most three moves that corresponding chosen three-subsets have identical labeled Venn-cell cardinalities on the union of the selected subsets. For a subsequent chosen three-subset, its intersections with the existing nonempty Venn cells determine how many old ground elements must be reused. Match those counts on the other side. A new triple uses at most three elements outside the union of previously selected triples. After three moves, that union has at most nine ground elements, leaving at least three fresh elements on each side. Therefore every chosen triple admits a matching response. The induced two-way correspondence preserves equality of selected three-subsets and whether selected triples are disjoint, so it is a partial graph isomorphism after four moves. The standard four-round game characterization proves \(K_n\equiv_4K_m\) for every \(n,m\ge12\).

**Separating the finite initial orders.** For an ordered triple \(\bar A=(A_0,A_1,A_2)\) of graph vertices, let its *one-extension profile* \(\pi(\bar A)\) be the complete atomic diagram of \(\bar A\), together with the set of complete atomic diagrams realized by \((A_0,A_1,A_2,B)\) as \(B\) ranges over graph vertices. Atomic diagrams record all equality and edge relations between the selected graph vertices. Let \(P_n\) be the set of profiles realized in \(K_n\). Each individual profile is definable by a formula of quantifier rank one with three free variables: specify the atomic triple diagram, existentially demand a realization of each permitted four-point atomic diagram, and universally exclude all forbidden diagrams. Consequently, if \(P_n\ne P_m\), the two graphs are distinguishable by a sentence \(\exists A_0\exists A_1\exists A_2\,\psi\) of quantifier rank four.

We now give a finite *exhaustive integer certificate* for \(P_6,\ldots,P_{12}\). For three ordered three-subsets, let \(c_b\) be the number of ground elements with membership bitmask \(b\in\{0,\ldots,7\}\). Every feasible triple has eight nonnegative Venn counts satisfying
\[
\sum_{b:b\land 2^j\ne0}c_b=3\quad(j=0,1,2),\qquad \sum_{b=0}^7c_b=n.
\]
Conversely, every such eight-tuple corresponds to an ordered triple of graph vertices. For a fourth selected three-subset, enumerate nonnegative integers \(t_b\le c_b\) with \(\sum_b t_b=3\). The resulting four-vertex Venn counts are \(d_b=c_b-t_b\) and \(d_{b+8}=t_b\) for \(0\le b<8\). For any selected indices \(i<j\), their intersection has cardinality \(\sum_{b:b_i=b_j=1}d_b\). The corresponding graph vertices are equal precisely if this intersection cardinality is three, and adjacent precisely if it is zero. These formulas enumerate **all** atomic triple and four-tuple diagrams, with no sampling.

The attached verifier iterates every feasible triple Venn vector and every feasible fourth-triple split. It calculates the following complete profile-set sizes and ordered set-difference certificate, with columns in order \(m=6,7,8,9,10,11,12\):

| \(n\) | \(\lvert P_n\rvert\) | \(\lvert P_n\setminus P_m\rvert\) in column order |
| ---: | ---: | --- |
| 6 | 11 | 0, 6, 10, 10, 10, 10, 10 |
| 7 | 31 | 26, 0, 19, 25, 26, 26, 26 |
| 8 | 25 | 24, 13, 0, 12, 13, 13, 13 |
| 9 | 26 | 25, 20, 13, 0, 5, 8, 8 |
| 10 | 28 | 27, 23, 16, 7, 0, 3, 4 |
| 11 | 25 | 24, 20, 13, 7, 0, 0, 1 |
| 12 | 25 | 24, 20, 13, 7, 1, 1, 0 |

Every off-diagonal pair has a nonzero difference in at least one direction. Hence every two distinct parameters from \(6,\ldots,12\) have distinct rank-four theories. The uniform-tail argument shows that parameters larger than twelve add no new classes. Finally \(\binom n3\) grows strictly with \(n\ge3\), so \(220\) is the smallest representative size for the infinite final class.

## Verification
Run \(\texttt{python3 verify.py}\) using standard-library Python. The fully integer-based calculation prints the Venn-vector orbit totals, full difference matrix, and \(\texttt{VERIFY_OK}\). For three small orders \(n=6,7,8\), an independent explicit graph enumeration of **all ordered triples and all one-vertex extensions** agrees with the Venn-based spectrum. The script additionally checks \(P_{12}=P_{13}\), though the entire infinite tail is proved by the game argument rather than inferred from this finite equality. The exact integer loops and the correctness argument for their exhaustiveness are both essential; the log alone is not a proof.

## Relationship to prior work
Verbitsky's 2004 work studies first-order graph definability through Ehrenfeucht games, especially families with small separators, trees, and outerplanar graphs. Harvey and Wood's 2013 work explicitly defines Kneser graphs and determines their treewidth and related extremal set properties. Their inspected statements do not classify the rank-four equivalence classes of \(KG(n,3)\). Known first-order logical-depth results for complete multipartite graphs and paths concern distinct graph families; they do not imply the present exact seven-class result. This comparison does not prove absolute historical priority.

## Limitations
The finite certificate is exhaustive only for the listed initial parameters; the algebraic Venn-cell EF strategy supplies the proof for the infinite tail. The theorem is sensitive to the relational signature: naming ground-set elements, intersections, counting predicates, or richer relations changes what formulas can distinguish. No complete result for \(KG(n,k)\) with \(k\ne3\), or at other quantifier ranks, is claimed. Unindexed or inaccessible literature could contain an equivalent theorem; independent mathematical audit has not been performed.

## References
1. O. Verbitsky, *The First Order Definability of Graphs with Separators via the Ehrenfeucht Game*, arXiv:math/0401361v1, publicly posted 2004-01-26, https://arxiv.org/html/math/0401361v1 .
2. D. J. Harvey and D. R. Wood, *Treewidth of the Kneser Graph and the Erdős–Ko–Rado Theorem*, arXiv:1310.5400v1, publicly posted 2013-10-21, https://arxiv.org/html/1310.5400v1 .
