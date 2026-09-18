# Polar-wandering spectral projections for symmetric moduli in von Neumann algebras

## Statement

Let \(M\) be a von Neumann algebra and let \(X_1,\ldots,X_m\in M\). Put
\[
X=\sum_{j=1}^m X_j,\qquad 
\mathsf S=\sum_{j=1}^m |X_j|_{\mathrm{sym}}
=\frac12\sum_{j=1}^m\bigl(|X_j|+|X_j^*|\bigr).
\]
Assume that \(X\) is invertible and write its polar decomposition as
\[
X=U|X|,\qquad a=\|X^{-1}\|^{-1}>0.
\]

Then the spectral projection
\[
E=\mathbf 1_{[0,a/2)}(\mathsf S)
\]
satisfies the **polar-wandering relation**
\[
\boxed{\,E\wedge U^*EU=0\,}.
\]

If \(M\) is finite and \(\operatorname{Tr}_Z:M\to Z(M)\) is the normalized center-valued trace, then
\[
\boxed{\ \operatorname{Tr}_Z(E)\le \frac12\,1\ }.
\]
Equivalently, by the comparison theorem for projections in a finite von Neumann algebra,
\[
E\precsim 1-E.
\]
Consequently every normal tracial state \(\tau\) on \(M\) obeys
\[
\tau\!\left(\mathbf 1_{[0,a/2)}(\mathsf S)\right)\le \frac12.
\]

There is a sharper polar-Hermitian form. If the polar unitary is a scalar multiple of a symmetry,
\[
U=\zeta V,\qquad |\zeta|=1,\qquad V=V^*=V^{-1},
\]
then for
\[
F=\mathbf 1_{[0,a)}(\mathsf S)
\]
one has
\[
\boxed{\,F\wedge VFV=0\,},
\qquad
\boxed{\ \operatorname{Tr}_Z(F)\le \frac12\,1\ }
\]
when \(M\) is finite.

Thus the median eigenvalue bounds for sums of symmetric moduli have a projection-theoretic form that remains meaningful in arbitrary von Neumann algebras and a center-valued form in finite ones.

## Proof

Set
\[
P=\sum_{j=1}^m |X_j^*|,
\qquad
Q=\sum_{j=1}^m |X_j|,
\qquad
\mathsf S=\frac{P+Q}{2}.
\]
For every \(j\),
\[
\begin{bmatrix}
|X_j^*| & X_j\\
X_j^* & |X_j|
\end{bmatrix}\ge0
\]
in \(M_2(M)\). Summing and conjugating by \(\operatorname{diag}(U^*,1)\) gives
\[
\begin{bmatrix}
U^*PU & |X|\\
|X| & Q
\end{bmatrix}\ge0.
\]
Evaluating the quadratic form on vectors of the form \((h,-h)\), or equivalently applying the positive map
\(
\begin{bmatrix}A&B\\B&C\end{bmatrix}\mapsto A+C-2B
\)
to this self-adjoint block, yields
\[
U^*PU+Q\ge 2|X|\ge 2a\,1. \tag{1}
\]

Let
\[
E=\mathbf 1_{[0,a)}(P+Q)
=\mathbf 1_{[0,a/2)}(\mathsf S).
\]
Suppose that \(E\wedge U^*EU\neq0\). In a faithful Hilbert-space representation choose a nonzero vector
\[
\xi\in \operatorname{Ran}(E)\cap\operatorname{Ran}(U^*EU).
\]
Then \(\xi\in\operatorname{Ran}(E)\) and \(U\xi\in\operatorname{Ran}(E)\). Since the spectral support of \(P+Q\) on \(E\) lies strictly below \(a\),
\[
\langle Q\xi,\xi\rangle
\le \langle(P+Q)\xi,\xi\rangle
<a\|\xi\|^2,
\]
and likewise
\[
\langle U^*PU\,\xi,\xi\rangle
=\langle P\,U\xi,U\xi\rangle
\le \langle(P+Q)U\xi,U\xi\rangle
<a\|\xi\|^2.
\]
Adding contradicts (1). Hence
\[
E\wedge U^*EU=0. \tag{2}
\]

Now suppose \(M\) is finite. Center-valued dimension is modular on projections:
\[
\operatorname{Tr}_Z(p\vee q)+\operatorname{Tr}_Z(p\wedge q)
=\operatorname{Tr}_Z(p)+\operatorname{Tr}_Z(q).
\]
Apply this to \(p=E\) and \(q=U^*EU\). They have the same center-valued trace, and by (2) their meet is zero. Therefore
\[
2\operatorname{Tr}_Z(E)
=\operatorname{Tr}_Z(E\vee U^*EU)
\le 1,
\]
which proves the center-valued half-dimension bound. Standard projection comparison in finite von Neumann algebras then gives \(E\precsim 1-E\). Composing the center-valued inequality with any normal tracial state gives the scalar trace statement.

