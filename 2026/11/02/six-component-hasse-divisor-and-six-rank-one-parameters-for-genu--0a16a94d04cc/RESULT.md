# Six-component Hasse divisor and six rank-one parameters for genus-three Howe curves in characteristic five

## Finding
Let \(k=\overline{\mathbb F}_5\), and let
\[
U=\{(a,b)\in k^2:(a-b)(a^2-4)(b^2-4)\ne0\}.
\]
For \((a,b)\in U\), let \(C_{a,b}\) be the smooth projective genus-three curve with affine equation
\[
y^2=(x^4-ax^2+1)(x^4-bx^2+1).
\]
Put
\[
Q=a^2-ab+b^2-1,\quad P_+=Q+2(a+b),\quad P_-=Q-2(a+b),
\]
and
\[
R=a^2b^2+2a^2-2ab+2b^2+1.
\]
The geometric Jacobian \(5\)-rank and \(a\)-number, for every \((a,b)\in U\), are
\[
f_5(C_{a,b})=\mathbf1_{P_+\ne0}+\mathbf1_{P_-\ne0}+\mathbf1_{R\ne0},\qquad a(C_{a,b})=3-f_5(C_{a,b}).
\]
The reduced nonordinary Hasse divisor \(V(P_+P_-R)\cap U\) has exactly six distinct geometrically irreducible smooth components: four affine lines and two hyperbolas. Its rank-one locus is precisely the following six reduced transverse double-intersection points:
\[
\begin{array}{ll}
P_+=P_-=0:&b=-a,\quad a^2=2;\\
P_+=R=0:&b=-a-2,\quad a^2+2a-2=0;\\
P_-=R=0:&b=-a+2,\quad a^2-2a-2=0.
\end{array}
\]
Each displayed quadratic has two distinct roots. These six points are all defined over \(\mathbb F_{25}\), none over \(\mathbb F_5\). No smooth member has \(5\)-rank zero. Every rank \(1,2,3\) occurs.

## Assumptions and scope
All assertions are over \(k=\overline{\mathbb F}_5\); coefficient pairs are ordered, in the displayed fixed-coordinate normal form. They are not being counted modulo curve isomorphism. The condition defining \(U\) is exactly the squarefreeness condition for the degree-eight polynomial, as established for this normal form in Ohashi's Lemma 3.1 [1]. The genus is three, because the squarefree defining polynomial has degree eight. The Hasse divisor here means the zero divisor of the determinant of the Hasse--Witt matrix on the smooth coefficient space; no assertion is made about extending that divisor through singular models.

## Proof
Write \(F(x)=(x^4-ax^2+1)(x^4-bx^2+1)\) and expand \(F(x)^2=\sum_m c_m x^m\). For the regular differential basis \(dx/y,x\,dx/y,x^2\,dx/y\), the characteristic-five Cartier--Manin coefficient matrix has entries \(c_{5i-j}\), with \(1\le i,j\le3\), up to the customary Frobenius-root/dual convention. Direct expansion gives the symmetric matrix
\[
H=\begin{pmatrix}
Q&0&-2(a+b)\\0&R&0\\-2(a+b)&0&Q
\end{pmatrix}.
\]
The constant vectors \((1,0,1),(1,0,-1),(0,1,0)\), whose coordinates lie in \(\mathbb F_5\), diagonalize \(H\) with diagonal entries \(P_-,P_+,R\), respectively. This also diagonalizes all Frobenius-twisted Cartier iterates, since the change-of-basis matrix is Frobenius-fixed. A semilinear one-dimensional operator with nonzero scalar has stable image of dimension one; with zero scalar it has stable image zero. Thus the \(5\)-rank is the number of nonzero entries among these three scalars, and the first Cartier rank is the same number. The \(a\)-number is three minus the first Cartier rank.

Put \(\eta^2-\eta+1=0\) and \(\tau^2=3\) in \(\mathbb F_{25}\). The following identities hold in characteristic five:
\[
\begin{split}
P_+&=(a+2)^2-(a+2)(b+2)+(b+2)^2\\
&=(a+2-\eta(b+2))(a+2-(1-\eta)(b+2)),\\
P_-&=(a-2-\eta(b-2))(a-2-(1-\eta)(b-2)),\\
R&=(ab+1)^2+2(a-b)^2\\
&=((a-\tau)(b+\tau)-1)((a+\tau)(b-\tau)-1).
\end{split}
\]
The first four factors are distinct lines, whose paired crossing points \((-2,-2)\) and \((2,2)\) lie outside \(U\). The last two factors are smooth irreducible affine hyperbolas. Their only mutual intersections have \(a=b\) and \(a^2=-1\), hence also lie outside \(U\). Each component has nonempty intersection with \(U\), and the six factors are pairwise distinct. This proves the geometric component and smoothness assertions.

