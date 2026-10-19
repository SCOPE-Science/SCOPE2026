# Sharp three-mode Gaussian square-coercivity constant

## Finding

Let \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\) be Gaussian probability measure on \(\mathbb C\). For every complex polynomial \(F(z)=a+bz+cz^2\) of degree at most two, let \(\|H\|_{\mathcal F^2}=\bigl(\int|H|^2\,d\gamma\bigr)^{1/2}\). Then the optimal constant in
\[
\|F^2-F(0)^2\|_{\mathcal F^2}\le C_2\inf_{t\in\mathbb R}\||F|^2-t\|_{L^2(\gamma)}
\]
is \(C_2=\sqrt{\mathcal R_*}=1.5633577120464347105\ldots\), with \(\mathcal R_*=2.4440873358150630698\ldots\).

The constant is specified exactly. Let \(q_*\) be the unique positive root of
\[
96q^3+96q^2+6q-1=0,
\]
and define
\[
y_*=\sqrt{q_*},\qquad x_*=2y_*(1+y_*^2)+\sqrt{4y_*^2(1+y_*^2)^2+y_*^2+\tfrac12}.
\]
With
\[
\begin{aligned}
N(x,y)&=(4+8y^2)x^2-8xy+2+24y^2+24y^4,\\
D(x,y)&=(2+4y^2)x^2-8xy+1+20y^2+20y^4,
\end{aligned}
\]
the exact squared constant is \(\mathcal R_*=N(x_*,y_*)/D(x_*,y_*)\). Numerically \(x_*=1.53802969380230015\ldots\) and \(y_*=0.27130150591501412\ldots\).

Equality for a nonconstant polynomial holds exactly for
\[
F(z)=\lambda\bigl(x_*+e^{i\theta}z-y_*e^{2i\theta}z^2\bigr),
\qquad\lambda\in\mathbb C\setminus\{0\},\quad\theta\in\mathbb R.
\]
Constant polynomials give equality trivially because both sides vanish. In contrast, on the affine subspace \(\operatorname{span}\{1,z\}\), the squared optimal constant is exactly \(2\). Thus adding the first non-affine Hermite/Fock mode strictly increases the optimal squared amplification factor.

## Assumptions and scope

The inequality is the square-coercivity inequality for Gaussian measurements restricted to the first three Fock monomial modes; \(F^2\) is an entire polynomial and hence belongs to \(\mathcal F^2\). The minimizing real \(t\) equals \(\int|F|^2\,d\gamma\). No normalization of \(F\) or positivity of its coefficients is assumed. Its constant concerns the centered square \(F^2-F(0)^2\), not the phase-orbit distance of \(F\), and not arbitrary entire functions or polyanalytic Fock spaces.

## Proof

**Gaussian moments.** For all nonnegative integers \(j,k\), orthogonality gives \(\int z^j\overline z^{\,k}\,d\gamma=\delta_{jk}j!\). Consequently, for \(F=a+bz+cz^2\),
\[
E_2:=\int|F|^2\,d\gamma=|a|^2+|b|^2+2|c|^2,
\]
and expanding the coefficients of \(F^2=a^2+2abz+(b^2+2ac)z^2+2bcz^3+c^2z^4\) gives
\[
E_4:=\int|F|^4\,d\gamma
=|a|^4+4|ab|^2+2|b|^4+8|ac|^2
+8\operatorname{Re}(b^2\overline{ac})+24|bc|^2+24|c|^4.
\]
The squared numerator is \(E_4-|a|^4\), and the minimized squared denominator is \(E_4-E_2^2\). For nonconstant \(F\), the denominator is strictly positive, since an entire function with constant modulus must be constant. Set \(\mathcal R(F)=(E_4-|a|^4)/(E_4-E_2^2)\).

**Relative phase and boundary cases.** At fixed coefficient magnitudes, \(E_2\) and \(|a|\) are fixed, while \(E_4\) depends on phases only through \(8\operatorname{Re}(b^2\overline{ac})\). The derivative of \((E_4-|a|^4)/(E_4-E_2^2)\) with respect to \(E_4\) is \((|a|^4-E_2^2)/(E_4-E_2^2)^2<0\). Thus the optimal phase is the negative interference \(b^2\overline{ac}=-|a||b|^2|c|\) whenever all three coefficients are nonzero. Multiplication of \(F\) by a nonzero scalar and rotation of its argument preserve \(\mathcal R\), so every potentially superior case can be represented by \(F(z)=x+z-yz^2\) with \(x,y>0\). If \(c=0\) and \(b\ne0\), the ratio is exactly \(2\). If \(a=0\) or \(b=0\), the moment formula gives a ratio at most \(2\). In particular, any global ratio strictly greater than \(2\) must have \(x,y>0\) and negative interference.

