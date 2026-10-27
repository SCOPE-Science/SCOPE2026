# A thermal gauge and exact heat coboundary for nonreciprocal harmonic networks

## Finding

For finite underdamped harmonic networks with positive bidirectional coupling on each undirected edge, *diagonal thermal calibration* is governed exactly by directed cycle products. On a tree (in particular a nonreciprocal harmonic chain), a positive diagonal gauge converts the force matrix to a symmetric one. This gives an **exact finite-time weighted heat identity**, not merely a relation between asymptotic average currents. At the corresponding bath-temperature ratios, a normalizable quadratic Gibbs law is invariant and is reversible under momentum reversal. For a chain of \(N\) oscillators with baths only at its endpoints, the constrained heat combination has the universal long-time characteristic function \((1+\Theta^2 z^2)^{-N}\) when initialized in that Gibbs state.

More precisely, write the stiffness matrix as \(\Phi_{ij}=-a_{ij}\) on adjacent distinct sites and \(\Phi_{ij}=0\) off the graph, where \(a_{ij},a_{ji}>0\) on every edge. The following assertions hold.

**(A) Cycle criterion and pathwise identity.** Positive diagonal matrices \(W=\operatorname{diag}(w_1,\ldots,w_N)\) satisfying \(W\Phi=\Phi^T W\) exist if and only if, for every oriented graph cycle \((i_0,i_1,\ldots,i_k=i_0)\),
\[
 \prod_{j=0}^{k-1}\frac{a_{i_j i_{j+1}}}{a_{i_{j+1}i_j}}=1.
\]
When one exists and \(W\Phi\) is positive definite, define
\[
 H_W(x,v)=\frac12v^TWMv+\frac12x^TW\Phi x.
\]
For each observation interval \([0,t]\), with the heat \(Q_i(t)\) *injected by* the bath at site \(i\) defined in the Stratonovich sense below, one has path by path
\[
 H_W(X_t,V_t)-H_W(X_0,V_0)=\sum_{i\in\mathcal B}w_i Q_i(t).
\]
The identity requires neither stationarity nor temperature calibration.

**(B) Calibrated reversibility.** If \(w_iT_i=\Theta>0\) for every thermostatted site and \(W\Phi\) is positive definite, the probability density proportional to \(\exp[-H_W/\Theta]\) is stationary, and the process obeys detailed balance with velocity reversal \((x,v)\mapsto(x,-v)\). Uniqueness and mixing follow whenever the corresponding Ornstein--Uhlenbeck drift is Hurwitz and the noise is controllable; these hypotheses hold for a connected positive-coupling chain with friction at its first site (and optionally its last), provided \(W\Phi\) is positive definite.

**(C) Exact long-time heat law for the chain.** Let \(N\ge2\). On the path graph write \(b_i=a_{i,i+1}>0\), \(c_i=a_{i+1,i}>0\), \(b=\prod_{i=1}^{N-1}b_i\), \(c=\prod_{i=1}^{N-1}c_i\), with positive masses and strictly positive endpoint frictions and no other baths. Choose \(w_1=c\) and recursively \(w_{i+1}=w_i b_i/c_i\), so \(w_N=b\). Assume \(W\Phi\) is positive definite. Then for all \(t\ge0\),
\[
 cQ_L(t)+bQ_R(t)=H_W(X_t,V_t)-H_W(X_0,V_0).
\]
If \(cT_L=bT_R=\Theta\) and the chain is started in its stationary distribution, then
\[
 \lim_{t\to\infty}\mathbb E\exp\{iz[cQ_L(t)+bQ_R(t)]\}
 =(1+\Theta^2z^2)^{-N}\qquad(z\in\mathbb R).
\]
Thus the limiting weighted heat is the difference of two independent \(\operatorname{Gamma}(N,\Theta)\) energies (shape and scale convention); its variance is \(2N\Theta^2\). Each fixed-time identity is exact, while the limit concerns the stationary large-time regime.

**(D) Sharp graph obstruction with all-site baths.** Suppose every vertex has positive friction and temperature and the linear drift has a strictly positive smooth invariant density. Then the stationary diffusion is reversible under the ordinary velocity reversal if and only if \(\operatorname{diag}(1/T_i)\Phi\) is symmetric positive definite. In particular, if even one directed graph cycle has unequal forward and backward coupling products, **no choice** of strictly positive site temperatures can produce velocity-reversal detailed balance. Conversely, on a tree with a positive-definite symmetrized stiffness, the calibration in (B) produces such reversibility.

## Assumptions and scope

