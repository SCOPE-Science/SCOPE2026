# Positive trace-class Bergman-to-Fock disk scaling and its sharp spectral staircase

## Finding

The weak Bergman-to-Fock limit for expanding Gaussian scales admits an exact, positive trace-class error for radial balls in every complex dimension. More precisely, fix an integer \(d\ge1\), a ball-size parameter \(t>0\), and a weight \(s>t\). Identify the normalized monomial bases of the weighted Bergman space on the unit ball and the Bargmann–Fock space on \(\mathbb C^d\) by the unitary \(U_s\) specified below. If \(T_{s,t}\) is Bergman Toeplitz localization on \(\{|z|^2<t/s\}\) and \(T_{\infty,t}\) is Fock Toeplitz localization on \(\{|w|^2<t\}\), then

\[
\Delta_{s,t}:=U_sT_{s,t}U_s^*-T_{\infty,t}\ge0
\]

and, **exactly for every** \(s>t\),

\[
\boxed{\|\Delta_{s,t}\|_{\mathcal S_1}=\frac{t^d}{d!}\left[\frac{\prod_{j=1}^{d}(s+j)}{(s-t)^d}-1\right].}
\]

There is a positive trace-class operator \(D_{d,t}\) such that

\[
\boxed{\lim_{s\to\infty}\|s\Delta_{s,t}-D_{d,t}\|_{\mathcal S_1}=0.}
\]

On each Fock homogeneous polynomial subspace of total degree \(k\ge0\), the limit operator acts by the scalar

\[
\boxed{a_{k,d}(t)=\frac{e^{-t}t^{k+d}(k+d+1+t)}{2(k+d-1)!}.}
\]

Thus the exact first-order trace and sharp operator-norm constants are

\[
\operatorname{tr}D_{d,t}=\frac{t^d}{d!}\left[\frac{d(d+1)}2+dt\right],\qquad
\lim_{s\to\infty}s\|\Delta_{s,t}\|_{\mathrm{op}}=\max_{k\ge0}a_{k,d}(t).
\]

The degree attaining the sharp operator-norm coefficient follows an explicit staircase. It switches between degrees \(k\) and \(k+1\) precisely at

\[
\boxed{t_k=\sqrt{1+(k+d)(k+d+1)}-1,\qquad k=0,1,\ldots.}
\]

For \(0<t<t_0\) the unique maximizing degree is zero; for \(t_{k-1}<t<t_k\), \(k\ge1\), it is \(k\); at \(t=t_k\), and only there, both degrees \(k\) and \(k+1\) maximize.

For example, with \(d=t=1\), the leading error on constants is \(3/(2e)\), whereas the leading error on linear functions is \(2/e\); thus the worst perturbative eigenmode is degree one even though both individual disk-localization operators attain their norms on constants.

## Assumptions and scope

Let \(\mathbb B_d=\{z\in\mathbb C^d:|z|<1\}\). The Bergman Hilbert space \(A_s^2(\mathbb B_d)\), \(s>-1\), has the normalized measure

\[
d\mu_{s,d}(z)=\frac{\Gamma(s+d+1)}{\pi^d\Gamma(s+1)}(1-|z|^2)^s\,dV(z).
\]

The Fock space \(\mathcal F_d^2\) has the normalized Gaussian measure \(\pi^{-d}e^{-|w|^2}\,dV(w)\). In either space, the Toeplitz operator with bounded radial symbol \(\phi\) is defined by its form \(\langle T_\phi f,g\rangle=\int\phi f\overline g\,d\mu\). The coordinate monomials \(z^\alpha\), with \(\alpha\in\mathbb N_0^d\), form orthogonal bases. Denote their normalized vectors by \(e_{s,\alpha}\) and \(e_{\infty,\alpha}\). The canonical *degree-preserving* unitary is \(U_se_{s,\alpha}=e_{\infty,\alpha}\). The comparison therefore takes place on a single specified Hilbert space, not through an implicit identification of differently weighted functions.

