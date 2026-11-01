# Fourier support of the \(2\times2\) matrix-square graph in all characteristics

## Finding
Let \(\mathbb F_q\) be a finite field of arbitrary prime-power order \(q\ge2\), let \(V=M_2(\mathbb F_q)\), and put
\[
\mathcal P_q=\{(X,X^2):X\in V\}\subset V\oplus V.
\]
Fix the canonical additive character \(\psi_q(t)=\exp(2\pi i\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(t)/p)\), where \(p\) is the characteristic. Identify the additive dual of \(V\oplus V\) by the trace pairing, and define the unnormalized coefficient
\[
F_q(A,B)=\sum_{X\in V}\psi_q\bigl(\operatorname{tr}(AX+BX^2)\bigr),\qquad A,B\in V.
\]
Here \(\operatorname{tr}\) denotes the matrix trace, not the field trace.

**Odd characteristic.** The coefficient \(F_q(A,B)\) is nonzero exactly in the following four mutually exclusive cases:

1. \(B=0\) and \(A=0\).
2. \(B\ne0\), \(\operatorname{tr}B=0\), and \(A\in\mathbb F_qI+\mathbb F_qB\).
3. \(\det B=0\), \(\operatorname{tr}B\ne0\), and \(\operatorname{tr}(AB)=\operatorname{tr}(A)\operatorname{tr}(B)\).
4. \(\det B\ne0\) and \(\operatorname{tr}B\ne0\), with arbitrary \(A\).

The singular values of unnormalized additive convolution by \(\mathbf1_{\mathcal P_q}\), including multiplicity, are

| Singular value | Multiplicity |
|---|---|
| \(q^4\) | \(1\) |
| \(q^3\) | \(q^2(q^3-1)\) |
| \(q^{5/2}\) | \(q^3(q^3-q)\) |
| \(q^2\) | \(q^4(q^4-2q^3+q)\) |
| \(0\) | \(q^8-R_{\mathrm{odd}}(q)\) |

where
\[
\boxed{R_{\mathrm{odd}}(q)=q^8-2q^7+q^6+2q^5-q^4-q^2+1.}
\]

**Characteristic two.** For \(q=2^m\), the nonzero coefficients are characterized as follows:

1. If \(B=\lambda I\) is scalar, exactly \(A=\lambda^{q/2}I\) survives.
2. If \(B\) is nonscalar, exactly the \(q^2\) solutions of
\[
\operatorname{tr}A=(\operatorname{tr}B)^{q/2},\qquad
\operatorname{tr}(AB)=(\operatorname{tr}(B^3))^{q/2}
\]
survive.

The singular values and multiplicities are

| Singular value | Multiplicity |
|---|---|
| \(q^4\) | \(q\) |
| \(q^3\) | \(q^2(q^4-q)\) |
| \(0\) | \(q^8-R_{\mathrm{even}}(q)\) |

with
\[
\boxed{R_{\mathrm{even}}(q)=q^6-q^3+q.}
\]
In particular, the fraction of supported additive Fourier frequencies tends to \(1\) as odd \(q\to\infty\), but tends to \(0\), at rate \(q^{-2}\), as powers of two grow. This is a characteristic-dependent dichotomy for the same noncommutative polynomial graph.

## Assumptions and scope
All finite fields, including non-prime fields, are covered. The trace pairing \(\langle A,X\rangle=\operatorname{tr}(AX)\) is nondegenerate. The Fourier coefficients above use the positive phase. If convolution is defined by \(Tf(z)=\sum_{w\in\mathcal P_q}f(z-w)\), a character indexed by \((A,B)\) has eigenvalue \(F_q(-A,-B)\); the zero sets and all stated singular-value multiplicities are unaffected by this sign convention. No normalization by the ambient group order is used.

## Proof
**1. Quadratic Fourier lemma.** Set \(Q_B(X)=\operatorname{tr}(BX^2)\) and define the self-adjoint linear operator
\[
L_B(X)=BX+XB.
\]
Cyclicity of matrix trace gives
\[
Q_B(X+Y)-Q_B(X)-Q_B(Y)=\operatorname{tr}(L_B(X)Y).
\]
Let \(K_B=\ker L_B\), and let \(r_B=4-\dim_{\mathbb F_q}K_B\). Squaring the absolute value of the character sum, changing \(X\) to \(X+H\), and summing first in \(X\) yields
\[
|F_q(A,B)|^2=q^4\sum_{H\in K_B}\psi_q\bigl(Q_B(H)+\operatorname{tr}(AH)\bigr).
\]
The phase restricted to \(K_B\) is an additive character, so the last sum is either \(|K_B|\) or \(0\). Therefore, in every characteristic,
\[
|F_q(A,B)|\in\{0,q^{4-r_B/2}\},
\]
and nonvanishing occurs if and only if the restricted additive phase is identically one. This proof uses exact character orthogonality and applies to non-prime fields.