The configuration space is \(\mathbb R^N\times\mathbb R^N\). The masses \(m_i>0\) comprise the diagonal matrix \(M\). The independent Brownian motions \(B_i\) drive only nodes \(i\) in a bath set \(\mathcal B\). With friction \(\gamma_i>0\) at those nodes and \(\gamma_i=0\) elsewhere, the stochastic dynamics is
\[
 dX_i=V_i\,dt,\qquad
 m_i\,dV_i=-(\Phi X)_i\,dt-\gamma_iV_i\,dt
 +\sqrt{2\gamma_iT_i}\,dB_i,
\]
where \(T_i>0\) for \(i\in\mathcal B\). The stochastic heat injected by bath \(i\), using the Stratonovich convention in the noise--velocity product, is
\[
 Q_i(t)=-\int_0^t\gamma_iV_i(s)^2\,ds
 +\sqrt{2\gamma_iT_i}\int_0^t V_i(s)\circ dB_i(s).
\]
This is the bath-work convention \(\int(\eta_i-\gamma_iV_i)\circ dX_i\), with the Stratonovich kinetic-energy correction understood. All matrices, degrees of freedom, masses, temperatures, and observation times are finite. No assertion is made for singular directed edges, nonquadratic interactions, or infinite graphs.

The graph may have cycles in (A), (B) and (D). The special chain in (C) is a path graph. Positive definiteness of \(W\Phi\) ensures confining weighted energy. The all-site converse in (D) assumes existence of a positive smooth invariant density; when \(\operatorname{diag}(1/T)\Phi\) is symmetric positive definite, existence, uniqueness and mixing follow directly from the positive friction at every node.

## Proof

**1. Diagonal gauge and cycles.** Symmetry of \(W\Phi\) at an edge is exactly \(w_i a_{ij}=w_j a_{ji}\), or \(w_j/w_i=a_{ij}/a_{ji}\). Multiplication along an oriented cycle proves necessity. Conversely, fix a root, assign \(w_{\mathrm{root}}=1\), and multiply these ratios along a path from the root to each vertex. The cycle condition makes this assignment independent of the path. Connectivity gives uniqueness of \(W\) up to a common positive scalar. This proves (A)'s criterion, including the automatic existence on any tree.

**2. Weighted heat equality.** Since \(M,W\) are constant diagonal matrices and \(W\Phi\) is symmetric, the Stratonovich chain rule gives
\[
 dH_W=V^TWM\circ dV+(W\Phi X)^T\circ dX
 =\sum_{i\in\mathcal B}w_i\left[-\gamma_iV_i^2\,dt+\sqrt{2\gamma_iT_i}\,V_i\circ dB_i\right].
\]
The two deterministic force terms cancel *exactly*. Integration proves the identity for arbitrary initial conditions and every finite time, simultaneously and almost surely. In Itô form both sides acquire the same finite correction \(\sum_{i\in\mathcal B}w_i\gamma_iT_i/m_i\,dt\), so no noise-induced term has been omitted.

**3. Calibrated Gibbs invariance and reversed detailed balance.** Set \(\rho(x,v)=Z^{-1}e^{-H_W(x,v)/\Theta}\), which is normalizable when \(W\Phi\) is positive definite. Decompose the generator as
\[
 L=A+\sum_{i\in\mathcal B}S_i,
 \quad A=v\cdot\nabla_x-(M^{-1}\Phi x)\cdot\nabla_v,
 \quad S_i=-\frac{\gamma_i}{m_i}v_i\partial_{v_i}+\frac{\gamma_iT_i}{m_i^2}\partial_{v_i}^2.
\]
The Hamiltonian vector field \(A\) preserves \(H_W\) and has zero Euclidean divergence; it is skew-adjoint in \(L^2(\rho)\). At \(w_iT_i=\Theta\), each \(S_i\) is the one-dimensional reversible Ornstein--Uhlenbeck generator for the \(v_i\)-marginal \(\exp[-w_im_iv_i^2/(2\Theta)]\); it is self-adjoint in \(L^2(\rho)\). With \(R(x,v)=(x,-v)\), \(RAR=-A\) and \(RS_iR=S_i\). Consequently \(L_\rho^*=RLR\), proving invariance and velocity-reversal detailed balance.

For the positive-coupling path with \(\gamma_1>0\), the deterministic weighted-energy derivative is \(-\sum_i w_i\gamma_iV_i^2\). An imaginary-axis drift eigenmode must have \(V_1=0\). If its frequency is nonzero, then \(X_1=0\) and the first nonzero coupling forces successively \(X_2=\cdots=X_N=0\); at zero frequency \(\Phi X=0\) and positivity again gives \(X=0\). Thus the drift is Hurwitz. Irreducibility of the tridiagonal stiffness propagates boundary noise to every normal mode, yielding a unique nondegenerate Gaussian invariant law and mixing. This establishes the advertised chain case without assuming all nodes have baths.

**4. Universal limiting heat difference.** For the path, direct recursion gives \(w_N=c\prod_i(b_i/c_i)=b\). Under the tuned endpoint temperatures, \(\rho\) is Gaussian with independent position and velocity blocks of covariances \(\Theta(W\Phi)^{-1}\) and \(\Theta(WM)^{-1}\), respectively. Diagonalizing these two positive quadratic forms shows that \(H_W/\Theta\) is one half the sum of \(2N\) independent standard Gaussian squares. Hence \(H_W\sim\operatorname{Gamma}(N,\Theta)\). By exponential mixing, the joint law of \(H_W(0)\) and \(H_W(t)\) converges to the product of two copies of this Gamma law. The pathwise identity now gives the asserted difference law. Its characteristic function is \((1-i\Theta z)^{-N}(1+i\Theta z)^{-N}\), and its variance is \(2N\Theta^2\).

