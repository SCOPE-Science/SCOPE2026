# Sharp second singular asymptotics and rank-two collapse for high Volterra powers

## Finding

For the Riemann–Liouville fractional integral \(I^\alpha\) on real or complex \(L^2(0,1)\), normalize \(T_\alpha=\Gamma(\alpha+1)I^\alpha\). As the real order \(\alpha\to+\infty\), the singular values, in descending order, obey

\[
s_2(T_\alpha)=\frac{1}{8\alpha}+O(\alpha^{-2}),
\qquad
\sum_{j\ge3}s_j(T_\alpha)^2=O(\alpha^{-4}),
\]

and the leading singular value satisfies

\[
\|T_\alpha\|=s_1(T_\alpha)
=\frac12+\frac{1}{8\alpha}+\frac{1}{32\alpha^2}+O(\alpha^{-3}).
\]

The result identifies the first nontrivial singular mode and a sharp norm correction beyond the previously known rank-one leading asymptotic. In particular, the best Hilbert–Schmidt rank-two error has size \(O(\alpha^{-2})\), while the best rank-one operator-norm error is asymptotic to \(1/(8\alpha)\).

## Assumptions and scope

Let \(\alpha>1\) be real and let \(I^\alpha\) act on \(L^2(0,1;\mathbb K)\), where \(\mathbb K=\mathbb R\) or \(\mathbb C\), by

\[
(I^\alpha f)(x)=\frac1{\Gamma(\alpha)}\int_0^x (x-y)^{\alpha-1}f(y)\,dy.
\]

The nonzero singular values are \(s_1\ge s_2\ge\cdots\ge0\), including multiplicities, and the symbols \(O(\cdot)\) refer to the limit \(\alpha\to+\infty\), with absolute constants independent of \(\alpha\) once sufficiently large. The statement applies to positive integer powers of the classical Volterra operator and, without rounding, to arbitrary large real fractional orders. No infinite-dimensional numerical experiment is used as proof.

## Proof

**1. Hankel normal form.** Multiplication by \(\Gamma(\alpha+1)\) makes the integral kernel \(\alpha(x-y)^{\alpha-1}\mathbf 1_{0<y<x<1}\). Apply the output coordinate change \(u=\alpha(1-x)\) and independent input change \(v=\alpha y\), with the \(\alpha^{-1/2}\) factors that make both maps unitary on \(L^2\). The resulting operator, extended by zero to \(L^2(0,\infty)\), is the compact *self-adjoint* Hankel integral operator \(K_\alpha\) with kernel

\[
k_\alpha(u,v)=\left(1-\frac{u+v}{\alpha}\right)_+^{\alpha-1},\qquad u,v\ge0.
\]

Both changes are isometries onto the interval \((0,\alpha)\), and the zero extension preserves every nonzero singular value.

**2. A sharp rank-two approximation.** Write \(\varepsilon=1/\alpha\), and define the real functions

\[
g(u)=e^{-u},\qquad
h(u)=\left(u-\tfrac12\right)e^{-u},\qquad
a(u)=\left(\tfrac u2-\tfrac{u^2}2+\tfrac18\right)e^{-u}.
\]

Here \(|f\rangle\langle f|\) denotes the rank-one operator with kernel \(f(u)\overline{f(v)}\). A two-term expansion of the scalar Hankel kernel yields the *Hilbert–Schmidt* estimate

\[
\left\|K_\alpha-
\left(|g+\varepsilon a\rangle\langle g+\varepsilon a|
-\varepsilon|h\rangle\langle h|\right)\right\|_{S_2}
=O(\varepsilon^2).
\tag{1}
\]

Indeed, with \(s=u+v\),

\[
k_\alpha(u,v)=e^{-s}\left[1+\varepsilon\left(s-\tfrac12s^2\right)\right]+\rho_\alpha(s),
\qquad \int_0^\infty s|\rho_\alpha(s)|^2\,ds=O(\varepsilon^4).
\tag{2}
\]

To justify the bound uniformly rather than pointwise, when \(0\le s\le\alpha/2\), expand

\[
(\alpha-1)\log(1-s/\alpha)
=-s+\sum_{m\ge1}\varepsilon^m
\left(\frac{s^m}{m}-\frac{s^{m+1}}{m+1}\right).
\]

Taylor's theorem in \(\varepsilon\), with \(\varepsilon s\le1/2\), and differentiation of this absolutely convergent series give

\[
|\rho_\alpha(s)|\le C\varepsilon^2e^{-s+1/2}(s^2+s^3+s^4).
\]

For \(s>\alpha/2\), both the original kernel and its displayed first-order approximation have exponentially small square-integrable tails; specifically the original is bounded by \(e^{-s/2}\) for \(\alpha\ge2\). The Hankel Hilbert–Schmidt identity \(\iint F(u+v)^2\,du\,dv=\int_0^\infty sF(s)^2\,ds\) proves (2). Finally, direct polynomial multiplication shows

\[
e^{-s}(s-s^2/2)=a(u)g(v)+g(u)a(v)-h(u)h(v),
\]

and the omitted \(\varepsilon^2|a\rangle\langle a|\) has Hilbert–Schmidt norm \(O(\varepsilon^2)\), proving (1).

**3. Sharp second singular mode.** Elementary exponential moments give

\[
\langle g,h\rangle=0,\qquad \|g\|_2^2=\tfrac12,\qquad\|h\|_2^2=\tfrac18.
\]

