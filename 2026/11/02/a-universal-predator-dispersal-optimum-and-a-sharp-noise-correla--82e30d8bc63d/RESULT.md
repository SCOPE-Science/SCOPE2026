# A universal predator-dispersal optimum and a sharp noise-correlation trichotomy for two-patch prey fluctuations

## Finding

In a symmetric, locally stable two-patch linear predator–prey stochastic model, predator exchange suppresses stationary local prey fluctuations most effectively at one **exact** migration rate. With additive prey forcing and no direct predator forcing, the optimal per-direction predator migration rate is
\[
\boxed{v_*=\frac{\sqrt{bc}}{2}},
\]
where \(b>0\) and \(c>0\) are the predator-to-prey and prey-to-predator local linear response magnitudes. This optimum does **not** depend on local prey damping, prey migration, prey-noise intensity, or spatial prey-noise correlation (except when the antisymmetric prey mode has no forcing). Migration slower or faster than this rate gives strictly larger local prey variance. In particular, zero migration and the infinite-migration limit give *equal* local prey variance, and any finite nonzero migration strictly improves on both.

The more general theorem below also gives the exact optimum with additive predator noise, and classifies the case of perfectly spatially correlated forcing. These results are statements about stationary covariance in the **linearized** model, not extinction probabilities in a nonlinear ecological population.

## Assumptions and scope

For patches \(i=1,2\), with \(j=3-i\), let \(X_i,Y_i\) be **centered** prey and predator deviations from a common positive reference equilibrium, governed by
\[
\begin{aligned}
dX_i&=\bigl[-aX_i-bY_i+u(X_j-X_i)\bigr]dt+\sqrt q\,dW_i^x,\\
dY_i&=\bigl[cX_i+v(Y_j-Y_i)\bigr]dt+\sqrt r\,dW_i^y.
\end{aligned}
\]
Assume \(a,b,c>0\), \(u,v\ge0\), \(q>0\), and \(r\ge0\). The two unit-rate prey Brownian motions have instantaneous correlation \(\rho_x\in[-1,1]\), the two predator Brownian motions have correlation \(\rho_y\in[-1,1]\), and all prey noises are independent of all predator noises. Perfect correlation or anticorrelation is allowed, as is zero predator noise. The covariance matrices are positive semidefinite; no assumption of spatially independent forcing is made.

Define \(A=a+2u\), \(Q=q(1-\rho_x)\), \(R=r(1-\rho_y)\), and
\[
P(A,V;Q,R)=\frac{Q(V^2+AV+bc)+b^2R}{2(A+V)(AV+bc)}.
\]
For every finite predator dispersal rate \(v\ge0\) there is a unique stationary Gaussian law (possibly degenerate). The stationary variance of the prey deviation in either patch is exactly
\[
\boxed{\mathcal V(v)=\tfrac12\bigl[P(a,0;q(1+\rho_x),r(1+\rho_y))
+P(A,2v;Q,R)\bigr].}
\]
The following are necessary and sufficient global minimizer classifications over all finite \(v\ge0\):

**(i) Antisymmetric prey forcing, \(Q>0\).** There is exactly one minimizing \(v\in(0,\infty)\), namely
\[
\boxed{v_*=\frac{AbR+\sqrt{b(A^2R+Qc^2)(Qc+bR)}}{2Qc}.}
\]
The variance strictly decreases for \(0\le v<v_*\) and strictly increases for \(v>v_*\). If \(R=0\), this reduces to \(v_*=\sqrt{bc}/2\); if \(R>0\), then \(v_*>\sqrt{bc}/2\).

**(ii) No antisymmetric prey forcing but predator forcing, \(Q=0<R\).** The variance decreases strictly for every finite \(v\ge0\), with a finite infimum attained only in the limit \(v\to\infty\). There is no finite minimizer.

**(iii) No antisymmetric forcing, \(Q=R=0\).** The variance is independent of \(v\), so every finite migration rate minimizes it. The sum-mode fluctuations can remain nonzero.

