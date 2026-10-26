# Single-vertex resetting: exact affine universality and cubic suppression of remote phase fluctuations

## Finding

On any finite connected undirected graph, consider the **unwrapped linear phase network** with deterministic drift \(\dot\theta=\omega-cL\theta\) and Poisson resets of one specified vertex to zero. At every positive reset rate, all stationary **mean phase differences** coincide exactly with their permanently pinned values. More strongly, for fixed graph, coupling and reset rate, every natural-frequency vector having the same total frequency \(\Omega\) gives the *same centered stationary distribution*: the only effect of changing the frequency profile is a deterministic translation.

If \(\Omega=0\), the stationary state is a point mass and stochastic resets generate no stationary fluctuations. If \(\Omega\ne0\), every pair of vertices has strictly positive stationary covariance. At high reset rate \(\lambda\), the reset-site variance is asymptotic to \(\Omega^2\lambda^{-2}\), but the covariance between **any two never-reset vertices** is asymptotic to a strictly positive graph-dependent constant times \(\lambda^{-3}\). This gives a universal one-power attenuation of remote fluctuations, with a coefficient determined by the grounded heat kernel.

## Assumptions and scope

Let \(G=(V,E)\) be a finite connected, simple, undirected graph with \(n=|V|\ge2\); let \(L\) be its combinatorial Laplacian and \(r\in V\) the sole reset vertex. Fix \(c>0\), \(\lambda>0\), and arbitrary \(\omega\in\mathbb R^V\), with \(\Omega=\sum_{i\in V}\omega_i\). Between events of one rate-\(\lambda\) Poisson process the unwrapped phases solve
\[
\dot\theta(t)=\omega-cL\theta(t).
\]
At each event, \(\theta_r\) is set to zero and all other coordinates are left unchanged. The process takes values in \(\mathbb R^V\), not on a phase torus; this is an exact statement about the linear phase model, not an assertion that the nonlinear Kuramoto sine model globally obeys it.

Write \(M=V\setminus\{r\}\), \(B=L_{MM}\), and \(a=-L_{Mr}\in\{0,1\}^{M}\). Connectivity implies \(B\) is positive definite. Set the pinned vector \(h_r=0\) and \(h_M=c^{-1}B^{-1}\omega_M\). Let \(J=I-e_re_r^T\). For any \(\lambda>0\) the process has a unique stationary law with finite second moments.

The stationary mean and covariance \(C\) satisfy exactly
\[
\mathbb E\theta=h+\frac{\Omega}{\lambda}\boldsymbol1,
\qquad
c(LC+CL)+\lambda(C-JCJ)=\frac{\Omega^2}{\lambda}e_re_r^T.
\]
The covariance is uniquely determined by the second equation. If \(\Omega\ne0\), \(C_{ij}>0\) for all \(i,j\in V\). In addition, as \(\lambda\to\infty\) with \(G,c,\omega\) fixed,
\[
C_{rr}=\frac{\Omega^2}{\lambda^2}+O(\lambda^{-3}),\qquad
C_{rM}=\frac{c\Omega^2}{\lambda^3}a^T+O(\lambda^{-4}),
\]
\[
C_{MM}=\frac{X}{\lambda^3}+O(\lambda^{-4}),\qquad
X=2c\Omega^2\int_0^\infty e^{-Bt}aa^Te^{-Bt}\,dt.
\]
Here the error terms are entrywise and \(X_{ij}>0\) for every pair \(i,j\in M\) if \(\Omega\ne0\). All limits and finite-rate formulas concern a fixed finite graph; uniformity as graph size increases is not asserted.

## Proof

**Stationarity and uniqueness.** Couple two copies by the same Poisson events. Their difference \(\delta\) obeys \(\dot\delta=-cL\delta\) between events, and \(\delta\mapsto J\delta\) at events. The generator gives
\[
\frac d{dt}\mathbb E\|\delta\|^2
=-2c\mathbb E(\delta^TL\delta)-\lambda\mathbb E\delta_r^2
\le-\kappa\mathbb E\|\delta\|^2,
\]
where \(\kappa\) is the smallest eigenvalue of \(2cL+\lambda e_re_r^T\), strictly positive by connectivity. The same quadratic drift bound with affine forcing supplies a uniform second-moment bound, and the synchronous coupling yields a unique stationary law by contraction (for instance in quadratic Wasserstein distance).

**Exact translation identity.** The pinned vector satisfies \(cLh=\omega-\Omega e_r\): the equality holds on \(M\) by the definition of \(h_M\), and summing the Laplacian rows yields its remaining component. Therefore \(Y=\theta-h\) obeys \(\dot Y=\Omega e_r-cLY\) between events. As \(h_r=0\), its resets are again \(Y\mapsto JY\). For \(\Omega\ne0\), divide by \(\Omega\) to obtain one universal process \(Z\) with drift \(e_r-cLZ\) and the same resets. Uniqueness proves the full stationary-law decomposition
\[
\theta_{\mathrm{st}}\;\stackrel d=\;h+\Omega Z_{\mathrm{st}}.
\]
For \(\Omega=0\), the difference process has zero forcing and contracts to zero, hence \(\theta_{\mathrm{st}}=h\) almost surely. Consequently, not merely the covariance but every centered finite-dimensional statistic of the stationary vector depends on \(\omega\) only through \(\Omega\).

**Mean and covariance.** The stationary first-moment equation is \((cL+\lambda e_re_r^T)m=\omega\). Summing components gives \(\lambda m_r=\Omega\); substituting back yields \(cL(m-h)=\Omega e_r-\lambda m_re_r=0\), so \(m=h+\Omega\boldsymbol1/\lambda\). In particular, \(m_i-m_j=h_i-h_j\) at *every* reset rate.

