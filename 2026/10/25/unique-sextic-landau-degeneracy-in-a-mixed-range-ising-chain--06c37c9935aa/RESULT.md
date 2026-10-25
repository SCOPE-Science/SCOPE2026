# Unique sextic Landau degeneracy in a mixed-range Ising chain

## Finding

Consider the finite-temperature variational free-energy density of the transverse-field Ising chain with an additional all-to-all transverse coupling, as in Granet [1]. Set \(a=2\beta>0\) and \(t=\tanh a\). Along the quadratic-degeneracy curve
\[
\lambda_0(a)=-\frac{1}{t+a(1-t^2)}<0,
\]
there is **exactly one** temperature \(\beta_*=a_*/2>0\) for which the quartic Landau coefficient vanishes. It is the unique positive zero of
\[
K(a)=16a^3(2-\cosh(2a))+16a^2\sinh(2a)
+4a(1+\cosh(2a))-2\sinh(2a)-\sinh(4a).
\]
The root satisfies \(1.1429918<a_*<1.1429919\), so \(\beta_*=0.571495912711\ldots\) and \(\lambda_*:=\lambda_0(a_*)=-0.834427697363\ldots\). The quartic coefficient is positive below \(\beta_*\) and negative above it. At the unique point the sixth derivative is **strictly positive**, with certified rational interval
\[
3.2305076<\partial_x^6 F_{\beta_*,\lambda_*,0}(0)<3.2306338.
\]
Consequently, the origin is a strict sextic local minimum at zero external field. At fixed \((\beta_*,\lambda_*)\), the unique nearby stationary local minimizer for small nonzero field \(h\) obeys the model-specific fifth-root law
\[
x_h=\operatorname{sgn}(h)\left(\frac{60}{|\lambda_*|\,\partial_x^6 F_{\beta_*,\lambda_*,0}(0)}\right)^{\!1/5}|h|^{1/5}(1+o(1)).
\]
This is a statement about **local** minima/stationary points of the exact variational potential, not a proof of a global thermodynamic tricritical phase diagram.

## Assumptions and scope

For integer \(N\ge2\), periodic boundary conditions, spin Pauli matrices, \(\beta>0\), and \(\lambda<0\), the source Hamiltonian is
\[
H_N(h,\lambda)=-\sum_{j=1}^{N}\sigma_j^z\sigma_{j+1}^z+h\sum_{j=1}^{N}\sigma_j^x
+\frac{\lambda}{N}\left(\sum_{j=1}^{N}\sigma_j^x\right)^2.
\]
We analyze the source's thermodynamic variational potential (equation (107) of [1]):
\[
F_{\beta,\lambda,h}(x)=-\frac1{2\pi\beta}\int_0^\pi
\log\left(2\cosh\left(2\beta\sqrt{1+x^2+2x\cos k}\right)\right)\,dk
-\frac{(x-h)^2}{4\lambda},\qquad x,h\in\mathbb R.
\]
All derivatives in the claim are with respect to \(x\). We use this analytic potential only locally near \(x=0\) and make no assertion about the global minimizer or the unproved full-shape hypothesis (118) of [1]. The model's thermodynamic variational representation is inherited from [1], not independently rederived here.

## Proof

**Quadratic and quartic coefficients.** The integrand is analytic in \(x\) near the origin. Let \(f(z)=\log(2\cosh(a\sqrt z))\) and use the normalized angular moments \(\langle\cos^{2j}k\rangle=\binom{2j}{j}/4^j\), \(\langle\cos^{2j+1}k\rangle=0\). Since the integral contribution is \(-\langle f(1+2x\cos k+x^2)\rangle/a\), differentiation gives
\[
F''(0)=-\frac1{2\lambda}-\frac{t+a(1-t^2)}2,
\qquad
F^{(4)}(0)=\frac{3K(a)}{64\cosh^4 a}.
\]
The quadratic-zero equation gives precisely \(\lambda_0(a)\). Its denominator is positive for every positive \(a\).

**Exact uniqueness.** Expanding hyperbolic functions in the explicit numerator yields the absolutely convergent identity
\[
K(a)=\frac{128}{3}a^3-\sum_{n=2}^{\infty}d_n a^{2n+1},\qquad
d_n=\frac{4\,2^{2n}}{(2n+1)!}\left[8n(n^2-n-1)+4^n\right]>0.
\]
Indeed \(n^2-n-1\ge1\) for integer \(n\ge2\). Thus \(K(a)/a^3=128/3-\sum_{n\ge2}d_n a^{2n-2}\) is continuous and strictly decreasing on \((0,\infty)\), approaches \(128/3\) at the lower endpoint, and tends to \(-\infty\) as \(a\to\infty\) (already the \(n=2\) term suffices). It therefore has exactly one positive zero, with the claimed sign classification; this conclusion does not rely on numerical root finding.

