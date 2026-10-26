# Seven rank-three theories of balanced finite Johnson graphs

## Finding
For integers \(n\ge 2k\ge2\), the Johnson graph \(J(n,k)\) has as vertices the \(k\)-element subsets of \([n]\), with distinct vertices adjacent when their intersection has size \(k-1\). In the pure graph language with equality and adjacency, let \(G\equiv_3H\) mean agreement on all first-order sentences of quantifier rank at most \(3\).

There are **exactly seven** \(\equiv_3\)-classes among these graphs, classified as follows:

| Class | Complete parameter condition | Representative |
| --- | --- | --- |
| 1 | \(k=1,\ n=2\) | \(J(2,1)\) |
| 2 | \(k=1,\ n\ge3\) | \(J(3,1)\) |
| 3 | \(k=2,\ n=4\) | \(J(4,2)\) |
| 4 | \(k=2,\ n=5\) | \(J(5,2)\) |
| 5 | \(k=2,\ n\ge6\) | \(J(6,2)\) |
| 6 | \(k=3,\ n=6\) | \(J(6,3)\) |
| 7 | \(k\ge3,\ n\ge2k,\ (n,k)\ne(6,3)\) | \(J(7,3)\) |

Thus for \(k\ge3\) all the graphs with \(n\ge2k\), apart from \(J(6,3)\), are indistinguishable by rank-three first-order sentences, even when both parameters vary without bound. Distinct rows are distinguishable at rank at most three. The balancing convention loses no nondegenerate cases because complementation of subsets gives \(J(n,k)\cong J(n,n-k)\).

## Assumptions and scope
Graphs are finite, simple, undirected, nonempty, and interpreted in the adjacency/equality signature. Quantifier rank counts the maximal number of nested quantifiers, without a bound on Boolean combination or total formula length. The classification includes complete graphs with \(k=1\), but excludes the one-vertex degenerate \(k=0\) or \(k=n\) cases. Adding such singleton graphs adds one further rank-three class.

## Proof
**1. A three-round game invariant.** For distinct vertices \(a,b\) in a graph \(G\), record \(e\in\{0,1\}\), their adjacency indicator, and a four-bit mask \(M_G(a,b)\): the bit for \((i,j)\in\{0,1\}^2\) is present if a *third vertex* \(c\notin\{a,b\}\) has adjacency indicators \(i\) to \(a\) and \(j\) to \(b\). Encode the bits for \((0,0),(0,1),(1,0),(1,1)\) by weights \(1,2,4,8\), respectively. Define \(\mathcal P(G)\) to be the set of resulting pairs \((e,M)\) over distinct ordered vertices.

For two nonempty **vertex-transitive** simple graphs, the Duplicator wins the three-round Ehrenfeucht--Fraïssé game if and only if their sets \(\mathcal P\) coincide. Indeed, after the first vertex is chosen, transitivity makes the possible second-vertex profiles independent of that choice. On round two, profiles can be matched in both directions. Equality of the masks permits every distinct third-vertex adjacency pattern to be answered; repetition of an earlier vertex is matched by repetition. Conversely, if some profile occurs only on one side, Spoiler chooses its first two vertices there, whichever side Duplicator uses for her first move; absence of the profile guarantees a winning final response to some third-vertex challenge. The standard game theorem identifies the three-round game with \(\equiv_3\).

**2. Pair geometry of Johnson graphs.** The symmetric group on the \(n\) ground elements acts transitively on vertices. For distinct \(k\)-sets \(A,B\), write \(d=k-|A\cap B|\). Then \(1\le d\le k\), and every such \(d\) occurs when \(n\ge2k\). The edge indicator is \(e=1\) precisely when \(d=1\). Write \(I=A\cap B\), \(X=A\setminus B\), \(Y=B\setminus A\), \(Z=[n]\setminus(A\cup B)\). These sets have sizes \(k-d,d,d,n-k-d\).

When \(k\ge3\), the masks for \(d=1\) and \(d=2\) are both \(15\). For \(d=1\), a common neighbor is obtained by replacing the unique element of \(X\) by an element of \(Z\), and an exclusive neighbor by replacing an element of \(I\) by one of \(Z\). A vertex adjacent to neither is obtained by replacing two elements of \(I\) with two elements of \(Z\). All these choices exist because \(|I|\ge2\) and \(|Z|\ge k-1\ge2\). Reversing \(A,B\) supplies the other exclusive-neighbor bit.

For \(d=2\), a common neighbor replaces one element of \(X\) by one of \(Y\), and an exclusive neighbor replaces one element of \(I\) by one of \(Z\). For the neither-neighbor bit, if \(k=3\), use one element each of \(X,Y,Z\); if \(k\ge4\), remove two elements from \(I\) and insert two elements of \(Z\). These sets have exactly \(k\) elements and meet neither \(A\) nor \(B\) in \(k-1\) elements. Thus all four bits occur.

