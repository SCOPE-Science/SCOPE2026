# Optimal heat-sampling intervals on normalized paths: a bandwidth crossover

## Finding
Fix an integer \(N\ge3\) and let \(L_N=I-D^{-1/2}AD^{-1/2}\) be the symmetric normalized Laplacian of the unit-edge path \(P_N\), whose vertices are \(0,\ldots,N-1\). For \(2\le m\le N\), let \(E_{N,m}\) be the span of its first \(m\) orthonormal eigenvectors, in increasing eigenvalue order. Observe the initial state through one endpoint and exactly \(m\) consecutive heat samples at times \(0,\tau,\ldots,(m-1)\tau\). Write \(\Theta_{N,m}(\tau)\) for the square sampling matrix in the orthonormal spectral basis, and let
\[
\mathcal D_{N,m}(\tau)=\det\bigl(\Theta_{N,m}(\tau)^*\Theta_{N,m}(\tau)\bigr),\qquad\tau>0.
\]
The following assertions hold.

**Finite-size uniqueness and the two-mode exception.** For every \(N\ge3\) and \(3\le m\le N\), there is exactly one \(\tau_{N,m}>0\) maximizing \(\mathcal D_{N,m}\) over all positive uniform sampling spacings. For \(m=2\), \(\mathcal D_{N,2}\) is strictly increasing and has no finite maximizer. Write
\[
\lambda_j=1-\cos\frac{\pi j}{N-1}\quad(0\le j<N),\qquad
r_j=\frac{\lambda_j}{\lambda_{m-1}}.
\]
Then the optimal spacing is characterized, without matrix diagonalization, by the unique positive solution \(s_{N,m}=\tau_{N,m}\lambda_{m-1}\) of
\[
\boxed{
\sum_{0\le i<j<m}\frac{r_j-r_i}{e^{s_{N,m}(r_j-r_i)}-1}
=\sum_{0\le i<j<m}r_i.}
\]

**Sharp bandwidth-fraction limit.** Let \(N\to\infty\) and \(m=m(N)\to\infty\), with \(3\le m\le N\) and \(m/N\to\theta\in[0,1]\). Put
\[
\rho_\theta(x)=
\begin{cases}
 x^2,&\theta=0,\\[2pt]
 \displaystyle\frac{1-\cos(\pi\theta x)}{1-\cos(\pi\theta)},&0<\theta\le1,
\end{cases}\qquad 0\le x\le1.
\]
There is a unique number \(s_\theta>0\) satisfying
\[
\boxed{
\int_0^1\int_u^1
\frac{\rho_\theta(v)-\rho_\theta(u)}{\exp\bigl(s_\theta[\rho_\theta(v)-\rho_\theta(u)]\bigr)-1}
\,dv\,du
=\int_0^1(1-u)\rho_\theta(u)\,du.}
\]
The integrand is interpreted by continuity on the diagonal (its value is \(1/s_\theta\)). The exact asymptotic design law is
\[
\boxed{\tau_{N,m}\lambda_{m-1}\longrightarrow s_\theta.}
\]
In particular, in the low-bandwidth regime \(m\to\infty\), \(m/N\to0\),
\[
\boxed{\tau_{N,m}\sim\frac{2s_0}{\pi^2}\left(\frac{N-1}{m-1}\right)^2,\qquad
s_0=3.50135659780166\ldots,}
\]
where \(s_0\) is determined exactly by the same integral equation with \(\rho_0(x)=x^2\) and right side \(1/12\). At the other extreme, whenever \(m/N\to1\),
\[
\boxed{\tau_{N,m}\longrightarrow s_1/2,\qquad s_1=2.19180873992866\ldots.}
\]
Numerical values are illustrative evaluations of the defining integral equation, not separate exact definitions.

