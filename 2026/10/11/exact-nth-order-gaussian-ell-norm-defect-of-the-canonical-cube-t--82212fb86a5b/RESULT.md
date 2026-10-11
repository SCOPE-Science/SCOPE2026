# Exact nth-order Gaussian ell-norm defect of the canonical cube truncation
## Finding
Fix an integer \(n\ge 2\). For \(0<\varepsilon<1/n\), define
\[
K_\varepsilon=B_\infty^n\cap\bigcap_{v\in\{-1,1\}^n}\{x\in\mathbb R^n:\langle x,v\rangle\le n(1-\varepsilon)\}.
\]
This is the symmetric family obtained by cutting every vertex of the cube by the hyperplane prescribed in Böröczky--Fodor--Hug. Then
\[
\ell(K_\varepsilon)=\ell(B_\infty^n)+c_n\varepsilon^n+o(\varepsilon^n)
\qquad(\varepsilon\downarrow0),
\]
with
\[
c_n=\frac{2^{\,n-1/2}n^{(n-1)/2}\Gamma((n+1)/2)}{n!\,\pi^{n/2}}>0.
\]
Thus the Gaussian \(\ell\)-norm defect of this canonical truncation is not merely \(O(\varepsilon^n)\): its first nonzero scale is exactly order \(\varepsilon^n\), with an explicit coefficient.

## Assumptions and scope
The dimension \(n\ge2\) is fixed while \(\varepsilon\downarrow0\). The Gaussian \(\ell\)-norm is
\[
\ell(K)=\mathbb E\,\|X\|_K,
\]
for a standard Gaussian vector \(X\in\mathbb R^n\). The parameter restriction \(0<\varepsilon<1/n\) is used only to make the local corner coordinates exact without additional boundary cases; it is automatic eventually in the stated asymptotic. The result concerns the specific all-vertex truncation used in the cited sharpness discussion and does not assert an optimal leading coefficient over all near-cube bodies.

## Proof
For every \(x\in\mathbb R^n\),
\[
\max_{v\in\{-1,1\}^n}\langle x,v\rangle=\|x\|_1.
\]
Hence
\[
K_\varepsilon=\{x:\|x\|_\infty\le1,\ \|x\|_1\le n(1-\varepsilon)\},
\]
and therefore its gauge is
\[
\|x\|_{K_\varepsilon}=
\max\left\{\|x\|_\infty,\frac{\|x\|_1}{n(1-\varepsilon)}\right\}.
\]
Let \(Y_i=|X_i|\), let \(M=\max_iY_i\), and let \(S=\sum_iY_i\). The variables \(Y_i\) are independent with half-normal density
\[
f(m)=\sqrt{\frac2\pi}e^{-m^2/2},\qquad m\ge0.
\]
Consequently
\[
\ell(K_\varepsilon)-\ell(B_\infty^n)
=\mathbb E\left[\frac{S}{n(1-\varepsilon)}-M\right]_+.
\]
The maximum is unique almost surely. By symmetry, condition on \(Y_1=M=m\) and write
\[
z_i=m-Y_i\quad(2\le i\le n).
\]
Then positivity of the displayed excess is equivalent to
\[
\sum_{i=2}^n z_i<n\varepsilon m.
\]
When \(\varepsilon<1/n\), this inequality itself implies \(0\le z_i<m\), so it exactly describes the relevant region. Multiplying the contribution of one maximizing coordinate by \(n\) gives
\[
\begin{aligned}
\Delta_\varepsilon
&:=\ell(K_\varepsilon)-\ell(B_\infty^n)\\
&=\frac1{1-\varepsilon}\int_0^\infty f(m)
\int_{\substack{z_i\ge0\\\sum_{i=2}^n z_i<n\varepsilon m}}
\left(n\varepsilon m-\sum_{i=2}^n z_i\right)
\prod_{i=2}^nf(m-z_i)\,dz\,dm.
\end{aligned}
\]
Put \(z_i=\varepsilon m w_i\). Then
\[
\frac{\Delta_\varepsilon}{\varepsilon^n}
=\frac1{1-\varepsilon}\int_0^\infty m^nf(m)
\int_{\substack{w_i\ge0\\\sum_{i=2}^n w_i<n}}
\left(n-\sum_{i=2}^n w_i\right)
\prod_{i=2}^nf\!\left(m(1-\varepsilon w_i)\right)\,dw\,dm.
\]
For \(0<\varepsilon<1/(2n)\), the inner domain is fixed and bounded, all arguments of \(f\) are nonnegative, and the integrand is dominated by a constant multiple of \(m^nf(m)\), which is integrable. Dominated convergence therefore yields
\[
\lim_{\varepsilon\downarrow0}\frac{\Delta_\varepsilon}{\varepsilon^n}
=\left(\int_{\substack{w_i\ge0\\\sum w_i<n}}
\left(n-\sum w_i\right)dw\right)
\left(\int_0^\infty m^nf(m)^n\,dm\right).
\]
The simplex integral is
\[
\int_{\substack{w_i\ge0\\\sum w_i<n}}
\left(n-\sum w_i\right)dw=\frac{n^n}{n!},
\]
while
\[
\int_0^\infty m^nf(m)^n\,dm
=\left(\frac2\pi\right)^{n/2}\frac12
\left(\frac2n\right)^{(n+1)/2}\Gamma\!\left(\frac{n+1}2\right).
\]
Multiplying these two factors gives exactly
\[
c_n=\frac{2^{\,n-1/2}n^{(n-1)/2}\Gamma((n+1)/2)}{n!\,\pi^{n/2}},
\]
which is strictly positive.

