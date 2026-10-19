# A six-dimensional image theorem for quaternion-contained generalized octonion commutators

## Finding

**Theorem.** Let \(F\) be a field of characteristic different from \(2\), let \(\mathcal O\) be a split octonion algebra over \(F\), and let \(H\subset\mathcal O\) be a quaternion *composition* subalgebra. Suppose \(A,B\in H\) are linearly independent, nonzero isotropic elements with \(N(A,B)=0\), where \(N(A,B)=N(A+B)-N(A)-N(B)\). Then

\[
\operatorname{Im}\bigl((x,y)\mapsto A(xy)-B(yx)\bigr)
=A\mathcal O+B\mathcal O,
\qquad \dim_F(A\mathcal O+B\mathcal O)=6.
\]

There is, moreover, a **single** \(h\in H\) for which the linear map \(y\mapsto A(hy)-B(yh)\) maps \(\mathcal O\) onto this six-dimensional space. The statement identifies an exact image (not only its linear span) in the quaternion-contained part of the orthogonal-zero-divisor case left open by the motivating classification [1].

## Assumptions and scope

The word *quaternion subalgebra* means a four-dimensional, unital, nondegenerate composition subalgebra; arbitrary degenerate associative subalgebras are not included. Because it contains a nonzero norm-zero element, \(H\) is split and can be identified with \(M_2(F)\). Choose a Cayley--Dickson complement \(\mathcal O=H\oplus H\omega\) with some \(\delta\in F^\times\) and

\[
(a+u\omega)(b+v\omega)=(ab+\delta\overline v u)+(va+u\overline b)\omega.
\]

Here \(\overline m=\operatorname{tr}(m)I-m\) for matrices \(m\in M_2(F)\). All products involving three octonions retain the parentheses shown in the theorem. No algebraic-closure or cardinality assumption on \(F\) is made.

## Proof

**1. An intrinsic upper bound and a block decomposition.** For arbitrary \(x,y\in\mathcal O\), the formula itself gives \(A(xy)-B(yx)\in A\mathcal O+B\mathcal O\). In Cayley--Dickson coordinates,

\[
A\mathcal O+B\mathcal O=(AH+BH)\oplus(HA+HB)\omega.
\]

For a fixed \(h\in H\) and variable \(z+r\omega\in\mathcal O\), direct multiplication gives

\[
A\bigl(h(z+r\omega)\bigr)-B\bigl((z+r\omega)h\bigr)
=(Ahz-Bzh)+\bigl(r(hA-\overline h B)\bigr)\omega.
\tag{1}
\]

Thus it suffices to choose \(h\) such that both matrix-space blocks of this linear map have full rank onto their respective summands. Equation (1) holds for every value of \(\delta\).

**2. Why there are precisely two cases.** Identify \(H=M_2(F)\). Since \(A\) and \(B\) are nonzero singular matrices, both have rank one. Write \(A=uv^{\mathsf T}\) and \(B=st^{\mathsf T}\). Polar orthogonality gives \(0=N(A+B)=\det(A+B)=\det[u,s]\det[v,t]\). Therefore their image lines agree, or their kernel lines agree. Both cannot agree because \(A,B\) are linearly independent. Simultaneous conjugation by \(\mathrm{GL}_2(F)\) normalizes the shared image to \(Fe_1\), or the shared kernel to \(Fe_2\). Such conjugation extends to the Cayley--Dickson algebra by applying it to both matrix components, because it commutes with the quaternion involution.

**3. Common image.** In the normalized form write

\[
A=\begin{pmatrix}a&b\\0&0\end{pmatrix},\quad
B=\begin{pmatrix}c&d\\0&0\end{pmatrix},\quad
\Delta=ad-bc\ne0.
\]

Here \(AH+BH\) is the two-dimensional space of first-row matrices, while \(HA+HB=H\). Choose a nonzero \(t\in F\) with \((a+bt-c,b-d)\ne(0,0)\), and take

\[
h=\begin{pmatrix}1&0\\t&1\end{pmatrix}.
\]

The choice is always possible: because \(A,B\) are independent, the excluded equation can hold for at most one value of \(t\), whereas \(F^\times\) contains at least two elements when \(\operatorname{char}(F)\ne2\). With the ordered basis \((E_{11},E_{12},E_{21},E_{22})\), the first component of (1), restricted to its nonzero output rows, has matrix

