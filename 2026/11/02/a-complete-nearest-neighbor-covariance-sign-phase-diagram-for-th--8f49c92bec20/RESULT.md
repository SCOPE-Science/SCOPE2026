# A complete nearest-neighbor covariance sign phase diagram for three-site asymmetric mass exchange

## Finding

An explicit family of closed three-site stochastic mass-exchange chains has stationary one-site means independent of the beta-splitting *concentration*, while its nearest-neighbor stationary covariance can change sign exactly once. The transition occurs on a sharp and explicitly classified region of the two bond-bias parameters.

Fix \(p,q,t>0\) in the dynamics below, and define
\[
Z=1+p+pq,
\qquad
\Delta=(1+p)(1+q)((1+p)t+1)((1+q)t+1)-q(t+1)(qt+1),
\]
\[
A(p,q)=p^2q(q+1)-p(q^2+4q+2)-3q-2.
\]
The process has a unique stationary law \(\mu_{p,q,t}\), with means \(\mathbb E X=(1,p,pq)/Z\) and
\[
\boxed{\operatorname{Cov}_{\mu_{p,q,t}}(X_0,X_1)
=\frac{p\,[A(p,q)t-2Z]}{2Z^2\Delta}.}
\]
The denominator is strictly positive for all \(p,q,t>0\). Accordingly, if \(A(p,q)\le0\), this covariance is strictly negative for every \(t>0\). If \(A(p,q)>0\), it is negative for \(0<t<t_*\), zero for \(t=t_*\), and positive for \(t>t_*\), where
\[
\boxed{t_*=\frac{2(1+p+pq)}{A(p,q)}.}
\]
Equivalently, for every fixed \(q>0\), the sign reversal is possible precisely when
\[
p>p_c(q)=\frac{q^2+4q+2+\sqrt{(q^2+4q+2)^2+4q(q+1)(3q+2)}}{2q(q+1)}.
\]
Thus the theory gives a complete algebraic phase diagram over all three positive parameters, rather than a single numerical witness.

For the integer-ratio example \(p=4\), \(q=2\), \(Z=13\) and \(A=32\), so \(t_*=13/16\). The complete stationary covariance matrix in this example is
\[
\operatorname{Cov}_{\mu_{4,2,t}}(X)
=\frac{1}{169(221t^2+114t+13)}
\begin{pmatrix}
12(23t+13)&4(16t-13)&-4(85t+26)\\
4(16t-13)&12(173t+39)&-4(535t+104)\\
-4(85t+26)&-4(535t+104)&40(62t+13)
\end{pmatrix}.
\]
The stationary means are always \((1,4,8)/13\); the \((0,1)\) covariance switches sign at \(13/16\) while the other two distinct-site covariances remain negative. A closed mass-conserving system therefore need not have exclusively negative spatial covariances.

## Assumptions and scope

Let \(\Delta_2=\{(x_0,x_1,x_2)\in[0,1]^3:x_0+x_1+x_2=1\}\). Independently, each adjacent edge \((0,1)\) and \((1,2)\) rings at Poisson rate one. At each left-edge event independently sample \(R\sim\operatorname{Beta}(t,pt)\), then replace
\[
(X_0,X_1,X_2)\mapsto
\big(R(X_0+X_1),(1-R)(X_0+X_1),X_2\big).
\]
At each right-edge event independently sample \(S\sim\operatorname{Beta}(t,qt)\), then replace
\[
(X_0,X_1,X_2)\mapsto
\big(X_0,S(X_1+X_2),(1-S)(X_1+X_2)\big).
\]
All samples and clocks are independent. There are no reservoirs, and the total mass is exactly one at every time. Here \(p,q\) set the two quenched splitting biases, while \(t\) changes the stochastic concentration but not \(\mathbb E R=1/(1+p)\) or \(\mathbb E S=1/(1+q)\). Claims hold for every real \(p,q,t>0\), except the displayed specialized matrix which concerns \(p=4,q=2\).

The two bond beta laws are compatible with a sitewise Dirichlet conditional-resampling law precisely when \(p=1\): otherwise the center site's shape parameters would need to be simultaneously \(pt\) and \(t\). In the positive-covariance region, no stationary Dirichlet law is possible, since a Dirichlet law with fixed total has strictly negative distinct-site covariances.

## Proof

