# Exact two-point normal \(L^2\)-Cartesian radius and its singular phase crossover

## Finding

**Theorem.** Let \(T\) be a bounded normal operator on a nonzero complex Hilbert space whose spectrum is contained in the two-point set \(\{\lambda,\mu\}\subset\mathbb C\). The \(L^2\)-Cartesian numerical radius is
\[
\omega_2(T)^2=\frac1{2\pi}\int_0^{2\pi}
\|\operatorname{Re}(e^{-it}T)\|^2\,dt.
\]
Assume both spectral points occur (so \(\sigma(T)=\{\lambda,\mu\}\)); the one-point specialization follows by setting them equal. Define
\[
R=\max\{|\lambda|,|\mu|\},\qquad
A=\frac{\big||\lambda|^2-|\mu|^2\big|}{2},\qquad
U=|\operatorname{Im}(\overline\lambda\mu)|.
\]
Then the **exact nonunitary two-spectral law** is
\[
\boxed{\omega_2(T)^2=\frac{R^2}{2}+\frac{U-A\arctan(U/A)}{\pi}.}\tag{1}
\]
Here \(A\arctan(U/A)\) is defined to be zero when \(A=0\); if \(A=U=0\), the entire correction is zero. Formula (1) is valid when one or both spectral points are zero, by continuity and directly from the integrand.

For fixed positive spectral moduli \(r=|\lambda|\) and \(s=|\mu|\), write the relative phase \(\delta=\arg\mu-\arg\lambda\). Then the squared radius is minimized exactly when \(\delta\equiv0\pmod\pi\), and maximized exactly when \(\delta\equiv\pi/2\pmod\pi\). The maximum is obtained in (1) by substituting \(U=rs\), and the minimum is \(R^2/2\). Consequently, for every nonzero normal operator with at most two spectral points,
\[
\boxed{\frac{\|T\|^2}{2}\le\omega_2(T)^2
\le\left(\frac12+\frac1\pi\right)\|T\|^2.}\tag{2}
\]
Equality on the left holds exactly when \(\operatorname{Im}(\overline\lambda\mu)=0\). Equality on the right holds exactly when \(\lambda,\mu\ne0\), \(|\lambda|=|\mu|\), and \(|\sin\delta|=1\). Thus the upper bound is sharp, attained by \(\operatorname{diag}(1,i)\), and excludes all genuinely unequal-radius spectra.

**Sharp singular phase transition.** For fixed \(0<s<r\), and \(\delta\to0\),
\[
\boxed{\omega_2(T)^2-\frac{r^2}{2}
=\frac{4r^3s^3}{3\pi(r^2-s^2)^2}|\delta|^3
+O_{r,s}(|\delta|^5).}\tag{3}
\]
At equal nonzero moduli \(r=s=\rho\), instead,
\[
\boxed{\omega_2(T)^2-\frac{\rho^2}{2}
=\frac{\rho^2}{\pi}|\sin\delta|
=\frac{\rho^2}{\pi}|\delta|+O_\rho(|\delta|^3).}\tag{4}
\]
The crossover is exact: when \(A,U>0\) and \(x=U/A\), the excess above \(R^2/2\) equals
\[
\frac U\pi\left(1-\frac{\arctan x}{x}\right).
\]
The profile in parentheses is asymptotic to \(x^2/3\) for small \(x\) and tends to one as \(x\to\infty\). Hence, at aligned phases, the squared radius as a function of relative phase is twice continuously differentiable but not three times differentiable when \(0<s<r\), whereas at equal positive moduli it is Lipschitz but not once differentiable. This is a sharp regularity transition, not merely a change of Taylor coefficient.

## Assumptions and scope

The operator norm and real part are those of a complex Hilbert space. The spectral points may have arbitrary multiplicity, finite or infinite. For a genuinely two-point normal spectrum, the spectral theorem gives \(T=\lambda P+\mu(I-P)\) with nonzero orthogonal spectral projections, and consequently
\[
\|\operatorname{Re}(e^{-it}T)\|^2
=\max\{\operatorname{Re}(e^{-it}\lambda)^2,
\operatorname{Re}(e^{-it}\mu)^2\}.
\]
The one-point and zero-operator cases are included by the evident specialization of (1). In phase statements requiring arguments, both spectral moduli are positive. Equations (3) and (4) concern spectral-phase perturbations at fixed moduli, not perturbations of arbitrary nonnormal operators. No assertion about more than two distinct spectral points is made.

## Proof

**Exact integral.** By invariance under common scalar phase, write \(\lambda=r>0\), \(\mu=s e^{i\delta}\), with \(r\ge s\ge0\); the zero case is immediate. Define
\[
a(t)=r^2\cos^2t,\qquad b(t)=s^2\cos^2(t-\delta).
\]
Since \(\max(a,b)=a+(b-a)_+\), the constant contribution to the angular mean is \(r^2/2\). Put \(A=(r^2-s^2)/2\ge0\) and \(U=rs|\sin\delta|\). Double-angle identities show that the difference is a shifted cosine:
\[
b(t)-a(t)=-A+B\cos(2t-\phi),\qquad
B=\frac12|s^2e^{-2i\delta}-r^2|=\sqrt{A^2+U^2},
\]
for an immaterial real shift \(\phi\). If \(U>0\) and \(A>0\), put \(\beta=\arccos(A/B)=\arctan(U/A)\), so \(0<\beta<\pi/2\) and \(B\sin\beta=U\). Angular averaging eliminates \(\phi\), and a single positive-cosine arc gives
\[
\begin{aligned}
\frac1{2\pi}\int_0^{2\pi}(b(t)-a(t))_+\,dt
&=\frac1{2\pi}\int_{-\beta}^{\beta}(B\cos v-A)\,dv\\
&=\frac{B\sin\beta-A\beta}{\pi}
=\frac{U-A\arctan(U/A)}{\pi}.
\end{aligned}
\]
This proves (1). If \(A=0\), the same integral has \(\beta=\pi/2\) and equals \(U/\pi\). If \(U=0\), then \(B=A\) and the positive part vanishes; (1) follows directly. All simultaneous-zero cases are therefore covered.

