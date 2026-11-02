# Random Gaussian-mixture limits and a \(q\)-product energy law for batch-reset Brownian gases

## Finding
For a Brownian gas reset in independently sampled, fixed-size batches, a positive limiting batch fraction leaves a **random macroscopic density** even as the particle number diverges. Its empirical mean-square displacement has an explicit exponential-perpetuity distribution, whose cumulants, large-value tail, and finite-population approximation error can be computed exactly.

Let \(\theta\in(0,1]\), \(q=1-\theta\), and let \(E_0,E_1,\ldots\) be independent exponential random variables of rate \(r\). Set \(T_k=\sum_{j=0}^k E_j\) and let \(\gamma_t\) denote the centered normal law of variance \(2Dt\). The limiting probability measure and empirical quadratic energy are
\[
\mu_\theta=\sum_{k=0}^{\infty}\theta q^k\gamma_{T_k},\qquad
Q_\theta=\int x^2\,\mu_\theta(dx)=2D\sum_{j=0}^{\infty}q^jE_j.
\]
For \(s\ge0\), the Laplace transform and all cumulants are
\[
\mathbb E[e^{-sQ_\theta}]=\prod_{j=0}^{\infty}\frac{1}{1+(2Ds/r)q^j}
=\frac{1}{(-2Ds/r;q)_\infty},\qquad
\kappa_k(Q_\theta)=\frac{(2D)^k(k-1)!}{r^k(1-q^k)}\quad(k\ge1).
\]
The standard infinite product notation is \((a;q)_\infty=\prod_{j\ge0}(1-aq^j)\). The variance-to-squared-mean ratio is strictly positive:
\[
\frac{\operatorname{Var}(Q_\theta)}{(\mathbb EQ_\theta)^2}=\frac{\theta}{2-\theta}.
\]
The sharp right-tail equivalent, including its full prefactor, is
\[
\mathbb P(Q_\theta>x)\sim \frac{e^{-rx/(2D)}}{\prod_{j=1}^{\infty}(1-q^j)}\quad(x\longrightarrow\infty).
\]
For \(q=0\), the empty product is one and the law is exactly exponential after scaling.

## Assumptions and scope
Fix \(D,r>0\). For every \(N\ge2\), let \(1\le m_N\le N\) be an integer and set \(\theta_N=m_N/N\), \(q_N=1-\theta_N\). Between reset events, \(N\) labeled coordinates satisfy independent Brownian equations \(dX_i=\sqrt{2D}\,dB_i\) on the full real line. A single external Poisson process of rate \(r\) marks all event times; at each event, a uniformly sampled \(m_N\)-subset of labels is instantaneously set to zero, independently of earlier marks and Brownian noises. All statements refer to the unique stationary law obtained from a two-sided history, which exists since every label is hit infinitely often in the past. Suppose \(\theta_N\to\theta\in(0,1]\).

Define \(\mu_N=N^{-1}\sum_{i=1}^N\delta_{X_i}\) and \(Q_N=N^{-1}\sum_{i=1}^N X_i^2\). The random measures are compared under a coupling of their common backward Poisson gaps \(E_0,E_1,\ldots\) across population sizes; for every bounded continuous test function, its empirical integral converges in probability under that coupling. This is weak convergence in probability of random probability measures; the quadratic observables additionally converge in \(L^2\). No claim is made about a subextensive reset fraction, about interacting particles, or about spatial confinement.

## Proof
**1. Stationary backward reset indices.** Starting from the observation time and listing the preceding Poisson waiting gaps as \(E_0,E_1,\ldots\), each fixed label is selected at an event with probability \(\theta_N\), independently from event to event. Its index \(K_i\) of the most recent selecting event therefore obeys \(\mathbb P(K_i=k\mid(E_j))=\theta_N q_N^k\), for \(k\ge0\). Conditionally on all marks and gaps, \(X_i\) is Gaussian with variance \(2DT_{K_i}\), independently over labels through their separate Brownian paths.

**2. Random empirical-measure law.** For any fixed number of labels and any fixed number of past events, their inclusion indicators converge jointly to independent Bernoulli variables of parameter \(\theta\), since a uniform fixed-size sample has asymptotically independent inclusion indicators when \(m_N/N\to\theta\). The truncation error at the last \(L\) events is uniformly bounded in probability by \(q_N^L\), which tends geometrically to zero uniformly for sufficiently large \(N\). Consequently, conditional on the gaps, the laws of any fixed collection of last-reset indices converge to independent geometric laws with weights \(\theta q^k\). Brownian paths are independent conditional on the marks. For each bounded continuous \(f\), it follows from the one-label conditional means and the two-label conditional covariances that
\[
\frac1N\sum_{i=1}^N f(X_i)\xrightarrow[]{\mathbb P}
\sum_{k=0}^{\infty}\theta q^k\int f(x)\,\gamma_{T_k}(dx).
\]
Applying this to a countable convergence-determining family and using uniform first-moment tightness from the second-moment bound below yields weak convergence in probability of \(\mu_N\) to \(\mu_\theta\).

