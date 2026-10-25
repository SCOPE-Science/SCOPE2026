# Sharp static LQR locality cost on a nearest-neighbor cyclic network

## Finding

For a stable discrete-time linear-quadratic network with scalar nodes, identical local dynamics, and strictly positive nearest-neighbor state-cost coupling, the optimal cost of restricting **static state feedback** to graph radius \(r\) has the exact asymptotic order
\[
\Delta_r=\Theta\!\left(r^{-3}4^{-r}\right),\qquad r\longrightarrow\infty.
\]
Here \(\Delta_r\) is the limsup, over increasing cycle sizes, of the minimum per-node stationary excess LQR cost among all stable radius-\(r\) static real feedback matrices; no translation-invariance assumption is imposed on the competing matrices.

The optimal centralized feedback kernel has coefficients satisfying
\[
k_j=(-1)^{j-1}\frac{\sqrt3}{2\sqrt\pi}\frac{2^{-j}}{j^{3/2}}\left(1+O(j^{-1})\right),\qquad j\to\infty.
\]
Consequently, writing \(E_r=2\sum_{j>r}k_j^2\),
\[
E_r\sim\frac{r^{-3}4^{-r}}{2\pi},\qquad
\liminf_{N\to\infty}\Delta_{N,r}\ge \frac12E_r.
\]
A finite-range Fourier truncation of the gain attains a uniform cost bound \(\limsup_N\Delta_{N,r}\le C E_r\) for all sufficiently large \(r\). Thus a radius sufficient and necessary, within this static-feedback class, for a thermodynamic-limit excess cost at most \(\varepsilon\) obeys
\[
r(\varepsilon)=\frac{\log(1/\varepsilon)-3\log\log(1/\varepsilon)}{\log4}+O(1).
\]
The logarithms are natural, and the bounded term may depend on the fixed physical parameters.

## Assumptions and scope

For every integer \(N\ge3\), let \(S_N\) be the cyclic shift on \(\mathbb R^N\), and set
\[
A_N=\tfrac12I_N,\qquad B_N=I_N,\qquad
Q_N=\tfrac94I_N+S_N+S_N^{\mathsf T},\qquad R_N=I_N.
\]
The state evolves as \(x_{t+1}=A_Nx_t+u_t+w_t\), where the disturbances are independent, centered and have covariance \(I_N\). The state cost is \(\tfrac12 x_t^{\mathsf T}Q_Nx_t\) and the input cost is \(\tfrac12u_t^{\mathsf T}u_t\). Because the Fourier symbol of \(Q_N\) is \(q(\theta)=9/4+2\cos\theta\ge1/4\), all these are valid positive-definite state weights.

A static gain \(F_N\in\mathbb R^{N\times N}\) produces \(u_t=-F_Nx_t\) and is called stable if the spectral radius of \(\tfrac12I_N-F_N\) is strictly smaller than \(1\). Its graph radius is at most \(r\) if \((F_N)_{ij}=0\) whenever the minimum cyclic distance between \(i\) and \(j\) exceeds \(r\). No normality, symmetry, translation invariance, or sign condition is required of admissible \(F_N\).

For stable feedback define the stationary covariance \(\Sigma_{F_N}\) by \(\Sigma_{F_N}=I_N+(\tfrac12I_N-F_N)\Sigma_{F_N}(\tfrac12I_N-F_N)^{\mathsf T}\), and define the normalized cost
\[
J_N(F_N)=\frac1{2N}\operatorname{tr}\big[(Q_N+F_N^{\mathsf T}F_N)\Sigma_{F_N}\big].
\]
Let \(K_N\) be the unique optimal unconstrained LQR gain and let \(\Delta_{N,r}\) be the infimum of \(J_N(F_N)-J_N(K_N)\) over all stable radius-\(r\) real static gains. An empty infimum is \(+\infty\), although the construction below gives feasible candidates for large \(r\). Set \(\Delta_r=\limsup_{N\to\infty}\Delta_{N,r}\), with \(r\) fixed before the network-size limit.

## Proof

