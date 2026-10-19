# Exact spherical-edge mass and thermal leakage for an isotropic trapped run-and-tumble particle

## Finding

Consider the isotropic run-and-tumble particle in a harmonic trap, with tumble rate \(\gamma\), trap rate \(\mu\), speed \(v_0\), and spatial dimension \(d\ge2\). Write \(\alpha=\gamma/\mu>0\) and \(r_0=v_0/\mu\). At stationarity without thermal noise, let \(R=\|\mathbf r\|/r_0\). Define
\[
 C_{d,\alpha}=\exp\!\left\{\frac{\alpha}{2}\left[\psi\!\left(\frac d2\right)-\psi\!\left(\frac{d-1}{2}\right)\right]\right\},
\]
where \(\psi\) is the digamma function. Then, for each fixed integer \(d\ge2\) and real \(\alpha>0\),
\[
 \boxed{\Pr\{R>1-\varepsilon\}\sim C_{d,\alpha}\varepsilon^\alpha\quad(\varepsilon\downarrow0).}
\]
For independent thermal Brownian diffusion with coefficient \(D>0\), write \(\mathbf r_D\) for a stationary particle position and \(\sigma=\sqrt{D\mu}/v_0\). For every fixed real \(u\), as \(\sigma\downarrow0\),
\[
 \boxed{\Pr\{\|\mathbf r_D\|>r_0(1+u\sigma)\}\sim C_{d,\alpha}\sigma^\alpha H_\alpha(u),\qquad H_\alpha(u)=\alpha\int_0^\infty t^{\alpha-1}\overline\Phi(u+t)\,dt.}
\]
Here \(\overline\Phi(s)=\Pr\{Z>s\}\) is the standard normal upper tail. The relation is uniform for \(u\) in any fixed compact real interval. At the original turning sphere,
\[
 \boxed{\Pr\{\|\mathbf r_D\|>r_0\}\sim C_{d,\alpha}\frac{2^{\alpha/2-1}\Gamma((\alpha+1)/2)}{\sqrt\pi}\left(\frac{D\mu}{v_0^2}\right)^{\alpha/2}.}
\]
For fixed \(\alpha>0\), the coefficient \(C_{d,\alpha}\) decreases strictly as integer dimension \(d\ge2\) increases and tends to \(1\). In dimensions two and three it is respectively \(2^\alpha\) and \((e/2)^\alpha\); these checks agree with the exact low-dimensional radial laws already known in the literature. The contribution is the sharp all-dimensional radial outer-shell asymptotic and complete \(O(\sqrt D)\) Gaussian leakage profile, not the stationary distribution or its Gaussian-convolution representation.

## Assumptions and scope

Fix integer \(d\ge2\), \(v_0,\mu,\gamma>0\). Between tumbles the position obeys \(d\mathbf r/dt=-\mu\mathbf r+v_0\mathbf n(t)\). Orientation is independently resampled from the uniform law on \(S^{d-1}\) at the events of a rate-\(\gamma\) Poisson process. The stationary athermal position exists and has support on the closed ball of radius \(r_0\). If \(D>0\), independent isotropic thermal noise adds \(\sqrt{2D}\,d\mathbf W_t\) to the position equation; there is no orientation-dependent thermal force. The limit \(D\downarrow0\) holds with \(d,\gamma,\mu,v_0,u\) fixed. Neither \(u\to\pm\infty\) simultaneously with \(D\downarrow0\) nor \(d\to\infty\) uniformly is claimed.

The exact stationary Dirichlet-mean representation and the independent Gaussian-convolution representation used below are established for this model in Guéneau, Majumdar and Schehr (2026), cited in References. What is derived here from those representations is the explicit sharp radial-edge coefficient and its thermal boundary layer for all \(d\ge2\).

## Proof

**1. From the stationary process to an isotropic Dirichlet mean.** Rescale time by \(\mu\) and position by \(r_0=v_0/\mu\). The stationary athermal vector admits
\[
 \mathbf X=\sum_{j=1}^\infty P_j\mathbf U_j,
\]
where \(\mathbf U_j\) are independent uniform unit vectors and \((P_j)\) are independent-of-directions GEM stick-breaking masses with concentration \(\alpha\): \(P_j=V_j\prod_{k<j}(1-V_k)\), \(V_j\overset{\mathrm{iid}}\sim\operatorname{Beta}(1,\alpha)\), \(\sum P_j=1\) almost surely. In particular \(\|\mathbf X\|\le1\). For \(|z|<1\), the Dirichlet-mean transform of one coordinate \(X_1\) is
\[
 \mathbb E(1-zX_1)^{-\alpha}=\exp\{-\alpha\mathbb E\log(1-zU_1)\},
\]
where \(U_1\) is the first coordinate of a uniform point on \(S^{d-1}\). This identity also follows from the standard gamma-process normalization: the gamma random measure's Laplace functional factorizes, and integrating its total mass yields the generalized Stieltjes transform. No independence of the coordinates of \(\mathbf X\) is asserted.

