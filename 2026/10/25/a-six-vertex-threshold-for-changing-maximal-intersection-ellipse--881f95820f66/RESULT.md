# A six-vertex threshold for changing maximal-intersection ellipse axes

## Finding
Let \(K\) be a centrally symmetric convex polygon in the Euclidean plane. For every ellipse area \(\lambda\) from the area of its John ellipse to that of its Löwner ellipse, write \(M_K(\lambda)\) for its unique maximal-intersection ellipse: among all ellipses of area \(\lambda\), it maximizes \(\operatorname{area}(E\cap K)\).

Every such family for a centrally symmetric polygon with at most four vertices is homothetic, and hence has common Euclidean principal axes. This property already fails at six vertices: the explicitly defined genuine hexagon
\[
K=\{(X,Y): |X|\le2,\ |3X+8Y|\le10,\ |-5X+24Y|\le26\}
\]
has two maximal-intersection ellipses with **strictly intermediate** areas whose positive-definite quadratic-form matrices do not commute. In particular, they cannot have a shared orthonormal principal-axis basis. Six vertices are the smallest possible among centrally symmetric planar polygons with this phenomenon.

## Assumptions and scope
A convex polygon is compact, full-dimensional, and has distinct extreme vertices; central symmetry is about its center. We use the unique John (maximum-area inscribed) and Löwner (minimum-area containing) ellipses. The fixed-area maximal-intersection family, and its uniqueness and continuity for planar centrally symmetric convex bodies, are as in Bochi, Theorem 1.2. An ellipse centered at the origin with symmetric positive-definite matrix \(Q\) is \(\{z:z^{\mathsf T}Qz\le1\}\). Two such ellipses have a common orthogonal principal-axis basis if and only if their matrices commute. The conclusion asserts noncoaxiality for some *two* intermediate members; it does not assert monotone rotation or prescribe the axes at every area.

## Proof
**Step 1: a rational six-vertex polygon.** Define
\[
H=\{(x,y): |x|\le1,\ |3x+4y|\le5,\ |-5x+12y|\le13\}.
\]
Its vertices are exactly the three opposite pairs \(\pm v_1,\pm v_2,\pm v_3\), where
\[
v_1=(1,1/2),\qquad v_2=(-1,2/3),\qquad v_3=(1/7,8/7).
\]
Indeed, substitution shows that each listed vertex lies on exactly two strip boundaries and satisfies the third; all six feasible intersections of nonparallel boundary lines appear on this list. Thus \(H\) is a genuine centrally symmetric hexagon. The displayed \(K\) is the image of \(H\) under \(T=\operatorname{diag}(2,1)\).

**Step 2: an exact John certificate.** Each bounding line of \(H\) is tangent to the unit disk \(B\), so \(B\subset H\). Take the unit contact vectors
\[
u_0=(1,0),\quad u_1=(3/5,4/5),\quad u_2=(-5/13,12/13)
\]
and the positive weights
\[
a_0=11/16,\quad a_1=125/224,\quad a_2=169/224.
\]
Direct rational calculation gives
\[
\sum_{i=0}^2 a_i u_i u_i^{\mathsf T}=I_2,\qquad \sum_{i=0}^2a_i=2.
\]
Give each of the opposite contacts \(\pm u_i\) weight \(a_i/2\). The first moments cancel, and the second moment is the identity. The sufficient contact condition in John's ellipse theorem proves \(J(H)=B\).

**Step 3: an exact Löwner certificate.** Define
\[
Q_0=\frac1{65}\begin{pmatrix}49&4\\4&48\end{pmatrix},\qquad
E_0=\{z:z^{\mathsf T}Q_0z\le1\}.
\]
The determinant is \(2336/4225>0\), and the first diagonal entry is positive. All three \(v_i\) lie on \(\partial E_0\). Since \(H\) is their centrally symmetric convex hull, \(H\subseteq E_0\). Let
\[
b_1=6929/12264,\quad b_2=12375/16352,\quad b_3=4753/7008.
\]
All are positive, and direct exact arithmetic yields
\[
\sum_{i=1}^3 b_iv_iv_i^{\mathsf T}
=Q_0^{-1}
=\begin{pmatrix}195/146&-65/584\\-65/584&3185/2336\end{pmatrix},
\qquad\sum_{i=1}^3b_i=2.
\]
Under \(Q_0^{1/2}\), the contact vectors become unit vectors, with identity second moment and vanishing first moment after symmetric splitting of the weights. The sufficient dual John–Löwner contact criterion proves \(L(H)=E_0\). These computations show the claimed ellipses are optimal, not merely feasible.

