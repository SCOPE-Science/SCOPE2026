# A three-phase exact packing law for one large and eight unit squares

## Finding
Let \(t\ge 2\) be real. Consider one closed axis-parallel square of side \(t\) and eight closed axis-parallel squares of side \(1\), all packed into an axis-parallel square container with disjoint interiors. Write \(L(t)\) for the least possible container side. Then
\[
L(t)=\begin{cases}
t+2,&2\le t\le 3,\\
5,&3\le t\le 4,\\
t+1,&t\ge4.
\end{cases}
\]
Consequently this nine-item packing problem has two sharp transitions: a growing first phase, a constant phase, and a growing contact phase. The plateau is not merely a local statement about a particular packing pattern; all packings satisfy the lower bound.

## Assumptions and scope
All nine items and the container are Euclidean squares whose edges are parallel to the coordinate axes. Translation is allowed; rotation is **not** allowed. Distinct items may share boundary points or edges, but their interiors are disjoint. The larger square has side \(t\ge2\) and the other eight each have side exactly \(1\). The statement does not cover \(0<t<2\), independently rotated squares, rectangular containers, or nine arbitrary side lengths. Scale invariance lets the smaller side be normalized to \(1\).

## Proof
**A two-strip obstruction.** We first prove: if \(t\ge2\) and \(L<\min\{5,t+2\}\), it is impossible to pack a square of side \(t\) together with eight unit squares in \([0,L]^2\).

Suppose such a packing existed, with the large square
\[
B=[a,a+t]\times[b,b+t]\subseteq[0,L]^2.
\]
Every unit square is disjoint in its interior from \(B\), so at least one of its coordinate projections is disjoint in its interior from the corresponding projection of \(B\). The total unused horizontal width of the container outside \([a,a+t]\) is \(L-t<2\). Thus at most one of the **left** and **right** complementary vertical strips can contain a full unit square (each would require width at least \(1\)). The analogous statement holds for the top and bottom complementary horizontal strips. After reflecting the picture separately about the container's horizontal and vertical midlines, we may assume every unit square belongs to the right-hand strip
\[
V=[a+t,L]\times[0,L]
\]
or the top strip
\[
H=[0,L]\times[b+t,L].
\]
If only one type of strip is usable, all unit squares lie in a single strip of width less than \(2\), hence have pairwise disjoint projections along its long axis and there can be fewer than \(5\). Thus both types are usable. Assign each unit square to either \(V\) or \(H\) containing it; squares in their overlap can be assigned arbitrarily. Write \(k\) and \(\ell\) for the two assignment counts.

Any two unit squares assigned to \(V\) have horizontal intervals of length \(1\) inside a common interval of length \(L-a-t\le L-t<2\). These horizontal intervals overlap in a set of positive length. Consequently, disjoint interiors require their vertical projections to be pairwise interior-disjoint, so \(k\le\lfloor L\rfloor\le4\), because \(L<5\). By interchanging the coordinate axes, \(\ell\le4\). Since \(k+\ell=8\), necessarily \(k=\ell=4\).

Among the four \(V\)-squares, select the one \(Q_V\) with highest lower \(y\)-coordinate; its lower \(y\)-coordinate is at least \(3\), hence its upper \(y\)-coordinate is at least \(4\). Among the four \(H\)-squares, select the one \(Q_H\) with rightmost lower \(x\)-coordinate; its lower \(x\)-coordinate is at least \(3\), hence its upper \(x\)-coordinate is at least \(4\). The inequalities follow because four pairwise interior-disjoint unit intervals require total length at least \(4\).

We show \(Q_V\) and \(Q_H\) overlap in the interior in **both** coordinates. Write \(x_V,x_H,y_V,y_H\) for their respective lower coordinates. Since \(Q_V\subseteq V\) and \(Q_H\subseteq H\),
\[
x_V+1\ge a+t+1\ge t+1>L-1\ge x_H,
\]
\[
y_H+1\ge b+t+1\ge t+1>L-1\ge y_V.
\]
The two remaining strict overlaps follow from
\[
x_H+1\ge4>L-1\ge x_V,
\qquad y_V+1\ge4>L-1\ge y_H.
\]
Thus both open coordinate intervals meet, and the interiors of \(Q_V\) and \(Q_H\) intersect. This contradiction proves the obstruction. Notice that \(L<t+1\) is independently impossible because no unit square can be disjoint from the large square; the same strip argument applies vacuously in that case.

