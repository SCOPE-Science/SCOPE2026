# Sharp all-lag positivity threshold for exponential-kernel truncated-trapezoidal convolution quadrature

## Finding

Let \(h>0\), \(\lambda\geq0\), and \(r=h\lambda\). Consider the optimized second-order truncated-trapezoidal (\(\operatorname{TTR}_2\)) multistep symbol
\[
\delta(\zeta)=(1-\zeta)+\frac12(1-\zeta)^2+\frac16(1-\zeta)^3
=\frac{10-15\zeta+6\zeta^2-\zeta^3}{6}.
\]
For the exponential convolution kernel \(k(t)=e^{-\lambda t}\), define all convolution-quadrature (CQ) weights by
\[
\sum_{n=0}^{\infty}\omega_n\zeta^n
=\frac{1}{\lambda+\delta(\zeta)/h}
=\frac{h}{r+\delta(\zeta)}.
\]
Write
\[
g(r)=1296r^4-154656r^3+1440720r^2-2997300r+1667125
\]
and let \(r_*\) be its unique zero in \((9332/10000,9333/10000)\). Numerically,
\[
r_*=0.933212708152000\ldots.
\]
Then the **sharp coefficientwise positivity classification** is:

* For \(0\leq r<r_*\), every \(\omega_n\) is strictly positive.
* At \(r=r_*\), \(\omega_6=0\), while every \(\omega_n\) with \(n\ne6\) is strictly positive.
* For every \(r>r_*\), at least one \(\omega_n\) is strictly negative.

Thus CQ with this kernel preserves nonnegativity of every finitely supported nonnegative input sequence exactly when \(h\lambda\leq r_*\). For comparison, BDF2-based CQ has the corresponding exact threshold \(h\lambda\leq1/2\). The larger threshold is specific to the \(\operatorname{TTR}_2\) symbol and the exponential kernel; it is not a statement about general completely monotone kernels or about energy coercivity.

## Assumptions and scope

The time step \(h\) is constant and strictly positive, \(\lambda\) is real and nonnegative, and the kernel's Laplace transform is exactly \(K(s)=(s+\lambda)^{-1}\). The method is Ferrari's optimal \(J=2\) truncated-trapezoidal symbol, with coefficient \(c_2^{(2)}=2/3\); there is no spatial discretization, startup approximation, or variable-step adaptation. All inequalities concern the exact Taylor coefficients at \(\zeta=0\); no floating-point sign convention is assumed.

For a discrete input \(v_0,v_1,\ldots\), the CQ output is \(y_n=\sum_{j=0}^n\omega_{n-j}v_j\). Coefficientwise nonnegativity is necessary and sufficient for \(y_n\geq0\) for all \(n\) and all nonnegative finitely supported inputs, by testing the unit impulse. Coefficientwise nonnegativity is stronger than positivity of certain convolution quadratic forms, and the two properties must not be conflated.

## Proof

