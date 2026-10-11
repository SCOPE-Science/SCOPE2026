# Exact Sidon constant of the \(2\times2\) frequency rectangle
## Finding
Let \(\Lambda=\{(0,0),(1,0),(0,1),(1,1)\}\subset\mathbb Z^2\). For a trigonometric polynomial
\[
P(z,w)=a+bz+cw+dzw,\qquad |z|=|w|=1,
\]
define its coefficient mass by \(\|P\|_{\ell^1}=|a|+|b|+|c|+|d|\). Then the sharp inequality is
\[
\|P\|_{\ell^1}\le \sqrt2\,\|P\|_{L^\infty(\mathbb T^2)},
\]
and the constant \(\sqrt2\) cannot be improved. Equivalently, the Sidon constant of \(\Lambda\) is exactly \(\sqrt2\).

Sharpness is attained by
\[
P_*(z,w)=1+z+w-zw.
\]
Indeed, for fixed \(z\), maximizing over \(w\) gives \(|1+z|+|1-z|\), whose maximum is \(2\sqrt2\); the coefficient mass is \(4\).

## Assumptions and scope
The ambient compact group is the two-torus \(\mathbb T^2\), with characters \(z^jw^k\). The claim concerns arbitrary complex coefficients \(a,b,c,d\). No classification of all equality cases is asserted.

The Sidon constant is taken in the standard Fourier-analytic sense: coefficient \(\ell^1\)-mass divided by the supremum norm of the associated trigonometric polynomial.

## Proof
Multiplying \(P\) by a unimodular scalar and rotating the variables \(z\) and \(w\) do not change either the coefficient mass or the torus supremum norm. When three reference coefficients are nonzero, these phase freedoms reduce the polynomial to
\[
Q(z,w)=A+Bz+Cw+D e^{i\phi}zw,
\]
with \(A,B,C,D\ge0\). The cases with zero coefficients follow by continuity.

For fixed \(z\), maximizing over \(w\) is exact:
\[
\sup_{|w|=1}|Q(z,w)|=|A+Bz|+|C+D e^{i\phi}z|=:F(z).
\]
Put \(\alpha=\phi/2\) and evaluate at the two antipodal points \(z_\pm=\pm e^{-i\alpha}\). Write
\[
X_\pm=|A\pm B e^{-i\alpha}|,\qquad
Y_\pm=|C\pm D e^{i\alpha}|.
\]
Then \(F(z_\pm)=X_\pm+Y_\pm\), while
\[
X_+^2+X_-^2=2(A^2+B^2),\qquad
Y_+^2+Y_-^2=2(C^2+D^2).
\]
Moreover the triangle inequality gives
\[
\begin{aligned}
X_+Y_+ + X_-Y_-
&= |(A+B e^{-i\alpha})(C+D e^{i\alpha})|\\
&\quad+|(A-B e^{-i\alpha})(C-D e^{i\alpha})|\\
&\ge 2(AC+BD),
\end{aligned}
\]
because the sum of the two complex products inside the last triangle inequality is exactly \(2(AC+BD)\).

Consequently,
\[
F(z_+)^2+F(z_-)^2
\ge 2(A^2+B^2+C^2+D^2)+4(AC+BD).
\]
The right-hand side has the exact decomposition
\[
(A+B+C+D)^2+(A-B+C-D)^2,
\]
so it is at least \((A+B+C+D)^2\). Hence
\[
\|Q\|_\infty
\ge \max\{F(z_+),F(z_-)\}
\ge \frac{A+B+C+D}{\sqrt2}.
\]
Undoing the phase normalization proves
\[
|a|+|b|+|c|+|d|\le\sqrt2\,\|P\|_\infty.
\]
For \(P_*(z,w)=1+z+w-zw\),
\[
\|P_*\|_\infty
=\max_{|z|=1}\bigl(|1+z|+|1-z|\bigr)
=2\sqrt2,
\]
where the upper bound follows from Cauchy--Schwarz and \(|1+z|^2+|1-z|^2=4\), and equality occurs at \(z=i\). Therefore the ratio is \(4/(2\sqrt2)=\sqrt2\), completing the proof.

## Verification
The proof is symbolic and covers all complex coefficients. The accompanying `artifacts/verify.py` independently checks the two-sample inequality on deterministic pseudorandom coefficient/phase data and checks the sharp Hadamard witness numerically. These computations are corroborative only; no finite experiment is used to infer the universal inequality.

## Relationship to prior work
Neuwirth's 2001 paper defines the same Fourier-analytic Sidon constant and determines it for every three-element subset of the integers, with primary MSC 42A05. It does not give a four-character two-variable rectangle formula. The later work of Cavalcante and Pellegrino studies the same four coefficient slots as bilinear forms on \(\ell_\infty^2\times\ell_\infty^2\), but optimizes Littlewood's \(4/3\) coefficient functional rather than coefficient \(\ell^1\)-mass, so its stated results do not imply this sharp Sidon inequality. General homogeneous-polynomial Sidon estimates of Ortega-Cerdà, Ounaïes, and Seip concern asymptotic index sets rather than this exact four-term constant.

A 2026 paper of Neuwirth explicitly reports that the one-variable four-frequency problem \(\{0,1,2,3\}\) still has unknown exact Sidon constant. The present rectangle calculation is a different two-variable geometry: the product structure permits an exact two-point phase certificate.

## Limitations
The result is only for the rectangular support \(\Lambda\) on \(\mathbb T^2\). It does not determine the Sidon constant of arbitrary four-character sets, does not settle the one-variable set \(\{0,1,2,3\}\), and does not classify every equality case. A residual literature risk remains that the same \(2\times2\) coefficient-\ell^1 inequality appears in older bilinear-form or unconditional-basis terminology not surfaced by the searches described in the review.

## References
1. S. Neuwirth, *The Sidon constant of sets with three elements*, arXiv:math/0102145v1, first public version 2001-02-19.
2. W. Cavalcante and D. Pellegrino, *Geometry of the closed unit ball of the space of bilinear forms on \(\ell_\infty^2\)*, arXiv:1603.01535v1, first public version 2016-03-04.
3. J. Ortega-Cerdà, M. Ounaïes, and K. Seip, *The Sidon constant for homogeneous polynomials*, arXiv:0903.1455v1, first public version 2009-03-08.
4. S. Neuwirth, *On the (Fourier analytic) Sidon constant of \(\{0,1,2,3\}\)*, arXiv:2603.28229v1, first public version 2026-03-30.
