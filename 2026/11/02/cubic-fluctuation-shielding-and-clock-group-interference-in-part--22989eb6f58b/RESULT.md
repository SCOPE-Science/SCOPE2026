# Cubic fluctuation shielding and clock-group interference in partially reset oscillator networks

## Finding

For a connected finite weighted undirected graph with harmonic (linearized Kuramoto) coupling, resetting a nonempty proper subset of phases at common rate \(r\) produces a stationary law whose mean is **independent of how the reset nodes are grouped into shared clocks**. In contrast, grouping changes the leading stationary covariance on nodes that are never reset. Their covariance has a universal \(r^{-3}\) matrix-scale law with a positive-semidefinite grounded-Laplacian Gramian whose forcing is determined by reset-clock groups.

Write \(V=U\sqcup S\), with \(U,S\ne\varnothing\). Let \(L\) be the weighted graph Laplacian, let \(A=\kappa L\), \(\kappa>0\), and let \(\omega\in\mathbb R^V\) be a fixed vector of intrinsic frequencies. Between jumps, the real-valued phase deviations follow
\[
\dot\theta=\omega-A\theta.
\]
Partition \(S\) into nonempty disjoint groups \(G_1,\ldots,G_m\). Each group has its own independent Poisson clock of rate \(r>0\); at a jump of that clock, every phase in the group is set to zero, leaving all other phases unchanged. For \(H=A_{UU}\), \(B=A_{US}\), define
\[
q=H^{-1}\omega_U,\quad b=\omega_S-A_{SU}q,\quad
 b_g=P_g^{(S)}b,\quad D=\sum_{g=1}^m b_gb_g^{\mathsf T},
\]
where \(P_g^{(S)}\) is the diagonal coordinate projection onto \(G_g\) within \(\mathbb R^S\). Since the graph is connected and \(S\ne\varnothing\), \(H\) is positive definite. For the unique stationary covariance \(C(r)=\operatorname{Cov}(\theta)\), the exact limiting law is
\[
\boxed{\lim_{r\to\infty}r^3 C_{UU}(r)=Q,\qquad HQ+QH=2BDB^{\mathsf T},}
\]
or equivalently
\[
Q=2\int_0^\infty e^{-Ht}BDB^{\mathsf T}e^{-Ht}\,dt\succeq0.
\]
This is matrix convergence in any norm in fixed dimension. More precisely, \(C_{UU}(r)=r^{-3}Q+O(r^{-4})\). The leading matrix is nonzero exactly when \(Bb_g\ne0\) for at least one clock group. No claim of a positive \(r^{-3}\) leading coefficient is made when all these boundary forcings cancel.

The group-independent stationary mean has the exact Schur-complement representation
\[
\mu_S=(rI+T)^{-1}b,\qquad \mu_U=q-H^{-1}B\mu_S,\quad
T=A_{SS}-A_{SU}H^{-1}B\succeq0.
\]
In particular, \(\mu_S=r^{-1}b+O(r^{-2})\) and \(\mu_U=q-r^{-1}H^{-1}Bb+O(r^{-2})\). The grouping affects neither expression.

**Sharp three-node example.** Take the unweighted three-vertex star with an unreset center \(0\), reset leaves \(1,2\), \(\kappa=1\), and frequencies \((0,\nu,-\nu)\), \(\nu\ne0\). If both leaves are reset by the *same* Poisson clock, the unique stationary law has \(\theta_0=0\) exactly. If each leaf has an *independent* rate-\(r\) clock, then
\[
\boxed{\operatorname{Var}(\theta_0)=\frac{\nu^2}{(r+1)(r^2+5r+5)}>0.}
\]
Both protocols have the identical stationary mean \((0,\nu/(r+1),-\nu/(r+1))\). For the equally natural frequencies \((0,\nu,\nu)\), common resetting instead doubles the leading center variance: \(\lim_{r\to\infty}r^3\operatorname{Var}(\theta_0)=2\nu^2\) under one common clock, versus \(\nu^2\) under independent clocks. Thus no universal ordering of clock-group covariance exists even when the reset rates, graph, and stationary means are held fixed.

## Assumptions and scope

