# Persistent cross-lane jump correlations in the dilute two-lane exclusion ring

## Finding
Consider the symmetric, totally right-moving two-lane product-stationary exclusion process described below, on two periodic lanes of the same length \(N\geq3\), with exactly one particle on each lane. Let \(X_t\) and \(Y_t\) be the **numbers of particle hops** on the respective lanes during \([0,t]\), not the currents through a particular fixed bond. Write
\[
\delta=\frac a2,\qquad w=p+\delta,\qquad
R_N=\frac{N-2}{p}+\frac2w,
\]
\[
E_N=\frac{\delta^2}{N}\left[
\frac{2(1-2/N)^2}{w}
+\frac{4(N-3)(N-2)(N-1)}{3N^2p}
\right].
\]
Under stationary initialization, the exact asymptotic cross-lane hop-count covariance per unit physical time is
\[
\boxed{C_N:=\lim_{t\to\infty}\frac{\operatorname{Cov}(X_t,Y_t)}{t}
=\frac12\left(p+\frac aN-\frac{N}{R_N}+E_N\right).}
\]
For every \(N\ge3\), \(p>0\), and \(a>-p\), this quantity is strictly positive if and only if \(a\ne0\), even though the stationary positions of the two particles are independent and uniform. The large-ring single-particle-per-lane limit is
\[
\boxed{\lim_{N\to\infty}C_N=\frac{a^2}{6p}.}
\]
However, at every fixed finite \(t\), stationary hop counts converge jointly with all moments, as \(N\to\infty\), to independent Poisson variables of mean \(pt\). In particular,
\[
\boxed{\lim_{t\to\infty}\lim_{N\to\infty}
\frac{\operatorname{Cov}(X_t,Y_t)}t=0,
\qquad
\lim_{N\to\infty}\lim_{t\to\infty}
\frac{\operatorname{Cov}(X_t,Y_t)}t=\frac{a^2}{6p}.}
\]
The assertion concerns one **unified** finite-size and dilute-limit covariance theorem; the Poisson limit specifies its physically important order-of-limits boundary.

## Assumptions and scope
Each lane is a directed periodic lattice of \(N\ge3\) sites, with sites interpreted modulo \(N\), exactly one distinguishable particle in each lane, and no lane changes. A jump of a particle from site \(k\) to \(k+1\) on either lane occurs at rate
\[
p+\frac a2\bigl(\eta^{\mathrm{other}}_k+\eta^{\mathrm{other}}_{k+1}\bigr),
\]
where \(\eta^{\mathrm{other}}_j\in\{0,1\}\) denotes occupation of the other lane; only unoccupied destinations on the particle's *own* lane are allowed. The parameters obey \(p>0\) and \(a>-p\), making rates \(p\), \(p+a/2\), and \(p+a\) positive in the parent many-particle process. In the one-per-lane sector only \(p\) and \(w=p+a/2\) occur. This is the symmetric, totally asymmetric specialization of the product-stationary class studied in the references.

There are no common imposed Poisson jump clocks between the lanes. Jump counts are recorded in units of individual forward hops; for a current averaged per site/bond, the normalization must be changed accordingly. All limits here take the long-time limit at **fixed finite** \(N\) before the large-ring limit, except where the reverse order is explicitly stated.

## Proof
**1. Relative coordinate and stationarity.** Let the occupied sites be \(x,y\), and set \(d=(y-x)\pmod N\). Define edge conductances
\[
c_0=c_1=w,\qquad c_2=\cdots=c_{N-1}=p.
\]
An \(X\)-hop changes \(d\) to \(d-1\) at rate \(c_d\), and a \(Y\)-hop changes \(d\) to \(d+1\) at rate \(c_{d+1}\). Thus the relative generator is
\[
(Qf)(d)=c_d(f(d-1)-f(d))+c_{d+1}(f(d+1)-f(d)).
\]
Every unoriented edge has equal forward and reverse rates. Consequently \(Q\) is reversible with uniform stationary law \(\pi(d)=1/N\). The original two-position chain is translation invariant, irreducible and has direct in/out balance, giving the unique uniform product law on the \(N^2\) position pairs. The mean hop rate on either lane is \(p+a/N\).

