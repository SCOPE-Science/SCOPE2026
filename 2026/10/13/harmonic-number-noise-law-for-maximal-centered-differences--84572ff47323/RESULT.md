# Harmonic-number noise law for maximal centered differences
## Finding
For every integer \(m\ge1\), the standard centered \((2m+1)\)-point first-derivative formula of maximal polynomial exactness is
\[
D_m f(0)=\frac1h\sum_{j=1}^m \alpha_{m,j}\bigl(f(jh)-f(-jh)\bigr),
\qquad
\alpha_{m,j}=(-1)^{j+1}\frac{(m!)^2}{j(m-j)!(m+j)!}.
\]
Its exact norm as a linear functional on sampled data with the maximum norm is
\[
\|D_m\|_{\ell_\infty\to\mathbb R}=\frac{H_m}h,
\qquad H_m=\sum_{j=1}^m\frac1j.
\]
Therefore, if every sample has a deterministic perturbation \(\eta_j\) satisfying \(|\eta_j|\le\varepsilon\), then
\[
|D_m\eta|\le\frac{\varepsilon H_m}h,
\]
and equality is attained by choosing each perturbation sign to agree with the corresponding stencil coefficient. The sharp worst-case amplification thus grows like \( (\log m+\gamma+o(1))/h\).

## Assumptions and scope
The grid is \(\{-mh,\ldots,-h,0,h,\ldots,mh\}\) with \(h>0\). The formula differentiates the degree-\(2m\) Lagrange interpolant at the center, so its usual smooth-function truncation order is \(2m\). The perturbation model is deterministic and componentwise: all \(2m+1\) sample errors may be chosen independently subject only to \(|\eta_j|\le\varepsilon\). The statement is an \(\ell_\infty\)-input worst-case law, not an RMS law for random noise and not a floating-point forward-error bound for computing the weights themselves.

## Proof
For a positive node index \(j\), differentiating the Lagrange cardinal polynomial at the center gives
\[
\ell_j'(0)=(-1)^{j+1}\frac{(m!)^2}{j(m-j)!(m+j)!}=\alpha_{m,j}.
\]
Reflection gives \(\ell_{-j}'(0)=-\ell_j'(0)\), while the center weight is zero. Hence the dimensionless coefficient absolute sum is
\[
2\sum_{j=1}^m a_{m,j},
\qquad
a_{m,j}=\frac{(m!)^2}{j(m-j)!(m+j)!}.
\]
Use the beta integral
\[
a_{m,j}
=\binom mj\int_0^1 t^m(1-t)^{j-1}\,dt.
\]
Summing over \(j\) and then putting \(s=1-t\) gives
\[
\begin{aligned}
S_m:=\sum_{j=1}^m a_{m,j}
&=\int_0^1 t^m\frac{(2-t)^m-1}{1-t}\,dt\\
&=\int_0^1\frac{(1-s^2)^m-(1-s)^m}s\,ds.
\end{aligned}
\]
Insert and subtract \(1\) in the numerator. In the first resulting integral set \(u=s^2\):
\[
S_m
=\frac12\int_0^1\frac{(1-u)^m-1}u\,du
-\int_0^1\frac{(1-s)^m-1}s\,ds.
\]
The standard finite geometric-series identity gives
\[
\int_0^1\frac{1-(1-x)^m}x\,dx=H_m.
\]
Therefore \(S_m=-H_m/2+H_m=H_m/2\), and the absolute coefficient sum is exactly \(H_m\). Restoring the factor \(h^-1\) proves the upper bound.

For sharpness, let \(w_k\) denote the coefficient multiplying the sample at node \(kh\), including the factor \(h^-1\). Choose \(\eta_k=\varepsilon\,\operatorname{sgn}(w_k)\) whenever \(w_k\ne0\). Then
\[
D_m\eta=\varepsilon\sum_k|w_k|=\frac{\varepsilon H_m}h,
\]
so the bound is attained.

## Verification
The accompanying `verify.py` reconstructs the coefficients with exact rational arithmetic for \(1\le m\le20\), checks polynomial moment exactness through degree \(2m\), and verifies that their absolute sum is exactly \(H_m\). These finite checks are supplementary; the all-\(m\) result is proved by the beta-integral identity above.

## Relationship to prior work
Fornberg's classical paper gives general finite-difference-weight recursions and tabulates centered equispaced coefficients; it explicitly identifies numerical differentiation as primary MSC 65D25. Sadiq and Viswanath later develop efficient finite-difference-weight algorithms and analyze superconvergence and numerical stability of weight computation. Those sources establish the standard weight-generation framework and motivate attention to numerical stability. The claim here is narrower and different: for the maximal centered first-derivative stencil it evaluates the exact data-to-derivative \(\ell_\infty\) operator norm in closed form, yielding the harmonic-number law \(H_m/h\).

## Limitations
No stochastic-noise variance statement is claimed. The result does not bound truncation error, finite-precision error in generating the coefficients, boundary or one-sided formulas, nonuniform grids, or higher derivative orders. The exact harmonic identity may conceivably appear in older numerical-differentiation or differentiation-formula conditioning literature under different terminology; that remains the main originality risk.

## References
1. B. Fornberg, “Generation of finite difference formulas on arbitrarily spaced grids,” *Mathematics of Computation* 51 (1988), 699–706. DOI: 10.1090/S0025-5718-1988-0935077-0.
2. B. Sadiq and D. Viswanath, “Finite Difference Weights, Spectral Differentiation, and Superconvergence,” arXiv:1102.3203; later *Mathematics of Computation* 83 (2014), 2403–2427.