The graph is finite, connected, undirected, with strictly positive edge weights and at least two vertices. The reset set \(S\) and unreset set \(U\) are both nonempty. Each reset group is a block of a partition of \(S\); different groups have independent exponential clocks, all of the same rate \(r>0\). Phases are real-valued deviations governed **exactly by the linear equation shown**; there is no additive thermal noise, nonlinear sine coupling, or phase wrapping. The result holds for arbitrary fixed real frequency vectors, including zero frequencies. All limits keep the graph, partition, weights, coupling, and frequencies fixed as \(r\to\infty\).

The variance formula concerns the unique stationary probability measure on real phase space and its finite second moments. It does not silently equate the harmonic approximation with the full nonlinear Kuramoto process.

## Proof

**1. Existence, uniqueness, and moments.** Write \(P_g\) for the full-space diagonal projection onto group \(G_g\), \(P=\sum_gP_g\), and \(R_g=I-P_g\). The jump generator acting on a sufficiently regular function is
\[
\mathcal L f(x)=(\omega-Ax)\cdot\nabla f(x)
+r\sum_g[f(R_gx)-f(x)].
\]
If two solutions use the same jump clocks, their difference \(d\) obeys homogeneous drift \(\dot d=-Ad\) and jumps \(d\mapsto R_gd\). Consequently,
\[
\mathcal L\|d\|^2=-2d^{\mathsf T}Ad-rd^{\mathsf T}Pd
\le-\lambda_{\min}(2A+rP)\|d\|^2.
\]
The matrix \(2A+rP\) is positive definite: the kernel of \(A\) consists only of constant vectors and a nonzero constant vector cannot vanish on \(S\). Thus synchronous coupling contracts squared distance exponentially in expectation. The same calculation with the affine drift yields \(\mathcal L\|x\|^2\le-c\|x\|^2+C_\omega\) for some positive constants, giving an invariant probability with finite second moment by tightness of time averages; the contraction makes it unique (and gives exponential Wasserstein convergence). Invariance justifies all moment equations below.

**2. First moment.** The generator of each coordinate gives
\[
(A+rP)\mu=\omega.
\]
The matrix is positive definite. Eliminating \(\mu_U\) by its \(U\)-block equation proves the displayed Schur complement formulas and proves that clock grouping does not affect the stationary mean. Since the Schur complement \(T\) of the grounded block in \(A\) is positive semidefinite, its resolvent is analytic in \(1/r\) near zero and yields the two mean expansions.

**3. Exact covariance identity.** Let \(C=\mathbb E[(\theta-\mu)(\theta-\mu)^{\mathsf T}]\). Applying the generator to all quadratic monomials and subtracting the product-of-means equation gives
\[
AC+CA+r\sum_g(C-R_gCR_g)
=r\sum_gP_g\mu\mu^{\mathsf T}P_g.
\tag{1}
\]
This is an exact finite-dimensional linear system at every \(r>0\). Its solution is unique by the same quadratic contraction applied to two-copy differences; equivalently, its homogeneous generator decays exponentially. In particular, (1) is not an independence approximation: the \(R_gCR_g\) terms keep all same-clock correlations.

**4. Uniform high-rate expansion.** Reorder coordinates as \(U,S\) and set \(t=1/r\). From step 2, \(\mu_S=t b+O(t^2)\). Make the block substitution
\[
C_{SS}=t^2D_t,\qquad C_{US}=t^3X_t,\qquad C_{UU}=t^3Y_t.
\]
The \(SS\), \(US\), and \(UU\) blocks of (1), after division by their first nonzero powers of \(t\), have an analytic limiting triangular linear system at \(t=0\). The \(SS\) jump operator multiplies a diagonal or same-group matrix entry by one, and an entry between distinct groups by two. Its source has entry \(b_ib_j\) within each group and zero across groups. It therefore uniquely gives \(D_0=D=\sum_gb_gb_g^{\mathsf T}\). The \(US\) block gives \(X_0=-BD\); the \(UU\) block gives
\[
HY_0+Y_0H=-(BX_0^{\mathsf T}+X_0B^{\mathsf T})=2BDB^{\mathsf T}.
\]
The final Sylvester map is invertible because \(H\) is positive definite. The full rescaled linear system is therefore invertible for sufficiently small \(t>0\), and analytic perturbation (or finite-dimensional matrix inversion) shows \(D_t=D+O(t)\), \(X_t=-BD+O(t)\), and \(Y_t=Q+O(t)\). The Sylvester integral formula proves \(Q\succeq0\). Since \(D=\sum_g b_gb_g^{\mathsf T}\), the integral has zero trace precisely when every \(Bb_g=0\), establishing the stated nonzero criterion.