To classify double intersections between *different* Hasse eigenvalue factors, first \(P_+-P_-=4(a+b)\) gives \(b=-a\), and then \(P_+=0\) gives \(3a^2-1=0\), or \(a^2=2\). At these two points direct substitution gives \(R=2\ne0\).

For \(P_+=R=0\), exact elimination in \(\mathbb F_5[a,b]\) gives
\[
\operatorname{Res}_b(P_+,R)=(a+2)^6(a^2+2a-2).
\]
When \(a=-2\), \(P_+=0\) forces \(b=-2\), which is excluded. For either simple root of \(a^2+2a-2\), the unique common \(b\)-root is \(b=-a-2\), as follows also by substituting into both equations and using their degree-two common-root calculation. Analogously,
\[
\operatorname{Res}_b(P_-,R)=(a-2)^6(a^2-2a-2),
\]
and outside the excluded point \((2,2)\) the solutions have \(b=-a+2\). All six resulting points satisfy \((a-b)(a^2-4)(b^2-4)\ne0\). There are no triple eigenvalue intersections, because \(R=2\) on \(V(P_+,P_-)\).

Finally, the Jacobian determinants of the corresponding pairs \((P_+,P_-)\), \((P_+,R)\), \((P_-,R)\), respectively, reduce on their solution sets to \(a\), \(2a+2\), and \(2-2a\). Each is coprime to the respective displayed quadratic defining its intersection parameters, establishing transversality and reducedness. The first pair is defined by \(a^2=2\) (whose discriminant is \(3\)); the other two quadratics each have discriminant \(2\). Both \(2\) and \(3\) are nonsquares in \(\mathbb F_5\), but become squares in \(\mathbb F_{25}\); hence the six points form three length-two Frobenius orbits. Their two zero Hasse eigenvalues give rank one, and there are no other rank-one points. The other ranks occur by moving off all components or onto exactly one component.

## Verification
The standalone script `verify_symbolic.py` recomputes \(F^2\), its Cartier--Manin coefficients, the determinant factorization, the six-factor identity, both elimination resultants, the intersection ideals and the nonvanishing intersection Jacobians, using exact characteristic-five polynomial arithmetic. It prints `HOWE_CHAR5_SYMBOLIC_HASSE_SIX_COMPONENTS_SIX_TRANSVERSE_POINTS_OK`.

The independently implemented `verify_fields.py` works directly in \(\mathbb F_{25}=\mathbb F_5[\tau]/(\tau^2-3)\), computes the matrix from polynomial convolution rather than substituting the displayed matrix, and iterates the semilinear operator. It exhaustively checks all 625 ordered coefficient pairs, comprising 119 singular models and 506 smooth models. Among the smooth pairs it finds 380 of rank three, 120 of rank two, and six of rank one, with \(a\)-numbers zero, one, and two, respectively. These finite counts corroborate but do not replace the geometric proof.

To replay from this directory, run `python verify_symbolic.py` (requires SymPy) and `python verify_fields.py` (Python standard library only).

## Relationship to prior work
Ohashi [1] establishes the normal form, its smoothness criterion, elliptic-quotient decomposition, and a maximality/minimality theorem **conditional on superspeciality**. Moriya and Kudo [2] supply explicit Richelot-isogeny constructions and enumeration methods for superspecial genus-three Howe curves. The present theorem concerns the complete characteristic-five ordinary and lower-rank stratification and the detailed six-component incidence geometry, not the elliptic decomposition itself. The absence of superspecial hyperelliptic genus-three curves in characteristic five is independently known from Ekedahl's bound (see [3]); it is not asserted here as novel in isolation. The novelty assessment is limited to the explicit Hasse-divisor geometry and six-point rank-one classification for this natural normal form.

## Limitations
The points and components are coefficient-marked; no distinctness claim is made about abstract curve-isomorphism classes. The theorem does not determine zeta functions or Newton polygons beyond \(5\)-rank, nor does it classify families with a different normalized equation. Earlier unindexed equivalent computations or reductions from more general formulas remain possible; primary-literature comparison supports but does not certify priority. No independent external mathematical validation has been performed.

## References
[1] R. Ohashi, *On the maximality of hyperelliptic Howe curves of genus 3*, arXiv:2112.11152, first posted 2021-12-21, Lemma 3.1, Section 3, Theorem 1.1. https://arxiv.org/abs/2112.11152

[2] T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926, first posted 2022-09-07, Sections 3--5. https://arxiv.org/abs/2209.02926

[3] R. Ohashi, H. Onuki, M. Kudo, R. Yoshizumi, K. Nuida, *Listing superspecial curves of genus three using Richelot isogeny graphs*, arXiv:2401.10500 (2024), published version Remark 4.1 on Ekedahl's bound. https://arxiv.org/abs/2401.10500
