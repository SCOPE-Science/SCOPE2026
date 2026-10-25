# Exact two-time current covariance and ballistic memory in a resetting run-and-tumble gas

## Finding
Consider a Poisson field of initial particle anchors of intensity \(\rho>0\) on the negative real half-line. Independently for each anchor, a particle moves at velocity \(\pm v\), reversing sign at rate \(\gamma>0\), and is reset at rate \(r>0\) to its anchor with a newly sampled fair velocity. Initialize every particle in its stationary *displacement-and-velocity* law conditional on its anchor. Let \(Q(t)\) count particles to the right of the origin at time \(t\ge0\), and put \(C(t)=\operatorname{Cov}(Q(0),Q(t))\).

Write
\[
\lambda=\frac{\sqrt{r(r+2\gamma)}}v,\qquad D_{\rm eff}=\frac{v^2}{2\gamma},\qquad z=s+r,\qquad k(s)=\frac{\sqrt{z(z+2\gamma)}}v,\qquad a(s)=\frac{z+2\gamma}{2v^2k(s)}.
\]
For every real \(s>0\), the *complete stationary two-time current covariance* has the explicit Laplace transform
\[
\boxed{\int_0^\infty e^{-st}C(t)\,dt
=\frac\rho{\lambda^2}\left[\frac\lambda2a(s)\left(\frac1{k(s)}+\frac1{k(s)+\lambda}\right)+\frac r{4v^2}\left(\frac1{k(s)}-\frac1{k(s)+\lambda}\right)\right]
+\frac{\rho r}{4s(s+r)(\lambda+k(s))}.}
\]
In particular,
\[
\boxed{C(0)=\frac\rho{2\lambda},\qquad C'(0+)=-\frac{\rho(v\lambda+r)}{4\lambda},\qquad \lim_{t\to\infty}C(t)=\frac\rho{8\lambda}.}
\]
For each fixed \(v,\gamma,r,\rho>0\), the approach to the nonzero plateau has the sharp large-lag law
\[
\boxed{C(t)-\frac\rho{8\lambda}\sim
\frac{\rho}{\lambda^2\sqrt{\pi D_{\rm eff}}}\left(\frac12+\frac r{8\gamma}\right)\frac{e^{-rt}}{\sqrt t}\quad(t\to\infty).}
\]
The mean is \(m=\mathbb EQ(t)=\rho/(2\lambda)\). At each time lag, \((Q(0),Q(t))\) is exactly bivariate Poisson with generating function
\[
\boxed{\mathbb E[u^{Q(0)}w^{Q(t)}]=\exp\bigl((m-C(t))(u-1)+(m-C(t))(w-1)+C(t)(uw-1)\bigr)}
\]
for \(u,w\ge0\). Thus, even though every individual particle resets and mixes, the annealed current retains a strict long-lag covariance \(m/4\) due solely to the frozen random initial anchors.

## Assumptions and scope
All four parameters are strictly positive and finite. Each velocity reverses sign at an independent rate-\(\gamma\) Poisson clock; at each rate-\(r\) resetting event the position returns to the particle's own fixed anchor and its velocity is independently resampled fairly. Particle clocks are mutually independent. Anchors form a stationary-rate Poisson point process on the negative half-line and do not move. The ensemble is stationary with respect to each particle's displacement and velocity at observation time zero; the initial-anchor disorder is annealed, not dynamically resampled. The current is the instantaneous number located in the positive half-line, equivalent to net integrated crossings from their initial negative positions. Endpoints have probability zero. There is no hard-core interaction or global/common resetting clock. The large-time asymptotic takes lag to infinity with all parameters fixed, including \(\gamma>0\).

## Proof
**Stationary one-particle resolvent.** Let \(X\) be displacement from an anchor and \(\sigma\in\{+1,-1\}\) velocity sign. Its invariant signed densities on \(x>0\) are
\[
\pi_\sigma(x)=A_\sigma e^{-\lambda x},\qquad A_\sigma=\frac{\lambda+\sigma r/v}{4}.
\]
Indeed, the position marginal is \(\lambda e^{-\lambda |x|}/2\): the Laplace-time free telegraph resolvent at rate \(r\) has transform \((r+2\gamma)/(r(r+2\gamma)+v^2q^2)\); multiplication by the reset rate \(r\) gives the stated two-sided exponential marginal. The stationary probability current \(j=v(\pi_+-\pi_-)\) on \(x>0\) obeys \(j'=-r(\pi_++\pi_-)\) and \(j(\infty)=0\), yielding \(j(x)=r e^{-\lambda x}/2\) and thus \(A_\sigma\). In particular, the probability that a particle anchored at \(-a\) is to the right of zero is \(p(a)=e^{-\lambda a}/2\) for \(a\ge0\).

**Poisson marking.** For each anchor, mark whether its particle lies to the right at each of the two observation times. The four marks are independent across anchors. Poisson thinning gives independent counts for the \((1,1),(1,0),(0,1)\) marks. Their common total marginal mean is \(m=\rho\int_0^\infty p(a)\,da=\rho/(2\lambda)\). The \((1,1)\) intensity is \(C(t)\), proving the bivariate-Poisson formula and identifying the covariance with the same-particle joint occupancy intensity.

**Renewal split.** Condition on whether there was a particle reset between the two observations. On the no-reset event of probability \(e^{-rt}\), the free displacement increment is \(W_t=\int_0^t v\sigma_u\,du\). Integrating the positive threshold \(a\) against an initial displacement \(x>0\) gives \(\min(x,x+W_t)_+\). With \(x\) density \(A_\sigma e^{-\lambda x}\), direct integration equals \(A_\sigma e^{\lambda\min(W_t,0)}/\lambda^2\). On the complementary event, the most recent reset was \(u\in(0,t)\) before observation, with density \(r e^{-ru}\,du\); the position at the later observation is a free displacement of duration \(u\), independent of the earlier displacement. Thus
\[
C(t)=\frac{\rho e^{-rt}}{\lambda^2}\sum_{\sigma=\pm1} A_\sigma\,\mathbb E_\sigma[e^{\lambda\min(W_t,0)}]
+\rho\int_0^t re^{-ru}H(u)\,du,
\]
where \(H(u)=\int_0^\infty p(a)\Pr(W_u>a)\,da\), for a free run-and-tumble walk with fair initial velocity.

**Exact transform.** Put \(\kappa(q)=\sqrt{q(q+2\gamma)}/v\). The free telegraph position resolvent, conditional on initial velocity \(\sigma v\), is
\[
\int_0^\infty e^{-qu}\Pr_\sigma(W_u\in dx)\,du
=e^{-\kappa(q)|x|}\left[\frac{q+2\gamma}{2v^2\kappa(q)}+\frac{\sigma\operatorname{sgn}(x)}{2v}\right]dx.
\]
Consequently the transform of \(\mathbb E_\sigma[e^{\lambda\min(W_t,0)}]\) equals
\[
\left(a_q+\frac\sigma{2v}\right)\frac1{\kappa(q)}+
\left(a_q-\frac\sigma{2v}\right)\frac1{\kappa(q)+\lambda},\qquad a_q=\frac{q+2\gamma}{2v^2\kappa(q)}.
\]
Separately, the symmetric free displacement obeys \(\int_0^\infty e^{-qu}\Pr(W_u>a)\,du=e^{-\kappa(q)a}/(2q)\). Hence \(\widehat H(q)=1/[4q(\lambda+\kappa(q))]\). Taking the lag Laplace transform of the renewal split with \(q=s+r\) yields the boxed closed transform.

**Two boundary regimes.** At lag zero the no-reset term gives \(\rho\sum A_\sigma/\lambda^2=\rho/(2\lambda)\). Its right derivative comes from free left-moving crossings at intensity \(\rho vA_-/\lambda\), together with resets removing previously positive particles at rate \(\rho r/(2\lambda)\). This sums to \(-\rho(v\lambda+r)/(4\lambda)\). The reset portion of the renewal split tends to \(\rho\int_0^\infty re^{-ru}H(u)\,du=\rho\int_0^\infty p(a)^2\,da=\rho/(8\lambda)\), and the no-reset portion vanishes.

For the sharp correction, analytically continue the transform to the right of its telegraph branch cuts, using the square root positive for real \(s>0\). Subtract the stationary pole \(\rho/(8\lambda s)\), and put \(z=s+r\). As \(z\to0\) in a slit sector, \(k(s)=\sqrt{z/D_{\rm eff}}(1+O(z))\). The apparent simple pole at \(z=0\) cancels between the no-reset and renewal terms. The leading remaining branch singularity is
\[
\widehat C(s)-\frac{\rho}{8\lambda s}
=\frac{\rho}{\lambda^2\sqrt{D_{\rm eff}}}
\left(\frac12+\frac r{8\gamma}\right)z^{-1/2}+O(1).
\]
The other telegraph branch point lies farther left at \(s=-r-2\gamma\), and \(\lambda+k(s)\) has no zero in \(\Re s>-r\). Inverse Laplace contour deformation about the branch point at \(s=-r\) gives the displayed \(e^{-rt}t^{-1/2}\) term with its positive exact coefficient. This is a fixed-parameter asymptotic and makes no uniform assertion as \(\gamma\downarrow0\).

## Verification
The independent numerical reproducer evaluates the transform by high-precision inverse Laplace transformation and simulates stationary particle displacements and their subsequent trajectories directly, without using the analytic resolvent in the simulation. With \((\rho,r,\gamma,v)=(1.4,0.7,1.3,2)\), the predicted covariances are approximately \(0.75248737\) at lag \(0.2\) and \(0.31435338\) at lag \(2\). Direct regenerative Monte Carlo using 250,000 particles gave \(0.74958844\pm0.00294825\) and \(0.31340388\pm0.00170505\), respectively (one-standard-error uncertainty). The theoretical stationary plateau equals \(0.2302830932\). The reproducer also checks the finite right derivative and branch-point tail against numerical inversion, while the proof, rather than simulation, establishes the infinite-volume identities and asymptotics.

## Relationship to prior work
Di Bello, Hartmann, Majumdar, Mori, Rosso and Schehr (arXiv:2302.06696; first public February 13, 2023) established the independently resetting Brownian and run-and-tumble step-gas models and their **single-observation** annealed and quenched current distributions. The already known stationary RTP position marginal and Poisson one-time current law are premises. The result here concerns an evaluated **two-time** RTP covariance transform, including its finite ballistic initial slope and exact long-lag correction. Jose, Rosso and Ramola (arXiv:2306.13613) studied current fluctuations for *non-resetting* run-and-tumble particles. General Poisson-marking and renewal identities are standard; their use alone is not claimed as original. A related previously known two-time Brownian-reset gas covariance does not imply the finite-velocity telegraph transform, which depends separately on the reversal and resetting rates.

## Limitations
This is a self-review mathematical result, not an independent scholarly audit. An unlocated equivalent specialization of a general Markov-renewal covariance formula cannot be ruled out absolutely. The result is annealed over Poisson anchors; replacing their law by a fixed lattice, allowing particle interactions, common resets, biased spin resampling, or a nonstationary displacement initialization changes the law. It does not characterize arbitrary multi-time cumulants or finite-sample inference. The branch asymptotic requires \(r,\gamma>0\) fixed and does not cover the zero-tumble limit.

## References
1. C. Di Bello, A. K. Hartmann, S. N. Majumdar, F. Mori, A. Rosso, G. Schehr, *Current fluctuations in stochastically resetting particle systems*, arXiv:2302.06696 (2023), Phys. Rev. E **108**, 014112. https://arxiv.org/abs/2302.06696
2. S. Jose, A. Rosso, K. Ramola, *Generalized disorder averages and current fluctuations in run and tumble particles*, arXiv:2306.13613 (2023), Phys. Rev. E **108**, L052601. https://arxiv.org/abs/2306.13613