**5. Exact star and reverse ordering.** For the three-node star and opposite leaf frequencies, simultaneous resetting preserves the invariant line \(\theta_0=0\), \(\theta_1=-\theta_2\). The contraction in step 1 forces the unique stationary distribution onto this line, hence its center variance is zero. For independent leaf clocks put \(m=\nu/(r+1)\) and, by swap-and-sign symmetry, write the centered covariance as
\[
C=\begin{pmatrix}v&k&k\\k&w&z\\k&z&w\end{pmatrix}.
\]
Equation (1) gives \(v=k\), \((r+3)k-v-w-z=0\), \((r+2)w-2k=rm^2\), and \((r+1)z=k\). Solving yields the displayed strictly positive center variance. With equal leaf frequencies, \(b=(\nu,\nu)\), \(H=(2)\), and \(B=(-1,-1)\), so the Gramian formula gives leading center variance \(2\nu^2/r^3\) for one group and \(\nu^2/r^3\) for singleton groups. With opposite frequencies it instead gives \(0\) and \(\nu^2/r^3\), respectively. This completes the claimed comparison.

## Verification

The accompanying self-contained `VERIFY.py` uses exact rational Gaussian elimination to reconstruct stationary first moments and covariance equations for several finite graphs and reset partitions. It checks the explicit three-node formula at seven positive resetting rates, the opposite- and equal-sign limiting Gramians, and finite-rate convergence toward the Gramian for three partitions of a five-vertex graph. Run `python3 VERIFY.py` from the same directory. Its finite tests support algebraic reproducibility; the arbitrary-graph theorem and the \(r\to\infty\) limit follow from the preceding proof, not from these experiments.

## Relationship to prior work

Paramero-Arias and Riascos (arXiv:2610.21842v1, first public October 15, 2026) study subsystem resetting in coupled Kuramoto networks, with the fast-reset grounded-Laplacian limit and finite-rate numerical exploration. The pinned limit and the basic linearization are theirs. The present result addresses the unresolved stochastic fluctuations **at finite large reset rates**, distinguishes multiple independent clock groups from one shared clock, and identifies a cubic covariance attenuation and exact clock-correlation cancellation in the harmonic model.

General linear piecewise-deterministic Markov-process moment formulas, including those of Soltani and Singh (arXiv:1711.04884), already imply that a closed linear system for first and second moments can be formulated. The exact moment-closure mechanism is **not** claimed as new. The evaluated result is the graph-specific \(r^{-3}\) covariance Gramian with partition-dependent forcing, its nonvanishing criterion, and the strict stationary-noise cancellation/reversal on an elementary connected graph. Earlier work on collectively versus independently reset diffusions makes reset-induced correlation a known physical theme, but does not by itself state this graph-grounded oscillator covariance law.

## Limitations

Only the exact harmonic linear system is covered. No claim is made about the full sine-coupled Kuramoto model, stability of nonlinear locked phases, modulo-angle statistics, reset clocks with unequal rates or nonexponential waiting times, or a thermodynamic large-network limit. The \(O(r^{-4})\) remainder is for each fixed finite graph and partition, not uniform over growing graphs. The \(r^{-3}\) coefficient may vanish through clock-group cancellation, in which case a higher-order study is needed. The exact-moment part fits within general piecewise-deterministic moment theory, and a full-text comparison with all such general results remains a priority caveat.

## References

1. K. Paramero-Arias and A. P. Riascos, *Synchronization induced by stochastic subsystem resetting in complex networks*, arXiv:2610.21842v1 (first public 2026-10-15). https://arxiv.org/abs/2610.21842. Openly accessible main-text rendering also consulted at https://www.paperpeel.com/paper/2610.21842.
2. M. Soltani and A. Singh, *Linear piecewise-deterministic Markov processes with families of random discrete events*, arXiv:1711.04884 (2017). https://arxiv.org/abs/1711.04884. General stationary-moment framework; only publicly retrievable abstract and metadata were accessible for comparison.
3. P. C. Bressloff, *Kuramoto model with stochastic resetting and coupling through an external medium*, arXiv:2411.15534 (2024). https://arxiv.org/abs/2411.15534. Different globally reset indirect-coupling setting.