## Assumptions and scope
The graph has \(N\ge3\) vertices and unit edges. The Laplacian is the **symmetric normalized** Laplacian, not the combinatorial Laplacian. The signal belongs to the first \(m\) distinct normalized-Laplacian modes, including the constant (zero-eigenvalue) mode. The sensor reads the value at a fixed endpoint. Heat evolution over one sampling step is \(R_\tau=e^{-\tau L_N}\). Exactly \(m\) observations are taken at the uniform times \(0,\tau,\ldots,(m-1)\tau\), with no per-time rescaling. The determinant is that of the information Gramian for these observations in the standard \(\ell^2\) signal norm; independent equal-variance observation noise multiplies it by a factor independent of \(\tau\). Maximization is only over \(\tau>0\), not over spatial sensors, nonuniform time grids, or alternative criteria such as the smallest frame bound.

## Proof
**1. Explicit path spectrum and exact determinant.** Put \(M=N-1\) and let the vertex degrees be \(d_0=d_M=1\), \(d_j=2\) for \(1\le j<M\). The orthonormal eigenvectors of \(L_N\) can be taken as
\[
 v_0(j)=\sqrt{\frac{d_j}{2M}},\quad
 v_k(j)=\sqrt{\frac{d_j}{M}}\cos\frac{\pi kj}{M}\ (1\le k<M),\quad
 v_M(j)=(-1)^j\sqrt{\frac{d_j}{2M}}.
\]
Their eigenvalues are exactly \(\lambda_k=1-\cos(\pi k/M)\). The eigenvalue equation follows from the cosine addition formula, including the degree-weighted endpoint equations. Orthogonality follows by summing the cosine products with vertex-degree weights, or by the symmetry and simplicity of the eigenvalues followed by the displayed norm calculation. All endpoint coefficients \(a_k=v_k(0)\) are nonzero and positive, with \(a_0=(2M)^{-1/2}\), \(a_k=M^{-1/2}\) for \(1\le k<M\), and \(a_M=(2M)^{-1/2}\).

The measurement matrix has entries
\[
\Theta_{\ell,k}=a_k e^{-\ell\tau\lambda_k},\qquad0\le\ell,k<m.
\]
It is a Vandermonde matrix in the strictly decreasing nodes \(q_k=e^{-\tau\lambda_k}\), multiplied by the diagonal endpoint amplitudes. Consequently
\[
\boxed{\mathcal D_{N,m}(\tau)=C_{N,m}
\prod_{0\le i<j<m}(e^{-\tau\lambda_i}-e^{-\tau\lambda_j})^2,}
\]
where
\[
C_{N,m}=\begin{cases}
(2M^m)^{-1},&2\le m<N,\\
(4M^N)^{-1},&m=N.
\end{cases}
\]
The determinant is strictly positive for every \(\tau>0\). This formula is an ingredient of the timing result and is not asserted as a new general Vandermonde identity.

**2. Existence, uniqueness, and the exact scalar equation.** The amplitudes are independent of \(\tau\). Factoring each Vandermonde difference as
\[
e^{-\tau\lambda_i}-e^{-\tau\lambda_j}
=e^{-\tau\lambda_i}\bigl(1-e^{-\tau(\lambda_j-\lambda_i)}\bigr)
\]
gives, for the logarithm \(\ell(\tau)=\tfrac12\log(\mathcal D_{N,m}(\tau)/C_{N,m})\),
\[
\ell'(\tau)=\sum_{i<j}\left[-\lambda_i+
\frac{\lambda_j-\lambda_i}{e^{\tau(\lambda_j-\lambda_i)}-1}\right],
\]
\[
\ell''(\tau)=-\sum_{i<j}\frac{(\lambda_j-\lambda_i)^2
 e^{\tau(\lambda_j-\lambda_i)}}{(e^{\tau(\lambda_j-\lambda_i)}-1)^2}<0.
\]
Thus \(\ell\) is strictly concave on \((0,\infty)\). As \(\tau\downarrow0\), each positive difference contributes asymptotically \(1/\tau\) to \(\ell'\), so \(\ell'(\tau)\to+\infty\). As \(\tau\to\infty\),
\[
\ell'(\tau)\longrightarrow-\sum_{i<j}\lambda_i.
\]
For \(m\ge3\) the latter sum is strictly positive because it includes \(\lambda_1\) paired with \(j=2\); therefore there is exactly one zero of \(\ell'\), and it is the global maximum. For \(m=2\) the sum is zero and \(\ell'(\tau)=\lambda_1/(e^{\tau\lambda_1}-1)>0\), proving the exceptional monotone case. Divide the stationarity equation by \(\lambda_{m-1}\) and set \(s=\tau\lambda_{m-1}\) to obtain the displayed exact characterization.

