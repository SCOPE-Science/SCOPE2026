# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof was checked from the defining integral rather than from numerical evidence. With \(a=\nu+1/2\), the target is exactly the positivity of
\[
D_a(r)=\int_0^1(1-x^2)^{a-1}b_r(x)\,dx,
\]
where
\[
b_r(x)=(1+x)e^{-2r(1-x)}+(1-x)e^{-2r(1+x)}-2x^{2r}.
\]
The beta-integral normalization and all powers of \(2\) and gamma factors were recomputed.

For \(r>0\), writing \(k=2r\) and
\[
H_r(x)=e^{-k}\frac{\cosh(kx)+x\sinh(kx)}{x^k}
\]
gives \(b_r=2x^k(H_r-1)\). The derivative calculation reduces the sign of \(H_r'\) to
\[
x\tanh(kx)-k(1-x^2),
\]
whose derivative is strictly positive. Hence \(H_r\) has one minimum, and because \(H_r(0+)=\infty\) and \(H_r(1)=1\), \(b_r\) has exactly one sign change from positive to negative.

The limiting integral was independently simplified:
\[
\int_0^1\frac{b_r(x)}{1-x^2}\,dx
=
\psi(r+1/2)-\log r+\operatorname{Ei}(-4r).
\]
Differentiating gives a Laplace transform whose kernel is negative on \((0,4)\) and positive on \((4,\infty)\). The decreasing exponential multiplier implies that this derivative can cross zero at most once, from positive to negative. Its left-end limit is \(\pi^2/2-4>0\), while the function itself tends to \(0\) at both \(0+\) and \(+\infty\). Therefore the limiting integral is strictly positive.

For \(a>0\), the additional factor \((1-x^2)^a\) is decreasing. Since the base integrand has one sign change from positive to negative, this factor can only increase its signed balance relative to its value at the crossing point. This yields strict positivity for every \(\nu>-1/2\). The half-order Bessel formulas give equality for \(\nu=-1/2\); \(r=0\) gives the other equality family.

Representative high-precision numerical checks were also performed, including negative orders close to \(-1/2\), but they are supplementary to the analytic argument.

## Originality

PASS, to the best of our knowledge.

Baricz and Pogány (2014) was inspected at the definition of \(\Phi_\nu\), its integral representation, Theorem 3, and the final Open Problem. The paper explicitly asks for a generalization of Kanter's inequality for \(\Phi_\nu\), while its proved Kanter bound is the \(\nu=0\) case.

Searches covered the exact source title and DOI, `Phi_nu`, "generalization of Kanter's inequality", the gamma ratio \(\Gamma(r+1/2)/\Gamma(r+\nu+1)\), the equivalent modified-Bessel statement, and the equivalent confluent-hypergeometric statement.

Veestraeten (2026), which directly cites Baricz–Pogány and revisits the same \(\Phi_\nu\) expression, was checked as a recent status source. Its accessible text rewrites \(\Phi_\nu\) through \({}_1F_1\) and discusses Kanter's inequality, but no equivalent gamma-ratio lower bound was located.

Residual originality risk remains because inequalities for Kummer functions and beta integrals are extensive and may use substantially different notation.

## Value

PASS.

The bound has the structure expected of a genuine Kanter extension: it reduces exactly to the known \(\nu=0\) theorem, has equality at the natural boundary order \(\nu=-1/2\), is exact at \(r=0\), and matches the leading asymptotics as \(r\to\infty\). The proof also isolates a reusable analytic mechanism: a one-sign-change kernel remains positive after all decreasing beta-type reweightings once the boundary-weight integral is controlled.

## Limitations

- The result does not classify every possible sharp bound for \(I_\nu+I_{\nu+1}\).
- Standard Bessel, beta, digamma, trigamma and exponential-integral identities are used and are not claimed as new.
- Equivalent prior coverage under different special-function notation remains possible.
- Independent audit has not been performed.
