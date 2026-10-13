# Arithmetic resonance of residence times in repulsive zero-range comb branches

## Finding
Consider an open branch with \(L\) sites in the repulsive zero-range transport model defined below. Let \(T_L\) be the stationary Palm mean time elapsed between a particle's entry from a reservoir into site 1 and its ultimate return to that reservoir. For \(u,h,z>0\), define \(\alpha=h/u\), \(c=(\log z)/u+1/2\), \(\lambda=z e^{h/2}\), and the one-periodic, zero-mean function
\[
\Theta_u(t)=\sum_{m\in\mathbb Z} e^{-u(m-t)^2/2},\qquad
\psi_u(t)=u^{-1}\frac{d}{dt}\log\Theta_u(t).
\]
There is a finite constant \(C=C(u,h,z)\) such that
\[
\lambda T_L=\frac{\alpha}{2}L^2+\left(c+\frac\alpha2\right)L
+\sum_{k=1}^L\psi_u(c+k\alpha)+C+o(1).
\tag{1}
\]
If \(\alpha=p/q\) is positive rational in lowest terms, put
\[
R_{u,q}(c)=q^{-1}\sum_{j=0}^{q-1}\psi_u(c+j/q).
\]
Then
\[
\lambda T_L=\frac\alpha2L^2+\left(c+\frac\alpha2+R_{u,q}(c)\right)L+O(1).
\tag{2}
\]
For irrational \(\alpha\), the corresponding linear coefficient is exactly \(c+\alpha/2\), with error \(o(L)\). If additionally \(\|m\alpha\|_{\mathbb R/\mathbb Z}\ge K m^{-\tau}\) for all positive integers \(m\) and fixed \(K,\tau>0\), its remainder improves to \(O(1)\). For each fixed \(u>0\), some \(A_u,\sigma_u>0\) satisfy \(\sup_c|R_{u,q}(c)|\le A_u e^{-\sigma_u q}\) for every \(q\ge1\). The arithmetic part of the linear coefficient is therefore a generalized Thomae function of the bias/repulsion ratio: it vanishes at every irrational ratio, is exponentially suppressed at large rational denominators, and can be nonzero at low-denominator rational ratios. In particular \(\lambda T_L/L^2\to h/(2u)\) for every positive \(h/u\).

## Assumptions and scope
Fix \(L\in\mathbb N\). At site \(k=1,\ldots,L\), a nonnegative integer \(n_k\) counts particles. Set \(g(0)=0\) and \(g(n)=e^{u(n-1)}\) for \(n\ge1\). A particle jumps from \(k\) to \(k+1\) at total rate \(e^{h/2}g(n_k)\), and from \(k+1\) to \(k\) at rate \(e^{-h/2}g(n_{k+1})\). A reservoir injects into site 1 at constant rate \(\lambda=ze^{h/2}\); site 1 loses particles to the same reservoir at total rate \(e^{-h/2}g(n_1)\). There is no loss at the far endpoint. Jumps choose one of the particles on the departing site uniformly, which defines individual residence times without altering occupation dynamics. The stationary Palm mean conditions on an injection event, not on a particle initially situated at the closed branch tip. There is no global particle-number constraint; the reservoir fugacity \(z\) remains fixed as \(L\to\infty\).

## Proof
**Stationary law and residence identity.** For \(x_k=ze^{kh}\), define
\[
F_u(x)=\sum_{m\ge0}x^m e^{-u m(m-1)/2},\quad
\pi_L(n_1,\ldots,n_L)=\prod_{k=1}^L\frac{x_k^{n_k}e^{-u n_k(n_k-1)/2}}{F_u(x_k)}.
\]
The normalization converges for each \(x_k>0\). Because the ratio of weights for increasing a site's occupation from \(n\) to \(n+1\) is \(x_k/g(n+1)\), the edge identities \(x_{k+1}/x_k=e^h\) and \(x_1=ze^h\) imply detailed balance for every internal hop and for injection versus exit. This proves stationarity. The process is irreducible and nonexplosive: its total particle count can grow only by immigration from a finite-rate Poisson process, while it has finitely many transitions and bounded rates at each fixed total count. The normalized reversible law yields positive recurrence. Under uniform labeling of departing particles, every tagged particle at a nonempty site has rate at least \(m_u e^{-h/2}\) toward the reservoir direction when that edge exists, where \(m_u=\inf_{n\ge1}e^{u(n-1)}/n>0\). Its embedded location chain is a biased nearest-neighbor walk on a finite interval with a positive probability of reaching the reservoir in a bounded number of steps; the uniformly bounded holding-time means establish eventual exit and finite mean residence. The mean number in the branch is \(\sum_{k=1}^L\rho_k\), where \(\rho_k=x_k F'_u(x_k)/F_u(x_k)\). Conservation of tagged arrivals, ergodicity, and the stationary queueing identity \(\mathbb E N=\lambda\mathbb E T\) now give
\[
\lambda T_L=\sum_{k=1}^L\rho_k.
\tag{3}
\]
This equation by itself is a direct application of established theory and is not claimed as the new contribution.

