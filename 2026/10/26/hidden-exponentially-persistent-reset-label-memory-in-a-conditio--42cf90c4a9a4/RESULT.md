# Hidden, exponentially persistent reset-label memory in a conditional quantum walk

## Finding

For the symmetric conditional-reset tight-binding walk, the reset label carries a slowly relaxing two-time memory that is not discernible from its symmetric one-time law. For fixed positive hopping parameter \(\gamma\) and reset rate \(\lambda\), and each integer reset-site distance \(a\ge1\), the exact integrated **event-anchored** label correlation is

\[
\mathcal T_a=\int_0^\infty C_a(t)\,dt=\frac{1}{2\lambda p_a},\qquad
p_a=\frac{b_a}{2}+\sum_{n=a+1}^\infty b_n,\qquad
b_n=\frac{\lambda}{\pi\gamma}Q_{n-1/2}\!\left(1+\frac{\lambda^2}{2\gamma^2}\right).
\]

Here \(Q_\nu\) is the real Legendre function of the second kind on arguments greater than one, \(p_a\) is the probability of a reset-label sign flip at the next event, and \(0<p_a<1/2\). The memory is strictly increasing in integer distance \(a\), with the sharp large-separation law

\[
\boxed{\mathcal T_a\sim\frac{\gamma}{\lambda^2}\sqrt{2\pi a\sinh\eta}\,\tanh(\eta/2)e^{a\eta}},
\qquad \eta=2\operatorname{arsinh}\left(\frac{\lambda}{2\gamma}\right)>0.
\]

Its early decay instead begins at an order that grows with the distance:

\[
\boxed{C_a(t)=1-\frac{\lambda(\gamma/2)^{2a}}{(2a+1)(a!)^2}t^{2a+1}+O(t^{2a+2})},\quad t\downarrow0.
\]

The reset-site labels are a symmetric Markov chain when indexed by **reset count**, but not when observed continuously in time. In particular, \(C_a(t)\) is not asserted to be an exponential function of \(t\). The exponential above describes growth of the integrated memory with spatial separation, not decay in elapsed time.

## Assumptions and scope

The Hilbert space is \(\ell^2(\mathbb Z)\). Between resets the particle evolves under the nearest-neighbor Hamiltonian

\[
H=-\frac{\gamma}{2}\sum_{x\in\mathbb Z}(|x\rangle\langle x+1|+|x+1\rangle\langle x|),\qquad\gamma>0.
\]

Reset times form an independent Poisson process of rate \(\lambda>0\). At each reset, an instantaneous position measurement determines the new state: measurement of a positive site sets \(|+a\rangle\), a negative site sets \(|-a\rangle\), and measurement at zero chooses the two signs with equal probability. The separation parameter \(a\) is any positive integer. The phase of the tight-binding amplitude is immaterial because decisions use Born probabilities. Define the label \(S(t)\in\{-1,+1\}\) as the sign of the most recent reset. The process begins at \(t=0\) **immediately after a reset** to either site, with the initial sign chosen symmetrically. We study the event-anchored observable \(C_a(t)=\mathbb E[S(0)S(t)]\), where no new reset before time \(t\) means \(S(t)=S(0)\). This is not the generic equilibrium-age, stationary-clock autocorrelation. The reset-count stationary measure is symmetric.

## Proof

**1. Conditional flip law.** Evolution for time \(u\) from site \(m\) gives position probabilities \(J_{|x-m|}(\gamma u)^2\). Starting at \(+a\), a negative measured position corresponds to lattice displacement less than \(-a\), and zero gives a fair tie. By reflection symmetry the sign-flip probability is

\[
f_a(u)=\frac12J_a(\gamma u)^2+\sum_{n=a+1}^\infty J_n(\gamma u)^2.
\]

For every \(u\), the two-sign symmetry and the Bessel completeness identity imply \(0\le f_a(u)\le1/2\), and this is strict on a set of positive measure. If \(U\) is an exponential inter-reset time of parameter \(\lambda\), independence of successive intervals and repeated measurement/collapse show that labels at consecutive reset events form a symmetric two-state Markov chain with flip probability

\[
p_a=\mathbb E[f_a(U)]=\int_0^\infty\lambda e^{-\lambda u}f_a(u)\,du.
\]

Set \(b_n=\int_0^\infty\lambda e^{-\lambda u}J_n(\gamma u)^2\,du\). Positivity and Tonelli give \(p_a=\frac12b_a+\sum_{n>a}b_n\). The standard Bessel-product Laplace transform yields

\[
b_n=\frac{\lambda}{\pi\gamma}Q_{n-1/2}\!\left(1+\frac{\lambda^2}{2\gamma^2}\right),\qquad n\ge0.
\]

The fixed-point \(n\)-step reset-event correlation is \(\mathbb E[S_0S_n]=(1-2p_a)^n\). No continuous-clock Markov assertion follows from this embedded chain.

**2. Continuous-clock renewal and exact integrated correlation.** Condition on the first reset time. On an interval of duration \(u\) without a reset the sign is unchanged. If the first reset occurs at \(u\), its sign is equal to the initial sign with probability \(1-f_a(u)\) and opposite with probability \(f_a(u)\), and the process renews. Thus

\[
C_a(t)=e^{-\lambda t}+\int_0^t\lambda e^{-\lambda u}[1-2f_a(u)]C_a(t-u)\,du.
\]

The kernel is nonnegative with mass \(1-2p_a\in[0,1)\). Its positive renewal-series solution is integrable, and integrating the equation and solving the resulting scalar identity gives

\[
\mathcal T_a=\frac{1/\lambda}{1-(1-2p_a)}=\frac{1}{2\lambda p_a}.
\]