**1. Unique stationary law.** The jump chain chooses either edge with probability \(1/2\). Its transition operator is Feller on the compact simplex, so a stationary probability measure exists. To prove uniqueness, couple two jump chains using exactly the same edge selections and beta variables. Their coordinate difference \(\delta\) has zero total. Each event is nonexpansive in \(\ell^1\). On a left-then-right pair, \(\|\delta_{n+2}\|_1=2R|\delta_{n,2}|\le R\|\delta_n\|_1\). On a right-then-left pair, \(\|\delta_{n+2}\|_1=2(1-S)|\delta_{n,0}|\le(1-S)\|\delta_n\|_1\). Same-edge pairs are nonexpansive. Averaging gives
\[
\mathbb E\|\delta_{n+2}\|_1\le
\left[\frac12+\frac{1}{4(1+p)}+\frac{q}{4(1+q)}\right]\|\delta_n\|_1.
\]
The bracket is strictly smaller than one for all positive \(p,q\). Iteration forces convergence in expected coupling distance. Testing any two stationary distributions against bounded Lipschitz observables yields equality. The continuous-time chain and its jump chain share stationary laws because the total event rate is the state-independent constant two.

**2. Fixed first-moment profile.** Put \(m_i=\mathbb E X_i\) under the stationary law. Vanishing of the generator applied to \(X_0\) and \(X_2\) implies
\[
m_0=\frac{1-m_2}{1+p},\qquad
m_2=\frac{q}{1+q}(1-m_0).
\]
These equations and mass conservation yield \(m_0=1/Z\), \(m_1=p/Z\), \(m_2=pq/Z\), independent of \(t\).

**3. Closed second-moment equations.** Define \(U=\mathbb EX_0^2\), \(W=\mathbb EX_2^2\), \(V=\mathbb EX_0X_2\), and the beta second moments
\[
a=\mathbb ER^2=\frac{t+1}{(1+p)((1+p)t+1)},\qquad
b=\mathbb E(1-S)^2=\frac{q(qt+1)}{(1+q)((1+q)t+1)}.
\]
Exactly, without a closure approximation,
\[
U=a(1-2m_2+W),\qquad
W=b(1-2m_0+U),
\]
\[
2V=\frac{m_2-W}{1+p}+\frac{q}{1+q}(m_0-U).
\]
Both \(a,b\) lie strictly between zero and one; hence \(1-ab>0\), and the three moment equations have a unique solution. Specifically,
\[
U=\frac{a[(1-2m_2)+b(1-2m_0)]}{1-ab},\qquad
W=\frac{b[(1-2m_0)+a(1-2m_2)]}{1-ab},
\]
with \(V\) given by the last displayed equation.

**4. Exact covariance and its phase region.** Since \(X_1=1-X_0-X_2\),
\[
\operatorname{Cov}(X_0,X_1)=-(U-m_0^2)-(V-m_0m_2).
\]
Substitute the rational expressions in Step 3, clear the positive denominators \(Z^2\) and \(1-ab\), and collect powers of \(t\). Direct polynomial simplification gives
\[
\operatorname{Cov}(X_0,X_1)
=\frac{p\bigl( [p^2q(q+1)-p(q^2+4q+2)-3q-2]t-2Z\bigr)}{2Z^2\Delta}.
\]
Here \(\Delta=(1+p)(1+q)((1+p)t+1)((1+q)t+1)(1-ab)>0\). Thus its numerator's affine sign proves the two regimes and the threshold \(t_*\), whenever \(A(p,q)>0\). As a quadratic in \(p\), \(A(p,q)\) has positive leading coefficient \(q(q+1)\), negative constant \(-(3q+2)\), and therefore exactly one positive zero; solving for it gives \(p_c(q)\) as displayed. The sign classification includes the boundary \(A=0\), where the covariance is strictly negative at every finite \(t>0\).

**5. Exact three-site witness and remaining covariances.** At \(p=4,q=2\) the preceding formula becomes \(4(16t-13)/[169(221t^2+114t+13)]\). Substitute \(p=4,q=2\) into the three moment equations: one obtains
\[
U=\frac{(t+1)(17t+13)}{13(221t^2+114t+13)},\quad
W=\frac{8(2t+1)(68t+13)}{13(221t^2+114t+13)},\quad
V=\frac{4t(34t+11)}{13(221t^2+114t+13)}.
\]
Using the fixed means and conservation gives the displayed complete covariance matrix. Its row sums vanish. The numerators of the two other distinct-site entries are \(-4(85t+26)\) and \(-4(535t+104)\), both strictly negative. The leading \(2\)-by-\(2\) principal minor is \(16(2735t^2+2210t+338)/[2197(221t^2+114t+13)^2]>0\), consistent with the expected covariance geometry. This proves all assertions.

