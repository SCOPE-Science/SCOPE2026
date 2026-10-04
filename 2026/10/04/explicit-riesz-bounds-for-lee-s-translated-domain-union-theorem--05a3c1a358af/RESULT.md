# Explicit Riesz bounds for Lee's translated-domain union theorem
## Finding
Let \(d\ge 1\), let \(S_1,S_2\subset\mathbb R^d\) be disjoint bounded measurable sets, and let \(a\in\mathbb R^d\setminus\{0\}\) satisfy \(S_1+a\subset S_2\). Define
\[
\Gamma_a=\{\xi\in\mathbb R^d:a\cdot\xi\in\mathbb Z\}.
\]
Assume \(\Lambda_1\subset\mathbb R^d\setminus\Gamma_a\), \(\Lambda_2\subset\Gamma_a\), and \(\operatorname{dist}(\Lambda_1,\Gamma_a)>0\). Suppose \(E(\Lambda_\ell)\) is a Riesz basis for \(L^2(S_\ell)\) with lower and upper Riesz bounds \(A_\ell,B_\ell\), for \(\ell=1,2\).

Set
\[
m=\inf_{\lambda\in\Lambda_1}\left|1-e^{2\pi i a\cdot\lambda}\right|>0,
\]
and let \(C_{12}\) be any Bessel bound of \(E(\Lambda_1)\) on \(L^2(S_2)\), meaning that every finitely supported coefficient family satisfies
\[
\left\|\sum_{\lambda\in\Lambda_1}c_\lambda e^{2\pi i\lambda\cdot x}\right\|_{L^2(S_2)}^2
\le C_{12}\sum_{\lambda\in\Lambda_1}|c_\lambda|^2.
\]
Then \(E(\Lambda_1\cup\Lambda_2)\) is a Riesz basis for \(L^2(S_1\cup S_2)\) with the explicit valid bounds
\[
L=\frac{A_1A_2m^2}{2\bigl(A_2+A_1m^2+2C_{12}\bigr)},
\qquad
U=B_1+C_{12}+2B_2.
\]
The constants are a priori bounds and are not asserted to be optimal.

## Assumptions and scope
The exponential system is \(E(\Lambda)=\{e^{2\pi i\lambda\cdot x}:\lambda\in\Lambda\}\). The hypotheses are those of the translated-domain union theorem in Dae Gwan Lee's paper, together with names for the input Riesz bounds and a cross-domain Bessel bound. Under those hypotheses \(C_{12}<\infty\): the frequency set \(\Lambda_1\) is separated and exponentials over a separated set are Bessel on every bounded domain. The proof below only needs the displayed Bessel inequality itself.

The positive phase gap \(m\) is forced by \(\operatorname{dist}(\Lambda_1,\Gamma_a)>0\). The result applies in every finite dimension and specializes to Lee's one-dimensional Theorem 1.

## Proof
Write, for finitely supported coefficient families,
\[
p_1(x)=\sum_{\lambda\in\Lambda_1}c_\lambda e^{2\pi i\lambda\cdot x},\qquad
p_2(x)=\sum_{\lambda\in\Lambda_2}c_\lambda e^{2\pi i\lambda\cdot x},\qquad q=p_1+p_2.
\]
Because \(a\cdot\lambda\in\mathbb Z\) for \(\lambda\in\Lambda_2\), one has \(p_2(x+a)=p_2(x)\). Since \(S_1+a\subset S_2\) and \(S_1\cap S_2\) is null,
\[
\begin{aligned}
2\|q\|_{L^2(S_1\cup S_2)}^2
&\ge \int_{S_1}|q(x+a)-q(x)|^2\,dx\\
&=\left\|\sum_{\lambda\in\Lambda_1}\bigl(e^{2\pi i a\cdot\lambda}-1\bigr)c_\lambda e^{2\pi i\lambda\cdot x}\right\|_{L^2(S_1)}^2\\
&\ge A_1m^2\sum_{\lambda\in\Lambda_1}|c_\lambda|^2.
\end{aligned}
\]
Thus
\[
\sum_{\lambda\in\Lambda_1}|c_\lambda|^2
\le \frac{2}{A_1m^2}\|q\|_{L^2(S_1\cup S_2)}^2.
\]
On \(S_2\), \(p_2=q-p_1\), so
\[
A_2\sum_{\lambda\in\Lambda_2}|c_\lambda|^2
\le \|p_2\|_{L^2(S_2)}^2
\le 2\|q\|_{L^2(S_1\cup S_2)}^2+2C_{12}\sum_{\lambda\in\Lambda_1}|c_\lambda|^2.
\]
Substitution of the preceding estimate gives
\[
\sum_{\lambda\in\Lambda_1\cup\Lambda_2}|c_\lambda|^2
\le
\frac{2\bigl(A_2+A_1m^2+2C_{12}\bigr)}{A_1A_2m^2}
\|q\|_{L^2(S_1\cup S_2)}^2,
\]
which is the claimed lower Riesz bound.