**Lower bounds.** If \(2\le t\le3\), the obstruction rules out every \(L<t+2\), since then also \(L<5\). Thus \(L(t)\ge t+2\). If \(3\le t\le4\), every \(L<5\) also satisfies \(L<t+2\); hence \(L(t)\ge5\). For all \(t\ge4\), just one unit square disjoint from the large square forces a separation of their projections along one axis, and hence \(L(t)\ge t+1\).

**Explicit upper-bound packings.** For \(2\le t\le3\), place \(B=[0,t]^2\) and put eight unit squares into two columns with lower-left corners \((t+i,j)\), where \(i=0,1\) and \(j=0,1,2,3\). They fit in \([0,t+2]^2\), since \(t+2\ge4\).

For \(3\le t\le4\), put \(B=[0,t]^2\), five unit squares with lower-left corners \((i,4)\), \(i=0,1,2,3,4\), and three with lower-left corners \((4,j)\), \(j=0,1,2\). This packs everything into \([0,5]^2\). All unit squares lie outside the interior of \(B\) because \(t\le4\), and the top and right collections are disjoint.

For \(t\ge4\), put \(B=[0,t]^2\), five unit squares with lower-left corners \((i,t)\), \(i=0,1,2,3,4\), and three with lower-left corners \((t,j)\), \(j=0,1,2\). The nine squares fit in \([0,t+1]^2\), since \(t+1\ge5\) and \(t\ge4\). These upper bounds match the lower bounds throughout the claimed ranges. \(\square\)

## Verification
The proof is exact, requires no numerical experiments, and contains no unproved enumeration. A critical potential failure is that a unit square might straddle two strips; this is handled by assigning overlap squares arbitrarily, and the contradiction applies to every possible partition. Another is the possibility of squares lying on both sides of the large square: the strict inequality \(L-t<2\) rules out two opposite strips of width at least one. The final overlap is strict in both axes because \(L<5\) and \(L<t+2\); endpoint cases are supplied by the upper-bound configurations. The coordinate constructions can be checked by direct interval arithmetic.

## Relationship to prior work
Badger's October 15, 2026 preprint establishes exact axis-parallel square-packing formulas for up to seven prescribed squares and an exact finite-strategy framework for general cardinalities. It does not determine the nine-square parameter ray \((t,1,1,1,1,1,1,1,1)\). A subsequent October 20, 2026 preprint by the same author gives the full eight-square formula and explicitly identifies the general nine-square problem as substantially more complicated; its eight-item formula does not cover a nine-item instance. Classical finite sequence-pair representations encode all feasible orthogonal packings but do not provide this optimized three-phase formula. The present result is deliberately a natural one-parameter exact subproblem, not a general solution for nine side lengths.

## Limitations
Only axis-parallel placements and \(t\ge2\) are treated. Nothing is claimed about rotations or the range \(0<t<2\). The result is reviewed by the same research model and has not received an independent mathematical audit. The bounded literature search did not identify the precise phase diagram, but unindexed or historical prior coverage remains possible.

## References
1. Matthew Badger, *Axis-parallel square packing with an exact formula for optimal packing of seven squares*, arXiv:2610.22622v1, first submitted 15 October 2026, https://arxiv.org/html/2610.22622v1 .
2. Matthew Badger, *An exact formula for optimal axis-parallel packing of eight squares*, arXiv:2610.28504v1, first submitted 20 October 2026, https://arxiv.org/html/2610.28504v1 . (Follow-up used for literature comparison, not as the dated source of the finding.)
3. Hiroshi Murata, Kunihiro Fujiyoshi, Shigetoshi Nakatake, and Yoji Kajitani, *VLSI module placement based on rectangle-packing by the sequence-pair*, IEEE TCAD **15** (1996), 1518–1524.
4. Jannik Silvanus and Jens Vygen, *Few sequence pairs suffice: Representing all rectangle placements*, SIAM Journal on Discrete Mathematics **34** (2020), 2017–2032.