**2. Total-count variance.** Put \(S_t=X_t+Y_t\). Its conditional jump intensity is \(\lambda_d=c_d+c_{d+1}\), with stationary average \(\bar\lambda=2(p+a/N)\). Let the zero-mean \(h\) solve the finite Poisson equation \(-Qh=\lambda-\bar\lambda\). The process
\[
S_t-\bar\lambda t+h(d_t)-h(d_0)
\]
is a square-integrable martingale. Its quadratic-variation rate under the stationary relative chain is \(\bar\lambda+2\mathcal E\), where
\[
\mathcal E=\langle\lambda-\bar\lambda,h\rangle_\pi
=\frac1N\sum_{d=0}^{N-1}c_d(h(d)-h(d-1))^2.
\]
Indeed, the cross term in the squared corrected jump sizes averages to \(2\langle Qh,1\rangle_\pi=0\), and each undirected edge contributes twice to the squared-corrector term. Boundedness of \(h\) for fixed \(N\) means endpoint corrections do not affect variance divided by \(t\).

The edge fluxes \(J_d=c_d(h(d)-h(d-1))\) satisfy
\[
J_d-J_{d+1}=\lambda_d-\bar\lambda,
\qquad \sum_d \frac{J_d}{c_d}=0.
\]
The unique solution is
\[
J_0=\delta(1-2/N),\qquad
J_1=-\delta(1-2/N),\qquad
J_d=\frac{2\delta}{N}(2d-1-N)\quad (2\le d\le N-1).
\]
Using the exact finite sum
\[
\sum_{d=2}^{N-1}(2d-1-N)^2=\frac{(N-3)(N-2)(N-1)}3,
\]
we obtain \(\mathcal E=E_N\), and hence
\[
\lim_{t\to\infty}\frac{\operatorname{Var}(S_t)}t
=2\left(p+\frac aN\right)+2E_N.
\]

**3. Difference-count variance.** Put \(D_t=Y_t-X_t\), the integer lift of the relative position. A forward edge traversal from \(d\) to \(d+1\) adds \(+1\) to \(D_t\); the reverse adds \(-1\). A harmonic corrector for this periodic reversible walk has positive effective edge increments \(\Delta_d=\mathsf J/c_{d+1}\), where consistency over one circuit requires \(\sum_d\Delta_d=N\). Thus \(\mathsf J=N/R_N\). The corrected lift is a martingale with quadratic-variation rate
\[
\frac2N\sum_{d=0}^{N-1}c_{d+1}\Delta_d^2
=\frac{2N}{R_N}.
\]
As for \(S_t\), the bounded periodic corrector does not affect variance growth, so \(\lim_{t\to\infty}\operatorname{Var}(D_t)/t=2N/R_N\).

**4. Cross covariance, strict positivity and the large-ring limit.** The exact identity \(\operatorname{Cov}(X_t,Y_t)=(\operatorname{Var}(S_t)-\operatorname{Var}(D_t))/4\) gives the displayed \(C_N\). The number \(p+a/N=(2w+(N-2)p)/N\) is the arithmetic mean of the positive edge conductances, while \(N/R_N\) is their harmonic mean. Their difference is nonnegative, and strictly positive when \(a\ne0\). Also \(E_N\ge0\), with equality exactly when \(a=0\). Directly taking \(N\to\infty\) in the explicit formula yields \(p+a/N-N/R_N\to0\) and \(E_N\to a^2/(3p)\). Hence \(C_N\to a^2/(6p)\).