**1. Rational recurrence and the critical sixth coefficient.** Put \(a=5/3+r\) and \(b=5/2\). The generating function becomes
\[
\sum_{n\geq0}\omega_n\zeta^n
=\frac{h}{a-b\zeta+\zeta^2-\zeta^3/6}.
\]
Normalize \(P_n(r)=a^{n+1}\omega_n/h\). Direct coefficient matching gives
\[
P_0=1,\quad P_1=b,\quad P_2=b^2-a,\qquad
P_n=bP_{n-1}-aP_{n-2}+\frac{a^2}{6}P_{n-3}\quad(n\geq3).
\]
All \(P_n\) are rational polynomials in \(r\), and direct exact expansion gives
\[
P_6(r)=\frac{g(r)}{46656}.
\]
The derivative \(g'(r)\) is strictly negative on \([4/5,15/16]\) by an exact rational Bernstein-basis sign certificate. Moreover \(g(9332/10000)>0>g(9333/10000)\). Hence the stated root exists, is unique in that interval, and \(\omega_6<0\) for \(r_*<r\leq15/16\). Positivity for \(r\leq r_*\) requires control of *every* index, not just the first six.

**2. A uniform all-lag bound from the roots.** Multiply the denominator by \(-6\) and consider
\[
f_r(z)=z^3-6z^2+15z-(10+6r).
\]
Its derivative is \(f'_r(z)=3((z-2)^2+1)>0\). Thus it has a unique real root \(s=s(r)\geq1\), strictly increasing with \(r\). The other roots are conjugate, have modulus \(R=\sqrt{s^2-6s+15}\), and have real part \((6-s)/2\). For \(0\leq r\leq15/16\), \(1\leq s\leq5/2\). Define
\[
\rho=\frac{s}{R},\qquad c=\frac{6-s}{2R}.
\]
In this regime \(0<\rho\leq1\) and \(7/10\leq c<4/5\). Factoring the denominator gives
\[
a-b\zeta+\zeta^2-\zeta^3/6
=a\left(1-\frac\zeta s\right)
\left(1-\frac{2c\zeta}{R}+\frac{\zeta^2}{R^2}\right).
\]
With the second-kind Chebyshev polynomials \(U_k\), the geometric and Chebyshev generating series yield the exact representation
\[
\frac{a s^n\omega_n}{h}
=\sum_{k=0}^n\rho^kU_k(c)
=\frac{1-\rho^{n+1}(U_{n+1}(c)-\rho U_n(c))}
{1-2\rho c+\rho^2}.
\]
For \(c=\cos\theta\), the sine representation of \(U_k\) and Cauchy–Schwarz give
\[
|U_{n+1}(c)-\rho U_n(c)|
\leq\sqrt{\frac{1-2\rho c+\rho^2}{1-c^2}}.
\]
Consequently **every** coefficient at index \(n\) is positive whenever
\[
\rho^{n+1}\sqrt{\frac{1-2\rho c+\rho^2}{1-c^2}}<1. \tag{1}
\]

**3. All indices for \(0\leq r\leq4/5\).** The rational inequality \(f_{4/5}(2263/1000)>0\) shows \(s<2263/1000\) in this interval. On \(1\leq s\leq2263/1000\), \(\rho\) is increasing, and exact rational endpoint comparisons give \(3/10<\rho<885/1000\). The bound \(7/10<c<4/5\) follows from monotonicity of \(c(s)\); in fact \(c'(s)=-3(s-1)/(2R^3)\leq0\). Therefore
\[
\frac{1-2\rho c+\rho^2}{1-c^2}
\leq\frac{1-(7/5)\rho+\rho^2}{9/25}
\leq\frac{67}{36}<\left(\frac75\right)^2.
\]
Since \((885/1000)^4(7/5)<1\), condition (1) holds for every \(n\geq3\). The initial polynomials \(P_0=1\), \(P_1=5/2\), \(P_2=55/12-r\) are positive. This proves strict positivity for the entire lower interval.

**4. All indices for \(4/5\leq r\leq r_*\).** Since \(r_*<9333/10000\) and
\(f_{9333/10000}(24933/10000)>0\), one has \(2<s<24933/10000\). The monotonicity of \(\rho(s)\) and a rational square comparison give \(\rho<997/1000\); moreover \(s>2\) implies \(\rho\geq c\). For \(c\geq7/10\) and \(c\leq\rho\leq1\),
\[
\frac{1-2\rho c+\rho^2}{1-c^2}
\leq\frac2{1+c}\leq\frac{20}{17}<\left(\frac{11}{10}\right)^2.
\]
The exact inequality \((997/1000)^{32}(11/10)<1\) makes condition (1) strict for every \(n\geq31\).

For the remaining finite set \(0\leq n\leq30\), generate the polynomials \(P_n(r)\) from the recurrence in Step 1. For every \(n\ne6\), all of the Bernstein coefficients of \(P_n\) on the slightly larger interval \([4/5,9333/10000]\) are **strictly positive**. The complete exact-rational test, including all degrees and coefficients, is the standalone standard-library script `certificate.py`. Since Bernstein basis functions are nonnegative and sum to one, these verified coefficient signs prove \(P_n(r)>0\) throughout that interval for each \(n\ne6\). The value \(P_6\) is positive before \(r_*\) and zero exactly at \(r_*\), by Step 1. This proves all-lag sufficiency and the unique vanishing index at the endpoint. This finite certificate is combined with the analytic tail bound: finite enumeration alone is not used to infer an infinite claim.

**5. Necessity at every larger step size.** For \(r_*<r\leq15/16\), the explicit \(P_6<0\) from Step 1 applies. For \(r>15/16\), the unique positive real denominator root satisfies \(s>5/2\), while the two complex poles have smaller modulus \(R<s\). Hence the Taylor series for \(h/(r+\delta(\zeta))\) has finite radius \(R\) and is analytic at the positive real point \(\zeta=R\). Pringsheim's theorem implies that a power series with all real nonnegative coefficients and finite radius of convergence must be singular at its positive real radius. This contradiction proves that **some** weight is negative for every \(r>15/16\), without asserting an index or frequency of negative weights in that outer region.

**6. BDF2 benchmark.** For \(\delta_{\mathrm{BDF2}}(\zeta)=3/2-2\zeta+\zeta^2/2\), the two denominator poles for exponential-memory CQ are positive real when \(r\leq1/2\), giving positive Taylor coefficients. When \(r>1/2\) the two poles are nonreal of minimal modulus, so Pringsheim's theorem rules out an all-nonnegative coefficient sequence. Thus the BDF2 threshold is exactly \(1/2\). The ratio of the TTR2 threshold to this benchmark is \(2r_*\approx1.8664254163\).

## Verification

`certificate.py` runs without third-party packages. It reconstructs \(P_0,\dots,P_{30}\) over exact rational arithmetic; verifies \(P_6=g/46656\); converts every other \(P_n\) to a Bernstein basis on \([4/5,9333/10000]\) and checks strict positivity of each coefficient; tests the negative Bernstein coefficients of \(g'\) on \([4/5,15/16]\); isolates \(r_*\) between rational endpoints; and checks all listed rational tail estimates. It completes **340 exact-rational checks**. The infinite-tail conclusion additionally relies on the displayed Chebyshev formula and its analytical bound, and necessity in the outer regime relies on Pringsheim's theorem; no bounded program execution substitutes for these arguments.

## Relationship to prior work

Ferrari [1], §§2–4, defines \(\operatorname{TTR}_J\), proves optimal coefficients under A-stability, and applies the method to convolution quadrature. At \(J=2\), his coefficient formula gives \(c_2^{(2)}=2/3\), fixing the symbol analyzed here. The present claim instead concerns the **sign of every individual CQ lag weight** for the exponential Laplace symbol \((s+\lambda)^{-1}\). The coefficientwise threshold is not a consequence of A-stability or of the principal error constant alone.

Banjai [2], §6, introduced the truncated-trapezoidal family in wave-equation discretization and discussed discrete coercivity. Karaa [3] studies positive definiteness of convolution quadratic forms generated by sequences (including BDF2), which does not imply coefficientwise nonnegativity: a sequence with negative off-diagonal entries can still define a positive-definite quadratic form. The classical BDF2 generating function and CQ definitions follow [1] and Lubich [4]. The exact all-lag TTR2 threshold, sixth-weight boundary, and outer complex-pole obstruction are not stated in the inspected material. This does not establish historical uniqueness; older specialized coefficient-sign results might exist.

## Limitations

The theorem is an exact-arithmetic, constant-step, scalar exponential-kernel result. It says nothing about arbitrary kernels, variable steps, full positivity of PDE solution operators, or stability in floating point. A-stability, positive-definite convolution forms, and entrywise nonnegative CQ weights are distinct properties. The exact polynomial root has not been established as a universally optimal parameter for any larger multistep family; only the specified optimized \(\operatorname{TTR}_2\) is analyzed. Priority against inaccessible specialized literature has not been independently adjudicated.

## References

[1] Matteo Ferrari, *Convolution quadrature based on a truncated trapezoidal rule*, arXiv:2607.11422, first public version July 13, 2026. https://arxiv.org/abs/2607.11422

[2] Lehel Banjai, *Implicit/explicit, BEM/FEM coupled scheme for acoustic waves with the wave equation in the second order formulation*, arXiv:2203.00986 (2022). https://arxiv.org/abs/2203.00986

[3] Samir Karaa, *Positivity of convolution quadratures generated by nonconvex sequences*, Comptes Rendus Mathématique 362 (2024), 1627–1634, https://doi.org/10.5802/crmath.669.

[4] Christian Lubich, *Convolution quadrature and discretized operational calculus. I*, Numerische Mathematik 52 (1988), 129–145.