**3. Exact finite-size quadratic control.** By conditioning only on the Poisson gaps and averaging the reset marks, one finds
\[
\mathbb E[Q_N\mid(E_j)]=2D S_N,\qquad S_N=\sum_{j=0}^{\infty}q_N^jE_j.
\]
Let \(A_i=T_{K_i}\) be the backward age of label \(i\). The chance that one reset event hits at least one of two distinct specified labels is
\[
h_{2,N}=1-\frac{\binom{N-2}{m_N}}{\binom N{m_N}}
=\theta_N(2-\theta_N)+\frac{\theta_N(1-\theta_N)}{N-1}.
\]
For the stationary age process, the age generator acting on \(A_iA_j\) gives
\(\mathbb E[A_iA_j]=2/(r^2\theta_N h_{2,N})\) for \(i\ne j\); the one-label moments are \(\mathbb E[A_i^2]=2/(r^2\theta_N^2)\). Brownian Gaussian fourth moments give \(\mathbb E[X_i^4]=12D^2\mathbb E[A_i^2]\), and \(\mathbb E[X_i^2X_j^2]=4D^2\mathbb E[A_iA_j]\) for distinct labels. Thus
\[
\mathbb EQ_N^2=\frac{(2D)^2}{r^2}\left(\frac{6}{N\theta_N^2}+\frac{2(N-1)}{N\theta_N h_{2,N}}\right),
\quad \mathbb E[(2DS_N)^2]=\frac{(2D)^2}{r^2}\frac{2}{\theta_N^2(2-\theta_N)}.
\]
Conditional expectation is an orthogonal projection in \(L^2\), so
\[
0\le\mathbb E[(Q_N-2DS_N)^2]
=\mathbb EQ_N^2-\mathbb E[(2DS_N)^2]
\le\frac{6(2D)^2}{r^2N\theta_N^2}.
\]
Here the upper bound uses \(h_{2,N}\ge\theta_N(2-\theta_N)\). Since \(\theta_N\to\theta>0\), the geometric exponential sums satisfy \(S_N\to\sum_{j\ge0}q^jE_j\) in \(L^2\), proving the claimed quadratic limit and exact measure second moment.

**4. Transform, cumulants, and tail.** Independence of the Poisson gaps yields
\(\mathbb E[e^{-sQ_\theta}]=\prod_{j\ge0}(1+2Ds q^j/r)^{-1}\). The product converges because \(q<1\), including \(q=0\). Expanding its logarithm at the origin yields the stated cumulants. In particular, \(\mathbb EQ_\theta=2D/(r\theta)\) and \(\operatorname{Var}(Q_\theta)=(2D/r)^2/[\theta(2-\theta)]\).

For the tail, write \(Q_\theta=2D(E_0+Y)\), where \(Y=\sum_{j\ge1}q^jE_j\) is independent of \(E_0\). The moment-generating function \(\mathbb E[e^{rY}]=\prod_{j\ge1}(1-q^j)^{-1}\) is finite. Moreover, for some \(\delta>0\) with \(q(1+\delta)<1\), \(\mathbb E[e^{r(1+\delta)Y}]<\infty\). Conditioning on \(Y\) gives
\[
\mathbb P(E_0+Y>z)=e^{-rz}\mathbb E[e^{rY}\mathbf1_{Y\le z}]+\mathbb P(Y>z).
\]
Dominated convergence handles the first term, and the higher exponential moment makes the second \(o(e^{-rz})\). Substitute \(z=x/(2D)\) to obtain the sharp prefactor.

## Verification
The supplementary standard-library Python program `verify_energy.py` checks reset-hit probabilities against direct batch enumeration, recomputes exact age-moment recurrences, verifies the finite-size projection-error identity and bound using rational arithmetic, and checks truncated product, cumulant and exponential-tail relations. Running it produced `PASS: 10664 bounded arithmetic checks`. It does not substitute for the infinite-population arguments or asymptotic-tail proof. The relevant results are obtained analytically above.

## Relationship to prior work
De Mauro, Majumdar and Schehr, arXiv:2601.20077 (2026), introduced and analyzed this same fixed-size batch-reset diffusion model. Their exact Fourier hierarchy, one- and two-point stationary marginals and the associated density-density correlation and spectral form factor (including the \(m/N\) large-population regime) are prior work. Their formulas already determine the macroscopic second-moment variance by pair integration. The present finding concerns the **law of the entire random empirical measure**, the explicit discounted-exponential law of its quadratic observable, all its cumulants, the full large-energy tail constant and a finite-population mean-square approximation bound; it does not claim prior model definitions or the previously available two-point consequences as new.

De Mauro, Biroli, Majumdar and Schehr, arXiv:2509.06658 (2025), establish a conditional-independent Gaussian-mixture description for the fully synchronous resetting model. At \(\theta=1\), the present limit reduces to this known single-age mixture. For \(0<\theta<1\), the limiting Gaussian mixture contains all of the common Poisson clock's backward gaps with geometrically decaying weights. Generic identities for independent discounted-exponential sums and infinite products are classical; their application alone is not claimed as novel.

## Limitations
The result is restricted to fixed \(\theta>0\); the extensive-to-subextensive batch-size crossover is not settled. Weak empirical-measure convergence does not assert a density in any strong function-space norm. The right-tail equivalent pertains to the limiting macroscopic observable, not a uniform joint limit in population size and energy. A broader previously established propagation-of-chaos theorem for a common marked environment or an exponential-perpetuity theorem could subsume individual steps; publication priority and independent mathematical validation have not been established. The numerical diagnostics are finite and cannot prove an infinite-limit result.

## References
1. G. de Mauro, S. N. Majumdar, and G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077, first public 2026-01-27. https://arxiv.org/html/2601.20077v3
2. G. de Mauro, M. Biroli, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, first public 2025-09-08. https://arxiv.org/abs/2509.06658
3. NIST Digital Library of Mathematical Functions, Chapter 17, \(q\)-series and \(q\)-products (notation). https://dlmf.nist.gov/17