If \(r=0\) and \(\rho_x<1\), the exact improvement at \(v_*\) relative to **both** \(v=0\) and the limit \(v\to\infty\) is
\[
\boxed{\mathcal V(0)-\mathcal V(v_*)=\lim_{v\to\infty}\mathcal V(v)-\mathcal V(v_*)
=\frac{Qbc}{4A(A+\sqrt{bc})^2}>0.}
\]
These boundary statements include \(u=0\) and the noise-correlation endpoints \(\rho_x=\pm1\), subject to the relevant case conditions.

## Proof

**Modal decomposition and existence.** Put \(X_{\pm}=(X_1\pm X_2)/\sqrt2\) and \(Y_{\pm}=(Y_1\pm Y_2)/\sqrt2\). The resulting independent-in-covariance symmetric and antisymmetric Ornstein–Uhlenbeck blocks have drift
\[
F(A_0,V_0)=\begin{pmatrix}-A_0&-b\\c&-V_0\end{pmatrix},
\]
with \((A_0,V_0)=(a,0)\) for the plus block, and \((A_0,V_0)=(a+2u,2v)\) for the minus block. Their diffusion covariance is diagonal with entries \((q(1\pm\rho_x),r(1\pm\rho_y))\). The trace is \(-A_0-V_0<0\) and determinant is \(A_0V_0+bc>0\), hence each drift is Hurwitz. Standard finite-dimensional Ornstein–Uhlenbeck theory therefore yields a unique (possibly degenerate) invariant centered Gaussian distribution, whose covariance is the unique solution of a continuous Lyapunov equation. The two blocks are uncorrelated because their Brownian covariance cross terms vanish; hence the variance of \(X_1=(X_++X_-)/\sqrt2\) is the half-sum of block variances.

**Exact block covariance.** For arbitrary \(A_0>0,V_0\ge0\), define \(p=\mathbb E X^2\), \(z=\mathbb E[XY]\), \(w=\mathbb E Y^2\) in a block, with prey and predator noise intensities \(Q_0,R_0\ge0\). The Lyapunov equation becomes
\[
-2A_0p-2bz+Q_0=0,\qquad
cp-(A_0+V_0)z-bw=0,\qquad
2cz-2V_0w+R_0=0.
\]
Multiplying the middle equation by \(V_0\), eliminating \(w\) with the third equation, and eliminating \(z\) with the first gives
\[
2(A_0+V_0)(A_0V_0+bc)p
=Q_0(V_0^2+A_0V_0+bc)+b^2R_0.
\]
No division by \(V_0\) is required, so the expression is valid also at \(V_0=0\). This establishes the claimed formula for \(\mathcal V(v)\).

**Global optimization.** The plus block is constant in \(v\). Differentiating the minus-block prey variance with respect to \(V=2v\) gives the exact identity
\[
\frac{\partial P(A,V;Q,R)}{\partial V}
=\frac{b\left[cQ(V^2-bc)-bR(A^2+2AV+bc)\right]}{2(A+V)^2(AV+bc)^2}.
\]
The denominator is strictly positive for all \(V\ge0\). If \(Q>0\), its numerator is a quadratic with positive leading coefficient, negative constant coefficient, and negative (or zero) linear coefficient. It has exactly one positive real root. Solving for that root yields
\[
V_* = \frac{AbR+\sqrt{b(A^2R+Qc^2)(Qc+bR)}}{Qc}.
\]
The derivative is negative before \(V_*\) and positive after it; since \(V=2v\), \(v_*=V_*/2\) is the unique global minimizer. For \(R=0\), the derivative numerator reduces to \(bcQ(V^2-bc)\), proving universality at \(V_*=\sqrt{bc}\). For \(R>0\), the critical equation forces \(V_*^2>bc\), so the optimum shifts strictly upward. If \(Q=0<R\), the derivative numerator is strictly negative at every finite \(V\ge0\); if \(Q=R=0\), it is identically zero. This proves all three cases.

**Exact improvement and endpoints.** When \(R=0\), direct subtraction gives
\[
P(A,V;Q,0)-\frac{Q}{2A}
=-\frac{bcQV}{2A(A+V)(AV+bc)}.
\]
Thus the endpoints \(V=0\) and \(V\to\infty\) have equal minus-block variance \(Q/(2A)\). At \(V=\sqrt{bc}=:w\),
\[
P(A,w;Q,0)=\frac{Q(A+2w)}{2(A+w)^2},
\]
and hence the minus-mode reduction is \(Qw^2/[2A(A+w)^2]\). The local patch variance is half the sum of modal variances, yielding the asserted gain \(Qbc/[4A(A+\sqrt{bc})^2]\).

