# The free middle lattice of Tufo's Enriques Fano host is \(I_{11,2}\)
## Finding
Let \(S\) be a general complex Enriques surface and let \(Y\) be the smooth Fano fourfold constructed by Federico Tufo. Thus
\[
Y\cong \operatorname{Bl}_S(\mathbf P^2\times\mathbf P^2),
\]
and the same variety is a general complete intersection of multidegrees \((1,2,0)\) and \((1,0,2)\) in \(\mathbf P^2\times\mathbf P^2\times\mathbf P^2\).

Write
\[
L_Y=H^4(Y,\mathbf Z)/\operatorname{tors}
\]
with the middle cup-product pairing. Then
\[
L_Y\cong I_{11,2}\cong
\langle1\rangle^{\oplus11}\oplus\langle-1\rangle^{\oplus2}.
\]
In particular, the free middle lattice is odd and unimodular, has rank \(13\), and has signature \((11,2)\).

## Assumptions and scope
Everything is taken after embedding the ground number field into \(\mathbf C\), so singular cohomology is used. The claim concerns the free quotient of \(H^4(Y,\mathbf Z)\); Tufo's \(2\)-torsion class in middle cohomology is not part of the lattice \(L_Y\).

Let \(X=\mathbf P^2\times\mathbf P^2\), let \(\pi:Y\to X\) be the blow-up map, let \(E\subset Y\) be the exceptional divisor, and write \(j:E\hookrightarrow Y\) and \(p:E\to S\). Let \(h_1,h_2\) be the two hyperplane classes on \(X\).

## Proof
For a blow-up along a smooth codimension-two center, the integral additive decomposition in degree four is
\[
H^4(Y,\mathbf Z)\cong \pi^*H^4(X,\mathbf Z)\oplus j_*p^*H^2(S,\mathbf Z).
\]
Tufo's computation is consistent with this decomposition: it gives a free rank-three summand from \(X\), the rank-ten Enriques lattice, and one \(2\)-torsion class.

The two summands are orthogonal for the middle pairing. Indeed, for \(a\in H^4(X,\mathbf Z)\) and \(b\in H^2(S,\mathbf Z)\), the projection formula gives
\[
\int_Y \pi^*a\,j_*p^*b
=
\int_E p^*(i^*a\,b)=0,
\]
because \(i^*a\,b\in H^6(S,\mathbf Z)=0\). For \(b,c\in H^2(S,\mathbf Z)\), the self-intersection formula and \(N_{E/Y}\cong\mathcal O_E(-1)\) give
\[
\int_Y j_*p^*b\,j_*p^*c
=
-\int_S b\,c.
\]
Thus on the free part the exceptional contribution is the negative of the Enriques intersection lattice.

On \(H^4(X,\mathbf Z)\), use the ordered basis
\[
(h_1^2,h_2^2,h_1h_2).
\]
Since \(h_1^3=h_2^3=0\) and \(\int_Xh_1^2h_2^2=1\), the Gram matrix is
\[
\begin{pmatrix}
0&1&0\\
1&0&0\\
0&0&1
\end{pmatrix},
\]
so this summand is \(U\oplus\langle1\rangle\), where \(U\) is the hyperbolic plane.

For a complex Enriques surface,
\[
H^2(S,\mathbf Z)/\operatorname{tors}
\cong
\operatorname{Num}(S)
\cong U\oplus E_8(-1),
\]
an even unimodular lattice of signature \((1,9)\). Therefore
\[
L_Y
\cong
\bigl(U\oplus\langle1\rangle\bigr)
\oplus
-\bigl(U\oplus E_8(-1)\bigr)
\cong
U^{\oplus2}\oplus E_8\oplus\langle1\rangle,
\]
where \(E_8\) in the last expression is positive definite. This lattice is unimodular, is odd because it contains a vector of square \(1\), and has signature
\[
(2,1)+(9,1)=(11,2).
\]
The classification of indefinite odd unimodular integral lattices now gives the unique lattice with this signature:
\[
L_Y\cong I_{11,2}.
\]

## Verification
The bundled `verify.py` constructs the Gram matrix
\[
U\oplus\langle1\rangle\oplus U\oplus E_8
\]
with exact integer arithmetic. It checks rank \(13\), determinant \(1\), odd parity, and inertia \((11,2)\). The stored output is `verification_output.txt`.

The script is only a finite consistency check of the displayed matrix. The general mathematical proof is the blow-up cup-product calculation above together with the standard Enriques lattice and the classification of indefinite odd unimodular lattices.

## Relationship to prior work
Tufo determines the complete-intersection and blow-up descriptions, the diagonal Hodge diamond, and the integral cohomology groups. In particular, his preprint records
\[
H^4(Y,\mathbf Z)\cong\mathbf Z^3\oplus\Lambda\oplus\mathbf Z/2\mathbf Z,
\]
where \(\Lambda\) is the rank-ten Enriques lattice. The inspected source does not determine the middle cup-product pairing or state the resulting isometry class \(I_{11,2}\).

Dolgachev records the classical identification \(\operatorname{Num}(S)\cong U\oplus E_8(-1)\). Combining that lattice with the codimension-two blow-up pairing determines the full free middle intersection lattice of Tufo's fourfold, rather than only its underlying abelian group.

Targeted searches under the exact source identifier, the complete-intersection multidegrees, signature language, and odd-unimodular-lattice language located no statement implying this lattice identification.

## Limitations
The result does not determine the torsion linking form, the full integral cohomology ring, characteristic classes, or the diffeomorphism type of \(Y\). It applies to Tufo's smooth general fourfold over \(\mathbf C\); no claim is made for singular degenerations or positive-characteristic analogues. An unindexed source could conceivably contain the same lattice calculation.

## References
1. Federico Tufo, *On the Fano dimension of an Enriques surface*, arXiv:2602.03385v1; published in *Comptes Rendus Mathématique* 364 (2026), 495--499, DOI 10.5802/crmath.840.
2. Igor V. Dolgachev, *A brief introduction to Enriques surfaces*, arXiv:1412.7744v2, especially the description of \(\operatorname{Num}(S)\) as \(U\oplus E_8(-1)\).
3. Standard blow-up cohomology and Gysin self-intersection formulas for a smooth codimension-two center, together with the classification of indefinite odd unimodular integral lattices.