For the second moments apply the generator to \(\theta_i\theta_j\). On subtracting the products of the first moments, the affine jump yields the exact stationary equation
\[
 c(LC+CL)+\lambda(C-JCJ)=\lambda(e_re_r^Tm)(e_re_r^Tm)^T
 =\Omega^2e_re_r^T/\lambda.
\]
The homogeneous operator is strictly positive definite on matrices in the Frobenius inner product, because
\(2c\operatorname{tr}(C^TLC)+\lambda(\|C\|_F^2-\langle C,JCJ\rangle_F)>0\) for nonzero \(C\), by graph connectivity and pinning. Thus the solution is unique. Moreover this operator is the negative generator of two independent continuous-time simple graph random walks, each jumping across edges at rate \(c\), killed at rate \(\lambda\) whenever at least one coordinate equals \(r\). Its inverse has strictly positive entries, since every pair-state communicates with \((r,r)\) before killing with positive probability. Consequently \(C_{ij}>0\) for all pairs whenever \(\Omega\ne0\).

**Strong-reset expansion.** Partition the covariance equation into \(rr\), \(rM\), and \(MM\) blocks. With \(d_r=L_{rr}\), the three identities are
\[
(\lambda+2cd_r)C_{rr}-2ca^TC_{Mr}=\Omega^2/\lambda,
\]
\[
\lambda C_{rM}+c(d_rC_{rM}+C_{rM}B-a^TC_{MM}-C_{rr}a^T)=0,
\]
\[
BC_{MM}+C_{MM}B=aC_{rM}+C_{Mr}a^T.
\]
The positive-definite Lyapunov map \(Y\mapsto BY+YB\) has bounded inverse. Eliminating \(C_{MM}\) from the latter two equations shows \(C_{rM}=O(C_{rr}/\lambda)\) for sufficiently large \(\lambda\). The first equation then gives \(C_{rr}=\Omega^2\lambda^{-2}+O(\lambda^{-3})\). Substitution yields \(C_{rM}=c\Omega^2a^T\lambda^{-3}+O(\lambda^{-4})\), and the third identity yields the stated \(X\). Each connected component of \(G\setminus\{r\}\) contains a neighbor of \(r\), so \((e^{-Bt}a)_i>0\) for all \(i\in M\) and \(t>0\). Thus every entry of \(X\) is strictly positive for \(\Omega\ne0\).

## Verification

The standalone `verify_reset_graph.py` reproduces the first- and second-moment linear systems directly from the graph Laplacian and reset map, and independently solves their matrix equations. It executes 140 deterministic checks across six connected graph families, two distinct choices of reset vertex, frequency-profile changes preserving \(\Omega\), zero-total-frequency cases, positive-semidefinite covariance, strict covariance positivity, and both strong-reset coefficients. It also tests the pathwise affine identity under common Poisson-reset trajectories using exact matrix exponentials. Execute `python verify_reset_graph.py` with NumPy and SciPy installed; the program prints `PASS 140 independent checks` on the checked environment. The proof does not depend on numerical assertions.

For the two-vertex graph with sole edge and coupling \(c\), the formula specializes to
\[
C_{rr}=\frac{\Omega^2(\lambda+c)}{\lambda^2(\lambda+3c)},\qquad
C_{ss}=C_{rs}=\frac{c\Omega^2}{\lambda^2(\lambda+3c)},
\]
illustrating the quadratic-versus-cubic scaling exactly.

## Relationship to prior work

Paramero-Arias and Riascos, arXiv:2610.21842v1 (October 15, 2026), formulate Poisson resetting of an oscillator subset on a connected graph and develop the **infinite-reset-rate** grounded-Laplacian approximation (especially their sections II.1–II.3 and III); their finite-rate results are primarily simulations. The grounded operator \(B\), the network model, and the hard-pinning limit are therefore prior work, not new claims here. The present result is an exact finite-rate theorem for the **single-reset-node unwrapped linearized model**, including the pathwise frequency-profile universality and the separated covariance exponents.

Majumder, Chattopadhyay and Gupta, arXiv:2402.14921, derive subsystem-reset synchronization for globally coupled nonlinear Kuramoto populations with analytical approximations for finite reset rates; Majumder, Acharya and Gupta, arXiv:2604.04769, develop a Fourier/continued-fraction method for generalized mean-field Kuramoto models. Their stated observables and nonlinear mean-field regimes do not give the present finite-graph affine stationary law or the explicit cubic remote covariance asymptotic. The graph-grounding and linear jump-process calculations use established ideas; originality is claimed only for their particular synthesis and structural consequence in this network-reset setting.

## Limitations

The theorem is exact only for an **unwrapped linear network**, which describes the small-phase-difference approximation near synchronization. It does not establish an exact statement for sine-coupled circle-valued Kuramoto phases, finite noise, multiple reset nodes, heterogeneous reset clocks, directed graphs, or a graph-size/large-reset double limit. The stationary law is generally non-Gaussian; only its mean and covariance are given in closed linear systems. The full universal law \(Z_{\mathrm{st}}\) is characterized dynamically, not by a closed density. Independent verification of originality has not been performed.

## References

1. K. Paramero-Arias and A. P. Riascos, *Synchronization induced by stochastic subsystem resetting in complex networks*, arXiv:2610.21842v1 (2026), https://arxiv.org/abs/2610.21842.
2. R. Majumder, R. Chattopadhyay and S. Gupta, *Kuramoto model subject to subsystem resetting: How resetting a part of the system may synchronize the whole of it*, arXiv:2402.14921 (2024), https://arxiv.org/abs/2402.14921.
3. R. Majumder, A. Acharya and S. Gupta, *Analytical approach to subsystem resetting in generalized Kuramoto models*, arXiv:2604.04769 (2026), https://arxiv.org/abs/2604.04769.