**2. Moment coefficients.** Write \(m_n=\mathbb E U_1^{2n}=(1/2)_n/(d/2)_n\), and set \(t=z^2\). Expanding the transform around zero gives
\[
 F(t)=\sum_{n\ge0}b_nt^n=\exp\left(\sum_{n\ge1}a_nt^n\right),\qquad a_n=\frac{\alpha m_n}{2n},\qquad b_n=\frac{(\alpha)_{2n}}{(2n)!}\mathbb E X_1^{2n}.
\]
For \(\beta=(d-1)/2>0\), the gamma ratio yields
\[
 m_n\sim\frac{\Gamma(d/2)}{\sqrt\pi}n^{-\beta},\qquad a_n\sim \frac{\alpha\Gamma(d/2)}{2\sqrt\pi}n^{-1-\beta}.
\]
In particular \(A=\sum_{n\ge1}a_n<\infty\).

**3. Coefficient asymptotic (including the nonstandard convolution step).** If a positive summable sequence obeys \(a_n\sim c n^{-1-\beta}\), \(\beta>0\), then
\[
 [t^n]\exp\left(\sum_{k\ge1}a_kt^k\right)\sim e^{A}a_n.
\]
For completeness, put \(q_n=a_n/A\) and \(q^{*j}\) for the \(j\)-fold convolution. Splitting \(\sum_{k=1}^{n-1}q_kq_{n-k}\) into \(k\le K\), \(K<k<n-K\), and \(k\ge n-K\), first let \(n\to\infty\) then \(K\to\infty\). Regular variation gives the two end sums \(2q_n\); the middle is \(o(q_n)\), bounded by a constant times \(q_n\sum_{k>K}q_k\). Thus \((q*q)_n\sim2q_n\), and induction with the same split gives \(q^{*j}_n\sim j q_n\) for each fixed \(j\). The same split gives \((q*q)_n\le Bq_n\) uniformly in \(n\) for some finite \(B\); convolution induction gives \(q^{*j}_n\le B^{j-1}q_n\), permitting dominated convergence in the factorial series. Therefore
\[
 \sum_{j\ge1}\frac{A^j}{j!}q^{*j}_n\sim q_n\sum_{j\ge1}\frac{jA^j}{j!}=Ae^Aq_n=e^Aa_n,
\]
as claimed.

**4. Exact boundary coefficient.** Since \(U_1\) is symmetric and \(U_1^2\sim\operatorname{Beta}(1/2,\beta)\),
\[
 A=-\alpha\mathbb E\log(1-U_1)
 =-\frac\alpha2\mathbb E\log(1-U_1^2)
 =\frac\alpha2\{\psi(\beta+1/2)-\psi(\beta)\}.
\]
Put \(C_{d,\alpha}=e^A\). Rotational invariance implies \(\mathbb E X_1^{2n}=m_n\mathbb E R^{2n}\), and Step 3 therefore gives
\[
 \mathbb E R^{2n}=\frac{(2n)!\,b_n}{(\alpha)_{2n}m_n}
 \sim C_{d,\alpha}\frac{\alpha}{2n}\frac{\Gamma(2n+1)\Gamma(\alpha)}{\Gamma(2n+\alpha)}
 \sim C_{d,\alpha}\Gamma(\alpha+1)(2n)^{-\alpha}.
\]
By monotonicity the same asymptotic holds for the continuous Mellin parameter \(s\to\infty\): \(\mathbb E R^s\sim C_{d,\alpha}\Gamma(\alpha+1)s^{-\alpha}\). Let \(Y=-\log R\in[0,\infty]\). The Laplace–Stieltjes Tauberian theorem (for monotone distribution functions, \(\alpha>0\)) then yields \(\Pr\{Y\le y\}\sim C_{d,\alpha}y^\alpha\) as \(y\downarrow0\). Because \(Y=-\log R\) and \(1-R=1-e^{-Y}\sim Y\), this is precisely the claimed near-sphere probability. This argument does not require pointwise asymptotics for any radial density.

**5. Thermal convolution and its sharp edge scaling.** The linear trap permits the stationary position to split independently as
\[
 \frac{\mathbf r_D}{r_0}=\mathbf X+\sigma\mathbf Z,\qquad \sigma=\frac{\sqrt{D\mu}}{v_0},\qquad \mathbf Z\sim N(0,I_d).
\]
Write \(\delta=1-R\) and \(\mathbf X=R\mathbf V\), where \(\mathbf V\) is uniform on the sphere and independent of \(R\) (the zero-radius event is immaterial). Step 4 gives \(\Pr(\delta\le h)\sim C_{d,\alpha}h^\alpha\). Consequently the rescaled radial-deficit measures \(\sigma^{-\alpha}\Pr(\delta/\sigma\in dt)\) converge vaguely on \((0,\infty)\) to \(C_{d,\alpha}\alpha t^{\alpha-1}dt\). For every fixed \(u,t\), if \(\delta=\sigma t\), the event
\[
 \|(1-\sigma t)\mathbf V+\sigma\mathbf Z\|>1+u\sigma
\]
converges to \(\mathbf V\cdot\mathbf Z>u+t\), whose probability is \(\overline\Phi(u+t)\). This gives the stated integral when \(t\) remains bounded; the contribution from \(0\le t\le\eta\) is at most \(O(\eta^\alpha)\) after normalization, so the endpoint at \(t=0\) causes no missing mass. For the tail, the triangle inequality makes the event impossible unless \(\delta\le\sigma(\|\mathbf Z\|+|u|)\). The small-deficit bound \(\Pr(\delta\le h)\le Kh^\alpha\) for small \(h\), together with the Gaussian moment bound and the exponentially small tail \(\Pr(\|\mathbf Z\|>c/\sigma)=o(\sigma^\alpha)\), makes the contribution from large \(\|\mathbf Z\|\) uniformly negligible after dividing by \(\sigma^\alpha\). A bounded Gaussian vector gives a bounded \(t\)-window, justifying the exchange. All estimates are uniform when \(u\) ranges over a fixed compact set, giving local uniformity in \(u\).

