# A dynamics-independent sensor-placement transition on finite normalized paths

## Finding
Let \(N\ge5\), and let \(P_N\) be the unit-edge path with vertices \(1,\dots,N\). Let \(L=I-D^{-1/2}AD^{-1/2}\) denote its symmetric normalized graph Laplacian. Its eigenpairs, in increasing order, are \((\lambda_j,u_j)\), \(\lambda_j=1-\cos(\pi j/(N-1))\), for \(0\le j\le N-1\). Let \(2\le m\le N\), and restrict signals to the first \(m\) orthonormal eigenvectors. For any spectral evolution \(T=\phi(L)\) with pairwise distinct eigenvalues \(\phi(\lambda_j)\), \(0\le j<m\), observe \(K\ge\lceil m/2\rceil\) consecutive iterates at either the **endpoint pair** \(E=\{1,N\}\) or the **inward pair** \(I=\{2,N-1\}\). If \(G_E,G_I\) are the corresponding \(m\)-dimensional information Gramians, then \(G_E\) is positive definite and
\[
\boxed{\frac{\det G_I}{\det G_E}=R_{N,m}:=2^m\prod_{j=1}^{m-1}\cos^2\!\left(\frac{\pi j}{N-1}\right).}
\]
The ratio is **independent of the evolution, the observation horizon, and all nonzero temporal eigenvalues**. If the path has an odd number of vertices and the selected band contains the central eigenmode, the inward Gramian is singular and the formula gives zero.

For every fixed \(N\ge5\), the strictly favorable bandwidths \(\{m\in\{2,\dots,N\}:R_{N,m}>1\}\) form exactly an initial nonempty interval of integers. Ties may occur at its upper boundary; for example \(R_{9,4}=1\). Define its last member by \(c_N=\max\{m:R_{N,m}>1\}\). With
\[
F(a)=\int_0^a\log(2\cos^2(\pi t))\,dt,\qquad 0\le a<\tfrac12,
\]
there is a unique \(a_*\in(1/4,1/2)\) satisfying \(F(a_*)=0\), and
\[
\boxed{\lim_{N\to\infty}\frac{c_N}{N-1}=a_*=0.40958108674922138\ldots.}
\]
In fact the transition has an explicit first finite-size correction. Put \(f(a)=\log(2\cos^2(\pi a))\) and
\[
\delta_*:=\frac{\log\cos(\pi a_*)}{f(a_*)}=0.68723930906431945\ldots.
\]
For every sequence of integers \(m=m_N\) with \(m-a_*(N-1)=O(1)\),
\[
\boxed{\log R_{N,m}=f(a_*)\bigl(m-a_*(N-1)-\delta_*\bigr)+O(N^{-1}).}
\]
Thus the sign switch occurs within a bounded number of modes of \(a_*(N-1)+\delta_*\), with an explicitly identified transition shift. For a concrete illustration, \(N=40\) and \(m=6\) give \(R_{40,6}\approx44.4721\), whereas \(m=17\) gives \(R_{40,17}\approx0.505923\).

## Assumptions and scope
The path has unit edges, no loops, and standard symmetric-normalized Laplacian; its endpoint degrees are \(1\) and interior degrees \(2\). Two distinct vertex sensors have equal measurement weight, and the objective is the determinant of the full spectral information Gramian, not its smallest eigenvalue or condition number. Each sensor provides \(K\) measurements at integer times \(0,\dots,K-1\). A real or complex spectral multiplier \(\phi\) is permitted provided the selected spectral values are distinct (distinctness within each parity class alone suffices). The result compares only these two **symmetric pairs**; it does not assert global optimality among all vertex pairs.

For precision, writing the unknown signal as \(x=\sum_{j=0}^{m-1}a_j u_j\), the observation matrix \(\Theta_S\), with rows indexed by \((v,t)\in S\times\{0,\dots,K-1\}\), is
\[
(\Theta_S)_{(v,t),j}=u_j(v)\phi(\lambda_j)^t,\qquad G_S=\Theta_S^*\Theta_S.
\]
Every determinant is a determinant on the coefficient space \(\mathbb C^m\), so the comparison uses the same orthonormal signal coordinates for both sensor choices.

