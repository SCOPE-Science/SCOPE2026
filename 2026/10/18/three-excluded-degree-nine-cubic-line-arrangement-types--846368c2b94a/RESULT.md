# Three excluded degree-nine cubic-line arrangement types

## Finding
Let \(\mathcal A\) be a reduced plane-curve arrangement over \(\mathbb C\) whose components are smooth cubic curves and distinct lines, of total degree nine. Suppose its only singularities are nodes \(A_1\), ordinary triple points \(D_4\), and two-branch contacts \(A_5\). Write \((k,d;n_2,n_3,t_5)\) for the numbers of smooth cubic components, line components, nodes, ordinary triple points, and \(A_5\) contacts. None of the following three weak combinatorics is geometrically realizable:
\[
(1,6;0,7,4),\qquad(1,6;3,5,5),\qquad(2,3;0,2,8).
\]
Consequently, using the degree-nine freeness restrictions in Talar's work, any **free** degree-nine arrangement of this specified kind necessarily has
\[
(k,d;n_2,n_3,t_5)=(2,3;3,0,9).
\]
No assertion is made that this remaining numerical type can be realized or is free.

## Assumptions and scope
All components are reduced and distinct in \(\mathbf P^2_{\mathbb C}\); each cubic component is geometrically smooth. An \(A_5\) point has exactly two smooth local branches with intersection multiplicity three; a \(D_4\) point has exactly three transverse smooth local branches. The conclusion excludes precisely three configurations, without assuming freeness for their nonrealizability.

## Proof
**One cubic and six lines.** A flex-tangent line meeting the smooth cubic with local multiplicity three uses its entire degree-three intersection number by Bézout. Every \(A_5\) point is one such cubic–line contact, as two distinct lines meet transversely and the cubic itself is smooth. Thus the \(t_5\) flex-tangent lines do not pass through any additional point of the cubic. In an ordinary triple point involving the cubic and two lines, both of those lines must come from the \(6-t_5\) nonflex lines. Let \(a\) be the number of ordinary triple points supported on three lines, \(b\) those supported on the cubic and two lines, and \(c\) the number of ordinary nodes supported on two lines. Counting the 15 unordered pairs of lines gives
\[
a+b=n_3,\quad 3a+b+c=15,\quad 0\le c\le n_2,\quad b\le\binom{6-t_5}{2}.
\]
For \((n_2,n_3,t_5)=(0,7,4)\), these equations force \((a,b,c)=(4,3,0)\), contradicting \(b\le\binom22=1\).

For \((n_2,n_3,t_5)=(3,5,5)\), the bound gives \(b=0\), so \(a=5\) and \(c=0\). Thus each of the six lines meets all five other lines exclusively in ordinary three-line concurrence points. Along a fixed line, each such concurrence accounts for **two** other lines. Five cannot be partitioned into pairs. This is impossible.

**Two cubics and three lines.** For \((n_2,n_3,t_5)=(0,2,8)\), no pair of lines can meet in an ordinary node, and two distinct lines cannot make an \(A_5\) contact. Consequently each pairwise intersection of the three lines must be an ordinary triple point. Since there are only two triple points in total, all three lines must concur at one point \(Q\), which is a triple-of-lines point not lying on either cubic (otherwise four branches would meet). The other triple point \(R\) cannot involve two lines, because all pairs of lines intersect only at \(Q\). It must therefore comprise both smooth cubics and one line, with the cubics transverse at \(R\). At every other point where the two cubics intersect, the allowed local singularity must be an \(A_5\) contact; hence all remaining local cubic–cubic intersection multiplicities are three. Bézout would require
\[
9=C_1\cdot C_2=1+3s
\]
for some nonnegative integer \(s\), a contradiction modulo three.

**Freeness consequence.** Talar's degree-nine necessary numerical analysis lists \((1,6;0,7,4)\), \((1,6;3,5,5)\), \((1,6;6,3,6)\), \((1,6;9,1,7)\), \((2,3;3,0,9)\), and \((2,3;0,2,8)\). His Hirzebruch inequality excludes the third and fourth of these. The three nonrealizability arguments above eliminate the first, second, and sixth, leaving only \((2,3;3,0,9)\) as a necessary type for freeness. This uses Talar's published necessary restrictions, not a claim of their sufficiency.

## Verification
The included standalone Python script `check_constraints.py` verifies the integer constraints in the one-cubic cases and the impossibility of \(9=1+3s\). The geometric premises—Bézout, two branches of \(A_5\), and three transverse branches of \(D_4\)—are proved and applied explicitly above and are not inferred from finite enumeration.

## Relationship to prior work
Przemysław Talar, *On cubic-line arrangements with simple singularities*, arXiv:2305.01530 (first posted 2023-05-02), Sections 1 and 3; published in *Boletín de la Sociedad Matemática Mexicana* 30 (2024), article 93, DOI 10.1007/s40590-024-00662-z. Section 3 identifies all three displayed configurations as cases whose geometric realizability was unresolved, and derives the necessary freeness restrictions used here. The proof here supplies additional incidence and Bézout obstructions, and makes no claim about the remaining type.

## Limitations
The remaining type \((2,3;3,0,9)\) is not classified. Nothing here concerns arrangements with other singularity types, singular cubics, or higher degrees. Originality depends on the accessible targeted prior-work search and may be limited by unindexed equivalent results. No independent audit has been performed.

## References
1. P. Talar, *On cubic-line arrangements with simple singularities*, arXiv:2305.01530 (2023), https://arxiv.org/abs/2305.01530 ; DOI 10.1007/s40590-024-00662-z (2024), https://link.springer.com/article/10.1007/s40590-024-00662-z.
2. Bézout's theorem for plane projective curves; standard local branch characterization of plane \(A_5\) and \(D_4\) singularities.