For \(u=0\), integration by parts or the positive-part moment identity yields
\[
 H_\alpha(0)=\alpha\int_0^\infty t^{\alpha-1}\overline\Phi(t)dt
 =\mathbb E (Z_+)^\alpha
 =\frac{2^{\alpha/2-1}\Gamma((\alpha+1)/2)}{\sqrt\pi}.
\]
Substituting \(\sigma^\alpha=(D\mu/v_0^2)^{\alpha/2}\) proves the explicit leakage asymptotic.

**6. Dimensional ordering.** With \(\beta=(d-1)/2\), the exponent of \(C_{d,\alpha}\) is \((\alpha/2)[\psi(\beta+1/2)-\psi(\beta)]\). Because the trigamma function \(\psi'\) is strictly decreasing on \((0,\infty)\), this difference strictly decreases with \(\beta\), and it tends to zero. The beta and gamma values give \(C_{2,\alpha}=2^\alpha\) and \(C_{3,\alpha}=(e/2)^\alpha\).

## Verification

The accompanying standalone `verify.py` evaluates the exact generalized-Stieltjes coefficient recurrence for seven combinations of dimension and tumbling ratio, comparing the resulting radial moments at four orders against the asymptotic coefficient. In the exactly solvable two-dimensional case it additionally tests the complete beta-moment formula to floating-point tolerance. A separate, fixed-seed finite-population simulation in the same script evaluates leakage for several dimensions and two decreasing thermal-noise scales. The discrete calculations and simulations are corroboration only; the tail, crossover and dimension statements follow analytically from Steps 1–6. Full convergence is not inferred from a finite number of moments, samples or thermal scales.

To reproduce, use Python 3 with NumPy and SciPy, and run `python verify.py` in the folder containing the two files. Random seeds and tested parameter tuples are fixed in the script.

## Relationship to prior work

Guéneau, Majumdar and Schehr (2026, arXiv:2602.08436) derive the exact stationary coordinate transform for the trapped isotropic particle, radial laws in dimensions one through three, and independent Gaussian convolution under thermal forcing. These underlying laws and the qualitative existence of a thermal rounding regime are prior results. Their all-dimensional transform and convolution formulas imply the present observables *in principle*; the additional result is the sharp extraction of a closed all-dimensional shell coefficient via a nontrivial coefficient/Tauberian argument, followed by a fully normalized \(O(\sqrt D)\) outside-radius crossover profile. In particular a generic Gaussian convolution statement does not itself assert the power \(D^{\alpha/2}\) or the coefficient displayed above.

Frydel (2023, arXiv:2309.12537) derives trapped run-and-tumble stationary moment recurrences, emphasizing lower-dimensional solutions; Frydel (2025) studies the special two-dimensional integral equation. The exact two-dimensional radial beta law supplies a consistency check, not a novelty claim. General Dirichlet mean and Tauberian theory provides the analytic tools and may contain implicit broader formulations; this is a remaining originality risk, not a claim of exhaustive literature coverage.

## Limitations

The result is an asymptotic theorem for each fixed dimension and fixed positive tumbling ratio. It does not classify density modes, claim exact finite-noise probabilities, or provide uniform limits in dimension, tumbling rate, or divergent boundary shift \(u\). The nearest source contains a complete exact stationary coordinate transform that mathematically determines these probabilities, so implicit coverage by deeper asymptotic analysis of that transform or by general Dirichlet-mean endpoint results remains possible. The finite simulations assess consistency only; they are not proofs of infinite-order asymptotics. Independent mathematical review has not been performed.

## References

1. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (first posted 2026-02-09), https://arxiv.org/abs/2602.08436.
2. D. Frydel, *Run-and-tumble oscillator: moment analysis of stationary distributions*, arXiv:2309.12537 (2023), https://arxiv.org/abs/2309.12537.
3. D. Frydel, *Integral equation formulation of run-and-tumble particles in a harmonic trap: special status of a system in two dimensions* (2025), https://www.researchgate.net/publication/393681269_Integral_equation_formulation_of_run-and-tumble_particles_in_a_harmonic_trap_special_status_of_a_system_in_two-dimensions.
4. W. Feller, *An Introduction to Probability Theory and Its Applications*, vol. II, Chapter XIII (Laplace-transform Tauberian theorem); the theorem is used only for a monotone distribution function.