**1. Scalar Riccati symbol.** The stabilizing Riccati solution \(P_N\succ0\) is circulant. At frequency \(\theta\), its eigenvalue \(p=p(q)\) obeys the scalar Riccati equation
\[
p=q+\frac{p}{4(1+p)},\qquad
p(q)=\frac{q-3/4+\sqrt{(q+1/4)(q+9/4)}}2.
\]
Here the square root is positive for real \(q\ge1/4\). The centralized feedback is \(K_N=\tfrac12 P_N(I_N+P_N)^{-1}\), with real-even Fourier symbol
\[
k(\theta)=\frac{p(q(\theta))}{2(1+p(q(\theta)))},\qquad 0<k(\theta)<\tfrac12.
\]
Its closed-loop eigenvalues lie strictly between \(0\) and \(1/2\). Define infinite-volume Fourier coefficients by \(k_j=(2\pi)^{-1}\int_{-\pi}^{\pi}k(\theta)e^{-ij\theta}\,d\theta\), so \(k_{-j}=k_j\in\mathbb R\).

**2. Exact performance-difference identity.** Riccati completion of squares gives, for every stable (possibly nonnormal and noncirculant) static \(F_N\),
\[
J_N(F_N)-J_N(K_N)=\frac1{2N}\operatorname{tr}\left[(F_N-K_N)^{\mathsf T}(I_N+P_N)(F_N-K_N)\Sigma_{F_N}\right].
\]
Indeed, the Riccati equation cancels all terms not involving the square, and summing the resulting one-step identity in stationary state yields the displayed equality. As \(I_N+P_N\succeq I_N\) and \(\Sigma_{F_N}=I_N+\sum_{j\ge1}(\tfrac12I_N-F_N)^j((\tfrac12I_N-F_N)^j)^{\mathsf T}\succeq I_N\),
\[
J_N(F_N)-J_N(K_N)\ge\frac1{2N}\|F_N-K_N\|_F^2.
\]
The cycle is distance-regular and \(K_N\) is circulant. Removing its entries within radius \(r\) is the best Frobenius approximation among **all** radius-\(r\) matrices; hence, without assuming a circulant competitor,
\[
\Delta_{N,r}\ge\frac1{2N}\sum_{d_{\rm cyc}(i,j)>r}|(K_N)_{ij}|^2.
\]
As \(N\to\infty\) with \(r\) fixed, this normalized squared tail converges to \(E_r=2\sum_{j>r}k_j^2\). This follows either from Parseval applied to discrete Fourier samples and their trigonometric projections or from convergence of the samples to the Fourier integral together with boundedness of the total Fourier energy. Thus \(\liminf_N\Delta_{N,r}\ge E_r/2\).

**3. Nearest complex singularity and sharp coefficient.** Write \(z=e^{i\theta}\) and \(q(z)=9/4+z+z^{-1}\). The algebraic gain \(k(z)\) has an analytic Laurent continuation across the unit circle in the annulus \(1/2<|z|<2\). The nearest outer square-root branch point occurs at \(z=-2\), because \(q(-2)=-1/4\). The other branch points corresponding to \(q=-9/4\) have modulus greater than \(2\) on the exterior side. With \(w=1+z/2\), the local expansions on the continuation from the unit circle are
\[
q(z)+\tfrac14=\tfrac32w+O(w^2),\quad
\sqrt{(q(z)+1/4)(q(z)+9/4)}=\sqrt3\,w^{1/2}+O(w^{3/2}),
\]
\[
p(z)=-\tfrac12+\tfrac{\sqrt3}{2}w^{1/2}+O(w),\qquad
k(z)=-\tfrac12+\sqrt3\,w^{1/2}+O(w).
\]
The next nonanalytic term is of order \(w^{3/2}\). Standard coefficient extraction for an isolated algebraic square-root singularity, applied to the positive Laurent coefficients, gives
\[
k_j=\sqrt3\,[z^j](1+z/2)^{1/2}+O(2^{-j}j^{-5/2})
=(-1)^{j-1}\frac{\sqrt3}{2\sqrt\pi}\,2^{-j}j^{-3/2}(1+O(j^{-1})).
\]
The inner branch point contributes to negative rather than positive Laurent indices; there are no other singularities on the outer modulus-\(2\) circle. Squaring and summing the geometric tail gives
\[
E_r=2\sum_{j>r}k_j^2
\sim\frac{3}{2\pi}\frac{4^{-(r+1)}}{(r+1)^3}\frac1{1-1/4}
\sim\frac{r^{-3}4^{-r}}{2\pi}.
\]

