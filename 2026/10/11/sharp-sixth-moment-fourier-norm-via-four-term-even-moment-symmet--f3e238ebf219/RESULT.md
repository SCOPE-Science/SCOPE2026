# Sharp sixth-moment Fourier norm via four-term even-moment symmetrization

## Finding

Let \(\mathbb T=\mathbb R/\mathbb Z\) carry probability Haar measure and define
\[
P_c(t)=c_0+c_1e^{2\pi it}+c_2e^{4\pi it}+c_3e^{6\pi it},\qquad c\in\mathbb C^4.
\]
There is a unique positive root \(\rho\) of
\[
\rho^5+4\rho^4+\rho^3-6\rho-4=0,
\qquad \rho=1.16174797736568\ldots.
\]
The sharp sixth-moment inequality is
\[
\boxed{\ \|P_c\|_{L^6(\mathbb T)}^6\leq
\frac{5(\rho^6+3\rho^5+9\rho^4+6\rho^3+9\rho^2+1)}{2(1+\rho^2)^3}
\left(\sum_{j=0}^{3}|c_j|^2\right)^3\ }.
\]
The optimal sixth-power constant is \(9.20352638278473\ldots\), and the corresponding norm constant is \(1.44763489647014\ldots\). Every nonzero equality case, and no other, has coefficient vector
\[
\boxed{\quad c=\lambda(1,\rho e^{i\beta},\rho e^{2i\beta},e^{3i\beta}),
\quad \lambda\in\mathbb C\setminus\{0\},\ \beta\in\mathbb R.\quad}
\]

The proof also supplies an exact **even-moment symmetrization principle**: for every integer \(s\geq2\), put
\[
A=\sqrt{\frac{|c_0|^2+|c_3|^2}{2}},\qquad
B=\sqrt{\frac{|c_1|^2+|c_2|^2}{2}}.
\]
Then
\[
\int_{\mathbb T}|P_c(t)|^{2s}\,dt\leq
\int_{\mathbb T}|A+B e^{2\pi it}+B e^{4\pi it}+A e^{6\pi it}|^{2s}\,dt.
\]
The two coefficient vectors have identical Euclidean norm. Thus every even-moment norm optimization on these four consecutive frequencies reduces globally to one nonnegative coefficient ratio, not merely to an assumed symmetric ansatz.

## Assumptions and scope

The Fourier frequencies are the four distinct integers \(0,1,2,3\), with no cyclic wraparound, on the continuous circle with normalized Haar measure. The coefficient vector is arbitrary complex and may initially contain zeros. Norms are unweighted, the input norm is \((\sum|c_j|^2)^{1/2}\), and no statement about non-even exponents, other supports, or discrete sampling grids is asserted. The symmetrization inequality holds for every integer \(s\geq2\); the algebraic sharp norm and complete equality classification are established for \(s=3\).

## Proof

**1. Even-exponent coefficient majorant.** For integer \(s\geq2\), Fourier orthogonality gives
\[
\int_{\mathbb T}|P_c|^{2s}
=\sum_{n=0}^{3s}\left|\sum_{j_1+\cdots+j_s=n}c_{j_1}\cdots c_{j_s}\right|^2.
\]
The triangle inequality therefore permits replacement of all \(c_j\) by the nonnegative numbers \(a,b,c,d\), respectively, without reducing the integral. This is the standard even-exponent majorant step; it is not the new sharp-constant calculation.

**2. An autocorrelation monotonicity lemma.** For \(Q(z)=a+bz+cz^2+dz^3\) with nonnegative coefficients, define its nonnegative autocorrelations
\[
R_0=a^2+b^2+c^2+d^2,\quad R_1=ab+bc+cd,\quad
R_2=ac+bd,\quad R_3=ad.
\]
For every integer \(s\ge2\), the integral \(\int|Q|^{2s}\) is the constant Laurent coefficient in
\[
\left(R_0+R_1(z+z^{-1})+R_2(z^2+z^{-2})+R_3(z^3+z^{-3})\right)^s.
\]
As a polynomial in \(R_0,R_1,R_2,R_3\), this constant coefficient has nonnegative integer coefficients. In particular it is coordinatewise nondecreasing in the nonnegative autocorrelations.