**3. Uniform limiting spectral profiles.** Assume \(m\to\infty\), \(N\to\infty\), and \(m/N\to\theta\). Let \(\theta_N=(m-1)/(N-1)\). The finite normalized eigenvalues satisfy the **exact** identity
\[
r_j=\rho_{\theta_N}\left(\frac{j}{m-1}\right),\qquad0\le j<m.
\]
The map \((\theta,x)\mapsto\rho_\theta(x)\), extended at \(\theta=0\) by \(x^2\), is continuous on the compact square \([0,1]^2\): uniform Taylor expansion of cosine proves continuity at \(\theta=0\). Thus the discretized spectral profiles converge uniformly to \(\rho_\theta\). For fixed \(s>0\), define
\[
H_s(a,b)=-a+\frac{b-a}{e^{s(b-a)}-1},\quad0\le a\le b\le1,
\]
using the continuous extension \(H_s(a,a)=-a+1/s\). The normalized finite stationarity function is
\[
G_{N,m}(s)=\frac1{m^2}\sum_{0\le i<j<m}H_s(r_i,r_j).
\]
By uniform continuity and the triangular Riemann-sum theorem,
\[
G_{N,m}(s)\longrightarrow
G_\theta(s)=\int_0^1\int_u^1H_s(\rho_\theta(u),\rho_\theta(v))\,dv\,du.
\]
This convergence is uniform on each compact interval of positive \(s\), because \(H_s\) is jointly continuous in \((s,a,b)\) there.

**4. Existence and convergence of the limiting optimizers.** The first term in \(G_\theta(s)\) integrates to \(-I_\theta\), where
\[
I_\theta=\int_0^1(1-u)\rho_\theta(u)\,du>0.
\]
For \(d>0\), the function \(d/(e^{sd}-1)\) is strictly decreasing in \(s>0\); the same holds at \(d=0\) by continuity. Hence \(G_\theta\) is continuous and strictly decreasing. As \(s\downarrow0\), the positive term tends to infinity (indeed, uniformly in \(d\in[0,1]\) it equals \(1/s+O(1)\)), so \(G_\theta(s)\to+\infty\). As \(s\to\infty\), the positive term is bounded by \(1/s\) and tends to zero, hence \(G_\theta(s)\to-I_\theta<0\). There is therefore a unique root \(s_\theta>0\).

Choose any \(s_-<s_\theta<s_+\) sufficiently close that \(G_\theta(s_-)>0>G_\theta(s_+)\). Uniform convergence at these two values implies \(G_{N,m}(s_-)>0>G_{N,m}(s_+)\) for all sufficiently large \(N\). Each finite function is strictly decreasing by Step 2 and has a unique zero, so \(s_-<s_{N,m}<s_+\). Letting the bracketing values approach the limiting root proves \(s_{N,m}\to s_\theta\).

**5. Diffusive and full-band limits.** When \(\theta=0\), \(\rho_0(u)=u^2\) and \(I_0=\int_0^1u^2(1-u)\,du=1/12\). Moreover,
\[
\lambda_{m-1}=1-\cos\frac{\pi(m-1)}{N-1}
\sim\frac{\pi^2(m-1)^2}{2(N-1)^2}.
\]
Combining this with \(\tau_{N,m}\lambda_{m-1}\to s_0\) gives the displayed sharp diffusive timing coefficient. If \(\theta=1\), then \(\lambda_{m-1}\to2\), yielding \(\tau_{N,m}\to s_1/2\). For \(0<\theta<1\), the same argument yields the more general limit \(\tau_{N,m}\to s_\theta/[1-\cos(\pi\theta)]\). This completes the proof.