The claim is for every integer \(d\ge1\), every \(t>0\), and every real \(s>t\). All trace-class limits keep \(d,t\) fixed while \(s\to\infty\). The trace-class error is positive and strictly nonzero for \(t>0\).

## Proof

**1. The entire radial spectra.** Rotational invariance, orthogonality, and the beta integral show that for every multi-index of total degree \(k\), the eigenvalues of the two Toeplitz localizers are respectively

\[
b_{k,d,s}(t)=\frac{\int_0^{t/s}v^{k+d-1}(1-v)^s\,dv}{B(k+d,s+1)},\quad
f_{k,d}(t)=\frac{\int_0^t y^{k+d-1}e^{-y}\,dy}{\Gamma(k+d)}.
\]

These are the distribution functions of \(sX\) with \(X\sim\mathrm{Beta}(k+d,s+1)\), and of \(Y\sim\mathrm{Gamma}(k+d,1)\). Each total degree \(k\) has multiplicity \(\binom{k+d-1}{d-1}\).

**2. Strict spectral domination.** For each \(m=k+d\), the density ratio of \(sX\) to \(Y\) on \((0,s)\) is a positive constant times \(e^y(1-y/s)^s\). Its logarithmic derivative is \(-y/(s-y)<0\), and the ratio vanishes for \(y\ge s\). Since the two densities each integrate to one, the monotone-likelihood-ratio crossing argument gives \(b_{k,d,s}(t)>f_{k,d}(t)\) for \(0<t<s\). Hence \(\Delta_{s,t}\ge0\).

**3. Exact trace.** The diagonal reproducing kernel of \(A_s^2(\mathbb B_d)\) equals \((1-|z|^2)^{-s-d-1}\). Positivity and Tonelli's theorem imply

\[
\begin{aligned}
\operatorname{tr}T_{s,t}
&=\frac{\Gamma(s+d+1)}{\Gamma(s+1)(d-1)!}
\int_0^{t/s}\frac{v^{d-1}}{(1-v)^{d+1}}\,dv\\
&=\frac{\prod_{j=1}^d(s+j)}{d!}\left(\frac{t}{s-t}\right)^d.
\end{aligned}
\]

The Fock diagonal kernel is \(e^{|w|^2}\), and therefore \(\operatorname{tr}T_{\infty,t}=t^d/d!\). Their positive difference is trace-class, and subtraction proves the exact trace-norm formula.

**4. The complete first-order operator, not just pointwise eigenvalue convergence.** With \(m=k+d\) fixed, the density of \(sX\) is

\[
\frac{y^{m-1}e^{-y}}{\Gamma(m)}
\left[1+\frac{m(m+1)-y^2}{2s}+O_{m,t}(s^{-2})\right],\qquad 0\le y\le t.
\]

The expansion uses \(\Gamma(s+m+1)/(s^m\Gamma(s+1))=1+m(m+1)/(2s)+O_m(s^{-2})\) and \((1-y/s)^s=e^{-y}[1-y^2/(2s)+O_t(s^{-2})]\). Integrating the first-order term and applying the gamma recurrence gives

\[
\lim_{s\to\infty}s\bigl(b_{k,d,s}(t)-f_{k,d}(t)\bigr)
=\frac{m(m+1)}2\bigl(F_m(t)-F_{m+2}(t)\bigr)
=a_{k,d}(t),
\]

where \(F_j(t)=\Gamma(j)^{-1}\int_0^t y^{j-1}e^{-y}\,dy\). The limit coefficients are positive. Summation with multiplicities and the exponential series yields

\[
\sum_{k\ge0}\binom{k+d-1}{d-1}a_{k,d}(t)
=\frac{t^d}{d!}\left[\frac{d(d+1)}2+dt\right].
\]

