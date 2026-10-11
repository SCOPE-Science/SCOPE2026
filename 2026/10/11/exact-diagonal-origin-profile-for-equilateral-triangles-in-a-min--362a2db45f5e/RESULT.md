# Exact diagonal-origin profile for equilateral triangles in a Minkowski square
## Finding
Let \(C=[-1,1]^2\) and let the Minkowski origin be \(z_c=(c,c)\), where \(0\le c<1\). For a positively oriented triangle \(P_1P_2P_3\subset C\), its cyclic oriented side lengths are the Minkowski lengths of \(P_2-P_1\), \(P_3-P_2\), and \(P_1-P_3\) for the gauge with unit disk \(C-z_c\). Let \(M(c)\) be the largest common side length among inscribed positively oriented equilateral triangles. Then
\[
M(c)=\max\!\left\{\frac{2}{1+c},\frac{1}{1-c}\right\}
=\begin{cases}
\frac{2}{1+c},&0\le c\le \frac13,\\
\frac{1}{1-c},&\frac13\le c<1.
\end{cases}
\]
The same formula holds for negative orientation. Hence the sharp minimum over diagonal origin positions is \(3/2\), reached exactly at the points that divide a square diagonal in the ratio \(1:2\), up to the symmetries of the square.

## Assumptions and scope
Write
\[
a=1-c,\qquad b=1+c.
\]
After translating the origin to zero, the unit disk is
\[
K_c=[-b,a]^2,
\]
and its oriented Minkowski functional is
\[
p_c(x,y)=\max\!\left\{\frac{x}{a},-\frac{x}{b},\frac{y}{a},-\frac{y}{b}\right\}.
\]
An inscribed positively oriented equilateral triangle means three boundary points of \(K_c\) whose cyclic side vectors have equal \(p_c\)-length. Degenerate triples are excluded. The statement classifies only this one-parameter square family; it does not assert a classification for arbitrary Minkowski unit disks.

## Proof
Let the common oriented side length be \(\lambda>0\), and let the cyclic side vectors be \(U,V,W\), so
\[
U+V+W=0,\qquad p_c(U)=p_c(V)=p_c(W)=\lambda.
\]
Put \(q_U=U/\lambda\), \(q_V=V/\lambda\), and \(q_W=W/\lambda\). Each normalized vector lies on \(\partial K_c\). Therefore, for each of the three normalized vectors, at least one coordinate is active on one of the four supporting lines
\[
x=a,\quad x=-b,\quad y=a,\quad y=-b.
\]
Choose one active coordinate for each vector. Two of the three chosen active coordinates use the same coordinate axis.

Suppose first that the two active values on that axis are \(a\) and \(-b\). One of the corresponding actual side vectors then has a coordinate of absolute value \(\lambda b\). Since every side joining two points of the square has each coordinate bounded by \(2\),
\[
\lambda b\le2,
\]
so \(\lambda\le2/b\).

Suppose instead that the two active values are both \(a\). Since the three normalized side vectors sum to zero, the third coordinate on this axis equals \(-2a\). Membership in \(K_c\) forces
\[
2a\le b,
\]
which is equivalent to \(c\ge1/3\). The corresponding actual side coordinate has absolute value \(2a\lambda\le2\), hence \(\lambda\le1/a\). Finally, if the two active values are both \(-b\), the third coordinate would be \(2b>a\), impossible.

Thus for \(0\le c<1/3\) only the mixed case can occur, giving \(\lambda\le2/b\). For \(c\ge1/3\), every case gives
\[
\lambda\le\max\!\left\{\frac2b,\frac1a\right\}.
\]
Because \(2/b=1/a\) exactly at \(c=1/3\), this is the claimed piecewise upper bound.

It remains to attain both branches. For \(0\le c\le1/3\), set
\[
t=-b+\frac{2a}{b}
\]
and use, in translated coordinates,
\[
P_1=(a,t),\qquad P_2=(-b,t),\qquad P_3=(t,-b).
\]
These points lie on \(\partial K_c\). Their cyclic side vectors are
\[
(-2,0),\qquad
\left(\frac{2a}{b},-\frac{2a}{b}\right),\qquad
\left(\frac{2(b-a)}{b},\frac{2a}{b}\right).
\]
The condition \(c\le1/3\) is exactly \(b-a\le a\), and direct evaluation of \(p_c\) gives common length \(2/b\). The signed area is positive.

For \(1/3\le c<1\), take
\[
P_1=(-b,-c),\qquad P_2=(-c,-b),\qquad P_3=(a,-b).
\]
The cyclic side vectors are
\[
(1,-1),\qquad(1,0),\qquad(-2,1).
\]
The condition \(c\ge1/3\) is equivalent to \(b\ge2a\), so all three vectors have \(p_c\)-length \(1/a\). Again the signed area is positive. This proves the positive-orientation formula. Interchanging the two coordinates preserves \(K_c\) and reverses orientation, so the negative-orientation maximum is identical.

The first branch decreases strictly and the second increases strictly, meeting only at \(c=1/3\), where the common value is \(3/2\). Central inversion handles the opposite direction on the same diagonal, and square symmetries give the corresponding points on the other diagonal.

## Verification
The upper bound uses only the boundary description of \(K_c\), the identity \(U+V+W=0\), and the coordinate diameter \(2\) of the square. The two constructions were checked by direct substitution into the displayed gauge. At \(c=1/3\), one has \(a=2/3\) and \(b=4/3\), and both branches give \(3/2\). The source extremizer condition \(2|zs_1|=|zs_3|\) is exactly this parameter value after the stated normalization.

No finite search is used for the theorem. The proof covers every \(c\) in the full nondegenerate range \(0\le c<1\) and both orientations.

## Relationship to prior work
Fabińska and Lassak introduced the asymmetric Minkowski-plane problem and, for a square whose origin divides a diagonal in the ratio \(1:2\), proved that every inscribed equilateral triangle has oriented side length at most \(3/2\). They used this single square to show that their conjectured universal \(3/2\) lower bound could not be improved. Their 2009 paper later proved the universal sharp \(3/2\) result. The present finding keeps the square fixed but moves the origin through the entire diagonal family, giving the exact maximum for every position and showing that the published extremal origin is the unique minimizer in that family, modulo square symmetries.

A 2025 review treats triangle perimeters in centrally symmetric normed planes and identifies the 2004 and 2009 papers as the corresponding non-centrally-symmetric literature. Its framework does not imply the asymmetric translated-square profile above.

## Limitations
The result concerns a square with origin constrained to a diagonal. It does not classify arbitrary interior origins of a square, arbitrary parallelograms with arbitrary origins, or arbitrary Minkowski unit disks. The literature comparison found no statement of the full two-branch profile, but an older 2003 conference-style paper by the same authors was not available in full text; it remains a residual indexing/access risk.

## References
1. E. Fabińska and M. Lassak, *Large Equilateral Triangles Inscribed in the Unit Disk of a Minkowski Plane*, Beiträge zur Algebra und Geometrie 45 (2004), 517–525. EUDML 233407.
2. E. Fabińska and M. Lassak, *Large triangles contained in the unit disk of a Minkowski plane*, Journal of Geometry 95 (2009), 31–39. DOI: 10.1007/s00022-009-0019-1.
3. J. Alonso, P. Martín Jiménez, and P. L. Papini, *Perimeter of Triangles Inscribed in the Unit Ball of Normed Planes*, Mediterranean Journal of Mathematics (2025). DOI: 10.1007/s00009-025-02805-6.