This conclusion is an exact duration-weighted correlation integral; simply substituting the average reset count into the event-index formula would incorrectly predict an exponential time law.

**3. Strict distance monotonicity.** Consecutive flip probabilities satisfy

\[
p_a-p_{a+1}=\frac12(b_a+b_{a+1})>0.
\]

Every \(b_n\) is strictly positive by its defining nonnegative integral. Thus \(\mathcal T_a\) strictly increases as \(a\) increases over the positive integers.

**4. Sharp large-separation constant.** Write \(1+\lambda^2/(2\gamma^2)=\cosh\eta\), where \(\eta=2\operatorname{arsinh}(\lambda/(2\gamma))\). The Legendre function has the integral representation

\[
Q_{n-1/2}(\cosh\eta)=\int_\eta^\infty
\frac{e^{-n v}}{\sqrt{2(\cosh v-\cosh\eta)}}\,dv,\quad n\ge1,\ \eta>0.
\]

Near its lower limit, \(\cosh(\eta+y)-\cosh\eta=y\sinh\eta+O(y^2)\); Laplace's method, with a globally exponentially bounded remainder, therefore gives

\[
Q_{n-1/2}(\cosh\eta)\sim
\sqrt{\frac{\pi}{2n\sinh\eta}}e^{-n\eta}.
\]

Hence \(b_n\sim\lambda e^{-n\eta}/[\gamma\sqrt{2\pi n\sinh\eta}]\). The same integral representation bounds ratios of successive terms by a fixed geometric factor below one. Dominated convergence applied to the tail \(\sum_{k\ge1}b_{a+k}/b_a\) yields

\[
p_a\sim\frac{\lambda e^{-a\eta}}{2\gamma\sqrt{2\pi a\sinh\eta}}\coth(\eta/2).
\]

Substituting into the exact identity for \(\mathcal T_a\) proves the advertised asymptotic with its explicit prefactor. Limits are for integer \(a\to\infty\) with \(\lambda,\gamma\) fixed, not a simultaneous scaling limit.

**5. High-order onset.** For fixed integer \(a\ge1\), the Bessel Taylor series gives

\[
f_a(u)=\frac{(\gamma/2)^{2a}}{2(a!)^2}u^{2a}+O(u^{2a+2}).
\]

A flip requires at least one reset. The contribution from exactly one reset up to \(t\) is \(2\lambda\int_0^t f_a(u)\,du+O(t^{2a+2})\) to \(1-C_a(t)\). Paths with at least two resets and at least one flip contribute only \(O(t^{2a+2})\), by conditioning on interval lengths and the Poisson event count. This proves the explicit \(t^{2a+1}\) coefficient.

## Verification

The independent `verify.py` constructs the flip probability by directly summing Bessel position probabilities and separately through half-integer Legendre functions. It verifies the agreement of the two calculations for 15 parameter triples, strict ordering of 12 adjacent distances, positivity, the analytic renewal-mass identity, eight early-time coefficient comparisons, and approach to the large-distance prefactor for three rate ratios. Run with `python verify.py` using NumPy, SciPy, and mpmath. The executable checks passed when applied to the code embedded alongside this statement. Numerical tests are corroboration, not substitutes for the renewal and Laplace-asymptotic proofs.

## Relationship to prior work

Acharya and Gupta (2023) established the underlying conditional-reset tight-binding model, exact single-time occupation distributions, the Poisson resetting formulation and Bessel/Legendre transform representations. These facts and the model are prior work. Perfetto, Carollo, Lesanovsky and Garrahan (2021) developed general conditional quantum-reset renewal descriptions; Rose, Touchette, Lesanovsky and Garrahan (2018) treated spectral methods for other resetting processes. General binary Markov-chain diagonalization and renewal equations are also prior mathematics. The present claim isolates the *event-anchored two-time reset-label observable* and determines its strictly distance-ordered integrated lifetime, sharp exponentially amplified large-separation constant, and high-order short-time onset in this exact conditional-reset model. Earlier one-time stationary localization results do not determine this observable without the additional flip-kernel calculation, and the embedded two-state Markov spectrum alone is not the continuous-time correlation. No universal novelty claim for general semi-Markov renewal identities is made.

## Limitations

The result assumes instantaneous measurement/collapse, exact sign-conditioned resetting, independent exponential waiting times, an infinite translation-invariant one-dimensional lattice and a fair tie at zero. It concerns the classical reset-sign record, not a claim about persistence of quantum coherence or stationary position-density correlations. Integrated event-anchored correlation and equilibrium-clock correlation have different age sampling. The theorem proves no universal single exponential relaxation in physical time; it does not address finite lattices, non-exponential waits, driving, imperfect detectors or joint large-distance/vanishing-rate limits. General renewal theory and special-function asymptotics are established tools, and an independently discovered equivalent model-specific result in unindexed literature remains a possibility.

## References

1. A. Acharya and S. Gupta, *Tight-binding model subject to conditional resets at random times*, arXiv:2308.14040 (first posted 2023-08-27), Phys. Rev. E **108**, 064125 (2023). https://arxiv.org/abs/2308.14040
2. G. Perfetto, F. Carollo, M. Magoni and I. Lesanovsky, *Designing non-equilibrium states of quantum matter through stochastic resetting*, arXiv:2106.13761 (2021). https://arxiv.org/abs/2106.13761
3. D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298 (2018). https://arxiv.org/abs/1806.01298
4. NIST Digital Library of Mathematical Functions, Chapter 14 (Legendre and Related Functions), integral representations and large-degree asymptotics. https://dlmf.nist.gov/14
