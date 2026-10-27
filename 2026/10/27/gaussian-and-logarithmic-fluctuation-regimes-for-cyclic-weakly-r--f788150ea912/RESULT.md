# Gaussian and logarithmic fluctuation regimes for cyclic weakly reinforced urns

## Finding
For the continuous-time weakly reinforced Pólya urn model on a simple cycle with \(d\ge3\) vertices, unit-rate independent vertex clocks, power exponent \(0\le\alpha<1\), and arbitrary deterministic strictly positive finite initial edge weights, label the \(d\) edges cyclically and write \(N(t)\in\mathbb R^d\) for their weights. Set \(Y(t)=N(t)-t\mathbf1\), and let \(S\) be the cyclic coordinate shift.

Define the symmetric matrix \(J=(\alpha/2)I-(\alpha/4)(S+S^{-1})\). Its Fourier eigenvalues are \(\beta_k=\alpha\sin^2(\pi k/d)\), for \(0\le k<d\). Put \(m_d=1\) when \(d\) is even and \(m_d=\cos^2(\pi/(2d))\) when \(d\) is odd, and let \(\alpha_c(d)=1/(2m_d)\).

**Subcritical theorem.** For every \(0\le\alpha<\alpha_c(d)\),
\[
 t^{-1/2}Y(t)\;\Longrightarrow\;\mathcal N_d\bigl(0,(I-2J)^{-1}\bigr).
\]
In the real Fourier eigenmode with eigenvalue \(\beta_k\), the limiting variance is \((1-2\beta_k)^{-1}\). The limiting total-count mode has variance one; the orthogonal Fourier modes are independent Gaussian components.

**Critical theorem.** At \(\alpha=\alpha_c(d)\), let \(P_*\) be the Euclidean orthogonal projection onto the eigenspace \(\ker(J-I/2)\), and \(Q_*=I-P_*\). Then
\[
 \left(\frac{P_*Y(t)}{\sqrt{t\log t}},\;\frac{Q_*Y(t)}{\sqrt t}\right)
 \Longrightarrow (G_*,G_\perp),
\]
where the Gaussian vectors are independent, \(\operatorname{Cov}(G_*)=P_*\), and \(\operatorname{Cov}(G_\perp)=Q_*(I-2J)^{-1}_{Q_*}Q_*\), the inverse being taken only on the range of \(Q_*\). Equivalently the noncritical Fourier eigenmode of eigenvalue \(\beta_k<1/2\) has limiting variance \((1-2\beta_k)^{-1}\).

The critical fluctuation space has dimension one for even \(d\) (the alternating mode) and dimension two for odd \(d\) (a conjugate pair of highest-frequency modes). Thus the threshold itself and the number of logarithmically enhanced directions distinguish odd from even cycles.

## Assumptions and scope
The underlying graph is the ordinary finite simple cycle \(C_d\), \(d\ge3\), with undirected edge labels modulo \(d\). At each vertex, a rate-one Poisson clock rings independently; the clock chooses one of its two incident edges with probability proportional to the current edge weight to power \(\alpha\), then increments the chosen weight by one. Only a single edge changes at a ring. The initial vector is deterministic with all entries in \((0,\infty)\). The limits concern real time \(t\to\infty\) and fixed \(d\), fixed \(\alpha\). The fixed-graph law of large numbers \(N(t)/t\to\mathbf1\) almost surely follows from Qin (2026, Theorem 1.1), whose permitted domain includes the hypotheses here.

At the critical value \(\alpha_c(d)\), the symbol \((I-2J)^{-1}_{Q_*}\) is not the inverse on the full space: it is the inverse of the strictly positive restriction \(Q_*(I-2J)Q_*\) to \(\operatorname{ran}Q_*\). The two limiting Gaussian vectors are supported on mutually orthogonal subspaces and are independent.

## Proof
**1. Drift and noise.** For any positive vector \(x\), the edge-selection intensity is
\[
 \Phi_e(x)=\frac{x_e^\alpha}{x_e^\alpha+x_{e-1}^\alpha}
 +\frac{x_e^\alpha}{x_e^\alpha+x_{e+1}^\alpha}.
\]
It is homogeneous of degree zero and \(\Phi(\mathbf1)=\mathbf1\). The counting-process compensation gives a square-integrable vector martingale \(M\) with
\[
 dN(t)=\Phi(N(t))\,dt+dM(t),\qquad
 d\langle M\rangle_t=\operatorname{diag}(\Phi(N(t)))\,dt.
\]
Off-diagonal predictable covariations vanish because there are no simultaneous edge increments. The intensity of any edge is bounded by two. In particular, jumps of \(M\) have bounded norm, and the established law of large numbers gives \(t^{-1}\langle M\rangle_t\to I\) almost surely.

