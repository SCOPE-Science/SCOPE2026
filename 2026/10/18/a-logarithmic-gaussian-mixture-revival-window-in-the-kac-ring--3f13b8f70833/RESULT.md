# A logarithmic Gaussian-mixture revival window in the Kac ring

## Finding

Let a classical Kac ring have \(N\) sites, initially all carrying spin \(+1\). At each site, independently place a stationary spin flipper with probability \(p\in(0,1/2)\), and let the ring shift one site per clock tick, reversing a passing spin exactly at flippers. Write \(M_N(t)\) for the magnetization per site at integer time \(t\), and set \(q=1-2p\in(0,1)\), \(\lambda=-\log q\), and \(\sigma_q^2=(1+q^2)/(1-q^2)\).

**Logarithmic revival-window theorem.** Suppose \(k_N\) is a sequence of integers with \(k_N\to\infty\) and \(k_N=O(\log N)\). If \(\sqrt N\,q^{k_N}\to a\in[0,\infty)\), then

\[
\sqrt N\,M_N(N-k_N)\ \xrightarrow{\mathrm d}\ S\,(a+G),
\]

where \(S\) takes \(+1\) and \(-1\) with equal probability, \(G\sim\mathcal N(0,\sigma_q^2)\), and \(S\) and \(G\) are independent. Thus a nonzero \(a\) produces the symmetric mixture of two Gaussians with means \(\pm a\), rather than a single centered Gaussian.

In the critical window \(k_N-(\log N)/(2\lambda)\to s\in\mathbb R\) (along any sequence or subsequence for which these integer offsets converge), \(a=e^{-\lambda s}\). The transition occurs at the backward-from-half-recurrence scale \((\log N)/(2\lambda)\). More generally, if \(k_N/\log N\to c\in(0,\infty)\), then for \(c<1/(2\lambda)\),

\[
\frac{|M_N(N-k_N)|}{q^{k_N}}\ \xrightarrow{\mathbb P}\ 1,
\]

while for \(c>1/(2\lambda)\),

\[
\sqrt N\,M_N(N-k_N)\ \xrightarrow{\mathrm d}\ \mathcal N(0,\sigma_q^2).
\]

The underlying finite-size variance identity (not claimed as new independently of classical Kac-ring second-moment work) is, whenever \(1\le k\le N/2\),

\[
N\,\operatorname{Var}(A_{N,k})
=1+2\sum_{d=1}^{k-1}q^{2d}-(2k-1)q^{2k},
\qquad A_{N,k}=\frac1N\sum_{i=0}^{N-1}\prod_{j=0}^{k-1}\epsilon_{i+j}.
\]

All indices in products are read modulo \(N\), and the static flipper signs \(\epsilon_i\) are independent with \(\mathbb P(\epsilon_i=-1)=p\).

## Assumptions and scope

The disorder is sampled once before evolution (quenched along each deterministic trajectory) but the limit law refers to sampling the disorder across rings. The initial spins are fixed to \(+1\), not sampled from an equilibrium spin ensemble. The formula uses discrete, synchronous one-site translation; it does not assert a stochastic collision process. The theorem concerns the near-half-recurrence times \(N-k_N\) with \(k_N=O(\log N)\) and \(k_N\to\infty\). No statement is made for \(p=0\), \(p=1/2\), time-dependent scatterers, or general initial spin configurations. Here \(N\to\infty\) through arbitrary positive integers; no parity restriction is needed.

## Proof

**1. Exact reversal identity.** Let \(E_N=\prod_{i=0}^{N-1}\epsilon_i\in\{-1,+1\}\). After \(t\) translations, every spin equals a product of \(t\) consecutive flipper signs. At time \(N-k\), the product of \(N-k\) signs equals \(E_N\) times the complementary product of \(k\) signs, because each sign is its own inverse. Summing over positions gives the identity

