# Uniform phenotypic fixation and critical inverse-time resource laws in a Bayesian eco-evolutionary game

## Finding
Consider the Gaussian-perception four-phenotype replicator–resource model defined below. For every positive finite perception variance, every initially interior resource and every initial phenotype mixture assigning positive weight to the contingent phenotype that harvests high when perceiving repletion and low when perceiving depletion, that phenotype fixes exponentially, the resource converges to a unique parameter-determined state, and no nonconstant recurrent interior dynamics persists. In particular, at either critical environmental threshold, the resource approaches the corresponding boundary with an **exact universal inverse-time coefficient**, even though the other phenotype frequencies vanish exponentially:

\[
\lim_{t\to\infty}t n(t)=\frac{1}{\varepsilon(1+\theta)[-\omega'(0)]}
\quad\text{when }(1+\theta)\omega(0)=1,
\]
\[
\lim_{t\to\infty}t[1-n(t)]=\frac{1}{\varepsilon(1+\theta)[-\omega'(1)]}
\quad\text{when }(1+\theta)\omega(1)=1.
\]
The two critical equalities cannot occur simultaneously at finite variance. The statement is a complete, quantified convergence result on the specified initial-state domain; neither boundary-initial resources nor populations missing the advantageous phenotype are included.

## Assumptions and scope
Fix payoffs \(T>R\), \(P>S\), a resource relaxation parameter \(\varepsilon>0\), a low/high-harvest productivity ratio \(\theta>0\), a perception cutoff \(c\in(0,1)\), and a Gaussian noise level \(\sigma>0\), all finite. An environmental state \(n\in[0,1]\) produces a perceived-depletion probability
\[
\omega(n)=\frac{\int_0^c\exp(-(u-n)^2/(2\sigma^2))\,du}{\int_0^1\exp(-(u-n)^2/(2\sigma^2))\,du},\qquad p(n)=1-\omega(n).
\]
Four immutable phenotypes \(LL,LH,HL,HH\) prescribe an action under **replete perception first, depleted perception second**; each letter is low or high harvest. This is the indexing of the explicit four-strategy payoff matrix and its replicator equation. In particular, \(HL\) prescribes high under replete perception and low under depleted perception.

Let \(z=(z_{LL},z_{LH},z_{HL},z_{HH})\) belong to the probability simplex, and put
\[
 x=z_{LL}+z_{LH},\qquad y=z_{LL}+z_{HL},\qquad q=p(n)x+\omega(n)y.
\]
Given an opponent's low-harvest probability \(q\), the payoff for one's action in perceived repletion is \(Rq+S(1-q)\) for low harvest and \(Tq+P(1-q)\) for high harvest. In perceived depletion those two payoffs are exchanged. A phenotype's expected payoff \(\pi_j\) is the perception-probability-weighted sum of its two action payoffs. The dynamics are
\[
\dot z_j=z_j(\pi_j-\sum_k z_k\pi_k),\qquad
\dot n=\varepsilon n(1-n)[-1+(1+\theta)q].
\]
Assume \(0<n(0)<1\) and \(z_{HL}(0)>0\); other initial phenotype frequencies may vanish. Set
\[
\delta=\min(T-R,P-S)>0,\qquad
m=\min\{1-\omega(0),\omega(1)\}>0,\qquad \kappa=\delta m,
\]
and \(C=[1-z_{HL}(0)]/z_{HL}(0)\). Define \(F(n)=(1+\theta)\omega(n)-1\).

Then for all \(t\ge0\),
\[
0\le1-z_{HL}(t)\le C e^{-\kappa t}.
\]
The limiting resource \(n_\infty\) is independent of the initial interior resource and of the initial phenotype mixture:
\[
 n_\infty=\begin{cases}
0,&F(0)\le0,\\
1,&F(1)\ge0,\\
\text{the unique }n_*\in(0,1)\text{ with }\omega(n_*)=(1+\theta)^{-1},&F(0)>0>F(1).
\end{cases}
\]
These alternatives exhaust all parameters because \(F\) is strictly decreasing. At the equalities \(F(0)=0\) or \(F(1)=0\), the inverse-time limits in the Finding hold. No theorem is asserted for the exceptional invariant face \(z_{HL}(0)=0\).

## Proof
**1. Perception monotonicity.** Let \(U\in[0,1]\) have density proportional to \(e^{-(u-n)^2/(2\sigma^2)}\). Differentiating an expectation in the parameter \(n\) gives
\[
\omega'(n)=\sigma^{-2}\operatorname{Cov}_n(\mathbf1_{\{U\le c\}},U).
\]
The covariance is strictly negative: conditioned on \(U\le c\), the conditional mean is strictly smaller than the conditional mean on \(U>c\), and both events have positive probability. Thus \(\omega'(n)<0\) on the closed resource interval, \(0<\omega(n)<1\), and \(m>0\).

**2. Uniform selection.** Define the common conditional action advantage
\[
 d(q)=(T-R)q+(P-S)(1-q)\ge\delta.
\]
Directly comparing the four phenotype payoffs, for every opponent mixture and resource state,
\[
\pi_{HL}-\pi_{LL}=p(n)d(q),\qquad
\pi_{HL}-\pi_{LH}=d(q),\qquad
\pi_{HL}-\pi_{HH}=\omega(n)d(q).
\]
Each is at least \(\kappa\). The replicator logarithmic-ratio identity therefore yields
\[
\frac{d}{dt}\log\frac{z_j}{z_{HL}}=\pi_j-\pi_{HL}\le-\kappa
\]
whenever \(z_j(0)>0\). Frequencies initially zero remain zero. Summing the resulting three exponentially decaying ratios and using \(z_{HL}\le1\) proves the fixation bound.

**3. Resource convergence.** Since \(x\le1-z_{HL}\) and \(1-y\le1-z_{HL}\), we have
\[
|q-\omega(n)|=|p(n)x+\omega(n)(y-1)|\le1-z_{HL}\le Ce^{-\kappa t}.
\]
Thus the *exact coupled equation* becomes
\[
\dot n=\varepsilon n(1-n)[F(n)+e(t)],\qquad |e(t)|\le(1+\theta)Ce^{-\kappa t}.
\]
Writing \(s=\log[n/(1-n)]\) gives \(\dot s=\varepsilon[F(n)+e(t)]\). If \(F(0)<0\), the logarithmic drift is eventually uniformly negative, implying \(n\to0\); for \(F(0)=0\), strict monotonicity supplies eventually negative drift whenever \(n\ge a\), for every \(a>0\), and consequently the same limit. Symmetrically, \(F(1)\ge0\) forces \(n\to1\). If \(F(0)>0>F(1)\), strict monotonicity gives a unique \(n_*\). For each \(a>0\), after the transient error becomes sufficiently small, the logit drift is positive for \(n\le n_*-a\) and negative for \(n\ge n_*+a\). The attracting trapping interval can be entered and not exited, proving convergence to \(n_*\). All arguments preserve interiority because the logistic boundary factors make both endpoints invariant.

**4. Sharp critical relaxation.** Suppose \(F(0)=0\). The established convergence gives \(n\to0\), and smoothness gives
\[
 F(n)=-b_0n+O(n^2),\qquad b_0=(1+\theta)[-\omega'(0)]>0.
\]
For large time, the coupled equation implies
\[
 \dot n\ge -K n^2-B e^{-\kappa t}n
\]
for finite positive constants \(K,B\). Setting \(v=1/n\) and applying an integrating factor to \(v'\le K+B e^{-\kappa t}v\) proves \(v(t)=O(t+1)\); hence \(e^{-\kappa t}/n(t)\to0\). Returning to the exact equation,
\[
\frac{d}{dt}\frac1n=-\varepsilon\frac{1-n}{n}[F(n)+e(t)]\longrightarrow\varepsilon b_0.
\]
Integrating and dividing by \(t\) gives \(1/[t n(t)]\to\varepsilon b_0\), proving the first limit. At \(F(1)=0\), replace \(n\) by \(v=1-n\); the expansion \(F(1-v)=(1+\theta)[-\omega'(1)]v+O(v^2)\) yields precisely the second limit by the same reciprocal comparison.

**5. Recurrence.** A periodic orbit with \(z_{HL}>0\) cannot have another phenotype present because its ratio to \(z_{HL}\) strictly decreases. On the remaining pure-\(HL\) face, the scalar resource equation cannot have a nonconstant periodic solution. More generally, every trajectory in the stated domain converges to a single equilibrium, excluding nonconstant recurrent limit sets there.

## Verification
The standalone `verify.py` independently checks 336 exact rational payoff-advantage identities at multiple perception probabilities and opponent phenotypes. It also checks the sign of the differentiated truncated-Gaussian formula at 51 resource points and numerically integrates a coupled critical-threshold example, obtaining the dimensionless products \(\varepsilon(1+\theta)[-\omega'(0)]\,t\,n(t)\) at times \(3000\), \(10000\), and \(30000\) equal to approximately \(0.99437\), \(0.99805\), and \(0.99927\). Run with Python, NumPy, and SciPy using `python verify.py`. These finite checks support transcription and scale; the infinite-time assertions rest on the preceding analytic argument.

## Relationship to prior work
Patra, Das Bairagya, and Chakraborty's *Bayesian ecoevolutionary game dynamics* introduced exactly this resource-feedback model, its four-strategy payoff matrix, truncated-Gaussian perception, local equilibrium classification, and the pure-phenotype scalar resource equation. Their discussion of the global outcome relies in part on numerical absence of other attractors. Their equations already imply the fixed-point threshold conditions; those conditions are **not claimed as new** here. The present statement adds the quantified all-initial-interior-trajectory convergence for the *fully coupled* replicator and resource, including equality surfaces and their universal inverse-time critical coefficients.

Classical evolutionary-selection arguments already establish elimination of strictly dominated strategies under replicator dynamics; that abstract elimination principle is not claimed as new. The contribution lies in the resource-dependent **uniform** domination estimate, its coupling to an asymptotically autonomous environment, and the exact boundary-time asymptotics. Weitz et al.'s feedback-evolving replicator games admit oscillatory resource dynamics but lack this permanently uniformly dominant contingent phenotype and hence do not imply the conclusion. Analogous inverse-time boundary laws in unrelated population models do not establish the Gaussian perception-channel coefficient here.

## Limitations
The theorem assumes a fixed finite Gaussian noise level, positive selection payoff gaps, resource initial data strictly between endpoints, and positive initial mass on the dominant phenotype. It does not cover mutation, finite-population stochasticity, alternative resource laws, zero-noise limits, or the invariant population faces omitting that phenotype. No empirical prediction or independent mathematical audit is asserted. General dominated-strategy elimination and one-dimensional critical-slowing mechanisms are established mathematical tools; the scope of the new claim is the precise coupled-model classification and exact coefficient, with residual risk from unindexed work.

## References
1. A. Patra, J. Das Bairagya, and S. Chakraborty, *Bayesian ecoevolutionary game dynamics*, Physical Review E 111, 044401 (2025), DOI:10.1103/PhysRevE.111.044401; open preprint arXiv:2504.02399v1, Sections II–IV and Appendices B–C.
2. J. S. Weitz, C. Eksin, K. Paarporn, S. P. Brown, and W. C. Ratcliff, *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback*, PNAS 113, E7518–E7525 (2016), DOI:10.1073/pnas.1604096113.
3. J. Hofbauer and J. W. Weibull, *Evolutionary selection against dominated strategies*, Journal of Economic Theory 71, 558–573 (1996), DOI:10.1006/jeth.1996.0133.
