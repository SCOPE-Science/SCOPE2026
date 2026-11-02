# Four rank-four theories of projective symplectic polar graphs

## Finding
For every prime power \(q\ge2\) and integer \(d\ge2\), let \(P(d,q)\) be the graph whose vertices are the one-dimensional subspaces of \(\mathbb F_q^{2d}\), with distinct vertices adjacent exactly when their nonzero representatives are orthogonal under a fixed nondegenerate alternating bilinear form. In first-order logic with equality and *only* the adjacency relation, the exact equivalence criterion is
\[
P(d,q)\equiv_4 P(e,r)
\quad\Longleftrightarrow\quad
\bigl((d=2)\Leftrightarrow(e=2)\bigr)
\ \land\
\bigl((q=2)\Leftrightarrow(r=2)\bigr).
\]
There are exactly four rank-four theories. Their least representatives in this family have \((d,q)=(2,2),(2,3),(3,2),(3,3)\), of orders respectively \(15,40,63,364\). Every graph in the family is rank-four equivalent to one with at most \(364\) vertices; \(364\) is sharp. All these graphs are rank-three equivalent, so four is the first quantifier rank that detects either distinction.

## Assumptions and scope
Let \(V\) have dimension \(2d\), and let \(B:V\times V\to\mathbb F_q\) be alternating and nondegenerate. The graph has no named coordinates, scalar operations, projective lines, form, or rank predicate. Form orthogonality is independent of representatives; \(E([u],[v])\) means \([u]\ne[v]\) and \(B(u,v)=0\). The result concerns finite prime-power fields and \(d\ge2\), not arbitrary polar spaces or extra named relations. The number of vertices is \((q^{2d}-1)/(q-1)\).

## Proof
**Extension lemma, up to three previously selected points.** A *three-point structural signature* records equalities, pairwise orthogonality, and, for three distinct points, whether they are projectively collinear (their representatives are dependent). Once \(q=2\) versus \(q\ge3\) and \(d=2\) versus \(d\ge3\) are fixed, (a) the possible signatures of a third point over each ordered pair and (b) the possible equality-and-adjacency patterns of a fourth point over each ordered triple depend only on this signature, not on \(q,d\).

To verify (a), take independent representatives \(u,v\). The map \(w\mapsto(B(w,u),B(w,v))\) is onto \(\mathbb F_q^2\). A distinct dependent third point exists on their projective line, with orthogonality to both if \(B(u,v)=0\), and to neither if \(B(u,v)\ne0\). Every choice of two orthogonality bits is possible for an independent third point, except both bits orthogonal when \(d=2\) and \(B(u,v)=0\): in that exceptional case the totally isotropic plane \(\langle u,v\rangle\) equals its own perpendicular. For \(d\ge3\), there is a further perpendicular direction. All other linear conditions have solutions outside \(\langle u,v\rangle\), even over \(\mathbb F_2\).

For (b), first suppose three distinct representatives \(u_1,u_2,u_3\) span a plane. Then the two independent linear forms on a new vector have freely chosen values \(a,b\), and the third value is \(\alpha a+\beta b\), where \(\alpha,\beta\ne0\). Their zero/nonzero patterns are: all zero; exactly one zero; and, *only when \(q\ge3\)*, none zero. Indeed, nonzero \(a,b\) with \(\alpha a+\beta b\ne0\) exist exactly when \(q>2\). Every nonzero pair of prescribed values has an affine solution fiber of size at least \(q^2>3\), so a projective point different from the three selected points exists. The all-zero pattern also has a new realization, except when \(q=2,d=2\) and the selected line is totally isotropic: there the two-dimensional common perpendicular is exactly the projective line of three selected points. If the selected line is nonisotropic, its perpendicular misses it, so the all-zero pattern is available.

If \(u_1,u_2,u_3\) are independent, the map
\[
\Phi(w)=(B(w,u_1),B(w,u_2),B(w,u_3))
\]
is onto \(\mathbb F_q^3\), with kernel dimension \(2d-3\). For \(d\ge3\), each zero/nonzero prescription admits a new point: a nonzero-value fiber has at least \(q^3>3\) vectors, each selected projective line meets it at most once, and the zero fiber has more than three projective points. For \(d=2,q\ge3\), each nonzero-value fiber is an affine line with \(q\) vectors. If all its points belonged to the three selected projective lines then \(q=3\), and those three points would be linearly dependent, contradicting independence of the representatives. The zero-value fiber is one projective point; it is forbidden exactly if one of the selected \(u_i\) is perpendicular to all three, a condition read off from the pairwise orthogonality bits.