\[
M_N(N-k)=E_N A_{N,k},\qquad
A_{N,k}=\frac1N\sum_{i=0}^{N-1}Y_{i,k},\qquad
Y_{i,k}=\prod_{j=0}^{k-1}\epsilon_{i+j}.
\]

Consequently \(|M_N(N-k)|=|A_{N,k}|\) for every disorder realization, while the global parity \(E_N\) is responsible for the sign of the macroscopic revival.

**2. Exact covariance and limiting variance.** For \(N\ge2k\), the two length-\(k\) cyclic intervals starting at indices separated by \(d\), with \(1\le d<k\), share exactly \(k-d\) flippers. Squaring shared signs removes them, so \(\mathbb E[Y_{i,k}Y_{i+d,k}]=q^{2d}\). For nonoverlapping intervals the expectation is \(q^{2k}\). Also \(\mathbb E Y_{i,k}=q^k\). Counting the \(k-1\) overlaps in both circular directions and the diagonal yields

\[
\mathbb E A_{N,k}=q^k,\qquad
N\operatorname{Var}(A_{N,k})=1-q^{2k}+2\sum_{d=1}^{k-1}(q^{2d}-q^{2k}).
\]

For \(k=k_N\to\infty\), the last expression tends to \(\sigma_q^2=(1+q^2)/(1-q^2)\), since \(kq^{2k}\to0\).

**3. Triangular-array central limit theorem.** Put \(Z_{i,N}=Y_{i,k_N}-q^{k_N}\), so \(|Z_{i,N}|\le2\), and each variable depends on a consecutive block of \(k_N\) independent flipper signs. Two sets of these variables are independent when the underlying flipper blocks are disjoint. Fix a main-block length \(b_N=\lfloor N^{1/4}\rfloor\). On the cyclic index set, retain successive runs of \(b_N\) variables and separate retained runs by discarded gaps of at least \(k_N\) variables. Treat the remainder and the wraparound as discarded. Retained run sums are independent; each is bounded in absolute value by \(2b_N=o(\sqrt N)\).

The number of discarded variables is \(O(Nk_N/b_N+b_N+k_N)\). A centered set of \(m\) of the \(Z\)-variables has variance at most \(4(2k_N+1)m\), because each variable overlaps fewer than \(2k_N\) other windows and each covariance has magnitude at most \(4\). Consequently the discarded total divided by \(\sqrt N\) tends to zero in \(L^2\): its variance after normalization is \(O(k_N^2/b_N+b_N k_N/N)\to0\). The independent retained run sums satisfy the Lindeberg condition and have normalized total variance tending to \(\sigma_q^2\) by the full-sum variance calculation and the negligible gaps. Lindeberg–Feller therefore gives

\[
\sqrt N(A_{N,k_N}-q^{k_N})\ \xrightarrow{\mathrm d}\ G,
\qquad G\sim\mathcal N(0,\sigma_q^2).
\]

**4. Independence of the global parity.** It is not enough to know that \(E_N\) is asymptotically fair: a separate argument rules out hidden dependence on the limiting Gaussian. Choose \(J_N\) consisting of sites spaced \(2k_N\) apart cyclically. Its cardinality is at least \(\lfloor N/(2k_N)\rfloor-1\), and each product \(Y_{i,k_N}\) contains at most one chosen sign. Conditional on the signs outside \(J_N\), write \(A_{N,k_N}=C_N+N^{-1}\sum_{j\in J_N}c_j\epsilon_j\) with \(|c_j|\le k_N\). For each real \(u\), independence of chosen signs gives

\[
\left|\mathbb E\left[E_N e^{iu\sqrt N(A_{N,k_N}-q^{k_N})}\right]\right|
\le\left(q+\frac{|u|k_N}{\sqrt N}\right)^{|J_N|}\longrightarrow0.
\]

Indeed \(\mathbb E[\epsilon e^{i\theta\epsilon}]=q\cos\theta+i\sin\theta\), whose modulus is at most \(q+|\theta|\). Also \(\mathbb E E_N=q^N\to0\). Thus the positive- and negative-parity weighted characteristic functions each tend to one half of the Gaussian characteristic function, proving joint convergence of the centered magnetization and parity to independent \((G,S)\), with \(S\) a fair sign.

