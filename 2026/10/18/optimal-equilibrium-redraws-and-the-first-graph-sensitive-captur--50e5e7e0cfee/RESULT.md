# Optimal equilibrium redraws and the first graph-sensitive capture correction

## Finding

**Theorem (finite reversible networks, fixed capture deadline).** Let \(Q\) be the irreducible generator of a finite reversible continuous-time Markov chain with equilibrium law \(\pi\). Let \(k_i\geq0\) be site-dependent killing rates, not all zero. Start a particle with law \(\pi\). At each prescribed reset time, conditional on its still being alive, replace its state by an independent draw from \(\pi\), without consuming time. Fix a deadline \(t>0\), and choose \(q-1\) strictly internal reset times, giving \(q\geq1\) positive segment lengths \(u_1,\ldots,u_q\) summing to \(t\).

Write \(K=\operatorname{diag}(k_i)\) and
\[
S(u)=\langle\mathbf1,e^{u(Q-K)}\mathbf1\rangle_\pi.
\]
The probability of missing capture by the deadline is exactly \(\prod_{a=1}^{q}S(u_a)\). If the killing rates are nonconstant, this probability has the **unique** minimum over all such schedules at \(u_a=t/q\), with value
\[
R_q(t)=\bigl[S(t/q)\bigr]^q.
\]
The optimal value decreases strictly with \(q\), and, for each finite \(q\), \(R_q(t)>e^{-\bar k t}\), where \(\bar k=\sum_i\pi_i k_i\). Its limit is \(e^{-\bar k t}\).

More precisely, define the equilibrium variance, centered third moment and graph Dirichlet energy by
\[
\sigma_k^2=\sum_i\pi_i(k_i-\bar k)^2,\qquad
\mu_{3,k}=\sum_i\pi_i(k_i-\bar k)^3,
\]
\[
\mathcal E_Q(k)=\frac12\sum_{i,j}\pi_i Q_{ij}(k_i-k_j)^2.
\]
Then, for each fixed \(t>0\), the optimally reset survival probability has the sharp high-budget expansion
\[
\boxed{\log R_q(t)=-\bar k t+\frac{\sigma_k^2t^2}{2q}
-\frac{[\mu_{3,k}+\mathcal E_Q(k)]t^3}{6q^2}+O_t(q^{-3}).}
\]
Thus the first finite-redraw penalty is determined only by the distribution of local killing strengths under equilibrium; network transitions first appear at the next order, through an explicit Dirichlet form. In the exceptional case \(k_i\equiv k>0\), **all** schedules have exactly the same survival probability \(e^{-kt}\).

For example, on the three-vertex path with symmetric adjacent jump rates \(r>0\), equilibrium law \((1/3,1/3,1/3)\), and killing rates \((0,2,4)\),
\[
\boxed{\log R_q(t)=-2t+\frac{4t^2}{3q}-\frac{4rt^3}{9q^2}+O_t(q^{-3}).}
\]
Changing the hopping rate leaves the first correction unchanged but changes the second.

## Assumptions and scope

The state space is finite, of cardinality at least two. All off-diagonal entries of \(Q\) are nonnegative, \(Q\mathbf1=0\), the chain is irreducible, and there is a strictly positive probability vector \(\pi\) satisfying detailed balance \(\pi_iQ_{ij}=\pi_jQ_{ji}\). The killing rates are finite, nonnegative and not all zero. Killing is an independent exponential local hazard accumulated along the live trajectory. Equilibrium resets use independent fresh samples and apply only if killing has not already occurred. Reset instants themselves have zero duration and no additional risk. All inequalities and uniqueness statements concern the fixed deadline \(t>0\); an optimizer is not claimed for protocols with reset costs or arbitrary restart-state distributions.

The inner product \(\langle f,g\rangle_\pi=\sum_i\pi_i f_i g_i\) is real. \(q\) denotes the number of positive live-trajectory segments, so \(q-1\) is the number of scheduled resets. The \(O_t\) bound holds for each fixed finite generator and killing vector as \(q\to\infty\).

## Proof

**Spectral survival and strict convexity.** In \(L^2(\pi)\), \(H=-Q+K\) is self-adjoint by detailed balance. For every real \(f\),
\[
\langle f,Hf\rangle_\pi
=\frac12\sum_{i,j}\pi_iQ_{ij}(f_i-f_j)^2+\sum_i\pi_i k_if_i^2.
\]
If this vanishes, irreducibility forces \(f\) constant and the nonzero killing vector forces that constant to be zero. Thus \(H\) is positive definite. Let its orthonormal eigenvectors be \(v_j\), with positive eigenvalues \(\lambda_j\). The no-reset survival probability is
\[
S(u)=\sum_j w_j e^{-\lambda_j u},\qquad
w_j=|\langle\mathbf1,v_j\rangle_\pi|^2\geq0,\quad\sum_jw_j=1.
\]
Writing \(F(u)=\log S(u)\), direct differentiation shows
\[
F''(u)=\operatorname{Var}_{\widehat w(u)}(\lambda_j)\geq0,
\qquad
\widehat w_j(u)=\frac{w_je^{-\lambda_j u}}{S(u)}.
\]
Equality for any \(u\) occurs exactly when \(\mathbf1\) belongs to a single eigenspace of \(H\). But \(H\mathbf1=k\), so this is equivalent to \(k\) being constant. Hence \(F\) is strictly convex on \([0,\infty)\) precisely in the nonconstant case; \(F(0)=0\).

