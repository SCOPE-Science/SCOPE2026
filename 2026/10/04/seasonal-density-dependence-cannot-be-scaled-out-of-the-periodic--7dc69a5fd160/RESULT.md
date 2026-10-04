# Seasonal density dependence cannot be scaled out of the periodic mosquito map

## Finding

Consider the periodic mosquito population model
\[
w_{n+1}
=
\left(
\frac{r_n+\mu_n\eta_n w_n}
{1+\eta_n w_n}
\right)w_n,
\qquad
r_n=a_nk_n+\mu_n,
\]
where the parameter sequences are \(N\)-periodic and positive.

The source states that the density-dependence factor can be scaled out by setting
\[
z_n=\eta_nw_n
\]
and then using the recurrence
\[
z_{n+1}
=
\left(
\frac{r_n+\mu_nz_n}
{1+z_n}
\right)z_n.
\]
That recurrence is correct when \(\eta_n\) is constant, but it is not correct for a genuinely time-varying periodic sequence.

The exact transformed equation is
\[
z_{n+1}
=
\frac{\eta_{n+1}}{\eta_n}
\left(
\frac{r_n+\mu_nz_n}
{1+z_n}
\right)z_n.
\]
Hence a nonconstant seasonal density-dependence profile cannot be removed by the source's pointwise rescaling.

More precisely, for positive states the displayed ratio-free transformed equation holds at every step if and only if
\[
\eta_{n+1}=\eta_n
\]
for every \(n\). For a periodic sequence, this is equivalent to \(\eta_n\) being constant.

There is a useful partial scaling invariance. If the whole profile is multiplied by one constant \(c>0\),
\[
\eta'_n=c\eta_n,
\]
then solutions are related by the global rescaling
\[
w'_n=\frac{w_n}{c}.
\]
Thus an overall amplitude of density dependence can be normalized, but its relative seasonal pattern cannot.

The source's threshold
\[
\alpha=\prod_{n=1}^{N}r_n
\]
is nevertheless correctly independent of \(\eta_n\). In the true transformed dynamics the additional factors telescope:
\[
\prod_{n=1}^{N}\frac{\eta_{n+1}}{\eta_n}=1.
\]
The error therefore concerns finite-density dynamics and periodic-orbit amplitudes, not the linear extinction/persistence threshold at the origin.

An exact two-season counterexample uses
\[
a_1=a_2=\frac{7}{10},\qquad
k_1=k_2=1,\qquad
\mu_1=\mu_2=\frac12,
\]
so
\[
r_1=r_2=\frac65,
\]
and
\[
\eta_1=\frac14,\qquad
\eta_2=\frac34.
\]
All of these values lie in the biological parameter ranges used by the source, and
\[
\alpha=\frac{36}{25}>1.
\]

If the source's ratio-free normalization were valid, the normalized map would be
\[
g(z)=
z\frac{\frac65+\frac12z}{1+z}.
\]
Its positive fixed point is
\[
z_*=\frac25.
\]
Pointwise conversion back to population size would then give
\[
w_1=\frac{z_*}{\eta_1}=\frac85,
\qquad
w_2=\frac{z_*}{\eta_2}=\frac{8}{15}.
\]

The original model gives something different. At the first season,
\[
w_2
=
\frac85
\frac{
\frac65+\frac12\frac14\frac85
}{
1+\frac14\frac85
}
=
\frac85.
\]
Therefore the claimed rescaled pair is not even an orbit. In normalized coordinates,
\[
z_1=\frac25,
\qquad
z_2=\eta_2w_2=\frac65,
\]
and the factor of three is precisely
\[
\frac{\eta_2}{\eta_1}=3.
\]

The true positive two-cycle can also be recovered exactly from the two-step return map. Its first phase \(x_*>0\) is the unique positive root of
\[
225x^3+2960x^2+4480x-5632=0.
\]
Numerically,
\[
w_1=x_*\approx0.8039743678767607,
\qquad
w_2\approx0.8705842366428630.
\]
The normalized phase values are
\[
\eta_1w_1\approx0.2009935919691902,
\qquad
\eta_2w_2\approx0.6529381774821472,
\]
so they are neither equal to each other nor equal to \(2/5\).

## Assumptions and scope

The result concerns the scalar periodic mosquito map printed as model (2) in the source. The parameter assumptions are the source's positive periodic setting, with
\[
0<a_n<1,\qquad
0<\mu_n<1,\qquad
0<\eta_n<1,
\]
and the original biological range
\[
0\le k_n\le1.
\]

The correction does not challenge the source's threshold
\[
\alpha=\prod_{n=1}^{N}r_n.
\]
That threshold is a linearization statement at \(w=0\), where \(\eta_n\) indeed drops out.

The result instead corrects the stronger finite-density scaling assertion used to justify fixing \(\eta_n\equiv1\) and rescaling simulations afterward. That justification is valid only when the density-dependence sequence is constant up to one common global factor.

## Proof

Set
\[
z_n=\eta_nw_n.
\]
Then
\[
w_n=\frac{z_n}{\eta_n}.
\]
Substitution into the original recurrence gives
\[
w_{n+1}
=
\left(
\frac{r_n+\mu_nz_n}{1+z_n}
\right)
\frac{z_n}{\eta_n}.
\]
Multiplying by \(\eta_{n+1}\) yields
\[
z_{n+1}
=
\frac{\eta_{n+1}}{\eta_n}
\left(
\frac{r_n+\mu_nz_n}{1+z_n}
\right)z_n.
\]