**Step 4: affine change and noncommutation.** The John and Löwner ellipse matrices of \(K=T H\) are, respectively,
\[
Q_J=\begin{pmatrix}1/4&0\\0&1\end{pmatrix},\qquad
Q_L=\frac1{65}\begin{pmatrix}49/4&2\\2&48\end{pmatrix}.
\]
Their commutator has entry
\[
(Q_JQ_L-Q_LQ_J)_{12}=(1/4-1)(2/65)=-3/130\ne0.
\]
The endpoint areas are \(2\pi\) and \(130\pi/\sqrt{2336}\), in increasing order. By the cited planar uniqueness/continuity theorem, \(M_K(\lambda)\) depends continuously on area through these endpoints and agrees there with the corresponding John and Löwner ellipses. Matrix entries therefore vary continuously. The commutator of matrices for two areas is continuous in the two parameters, and is nonzero at the pair of endpoints. Choosing both areas strictly inside, sufficiently close to the opposite endpoints, preserves noncommutation. Hence some two **intermediate** members have no common orthogonal axes.

**Step 5: minimal vertex count.** A centrally symmetric, full-dimensional planar polygon with fewer than six vertices must be a parallelogram. Every parallelogram is an invertible affine image of a square. A square is invariant under quarter-turn rotation. For each intermediate area its maximal-intersection ellipse is unique, so it is quarter-turn invariant and therefore a Euclidean disk. At both endpoints the unique John and Löwner ellipses have the same symmetry. Consequently the fixed-area family for the square consists of concentric disks; after any affine map, it consists of homothetic ellipses, with a shared orthogonal eigenspace decomposition. Thus no centrally symmetric quadrilateral exhibits the phenomenon.

## Verification
Run \(\texttt{python3 verify.py}\) with the standalone accompanying standard-library script. It enumerates all feasible strip-boundary intersections, checks the six-vertex description, proves positive definiteness and the three vertex boundary identities, verifies both positive contact-weight moment identities using exact rational arithmetic, checks the displayed inverse and endpoint nonzero commutator. The continuous-intermediate conclusion and four-vertex obstruction are deductions in the proof, not claims of numerical enumeration or finite exhaustive search over ellipses.

## Relationship to prior work
Artstein-Avidan and Katzin introduced fixed-area maximal intersection positions. Bochi established existence, uniqueness and continuous interpolation for centrally symmetric plane convex bodies, and supplied a nonpolygonal example in a separate discussion of maximal-intersection positions. The present contribution is a minimal **polygonal** counterexample to fixed axes, with independently checked rational John and Löwner contact certificates. Classical John–Löwner contact optimality criteria are inputs, not claimed as new.

## Limitations
The example proves the existence of two noncoaxial interior members without calculating the entire intermediate path, its rate of change, or whether a continuous principal eigenvector can be globally selected without degeneracies. The result is confined to planar centrally symmetric polygons, and does not cover arbitrary convex bodies, noncentrally symmetric quadrilaterals, higher-dimensional polytopes, or uniqueness of unconstrained-area approximants. The priority comparison is based on relevant accessible literature and search records; it is not an exhaustive proof of publication priority. No independent mathematical review has been performed.

## References
1. S. Artstein-Avidan and D. Katzin, *Isotropic Measures and Maximizing Ellipsoids: Between John and Loewner*, arXiv:1612.01128, first posted 2016-12-04, https://arxiv.org/html/1612.01128v1 .
2. J. Bochi, *On the approximation of convex bodies by ellipses with respect to the symmetric difference metric*, arXiv:1702.03808, first posted 2017-02-13, especially Theorem 1.2 and Section 5, https://arxiv.org/html/1702.03808v3 .
3. F. John, *Extremum Problems with Inequalities as Subsidiary Conditions*, 1948; standard contact characterization also discussed in Bochi, Section 5.2.