**Exact schedule optimization.** Markov evolution with killing gives no-reset survival \(S(u)\). At any live reset, independently redrawing \(\pi\) renews this law, so the full survival factorizes as \(\prod_a S(u_a)\). Jensen's inequality yields
\[
\sum_{a=1}^{q}F(u_a)\geq qF(t/q).
\]
Strict convexity makes equal segment lengths the unique minimizer for nonconstant \(k\). For positive \(a,b\), strict convexity and \(F(0)=0\) imply \(F(a)+F(b)<F(a+b)\), so splitting a segment strictly reduces survival. In particular \(R_{q+1}(t)<R_q(t)\). Jensen applied to the spectral mixture gives \(S(u)\geq e^{-u\sum_jw_j\lambda_j}=e^{-\bar k u}\), strictly when \(k\) is nonconstant, because \(\sum_jw_j\lambda_j=\langle\mathbf1,H\mathbf1\rangle_\pi=\bar k\). Consequently \(R_q(t)>e^{-\bar k t}\) for all finite \(q\). Its stated limit follows from differentiability of \(F\) at zero. Constant \(k\) makes \(H\mathbf1=k\mathbf1\), and \(S(u)=e^{-ku}\), proving the equality boundary.

**First graph-sensitive correction.** Since the state space is finite, \(S\) is analytic at zero and positive on the nonnegative real axis. Let \(m_j=\langle\mathbf1,H^j\mathbf1\rangle_\pi\). Self-adjointness, \(Q\mathbf1=0\), and \(H\mathbf1=k\) give
\[
m_1=\bar k,\quad m_2=\sum_i\pi_i k_i^2,\quad
m_3=\sum_i\pi_i k_i^3+\langle k,-Qk\rangle_\pi.
\]
Detailed balance identifies \(\langle k,-Qk\rangle_\pi=\mathcal E_Q(k)\). Expanding the logarithm of \(S(u)=1-m_1u+m_2u^2/2-m_3u^3/6+O(u^4)\) yields
\[
F(u)=-\bar k u+\frac{\sigma_k^2}{2}u^2
-\frac{\mu_{3,k}+\mathcal E_Q(k)}6u^3+O(u^4).
\]
Substitute \(u=t/q\) and multiply by \(q\), obtaining the claimed \(O_t(q^{-3})\) remainder. On the indicated path, the centered third moment vanishes, the variance is \(8/3\), and the Dirichlet energy is \(8r/3\), giving the specialized formula.

## Verification

Execute `python verify.py` after installing the packages in `requirements.txt`. The checker builds finite reversible generators, independently computes spectral and matrix-exponential survival probabilities, verifies the first three generator moments, compares the unequal and equal segment schedules, checks monotonicity under refinement, and tests the displayed high-budget expansion. It also checks the three-site path coefficients at three hopping rates and a network with nonuniform equilibrium weights. All 111 assertions in the packaged run passed. These are finite computational checks of the analytic formulas, not substitutes for the proof for every finite state space.

## Relationship to prior work

Evans and Majumdar (2011) introduced a now-standard diffusive stochastic-resetting and capture setting with reset to a fixed position, where a nonzero optimal Poisson reset rate can occur. Eule and Metzger (2015/2016) developed general renewal descriptions for nonexponential resetting times and search. Pal and Reuveni (2016) proved broad renewal identities and an optimality principle for deterministic restart of the *mean* completion time. Van Moorsel and Wolter (2004), as described in Lorenz (2016), established equi-hazard necessary conditions for finite-restart deadline optimization; those conditions encompass the critical-point aspect of the equal-interval claim. Lorenz's full 2016 article examines generic fixed-cutoff algorithms and deadlines.

The claimed distinction is not the generic reset-product identity, equi-hazard stationarity, or log-convexity alone. It is the exact network-wide stationary-equilibrium classification with strict global finite-budget optimization and, centrally, the quantitative \(q^{-1}\) and \(q^{-2}\) terms isolating the **first graph-sensitive Dirichlet-energy correction** for imperfect spatial absorption. Such coefficients and their explicit equality boundary were not found in the inspected primary text. The 2004 paper's full text could not be examined, and differently indexed equivalent literature remains a genuine originality risk.

## Limitations

The graph is finite, the unreset transport is reversible and irreducible, and reset samples exactly the unreset equilibrium distribution. The order-two coefficient may have either sign because the centered killing skewness may be negative; no global sign is claimed for that coefficient alone. The expansion fixes \(t\) as the number of resets grows. Actual state-redraw costs, partial redraws, fixed reset sites, correlated schedules, irreversible driving, and optimization over reset locations are outside scope. The initial law and each redraw law must match \(\pi\); a point source need not satisfy this theorem. Independent verification beyond the supplied proof and finite calculations has not been performed.

## References

1. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, arXiv:1102.2704 (first posted 2011-02-14).
2. S. Eule and J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, arXiv:1510.07876 (first posted 2015-10-27); *New Journal of Physics* **18** (2016), 033006, doi:10.1088/1367-2630/18/3/033006.
3. A. Pal and S. Reuveni, *First Passage Under Restart*, arXiv:1607.06048 (first posted 2016-07-20).
4. A. van Moorsel and K. Wolter, *Optimal restart times for moments of completion time*, *IEE Proceedings: Software* **151** (2004), 219–223, doi:10.1049/ip-sen:20041090.
5. J.-H. Lorenz, *Completion Probabilities and Parallel Restart Strategies under an Imposed Deadline*, *PLOS ONE* **11** (2016), e0164605, doi:10.1371/journal.pone.0164605 (first journal publication 2016-10-12).