**Exact extrema and equality.** The correction \(f_A(U)=U-A\arctan(U/A)\) is nonnegative, and for \(A>0\) has derivative \(U^2/(A^2+U^2)>0\) whenever \(U>0\); for \(A=0\), it is simply \(U\). Because \(U=rs|\sin\delta|\), the asserted phase minimizers and maximizers follow for \(r,s>0\). The left equality in (2) is exactly \(U=0\). For the upper bound, fix the dominant modulus \(R=r\). The angular integrand is pointwise nondecreasing as \(s\) grows to \(r\), so its mean is at most the equal-modulus mean, which by (1) is \(r^2(1/2+|\sin\delta|/\pi)\). This is at most \(r^2(1/2+1/\pi)\). If \(|\sin\delta|>0\) and \(s<r\), there is an open set of angles near a zero of \(r\cos t\) where the smaller term is the maximum, so increasing \(s\) strictly increases the mean. Thus upper equality requires \(s=r\) and \(|\sin\delta|=1\), and these conditions suffice. The zero-eigenvalue cases are strict at the upper bound unless \(T=0\), which is excluded there.

**Singular crossover.** For fixed \(A>0\), Taylor expansion of \(\arctan(U/A)\) at zero gives
\[
f_A(U)=\frac{U^3}{3A^2}-\frac{U^5}{5A^4}+O_A(U^7).
\]
Since \(U=rs|\sin\delta|=rs|\delta|+O_{r,s}(|\delta|^3)\), substitution with \(A=(r^2-s^2)/2\) yields (3) with its stated remainder. If \(r=s=\rho\), \(A=0\) identically, so the exact correction is \(U/\pi=\rho^2|\sin\delta|/\pi\), proving (4). Factoring \(U\) from the exact correction gives the crossover profile and its two limiting behaviors. \(\square\)

## Verification

The proof uses only the spectral theorem for normal operators, elementary trigonometric identities, positive-part integration and Taylor series with explicitly fixed parameters. All branch and degeneracy cases \(A=0\), \(U=0\), and zero eigenvalues are treated. As a supplementary finite check, `verify_two_spectrum.py` evaluates angular midpoint quadrature for 216 specified and seeded complex spectral pairs; each agreed with (1) to the recorded tolerance, with maximal absolute discrepancy below \(1.7\cdot10^{-7}\). Quadrature is not a proof of the all-dimensional statements. The exact proof does not require the checker or any external certificate.

## Relationship to prior work

Audeh, Moradi and Sahoo introduced \(\omega_2\) and gave general bounds; their Theorem 17 bounds \(\omega_2\) for commuting Cartesian parts (normal operators) but does not compute the dependence on both nonunitary eigenvalue radii and their relative phase. The public result *Exact projective spectral-gap formula and optimal finite spectra for the \(L^2\)-Cartesian radius of unitaries* gives the equal-radius unitary subcase, including its optimal two-point upper bound; hence that special case and the upper constant by itself are not claimed new. The public result *Exact rank-one overlap profile for the \(L^2\)-Cartesian numerical radius* includes the normal rank-one endpoint with a zero eigenvalue; it does not supply the interior positive-unequal-radii profile. A separate public cubic-stability theorem bounds deviations from phase-self-adjoint operators but does not give (1) or its exact unequal-radii coefficient. The new contribution is the complete two-point **nonunitary** formula and the exact cubic/linear crossover at spectral radial equality.

## Limitations

The result is specific to normal operators with at most two spectral values and the second angular moment. It does not compute the radius for three-point or continuous spectra or for nonnormal operators. The sharp upper constant is already implied by the published unitary special case together with radial domination, and is included for completeness, not claimed independently original. The elementary trigonometric integral may have appeared in older convex-support or width-moment literature under another name; the searched literature did not establish historical priority. The analytical conclusion is not independently audited.

## References

1. W. Audeh, H. R. Moradi, S. Sahoo, *The \(L^2\)-Cartesian Numerical Radius of Hilbert Space Operators*, arXiv:2610.04844v1, first publicly available 2026-10-04, especially Theorem 17. https://arxiv.org/html/2610.04844v1
2. *Exact projective spectral-gap formula and optimal finite spectra for the \(L^2\)-Cartesian radius of unitaries*, public mathematical research record (2026), complete theorem and proof inspected.
3. *Exact rank-one overlap profile for the \(L^2\)-Cartesian numerical radius*, public mathematical research record (2026), complete theorem and proof inspected.
4. *Cubic operator-norm stability for the \(L^2\)-Cartesian numerical radius*, public mathematical research record (2026), complete theorem and proof inspected.
5. Standard spectral theorem and elementary calculus of trigonometric integrals.
