# Pulse-time invariance and complete global selection in shared-crowding competition

## Finding

Consider any finite number \(N\ge2\) of species undergoing periodically repeated seasonal growth, shared crowding, and finitely many **species-specific, possibly asynchronous multiplicative pulses** per season. Between pulses, let
\[
\dot x_i=x_i\left(a_i(t)-\sum_{j=1}^{N}b_j(t)x_j\right),\qquad 1\le i\le N.
\]
At a pulse time \(\tau_\ell\), replace \(x_i\) by \(p_{i,\ell}x_i\), with \(p_{i,\ell}>0\). All coefficients and the pulse schedule repeat with a common period \(T>0\). Each \(b_j\) is nonnegative and has positive integral over a season. The initial state is strictly positive unless stated otherwise.

**Theorem (exact stroboscopic selection and timing invariance).** The map from the beginning of one season to the same phase in the next is exactly
\[
F_i(u)=\frac{\mu_i u_i}{1+\sum_{j=1}^{N}c_j u_j},\qquad
\mu_i=\exp\!\left(\int_0^T a_i(s)\,ds\right)\prod_{\ell}p_{i,\ell},\qquad c_j>0.
\]
The coefficients \(c_j\) are constructive finite sums of seasonal integrals (given below). In particular, moving any of the pulses within the season **without changing its multiplier** does not change any \(\mu_i\), even though it generally changes \(c_j\) and the eventual abundances. Every iterate is explicit:
\[
F_i^k(u)=\frac{\mu_i^k u_i}{1+\sum_{j=1}^{N}c_j u_j\sum_{q=0}^{k-1}\mu_j^q},\qquad k\ge0.
\]
Set \(\Lambda=\max_i\mu_i\), \(I=\{i:\mu_i=\Lambda\}\), and \(H=\sum_{i\in I}c_i u_i>0\). The **complete long-time trichotomy** is:

- If \(\Lambda>1\), every index outside \(I\) becomes extinct, whereas for \(i\in I\),
  \[
  F_i^k(u)\longrightarrow\frac{(\Lambda-1)u_i}{H}>0.
  \]
  For each \(j\notin I\), the sharper asymptotic is \(F_j^k(u)\sim[(\Lambda-1)u_j/H](\mu_j/\Lambda)^k\). Thus a unique maximizing multiplier selects one species, while a tie selects a neutral coexistence simplex with relative abundances inherited from the initial condition.
- If \(\Lambda=1\), all species become extinct. For \(i\in I\), \(kF_i^k(u)\to u_i/H\); for \(j\notin I\), \(k\mu_j^{-k}F_j^k(u)\to u_j/H\). Hence the dominant species have the sharp critical decay \(1/k\).
- If \(\Lambda<1\), all species become extinct geometrically, with
  \[
  \frac{F_i^k(u)}{\mu_i^k}\longrightarrow
  \frac{u_i}{1+\sum_j c_j u_j/(1-\mu_j)}.
  \]

Every nonzero fixed point lies in one of the simplices
\[
\left\{u\ge0: u_j=0\ (\mu_j\ne\lambda),\quad
\sum_{j:\mu_j=\lambda}c_ju_j=\lambda-1\right\},
\qquad\lambda\in\{\mu_i:\mu_i>1\}.
\]
There are **no stroboscopic cycles of least period greater than one**, hence no seasonal subharmonic cycles. At a fixed point supported on the maximizing group \(I\) with \(\Lambda>1\), the multiplier spectrum is \(1\) with multiplicity \(|I|-1\), \(1/\Lambda\), and \(\mu_j/\Lambda\) for \(j\notin I\). The coexisting tied-winner simplex is normally attracting but has neutral compositional directions.

## Assumptions and scope

The functions \(a_i(t)\) are real-valued, bounded, piecewise continuous, and \(T\)-periodic. The functions \(b_i(t)\) are bounded, piecewise continuous, nonnegative, and \(T\)-periodic, with \(\int_0^T b_i(s)\,ds>0\) for every species. There are finitely many predetermined pulse phases in \((0,T]\), repeated exactly each season. At each phase, the species-specific factors \(p_{i,\ell}\) are fixed positive real numbers (including \(1\) for unaffected species). Solutions are right-continuous at pulses. Start immediately after phase \(0\) and sample immediately after the last event at phase \(T\), so each one-period map includes exactly one instance of each pulse. Species labels and initial state may be arbitrary, with \(u_i>0\) for the complete global selection assertion. The fixed-point classification also permits zero components.

The shared-crowding hypothesis means the effect of species \(j\), namely \(b_j(t)x_j\), is **the same in each receiver species' per-capita equation**. This rank-one restriction is essential; no conclusion is asserted for general competition matrices, density-dependent pulse multipliers, migration between species, or state-dependent pulse times.

## Proof

