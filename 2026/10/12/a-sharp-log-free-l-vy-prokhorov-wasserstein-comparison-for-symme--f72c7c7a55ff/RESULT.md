# A sharp log-free Lévy–Prokhorov/Wasserstein comparison for symmetric geometric laws
## Finding
For \(0<B\le1\), consider the symmetric geometric family
\[
\mu_r(\{k\})=\frac{1-r}{1+r}r^{|k|},
\qquad
k\in\mathbb Z,\quad 0\le r<1.
\]
Each law is centered and log-concave. Its first absolute moment is
\[
\mathbb E_{\mu_r}|X|=\frac{2r}{1-r^2}.
\]
Hence the constraint \(\mathbb E_{\mu_r}|X|\le B\) is equivalent to
\[
0\le r\le R_B:=\frac{B}{\sqrt{1+B^2}+1}.
\]

For any \(0\le r<s\le R_B\),
\[
d_{\mathrm{LP}}(\mu_r,\mu_s)
=
\frac{2(s-r)}{(1+r)(1+s)}
\]
and
\[
W_1(\mu_r,\mu_s)
=
2\left(\frac{s}{1-s^2}-\frac{r}{1-r^2}\right).
\]
Consequently
\[
\frac{W_1(\mu_r,\mu_s)}{d_{\mathrm{LP}}(\mu_r,\mu_s)}
=
\frac{1+rs}{(1-r)(1-s)}.
\]
The right-hand side increases in each parameter. Therefore
\[
W_1(\mu_r,\mu_s)
\le
\left(1+B^2+B\sqrt{1+B^2}\right)
d_{\mathrm{LP}}(\mu_r,\mu_s),
\]
and this constant is sharp as a supremum over distinct pairs. At \(B=1\),
\[
W_1(\mu_r,\mu_s)\le(2+\sqrt2)d_{\mathrm{LP}}(\mu_r,\mu_s),
\]
with \(2+\sqrt2\) best possible.

## Assumptions and scope
The metric on \(\mathbb Z\) is the ordinary Euclidean distance inherited from \(\mathbb R\). The Lévy–Prokhorov distance is the standard one induced by this metric, and \(W_1\) is the ordinary first Wasserstein distance. The parameter range is \(0<B\le1\). The endpoint \(r=0\) denotes the point mass at zero.

The finding concerns only the centered symmetric geometric, also called discrete-Laplace, family. It does not remove the logarithmic factor for arbitrary discrete log-concave laws and does not assert that the displayed family is extremal for the full class.

## Proof
Write
\[
p_r(k)=\frac{1-r}{1+r}r^{|k|}.
\]
A geometric-series calculation gives
\[
\mathbb E_{\mu_r}|X|
=
2\frac{1-r}{1+r}\sum_{k\ge1}kr^k
=
\frac{2r}{1-r^2}.
\]
Solving \(\frac{2r}{1-r^2}\le B\) gives \(r\le R_B\).

Because \(B\le1\),
\[
R_B\le\sqrt2-1.
\]
For every integer \(k\ge1\), the function
\[
r\longmapsto \frac{1-r}{1+r}r^k
\]
is increasing on \([0,\sqrt2-1]\). Indeed, for \(r>0\) its logarithmic derivative is
\[
\frac{k}{r}-\frac{2}{1-r^2},
\]
which is bounded below by
\[
\frac1r-\frac{2}{1-r^2}\ge0
\]
exactly on \(0<r\le\sqrt2-1\). Thus if \(r<s\le R_B\), then
\[
p_r(0)>p_s(0),
\qquad
p_r(k)<p_s(k)\quad\text{for every }k\ne0.
\]
The minimum mismatch probability in a coupling is therefore
\[
\delta
=
p_r(0)-p_s(0)
=
\frac{2(s-r)}{(1+r)(1+s)}.
\]
Since \(\delta<1\), any coupling of integer-valued variables has
\[
\{|X-Y|>\varepsilon\}=\{X\ne Y\}
\]
for \(0<\varepsilon<1\). The Ky–Fan coupling representation of the Lévy–Prokhorov metric therefore gives
\[
d_{\mathrm{LP}}(\mu_r,\mu_s)=\delta.
\]