**5. Reversed order of limits.** Start with the uniform independent stationary positions and construct independent rate-\(p\) Poisson jump processes. Couple the interacting trajectories using the common portions of their jump clocks, adding/removing jumps only when the two particles occupy sites whose relative separation belongs to \(\{0,1,N-1\}\). Before the first disagreement, the baseline relative position is uniform at every time. The total disagreement hazard there is bounded by \(|a|\), and the stationary probability of the three potentially interacting separations is \(3/N\). Hence the probability of any coupling disagreement before a fixed time \(t\) is bounded by \(3|a|t/N\). All hop counts are dominated by Poisson counts of a rate bounded uniformly in \(N\), giving uniform integrability of all fixed positive integer moments. Thus the joint law and every mixed moment converge at fixed \(t\) to two independent \(\operatorname{Poisson}(pt)\) variables; their covariance tends to zero. This establishes the stated noncommutation.

## Verification
The standalone standard-library program `verify.py` independently differentiates the principal eigenvalue of a two-field tilted relative-chain generator, solving the corresponding *mixed* Poisson equations over exact rational numbers. It checks the reduced-chain formula for \(N=3,\ldots,10\) over five sets of rational rates, then checks nine cases against an independent physical \(N^2\)-state position generator; it verifies uniform stationarity, positive covariance, zero coupling and rational large-ring convergence, for a total of 60 tracked exact check cases. Run `python3 verify.py` in the directory containing the program. These finite checks are cross-checks; the argument above proves the all-size claim.

## Relationship to prior work
The symmetric right-moving hopping-rate family and its product stationary law are already established in Popkov and Schütz (2002, arXiv:cond-mat/0211659, Eq. (4)), and the broader two-lane product model is described by Popkov and Peschel (2001). Subsequent exact stationary current and hydrodynamic or dynamical-universality results include Popkov et al. (2015), Schmidt et al. (2026), and Popkov (2026), arXiv:2605.06949, Eqs. (7)–(11). These rates and the product measure are **not** presented as new. The specific result here concerns finite-sector **joint time-integrated lane hop-count fluctuations**, their exact all-\(N\) covariance, and the noncommuting dilute and long-time limits. Stationary product measures and one-time current-density formulas alone do not determine such two-time cumulants. No directly matching theorem was located in the primary materials inspected, but exhaustive publication priority is not asserted.

## Limitations
The theorem is about exactly one particle on each of two equally long periodic lanes, equal base rates, symmetric coupling, no reverse hops, and stationary initial positions. It does not give finite-density covariance, external-clock correlations, unequal-rate asymmetry, fixed-bond counting covariance, a uniform-in-\(N\) time-to-asymptopia estimate, or an intermediate scaling law when \(t\) grows with \(N\). The reversibility exploited is only that of the **relative-coordinate chain**, not detailed balance of the driven physical particle dynamics. Source novelty remains subject to independent expert literature review.

## References
- V. Popkov, *Multilane Asymmetric Exclusion Process with stationary Bernoulli measure*, arXiv:2605.06949 (first submitted 2026-05-07), https://arxiv.org/html/2605.06949.
- V. Popkov and G. M. Schütz, *Shocks and excitation dynamics in a driven diffusive two-channel system*, arXiv:cond-mat/0211659 (2002), https://arxiv.org/abs/cond-mat/0211659.
- V. Popkov and I. Peschel, *Symmetry breaking and phase coexistence in a driven diffusive two-channel system*, arXiv:cond-mat/0106216 (2001), https://arxiv.org/abs/cond-mat/0106216.
- V. Popkov, A. Schadschneider, J. Schmidt and G. M. Schütz, *Fibonacci family of dynamical universality classes*, arXiv:1505.04461 (2015), https://arxiv.org/abs/1505.04461.
- J. Schmidt, Ž. Krajnik and V. Popkov, *Universality in driven systems with a multiply-degenerate umbilic point*, arXiv:2601.04116 (2026), https://arxiv.org/abs/2601.04116.
