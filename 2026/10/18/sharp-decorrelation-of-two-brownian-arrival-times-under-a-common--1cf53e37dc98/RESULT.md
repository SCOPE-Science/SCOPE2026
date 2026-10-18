# Sharp decorrelation of two Brownian arrival times under a common reset clock

## Finding

For any \(d,D,r>0\), let two independent Brownian paths, each with generator \(D\partial_{xx}\), start at \(d\) and be absorbed irreversibly at zero. Until absorbed, both are instantaneously returned to \(d\) at the event times of one shared rate-\(r\) Poisson process; independent Brownian noise is used for each path and each excursion. Denote their individual absorption times by \(T_1,T_2\), and put \(z=d\sqrt{r/D}\).

Define the unreset survival function \(Q(t)=\operatorname{erf}(d/\sqrt{4Dt})\), its integral \(K(t)=\int_0^tQ(u)\,du\), and
\[
 p=e^{-z},\quad
 A=\int_0^\infty r e^{-rt}K(t)^2\,dt,\quad
 J=\int_0^\infty r e^{-rt}[1-Q(t)]^2\,dt.
\]
Then the exact mixed moment, covariance, and common marginal variance are
\[
 \mathbb E[T_1T_2]=\frac{A}{p(2p-J)},\qquad
 \operatorname{Cov}(T_1,T_2)=\frac{A}{p(2p-J)}-\frac{(1-p)^2}{r^2p^2},
\]
\[
 \operatorname{Var}(T_i)=\frac{e^{2z}-ze^z-1}{r^2},\qquad i\in\{1,2\}.
\]
The covariance is **strictly positive** for every \(d,D,r>0\). Nevertheless, for fixed \(d,D>0\) and \(r\to\infty\), their Pearson correlation satisfies the sharp asymptotic
\[
 \boxed{\operatorname{Corr}(T_1,T_2)\sim
 \frac{2^{1/4}}{\sqrt{\pi z}}\,e^{-(\sqrt2-1)z},\qquad z=d\sqrt{r/D}\to\infty.}
\]
Here \(f(z)\sim g(z)\) means \(f(z)/g(z)\to1\). Equivalently, the decay is stretched exponential in \(\sqrt r\), multiplied by \(r^{-1/4}\), despite the always-positive correlation at finite resetting rate.

## Assumptions and scope

Each walker evolves on \((0,\infty)\) as \(dX=\sqrt{2D}\,dB\), with a perfectly absorbing endpoint at zero. A **single** independent Poisson clock of rate \(r\) resets all still-unabsorbed walkers at each ring; an absorbed walker stays absorbed. Hits exactly at a clock ring have probability zero. Instantaneous resetting has no travel-time overhead and leaves the other walker's Brownian noise independent. Only the two identical starting-distance, equal-diffusivity walkers and the irreversible first-arrival statistics are claimed. All integrals above are finite for \(d,D,r>0\); in particular \(p>0\) and \(2p-J>0\) because \(J\le p\) (both walkers cannot hit before the clock more frequently than one can).

## Proof

