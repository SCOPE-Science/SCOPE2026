# Two sharp spectral-order thresholds for sampled two-harmonic von Mises kernels

## Finding
For each integer \(N\ge7\), \(t>0\), and \(\rho\ge0\), put \(\theta_k=2\pi k/N\) and consider the circulant kernel matrix
\[
K_{ab}=\exp\bigl(t\cos\theta_{a-b}+\rho t\cos(2\theta_{a-b})\bigr),\qquad a,b\in\mathbb Z/N\mathbb Z.
\]
Its positive Fourier eigenvalues are \(\lambda_j=\sum_{k=0}^{N-1}\exp(t\cos\theta_k+\rho t\cos2\theta_k)\cos(j\theta_k)\), with \(\lambda_j=\lambda_{N-j}\). Set \(m=\lfloor N/2\rfloor\), \(c_N=\cos(2\pi/N)\), and \(d_N=1\) for even \(N\), or \(d_N=\cos(\pi/N)\) for odd \(N\). Define the sharp large-parameter threshold
\[
\rho_*(N)=\frac{1}{2(d_N-c_N)}.
\]
Then \(\rho_*(N)>1\) and:

1. For **all** \(t>0\), the Fourier eigenvalues satisfy \(\lambda_0\ge\lambda_1\ge\cdots\ge\lambda_m\) if and only if \(0\le\rho\le1\). Every inequality is strict if \(0\le\rho<1\).
2. If \(\rho>1\), then \(\lambda_2>\lambda_1\) for every sufficiently small positive \(t\).
3. For a given \(\rho\), the **strict** ordering \(\lambda_0>\lambda_1>\cdots>\lambda_m\) holds for every sufficiently large \(t\) if and only if \(0\le\rho<\rho_*(N)\). If \(\rho\ge\rho_*(N)\), then \(\lambda_2>\lambda_1\) for every sufficiently large \(t\).

Consequently \(1<\rho<\rho_*(N)\) is a genuine *mode-order healing region*: the adjacent-mode inequality \(\lambda_1>\lambda_2\) is initially false but ultimately true. The sharp threshold exhibits a parity effect,
\[
\rho_*(N)\sim\begin{cases}N^2/(4\pi^2),&N\text{ even},\\N^2/(3\pi^2),&N\text{ odd},\end{cases}\qquad N\to\infty.
\]

## Assumptions and scope
The matrix uses the unnormalized Fourier spectrum of the sampled positive definite kernel on the regular \(N\)-gon; multiplying all eigenvalues by a common positive normalization does not change ordering. The angular distance of a residue \(j\) is \(d(j)=\min\{j,N-j\}\). All spectral assertions concern **every** \(N\ge7\), \(\rho\ge0\), and the specified positive times. ``Eventually'' means there exists a finite threshold depending on \(N,\rho\) after which the assertion holds for all larger times. No assertion is made about the number or uniqueness of intermediate crossings.

## Proof
**(a) Positive spectrum and the heat-semigroup reduction.** Let \(S\) denote cyclic translation on functions on \(\mathbb Z/N\mathbb Z\) and set
\[
L_\rho=\tfrac12(S+S^{-1})+\tfrac\rho2(S^2+S^{-2})-(1+\rho)I.
\]
This is the generator of the continuous-time symmetric random walk with jumps \(\pm1,\pm2\). Its heat kernel \(p_t=e^{tL_\rho}\delta_0\) has strictly positive entries for every \(t>0\) because the rate of each \(\pm1\) jump is positive and the Poisson expansion assigns positive mass to every residue. The discrete Fourier inversion formula yields
\[
\lambda_j=N e^{(1+\rho)t}p_t(j),\qquad 0\le j<N,
\]
which simultaneously proves positive definiteness and reduces eigenvalue order to radial order of the heat mass.