For \(k\ge0\),
\[
F_r(k)=1-\frac{r^{k+1}}{1+r},
\]
whereas for \(j\ge1\),
\[
F_r(-j)=\frac{r^j}{1+r}.
\]
For \(r<s\), the CDF differences have opposite signs on the two half-lines, and the one-dimensional identity
\[
W_1(\mu_r,\mu_s)
=
\sum_{k\in\mathbb Z}|F_r(k)-F_s(k)|
\]
yields
\[
W_1(\mu_r,\mu_s)
=
2\sum_{j\ge1}
\left(
\frac{s^j}{1+s}-\frac{r^j}{1+r}
\right)
=
2\left(\frac{s}{1-s^2}-\frac{r}{1-r^2}\right).
\]
Dividing by the exact Lévy–Prokhorov distance and simplifying gives
\[
\frac{W_1}{d_{\mathrm{LP}}}
=
\frac{1+rs}{(1-r)(1-s)}.
\]
This ratio is strictly increasing in both \(r\) and \(s\). Hence its supremum under the moment constraint is
\[
\frac{1+R_B^2}{(1-R_B)^2}
=
1+B^2+B\sqrt{1+B^2}.
\]
Sharpness follows by fixing \(s=R_B\) and letting \(r\uparrow R_B\) through distinct values. Substitution of \(B=1\) gives \(2+\sqrt2\).

## Verification
The standalone script `verify.py` checks the moment formula, the central-versus-noncentral mass ordering, the exact Lévy–Prokhorov and \(W_1\) formulas against direct truncated sums on a deterministic parameter grid, the ratio identity, and approach to the sharp constant. It uses only the Python standard library.

Its successful terminal line is:
`VERIFY_OK B1_constant=3.414213562373095 max_formula_error<1e-12`.

The finite computation is a regression check only. The all-parameter statement and sharpness are proved analytically above.

## Relationship to prior work
Marsiglietti and Pandey study quantitative equivalence of statistical distances for discrete log-concave measures. Their Theorem 3.1 gives a \(W_1\)-versus-Lévy–Prokhorov bound for centered log-concave laws, and Remark 3.3 specializes it to first absolute moment at most one with a logarithmic factor. Remark 3.4 explicitly says that removing that logarithmic factor in the full class remains open. The same paper lists geometric laws among basic discrete log-concave examples and later mentions the symmetric geometric distribution as a natural reference measure.

The present result does not solve that open problem for the full class. It gives an exact, sharp log-free comparison on the canonical symmetric log-affine geometric family, with the whole dependence on the first-absolute-moment budget \(B\) and the exact unit-budget constant \(2+\sqrt2\).

Targeted searches for the symmetric-geometric/discrete-Laplace formulation, exact \(W_1\)-to-Lévy–Prokhorov ratio, and the constant \(2+\sqrt2\) did not locate a covering published statement.

## Limitations
The proof relies crucially on \(B\le1\). In that range the noncentral point masses are monotone in the geometric parameter, so the two laws cross only at the central atom. For larger moment budgets additional crossing locations appear, and the same formula need not hold.

The result is a sharp benchmark for a natural one-parameter subfamily, not a resolution of the general logarithm-removal question. Search noncoverage is evidence of originality, not a proof that no equivalent identity exists under different terminology.

## References
1. A. Marsiglietti and P. Pandey, *A Note on Statistical Distances for Discrete Log-Concave Measures*, arXiv:2309.03197v1, first public 2023-09-06; revised version arXiv:2309.03197v2.
2. A. L. Gibbs and F. E. Su, *On Choosing and Bounding Probability Metrics*, arXiv:math/0209021.