## Verification
The accompanying `CHECK.py` is a standalone Python-standard-library regression checker. It reconstructs the eigenvector equations and orthonormality on small paths, compares direct Gaussian-elimination determinants with the product identity, brackets the finite unique maximum, evaluates the limiting integral equations by triangular midpoint quadrature, and tests a separate three-mode asymptotic identity. Run `python3 CHECK.py` from a directory containing the file. In the delivered version the replay produces `VERIFY_OK 2198 supplementary_assertions`. Finite tests do not certify the unbounded-dimensional result; Steps 1–5 prove all quantified assertions. The quoted decimals are reproducible with high-order quadrature and scalar bisection, whereas exact claims are the integral characterizations.

## Relationship to prior work
Bulai, Cabrelli, Cordero, Molter and Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces* (arXiv:2609.25472v1, first public September 21, 2026), develop normalized-graph Laplacian dynamical sampling and compare path-graph frame bounds numerically at a fixed temporal damping. Their Section 4.3 does not optimize the **sampling interval**, or determine a bandwidth-fraction crossover law. The established finite-dimensional frame criterion is used here only as context.

*Universal endpoint optimality for dynamical sampling on normalized paths* (published-finding corpus mathematical record `2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f`) gives an exact **full-spectrum** endpoint information determinant for arbitrary injective spectral evolution and compares sensor locations. The current result instead optimizes the temporal heat step for variable low-pass bandwidth, proves the unique optimal interval and derives the continuum family \(s_\theta\). The older full-spectrum formula is consistent with, but does not state or numerically determine, this timing-limit family.

*A universal optimal observation horizon for arithmetic-spectrum flows* (published-finding corpus mathematical record `2026/10/11/SCOPE-a-universal-optimal-observation-horizon-for-arithmetic-spectrum--64dbf45b5739`) treats a different two-observable **arithmetic-spectrum** confluent-Vandermonde system. Its limiting constant \(2.121467\ldots\) arises from a different integral and is not a special case or proof of the normalized-path heat constant \(s_0=3.501356\ldots\) or the crossover \(s_\theta\). Classical Vandermonde and logarithmic-concavity calculations, and general optimal-design and frame principles, are background rather than asserted new results.

## Limitations
The objective is D-optimality (maximal information determinant) for one endpoint, fixed low-pass spectral dimension, exactly \(m\) observations, and **uniform** temporal spacing. A design with optimal determinant need not minimize the spectral condition number or maximize the smallest frame bound. No optimality over arbitrary nonuniform sampling times, sensors, or noisy dynamics is claimed. The bandwidth-fraction limit requires \(m\to\infty\); fixed small \(m\) has a different limiting scalar equation. The result does not assert any independent audit or resolution of all historical priority questions.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter and S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472v1 (2026-09-21), https://arxiv.org/abs/2609.25472.
2. A. Aguilera, C. Cabrelli, F. Negreira and V. Paternostro, *Existence and Properties of Frames of Iterations* (displayed as *Optimal Dynamical Frames*), arXiv:2506.00567 (2025), https://arxiv.org/abs/2506.00567.
3. *Universal endpoint optimality for dynamical sampling on normalized paths*, published-finding corpus mathematical record `2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f`, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f.
4. *A universal optimal observation horizon for arithmetic-spectrum flows*, published-finding corpus mathematical record `2026/10/11/SCOPE-a-universal-optimal-observation-horizon-for-arithmetic-spectrum--64dbf45b5739`, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-universal-optimal-observation-horizon-for-arithmetic-spectrum--64dbf45b5739.
5. H. Dette, V. B. Melas and W. K. Wong, *Locally D-optimal designs for exponential regression models*, Statistica Sinica 16 (2006), 789–803, https://www3.stat.sinica.edu.tw/statistica/j16n3/j16n36/j16n36.html (distinct setting: unknown exponential regression parameters and optimized approximate designs).