The best rank-one approximation inequality applied to (1) gives \(s_2(K_\alpha)\le\varepsilon/8+O(\varepsilon^2)\). For the opposite inequality, take the Rayleigh quotient in the direction \(h\):

\[
\frac{\langle h,K_\alpha h\rangle}{\|h\|_2^2}
=-\frac{\varepsilon}{8}+O(\varepsilon^2),
\]

because \(\langle h,g+\varepsilon a\rangle=O(\varepsilon)\). The self-adjoint min–max principle produces a negative eigenvalue of absolute value at least \(\varepsilon/8-O(\varepsilon^2)\). Since (1) also gives \(K_\alpha\to|g\rangle\langle g|\) in operator norm, exactly one eigenvalue can have order-one magnitude. Thus this negative eigenvalue contributes to the nonleading singular spectrum, establishing

\[
s_2(T_\alpha)=\tfrac18\varepsilon+O(\varepsilon^2).
\]

The displayed approximation (1) has rank at most two. Hilbert–Schmidt Eckart–Young therefore yields \(\sum_{j\ge3}s_j(T_\alpha)^2\le\|R_\alpha\|_{S_2}^2=O(\varepsilon^4)\), establishing the rank-two tail conclusion.

**4. Norm coefficient from the exact Hilbert–Schmidt mass.** Integrating the original kernel directly yields, for every \(\alpha>1\),

\[
\|T_\alpha\|_{S_2}^2
=\frac{\alpha^2}{(2\alpha-1)(2\alpha)}
=\frac1{4-2\varepsilon}.
\]

The already proved singular-value formulas imply

\[
s_1(T_\alpha)^2
=\frac1{4-2\varepsilon}
-\left(\frac{\varepsilon}{8}+O(\varepsilon^2)\right)^2
-O(\varepsilon^4)
=\frac14+\frac\varepsilon8+\frac{3\varepsilon^2}{64}+O(\varepsilon^3).
\]

Taking the positive square root gives \(s_1(T_\alpha)=1/2+\varepsilon/8+\varepsilon^2/32+O(\varepsilon^3)\), completing the proof.

## Verification

A standalone script `check_volterra.py` uses Gauss–Laguerre Nyström discretization of the self-adjoint Hankel kernel and computes finite singular spectra at orders \(\alpha\in\{20,40,80,160,320\}\). The resulting values of \(\alpha s_2\) decrease from approximately \(0.1298465863\) to \(0.1252935799\), tending toward the analytical constant \(1/8\); the scaled second-order norm residual approaches \(1/32\). The discretized Hilbert–Schmidt masses agree with the exact mass within roundoff at these test points. These finite-precision checks corroborate, but do not establish, the infinite-order theorem; the proof is the analytic Hilbert–Schmidt expansion and min–max argument above.

Reproduction: install Python 3 with NumPy at least 1.24 and SciPy at least 1.10, then execute `python check_volterra.py`. The script prints `FINITE_NUMERICAL_CHECKS_OK` on success.

## Relationship to prior work

The leading \(\Gamma(\alpha+1)\|I^\alpha\|\to1/2\), asymptotic rank-one behavior, and asymptotic equality of the operator, Hilbert–Schmidt and trace norms were established in work by Kershaw, Thorpe and Eveson; these are **not** asserted as new. Eveson's complete published 2003 paper and 2004 arXiv preprint were examined, including the rank-one comparison results and discussion of the rate of trace-norm collapse. Neither inspected full text specifies the sharp second singular coefficient \(1/8\), the rank-two Hilbert–Schmidt remainder, or the \(1/32\) operator-norm coefficient as consequences of its stated theorems. Thorpe's 1998 abstract confirms the leading norm asymptotic, but its complete text could not be inspected, so the literature comparison is not exhaustive. Known large-*singular-index* estimates for fractional integration are in a different limit from the large-*order*, fixed-index limit proved here.

## Limitations

The theorem quantifies the second singular value and the squared tail beyond rank two; it gives no sharp constant for the third or later individual singular values and no complete trace-norm defect asymptotic. It does not assert that the displayed remainder bounds or numerical discretization errors have optimal rates. Unavailable full texts of certain historical papers leave an originality risk.

## References

1. S. P. Eveson, *Norms of Iterates of Volterra Operators on* \(L^2\), Journal of Operator Theory **50** (2003), 369–386, https://jot.theta.ro/jot/archive/2003-050-002/2003-050-002-010.pdf.
2. S. P. Eveson, *Asymptotic Behaviour of Iterates of Volterra Operators on* \(L^p(0,1)\), arXiv:math/0409516v1 (publicly posted 2004-09-27), https://arxiv.org/abs/math/0409516.
3. B. Thorpe, *The Norm of Powers of the Indefinite Integral Operator on (0,1)*, Bulletin of the London Mathematical Society **30** (1998), 543–548, DOI:10.1112/S0024609398004810 (publisher abstract inspected; full text unavailable).
4. M. R. Dostanić, *Estimates for the norm of powers of Volterra's operator through its singular values*, Mathematische Zeitschrift **236** (2001), DOI:10.1007/PL00004837 (bibliographic abstract inspected; full text unavailable).
5. P. Burman, *Sharp bounds for singular values of fractional integral operators*, Journal of Mathematical Analysis and Applications **327** (2007), DOI:10.1016/j.jmaa.2006.03.073 (abstract inspected).
