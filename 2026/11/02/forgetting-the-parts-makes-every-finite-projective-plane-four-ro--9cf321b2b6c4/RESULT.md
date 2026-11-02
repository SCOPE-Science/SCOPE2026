# Forgetting the parts makes every finite projective plane four-round equivalent

## Finding
Let \(\Pi\) be any finite projective plane of order \(q\ge2\), with point set \(\mathcal P\), line set \(\mathcal L\), and incidence relation \(I\). Its **uncoloured Levi graph** \(G(\Pi)\) has vertices \(\mathcal P\sqcup\mathcal L\) and edges \(p\ell\) precisely when \(I(p,\ell)\). Neither part is named in the first-order graph language \(\{E,=\}\).

For any two such planes \(\Pi,\Pi'\), including non-Desarguesian planes and planes of different orders,
\[
G(\Pi)\equiv_4 G(\Pi').
\]
Thus the entire family has **exactly one quantifier-rank-four theory**, represented by the \(14\)-vertex Heawood graph \(G(\mathrm{PG}(2,2))\). This is the smallest possible representative within the family.

The bound is sharp as a logical depth for the smallest order: if \(\Pi\) has order \(q\ge3\), then
\[
\operatorname{D}\!\bigl(G(\mathrm{PG}(2,2)),G(\Pi)\bigr)=5,
\]
where \(\operatorname D\) is the minimum quantifier rank of a distinguishing first-order sentence in \(\{E,=\}\). The rank-five witness says that a vertex has at least four distinct neighbours. No claim is made here about the complete rank-five classification of all projective planes.

## Assumptions and scope
A finite projective plane of order \(q\) has exactly \(N=q^2+q+1\) points and the same number of lines, exactly \(q+1\) lines through each point and \(q+1\) points on each line. Two distinct points lie on exactly one common line, and two distinct lines meet at exactly one common point. We assume \(q\ge2\), and make no coordinatizability or Desarguesian hypothesis. The graph has \(2N\) vertices and is bipartite, without a distinguished bipartition in the logical signature. Quantifier rank, rather than number of variables or counting-quantifier rank, is the resource measured.

## Proof
**1. Uniform incidence supplies the required choices.** Let \(a,b\) be two distinct elements of the same part of the Levi graph. Among elements of the opposite part, the numbers adjacent to both, just \(a\), just \(b\), and neither are, respectively,
\[
1,\qquad q,\qquad q,\qquad q(q-1).
\]
All four are positive for \(q\ge2\). If \(a\) and \(\ell\) lie in opposite parts, there are fresh vertices of either part both incident and nonincident with the element of the opposite part: each line/point has \(q+1\ge3\) neighbours and \(q^2\ge4\) nonneighbours within the other part. Excluding up to one already selected vertex leaves a choice. The same counts work after interchange of points and lines.

**2. A maintained geometric type for three selected vertices.** In the four-round Ehrenfeucht–Fraïssé game, Duplicator may preserve the following information for each ordered list of at most three selections: repetitions and their equalities; which selected vertices are on the same side of the bipartition (after an arbitrary initial choice of which part corresponds to which); all point–line incidences among selected vertices; and, only when three *distinct* selected vertices lie in the same part, whether they have one common opposite-part neighbour (collinearity or concurrence). This extra last predicate is *not* part of the graph signature; it is a bookkeeping invariant for the strategy.

Starting with zero selections, every first vertex can be matched on a chosen corresponding side. For a second distinct selection, the other structure has a vertex in either prescribed part, with either incidence choice when the parts differ, by the incidence counts. For a third distinct selection, if the first two are in the same part, the choice of a third vertex in that part can be made collinear/concurrent with them because their unique common neighbour has \(q+1\ge3\) neighbours; a noncollinear/nonconcurrent choice exists since \(N-(q+1)=q^2>0\). A third vertex in the opposite part can realize each of the four possible incidence patterns to the first two by the displayed counts. If the first two lie in opposite parts, a third vertex in either part can be chosen incident or nonincident to the selected vertex of the opposite part, again with a fresh choice. Repeated selections are answered by repetition. These choices preserve the full stated three-vertex type in either direction.

**3. Every required fourth-vertex atomic pattern survives.** Suppose three distinct selected vertices all lie in the same part. A fresh fourth vertex in that part has adjacency pattern \(000\) to them, which exists because \(N\ge7\). A fourth vertex in the opposite part can have a prescribed nonempty incidence subset as follows:

- If the triple has a common neighbour, pattern \(111\) occurs, no pattern with exactly two \(1\)'s occurs, and each singleton pattern occurs, since each selected vertex lies on \(q\ge2\) further opposite-part elements through it.
- If the triple has no common neighbour, pattern \(111\) does not occur, all three doubleton patterns occur through the unique joins of each pair, and every singleton pattern occurs because each selected vertex has \(q+1\ge3\) neighbours, exactly two of which join it to another selected vertex.

Thus the *uncoloured graph adjacency* patterns for the fourth move are controlled by the maintained triple type. In particular, a missing opposite-part \(000\) configuration is harmless because a fresh same-part vertex supplies \(000\).

Now suppose two distinct selected vertices \(a,b\) occupy one part and the third, \(\ell\), occupies the other. A new vertex on the side of \(a,b\) is adjacent to neither \(a\) nor \(b\), and can be chosen either adjacent or nonadjacent to \(\ell\). The former is available because \(\ell\) has at least three neighbours, of which at most two are selected; the latter because \(\ell\) has at least \(q^2\) nonneighbours on that side. A new vertex on the side of \(\ell\) has no edge to \(\ell\). Its patterns on \(a,b\) are \(00,10,01\) and, if \(\ell\) is not their unique common neighbour, \(11\). There are \(q(q-1)\ge2\) possible vertices for \(00\), and \(q\ge2\) for each singleton pattern, so excluding the already selected \(\ell\) leaves all three patterns available. The \(11\) vertex is their unique common neighbour; it is fresh exactly when it is not \(\ell\), a condition already determined by the existing incidence diagram. Interchanging the parts covers the other mixed case. If a previous selection is repeated, Duplicator repeats its match; with fewer than three distinct selections the incidence counts in Step 1 give every fresh atomic pattern.

The fourth response therefore preserves equality and adjacency of all four selected vertices. Duplicator wins the four-round game between any two planes, which proves \(G(\Pi)\equiv_4G(\Pi')\).

**4. Exact separation at the next rank.** The first-order sentence
\[
\exists x\,\exists y_1\,\exists y_2\,\exists y_3\,\exists y_4\,
\left(\bigwedge_{1\le i<j\le4}y_i\ne y_j\ \wedge\
\bigwedge_{i=1}^4 E(x,y_i)\right)
\]
has quantifier rank five. It is false in the Heawood graph, where every degree is three, and true in every plane of order at least three, where every degree is \(q+1\ge4\). The preceding four-round equivalence proves this distinguishing rank is minimal. Finally, since \(2(q^2+q+1)\ge14\), equality at \(q=2\), the within-family smallest representative has exactly fourteen vertices.

## Verification
Two independently structured finite computations accompany the proof. `verify_local.py` enumerates all ordered triples (including repetitions) for projective planes over \(\mathbb F_2\) and \(\mathbb F_3\), checks uniformity of the geometric three-vertex extension signatures, and compares all one-, two-, and three-selection profiles; all \(48\) oriented geometric triple types agree. `verify_ef.cpp` computes exact, unrestricted-vertex four-round first-order types directly from atomic equality/adjacency-extension sets, for \(\mathrm{PG}(2,2)\), \(\mathrm{PG}(2,3)\), and \(\mathrm{PG}(2,5)\). All three root types agree. Run `reproduce.sh` in a directory containing the supplied code; the two recorded outputs are included as `local_output.txt` and `ef_output.txt`. These computations corroborate but do not replace the general incidence-axiom proof.

## Relationship to prior work
Pikhurko, Veith and Verbitsky (2003) develop quantitative graph definability and the Ehrenfeucht–Fraïssé characterization of distinguishing quantifier rank; their work supplies general methods, not this uniform projective-plane comparison. Venema (1998/1999) studies a **two-sorted modal logic** of projective planes, a different language and logical fragment: modal equivalence or validity does not imply this four-round claim in pure graph first-order logic. Its abstract was accessible, but the full text was not obtained; that source remains a priority-check limitation.

A closely related *point/line-sorted first-order* classification distinguishes the Fano plane from planes of order three already at rank four, using a covering-of-points formula. That result does **not** imply equivalence in the weaker uncoloured signature. Here the inability to name the two sides is essential: a graph-quantified fourth vertex can be taken from either side, and a same-side vertex supplies the otherwise missing zero-adjacency extension. Results on affine and biaffine incidence geometries concern different families and do not imply this projective-plane theorem. De Winter, Lazebnik and Verstraëte (2008) characterize projective planes by extremal short-cycle counts, not a stated rank-four logical equivalence; only their abstract was inspected. No claim of exhaustive historical priority is made.

## Limitations
The theorem concerns **finite projective planes of order at least two** and pure first-order graph logic with equality and undirected adjacency, *without* unary point/line predicates or counting. It does not claim the full classification at rank five, extend to arbitrary partial planes, characterize all graphs equivalent to the Heawood graph, or establish an independent audit. The historical-priority comparison remains bounded by accessible literature, particularly the unavailable full text of the directly relevant modal-logic paper.

## References
1. O. Pikhurko, H. Veith, O. Verbitsky, *The First Order Definability of Graphs: Upper Bounds for Quantifier Rank* (initial public arXiv submission 2003-11-04), https://arxiv.org/abs/math/0311041 .
2. Y. Venema, *Points, Lines and Diamonds: A Two-Sorted Modal Logic for Projective Planes*, ILLC report ML-1998-04; *Journal of Logic and Computation* 9 (1999), 601–621, https://doi.org/10.1093/logcom/9.5.601 .
3. S. De Winter, F. Lazebnik, J. Verstraëte, *An Extremal Characterization of Projective Planes*, *Electronic Journal of Combinatorics* 15 (2008), R143, https://doi.org/10.37236/867 .