Finally, for \(d=2,q=2\), every fiber of \(\Phi\) has two vectors. Write \(r_i=\Phi(u_i)\in\mathbb F_2^3\); these three rows are determined by the pairwise adjacency bits. The zero fiber has a new point exactly when no \(r_i=0\). A nonzero fiber has no new point exactly when its prescribed value equals two identical rows among the \(r_i\); then the two chosen representatives exhaust that fiber, since their sum generates the one-dimensional kernel. Hence here too every permitted fourth-point pattern is determined solely by the structural signature. Equality cases for fourth points are automatic.

Given the same two parameter dichotomies, Duplicator preserves equalities and orthogonality in the first two rounds, adds projective collinearity in the third round using (a), then matches every fourth adjacency/equality pattern using (b). This is a four-round Ehrenfeucht–Fraïssé strategy and proves the forward equivalences. The same first-two-round extension reasoning shows all graphs agree through rank three.

For the reverse direction, the following two rank-four properties detect the two dichotomies. Let \(E\) denote adjacency. First, there exist distinct mutually adjacent \(x,y,z\) and a fourth \(w\) with \(E(w,x)\land E(w,y)\land\neg E(w,z)\). This holds exactly when \(d\ge3\): the first three vectors must be independent and pairwise orthogonal, which is impossible in Witt rank two but possible in Witt rank at least three.

Second, there exist distinct pairwise nonadjacent \(x,y,z\) such that (i) every \(w\) orthogonal to both \(x,y\) is also orthogonal to \(z\), and (ii) some fourth \(w\) is nonadjacent to all three. Each of (i) and (ii) uses one extra quantifier after the three chosen points; their conjunction still has rank four. Condition (i) forces the three representatives to be dependent: for an independent triple the prescribed form values \((0,0,1)\) give a new witness; this is true even for \(q=2,d=2\) because none of the selected rows has these values. On a nonisotropic projective line, condition (ii) is realizable exactly when \(q\ge3\), by choosing two nonzero form values whose required nonzero linear combination is also nonzero. These two sentences distinguish all four classes.

The class of \(d\ge3,q\ge3\) has least representative \(P(3,3)\) of size \((3^6-1)/2=364\), proving sharpness of the representative bound.

## Verification
Run `python3 verify_polar.py` (standard library only). The script enumerates projective points, computes the alternating form over prime fields and \(\mathbb F_4\), and computes exact rank-four root types by recursively collecting full atomic extension profiles. It covers \((q,d)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2),(7,2)\); all \(28\) unordered cross-comparisons agree with the theorem. The expected final line is `VERIFY_OK`. Run `python3 separator_check.py` to check both explicit distinguishing properties directly on five models (expected `SEPARATOR_VERIFY_OK`). These finite comparisons do not prove the infinite cases; the preceding linear-algebraic extension lemma does.

## Relationship to prior work
Pikhurko and Verbitsky survey Ehrenfeucht–Fraïssé logical complexity of finite graphs (arXiv:1003.4865; first public date 2010-03-25), furnishing the logical framework but not a classification of this polar family. Abiad and Haemers study switching and adjacency-matrix two-ranks for binary symplectic graphs (arXiv:1412.2945; first public date 2014-12-09); their binary convention takes nonorthogonality as adjacency, so their graphs are complements of the graphs considered here. Brouwer, Ihringer, and Kantor study the combinatorial four-vertex condition and switched symplectic polar graphs (arXiv:2107.00076), which concerns local subgraph counts and does not state the across-parameter, graph-language first-order equivalence or its field/Witt-rank separating sentences. No assertion is made that absence from these works proves novelty across all literature.

## Limitations
The result is restricted to symplectic point-collinearity graphs, to prime-power fields, and to quantifier rank at most four. The proof is not a classification of general strongly regular graphs, polar spaces of other types, or the richer language naming lines or the form. Independent review and an exhaustive historical-priority search are not included. Computational data are checks of selected finite models, not certificates for infinite families.

## References
1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first public 2010-03-25. https://arxiv.org/abs/1003.4865
2. A. Abiad and W. H. Haemers, *Switched symplectic graphs and their 2-ranks*, arXiv:1412.2945, first public 2014-12-09. https://arxiv.org/abs/1412.2945
3. A. E. Brouwer, F. Ihringer and W. M. Kantor, *Strongly regular graphs satisfying the 4-vertex condition*, arXiv:2107.00076, first public 2021-06-30. https://arxiv.org/abs/2107.00076
4. A. E. Brouwer, *Symplectic graphs* (online reference). https://aeb.win.tue.nl/graphs/Sp.html