Set \(A=\sqrt{(a^2+d^2)/2}\), \(B=\sqrt{(b^2+c^2)/2}\). The symmetric sequence \((A,B,B,A)\) has autocorrelations
\[
R_0'=R_0,\qquad R_1'=2AB+B^2,\qquad
R_2'=2AB,\qquad R_3'=A^2.
\]
Cauchy--Schwarz and the arithmetic--geometric mean yield
\[
ab+cd\le2AB,\quad ac+bd\le2AB,\quad bc\le B^2,\quad ad\le A^2.
\]
Thus \(R_j'\ge R_j\) for all \(j\), proving the stated global symmetrization inequality.

**3. Exact sixth-moment polynomial and optimization.** For \(s=3\), constant-coefficient extraction gives exactly
\[
\int|Q|^6=R_0^3+6R_0(R_1^2+R_2^2+R_3^2)+6R_1^2R_2+12R_1R_2R_3.
\]
The maximizer after the preceding symmetrization cannot have \(A=0\) or \(B=0\), because both boundary ratios yield sixth-power quotient \(5/2\), whereas the trial ratio \(B/A=1\) yields \(145/16>5/2\). Write \(t=B/A>0\); after dividing by the cube of the coefficient \(\ell^2\)-norm, direct coefficient convolution gives
\[
F(t)=\frac{5(t^6+3t^5+9t^4+6t^3+9t^2+1)}{2(1+t^2)^3},
\]
with derivative
\[
F'(t)=-\frac{15t(t^5+4t^4+t^3-6t-4)}{2(1+t^2)^4}.
\]
The quintic in parentheses is negative at zero and positive for sufficiently large \(t\). Its nonzero coefficient signs contain exactly one change, so Descartes' rule of signs proves that it has exactly one positive root \(\rho\). Thus \(F\) increases for \(0<t<\rho\) and decreases for \(t>\rho\). The displayed sharp constant follows.

**4. Equality without a symmetry assumption.** At \(\rho\), all four symmetric coefficients are strictly positive. The cubic autocorrelation expression is strictly increasing in \(R_1,R_2,R_3\) when those quantities are positive and \(R_0>0\). Equality in the symmetrization consequently forces \(ad=A^2\), hence \(a=d=A\), and then equality in \(ac+bd\le2AB\) forces \(b=c=B\). No asymmetric magnitude optimizer exists.

For the complex coefficient-majorant inequality to be sharp, the two groups of triples contributing to the coefficient of \(z^2\) in \(P_c(z)^3\) must have the same argument; this says \(\arg c_0+\arg c_2\equiv2\arg c_1\) modulo \(2\pi\). The three groups at \(z^3\) must likewise align; together these conditions say \(\arg c_j\equiv\alpha+j\beta\) for every \(j=0,1,2,3\). Conversely affine coefficient phases make every convolution coefficient sum phase-aligned, while \(B/A=\rho\) saturates the amplitude bound. This proves the complete classification.

## Verification

The accompanying self-contained `artifacts/verify.py` uses only Python's standard library. It independently enumerates the integer coefficient-convolution polynomial, checks the Laurent autocorrelation identity for exact rational data, verifies the derivative polynomial coefficient-by-coefficient, and tests the symmetrization inequalities on exact rational inputs. It separately compares analytic sixth moments against finite Fourier-grid quadrature, and reproduces the maximizing and nonmaximizing examples. The finite computations are consistency checks only; the universal statements are proved by the algebraic steps above.

## Relationship to prior work

Mockenhaupt and Schlag (arXiv:math/0207226v1, 2002) explain the even-exponent Hardy--Littlewood majorant principle and analyze majorant estimates for random spectra and arithmetic progressions. Krenedits (arXiv:1006.0409, first posted 2010) examines idempotent majorant counterexamples at non-even exponents, including the role of four-term examples. Neither primary statement supplies the sharp weighted \(L^2\)-to-\(L^6\) constant for the fixed four-frequency interval or its entire extremizer set. Existing three-frequency sixth-moment and four-frequency fourth-moment computations solve different optimization problems: neither implies the quintic critical ratio here. The connection to general even-moment majorization is used explicitly rather than presented as new.

## Limitations

This result applies only to the four consecutive frequencies on the continuous circle, with its exact coefficient normalization. The root description is algebraically exact; its printed decimals are approximations. The all-even-moment symmetrization is not a closed sharp-constant formula for arbitrary exponents. The literature comparison does not certify absolute priority, especially against older low-degree Nikolskii tables or polynomial tensor-eigenvalue calculations not discovered in the searches. The statements have not been compared exhaustively with unindexed print tables.

## References

- G. Mockenhaupt and W. Schlag, *On the Hardy--Littlewood majorant problem for random sets*, arXiv:math/0207226v1 (first posted 2002-07-25), https://arxiv.org/abs/math/0207226 .
- S. Krenedits, *Three-term idempotent counterexamples in the Hardy--Littlewood majorant problem*, arXiv:1006.0409 (first posted 2010-06-02), https://arxiv.org/abs/1006.0409 .