Direct differentiation at \(\mathbf1\) yields
\[
 D\Phi(\mathbf1)=J=\frac\alpha2 I-\frac\alpha4(S+S^{-1}).
\]
The discrete Fourier basis diagonalizes \(J\); its eigenvalues are \(\alpha\sin^2(\pi k/d)\). Their maximum is \(\alpha m_d\). The location and multiplicity of that maximum are a unique alternating real frequency for even \(d\) and the pair of frequencies \((d-1)/2,(d+1)/2\) for odd \(d\). These facts give the threshold and the asserted dimensions.

**2. Localized rate estimate.** Set \(\delta(t)=N(t)/t-\mathbf1=Y(t)/t\) for \(t>0\). Its semimartingale drift is \(t^{-1}F(\mathbf1+\delta)\), where \(F(x)=\Phi(x)-x\), and its martingale increment is \(t^{-1}dM(t)\). Taylor expansion in a fixed positive neighborhood of \(\mathbf1\) gives
\[
 F(\mathbf1+z)=-(I-J)z+O(\|z\|^2),\qquad
 \langle z,F(\mathbf1+z)\rangle
 \le-(1-\beta_{\max}-\eta)\|z\|^2
\]
for every sufficiently small neighborhood radius (depending on \(\eta>0\)). The deterministic limit \(\delta(t)\to0\) almost surely permits localization after a large deterministic time \(T\): let \(\tau\) be the first exit from this neighborhood after \(T\), and kill \(\|\delta(t)\|^2\) at \(\tau\). For \(V_T(t)=\mathbb E[\|\delta(t)\|^2\mathbf1_{\{\tau>t\}}]\), the jump version of Itô's formula, with the nonpositive killing contribution at exit, yields the upper differential inequality
\[
 V_T'(t)\le-\frac{2(1-\beta_{\max}-\eta)}{t}V_T(t)+\frac{2d}{t^2},\quad t>T.
\]
At or below criticality \(\beta_{\max}\le1/2\). Hence for every fixed \(\epsilon\in(0,1/2)\), selecting \(\eta<\epsilon/2\) gives \(V_T(t)=O_{T,\epsilon}(t^{-1+\epsilon})\) (the exponent can be weakened to absorb the forcing integral). Also \(\Pr(\tau=\infty)\to1\) as \(T\to\infty\), by almost-sure homogenization. Consequently, on events with arbitrarily large probability, the quadratic Taylor remainder \(R(t)=\Phi(\mathbf1+\delta(t))-\mathbf1-J\delta(t)\) has \(\mathbb E\|R(t)\|\mathbf1_{\{t<\tau\}}=O(t^{-1+\epsilon})\).

**3. Linear convolution and the nonlinear remainder.** The exact centered equation is
\[
 dY(t)=\frac{JY(t)}t\,dt+R(t)\,dt+dM(t).
\]
For \(t\ge T\), variation of constants gives
\[
 Y(t)=(t/T)^JY(T)+\int_T^t(t/s)^J\,dM(s)
 +\int_T^t(t/s)^J R(s)\,ds.
\]
Analyze the final term on each real spectral subspace of \(J\) with eigenvalue \(\beta\in[0,1/2]\). For \(\beta<1/2\), after division by \(\sqrt t\), its localized expected norm is bounded by a constant times
\[
 t^{\beta-1/2}\int_T^t s^{-\beta-1+\epsilon}\,ds=o(1)
\]
for any \(\epsilon<1/2\); the same applies to the deterministic initial term. For \(\beta=1/2\), the remainder divided by \(\sqrt{t\log t}\) is bounded by a constant times \((\log t)^{-1/2}\int_T^\infty s^{-3/2+\epsilon}ds=o(1)\), and likewise the initial term vanishes. Letting first \(t\to\infty\) and then \(T\to\infty\) removes localization. Thus only the stochastic convolution contributes to either claimed limit.