By the exact trace formula the same number is \(\lim_{s\to\infty}s\operatorname{tr}\Delta_{s,t}\). Since all the diagonal coefficients are nonnegative, the discrete Scheffé lemma (or splitting the sum at a finite degree and using equality of the limiting sums) upgrades pointwise convergence to \(\mathcal S_1\)-convergence. This step controls all degrees, not just fixed-degree truncations.

**5. Exact maximizing-degree transitions.** The ratio of consecutive positive limit eigenvalues is

\[
\frac{a_{k+1,d}(t)}{a_{k,d}(t)}
=\frac{t(k+d+2+t)}{(k+d)(k+d+1+t)}.
\]

It exceeds one exactly when \(t(t+2)>(k+d)(k+d+1)\). As the right-hand side is strictly increasing with \(k\), there is a single peak, with a tie only at \(t_k\). Trace-class convergence implies operator-norm convergence of \(s\Delta_{s,t}\), proving the stated sharp norm constant and its degree staircase.

## Verification

The accompanying `VERIFY.py` evaluates the normalized incomplete-beta and incomplete-gamma eigenvalues, compares their weighted sums with the exact trace formula in dimensions one through four, checks nonnegative differences, tests the first-order trace-class coefficient numerically, and verifies consecutive-degree equality at transition parameters. Run with `python VERIFY.py` in an environment containing Python 3, NumPy, and SciPy. The program tests 52 configurations. These finite computations are supplementary; the analytic proof above establishes all dimensions and parameters.

## Relationship to prior work

Ma, Yan, Zheng and Zhu (2026) establish a general weak localization-operator convergence from weighted Bergman to Fock spaces, and in Theorem 4.5 prove sharp disk-symbol operator-norm convergence in one complex dimension. Their proof already displays the one-dimensional incomplete-gamma and incomplete-beta spectral integrals; these are acknowledged as prior spectral formulas, not rediscovered here. The present result is the *positive difference* of the two **canonically identified** localizers, its all-dimensional **exact trace-class error**, the whole first-order **trace-class operator**, and its **sharp operator-norm staircase**. Those conclusions are not stated by Theorems 1.3, 4.5 or 4.6 in the inspected original manuscript.

Esmeral and Paternina Montalvo (2025) characterize radial Toeplitz forms in weighted disk Bergman spaces, including the known radial spectral diagonalization. Gröchenig and Ortega-Cerdà (2022) use incomplete-gamma spectra for finite-dimensional Fock polynomial sampling. Neither studied the weighted-Bergman/Fock difference or its first-order positive trace-class law. These sources establish important inputs and context rather than excluding all possible historical priority.

## Limitations

Only characteristic functions of *centered Euclidean balls* are treated; no general nonradial-symbol or non-ball trace-class comparison follows. The quantitative limit fixes dimension and ball size; no simultaneous limit with \(d\) or \(t\) increasing is claimed. The unitary comparison depends on the specified normalized-monomial identification. The result does not imply global trace-class convergence for arbitrary localization symbols. The spectral beta/gamma formulas are established prior facts. Unindexed equivalent first-order statements may exist; there has been no independent audit.

## References

1. P. Ma, F. Yan, D. Zheng and K. Zhu, *Localization operators on Bergman and Fock spaces*, arXiv:2603.04051v1 (first publicly available March 4, 2026), especially Sections 2 and 4, Theorem 4.5 and equations (4.17)–(4.20). https://arxiv.org/html/2603.04051
2. K. Esmeral and A. E. Paternina Montalvo, *Radial Toeplitz Forms on the Weighted Bergman Space over the Unit Disk*, Journal of Mathematical Sciences, first online May 9, 2025. https://doi.org/10.1007/s10958-025-07728-x
3. K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz-Zygmund inequalities for polynomials in Fock space*, Mathematische Zeitschrift (2022), especially Sections 2–3. https://doi.org/10.1007/s00209-022-03087-4
4. W. Bauer and R. Fulsche, *Berger-Coburn theorem, localized operators, and the Toeplitz algebra*, arXiv:1905.12246, for broader Bergman/Fock operator context. https://arxiv.org/html/1905.12246v2
