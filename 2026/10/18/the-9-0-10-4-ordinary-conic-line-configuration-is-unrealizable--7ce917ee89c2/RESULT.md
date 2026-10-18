# The \((9;0,10,4)\) ordinary conic–line configuration is unrealizable

## Finding
There is **no** reduced divisor in \(\mathbb P^2_{\mathbb C}\) formed by one smooth conic and nine distinct lines with precisely \(n_2=0\) ordinary nodes, \(n_3=10\) ordinary triple points and \(n_4=4\) ordinary quadruple points, and no other singularities. In the conventional notation for the component and singularity counts, the unrealizable configuration is \((9;0,10,4)\). The assertion concerns geometric realizability, and does not assume that the divisor is free.

## Assumptions and scope
Work over \(\mathbb C\). Every component is reduced and geometrically smooth; the conic is irreducible and the nine lines are pairwise distinct. "Ordinary" means that branches through each singularity have pairwise distinct tangent directions. Thus every intersection of the conic with each line is transverse and contributes one of the two intersections predicted by Bézout. No nonordinary singularities or points of multiplicity at least five are allowed. All counts refer to geometric points.

Write \(a\) for the number of ordinary quadruple points on the conic (each involving the conic and three lines), and \(b\) for the number of ordinary triple points on the conic (each involving the conic and two lines). Because there are no nodes, the conic's \(18\) line-intersection incidences give
\[
3a+2b=18,\qquad 0\leq a\leq4,
\]
so \((a,b)\in\{(0,9),(2,6),(4,3)\}\).

## Proof
**Case \(a=0\).** All four quadruple points are intersections of four lines. A single line cannot contain three such points: each quadruple point supplies three *distinct* other lines, hence three points would require nine other lines, while only eight exist. Also two different quadruple points are joined by at most one line of the arrangement. Consequently at most \(\binom42=6\) of the nine lines may contain two quadruple points, with all remaining lines containing at most one. The total number of line–quadruple incidences would be at most \(6\cdot2+3\cdot1=15\), rather than the required \(4\cdot4=16\). Contradiction.

**Case \(a=2\).** Two quadruple points consist entirely of lines, and two lie on the conic. There are four ordinary triple points off the conic and six on it. For each line \(L\), let \(q_C(L)\) count conic quadruple points on \(L\); let \(q_L(L)\) count all-line quadruple points on \(L\); and let \(t_L(L)\) count all-line ordinary triple points on \(L\). The line has exactly two intersections with the conic. Counting its other eight line incidences at distinct geometric intersection points yields
\[
q_C(L)+3q_L(L)+2t_L(L)=6. \tag{1}
\]
For \(q_L(L)=1\), equation (1), \(0\le q_C(L)\le2\), and integrality imply \((q_C(L),t_L(L))=(1,1)\). If the two all-line quadruple points have no common arrangement line, eight lines satisfy \(q_L=1\), forcing at least eight conic–quadruple incidences, whereas there are only \(2\cdot3=6\). Therefore they have exactly one common line (they cannot have two). The other six lines passing through one of these quadruple points each have \(q_L=1\), using all six conic–quadruple incidences. The two remaining lines have \(q_L=q_C=0\), so equation (1) forces \(t_L=3\) on *each* of them. Each of these two distinct lines would pass through three of the same four all-line triple points; their point sets overlap in at least two distinct triple points. Two distinct projective lines cannot meet twice. Contradiction.

**Case \(a=4\).** Every quadruple point lies on the conic. Upon deleting the conic, the nine-line arrangement has \(t_2=b=3\) nodes and \(t_3=(10-b)+a=11\) ordinary triple points, with no other multiplicities. Indeed the four former quadruple points become triple intersections of lines, and the three former conic triple points become ordinary double intersections of lines.

We prove that nine complex projective lines cannot have precisely three double and eleven triple points and no other intersections. Each line meets the other eight lines, so if it contains \(r\) triple points and \(s\) nodes, then \(2r+s=8\). In particular \(s\) is even. The three nodes contribute six line-node incidences. Since two distinct lines meet only once, at least three lines contain nodes; hence exactly three lines have \(s=2\), and the other six have \(s=0\). The three node-carrying lines form a triangle. Each of them has three triple points, and each of the other six lines has four.