For the polar-Hermitian improvement, write \(U=\zeta V\) with \(V=V^*=V^{-1}\). Inequality (1) becomes
\[
VPV+Q\ge 2|X|.
\]
Conjugating by \(V\) gives
\[
P+VQV\ge 2V|X|V=2|X^*|.
\]
Adding and dividing by two yields
\[
\mathsf S+V\mathsf S V
=\frac12(P+Q+VPV+VQV)
\ge |X|+|X^*|
\ge 2a\,1. \tag{3}
\]
If \(F=\mathbf 1_{[0,a)}(\mathsf S)\) had a nonzero intersection with \(VFV\), a nonzero vector \(\xi\) in that intersection would satisfy
\[
\langle \mathsf S\xi,\xi\rangle<a\|\xi\|^2,
\qquad
\langle V\mathsf S V\xi,\xi\rangle<a\|\xi\|^2,
\]
contradicting (3). Thus \(F\wedge VFV=0\), and the same center-valued dimension argument proves the improved finite-algebra estimate.

## Matrix consequences and sharpness

For \(M=M_d(\mathbb C)\), the normalized center-valued trace of a projection is its rank divided by \(d\). The general bound therefore says that at most half the dimensions can lie strictly below \(a/2\). When \(d\in\{2n-1,2n\}\), this is exactly
\[
\lambda_n(\mathsf S)\ge \frac a2.
\]
For \(a=1\), this recovers Theorem 3.1 of Aouichaoui--Lee (2026), but the projection-wandering statement and the center-valued finite-von-Neumann formulation are stronger structural versions.

The factor \(1/2\) is sharp already in \(M_3(\mathbb C)\). Proposition 3.2 of Aouichaoui--Lee constructs, for every \(0<\varepsilon<1\), two matrices with unitary sum and
\[
\mathsf S=
\operatorname{diag}\!\left(\frac{1+\varepsilon}{2},
\varepsilon^{-1},
\frac{1+\varepsilon}{2}\right)
\]
up to ordering. Hence any universal threshold \(c>1/2\) would make the spectral projection below \(c\) have normalized rank at least \(2/3\) for sufficiently small \(\varepsilon\), contradicting a half-dimension conclusion.

The polar-Hermitian threshold \(a\) is also best possible: taking one summand equal to the identity and the remaining summands zero gives \(a=1\) and \(\mathsf S=1\).

The symmetrization is essential. Aouichaoui--Lee Proposition 2.4 gives three matrices with sum \(I_3\) for which
\[
\sum_j |X_j|=\operatorname{diag}(b,\varepsilon,\varepsilon)
\]
with \(\varepsilon>0\) arbitrarily small. Therefore no positive universal threshold can give the analogous half-dimension statement for the one-sided sum \(\sum_j|X_j|\).

## Relation to prior literature

Bourin--Lee introduced and developed triangle/eigenvalue inequalities for the operator symmetric modulus. Their 2026 paper works with finite matrices and obtains, among other results, stronger first-half eigenvalue bounds when the sum is polar Hermitian. Aouichaoui--Lee then proved the sharp matrix median inequality
\[
\left|\sum_jX_j\right|\ge I
\quad\Longrightarrow\quad
\lambda_n\!\left(\sum_j|X_j|_{\mathrm{sym}}\right)\ge\frac12,
\qquad d\in\{2n-1,2n\},
\]
using block positivity and Weyl's eigenvalue inequality.

The result here replaces the Weyl-eigenvalue step by the projection identity
\[
E\wedge U^*EU=0,
\]
which needs no finite-dimensional ordering of eigenvalues. Finiteness enters only afterward, through center-valued dimension. This both explains the matrix median phenomenon and extends it to type II finite von Neumann algebras.

There is related literature extending matrix positive-block and singular-value inequalities to semifinite von Neumann algebras, including Nurahemet--Ospanov (2023) and earlier work on generalized singular numbers. Those results make such an extension a serious prior-art risk; the novelty claim here is specifically the polar-wandering spectral-projection formulation, its center-valued half-dimension consequence, and the unified polar-Hermitian strengthening.

## Originality and limitations

To the best of our knowledge, the polar-wandering relation and the center-valued median formulation above are not stated in the sources located. The underlying ingredients--positive \(2\times2\) operator blocks, polar decomposition, spectral projections, and center-valued dimension--are standard. Accordingly, the contribution is a structural synthesis and extension of a very recent matrix inequality, not a new foundational theorem about von Neumann algebras.

The result concerns bounded elements of von Neumann algebras. It does not claim an extension to arbitrary measurable unbounded operators, nor a full singular-value majorization theorem. In properly infinite von Neumann algebras the meet-zero statement still holds, but there is no normalized center-valued half-dimension conclusion of the form above.

## Sources

- Mohamed Amine Aouichaoui and Eun-Young Lee, *Solutions to some open problems in matrix analysis*, arXiv:2609.20094v1 (2026).
- Jean-Christophe Bourin and Eun-Young Lee, *Triangle inequalities for the operator symmetric modulus*, arXiv:2602.19607v1 (2026), Proc. Amer. Math. Soc., in press.
- Bahargul Nurahemet and Myrzagali N. Ospanov, *On 2x2 positive matrices of tau-measurable operators*, Operators and Matrices 17 (2023), DOI: 10.7153/oam-2023-17-45.