For \(d\ge3\), no vertex is adjacent to both \(A\) and \(B\), since Johnson distance satisfies the triangle inequality. Both exclusive-neighbor bits occur by replacing an element of \(X\) with one from \(Y\), and symmetrically. A vertex nonadjacent to both exists when \(k\ge4\): for \(d\ge4\), replace two elements of \(X\) by two of \(Y\); for \(d=3\), replace two elements of \(X\) and one of \(I\) by two elements of \(Y\) and one of \(Z\). In the latter construction \(I\) and \(Z\) are nonempty because \(n\ge2k\) and \(k\ge4\). For \(k=3,d=3\), the nonadjacent-to-both bit occurs exactly when \(n\ge7\): with an element of \(Z\), choose one element from each of \(X,Y,Z\); at \(n=6\), every other three-set contains at least two members of one of the disjoint sets \(A,B\).

Hence, for \(k\ge3\), all edge profiles are \((1,15)\); distance-two nonedge profiles are \((0,15)\); distance-at-least-three nonedge profiles are \((0,7)\), except that \(J(6,3)\) has \((0,6)\) instead. All three distance categories occur, establishing rows 6--7.

**3. The small subset sizes.** For \(k=1\), \(J(n,1)=K_n\), with one edge profile \((1,0)\) for \(n=2\) and \((1,8)\) for \(n\ge3\). For \(k=2\), an adjacent pair of two-sets has a third common neighbor and third exclusive neighbors for \(n\ge4\), but has a third nonneighbor of both only when \(n\ge5\). A nonadjacent pair is disjoint, always has a common neighbor, has exclusive neighbors only when \(n\ge5\), and has a common nonneighbor only when \(n\ge6\). These constructions are immediate by choosing crossing two-sets or elements outside the union of the two selected sets.

Collecting the masks gives the complete table:

| Parameter row | Edge masks | Nonedge masks |
| --- | --- | --- |
| 1 | \(\{0\}\) | \(\varnothing\) |
| 2 | \(\{8\}\) | \(\varnothing\) |
| 3 | \(\{14\}\) | \(\{8\}\) |
| 4 | \(\{15\}\) | \(\{14\}\) |
| 5 | \(\{15\}\) | \(\{15\}\) |
| 6 | \(\{15\}\) | \(\{6,15\}\) |
| 7 | \(\{15\}\) | \(\{7,15\}\) |

The seven profiles are pairwise distinct, so the game invariant proves both the stated equivalences and the sharp number of classes. \(\square\)

## Verification
`verify_johnson.py` directly enumerates \(k\)-subsets, one representative of each intersection-size orbit of a vertex pair, and every possible third vertex. It compares the resulting masks against the table for \(34\) parameter pairs with \(1\le k\le8\), and checks that precisely seven signatures occur. Its output is included as `verification_output.txt`. The finite computation corroborates the formulas; the unrestricted quantifiers follow from the symbolic proof above, not extrapolation from the sample.

## Relationship to prior work
Ehrenfeucht--Fraïssé techniques and graph quantifier-rank distinguishability are classical; Verbitsky's 2004 preprint treats separator classes and general logical depth rather than the Johnson-family three-round partition. Silberstein and Etzion (2010) study codes in Johnson graphs and provide the standard subset-graph definition and complement symmetry, but their results concern existence constraints for perfect codes, not first-order rank-three theories. Gavrilyuk and Goryainov (first online 2012) study equitable colorings of \(J(v,3)\). Chalopin and coauthors (2022) analyze definability with metric betweenness and partial Johnson graphs, not the rank-three theories of the Johnson graphs themselves. An earlier classification of triangular graphs \(J(n,2)\) supplies the low-width special case only; it does not imply the all-width collapse or the exceptional \(J(6,3)\) behavior.

## Limitations
The result concerns precisely quantifier rank three in the ordinary adjacency/equality language. It does not classify higher ranks, counting logic, graph formulas with metric betweenness, or more general Johnson-scheme relation graphs. The literature comparison does not rule out equivalent uncatalogued results or folklore. The numerical program tests only finite instances; the symbolic argument is required for the infinite family.

## References
1. O. Verbitsky, *The First Order Definability of Graphs with Separators via the Ehrenfeucht Game*, arXiv:math/0401361v1 (public 2004-01-26), https://arxiv.org/abs/math/0401361.
2. N. Silberstein and T. Etzion, *On Perfect Codes in the Johnson Graph*, arXiv:1004.5195v1 (public 2010-04-29), https://arxiv.org/abs/1004.5195.
3. A. L. Gavrilyuk and S. V. Goryainov, *On Perfect 2-Colorings of Johnson Graphs \(J(v,3)\)*, Journal of Combinatorial Designs 21 (2013), 232--252, first online 2012-07-30, doi:10.1002/jcd.21327.
4. J. Chalopin, M. Changat, V. Chepoi and J. Jacob, *First-Order Logic Axiomatization of Metric Graph Theory*, arXiv:2203.01070v1 (public 2022-03-02), https://arxiv.org/abs/2203.01070.
5. M. Bodirsky and B. Bodor, *Structures preserved by primitive actions of the infinite symmetric group*, arXiv:2501.03789v4 (2025), https://arxiv.org/abs/2501.03789.