No triple point can contain two triangle lines (their mutual intersections are nodes). Thus there are nine distinct triples containing one triangle line and two of the six other lines. Exactly two triple points remain; they involve only the six other lines. Each of these six lines contains one of the latter two points, and they accordingly split into two disjoint pencils of three lines, with distinct vertices \(U,V\). The remaining nine mixed triple points are precisely the intersections of a line from the first pencil with a line from the second pencil, each also lying on exactly one of the three triangle lines.

For completeness, two distinct pencils of three lines over \(\mathbb C\) and three transversal lines passing through their nine cross-intersections in a \((3,3)\)-net have concurrent transversal lines. To see this, choose projective coordinates making \(U=[1:0:0]\) and \(V=[0:1:0]\), with joining line \(Z=0\). That joining line cannot belong to either pencil, because it would pass through the other triple vertex and create a fourth line there. The two pencils therefore have equations \(Y=a_iZ\), \(X=b_jZ\), respectively, for pairwise distinct \(a_0,a_1,a_2\) and \(b_0,b_1,b_2\). Each transversal line meets the nine grid points \([b_j:a_i:1]\) along the graph \(b=f(a)\) of an invertible affine map carrying the three-element set \(A=\{a_0,a_1,a_2\}\) bijectively onto \(B=\{b_0,b_1,b_2\}\). Call these maps \(f_0,f_1,f_2\). Because the transversal lines partition the nine grid points, the map \(T=f_0^{-1}\circ f_1\) permutes \(A\) without a fixed element. It is therefore a 3-cycle. The remaining transversal map equals \(f_0\circ T^2\), since the two sides agree on three distinct elements of \(A\) and both are affine. Because \(T\) is a nonidentity affine map of order three over \(\mathbb C\), it has a fixed point \(a_*\) in \(\mathbb C\). Every one of the three graph lines \(b=f_i(a)\) passes through \((a_*,f_0(a_*))\). They are concurrent, contradicting that the three exceptional lines form a triangle with three nodes.

All possibilities for \(a\) are impossible, proving the theorem. \(\square\)

## Verification
The proof is symbolic and combinatorial, not based on unbounded computation. Its numerical checkpoints are \(3a+2b=18\), equation (1) on each line, and the incidence identity \(3t_3+6t_4=36\) for the nine-line subarrangement. They are exact over \(\mathbb C\). The order-three affine-map argument depends on characteristic zero and is not asserted in characteristic three.

## Relationship to prior work
Pokora's 2023 preprint on free arrangements of nine lines and one conic lists \((9;0,10,4)\) among the numerical possibilities obtained from freeness restrictions and notes that several degree-nine possibilities remained without known realizations over \(\mathbb R\) or \(\mathbb C\) (Section 3, case \(d=9\), and Remark 3.3). The present theorem removes this specific *geometric* possibility even without freeness, by a different incidence argument. Standard results about plane \(3\)-nets and the Fermat/Ceva configuration give context for the concurrent-transversal lemma; here the precise order-three lemma is proved directly, so no converse is inferred from only a paper title or a general net classification.

## Limitations
No conclusion is claimed for the other numerical candidates in Pokora's partial classification, for nonordinary singularities, or for positive characteristic. Independent verification of novelty, including older non-digitized incidence-geometry literature, remains desirable.

## References
1. P. Pokora, *Freeness of arrangements of lines and one conic with ordinary quasi-homogeneous singularities*, first public preprint 2023-12-20, arXiv:2312.13052; see Section 3, case \(d=9\), and Remark 3.3.
2. S. Yuzvinsky, *Realization of finite Abelian groups by nets in \(\mathbb P^2\)*, Compositio Mathematica 140 (2004), 1614–1624, DOI:10.1112/S0010437X04000600, for geometric net terminology and related pencils.