## Verification
The reduction from the \(2^n\) truncating halfspaces to the single \(\ell_1\)-constraint is exact because the support function of the sign cube is \(\|x\|_1\). The local integral keeps every normalization factor explicitly: the factor \(n\) from the maximizing coordinate cancels the denominator \(n\) in the gauge excess. The change of variables contributes \((\varepsilon m)^{n-1}\), and the remaining linear factor contributes one further \(\varepsilon m\), explaining the order \(\varepsilon^n\).

The accompanying `verify.py` numerically checks, for several dimensions, that the Gamma-function expression agrees with direct numerical quadrature of the half-normal moment entering the coefficient. This finite computation checks the closed-form arithmetic only; the asymptotic statement is proved by the dominated-convergence argument above.

## Relationship to prior work
Böröczky--Fodor--Hug define exactly this all-vertex truncation in their optimality discussion for their strengthened cube inequalities. They prove only the upper estimate
\[
\ell(K_\varepsilon)\le(1+\gamma_2\varepsilon^n)\ell(B_\infty^n)
\]
for a dimension-dependent constant \(\gamma_2>0\), using it to show that the stability exponent in their theorem cannot be pushed below \(n\). Their paper does not state a leading coefficient or an asymptotic equality for this family. The result above identifies the exact first nonzero Gaussian response and therefore certifies directly that the canonical witness has genuinely \(n\)-th order contact with the cube in \(\ell\)-norm.

The authors' earlier non-symmetric stability paper treats simplex extremizers rather than the symmetric cube truncation. Targeted searches for an exact Gaussian \(\ell\)-norm asymptotic, an equivalent half-normal maximum formulation, and a leading coefficient for the all-corner truncation did not locate a stronger or equivalent statement.

## Limitations
The theorem is asymptotic for fixed dimension. It does not give a remainder uniform in \(n\), it does not determine the best global near-cube stability exponent, and it does not optimize the leading coefficient among all perturbations. Bibliographic searches cannot exclude an equivalent formula hidden under substantially different terminology, especially for this recent source family.

## References
1. K. J. Böröczky, F. Fodor, D. Hug, “Strengthened inequalities for the mean width and the \(\ell\)-norm of origin symmetric convex bodies,” arXiv:2410.11460v1, first public 2024-10-15; *Mathematische Annalen* 393 (2025), 271–316, DOI:10.1007/s00208-025-03228-0. Primary MSC 52A40.
2. K. J. Böröczky, F. Fodor, D. Hug, “Strengthened inequalities for the mean width and the \(\ell\)-norm,” arXiv:2001.10706v1, first public 2020-01-29. This is the earlier non-symmetric simplex analogue.