## Proof
**1. Explicit path eigenbasis and transfer between symmetric pairs.** Set \(M=N-1\), and let \(d_v=1\) at \(v=1,N\) and \(d_v=2\) otherwise. An orthonormal eigenbasis of \(L\) is given by
\[
u_j(v)=\sqrt{\frac{d_v}{M}}\cos\left(\frac{\pi j(v-1)}M\right),\quad 1\le j\le M-1,
\]
and by the same cosine expression with factor \(\sqrt{d_v/(2M)}\) for \(j=0,M\). This follows directly by checking the normalized-adjacency recurrence and the discrete cosine orthogonality identities, including the two endpoint modes. For every \(0\le j\le M\),
\[
u_j(2)=\sqrt2\cos\!\left(\frac{\pi j}M\right)u_j(1),\qquad
u_j(N-1)=\sqrt2\cos\!\left(\frac{\pi j}M\right)u_j(N).
\]
The second identity uses \(\cos(\pi j(M-1)/M)=(-1)^j\cos(\pi j/M)\); the same \((-1)^j\) relates the two endpoint values. Therefore, for the diagonal matrix \(C=\operatorname{diag}(\sqrt2\cos(\pi j/M):0\le j<m)\), the two observation matrices satisfy the **exact column identity** \(\Theta_I=\Theta_E C\) for all times and spectral multipliers. Consequently \(G_I=C^*G_E C\).

**2. The endpoint information matrix is nonsingular.** Every selected endpoint eigenvector entry \(u_j(1)\) is nonzero and satisfies \(u_j(N)=(-1)^j u_j(1)\). Adding and subtracting the two sensor outputs at each time splits the observation matrix into independent even-\(j\) and odd-\(j\) Vandermonde blocks. Those blocks contain respectively \(\lceil m/2\rceil\) and \(\lfloor m/2\rfloor\) columns and \(K\ge\lceil m/2\rceil\) rows. Their spectral nodes are distinct by assumption, so both have full column rank. Thus \(G_E\) is positive definite. Taking determinants of \(G_I=C^*G_E C\) yields the boxed exact ratio, without evaluating any Vandermonde determinant. If \(M\) is even and \(m>M/2\), the selected mode \(j=M/2\) has \(C_{jj}=0\) and the inward pair fails to observe it; otherwise \(C\) is invertible.

**3. One finite cutoff, including all high frequencies.** Write \(R_m=R_{N,m}\) for fixed \(N\). Then \(R_1=2\) and
\[
\frac{R_{m+1}}{R_m}=2\cos^2\left(\frac{\pi m}{M}\right),\qquad 1\le m\le M,
\]
whenever both sides are nonzero (the product expression also defines the zero case). The factor is at least \(1\) for \(m/M\in[0,1/4]\cup[3/4,1]\) and at most \(1\) between those regions. In particular, \(R_2=4\cos^2(\pi/M)\ge2>1\) for \(M\ge4\). At the last bandwidth \(m=N=M+1\), the ratio is zero if \(M\) is even. If \(M\) is odd, the classical root-of-unity identity \(\prod_{j=1}^{M-1}|\cos(\pi j/M)|=2^{1-M}\) gives
\[
R_{N,N}=2^{M+1}2^{2(1-M)}=2^{3-M}=2^{4-N}<1.
\]
Since the sequence first increases, then decreases, then increases to a final value less than \(1\), its strictly-above-one indices constitute a single initial interval. The switch can include a tie: \(R_{9,4}=16[\cos(\pi/8)\cos(\pi/4)\cos(3\pi/8)]^2=1\) exactly. This proves the finite assertion without declaring all transitions strict.