**2. Odd characteristic.** For \(H\in K_B\), polarization at \((H,H)\) gives \(2Q_B(H)=0\), hence \(Q_B(H)=0\). Thus nonvanishing is equivalent to \(A\in K_B^\perp=\operatorname{im}L_B\); the last equality follows from self-adjointness. A direct polynomial determinant calculation gives
\[
\det(L_B)=4\det(B)(\operatorname{tr}B)^2.
\]
If both determinant and trace of \(B\) are nonzero, the image is all of \(V\). For \(B=0\) it is zero. If \(B\ne0\) is traceless, a direct \(2\times2\) multiplication shows \(\operatorname{im}L_B=\mathbb F_qI+\mathbb F_qB\), of dimension two, whether \(B\) is invertible or nilpotent. If \(\det B=0\) and \(t=\operatorname{tr}B\ne0\), then \(B^2=tB\) and \(\ker L_B=\mathbb F_q(I-B/t)\), so its image is the stated trace hyperplane of dimension three. This proves the four nonvanishing cases and all corresponding magnitudes.

**3. Characteristic two.** The operator \(L_B\) is the commutator map. If \(B=\lambda I\), it is zero and
\[
Q_B(X)=\lambda(\operatorname{tr}X)^2.
\]
For the canonical field character, \(\psi_q(cu^2)=\psi_q(c^{q/2}u)\). Nonvanishing therefore requires \(A=\lambda^{q/2}I\). If \(B\) is nonscalar, its matrix centralizer is exactly \(K_B=\mathbb F_qI+\mathbb F_qB\), of dimension two. For \(H=sI+tB\),
\[
Q_B(H)=s^2\operatorname{tr}B+t^2\operatorname{tr}(B^3).
\]
The additive phase on \(K_B\) is identically one precisely when the two field-linear coefficient identities displayed in the finding hold. They are independent because \(I,B\) are linearly independent and the trace pairing is nondegenerate. Hence each nonscalar \(B\) admits exactly \(q^2\) supported first frequencies.

**4. Multiplicities.** In odd characteristic, the number of matrices \(B\) in the respective rank classes \(r_B=0,2,3,4\) is
\[
1,\quad q^3-1,\quad q^3-q,\quad q^4-2q^3+q.
\]
Indeed, the trace-zero subspace has size \(q^3\). The rank-one matrices with nonzero trace number \(q^3-q\): the total number of nonzero rank-one matrices is \((q^2-1)^2/(q-1)\), of which \(q^2-1\) are nonzero nilpotents. Every \(B\) of rank \(r_B\) supports exactly \(q^{r_B}\) values of \(A\). Multiplying these counts proves each odd-characteristic singular-value multiplicity and the rank polynomial. In characteristic two, exactly \(q\) matrices \(B\) are scalar and \(q^4-q\) are nonscalar; their respective supported first-frequency counts are \(1\) and \(q^2\). This gives the second table and its rank polynomial. The asymptotic claims follow by division by the ambient dimension \(q^8\).

## Verification
Run the included standalone checker with `python3 verify_matrix_square_graph.py`. It uses exact integers: cyclotomic-coefficient tests for odd characteristic, Walsh sums for characteristic two, and finite-field arithmetic without numerical tolerances. It exhaustively evaluates all \(256\) frequencies at \(q=2\) and all \(6561\) frequencies at \(q=3\), and checks deterministic samples and all matrix-parameter rank strata at \(q=4,5,9\). Its final output is `ALL_MATRIX_SQUARE_EXACT_CHECKS_OK`. The enumeration is not used as a proof for arbitrary fields; the preceding quadratic-radical argument proves the theorem uniformly.

## Relationship to prior work
Finite-field paraboloid Fourier transforms and quadratic Gauss sums are classical. Iosevich and Koh (2008, arXiv:0805.0814, Section 3, Lemmas 5 and 6) treat the scalar quadratic paraboloid and its Fourier coefficients for odd fields. Their nondegenerate scalar-quadratic calculation does not directly supply the matrix-square family, the singular Sylvester strata, or the characteristic-two affine frequency conditions. The general quadratic-form Fourier lemma is standard and is deliberately not claimed as new; the contribution here is its complete matrix-square specialization and the resulting exact uniform spectral distribution and characteristic dichotomy. Related studies of finite-field quadratic maps and zero-difference-balanced functions (Carlet, Gong and Tan, arXiv:1410.2903) address different scalar-field polynomial families. No proof of a broader priority or novelty claim is supplied by unsuccessful searches.

## Limitations
This is an exact statement only for \(2\times2\) matrices over finite fields. It does not classify the complex phases of the nonzero Fourier coefficients, spectra for larger matrix sizes, or prime-power rings. The originality comparison is bounded by accessible historical literature and indexed research records; a matrix-Jordan-algebra or quadratic-map result with equivalent rank counts could exist. Independent validation has not been performed.

## References
- A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, first public preprint 2008-04-28, arXiv:0804.4505.
- A. Iosevich and D. Koh, *Extension Theorems for Paraboloids in the Finite Field Setting*, first public preprint 2008-05-06, arXiv:0805.0814 (especially Section 3).
- C. Carlet, G. Gong and Y. Tan, *Quadratic Zero-Difference Balanced Functions, APN Functions and Strongly Regular Graphs*, first public preprint 2014-10-10, arXiv:1410.2903.