For the upper bound,
\[
\|p_1\|_{L^2(S_1\cup S_2)}^2\le(B_1+C_{12})\sum_{\lambda\in\Lambda_1}|c_\lambda|^2.
\]
Periodicity by \(a\) also gives
\[
\|p_2\|_{L^2(S_1)}^2
=\|p_2\|_{L^2(S_1+a)}^2
\le\|p_2\|_{L^2(S_2)}^2,
\]
so
\[
\|p_2\|_{L^2(S_1\cup S_2)}^2\le2B_2\sum_{\lambda\in\Lambda_2}|c_\lambda|^2.
\]
The triangle inequality followed by Cauchy--Schwarz therefore yields
\[
\|q\|_{L^2(S_1\cup S_2)}^2
\le\bigl(B_1+C_{12}+2B_2\bigr)
\sum_{\lambda\in\Lambda_1\cup\Lambda_2}|c_\lambda|^2.
\]

For completeness, let \(f=f_1+f_2\in L^2(S_1\cup S_2)\), with \(f_\ell\) supported on \(S_\ell\), be orthogonal to \(E(\Lambda_1\cup\Lambda_2)\). Transfer \(f_1\) to \(S_1+a\) and define on \(S_2\)
\[
g(y)=f_2(y)+f_1(y-a)\mathbf 1_{S_1+a}(y).
\]
For \(\lambda\in\Lambda_2\), the translation phase is one, hence the Fourier coefficient of \(g\) at \(\lambda\) equals that of \(f\) and vanishes. Completeness of \(E(\Lambda_2)\) gives \(g=0\). It follows that the Fourier coefficients of \(f\) at \(\lambda\in\Lambda_1\) equal
\[
\bigl(1-e^{-2\pi i a\cdot\lambda}\bigr)\widehat f_1(\lambda).
\]
The factor never vanishes on \(\Lambda_1\), so completeness of \(E(\Lambda_1)\) gives \(f_1=0\), and then \(f_2=0\). Hence the Riesz sequence is complete and is a Riesz basis.

## Verification
Every inequality above is dimension-independent and uses only the two input Riesz inequalities, one cross-domain Bessel inequality, the identity \(p_2(x+a)=p_2(x)\), and the inclusion \(S_1+a\subset S_2\). The lower-bound denominator is obtained by adding the independently derived coefficient estimates; no finite experiment is used. The proof also reconstructs completeness directly rather than assuming it from the source theorem.

Boundary behavior is explicit: if the phase gap \(m\) tends to zero, the certified lower bound tends to zero, as expected near the forbidden hyperplane lattice. No optimality claim is made for either displayed bound.

## Relationship to prior work
Lee's Theorem 4 proves the qualitative union theorem in \(\mathbb R^d\), with Theorem 1 as its one-dimensional special case. The paper explicitly notes that practical applications require frame/Riesz constants, says its proofs do not readily provide a straightforward method for determining them, and leaves estimation of those constants for future investigation. The present finding supplies such constants for the translated-domain theorem by a direct two-region difference estimate.

Asipchuk and Drezels study explicit exponential bases and stability on unions of intervals, while later planar-domain work of Asipchuk and De Carli develops frame-bound estimates for rectangle constructions. Those constructions address different geometric mechanisms and do not, in the material inspected, supply the displayed quantitative bound for Lee's translated-domain union theorem.

## Limitations
The bounds depend on the cross-domain Bessel constant \(C_{12}\), so a numerical application still requires an estimate of that standard quantity. The formulas are sufficient bounds, not best constants. The finding treats Lee's translated-domain theorem (Theorem 4 and hence Theorem 1); it does not claim quantitative bounds for the more elaborate multi-coset union theorems in the same paper.

## References
1. D. G. Lee, *Unions of exponential Riesz bases*, arXiv:2208.12205, first posted 2022-08-25; AIMS Mathematics 9 (2024), 23890--23908, doi:10.3934/math.20241161.
2. O. Asipchuk and V. Drezels, *Examples of exponential bases on union of intervals*, Canadian Mathematical Bulletin 66 (2023), 1296--1312, doi:10.4153/S0008439523000371.
3. O. Asipchuk and L. De Carli, *Methods of Construction of Exponential Bases on Planar Domains*, Bulletin of the Malaysian Mathematical Sciences Society (2026), doi:10.1007/s40840-026-02112-7.