**5. Necessity with baths at all vertices.** Write \(G=\operatorname{diag}(1/T_i)\). Assume a positive smooth stationary density \(\rho\) with velocity-reversal detailed balance, i.e. \(L_\rho^*=RLR\). Comparing the coefficients of \(\partial_{v_i}\) in these two generators, with every \(\gamma_i>0\), forces
\[
 \partial_{v_i}\log\rho=-\frac{m_i}{T_i}v_i.
\]
Therefore \(\rho(x,v)=f(x)\exp[-\sum_i m_iv_i^2/(2T_i)]\) up to normalization. The thermostat adjoints vanish on this velocity Maxwellian; the remaining stationary Fokker--Planck equation, after separating every coefficient of \(v_i\), requires
\[
 \nabla_x\log f=-G\Phi x.
\]
A gradient of a quadratic linear vector field exists exactly when \(G\Phi\) is symmetric. Normalizability on \(\mathbb R^N\) requires it to be positive definite. This proves necessity; sufficiency is step 3 with \(W=G\) and \(\Theta=1\). Symmetry at edges gives \(a_{ij}/T_i=a_{ji}/T_j\), so multiplying around a cycle proves the zero-circulation condition. Conversely a balanced connected graph admits positive calibration temperatures proportional to reciprocals of its gauge weights, provided the symmetrized stiffness is positive definite. This proves (D).

## Verification

The independently runnable `VERIFY.py` reproduces deterministic identities for numerous finite chains, a calibrated cyclic network and a non-calibratable directed triangle. It checks the symmetry \(W\Phi=\Phi^TW\), positive-definiteness, the exact stationary Lyapunov matrix equation for the underdamped Gaussian process, the predicted Gibbs covariance, the source-chain endpoint-weight normalization and the cycle-product obstruction. It also checks the form of the limiting characteristic function. Execute `python VERIFY.py` with NumPy and SciPy installed; the observed execution reported **591 deterministic checks passed**.

The general cycle characterization, generator adjoint identity and infinite-time Gamma difference law are proved above, not inferred from those finite calculations.

## Relationship to prior work

Cheng, Li and Tu [1] obtain the exact two-bath mean heat currents \(\langle j_L\rangle=\kappa b(cT_L-bT_R)\), \(\langle j_R\rangle=-\kappa c(cT_L-bT_R)\) and a rank-one long-time joint heat scaled cumulant-generating function. Their work supplies the physical model, the meaning of \(b,c\) and the temperature-calibration line. Neither the mean-current identity nor the rank-one scaled cumulants alone determine the **finite-time pathwise weighted heat equality**, the non-Gaussian order-one limiting law of its null-current combination, or the graph-cycle criterion for reversibility. Those are the additions proved here.

The diagonal symmetrizer criterion and cycle-product consistency themselves are classical graph and linear-algebra principles; they are used rather than claimed invented. Earlier related works [2--4] study heat, irreversibility and coupled thermal oscillators, including two-particle special cases. Their possible relevance to a shorter version of the finite-time identity is a material priority risk. The nontrivial claimed synthesis is the exact chain heat coboundary, its Gamma-difference limit and the thermally calibrated graph classification under explicit hypotheses.

## Limitations

The graph criterion concerns **diagonal** positive gauges and the ordinary velocity-reversal notion of detailed balance; it does not classify arbitrary changes of variables, nonlinear forces or reversals with altered parity assignments. The all-site necessity uses positive friction at every vertex and a smooth positive invariant density; for partially thermostatted graphs only sufficiency is claimed. A finite path with strict positive couplings and confining weighted stiffness meets the needed uniqueness/mixing conditions. The Gamma-difference law requires exact temperature calibration, stationarity and a long-time limit at fixed finite \(N\); it does not describe extensive heat fluctuations off calibration. The underlying cycle condition is known in other contexts, and specialized two-site precursors may exist.

## References

[1] Z. Cheng, G. Li and Z. C. Tu, *Energy Transport Structure and Fluctuation Theorem in Nonreciprocal Harmonic Chains*, arXiv:2609.09593v1 (first posted 2026-09-09), https://arxiv.org/abs/2609.09593 .

[2] S. A. M. Loos, S. Arabha, A. Rajabpour, A. Hassanali and E. Roldán, *Nonreciprocal nanoparticle refrigerators: design principles and constraints*, arXiv:2211.05502, https://arxiv.org/abs/2211.05502 .

[3] S. A. M. Loos and S. H. L. Klapp, *Irreversibility, heat and information flows induced by non-reciprocal interactions*, arXiv:2008.00894, https://arxiv.org/abs/2008.00894 .

[4] R. R. Netz, *Approach to equilibrium and non-equilibrium stationary distributions of interacting many-particle systems that are coupled to different heat baths*, arXiv:2009.07544, https://arxiv.org/abs/2009.07544 .
