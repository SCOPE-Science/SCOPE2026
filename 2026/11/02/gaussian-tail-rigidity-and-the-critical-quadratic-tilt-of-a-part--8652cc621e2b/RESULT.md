# Gaussian-tail rigidity and the critical quadratic tilt of a partially reset harmonic diffusion

## Finding

A particle diffusing in a harmonic well and undergoing Poisson resets that contract its current position has a sharply controlled stationary upper tail. For every contraction strength strictly below unity, the exact process retains a Gaussian far tail with a rate-dependent algebraic prefactor, even though its commonly used second-order frequent-weak-reset diffusion approximation has a power-law stationary tail. The Gaussian critical exponential tilt is finite precisely above a sharp reset-rate threshold.

Let \(\sigma^2=D/\kappa\), \(\beta=r/(2\kappa)\), and
\[
P(a,\beta)=\prod_{j=1}^{\infty}\left(1-\frac{\beta a^{2j}}{j+\beta}\right)^{-1}.
\]
The infinite product converges to a finite positive value for each fixed \(0\le a<1\). The stationary density \(p\) satisfies the exact equivalent
\[
p(x)\sim\frac{\Gamma(1+\beta)P(a,\beta)}{\sqrt{2\pi}\,\sigma}
\left(\frac{2\sigma^2}{x^2}\right)^{\beta}
\exp\left(-\frac{x^2}{2\sigma^2}\right),\qquad |x|\to\infty.
\]
For all integers \(n\ge1\) its even moments are
\[
\mathbb E[X^{2n}]=\frac{(2n)!D^n}{\prod_{j=1}^n[2j\kappa+r(1-a^{2j})]},
\]
and consequently
\[
\frac{\mathbb E[X^{2n}]}{(2n-1)!!\sigma^{2n}}
\sim\Gamma(1+\beta)P(a,\beta)n^{-\beta}.
\]
Finally, the sharp quadratic-moment boundary is
\[
\mathbb E[e^{\theta X^2}]<\infty\quad\Longleftrightarrow\quad
\theta<\frac1{2\sigma^2}\ \text{or}\ 
\left(\theta=\frac1{2\sigma^2}\text{ and }r>\kappa\right).
\]
The statement includes negative \(\theta\). Values greater than the displayed boundary produce an infinite expectation.

## Assumptions and scope

Fix \(\kappa,D,r>0\) and a deterministic contraction factor \(a\in[0,1)\). Between jumps, the process solves
\[
dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dB_t.
\]
An independent rate-\(r\) Poisson clock replaces \(X_t\) by \(aX_{t-}\) at each jump. Resetting does not replace the state by an independent sample and does not change the well or diffusion noise. The displayed law is the continuous-time stationary marginal, not merely the distribution immediately after reset events. The case \(a=1\) is deliberately excluded: resets then have no effect and the invariant law is the ordinary Gaussian of variance \(\sigma^2\). All limits in \(|x|\) or moment order hold with other parameters fixed; no uniformity as \(a\uparrow1\) is asserted.

## Proof

**1. Construction and uniqueness.** Two solutions sharing noise and reset times satisfy
\[
|X_t-Y_t|=e^{-\kappa t}a^{N_t}|X_0-Y_0|.
\]
Thus synchronous coupling contracts distances. A bilateral Brownian/Poisson construction from the infinite past gives the unique invariant law. Conditional on the Poisson path the invariant position is centered Gaussian with random variance
\[
V=2D\int_0^\infty e^{-2\kappa t}a^{2N_t}\,dt,
\qquad 0<V<\sigma^2\quad\text{almost surely}.
\]
The strict bounds follow from \(D>0\), a positive first Poisson age, and \(a<1\). In particular, \(X\mid V\sim N(0,V)\), so \(X\) has a positive symmetric density and all polynomial moments are finite.