For every positive \(z_n\), the second factor is positive. Therefore the source's ratio-free formula agrees with the true transformed equation for every positive state at step \(n\) exactly when
\[
\frac{\eta_{n+1}}{\eta_n}=1.
\]
Requiring this for every \(n\) makes the periodic sequence constant.

Now suppose instead that two density-dependence profiles satisfy
\[
\eta'_n=c\eta_n
\]
with a single constant \(c>0\). If \(w_n\) solves the model with \(\eta_n\), put
\[
w'_n=\frac{w_n}{c}.
\]
Then
\[
\eta'_nw'_n=\eta_nw_n,
\]
and direct substitution shows that \(w'_n\) solves the model with \(\eta'_n\). This proves the weaker global scaling invariance.

At the origin, the derivative of the \(n\)-th one-step map is
\[
r_n.
\]
Thus the derivative of one full period is
\[
\alpha=\prod_{n=1}^{N}r_n.
\]
The same fact appears in normalized coordinates because
\[
\prod_{n=1}^{N}
\left(
\frac{\eta_{n+1}}{\eta_n}r_n
\right)
=
\frac{\eta_{N+1}}{\eta_1}
\prod_{n=1}^{N}r_n
=
\alpha,
\]
using periodicity
\[
\eta_{N+1}=\eta_1.
\]

For the exact counterexample, define
\[
h_j(w)
=
w
\frac{
\frac65+\frac12\eta_jw
}{
1+\eta_jw
},
\qquad
\eta_1=\frac14,
\quad
\eta_2=\frac34.
\]
The source's normalized map has positive fixed point \(2/5\), but
\[
h_1\left(\frac85\right)=\frac85,
\]
so the back-scaled phase value \(8/15\) is not reached.

For completeness, the two-step return map is
\[
H(x)
=
\frac{
3x(5x+48)(5x^2+80x+128)
}{
20(x+4)(15x^2+184x+160)
}.
\]
A direct subtraction gives
\[
H(x)-x
=
-\frac{
x\left(225x^3+2960x^2+4480x-5632\right)
}{
20(x+4)(15x^2+184x+160)
}.
\]
For \(x>0\), the denominator is positive. The polynomial
\[
P(x)=225x^3+2960x^2+4480x-5632
\]
satisfies
\[
P(0)<0
\]
and
\[
P'(x)=675x^2+5920x+4480>0.
\]
Hence it has exactly one positive zero. This proves uniqueness of the positive two-cycle without relying on numerical iteration.

## Verification

The bundled `verify.py` uses exact rational and symbolic arithmetic to reproduce:

\[
r_1=r_2=\frac65,
\qquad
\alpha=\frac{36}{25},
\]
the source-normalized fixed point
\[
z_*=\frac25,
\]
the source-implied pair
\[
\left(\frac85,\frac{8}{15}\right),
\]
and the actual first step
\[
h_1\left(\frac85\right)=\frac85.
\]

It symbolically reconstructs the two-step return map and its fixed-point polynomial, verifies strict monotonicity of that polynomial on the positive axis, and computes the unique positive root and corresponding second phase.

The checker also verifies the correct normalized update
\[
z_2=\frac{\eta_2}{\eta_1}g(z_1)=\frac65.
\]

## Relationship to prior work

Wang, Gu, Wang, Liao, and Zheng study the exact periodic mosquito model considered here. Their Section 5 notes correctly that the threshold \(\alpha\) is independent of \(\eta_n\), but then attributes this to a pointwise transformation \(z_n=\eta_nw_n\) that omits the factor \(\eta_{n+1}/\eta_n\). They consequently fix \(\eta_n\equiv1\) in their numerical study and state that the simulations can be rescaled if necessary.

Elaydi and Sacker study periodically forced Beverton-Holt population equations and show that periodic environmental quantities such as carrying capacities can change the attracting periodic population and its average. Their result is consistent with the distinction made here between a linear threshold and finite-density seasonal dynamics, but it does not identify the algebraic error in this mosquito model.

Bilgin and Kulenović survey and analyze discrete single-species population models, including a Beverton-Holt model with periodic environment. Their periodic-environment section likewise treats the periodic carrying-capacity profile as dynamically meaningful rather than removable by a phasewise state scaling. It does not contain the source-specific transformed equation or the exact two-season counterexample above.

## Limitations

The correction does not invalidate the source's figure computed under the explicitly constant choice
\[
\eta_n\equiv1.
\]
It also does not invalidate the threshold criterion involving \(\alpha\).

The result does not provide a complete sensitivity theory for arbitrary seasonal \(\eta_n\). It establishes the exact transformed recurrence, characterizes when the source's normalization is valid, and supplies an exact counterexample showing why simulations with constant \(\eta\) cannot generally be transferred to a nonconstant periodic profile by pointwise rescaling.

## References

1. X. Wang, Y. Gu, J. Wang, F. Liao, B. Zheng, “Periodic solutions and stability of a discrete mosquito population model with periodic parameters,” Discrete and Continuous Dynamical Systems - B 29 (2024), 4481–4491. DOI: 10.3934/dcdsb.2024051. Early access 8 April 2024.
2. S. Elaydi, R. J. Sacker, “Periodic difference equations, population biology and the Cushing-Henson conjectures,” Mathematical Biosciences 201 (2006), 195–207. DOI: 10.1016/j.mbs.2005.12.021.
3. A. Bilgin, M. R. S. Kulenović, “Global Asymptotic Stability for Discrete Single Species Population Models,” Discrete Dynamics in Nature and Society (2017), Article 5963594. DOI: 10.1155/2017/5963594.