## Verification

The included standard-library script `verify.py` performs exact rational-polynomial arithmetic: both the general \((p,q,t)\)-dependent covariance identity and the specialized full matrix are verified through coefficient-level rational identities rather than floating-point parameter scans. It tests the stationary generator moment equations, the threshold criterion and exact rational cases including \(t=13/16\). Run `python3 verify.py`. The exact algebra verifies the formula; the proof's coupling argument and sign reasoning are necessary to establish stationarity and the complete real-parameter classification. No finite simulation is used as an infinite-parameter proof.

For example, \(\operatorname{Cov}_{4,2,1/2}(X_0,X_1)=-80/84669\), whereas \(\operatorname{Cov}_{4,2,1}(X_0,X_1)=1/4901\). A separately performed Monte Carlo comparison agreed with both values within sampling uncertainty but is not used for any proof step.

## Relationship to prior work

Giusfredi, Avena and Politi [1] establish the general finite-segment beta-redistribution generator, a Gibbsian exact stationary **mean** profile, and localization laws for a binary-swapped Sinai environment. Their Section 7 explicitly observes that second moments require a larger linear system and treats small sizes numerically. The present \((p,q,t)\) family lies in their unrestricted edge-law definition, not generally in their binary-swapped special environment. The exact nearest-neighbor covariance sign **phase diagram** at unchanged means is not one of their results; neither the model nor the stationary mean formula is claimed as new.

Giardinà, Redig and van Tol [2] develop powerful generalized KMP theory with homogeneous symmetric beta kernels and reversible product marginals, together with boundary-driven mixtures; this does not itself give the incompatible asymmetric edge-kernel sign diagram. Carinci and collaborators [3] already prove positive association in the *reservoir-driven harmonic* model. Thus positivity of correlations per se is known and is not claimed as new: this result concerns an exact negative-to-positive transition under **fixed total mass** and **fixed means**. Capanna, Gabrielli and Tsagkarogiannis [4] consider reversible gradient families and reservoir-driven macroscopic nonequilibrium states, rather than this finite closed asymmetric-beta covariance formula.

Gilbert [5] analyzes higher correlations in stochastic energy-exchange processes with reservoirs. Only an abstract-level comparison was possible, and broader general correlation methods could subsume ingredients of this calculation. This is a qualified best-knowledge comparison of statements and their hypotheses, not a claim to have exhaustively proved global publication priority.

## Limitations

The structural sign classification is for two-parameter bond-bias ratios with a *common concentration scale* and equal positive edge rates on exactly three sites. It does not cover arbitrary independent beta concentrations, unequal edge rates, more sites, infinite-volume Sinai localization, reservoir drive, or full invariant joint densities. The two other pair covariances are classified as always negative **only for the displayed \(p=4,q=2\) example**, not for all \(p,q\). Existing positive-correlation theorems in open systems are credited. Some potentially relevant complete older higher-correlation texts were inaccessible, so publication-priority risk remains despite direct primary-paper and indexed-record comparisons.

## References

[1] M. Giusfredi, L. Avena, P. Politi, *Localization induced by Sinai disorder in mass-exchange models*, arXiv:2610.21777v1 (first public 15 October 2026), https://arxiv.org/html/2610.21777v1 .

[2] C. Giardinà, F. Redig, B. van Tol, *Intertwining and Propagation of Mixtures for Generalized KMP Models and Harmonic Models*, J. Stat. Phys. 192, 21 (2025), https://doi.org/10.1007/s10955-025-03393-1 .

[3] G. Carinci, C. Franceschini, D. Gabrielli, C. Giardinà, D. Tsagkarogiannis, *Solvable Stationary Non Equilibrium States*, J. Stat. Phys. 191, 10 (2024), https://doi.org/10.1007/s10955-023-03226-z .

[4] M. Capanna, D. Gabrielli, D. Tsagkarogiannis, *On a class of solvable stationary non equilibrium states for mass exchange models*, arXiv:2309.14836 (2023), https://arxiv.org/abs/2309.14836 .

[5] T. Gilbert, *Heat conduction and the nonequilibrium stationary states of stochastic energy exchange processes*, arXiv:1703.01240 (2017), https://arxiv.org/abs/1703.01240 .