**1. One unreset attempt and the first renewal.** Let \(H_1,H_2\) be independent unreset Brownian absorption times, and \(R\) an independent exponential variable with rate \(r\). The standard one-dimensional reflection principle gives \(\Pr(H_i>t)=Q(t)\) and \(\mathbb E[e^{-sH_i}]=e^{-d\sqrt{s/D}}\). Hence \(p=\Pr(H_i<R)=e^{-z}\). Let \(U_i=H_i\wedge R\) and \(I_i=\mathbf1_{\{H_i>R\}}\). With future absorption times \((T'_1,T'_2)\) generated from a fresh common clock and independent fresh Brownian noises, jointly independent of the initial cycle, the regenerative identity is \(T_i=U_i+I_iT_i'\).

Conditioning on \(R=t\), the independent \(U_1,U_2\) have mean \(K(t)\), so \(\mathbb E[U_1U_2]=A\). Also
\[
 \mathbb E[U_1I_2]=\int_0^\infty re^{-rt}K(t)Q(t)\,dt=\frac{rA}{2},
\]
where the last equality uses \(K'=Q\), integration by parts, and \(K(t)\le t\). Finally \(\mathbb E[I_1I_2]=1-2p+J\), since \(J=\Pr(H_1<R,H_2<R)\). The first moment obeys \(m=\mathbb E[U_i]+(1-p)m\) with \(\mathbb E[U_i]=(1-p)/r\), whence \(m=(1-p)/(rp)\). Writing \(M=\mathbb E[T_1T_2]\), expansion of both regenerative identities gives
\[
 M=A+2\left(\frac{rA}{2}\right)m+(1-2p+J)M.
\]
Thus \(M=A(1+rm)/(2p-J)=A/[p(2p-J)]\), proving the cross-moment and covariance formulas.

**2. The marginal variance.** For an individual walker, the standard resetting renewal equation yields the absorption-time Laplace transform
\[
 \mathbb E[e^{-sT_i}]=\frac{(s+r)e^{-d\sqrt{(s+r)/D}}}{s+r e^{-d\sqrt{(s+r)/D}}},\qquad s\ge0.
\]
Differentiating twice at \(s=0\) (or expanding the analytic transform there) gives \(\mathbb E T_i=(e^z-1)/r\) and \(\operatorname{Var}T_i=(e^{2z}-ze^z-1)/r^2\). Its positivity also follows probabilistically because the hitting time is nondegenerate.

**3. Strict positivity.** Condition on the entire common reset-clock realization \(\mathcal C\). The two absorption times are conditionally independent and identically distributed, so
\[
 \operatorname{Cov}(T_1,T_2)=\operatorname{Var}(\mathbb E[T_1\mid\mathcal C])\ge0.
\]
The conditional mean is genuinely nonconstant. Indeed, conditioning on the first clock gap \(R=s\) and averaging all later clock gaps gives \(\mathbb E[T_1\mid R=s]=K(s)+Q(s)m\). This function tends to \(m\) as \(s\downarrow0\), but diverges as \(s\to\infty\) because \(K(s)\to\infty\), while \(Q(s)m\ge0\). Since an exponential gap has positive density on every positive interval, its variance is strictly positive. The law of total variance then implies \(\operatorname{Var}(\mathbb E[T_1\mid\mathcal C])>0\).

**4. Rare simultaneous success.** Use dimensionless time \(\tau=rt\). The density for an unreset hit at time \(\tau\) is \(z\tau^{-3/2}e^{-z^2/(4\tau)}/(2\sqrt\pi)\). Conditioning on which of two hits is last gives the one-dimensional integral
\[
 J=\frac{z}{\sqrt\pi}\int_0^\infty
 \tau^{-3/2}e^{-\tau-z^2/(4\tau)}
 \operatorname{erfc}\!\left(\frac{z}{2\sqrt\tau}\right)d\tau.
\]
The asymptotic \(\operatorname{erfc}(y)=e^{-y^2}/(\sqrt\pi y)(1+O(y^{-2}))\) is uniform in a fixed relative neighborhood of the unique Laplace saddle \(\tau=z/\sqrt2\). Outside such neighborhoods the phase \(\tau+z^2/(2\tau)\) exceeds its minimum \(\sqrt2z\) by a fixed positive multiple of \(z\); the standard complementary-error-function upper bound controls the tails. Consequently
\[
 J\sim\frac2\pi\int_0^\infty\frac{d\tau}{\tau}e^{-\tau-z^2/(2\tau)}
 =\frac4\pi K_0(\sqrt2z)
 \sim\frac{2^{5/4}}{\sqrt{\pi z}}e^{-\sqrt2z},
\]
where \(K_0\) is the modified Bessel function and its large-argument asymptotic is \(K_0(w)\sim\sqrt{\pi/(2w)}e^{-w}\).

**5. Controlling the cycle time and extracting the correlation.** Since \(K(R)\le R\) and \(R-K(R)\le R\Pr(H_1\le R\mid R)\),
\[
 0\le2-r^2A\le2\mathbb E[(rR)^2\mathbf1_{\{H_1<R\}}]
 =2e^{-z}\left(\frac{z^2}{4}+\frac{5z}{4}+2\right).
\]
The equality follows by conditioning on \(H_1<R\), using the memoryless exponential overshoot \(R-H_1\), and differentiating the unreset hitting transform. Thus \(r^2A=2+O(z^2e^{-z})\). With \(p=e^{-z}\) and the expression above for \(J\), one has \(J/p\to0\), while \(z^2p=o(J/p)\). Multiplying covariance and variance by \(r^2p^2\) shows
\[
 r^2p^2\operatorname{Cov}(T_1,T_2)
 =\frac{r^2A}{2-J/p}-(1-p)^2
 \sim\frac{J}{2p},
 \qquad r^2p^2\operatorname{Var}(T_i)=1-zp-p^2\to1.
\]
Therefore \(\operatorname{Corr}(T_1,T_2)\sim J/(2p)\sim2^{1/4}(\pi z)^{-1/2}e^{-(\sqrt2-1)z}\), completing the proof.

## Verification

The accompanying `verify.py` evaluates \(A\) and \(J\) independently by high-precision quadrature, computes the exact correlation and asymptotic prediction, and independently samples Brownian first hitting times using the exact Lévy-law identity \(H=d^2/(2DZ^2)\) for a standard Gaussian \(Z\). This is an exact-event simulation rather than a discretized Brownian path. It also checks the saddle approximation to \(J\). The proof is analytical and does not rely on this numerical evidence. For \(z=3\), a seeded 250,000-pair simulation gave correlation approximately \(0.01187\) against quadrature \(0.01229\). At \(z=20\), exact correlation was approximately \(3.5429\times10^{-5}\), compared with the leading prediction \(3.7875\times10^{-5}\). The large-\(z\) approximation is not accurate at small \(z\).

To reproduce, run `python verify.py` with NumPy and mpmath installed; no network access is needed. The code's normalized time takes \(r=1\), \(D=1\), and initial distance \(z\), which preserves the dimensionless correlation and joint-success probability.

## Relationship to prior work

Vatash, Goldfarb, Rudyak and Roichman (2026, arXiv:2609.23542v1) explicitly state that a common Poisson reset clock creates correlations between labeled first-passage times and study how the clock alters optimal ordered-arrival times. The present statement instead computes the individual-time covariance exactly, proves its strict sign, and identifies the sharp strong-reset Pearson-correlation decay with its exponent and prefactor. Biroli, Majumdar and Schehr (2023, arXiv:2303.18012v1) analyze first-arrival mean times under common and separate clocks; their first-of-many stopping statistic is not the pair of irreversible labeled hitting times studied here. The single-walker survival and resetting Laplace identities go back to Evans and Majumdar (2011) and are used as known inputs. The 2025 non-Poissonian simultaneous-reset correlation literature concerns particle-position observables rather than this irreversible joint hitting-time statistic. General regenerative-moment calculus underlies the derivation; the model-specific rare-double-success asymptotic supplies the sharp correlation exponent.

## Limitations

The result is for two otherwise independent Brownian particles, identical initial distances, one perfectly absorbing half-line target, a common *Poisson* clock, and instantaneous returns of only surviving particles. It does not treat direct interactions, target depletion, correlated Brownian noises, non-Poissonian clocks, or the covariance of ordered times at arbitrary particle number. Strong resetting means \(z\to\infty\), with fixed \(d,D\) and increasing \(r\); the leading formula is not a uniformly accurate approximation at moderate or small \(z\). The work is not independently audited. A more general multivariate-resetting theorem could subsume the result even if it does not present this specialization explicitly; that possibility remains a novelty limitation.

## References

1. R. Vatash, E. Goldfarb, V. Yu. Rudyak, Y. Roichman, *Rank-dependent optimal resetting in multiparticle search*, arXiv:2609.23542v1 (first posted September 20, 2026), https://arxiv.org/abs/2609.23542.
2. M. Biroli, S. N. Majumdar, G. Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012v1 (2023), https://arxiv.org/abs/2303.18012.
3. M. R. Evans, S. N. Majumdar, *Diffusion with stochastic resetting*, Physical Review Letters 106, 160601 (2011).
4. G. de Mauro et al., *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (2025), https://arxiv.org/abs/2509.06658.