\[
\begin{pmatrix}
a+bt-c&-ct&b-d&-dt\\
0&a+bt-c&0&b-d
\end{pmatrix}.
\]

The displayed condition makes its rank exactly two. For the second block, the matrix \(D=hA-\overline hB\) has determinant

\[
\det D=2t\Delta\ne0.
\]

Right multiplication \(r\mapsto rD\) is therefore a bijection of \(H\). Hence (1) has rank \(2+4=6\) and image \((AH)\oplus H\omega=A\mathcal O+B\mathcal O\).

**4. Common kernel.** In the other normalized form write

\[
A=\begin{pmatrix}a&0\\b&0\end{pmatrix},\quad
B=\begin{pmatrix}c&0\\d&0\end{pmatrix},\quad
\Delta=ad-bc\ne0.
\]

Now \(AH+BH=H\), whereas \(HA=HB\) is the two-dimensional space of matrices with zero second column. Take \(h=E_{12}+E_{21}\). In the ordered basis \(E_{11},E_{12},E_{21},E_{22}\), the matrix of the first component \(z\mapsto Ahz-Bzh\) is

\[
\begin{pmatrix}
0&-c&a&0\\
-c&0&0&a\\
0&-d&b&0\\
-d&0&0&b
\end{pmatrix},
\qquad 
\det=-\Delta^2\ne0.
\]

Since \(\overline h=-h\), we have \(D=hA-\overline hB=h(A+B)\). The matrix \(h\) is invertible and \(A+B\) has rank one (the two nonzero column vectors are independent), so \(D\) has rank one. Consequently right multiplication \(r\mapsto rD\) on \(H\) has rank two, and its image is the common two-dimensional right ideal \(HA=HB\). Thus (1) has rank \(4+2=6\) and image \(H\oplus (HA)\omega=A\mathcal O+B\mathcal O\).

These are the only possible cases, so the upper bound is always attained by a fixed-slice linear map. This proves the theorem. \(\square\)

## Verification

The included `verify.py` implements the Cayley--Dickson multiplication and computes exact matrix ranks modulo \(3\), \(5\), and \(7\). For each prime, it exhaustively checks every ordered pair of independent row vectors in the common-image normal form and every ordered pair of independent column vectors in the common-kernel normal form. The numbers of pairs per form are respectively \(48\), \(480\), and \(2016\). Every prescribed fixed slice has rank six and lies in the stated target space. Run `python3 verify.py` to reproduce these checks.

The symbolic determinant identities and the two-dimensional output calculation above provide the proof over **all** fields in the stated characteristic; finite-field tests do not prove the universal assertion.

## Relationship to prior work

De Mello and Saini [1], Theorem 1.1(iii) and Proposition 5.1, show that for arbitrary independent orthogonal isotropic coefficients the **linear span** of the image has dimension six; they do not assert that the image itself is linear. Their Theorem 6.1 proves a corresponding image-is-subspace property when both variables range only in a quaternion algebra. Neither statement establishes a single six-dimensional linear slice of the *octonion* map. This theorem fills that distinction for coefficients co-contained in a quaternion composition subalgebra, with explicit witnesses in the two incidence types.

Panja, Saini and Singh [2] earlier studied generalized commutator images in the associative matrix algebra \(M_2(F)\), also a different evaluation domain. The matrix-algebra results and the six-dimensional span result are not claimed as new.

## Limitations

Pairs of independent orthogonal zero divisors that are **not** co-contained in any quaternion composition subalgebra remain outside this result; no claim is made that their images are subspaces. The characteristic-two case is excluded. The theorem does not classify images for arbitrary multilinear generalized polynomials. No independent mathematical audit has been performed.

## References

[1] T. C. de Mello and P. Saini, *Generalized commutator on octonion algebra*, arXiv:2610.04466v1 (first public version, 2026-10-03), Theorem 1.1 and Sections 2, 5, 6. https://arxiv.org/html/2610.04466v1

[2] S. Panja, P. Saini and A. Singh, *Images of polynomial maps with constants*, arXiv:2312.13865 (2023); later published in *Mathematika* 71 (2025), e70031. https://arxiv.org/abs/2312.13865