**Example.** With \(a=2,b=4,c=9,u=1,q=5,r=0,\rho_x=0\), one has \(A=4,Q=5\), and the unique optimum is \(v_*=3\). At \(v=0\), and again as \(v\to\infty\), the local prey variance is \(15/16=0.9375\). At \(v=3\), it is \(33/40=0.825\); the reduction is \(9/80=0.1125\). These values concern centered stochastic deviations, not absolute prey density.

## Verification

The standalone standard-library file `verify.py` replays the **full four-dimensional Lyapunov equation**, without using the modal closed form to compute its matrix entries. It compares that result with the formula in three cases using exact rational arithmetic, and in 200 seeded randomly chosen admissible cases using numerical elimination. It additionally tests exact stationary gains and their universality across 120 seeded parameter configurations, the perfect spatial-correlation boundary, predator-only antisymmetric forcing, and the displayed numerical example. The code returns a nonzero status on any failed assertion. Its finite tests corroborate the analytical proof; they do not replace the derivative-sign argument.

## Relationship to prior work

Bonsall and Hastings (2004) established the ecological relevance of predator–prey metapopulation fluctuations, dispersal and demographic versus environmental stochasticity. Their full article develops fitted Markov-chain and stochastic population models; it does not state a sharp stationary prey-variance-minimizing predator-migration rate for the symmetric two-patch Ornstein–Uhlenbeck limit.

Quévreux, Barbier and Loreau (2020 preprint; 2021 journal publication) develop linearized trophic metacommunity fluctuation calculations, including related two-patch predator-only dispersal cases, but target interpatch **synchrony**, perturbation transmission and covariance decomposition. Their general Lyapunov framework is substantively related and provides a potentially broader computational starting point, but the inspected results do not give the exact three-regime global variance optimizer, the universal half-frequency rate, or the equal-endpoint positive-gain formula for this model.

Quévreux, Pigeault and Loreau (2021) likewise solve Lyapunov covariance equations in two-patch predator–prey models, but study density-dependent dispersal and synchrony inversion, not the exact variance-optimal rate with arbitrary correlated additive prey/predator noise. All three sources make covariance and spatial ecological fluctuation modeling prior knowledge; the contribution here is **the exact global optimum and its structural parameter independence/forcing trichotomy** under the specified linear model. This is a narrowly scoped analytical specialization, not a claim of priority for the Lyapunov technique.

## Limitations

The covariance result describes fluctuations around equilibrium in an additive-noise **linear** approximation. Such Gaussian deviations can be negative, and the theorem neither implies preservation of positive populations nor determines nonlinear extinction, invasion, rescue, synchrony optimality or empirical ecological best practice. The noise-correlation structure assumes independent prey/predator noise channels, and the two patches have symmetric local coefficients. Variance of an individual prey patch is the objective; the variance of total prey or other objectives may have different optimal rates. The published literature was checked against explicit claims and relevant full text, but historical priority against every possible specialized covariance calculation is not independently established.

## References

1. Bonsall, M. B., and Hastings, A. (2004). Demographic and environmental stochasticity in predator–prey metapopulation dynamics. *Journal of Animal Ecology* 73, 1043–1055. DOI: 10.1111/j.0021-8790.2004.00874.x (first published 29 October 2004).
2. Quévreux, P., Barbier, M., and Loreau, M. (2020 preprint; 2021 journal). Synchrony and perturbation transmission in trophic metacommunities. *The American Naturalist* 197, E188–E203. DOI: 10.1086/714131; preprint DOI: 10.1101/2020.01.21.914093.
3. Quévreux, P., Pigeault, R., and Loreau, M. (2021). Predator avoidance and foraging for food shape synchrony and response to perturbations in trophic metacommunities. *Journal of Theoretical Biology* 528, 110836. Public author-archived manuscript: https://sete-moulis-cnrs.fr/fr/content_page/download/605/955/30.