**Exact discrete-Gaussian reduction.** Completing the square in the site weight gives a lattice Gaussian proportional to \(e^{-u(m-t_k)^2/2}\), conditioned on \(m\ge0\), with center \(t_k=c+k\alpha\). For the unconditioned distribution on all \(m\in\mathbb Z\), differentiation of \(\Theta_u\) yields the exact mean \(t_k+\psi_u(t_k)\). Let \(\delta_k\) denote the difference between conditioned and unconditioned means. Since \(t_k\) grows linearly and the omitted mass is a negative Gaussian tail, for sufficiently large \(k\), \(|\delta_k|\le B(1+t_k)e^{-b t_k^2}\) with constants \(B,b>0\). Thus \(\sum_{k\ge1}|\delta_k|<\infty\), and its tail tends to zero. Summing \(t_k=c+k\alpha\) in (3) yields (1), with \(C=\sum_{k\ge1}\delta_k\).

**Arithmetic response.** \(\Theta_u(t)>0\) for real \(t\), is one-periodic, and is analytic; so is \(\psi_u\). Its period integral vanishes because it is the logarithmic derivative of a periodic positive function. A rational rotation \(c+k p/q\) cycles through every \(q\)-point translate, giving (2) with bounded periodic partial-sum error. An irrational rotation is equidistributed, so its mean \(\psi_u\) is zero and the partial sums are \(o(L)\). In the Diophantine case, expand \(\psi_u(t)=\sum_{m\ne0}\widehat\psi_u(m)e^{2\pi i m t}\). Analyticity in a thin complex strip implies \(|\widehat\psi_u(m)|\le B_u e^{-\sigma_u|m|}\). The partial geometric sums are bounded by \(2/|1-e^{2\pi i m\alpha}|\le B' m^{\tau}\), uniformly in \(L\). Absolute convergence gives the \(O(1)\) remainder. Averaging on a \(q\)-grid annihilates every Fourier mode except multiples of \(q\), proving the exponential bound on \(R_{u,q}\). The rational/irrational correction therefore has the stated continuity behavior: its nonzero values at rational points are isolated discontinuities in the sense of a Thomae-type coefficient, whereas it is continuous at every irrational point. The correction is genuinely nonzero in this model: for \(c=1/4\) and \(q=1\), as \(u\to\infty\), the lattice Gaussian concentrates at \(m=0\), so \(\psi_u(1/4)\to-1/4\).

## Verification
Run `python3 verify.py` using the standard library. The supplied checker reconstructs rational detailed-balance fluxes on a two-site branch, tests the fugacity identity separately, evaluates conditioned and unconditioned Gaussian moments, and compares rational and irrational arithmetic limits. It reports `VERIFY_OK 41`. Finite checks illustrate but do not prove the infinite-size result; the Gaussian tail, Fourier, and equidistribution arguments above are the proof.

## Relationship to prior work
Majumder and Barma [1] introduce exactly the on-site repulsion and bias-dependent zero-range rates and derive their stationary product fugacity and branch density profiles. Their Section IV already observes population plateaus and periodic modulation under field/repulsion ratios. Consequently neither the product stationary law nor the per-site mean occupancy nor the leading Little-law identity is novel here. Little [2] establishes the stationary conservation identity underlying (3). The new assertion is the sharp **arithmetic classification of the linear finite-depth residence-time coefficient** under the explicit grand-canonical open-boundary reservoir, including its rational/irrational dichotomy, uniform denominator suppression, and bounded Diophantine remainder. General zero-range invariant-measure methodology, including related developments [3], is background rather than a claimed innovation.

## Limitations
This is an **entrance-to-exit stationary Palm mean**. It does not solve the different time-to-escape problem for a particle initialized at the remote tip of a branch, which [1] discusses as future work. The reservoir is idealized as fixed-fugacity Poisson immigration; the result is not claimed for canonical ensembles, a dynamically coupled finite backbone, arbitrary repulsion laws, vanishing interaction \(u=0\), or fluctuations of residence times. Rational/irrational dependence concerns a subleading \(O(L)\) term, not the universal leading \(O(L^2)\) scaling. For general Liouville irrational parameters only \(o(L)\) (not a uniform bounded error) is established. The result does not establish novelty beyond the literature inspected below.

## References
[1] S. Majumder and M. Barma, “Stochastic systems with Bose–Hubbard interactions: Effects of bias on particles on a random comb,” arXiv:2601.09962v1 (first posted 2026-01-15), https://arxiv.org/html/2601.09962v1.

[2] J. D. C. Little, “A Proof for the Queuing Formula: L=λW,” Operations Research 9 (1961), 383–387, doi:10.1287/opre.9.3.383.

[3] J. Kuan, “Stochastic Fusion of Interacting Particle Systems and Duality Functions,” arXiv:1908.02359 (2019), https://arxiv.org/abs/1908.02359.
