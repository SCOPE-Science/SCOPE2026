# Infinitely many minimal evolution envelopes of the dual numbers

## Finding
Let \(A=\mathbb C[\varepsilon]/(\varepsilon^2)\). For every integer \(m\ge3\), there is a three-dimensional complex evolution algebra \(E_m\) with \(E_m^2\cong A\) as algebras; in particular, \(A\) is an ideal in \(E_m\). These algebras are pairwise nonisomorphic. No evolution algebra of dimension two contains \(A\) as an ideal. Thus the dual numbers possess infinitely many nonisomorphic evolution envelopes of the minimum possible dimension, which is three.

An explicit isomorphism invariant distinguishing these envelopes is
\[
\mathcal I(E_m)=\frac{2(3m+2)^2}{7m^2+6m+4}.
\]
It decreases strictly as the integer \(m\) runs through \(3,4,5,\ldots\). The invariant arises from the pencil of symmetric multiplication forms induced by the two coordinates on the characteristic ideal \(E_m^2\).

## Assumptions and scope
Work over the complex field. An evolution algebra is a commutative, not necessarily associative, algebra with a basis \(e_1,e_2,e_3\) such that \(e_ie_j=0\) whenever \(i\ne j\). Its square \(E^2\) is the linear span of all products, which is a characteristic ideal. An evolution envelope of \(A\) is an evolution algebra containing an ideal isomorphic to \(A\), and is dimension-minimal when its dimension is minimal among such algebras. Algebras and isomorphisms are complex-linear. The parameter \(m\) ranges over integers at least three, not arbitrary complex values for which some displayed denominators can vanish.

Set \(b_1=1\), \(b_2=2\), \(b_3=m\), and identify \(A\) with the two-dimensional subspace of a three-dimensional vector space with basis \(e_1,e_2,e_3\) by
\[
\iota_m(s+t\varepsilon)=(s+t)e_1+(s+2t)e_2+(s+mt)e_3.
\]
Define scalar pairs \((w_i,z_i)\), for \(i=1,2,3\), by
\[
\begin{aligned}
(w_1,z_1)&=\left(\frac{2m}{m-1},-\frac{m+2}{m-1}\right),\\
(w_2,z_2)&=\left(-\frac{m}{m-2},\frac{m+1}{m-2}\right),\\
(w_3,z_3)&=\left(\frac{2}{(m-1)(m-2)},-\frac{3}{(m-1)(m-2)}\right).
\end{aligned}
\]
Define \(E_m\) by \(e_i^2=\iota_m(w_i+z_i\varepsilon)\) and \(e_ie_j=0\) for \(i\ne j\).

## Proof
**1. The embedded dual-number product.** Let \(V\) be the Vandermonde matrix with rows \((1,1,1)\), \((b_1,b_2,b_3)\), and \((b_1^2,b_2^2,b_3^2)\). Its determinant is \((m-1)(m-2)\ne0\). Direct substitution of the displayed coefficients gives
\[
V(w_1,w_2,w_3)^\mathsf T=(1,0,0)^\mathsf T,\qquad
V(z_1,z_2,z_3)^\mathsf T=(0,1,0)^\mathsf T.
\]
For any \(s,t,u,v\in\mathbb C\), expand the product using the defining natural basis:
\[
\begin{aligned}
&\iota_m(s+t\varepsilon)\,\iota_m(u+v\varepsilon)\\
&\quad=\sum_{i=1}^3(s+b_it)(u+b_iv)\,\iota_m(w_i+z_i\varepsilon)\\
&\quad=\iota_m\bigl(su+(sv+tu)\varepsilon\bigr).
\end{aligned}
\]
This is precisely multiplication in \(A\), so \(\iota_m(A)\) is a subalgebra isomorphic to the dual numbers. The coefficient vectors \(w=(w_i)\) and \(z=(z_i)\) are linearly independent (their \(V\)-images are distinct basis vectors). Therefore \(e_1^2,e_2^2,e_3^2\) span \(\iota_m(A)\); equivalently \(E_m^2=\iota_m(A)\). Every \(E_m^2\) is an ideal, since products with arbitrary elements of \(E_m\) remain in the linear span of all products. In addition, all \(w_i\ne0\), so the constructed evolution algebras have zero annihilator.

**2. Minimal dimension.** If a two-dimensional evolution algebra contained \(A\) as an ideal, it would itself be isomorphic to \(A\). But \(A^2=A\) and \(\varepsilon^2=0\) with \(\varepsilon\ne0\). For a two-dimensional perfect evolution algebra the squares of the two natural-basis vectors are linearly independent, so the square of \(ae_1+be_2\) vanishes only if \(a^2=b^2=0\), hence only for the zero vector over \(\mathbb C\). Thus \(A\) cannot be an evolution algebra. Every envelope has dimension at least three; the displayed \(E_m\) attain this lower bound.