**1. Exact flow between pulses.** For any flow interval \([s,t]\), define
\[
E_i(s,v)=\exp\!\left(\int_s^v a_i(r)\,dr\right),\qquad
B_i(s,t)=\int_s^t b_i(v)E_i(s,v)\,dv.
\]
For initial \(z=(z_1,\ldots,z_N)\) at time \(s\), put
\[
D(v)=1+\sum_j z_j B_j(s,v),\qquad
x_i(v)=\frac{z_iE_i(s,v)}{D(v)}.
\]
Since \(D(v)\ge1\) and \(D'(v)=\sum_jb_j(v)z_jE_j(s,v)\), differentiation gives
\(\dot x_i/x_i=a_i-D'/D=a_i-\sum_jb_jx_j\) almost everywhere. This proves the solution formula, positivity, and absence of finite-time blow-up on the interval.

**2. Closure under multiple asynchronous pulses.** Write \(L_{m,c}(u)_i=m_i u_i/(1+c\cdot u)\). For positive vectors \(m,n\) and nonnegative \(c,d\), direct substitution gives
\[
L_{n,d}\circ L_{m,c}=L_{n\odot m,\ c+m\odot d},
\]
where \(\odot\) denotes componentwise multiplication. An ODE flow interval has \(m_i=E_i(s,t)\), \(c_i=B_i(s,t)\); a pulse has \(m_i=p_{i,\ell}\) and \(c_i=0\). Ordered composition therefore gives an exact one-period map \(F=L_{\mu,c}\), with
\[
\mu_i=\prod_{r=1}^{R}m_i^{(r)},\qquad
c_i=\sum_{r=1}^{R}c_i^{(r)}\prod_{q=1}^{r-1}m_i^{(q)}.
\]
Every summand is nonnegative. Because each \(b_i\) is positive on a set of positive measure in the season, \(c_i>0\). Multiplying the factors \(m_i^{(r)}\) yields the displayed seasonal exponential and all pulse factors; the pulse phases do not enter \(\mu_i\). The \(c_i\) generally do depend on the pulse phases.

**3. Iterates and exhaustive asymptotic trichotomy.** Induction using the same composition identity yields
\[
F_i^k(u)=\frac{\mu_i^k u_i}{D_k},\qquad
D_k=1+\sum_jc_ju_j\sum_{q=0}^{k-1}\mu_j^q.
\]
If \(\Lambda>1\), divide \(D_k\) by \(\Lambda^k\) to get the strictly positive limit \(H/(\Lambda-1)\). The first case and its subdominant rates follow. If \(\Lambda=1\), \(D_k/k\to H\), establishing the critical rates. If \(\Lambda<1\), every geometric series converges and \(D_k\to 1+\sum_jc_ju_j/(1-\mu_j)\). These three cases exhaust every possible positive multiplier vector. By the finite composition formulas in step 2, convergence at pulse times gives convergence to the corresponding within-period orbit profiles at every fixed regular seasonal phase.

**4. Fixed points and absence of subharmonics.** If \(F(u)=u\ne0\), then for every active species \(i\), \(\mu_i=1+c\cdot u>1\). Thus all active species share one multiplier \(\lambda>1\) and \(c\cdot u=\lambda-1\), giving exactly the stated fixed simplices. Conversely, any point of such a simplex is fixed. If \(F^q(u)=u\) for some positive integer \(q\), the explicit ratio law
\[
\frac{F_i^k(u)}{F_j^k(u)}=\frac{u_i}{u_j}\left(\frac{\mu_i}{\mu_j}\right)^k
\]
for active coordinates forces their multipliers to be equal. On their common support, the scalar quantity \(s=c\cdot u\) obeys \(s\mapsto\lambda s/(1+s)\), a strictly increasing one-dimensional map. It has no nonfixed periodic orbits, so \(F(u)=u\) and there are no subharmonics.

**5. Stability on the winning simplex.** Differentiating gives
\[
\frac{\partial F_i}{\partial u_j}
=\frac{\mu_i\delta_{ij}}{1+c\cdot u}
-\frac{\mu_i u_i c_j}{(1+c\cdot u)^2}.
\]
At a top-group fixed point, the block for supported coordinates is \(\mathrm{Id}-u^*c^\top/\Lambda\): its radial eigenvalue is \(1/\Lambda\), while its \(|I|-1\) tangent eigenvalues are \(1\). Rows for the absent coordinates are diagonal with eigenvalues \(\mu_j/\Lambda\); an upper-triangular block structure leaves the spectrum unchanged. All eigenvalues normal to the top simplex have modulus strictly less than \(1\). This proves the stated normal attraction, not hyperbolicity of individual coexisting points.

**6. Exact phase-shift witness.** Take two species, \(T=1\), \(a_i=0\), \(b_i=1\) and pulses \(p_1=2\), \(p_2=3\). Put species 1's pulse at phase \(1/4\). If species 2's pulse occurs at phase \(3/4\), then \((\mu_1,\mu_2)=(2,3)\) and \((c_1,c_2)=(7/4,3/2)\). If its pulse moves to phase \(1/4\) while all pulse factors are kept fixed, then \((c_1,c_2)=(7/4,5/2)\). Species 2 is the winner in both schedules, but its limiting postperiod density changes **exactly** from \(4/3\) to \(4/5\). This shows that outcome invariance is nontrivial: abundance responds to timing even though winner identity cannot.

## Verification

Run `python3 verify.py` from the directory containing this document. The standalone standard-library checker uses exact rational arithmetic to independently compare the ordered flow–pulse composition with the effective map and its iterates, checks the two different timing coefficients and survivor amplitudes in the exact witness, and checks a fixed neutral simplex and its two nontrivial matrix invariants. It also tests finite iterates in subcritical, critical, supercritical, and tied-multiplier cases. Every reported check passed. These finite tests verify the algebra used in the proof; they do not establish infinite-time conclusions independently of step 3.

## Relationship to prior work

Courcelle, MacDonald, and Patel (2026) develop sufficient, robust permanence criteria for periodically pulsed Lotka–Volterra systems. Their available abstract and a detailed secondary account concern general Morse-decomposition and invasion-growth methods, not the present closed-form composition and **asynchronous timing-invariant selection** theorem. The preprint's full primary text was not examined, which leaves a genuine historical-priority risk.

Schreiber (2025) treats a wider class of flow–kick systems, including impulsive Lotka–Volterra models, and derives permanence and extinction tests via invasion graphs. Hosack, El-Hachem, and Beeton (2025) explicitly state the general multispecies Leslie–Gower recurrence; the stroboscopic map here is a **special equal-row instance** of that known recurrence and is not itself claimed as a newly invented map. The additional assertions are its exact realization under **multiple staggered pulses**, its closed iterates and sharp critical rates, its complete neutral-simplex and subharmonic classification, and invariance of winner selection under rearranged pulse timings. Sacker (2011) also treats periodic multispecies Leslie–Gower systems, proving global coexistence under a weak-coupling hypothesis; that theorem does not imply the equal-row strong-overlap and neutral regimes here. Neither accessible primary treatment established the present all-parameter pulse-timing and critical-rate conclusions.

Inamine and collaborators (2022) compare pulses and continuous disturbance in two-species competition, primarily through simulations of a non-rank-one interaction matrix, rather than an all-parameter exact formula. Xiao and collaborators (2026) investigate nonautonomous competition with impulsive pollution and species interventions using comparison and Lyapunov criteria, with an auxiliary pollutant system and a general interaction matrix. Their qualitative conclusions do not give the present exact projective reduction.

## Limitations

The model assumes fixed pulse phases, positive multiplicative (not additive) pulses, periodic coefficients, and a rank-one shared-crowding interaction matrix. Species-specific receiver sensitivities, nonlinear releases, or state-dependent pulse times can change competitive outcomes when pulses move and are outside this theorem. A neutral coexistence simplex is normally attracting but **not** robustly asymptotically stable in every composition direction. The formula concerns deterministic dynamics and excludes demographic noise. The motivating recent preprint's full text remains inaccessible, and the search cannot certify global historical novelty. No independent validation is asserted.

## References

1. E. Courcelle, J. Shaw MacDonald, and S. Patel, *Persistence of n-Species Lotka–Volterra Models with Periodic Pulses*, arXiv:2609.09343, first posted September 8, 2026. https://arxiv.org/abs/2609.09343
2. S. J. Schreiber, *Coexistence and Extinction in Flow-Kick Systems: An Invasion Growth Rate Approach*, Journal of Mathematical Biology **91**, 50 (2025), https://doi.org/10.1007/s00285-025-02283-0.
3. G. R. Hosack, M. El-Hachem, and N. J. Beeton, *Stability of Difference Equations with Interspecific Density Dependence, Competition, and Maturation Delays*, Bulletin of Mathematical Biology **87**, 137 (2025), https://doi.org/10.1007/s11538-025-01515-0.
4. H. Inamine, A. Miller, S. Roxburgh, A. Buckling, and K. Shea, *Pulse and Press Disturbances Have Different Effects on Transient Community Dynamics*, The American Naturalist **200** (2022), https://doi.org/10.1086/720618.
5. R. J. Sacker, *Global Stability in a Multi-Species Periodic Leslie–Gower Model*, Journal of Biological Dynamics **5** (2011), 549–562, https://doi.org/10.1080/17513758.2011.554891.
6. L. Xiao, H. Qi, Y. Qi, and B. Liu, *Dynamics of a Non-Autonomous Competitive System under Simultaneous Impulsive Pollution and Anthropogenic Disturbances*, Electronic Research Archive **34** (2026), 3678–3695, https://doi.org/10.3934/era.2026166.