**4. Gaussian covariance.** In the orthogonal spectral projections \(P_\beta\), the stochastic convolution equals \(t^\beta\int_T^t s^{-\beta}P_\beta\,dM(s)\). Since \(\operatorname{diag}(\Phi(N(s)))\to I\) almost surely, its normalized predictable quadratic covariation tends to \((1-2\beta)^{-1}P_\beta\) when \(\beta<1/2\), and to \(P_*\) for the critical \(\beta=1/2\) normalized by \(\sqrt{t\log t}\). Different spectral projections have vanishing cross covariations; in particular mixed critical/noncritical covariations are \(O((\log t)^{-1/2})\). Jumps of the normalized stochastic convolutions vanish uniformly on \([T,t]\): for the subcritical spectral eigenvalue \(\beta<1/2\) their deterministic bound is \(O(t^{\beta-1/2}T^{-\beta})\), and for a critical eigenvalue the bound is \(O((T\log t)^{-1/2})\). The multivariate martingale central limit theorem therefore gives joint centered Gaussian convergence with the stated block-diagonal covariance. Orthogonal Gaussian blocks are independent. The theorem follows.

## Verification
The standalone `verify.py` tests the finite-dimensional input independently of the proof for cycle sizes 3 through 21. It computes the intensity by its original two-endpoint formula, compares central finite-difference Jacobians with \(J\), compares all eigenvalues against their Fourier expression, confirms the odd/even maximizer multiplicities, checks covariance inverses and direct finite Fourier inversion, and checks that all edge intensities sum exactly to the total vertex firing rate. The recorded program run passed 315 numerical/linear-algebra checks.

These finite computations do not establish the infinite-time martingale central limit theorem. That conclusion is supplied by the localized moment bound, deterministic variation of constants, and predictable quadratic-variation argument above.

## Relationship to prior work
Qin, *Homogenization of weakly reinforced Pólya urns on countable networks*, arXiv:2610.11780 (first public October 8, 2026), Theorem 1.1 supplies the all-parameter almost-sure convergence of normalized edge weights, including on finite cycles. Its proof gives the compensator and stochastic-approximation equation; it does not state the Gaussian or critical logarithmic fluctuations proved here. Couzinié and Hirsch (2021) earlier established several homogenization regimes for the same WARM dynamics, including extensions on regular graphs; their theorem does not identify these fluctuation distributions. Classical finite-dimensional martingale limit methods are standard inputs, not claimed as novel. The contribution is the complete covariance and critical-subspace calculation for this particular edge-reinforced cycle with a rigorous localized remainder estimate, especially the parity-dependent rank of the logarithmic enhancement.

## Limitations
The result is finite-graph only, has equal rate-one firing at each vertex, and fixes the cycle size and reinforcement exponent before \(t\to\infty\). It does **not** determine fluctuation limits for \(\alpha>\alpha_c(d)\), does not address joint limits with the graph size growing, and does not prove a functional (path-space) central limit theorem. The qualifier “critical” refers to the sharp boundary of the Gaussian and logarithmic regimes established here; no supercritical non-Gaussian asymptotic claim is made. The potentially overlapping 2026 Angel–Hermon–Yao preprint cited by Qin was not available for full inspection; a priority comparison with its complete text remains open. Independent proof validation has not been performed.

## References
1. Shuo Qin, *Homogenization of weakly reinforced Pólya urns on countable networks*, arXiv:2610.11780, version 1 October 8, 2026. https://arxiv.org/pdf/2610.11780 .
2. Yannick Couzinié and Christian Hirsch, *Weakly reinforced Pólya urns on countable networks*, Electronic Communications in Probability **26** (2021), article 35, DOI:10.1214/21-ECP404. https://pure.rug.nl/ws/portalfiles/portal/214249018/21_ECP404.pdf .
3. Michel Benaïm, Itai Benjamini, Jun Chen and Yuri Lima, *A generalized Pólya's urn with graph based interactions*, Random Structures & Algorithms **46** (2015), 614–634, DOI:10.1002/rsa.20523. Its bins sit at graph vertices, and its synchronous one-allocation-per-edge-per-round update differs from the independent Poisson vertex-clock model here, even after a line-graph duality for cycles.
4. Omer Angel, Jonathan Hermon and Dong Yao, *Long-time behavior of graph-based weakly reinforced Pólya urns* (2026), preprint cited as reference [3] by Qin; full text not inspected.