**4. Universal thermodynamic cutoff.** On every compact subinterval of \([0,1/2)\), the logarithmic product is a Riemann sum, giving uniformly
\[
\frac1M\log R_{N,m}=F(m/M)+o(1)\quad\text{as }M\to\infty.
\]
Here \(F'(a)=\log(2\cos^2(\pi a))\) is positive before \(a=1/4\) and negative between \(1/4\) and \(1/2\). Also \(F(0)=0\), \(F(1/4)>0\), and the elementary cosine integral gives \(F(1/2)=-\tfrac12\log2<0\). Therefore \(F\) has precisely one zero \(a_*\) in \((1/4,1/2)\). Given \(a_-<a_*<a_+<1/2\), the Riemann-sum limit puts the last positive index between \(a_-M\) and \(a_+M\) for large \(M\); Step 3 forbids reentry at higher bandwidths. Hence \(c_N/M\to a_*\).

**5. Sharp bounded-width location.** Define \(f(t)=\log(2\cos^2(\pi t))\). Euler–Maclaurin summation with the first boundary correction, uniformly for \(a=m/M\) in a compact neighborhood of \(a_*\), gives
\[
\begin{aligned}
\log R_{N,m}
&=\log2+\sum_{j=1}^{m-1}f(j/M)\\
&=M F(a)+\log2-\tfrac12f(0)-\tfrac12f(a)+O(M^{-1})\\
&=M F(a)-\log\cos(\pi a)+O(M^{-1}).
\end{aligned}
\]
When \(m-a_*M=O(1)\), Taylor expansion at \(a_*\) and \(F(a_*)=0\) give
\[
\log R_{N,m}=f(a_*)(m-a_*M)-\log\cos(\pi a_*)+O(M^{-1}).
\]
Since \(f(a_*)<0\), this is exactly the claimed correction with \(\delta_*=\log\cos(\pi a_*)/f(a_*)\). It also implies the cutoff location \(c_N=a_*M+O(1)\) and the numerical values can be obtained reproducibly by one-dimensional quadrature and bisection.

## Verification
The supplied standalone standard-library checker `verify_two_sensor.py` was executed on the embedded version and independently checked the complete normalized-path eigenbasis, its transfer matrix, Gram congruence for several spectral evolutions and horizons, small determinant ratios, the all-bandwidth strict-win interval for paths through \(N=500\), and the numerical root and finite-shift asymptotic. Its final output was `TWO_SENSOR_CHECK_OK`. Finite tests are supplemental: every all-\(N\), all-\(m\), all-\(K\), and all-\(\phi\) statement follows from Steps 1–5.

## Relationship to prior work
Bulai, Cabrelli, Cordero, Molter and Saliani (arXiv:2609.25472v1; first publicly available 2026-09-21) establish finite-graph dynamical-sampling matrices, derive normalized-path eigenvectors, and numerically study sensor placement and frame bounds. Those general formulas are used as starting facts; their relevant finite-path section does not give this **two-symmetric-pair information-determinant ratio, single finite cutoff, or asymptotic critical density and finite-size shift**. A separately published exact result, *Universal endpoint optimality for dynamical sampling on normalized paths* (public identifier `2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f`), proves endpoint superiority for **one sensor, all path eigenmodes, and a full square time history**. Its assertion cannot be transferred to the current **two-sensor, variable-low-pass-band** comparison: indeed, the present ratio exceeds \(1\) for small selected bands. General graph D-optimal sensor-design work, including Jayawant and Ortega (2022), supplies motivation, not an inspected formula for this finite-path transition. No claim of global optimality among all two-vertex choices is made.

## Limitations
Only two particular symmetric sensor placements on a normalized unit-edge path are compared, using equal measurement weights. The optimization metric is the determinant of the information Gramian, not its minimum eigenvalue, operator norm, condition number, or reconstruction under correlated noise. Multipliers must separate spectral nodes within each parity class; if this is violated, the denominator may be singular. The integer transition can contain an exact tie and the universal density is an asymptotic statement, with the stated local finite-size expansion. Older or unindexed literature might contain an equivalent D-optimal placement law, and no independent audit has been performed.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter and S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472v1 (2026-09-21), https://arxiv.org/html/2609.25472v1 (finite-graph observation matrices and normalized-path eigenvectors).
2. *Universal endpoint optimality for dynamical sampling on normalized paths*, public mathematical result dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f (single-sensor comparison; distinct sampling design).
3. A. Jayawant and A. Ortega, *Practical graph signal sampling with log-linear size scaling*, Signal Processing **194** (2022), article 108436, https://doi.org/10.1016/j.sigpro.2021.108436 (general graph D-optimal design methodology; abstract and metadata inspected).
4. Euler–Maclaurin summation and the elementary integral \(\int_0^{\pi/2}\log\cos t\,dt=-(\pi/2)\log2\) (classical identities, applied with displayed details).
