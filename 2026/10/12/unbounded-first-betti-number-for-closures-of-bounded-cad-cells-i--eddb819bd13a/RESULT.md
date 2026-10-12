# Unbounded first Betti number for closures of bounded CAD cells in \(\mathbf R^4\)
## Finding
For every integer \(m\ge1\), there is a bounded cylindrical algebraic decomposition (CAD) cell
\[
C_m\subset\mathbf R^4
\]
whose closure strongly deformation retracts onto a finite graph homotopy equivalent to
\[
\bigvee^m S^1.
\]
In particular,
\[
\pi_1(\overline{C_m})\cong F_m,
\qquad
H_1(\overline{C_m};\mathbf Z)\cong\mathbf Z^m,
\]
and
\[
\widetilde H_i(\overline{C_m};\mathbf Z)=0
\quad\text{for every }i\ne1.
\]
Thus the first Betti number of the closure of a bounded CAD cell is unbounded even with ambient dimension fixed equal to \(4\).

## Assumptions and scope
Let
\[
\mathbb D_s=\{(x,y)\in\mathbf R^2:x^2+y^2<1\}\setminus\bigl((-1,0]\times\{0\}\bigr)
\]
be the slit disk used by Michel. His cornet cell \(\mathfrak C\subset\mathbf R^3\) is a bounded CAD cell, and Proposition 3.3 of the source gives a semialgebraic homeomorphism of pairs
\[
(\overline{\mathfrak C},\mathfrak C)\cong(\overline{\mathbb D_s},\mathbb D_s).
\]
Proposition 3.5 transfers sections over \(\mathbb D_s\) to CAD-cell sections over \(\mathfrak C\), preserving the homeomorphism type of the pair consisting of the section and its closure.

Fix \(m\ge1\). Put
\[
t_j=-1+\frac jm\qquad(0\le j\le m)
\]
and
\[
h_m(x)=\prod_{j=0}^{m}(x-t_j).
\]
Define the continuous semialgebraic function \(f_m:\mathbb D_s\to\mathbf R\) by
\[
f_m(x,y)=
\begin{cases}
 h_m(x),&-1<x<0\text{ and }y>0,\\
-h_m(x),&-1<x<0\text{ and }y<0,\\
0,&x\ge0.
\end{cases}
\]
There is no ambiguity on the removed slit. Continuity at \(x=0\) holds because \(h_m(0)=0\).

## Proof
Let
\[
G_m=\{(x,y,f_m(x,y)):(x,y)\in\mathbb D_s\}\subset\mathbf R^3.
\]
Inside \(\overline{G_m}\), define
\[
A_m=
\{(x,0,h_m(x)):-1\le x\le0\}
\cup
\{(x,0,-h_m(x)):-1\le x\le0\}.
\]
The two arcs meet exactly at the \(m+1\) points with first coordinate \(t_0,\ldots,t_m\), because these are precisely the zeros of \(h_m\) on \([-1,0]\).

Consider
\[
F((x,y,z),s)=
\left(
\frac{(1-s)(x+|x|)+(x-|x|)}2,
(1-s)y,
z
\right),
\qquad 0\le s\le1.
\]
This is the deformation used in Michel's one-loop example, and it works unchanged for \(f_m\). If \(x<0\), the first coordinate is fixed and, for \(s<1\), the sign of the second coordinate is unchanged; hence the third coordinate remains the correct value \(\pm h_m(x)\). At \(s=1\) the point lands on the corresponding branch of \(A_m\). If \(x\ge0\), every point of \(\overline{G_m}\) above that half-disk has third coordinate \(0\), and the first two coordinates are radially scaled toward the origin while remaining in the closed disk. Points of \(A_m\) are fixed throughout. Therefore \(F\) is a strong deformation retraction
\[
\overline{G_m}\searrow A_m.
\]

The finite graph \(A_m\) has \(m+1\) vertices and \(2m\) edges: on each interval \([t_{j-1},t_j]\), the two graphs \(z=\pm h_m(x)\) are distinct except at their endpoints and form one cycle. Hence its cycle rank is
\[
2m-(m+1)+1=m.
\]
A connected graph of cycle rank \(m\) is homotopy equivalent to \(\bigvee^m S^1\). This proves
\[
\overline{G_m}\simeq\bigvee^m S^1.
\]

Now let \(\varphi:(\overline{\mathfrak C},\mathfrak C)\to(\overline{\mathbb D_s},\mathbb D_s)\) be Michel's semialgebraic homeomorphism of pairs and set
\[
C_m=\mathfrak C\odot\{f_m\circ\varphi\}\subset\mathbf R^4.
\]
By the section-transfer proposition, \(C_m\) is a CAD cell and
\[
(\overline{C_m},C_m)\cong(\overline{G_m},G_m).
\]
The base closure \(\overline{\mathfrak C}\) is compact because it is homeomorphic to the closed unit disk, and \(f_m\) is bounded on the slit disk; hence \(C_m\) is bounded. The claimed homotopy, fundamental-group, and homology statements follow.

## Verification
The construction was checked against the full text of Michel's paper. Proposition 3.3 supplies the explicit cornet--slit-disk homeomorphism of pairs, Proposition 3.5 transfers sections while preserving closures, and Proposition 3.10 uses the same deformation formula above to retract one particular graph closure onto one circle.

For the present family, preservation of \(\overline{G_m}\) by the deformation is checked by the two half-planes \(x<0\) and \(x\ge0\), as in the proof. No finite experiment is used. The graph calculation is exact: the zero set of \(h_m\) on \([-1,0]\) has exactly \(m+1\) points, producing \(2m\) edges and cycle rank \(m\).

## Relationship to prior work
Michel constructs a bounded CAD cell in \(\mathbf R^4\) whose closure is not simply connected; in the proof of Proposition 3.10, that closure is explicitly retracted onto a single circle. The paper remarks that its methods can produce infinitely many distinct counterexamples, but it does not state an unbounded Betti-number theorem or construct closures with arbitrary free fundamental-group rank.

Davenport--Locatelli--Sankaran prove regularity, and hence ball-like closure behavior, for strong well-based CADs of bounded semialgebraic sets. Their theorem concerns a substantially stronger hypothesis and therefore does not imply any bound for arbitrary CAD-cell closures. Searches using the formulations “bounded CAD cell closure first Betti number,” “CAD cell closure fundamental group,” “cylindrical algebraic decomposition cell closure homology,” and “wedge of circles CAD cell closure” found no prior statement implying the family above.

## Limitations
The construction proves unbounded first Betti number and arbitrary finite free fundamental-group rank for closures of bounded CAD cells in \(\mathbf R^4\). It does not classify all homotopy types realizable as CAD-cell closures, does not assert analogous behavior in ambient dimension at most \(3\), and does not produce torsion in homology or higher-dimensional homology classes.

## References
L. Michel, “On some Exotic Cylindrical Algebraic Decompositions and Cells,” arXiv:2601.09795v1, first public 2026-01-14; especially Propositions 3.3, 3.5, and 3.10 and the discussion in Section 3.2.

J. H. Davenport, A. F. Locatelli, and G. K. Sankaran, “Regular cylindrical algebraic decomposition,” Journal of the London Mathematical Society 101 (2020), 43--59, DOI 10.1112/jlms.12257.