**Exact two-variable optimization.** For \(F=x+z-yz^2\), the quotient is \(\mathcal R(x,y)=N(x,y)/D(x,y)\), using the polynomials in the finding. Note that
\[
N(x,y)-2D(x,y)=8y\,[x-2y(1+y^2)].
\]
A direct differentiation gives
\[
\frac{\partial\mathcal R}{\partial x}
=-\frac{8y(2y^2+1)}{D(x,y)^2}\,Q(x,y),
\qquad
Q(x,y)=2x^2-8xy(1+y^2)-2y^2-1.
\]
For each \(y>0\), the polynomial \(Q(\cdot,y)\) has exactly one positive zero, namely
\[
x_y=2y(1+y^2)+\sqrt{4y^2(1+y^2)^2+y^2+\tfrac12}.
\]
Hence \(x\mapsto\mathcal R(x,y)\) strictly increases up to \(x_y\) and strictly decreases afterward. Also \(x_y>2y(1+y^2)\), so \(\mathcal R(x_y,y)>2\). The continuous profile \(\mathcal R(x_y,y)\) tends to \(2\) both as \(y\downarrow0\) and as \(y\to\infty\), the latter using \(x_y=4y^3+4y+O(y^{-1})\). It therefore has an interior global maximum.

For its second stationary equation, differentiation gives
\[
\frac{\partial\mathcal R}{\partial y}=-\frac{8H(x,y)}{D(x,y)^2},
\]
where
\[
\begin{aligned}
H(x,y)={}&4x^3y^2-2x^3+16x^2y^5+16x^2y^3+8x^2y\\
&+12xy^4+4xy^2-x+8y^3+4y.
\end{aligned}
\]
Eliminating \(x\) from \(Q(x,y)=H(x,y)=0\) yields the exact polynomial identity
\[
\operatorname{Res}_x(Q,H)=16(2y^2+1)
(8y^6+16y^4+10y^2+1)
(96y^6+96y^4+6y^2-1).
\]
The first two factors are positive for \(y>0\). The remaining factor has exactly one positive zero, since \(96q^3+96q^2+6q-1\) is strictly increasing on \([0,\infty)\), negative at zero and positive at one. Therefore every positive stationary point of the optimal profile must have \(y=y_*\). An interior maximizer exists, so it must be \((x_*,y_*)\), and this maximizer is unique. All boundary cases have ratio at most \(2<\mathcal R_*\), establishing both sharpness and the full equality classification. The resultant is an elementary finite polynomial identity and can be verified by expansion; its verification is reproduced in the standalone checker.

## Verification

The file `checker.py` independently expands the Gaussian fourth moment by radial-angular quadrature, verifies the two exact derivative identities and the resultant using polynomial arithmetic, checks 250 randomly chosen complex quadratic coefficients, and verifies nine rotated/scaled equality configurations. The analytic proof establishes the global statement; the finite trials are supplementary. Run it with `python checker.py` using NumPy and SymPy.

## Relationship to prior work

Bortolotto and Ramos (first posted August 26, 2026) prove that a universal, unspecified constant controls the same centered square by the Gaussian \(L^2\) fluctuation of \(|F|^2\) for every polynomial and a class of entire functions. Their theorem does not give the best constant on the three-mode subspace. The present finite-dimensional sharp result is compatible with that infinite-dimensional theorem and yields a rigorous lower bound \(C\ge C_2\) for any universal constant in it. Bertolini, de Dios Pont, Pineau, Ramos and Taylor (May 19, 2026) treat a related but different modulus phase-retrieval stability inequality and an orthogonal coercivity estimate, not this centered-square ratio. No claim of solving the infinite-dimensional best-constant problem is made.

## Limitations

This is a sharp **three-mode restriction**, not the optimal constant over all polynomials or entire Fock functions. The coefficient-phase and uniqueness proof depends on the degree-two expansion. It does not establish robustness for sampled measurements, other Gaussian weights, higher dimensions, or other phase-retrieval metrics. Historical priority outside the identified literature remains subject to independent verification.

## References

1. C. Bortolotto and J. P. G. Ramos, *A complex-analytic proof of square-restricted stable phase retrieval in Fock space*, arXiv:2608.26365 (initial version posted 2026-08-26), https://arxiv.org/abs/2608.26365.
2. S. Bertolini, J. de Dios Pont, B. Pineau, J. P. G. Ramos and M. A. Taylor, *L²-Stability for STFT phase retrieval*, arXiv:2605.20527 (initial version posted 2026-05-19), https://arxiv.org/abs/2605.20527.
3. K. Zhu, *Analysis on Fock Spaces*, Springer, 2012 (standard Gaussian Fock monomial normalization).