**2. The endpoint perpetuity.** Let \(T\) be the time since the last Poisson mark in the bilateral stationary construction. By memorylessness, \(T\sim\mathrm{Exp}(r)\) is independent of an earlier copy \(V'\) of the stationary variance. Splitting the integral at that mark yields
\[
V=\sigma^2(1-e^{-2\kappa T})+a^2e^{-2\kappa T}V'.
\]
Set \(U=e^{-2\kappa T}\). Then \(U\) has density \(\beta u^{\beta-1}\) on \((0,1)\). Define
\[
\Delta=\sigma^2-V=UW,\qquad W=\sigma^2-a^2V',
\]
where \(U\) and \(W\) are independent and
\[
\sigma^2(1-a^2)\le W\le\sigma^2.
\]
For every \(0<z\le\sigma^2(1-a^2)\), the endpoint deficit obeys the **exact**, not merely asymptotic, law
\[
\Pr(\Delta\le z)=z^\beta\,\mathbb E[W^{-\beta}].
\]
This follows by conditioning on \(W\) and using \(\Pr(U\le u)=u^\beta\).

**3. Exact moments and normalization of the edge coefficient.** The generator on monomials is
\[
\mathcal L(x^{2n})=-[2n\kappa+r(1-a^{2n})]x^{2n}
+2n(2n-1)Dx^{2n-2}.
\]
All monomials are integrable because \(V\le\sigma^2\). Integrating this identity in the invariant law and iterating from \(\mathbb E[X^0]=1\) proves the stated even moments. Dividing by centered Gaussian moments gives the finite product
\[
A_n:=\frac{\mathbb E[X^{2n}]}{(2n-1)!!\sigma^{2n}}
=\frac{\Gamma(n+1)\Gamma(1+\beta)}{\Gamma(n+1+\beta)}
\prod_{j=1}^n\left(1-\frac{\beta a^{2j}}{j+\beta}\right)^{-1}.
\]
Absolute convergence of the logarithmic correction follows from \(a<1\); the Gamma ratio is asymptotic to \(n^{-\beta}\). Hence \(A_n\sim\Gamma(1+\beta)P(a,\beta)n^{-\beta}\).

An independent derivation conditions on \(W\) in the perpetuity:
\[
A_n=\mathbb E[(V/\sigma^2)^n]
=\mathbb E\!\left[\beta\int_0^1u^{\beta-1}
\bigl(1-uW/\sigma^2\bigr)^n\,du\right].
\]
With \(t=nuW/\sigma^2\), dominated convergence, uniformly over the displayed compact interval for \(W\), gives
\[
\lim_{n\to\infty}n^\beta A_n
=\Gamma(1+\beta)\mathbb E[(\sigma^2/W)^\beta].
\]
Comparison with the exact product therefore identifies
\[
\boxed{\mathbb E[(\sigma^2/W)^\beta]=P(a,\beta)}.
\]
This proves the exact product amplitude is the physical endpoint-variance coefficient; it is not an arbitrary normalization.

**4. Sharp Gaussian density tail.** The Gaussian-mixture density is
\[
p(x)=\mathbb E\left[(2\pi V)^{-1/2}e^{-x^2/(2V)}\right].
\]
Put \(z=x^2/(2\sigma^2)\) and insert \(V=\sigma^2-UW\). At fixed \(W\), rescale \(u\) by \(t=zuW/\sigma^2\) in the Beta integral. The factor from the Gaussian exponent converges to \(e^{-t}\), and the square-root prefactor converges to one. Its integrable domination follows from \(W/\sigma^2\in[1-a^2,1]\) and the exponential suppression as \(uW/\sigma^2\to1\). Consequently
\[
\lim_{z\to\infty}z^\beta\frac{p(x)}{e^{-z}/(\sqrt{2\pi}\sigma)}
=\Gamma(1+\beta)\mathbb E[(\sigma^2/W)^\beta]
=\Gamma(1+\beta)P(a,\beta).
\]
This is precisely the stated two-sided density asymptotic. It also shows the leading exponential rate is the unreset equilibrium variance for every fixed \(a<1\).

**5. Quadratic exponential threshold.** Conditional Gaussian integration gives
\[
\mathbb E[e^{\theta X^2}\mid V]
=(1-2\theta V)^{-1/2}
\]
whenever \(2\theta V<1\), and an infinite conditional expectation otherwise for positive \(\theta\). Since \(0<V<\sigma^2\), finiteness is uniform below \(\theta_c=1/(2\sigma^2)\). Above that threshold, \(V\) exceeds \(1/(2\theta)\) with positive probability (an arbitrarily long reset-free interval), giving divergence. Exactly at \(\theta_c\),
\[
\mathbb E[e^{X^2/(2\sigma^2)}]
=\mathbb E[(\sigma^2/\Delta)^{1/2}]
=\mathbb E[U^{-1/2}]\,\mathbb E[(\sigma^2/W)^{1/2}].
\]
The second factor is finite and bounded between one and \((1-a^2)^{-1/2}\). The first factor equals \(\beta/(\beta-1/2)\) if \(\beta>1/2\), and diverges otherwise. Thus the critical transform is finite exactly when \(r>\kappa\), as claimed. At the threshold its precise finite value is the displayed factorization.

**6. Comparison with the weak-reset diffusion equation.** In the linear example of Galla [1], take \(f(x)=-\kappa x\), proportional resets \(x\mapsto(1-s)x\), and \(r=\lambda/s\) for \(s>0\). The second-order truncated Fokker–Planck equation has drift \(-(\kappa+\lambda)x\) and diffusion coefficient \(2D+\lambda s x^2\). Its zero-flux stationary solution is
\[
p_{\rm diff}(x)\propto(2D+\lambda s x^2)^{-1-(\kappa+\lambda)/(\lambda s)}.
\]
For every fixed \(s>0\) its polynomial moment of absolute order \(q\ge0\) is finite only if
\[
q<1+\frac{2(\kappa+\lambda)}{\lambda s},
\]
whereas the original Poisson-contraction process has all polynomial moments and the sharp Gaussian tail just established. This is a nonuniformity in arbitrarily high moments and far tails at fixed \(s\); it does not assert that the approximation is invalid at fixed \(x\) in the intended frequent-weak-reset limit.

## Verification

Run the standalone program with `python3 verify.py` (Python standard library only). It checks the stationary generator recurrence with exact rational arithmetic, Gamma/product high-moment asymptotics, independent seeded simulations of the variance perpetuity, the special-case complete-reset mixture-density asymptotics by numerical quadrature, and the endpoint Beta-moment identity. The bounded replay passed **54 checks**. These numerical checks supplement, but do not replace, the infinite-quantifier proofs above. The full stationary density is a variance mixture, not an elementary closed form.

## Relationship to prior work

Galla [1] derives the second-order frequent-weak-reset Fokker–Planck model and its stationary power-law profile. That approximate profile is not asserted there to be a global far-tail equivalent for the original jump process; the present comparison explicitly respects its limited asymptotic regime. Olsen and Gupta [2] analyze partial resetting in a background harmonic potential and give the stationary second moment and work rate, which are acknowledged as prior information. The special case \(n=1\) of the present moment formula is therefore not new. Biroli et al. [3] derive stationary exponential tails for partial resets during **free** Brownian motion, a distinct unconfined model, and identify adding a confining potential as a separate direction. Tal-Friedman et al. [4] similarly study free diffusion and drift with rescaling resets. Olsen [5] treats resets **to independently drawn random positions** in a harmonic potential; that renewal property does not hold for resets depending on the current state. The contribution assessed here is the exact sharp Gaussian-edge prefactor, full high-moment decay law and critical quadratic exponential-moment boundary for instantaneous proportional resets in the harmonic well, together with their controlled comparison to the diffusion approximation.

## Limitations

The theorem concerns a one-dimensional linear harmonic drift, constant Brownian diffusivity, independent Poisson reset times, and deterministic contractions \(0\le a<1\); other potentials, renewal clocks and random contraction factors are not covered. The stated asymptotics are not uniform in the limits of no reset \(a\uparrow1\), vanishing reset intensity or simultaneous far-tail and weak-reset scaling. The sampled numerical checks are finite and cannot certify asymptotic claims on their own. Similar endpoint arguments may exist in general perpetuity and Gaussian variance-mixture literature; the literature comparison supports a qualified research originality assessment rather than certified publication priority. Independent validation has not been performed.

## References

[1] Tobias Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635 (first posted 25 February 2026), https://arxiv.org/html/2602.21635; particularly supplemental §S1.1.

[2] Kristian Stølevik Olsen and Deepak Gupta, *Thermodynamic work of partial resetting*, arXiv:2401.11919 (2024), https://arxiv.org/abs/2401.11919; §§III.C and IV.B.

[3] Marco Biroli, Yannick Feld, Alexander K. Hartmann, Satya N. Majumdar and Grégory Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387 (2024), https://arxiv.org/abs/2406.08387.

[4] Ofir Tal-Friedman, Yael Roichman and Shlomi Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363 (2022), https://arxiv.org/abs/2205.03363.

[5] Kristian Stølevik Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (2023), https://arxiv.org/abs/2310.04840.
