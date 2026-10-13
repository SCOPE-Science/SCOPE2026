# The \(M_{72}\) minifold has two anticanonical Hilbert functions in its right-dual collection
## Finding
Let \(M_{72}\) be the three-dimensional non-commutative Fano minifold constructed by Loginov and Orlov, and put
\[
T=S^{-1}[3].
\]
Write the standard exceptional collection as
\[
\mathcal P=(P_3,P_2,P_1,P_0)
\]
and order its right dual as
\[
\mathcal P^\vee=(E_1,E_2,E_3,E_4)
\]
so that the Euler matrix is
\[
A=
\begin{pmatrix}
1&3&7&6\\
0&1&6&7\\
0&0&1&3\\
0&0&0&1
\end{pmatrix}.
\]
For every integer \(p\ge0\), define
\[
h_i(p)=\dim_{\mathbf C}\operatorname{Hom}(E_i,T^pE_i).
\]
Then the four functions take exactly two values:
\[
h_1(p)=h_4(p)
=(2p+1)(6p^2+6p+1)
=12p^3+18p^2+8p+1,
\]
whereas
\[
h_2(p)=h_3(p)
=(2p+1)(24p^2+24p+1)
=48p^3+72p^2+26p+1.
\]
Equivalently,
\[
\sum_{p\ge0}h_1(p)t^p
=
\sum_{p\ge0}h_4(p)t^p
=
\frac{1+35t+35t^2+t^3}{(1-t)^4},
\]
and
\[
\sum_{p\ge0}h_2(p)t^p
=
\sum_{p\ge0}h_3(p)t^p
=
\frac{1+143t+143t^2+t^3}{(1-t)^4}.
\]

For comparison, all four objects of the standard collection \(\mathcal P\) have the first Hilbert function. Hence passing to the right dual changes the complete anticanonical Hilbert polynomial for exactly the two middle objects, and their leading coefficient is four times larger. This gives an explicit boundary to object-independence: the Hilbert dimension remains \(3\), as proved generally by Loginov--Orlov, but the Hilbert polynomial itself need not be invariant under right duality.

## Assumptions and scope
The ground field is \(\mathbf C\). The object \(M_{72}\), the functor \(T=S^{-1}[3]\), and the two exceptional collections are those of arXiv:2609.39766v1.

The source constructs \(M_{72}\) from a periodic quadratic \(\mathbf Z\)-algebra, identifies \(\mathcal P\) as a full strong exceptional collection, and gives the Euler matrices
\[
A_{\mathrm{pr}}=
\begin{pmatrix}
1&3&11&18\\
0&1&6&11\\
0&0&1&3\\
0&0&0&1
\end{pmatrix},
\qquad
A=
\begin{pmatrix}
1&3&7&6\\
0&1&6&7\\
0&0&1&3\\
0&0&0&1
\end{pmatrix}
\]
for \(\mathcal P\) and \(\mathcal P^\vee\), respectively. The relevant helices are geometric, so the Euler characteristics computed below are actual Hom dimensions in nonnegative anticanonical degree.

No assertion is made about arbitrary exceptional objects outside these two distinguished collections.

## Proof
For an Euler matrix \(A\), Loginov--Orlov identify the action of \(T\) on numerical \(K\)-theory as
\[
T_*=-A^{-t}A.
\]
Write
\[
N=T_*-I.
\]
Maximal unipotence in dimension three gives \(N^4=0\). Their binomial formula therefore yields, for the \(i\)-th basis vector \(e_i\),
\[
h_i(p)
=
e_i^t A T_*^p e_i
=
\sum_{k=0}^3
\binom pk\, e_i^t A N^k e_i.
\]

For the right-dual matrix \(A\), exact multiplication gives the four coefficient vectors
\[
(1,38,108,72),\quad
(1,146,432,288),\quad
(1,146,432,288),\quad
(1,38,108,72).
\]
Thus
\[
h_1(p)=h_4(p)
=
1+38p+108\binom p2+72\binom p3
=
12p^3+18p^2+8p+1,
\]
and
\[
h_2(p)=h_3(p)
=
1+146p+432\binom p2+288\binom p3
=
48p^3+72p^2+26p+1.
\]

Applying the same calculation to \(A_{\mathrm{pr}}\) gives
\[
e_i^t A_{\mathrm{pr}}(T_{\mathrm{pr}}-I)^k e_i
=
(1,38,108,72)_k
\]
for every \(i=1,2,3,4\). Hence every object of \(\mathcal P\) has the first polynomial. For \(P_0\), this agrees with the polynomial printed explicitly in the source from its second-Veronese description.

The rational generating functions follow by multiplying the series of each cubic polynomial by \((1-t)^4\). The numerators are
\[
1+35t+35t^2+t^3
\]
and
\[
1+143t+143t^2+t^3.
\]

## Verification
The bundled `verify.py` uses exact rational arithmetic and reconstructs both Euler matrices. It inverts them, computes
\[
T_*=-A^{-t}A,
\]
checks \(N^4=0\), recomputes all eight binomial-basis coefficient vectors, expands the two resulting polynomials, and recovers both Hilbert-series numerators. Its saved output ends in `VERIFY_OK`.

The computational step is an exact finite matrix identity, not evidence for only finitely many values of \(p\). The universal formulas follow because \(N^4=0\), so the binomial expansion of \(T_*^p\) terminates identically for every \(p\ge0\).

## Relationship to prior work
Loginov--Orlov prove that for any object in a geometric helix of a three-dimensional non-commutative minifold, the anticanonical Hilbert function is a cubic polynomial with positive leading coefficient, and consequently its degree is independent of the chosen object. In their \(M_{72}\) construction they compute
\[
12p^3+18p^2+8p+1
\]
for \(P_0\), then print the Euler matrix of the right-dual collection in order to identify the Euler-degree-\(72\) mutation class.

The source does not compute the four right-dual Hilbert functions or state that two of them have leading coefficient four times the other two. Targeted searches for the exact middle polynomial, the numerator \(1+143t+143t^2+t^3\), the right-dual matrix together with Hilbert-function language, and object-dependence of the \(M_{72}\) anticanonical Hilbert polynomial did not locate an implication-equivalent statement.

The new calculation therefore sharpens the source's general invariance statement: Hilbert dimension is object-independent, but already on its new non-commutative minifold the full Hilbert polynomial is not invariant under right duality.

## Limitations
The result concerns the two distinguished exceptional collections in the \(M_{72}\) family. It does not classify the Hilbert polynomials of every exceptional object or every mutation in the full braid-group orbit.

The equality between Euler characteristic and Hom dimension uses geometricity of the relevant helices. Without this vanishing property, the same numerical matrix calculation would determine only Euler characteristics.

The finding does not identify the graded anticanonical algebras for the middle right-dual objects up to algebra isomorphism; it determines their Hilbert functions and Hilbert series.

## References
1. Konstantin Loginov and Dmitri Orlov, *Non-commutative Fano varieties and three-dimensional minifolds*, arXiv:2609.39766v1, 30 September 2026.