**Nonzero sixth derivative.** With \(t=\tanh a\), direct sixfold differentiation and angular averaging give
\[
\begin{aligned}
F^{(6)}(0)=\frac5{16}\big(&120a^5t^6-240a^5t^4+136a^5t^2-16a^5\\
&-72a^4t^5+120a^4t^3-48a^4t\\
&-18a^3t^4+24a^3t^2-6a^3\\
&-12a^2t^3+12a^2t-9at^2+9a-9t\big).
\end{aligned}
\]
The accompanying exact-rational interval checker first certifies \(K(1.1429918)>0>K(1.1429919)\) by bounding exponentials with a finite Taylor sum and an explicit geometric remainder, then propagates this root interval into the displayed sixth-derivative polynomial. It proves \(3<F^{(6)}(0)<4\) (indeed the stated narrower rational interval) without floating-point sign assumptions. The symbolic checker independently reconstructs the second, fourth, and sixth derivatives by applying \(\frac1{2y}(\partial_y+a(1-t^2)\partial_t)\) repeatedly to \(f\), then using the exact angular moments. Neither finite checker substitutes for the analytical all-temperature coefficient-sign argument above.

**Local unfolding.** Evenness in \(x\) when \(h=0\), the vanishing second and fourth derivatives, and the strict positive sixth derivative show
\[
F_{\beta_*,\lambda_*,0}(x)-F_{\beta_*,\lambda_*,0}(0)
=\frac{F^{(6)}(0)}{720}x^6+O(x^8),
\]
so zero is a strict local minimum. The field adds exactly \(h x/(2\lambda_*)\) to the \(x\)-dependent part of \(F\). Its stationarity equation is therefore \(F^{(6)}(0)x^5/120+h/(2\lambda_*)+O(x^7)=0\). Analytic local monotonicity of this odd derivative for sufficiently small \(x\), and balancing these terms, give the unique nearby minimizer and fifth-root asymptotic. Along \(\lambda=\lambda_0(a)\), for \(a>a_*\) sufficiently close to \(a_*\), the implicit-function theorem in \(y=x^2\) also gives a pair of local minima with \(x^2=-20F^{(4)}(0)/F^{(6)}_{\beta_*,\lambda_*,0}(0)+o(a-a_*)\). For \(a<a_*\) the origin remains a strict quartic local minimum on this curve.

## Verification

`check_derivatives_landau.py` (SymPy) reconstructs all three derivatives from an explicit operator and exact combinatorial angular averages. `check_landau.py` (Python standard library) uses only integer/rational arithmetic, an 80-term exponential Taylor sum, and a geometric remainder to certify the root bracket and sextic positivity. Execute with `python check_derivatives_landau.py` and `python check_landau.py`; both were executed successfully. The proof of uniqueness across **all** \(a>0\) is the sign-defined entire power series, not a finite scan. The files are standalone and included alongside this note.

## Relationship to prior work

Granet [1, equations (107), (118)–(121)] derived the potential, gave numerical values \(\beta_*\approx0.571496\) and \(\lambda_*\approx-0.834428\), and explicitly treated a global finite-temperature shape statement as an unproved numerical hypothesis. The exact-value numerical location is **not** claimed as new. The addition here is the exact all-temperature uniqueness and sign certificate for the quartic degeneracy, the rigorous nonzero sixth-order coefficient, and the consequent local field scaling in this concrete spin-chain potential. Generic Landau expansion and fifth-root balance are known techniques; neither alone establishes the model-specific uniqueness and nondegeneracy. Schmid et al. [2] studied tricriticality in a distinct interacting-fermion Hamiltonian mean-field model and does not provide this spin-chain calculation on the basis of its abstract. Wider potentially equivalent treatments remain a residual literature risk.

## Limitations

The sixth-order result establishes a **local** degeneracy only; it does not establish Granet's full hypothesis (118), exclusion of distant competing minima, a global phase boundary, thermodynamic critical exponents of actual Gibbs observables, universality across other spin models, or finite-size fluctuation statements. The fifth-root law describes the stationary **local variational minimizer**. Literature searches cannot prove absolute novelty; analogous non-indexed results are possible.

## References

[1] E. Granet, *Exact mean-field solution of a spin chain with short-range and long-range interactions*, arXiv:2209.08756 (first posted 19 September 2022), SciPost Physics 14, 133 (2023), doi:10.21468/SciPostPhys.14.5.133. https://arxiv.org/abs/2209.08756

[2] H. Schmid, J. Dieplinger, A. Solfanelli, S. Succi, S. Ruffo, *Tricritical point in the quantum Hamiltonian mean-field model*, arXiv:2202.08855, Physical Review E 106, 024109 (2022). https://arxiv.org/abs/2202.08855