**4. Matching finite-range construction.** Let \(k^{(r)}(\theta)=\sum_{|j|\le r}k_j e^{ij\theta}\), and for \(N>2r\) let \(F_N^{(r)}\) be the corresponding real symmetric circulant radius-\(r\) feedback gain. By the exponential Fourier tail, \(\sup_\theta|k^{(r)}(\theta)-k(\theta)|\le\sum_{|j|>r}|k_j|\to0\). Since \(0<k(\theta)<1/2\), for all sufficiently large \(r\), uniformly in \(N\), \(\|\tfrac12I_N-F_N^{(r)}\|_2\le3/4\). Consequently \(\Sigma_{F_N^{(r)}}\preceq(1-(3/4)^2)^{-1}I_N\). Also \(I_N+P_N\preceq C_PI_N\), where \(C_P=1+p(17/4)\) is independent of \(N\). The identity of step 2 therefore implies
\[
J_N(F_N^{(r)})-J_N(K_N)
\le\frac{8C_P}{7N}\|F_N^{(r)}-K_N\|_F^2.
\]
Discrete Fourier sampling and Parseval show \(\lim_{N\to\infty}N^{-1}\|F_N^{(r)}-K_N\|_F^2=E_r\). Therefore, for all large \(r\),
\[
\frac12 E_r\le\liminf_{N\to\infty}\Delta_{N,r}\le\Delta_r\le\frac{8C_P}{7}E_r.
\]
This proves the two-sided sharp \(\Theta(r^{-3}4^{-r})\) law. Solving these two-sided inequalities for the smallest integer radius with \(\Delta_r\le\varepsilon\) yields \(r(\varepsilon)=[\log(1/\varepsilon)-3\log\log(1/\varepsilon)]/\log4+O(1)\).

## Verification

The standalone `check.py` evaluates the Riccati symbol, compares Fourier coefficients with the algebraic singularity prediction, and checks the exact Riccati cost-difference identity and radial Fourier tails on cycles with multiple sizes. Run with Python 3 and NumPy using `python check.py`. The analytic proof, not the finite floating-point checks, establishes the universal limits and lower bound against arbitrary noncirculant static controllers.

## Relationship to prior work

Zhou and Matias (arXiv:2610.11699v1, 8 October 2026) prove general upper bounds for spatiotemporal decay of near-optimal distributed LQR responses, with logarithmic sufficient communication ranges. Shin, Lin, Qu, Wierman and Anitescu (arXiv:2204.05551v2) prove exponential decay of centralized gains and exponentially small performance loss from truncated static feedback under network assumptions. The present result gives a complementary **sharp lower bound**, an exact geometric base and a nontrivial cubic polynomial factor for one explicitly specified cost-coupled cyclic family. The proof does not rely on interpreting general upper bounds as a necessity claim. Earlier spatially invariant Riccati and spectral-factorization literature supplies relevant analytic techniques; the exact cost-gap asymptotic should not be presented as a theorem for all locally coupled networks.

## Limitations

The lower bound is for stable memoryless state-feedback matrices with a strict graph-radius constraint, not all causal/dynamic/distributed controllers or SLS impulse-response-local policies. The radius is fixed before taking the cycle-size limit; simultaneous radius/network-size limits are not addressed. The statement establishes an exact asymptotic **order**, not an exact leading coefficient for the *optimally minimized cost gap*. The coefficient and \(E_r\) formulas refer to the centralized feedback kernel. No finite-precision guarantees or sample-complexity claims are made. Algebraic singularity analysis is classical; the claimed contribution is its use together with a uniform Riccati performance-difference lower bound to quantify static control locality cost on this specific family.

## References

1. Chenchen Zhou and José Matias, *Spatiotemporal Response Decay for Near-Optimal Distributed LQR via System Level Synthesis*, arXiv:2610.11699v1 (first public 8 October 2026), https://arxiv.org/abs/2610.11699.
2. Sungho Shin, Yiheng Lin, Guannan Qu, Adam Wierman, and Mihai Anitescu, *Near-Optimal Distributed Linear-Quadratic Regulator for Networked Systems*, arXiv:2204.05551v2 (2022), https://arxiv.org/abs/2204.05551.
3. Zhang, Li and Li, *On the Optimal Control of Network LQR with Spatially-Exponential Decaying Structure*, arXiv:2209.14376 (2022), https://arxiv.org/abs/2209.14376.
4. Emily Jensen, Jonathan P. Epperlein and Bassam Bamieh, *Localization of the LQR Feedback Kernel in Spatially-Invariant Problems over Sobolev Spaces*, Proceedings of IEEE CDC (2020), DOI:10.1109/CDC42340.2020.9304235.