**3. An intrinsic pencil invariant.** Let \(E\) be one of these envelopes and write its characteristic ideal \(D=E^2\cong A\). Since \(D\) is the dual-number algebra, it has its own canonical identity \(1_D\), unique radical line \(\mathfrak r=\mathbb C\varepsilon_D\), and canonical residue homomorphism \(\pi:D\to\mathbb C\). Choose any nonzero generator \(\varepsilon_D\) of \(\mathfrak r\). Every \(a\in D\) has the unique form \(a=\pi(a)1_D+\eta(a)\varepsilon_D\). Define symmetric complex bilinear forms on \(E\) by
\[
B_0(x,y)=\pi(xy),\qquad B_1(x,y)=\eta(xy).
\]
If \(B_0\) is nondegenerate, there is a unique endomorphism \(T\) satisfying \(B_1(x,y)=B_0(Tx,y)\). Under any algebra isomorphism of envelopes the induced isomorphism on \(D\) carries \(1_D\) to \(1_{D'}\), preserves \(\pi\), and sends \(\varepsilon_D\) to a nonzero scalar multiple of \(\varepsilon_{D'}\). Thus \(B_0\) undergoes congruence and \(B_1\) undergoes the same congruence plus a nonzero scalar multiplication. Consequently \(T\) changes only by similarity and a nonzero overall scalar. Wherever \(\operatorname{tr}(T^2)\ne0\), the ratio
\[
\mathcal I(E)=\frac{\operatorname{tr}(T)^2}{\operatorname{tr}(T^2)}
\]
is therefore independent of choices and invariant under algebra isomorphisms.

**4. Explicit evaluation and separation.** In the natural basis of \(E_m\) the two forms have diagonal matrices \(\operatorname{diag}(w_1,w_2,w_3)\) and \(\operatorname{diag}(z_1,z_2,z_3)\). Because the \(w_i\) are nonzero, \(B_0\) is nondegenerate, and the eigenvalues of \(T\) are
\[
\frac{z_1}{w_1}=-\frac{m+2}{2m},\qquad
\frac{z_2}{w_2}=-\frac{m+1}{m},\qquad
\frac{z_3}{w_3}=-\frac32.
\]
Their squared sum is strictly positive for every integer \(m\ge3\). Direct simplification gives
\[
\mathcal I(E_m)=\frac{2(3m+2)^2}{7m^2+6m+4}.
\]
The rational function of a real variable \(x\) on the right has derivative
\[
-\frac{4(3x+2)(5x-6)}{(7x^2+6x+4)^2}<0\qquad (x\ge3).
\]
Hence \(\mathcal I(E_m)\) takes different values for distinct integers \(m\ge3\). The resulting minimal evolution envelopes are pairwise nonisomorphic. This completes the proof.

## Verification
The standalone exact-arithmetic program `VERIFY_EXACT.py` solves the three Vandermonde equations with rational fractions for every integer parameter \(3\le m\le23\), directly checks all pairwise products of 625 selected dual-number inputs, and compares the intrinsic invariant against its closed formula. The independent symbolic checker `VERIFY_SYMBOLIC.py` uses exact symbolic inversion, derives the three eigenvalues, simplifies the invariant and verifies its derivative. The recorded outputs in `VERIFY_EXACT.out` and `VERIFY_SYMBOLIC.out` end in `VERIFY_OK`. Reproduce using standard Python 3 with `sympy` installed by running each file directly. The unbounded-parameter conclusion is established by the preceding symbolic proof, not by this finite test range.

## Relationship to prior work
Costoya, Fernández Ouaridi and Viruel (2026, arXiv:2609.32784, first public 2026-09-26) prove general finite-dimensional commutative-algebra embedding theorems and relate minimum evolution-envelope dimension to simultaneous Waring rank; their general results, including the existence and minimum dimension of envelopes for truncated polynomial algebras, are prior work and not claimed here. Kaygorodov, Martín González and Viruel (2026, arXiv:2610.22248, Question 42, page 26) explicitly ask which commutative algebras have a unique minimum evolution envelope. The present finding establishes an infinite family of different *minimal envelopes of one fixed algebra*, together with an explicit intrinsic moduli-separating invariant. No general construction or all-field envelope theorem is claimed as new.

## Limitations
The classification of **all** minimum envelopes of \(A\) is not attempted: the finding proves the existence of infinitely many distinct isomorphism classes. It is over \(\mathbb C\) only. The invariant is defined only where the canonical residue multiplication form is nondegenerate and its associated endomorphism has nonzero squared trace. Existing general existence/minimum-dimension results are acknowledged. The full text of arXiv:2609.32784 was not accessible during the literature comparison, so an implicit or explicit prior instance of the infinite family cannot be wholly excluded; the full text of the survey's Question 42 was examined.

## References
1. C. Costoya, A. Fernández Ouaridi and A. Viruel, *Commutative algebras are ideals of evolution algebras*, arXiv:2609.32784 (first submitted 2026-09-26), https://arxiv.org/abs/2609.32784.
2. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (2026-10-15), particularly Question 42, p. 26, https://arxiv.org/abs/2610.22248.
