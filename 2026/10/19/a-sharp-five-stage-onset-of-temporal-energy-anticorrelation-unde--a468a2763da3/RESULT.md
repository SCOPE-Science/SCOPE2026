# A sharp five-stage onset of temporal energy anticorrelation under collective renewal resetting

## Finding

Consider a stationary gas of at least two independent one-dimensional Brownian particles, each with diffusion generator \(D\partial_{xx}\), where \(D>0\). All particles are returned simultaneously to the origin after each independent renewal interval. Each interval is Erlang distributed with an **integer shape** \(k\geq1\) and stage rate \(\lambda>0\), that is, a sum of \(k\) independent exponential waiting times of rate \(\lambda\). Between collective resets the particles' Brownian noises are mutually independent. Let \(X_i(t)\) be a stationary particle position and define the two-time cross-particle energy covariance, for distinct particles \(i\ne j\), by

\[
\mathcal K_k(u)=\operatorname{Cov}\bigl(X_i(0)^2,X_j(u)^2\bigr),\qquad u\ge0.
\]

**Theorem (sharp clock-regularity threshold).** There is a dimensionless function \(C_k\), given constructively in the proof, such that

\[
\mathcal K_k(u)=\frac{4D^2}{\lambda^2}C_k(\lambda u).
\]

For every lag \(u\ge0\), \(\mathcal K_k(u)>0\) when \(1\le k\le4\). For every integer \(k\ge5\), the covariance takes strictly positive and strictly negative values on **infinitely many disjoint lag intervals**. More precisely, setting \(\zeta_k=e^{2\pi i/k}\),

\[
C_k(t)=2\operatorname{Re}\!\left[-\frac{e^{(\zeta_k-1)t}}{(\zeta_k-1)^2}\right]
+o\!\left(e^{(\cos(2\pi/k)-1)t}\right),\qquad t\to\infty,\quad k\ge5.
\]

The positive equal-time covariance is known explicitly, for every \(k\ge1\):

\[
\mathcal K_k(0)=\frac{4D^2}{\lambda^2}\frac{(k+1)(k+5)}{12}>0.
\]

Thus the onset of negative **time-lagged** cross-particle energy correlation occurs sharply between four and five exponential stages in the inter-reset clock, even though the same-time energy covariance is always positive. The boundary \(k=5\) is not an empirical threshold: it follows from an exact change in the dominant spectral mode.

## Assumptions and scope

Every \(k\) is a positive integer; \(\lambda,D>0\); there are at least two particles and \(i\ne j\). Brownian noise processes are independent across particle labels and independent of the common reset clock. Resets affect all particles simultaneously and set all positions exactly to zero. The stationary process is constructed from the equilibrium version of a renewal process with finite mean \(k/\lambda\); the resulting particle-position distribution has moments of every order. The theorem concerns a *cross-particle*, *two-time*, *squared-position* covariance. It does not claim negative ordinary position covariance or negative equal-time squared-position covariance, and it does not assert that the negative excursions have appreciable magnitude at arbitrarily large lag.

## Proof

**1. Reduction to a stationary renewal-age covariance.** Write \(A(t)\) for the elapsed time since the most recent collective reset. Conditional on the entire reset schedule, each \(X_i(t)\) is a centered Gaussian of variance \(2DA(t)\). Because the Brownian motions for two different particle labels are independent even when observed at different times, conditional independence implies

\[
\mathbb E[X_i(0)^2X_j(u)^2\mid\text{reset schedule}]
=(2D)^2 A(0)A(u),\qquad i\ne j.
\]

Consequently,

\[
\mathcal K_k(u)=4D^2\operatorname{Cov}(A(0),A(u)).
\]

Rescaling time by \(\lambda\) reduces the rest of the proof to unit stage rate. We work in these dimensionless units and denote the elapsed age by \(A(t)\) again.

**2. Finite-state Markov realization of the renewal age.** Represent each Erlang interval by \(k\) consecutive exponential stages. Let \(J(t)\in\{0,1,\ldots,k-1\}\) be the current stage, increasing by one at unit rate and cycling from \(k-1\) to zero. The age grows at speed one; at the transition \(k-1\to0\) the age is set to zero. The stage chain is stationary uniform, and, conditional on \(J(0)=j\), the age is a sum of \(j+1\) independent unit-exponential stages, hence has a Gamma law of shape \(j+1\). In particular,