**(b) Cyclic unimodal convolution.** Let \(\mathcal U\) be the cone of nonnegative symmetric functions \(u\) on the cyclic group satisfying \(u(0)\ge u(1)\ge\cdots\ge u(m)\). For integers \(0\le r\le m\), define \(U_r(j)={\bf1}_{\{d(j)\le r\}}\); \(U_m\) is constant. Every \(u\in\mathcal U\) decomposes as
\[
u=\sum_{r=0}^{m-1}[u(r)-u(r+1)]U_r+u(m)U_m.
\]
For \(r,s<m\), a direct shift of the summation interval gives
\[
(U_r*U_s)(j)-(U_r*U_s)(j+1)=U_s(j-r)-U_s(j+r+1)\ge0\quad(0\le j<m).
\]
For the final inequality, the elementary identity
\[
\cos\frac{2\pi(j-r)}N-\cos\frac{2\pi(j+r+1)}N
=2\sin\frac{\pi(2j+1)}N\sin\frac{\pi(2r+1)}N>0
\]
holds for \(0\le j,r<m\). Since \(\cos(2\pi u/N)\) decreases strictly as the cyclic distance \(d(u)\) increases from \(0\) to \(m\), it follows that \(d(j-r)<d(j+r+1)\) and hence \(U_s(j-r)\ge U_s(j+r+1)\). If either radius equals \(m\), the convolution is constant. Thus \(\mathcal U*\mathcal U\subset\mathcal U\).

For \(0\le\rho\le1\) and sufficiently small \(\epsilon>0\), the Euler kernel \((I+\epsilon L_\rho)\delta_0\) has radial entries \(1-(1+\rho)\epsilon,\epsilon/2,\rho\epsilon/2,0,\ldots\); it belongs to \(\mathcal U\). Closure under convolution and limits gives \(p_t=\lim_{h\to\infty}(I+(t/h)L_\rho)^h\delta_0\in\mathcal U\). This proves all-time weak ordering.

For strictness when \(\rho<1\), decompose \(L_\rho=(1-\rho)L_0+\rho L_1\) where \(L_0=(S+S^{-1})/2-I\) and \(L_1=(S+S^{-1}+S^2+S^{-2})/2-2I\). Their convolution semigroups commute. The nearest-neighbor heat kernel \(a=e^{(1-\rho)tL_0}\delta_0\) is strictly radially decreasing: its adjacent differences satisfy an irreducible tridiagonal linear ODE with nonnegative off-diagonal entries, and start at \((1,0,\ldots,0)\); positivity propagation in the matrix exponential makes all differences positive for any \(t>0\). The second heat kernel \(b=e^{\rho t L_1}\delta_0\) belongs to \(\mathcal U\). Moreover,
\[
b(0)-b(1)=\frac1N\sum_{k=0}^{N-1}e^{\rho t(\cos\theta_k+\cos2\theta_k-2)}(1-\cos\theta_k)>0.
\]
Thus its \(U_0\) coefficient is strictly positive; in the arc decomposition, \(a*b\) contains a positive multiple of strictly decreasing \(a\), plus weakly decreasing functions. This proves the strict ordering for \(\rho<1\). Conversely, for \(\rho>1\), the distinct \(\pm1\) and \(\pm2\) first-jump contributions give \(p_t(1)=t/2+O(t^2)\) and \(p_t(2)=\rho t/2+O(t^2)\), proving the failure for small time and the necessity of \(\rho\le1\) in the all-time criterion.

**(c) Exact eventual threshold.** Write \(F_\rho(x)=x+\rho(2x^2-1)\). The frequency exponent is \(F_\rho(\cos\theta_k)\). At nonzero frequencies \(k=1,\ldots,m\), the cosine coordinates cover \([-d_N,c_N]\); for \(\rho>0\), strict convexity implies that the maximal exponent among these nodes is attained only at one or both endpoints. Its endpoint difference factors as
\[
F_\rho(c_N)-F_\rho(-d_N)=(c_N+d_N)[1-2\rho(d_N-c_N)].
\]
For \(\rho=0\), monotonicity of \(F_0\) gives the same first-endpoint dominance. If \(\rho<\rho_*(N)\), frequency \(k=1\) and its reflection are the unique dominant nonconstant modes. For every \(0\le j<m\), the leading term in the adjacent difference is
\[
\lambda_j-\lambda_{j+1}=2e^{tF_\rho(c_N)}[\cos(j\theta_1)-\cos((j+1)\theta_1)]+o(e^{tF_\rho(c_N)}),
\]
strictly positive since \(0\le j<m\) places both angles in the strictly decreasing cosine interval \([0,\pi]\). There are finitely many differences, so they are eventually simultaneously positive.