**5. Crossover.** Combine the exact identity from Step 1 with the joint convergence from Steps 3–4 and \(\sqrt N q^{k_N}\to a\). This gives the Gaussian mixture. If \(k_N/\log N\to c<1/(2\lambda)\), then \(\sqrt Nq^{k_N}\to\infty\) and the variance bound in Step 2 gives \(A_{N,k_N}/q^{k_N}\to1\) in probability. If \(c>1/(2\lambda)\), the deterministic shift \(\sqrt Nq^{k_N}\to0\), yielding the centered normal law. This proves every assertion.

## Verification

The included `verify.py` independently enumerates every flipper word on rings with \(4\le N\le12\), for each \(1\le k\le\lfloor N/2\rfloor\), comparing weighted exact moments against the stated covariance formula. A separate seeded Monte Carlo test at \(N=6000\) checks the second moment of the *signed* half-recurrence magnetization against the Gaussian-mixture prediction. Both tests complete successfully with Python's standard library only. Enumeration does not prove the asymptotic theorem; Steps 3–4 above do.

## Relationship to prior work

The deterministic ring, half-period parity recurrence and first/second moments are classical. Gottwald and Oliver's 2009 study derives a finite-size variance bound, exact for fully aligned initial spins, and explicitly treats the interval approaching half recurrence (its Section 5, Eq. (27), and Exercises 9–10). **The finite variance identity above is therefore used as a proof input, not claimed as an independently novel formula.** Its variance calculations do not, by themselves, determine the limiting probability law in the logarithmic backward window.

Hiura (2021) derives quenched dynamical large deviations and an Ornstein–Uhlenbeck central-limit process for time horizons held fixed as \(N\to\infty\); Section 2.2 explicitly states that this limit sets aside recurrence. The present regime \(t=N-k_N\) is outside that fixed-time limit and has a different, symmetric two-component limit. Chandrasekaran and Jain (2012) address entropy and the recurrence of statistical fluctuations, so their work is a plausible specialized comparison; only the abstract was accessible and its exact relation to the logarithmic mixture remains uncertain.

## Limitations

The theorem does not establish a new mean or variance formula in isolation, a universal rate of convergence, or a limit for superlogarithmic backward windows. The Gaussian mixture is an annealed-over-disorder distribution for a deterministic ring with fixed flippers, not a claim of stochastic motion during a run. The full text of Chandrasekaran and Jain (2012) was not obtained; a finer result under alternative terminology could reduce the originality assessment. The initial all-aligned state is essential to the proof as written. No independent external audit has been conducted.

## References

1. G. A. Gottwald and M. Oliver, *Boltzmann's Dilemma: An Introduction to Statistical Mechanics via the Kac Ring*, SIAM Review **51** (2009), 613–635. DOI: `10.1137/070705799`. Publisher online publication: 2009-08-05. An open full-text manuscript is available at `https://www.aquila.infn.it/ciuchi/didattica/MS/Notes/02_Foundations/references/kac-ring.pdf`.
2. K. Hiura, *Macroscopic dynamical fluctuations in Kac ring model*, Journal of Statistical Physics **186** (2022), article 10; earliest arXiv posting 2021-09-14, `arXiv:2109.06434`. Full text: `https://arxiv.org/html/2109.06434v2`.
3. A. Chandrasekaran and S. R. Jain, *Kac's ring: Entropy and Poincaré recurrence*, Physica A **391** (2012), 3702–3707. DOI: `10.1016/j.physa.2012.02.010`. Abstract examined; full text not accessed.
4. M. Kac, *Some remarks on the use of probability in classical statistical mechanics*, Bulletin de l'Académie Royale de Belgique (1956). Historical origin of the model; the exact public day of this historical work was not verified.