\[
\bar a=\mathbb E A(0)=\frac{k+1}{2},\qquad
\mathbb E[A(0)^2\mid J(0)=j]=(j+1)(j+2).
\]

Introduce the centered phase correlations

\[
G_j(t)=\mathbb E[(A(0)-\bar a)\mathbf1_{\{J(t)=j\}}],\qquad
F_j(t)=\mathbb E[(A(0)-\bar a)A(t)\mathbf1_{\{J(t)=j\}}].
\]

By the generator of the stage-and-age process, with indices of \(G\) interpreted cyclically,

\[
\begin{aligned}
G_j'&=G_{j-1}-G_j, &&0\le j<k,\\
F_0'&=G_0-F_0,\\
F_j'&=G_j+F_{j-1}-F_j,&&1\le j<k.
\end{aligned}
\]

At the exceptional transition \(k-1\to0\), the incoming age is zero; thus there is **no** \(F_{k-1}\) term in the equation for \(F_0\). Direct Gamma moments yield the initial conditions

\[
G_j(0)=\frac{2j+1-k}{2k},\qquad
F_j(0)=\frac{(j+1)(2j+3-k)}{2k}.
\]

The target covariance is exactly

\[
C_k(t)=\operatorname{Cov}(A(0),A(t))=\sum_{j=0}^{k-1}F_j(t).
\]

These equations uniquely define \(C_k\) for all integers \(k\ge1\) and all \(t\ge0\), without simulation or an infinite-series approximation. Summing the conditional Gamma second moments and subtracting \(\bar a^2\) gives

\[
C_k(0)=\frac{(k+1)(k+5)}{12}.
\]

**3. Complete positivity for the first four shapes.** Solving these finite linear systems, or equivalently using their rational Laplace transforms, gives the following *exact* formulas:

\[
\begin{aligned}
C_1(t)&=e^{-t},\\
C_2(t)&=2e^{-t}-\tfrac14e^{-2t},\\
C_3(t)&=3e^{-t}-\tfrac23 e^{-3t/2}
\cos\!\left(\tfrac{\sqrt3}{2}t+\tfrac\pi3\right),\\
C_4(t)&=(4+\sin t)e^{-t}-\tfrac14e^{-2t}.
\end{aligned}
\]

For \(C_2\), the first positive term strictly dominates the second. For \(C_3\), use \(|\cos|\le1\) and \(e^{-3t/2}\le e^{-t}\); for \(C_4\), use \(4+\sin t\ge3\) and \(e^{-2t}\le e^{-t}\). All four functions are strictly positive for all finite \(t\ge0\). In particular, at the boundary shape \(k=4\), an oscillating mode exists but never overcomes a larger positive nonoscillatory mode.

For exact reproduction, the Laplace transforms of these four covariances, with Laplace variable \(p>0\), are respectively

\[
\frac1{p+1},\quad
\frac{7p+15}{4(p+1)(p+2)},\quad
\frac{8p^2+26p+27}{3(p+1)(p^2+3p+3)},\quad
\frac{15p^3+65p^2+104p+70}{4(p+1)(p+2)(p^2+2p+2)}.
\]

**4. Spectral dominance and infinitely many sign reversals at all larger shapes.** The cyclic system for \(G\) has eigenvalues \(\zeta^m-1\), where \(\zeta=e^{2\pi i/k}\), with eigenvectors whose \(j\)-th components are \(\zeta^{-mj}\). The homogeneous \(F\) subsystem is triangular with eigenvalue \(-1\) repeated \(k\) times. When \(k\ge5\), the two conjugate cyclic eigenvalues

\[
\zeta-1,\qquad\overline\zeta-1
\]

have real part \(\cos(2\pi/k)-1>-1\), strictly exceeding the real part of every other nonzero cyclic eigenvalue and all homogeneous \(F\) eigenvalues. The cyclic zero eigenvalue does not contribute because \(\sum_jG_j(0)=0\).

It remains essential to check that the slow conjugate modes **actually have nonzero coefficient** in the covariance. Projecting \(G(0)\) onto the eigenvector with components \(\zeta^{-j}\) gives

\[
a=\frac1k\sum_{j=0}^{k-1}\zeta^jG_j(0)
=\frac1{k(\zeta-1)}\ne0.
\]