If \(\rho>\rho_*(N)\), the opposite endpoint \(k=m\) dominates. When \(N\) is odd, its paired contribution to \(\lambda_1-\lambda_2\) is \(2e^{tF_\rho(-d_N)}[-d_N-c_N]<0\); when \(N\) is even, the unpaired antipodal term is \(-2e^{tF_\rho(-1)}<0\). At equality \(\rho=\rho_*(N)\), both endpoint frequency contributions must be included. Their leading combined coefficients in \(\lambda_1-\lambda_2\) equal \(-2[d_N+\cos(4\pi/N)]<0\) for odd \(N\), and \(2[\cos(2\pi/N)-\cos(4\pi/N)-1]<0\) for even \(N\). These signs hold for all \(N\ge7\): the first inequality follows from \(\cos(\pi/N)+\cos(4\pi/N)>0\), and the second from \(\cos u-\cos(2u)<1\) for \(u=2\pi/N\le\pi/4\). Thus even at the boundary \(\lambda_2>\lambda_1\) for all sufficiently large \(t\). The strict all-adjacent ordering at large time is therefore equivalent to \(\rho<\rho_*(N)\).

Finally, Taylor expansion of \(d_N-c_N\) yields \(2\pi^2/N^2+O(N^{-4})\) for even \(N\), and \(3\pi^2/(2N^2)+O(N^{-4})\) for odd \(N\), proving the parity-dependent asymptotics. The smallest threshold \(\rho_*(N)\) for \(N\ge7\) is greater than \(1\).

## Verification
A standalone program `check.py` checks cyclic arc-convolution closure exactly in integer arithmetic for cyclic orders \(5\) through \(50\), and numerically checks sample spectra and eventual endpoint thresholds at high precision for cyclic orders \(7\) through \(21\). It reported **23,414 arc-convolution assertions and 147 numerical spectral assertions, all passing**. These are finite corroborations; the proof above establishes the universal assertions without extrapolating from experiments.

## Relationship to prior work
The generalized von Mises family with first and second circular harmonics appears in directional statistics, including Salvador and Gatto (2021), where modality of the *spatial* circular density is studied. In the present parametrization, the spatial density becomes bimodal for \(\rho>1/4\) since its angular derivative has factor \(\sin\theta(1+4\rho\cos\theta)\). The kernel spectrum nevertheless stays ordered for every time through \(\rho=1\), showing that spatial and Fourier spectral unimodality differ. Chinta, Jorgenson, Karlsson, and Smajlović (2024) analyze a discrete Gaussian/nearest-neighbor cycle heat kernel (the case with no second-neighbor jump), without the two competing spectral thresholds. Lyons and White (2021) study monotonicity of continuous-time walks with respect to the walk parameters, a different assertion from componentwise distance-order inequalities. Standard symmetric-unimodal convolution methods inform the cone argument; the claimed result is the *combined sharp all-time/eventual threshold and parity law*, not the generic convolution observation.

## Limitations
No uniqueness, count, or monotonicity of intermediate crossing times is asserted. The theorem applies to nonnegative \(\rho\) and regular equally spaced samples of size \(N\ge7\), not arbitrary sampling geometries or negative second-harmonic coefficients. The claims are proved analytically, but independent external evaluation and comprehensive historical priority certification have not been performed. Classical circular unimodality literature may contain related formulations not identified in the inspected materials.

## References
- G. Chinta, J. Jorgenson, A. Karlsson, L. Smajlović, *The discrete analogue of the Gaussian*, arXiv:2409.14344v1, publicly released 2024-09-22, https://arxiv.org/abs/2409.14344 . Full text examined, especially discrete-circle heat-kernel identities.
- S. Salvador and R. Gatto, *Bayesian tests of symmetry for generalized von Mises distribution*, *Computational Statistics* (2021), DOI 10.1007/s00180-021-01147-7. Full accessible article inspected for the two-harmonic family and spatial modality.
- R. Lyons and G. White, *Monotonicity for continuous-time random walks*, arXiv:2109.10386 (2021). Accessible manuscript inspected for the scope of its monotonicity results.
- J. A. Cañizo, *Convolution of symmetric, radially decreasing functions*, expository online note (classical Euclidean convolution principle). Used only as comparative background, not a source for the cycle-specific threshold.