For this forcing mode, the particular \(F\)-solution has component \(a(j+1)\zeta^{-(j+1)}e^{(\zeta-1)t}\), since the triangular recursion is solved by \(w_j=(j+1)\zeta^{-(j+1)}\). The sum over components has exact coefficient

\[
a\sum_{j=0}^{k-1}(j+1)\zeta^{-(j+1)}
=\frac1{k(\zeta-1)}\frac{k}{1-\zeta}
=-\frac1{(\zeta-1)^2}\ne0.
\]

The conjugate eigenmode contributes the complex conjugate coefficient. Every remaining mode decays at a strictly faster exponential rate (possibly times a fixed polynomial), proving the asserted two-term complex asymptotic. Its leading real part is a nonzero-amplitude sinusoid with frequency \(\sin(2\pi/k)>0\). Selecting successively large times where that sinusoid equals its positive and negative amplitudes makes the lower-order remainder negligible. By continuity the covariance therefore assumes each sign on infinitely many disjoint lag intervals. This establishes both directions of the sharp threshold and completes the proof.

## Verification

The accompanying standalone file `verify.py` implements the phase-and-age generator independently of the closed-form expressions, checks the four positive-shape formulas at 31 lags each, evaluates negative finite-lag covariances for shapes \(k=5,6,8\), verifies the complex residue identity for several shapes, and separately samples the stationary renewal clock directly rather than integrating its generator. The recorded numerical output is:

```text
124 closed-form phase-generator comparisons passed
phase-generator C(5,4.75) = -0.010594946
phase-generator C(6,4.60) = -0.136240698
phase-generator C(8,5.00) = -0.682183403
renewal MC k=2 t=1.00: 0.704616 versus matrix 0.701925
renewal MC k=4 t=2.00: 0.659886 versus matrix 0.659822
renewal MC k=8 t=5.00: -0.672403 versus matrix -0.682183
dominant complex-mode residue identities passed
```

The simulation is corroboration only; the infinite-lag sign-change claim follows from the exact spectral proof above. To reproduce, run `python verify.py` with NumPy and SciPy installed, from the directory containing both this document and the script.

## Relationship to prior work

De Mauro, Biroli, Majumdar and Schehr (2025/2026) establish collective-renewal resetting, the conditionally independent stationary Brownian-gas mixture, and the **equal-time** squared-position cross-particle covariance. Their Eqs. (18)–(33) concern same-time correlations as functions of elapsed observation time, not the stationary covariance between two different observation times. The common-age conditioning used in Step 1 is an acknowledged specialization of their framework. Eule and Metzger (2015/2016) already treat arbitrary renewal resetting and Gamma waiting-time families for **one-time** stationary distributions. Stojkoski and collaborators (2021) compute **one-particle** two-time correlations under Poisson resetting. Bengtsson (2022/2024) derives renewal-based covariance relations for a **binary alternating switch**, a different observable from continuously accumulated reset age. Classical stationary renewal-age theory supplies the gamma phase representation in Step 2, while the explicit sharp five-stage covariance-sign classification and its application to a two-particle energy measurement are the claims evaluated here.

## Limitations

The threshold is proved only for **integer** Erlang shapes, not arbitrary positive real Gamma shape parameters, and assumes perfect simultaneous resets, independent particle noise, and free Brownian motion. It concerns second-order fluctuations of squared positions across distinct particles, not cumulants of the total energy at finite particle number. The sign-changing component decays exponentially: the theorem does not imply sustained finite-amplitude negative correlations. Some broader renewal-process spectral or phase-type covariance theory could implicitly subsume the result; explicit full-text overlap is a remaining literature risk. The equations here prove neither experimental detectability nor universality beyond the specified model.

## References

1. G. de Mauro, M. Biroli, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, initial version posted 8 September 2025; *Physical Review E* **113**, 014120 (2026). https://arxiv.org/abs/2509.06658
2. S. Eule, J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, arXiv:1510.07876; *New Journal of Physics* **18**, 033006 (2016). https://arxiv.org/abs/1510.07876
3. V. Stojkoski, T. Sandev, L. Kocarev, A. Pal, *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, arXiv:2107.11686 (2021). https://arxiv.org/abs/2107.11686
4. H. Bengtsson, *Characteristics of the switch process and geometric divisibility*, arXiv:2205.06103 (2022); *Journal of Applied Probability* **61** (2024), 802–809. https://arxiv.org/abs/2205.06103
