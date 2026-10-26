# A four-phase Poisson crossover at the deterministic edge of a chiral lattice walk

## Finding
Consider the translation-invariant chiral random walk on the unbounded square lattice described below. The deterministic coin is a clockwise four-cycle and is selected with probability \(p_n\) at each of the \(n\) steps; otherwise the direction is independently randomized. Suppose \(0\le p_n\le1\) and \(n(1-p_n)\to\lambda\in[0,\infty)\). For a walker initially at the origin with a uniform internal direction, the position \(X_n\) has a residue-dependent weak limit along each congruence class \(n\equiv r\pmod4\), \(r\in\{0,1,2,3\}\). The limits for \(r=1\) and \(r=3\) coincide for the uniform starting direction, leaving exactly three distinct residue-class laws for each fixed finite \(\lambda\). Its limiting characteristic function is, with \(c_j=\cos\theta_j\),

\[
\Phi_r(\theta_1,\theta_2;\lambda)=\frac14\bigg[(1+c_1)(1+c_2)e^{\lambda(g_0-1)}+(-1)^r(1-c_1)(1-c_2)e^{\lambda(g_2-1)}+2\cos(\pi r/2)(1-c_1c_2)e^{\lambda(g_1-1)}\bigg],
\]

where \(g_0=(1+c_1)(1+c_2)/4\), \(g_1=(1-c_1c_2)/4\), and \(g_2=(1-c_1)(1-c_2)/4\). This is a characteristic function of a probability distribution on \(\mathbb Z^2\), not an approximation to a Gaussian.

For all such sequences the unscaled mean-squared displacement has the exact limit

\[
\lim_{\substack{n\to\infty\\n\equiv r\pmod4}}\mathbb E\|X_n\|^2
=\lambda+1-e^{-\lambda}\cos(\pi r/2).
\]

There is also an orientation-independent compound-Poisson limit for a natural orbit-center observable. Write the directions in the order \(\rightarrow,\leftarrow,\uparrow,\downarrow\) and put \(B_{\rightarrow}=(0,0)\), \(B_{\leftarrow}=(1,1)\), \(B_{\uparrow}=(1,0)\), \(B_{\downarrow}=(0,1)\). For \(C_n=X_n+B_{D_n}\), the displacement \(C_n-C_0\) converges along **every** subsequence to a compound-Poisson sum with rate \(\lambda\) and increments \(U-V\), where \(U,V\) are independent uniform vertices of the unit square. Its characteristic function is

\[
\exp\!\left\{\lambda\left[\frac{(1+\cos\theta_1)(1+\cos\theta_2)}4-1\right]\right\}.
\]

This center statement holds for every fixed initial direction as well as mixtures of initial directions. For the limiting family, a further \(\lambda\to\infty\) rescaling sends the position divided by \(\sqrt\lambda\) to a centered bivariate Gaussian with covariance \(I_2/2\).

## Assumptions and scope
The walk has no walls, obstacles, spatially varying coins, or coherent quantum amplitudes. Its state is \((X_t,D_t)\in\mathbb Z^2\times\{\rightarrow,\leftarrow,\uparrow,\downarrow\}\). At each time, independently select with probability \(p_n\) the permutation \(P:\rightarrow\mapsto\downarrow\mapsto\leftarrow\mapsto\uparrow\mapsto\rightarrow\), or with probability \(1-p_n\) choose the new direction uniformly from the four possibilities. Move by one lattice unit in the selected direction. The parameter is constant within each length-\(n\) experiment, although it can depend on the experiment length. Distances use unit lattice spacing. The displayed position law assumes \(X_0=(0,0)\) and uniform \(D_0\); the center law permits any fixed initial direction. Convergence is for fixed \(\lambda\) as \(n\to\infty\) within each residue class.

## Proof
**1. Four-step rotating frame.** Let \(v_d\) be the signed unit vector associated with direction \(d\), and define \(B_d\) as above. Directly for all four directions, \(B_{Pd}+v_{Pd}=B_d\). Thus the center \(C=X+B_D\) is preserved under every deterministic step. For Fourier variable \(\theta\), transform the center coordinate instead of the position. Then the deterministic step acts only as the permutation matrix \(P\), satisfying \(P^4=I\). The fully randomized step has Fourier matrix

\[
Q(\theta)_{b,a}=\tfrac14\exp\big(i\theta\cdot(B_{P^{-1}b}-B_a)\big).
\]

Consequently the Fourier evolution matrix of one step is \(M_n(\theta)=P+\varepsilon_n(Q-P)\), with \(\varepsilon_n=1-p_n\).

**2. Critical matrix limit.** Expanding four factors, uniformly for fixed real \(\theta\),

\[
M_n(\theta)^4=I+4\varepsilon_n\big(G(\theta)-I\big)+O(\varepsilon_n^2),
\quad G(\theta)=\tfrac14\sum_{j=0}^3P^{-j-1}Q(\theta)P^j.
\]

All matrices here are four-by-four and the remainder bound follows from a finite polynomial expansion. The matrix \(G\) commutes with \(P\) by the cyclic twirl. If \(n=4m+r\), the matrix-power limit \((I+4\varepsilon_n(G-I)+O(\varepsilon_n^2))^m\to e^{\lambda(G-I)}\) gives

\[
M_n(\theta)^n\longrightarrow P^r e^{\lambda(G(\theta)-I)}.
\]

This also covers \(\lambda=0\) since \(n\varepsilon_n^2\to0\). These pointwise limits are continuous at \(\theta=0\), and hence determine weak limits by the characteristic-function continuity theorem.

**3. Explicit diagonalization.** In cyclic order \(\rightarrow,\downarrow,\leftarrow,\uparrow\), the four center offsets are \((0,0),(0,1),(1,1),(1,0)\). For starting direction \(a\) and final direction \(b\),

\[
G_{b,a}(\theta)=\tfrac1{16}\sum_{j=0}^3
\exp\!\big(i\theta\cdot(B_{P^jb}-B_{P^ja})\big).
\]

The diagonal terms equal \(1/4\); the two adjacent cyclic differences have coefficient \((\cos\theta_1+\cos\theta_2)/8\); the opposite difference has coefficient \(\cos\theta_1\cos\theta_2/4\). Therefore

\[
G=\tfrac14[I+a(P+P^{-1})+bP^2],\qquad
 a=(c_1+c_2)/2,\quad b=c_1c_2.
\]

The four cyclic Fourier eigenvalues are \(g_0,g_1,g_2,g_1\). Converting the uniform initial direction and the final center coordinate back to physical position gives Fourier-mode weights \((1+c_1)(1+c_2)/4\), \((1-c_1c_2)/4\) twice, and \((1-c_1)(1-c_2)/4\). The residual \(P^r\) multiplies modes by \(1,i^r,(-1)^r,(-i)^r\). Combining the conjugate pair yields the stated \(\Phi_r\). Odd and even residues are distinguished by the Fourier value at \(\theta=(\pi,\pi)\), while residues \(r=0\) and \(r=2\) give \(e^{-\lambda/2}\) and \(-e^{-\lambda/2}\) at \(\theta=(\pi,0)\). Thus exactly three laws remain for each finite \(\lambda\), since the formulas for \(r=1\) and \(r=3\) agree.

**4. Compound-Poisson orbit center.** The sum of every column of \(G(\theta)\) equals \(g_0(\theta)\). Hence summing over the final direction after the matrix limit gives \(\exp[\lambda(g_0-1)]\), independently of the initial direction. Moreover \(g_0(\theta)\) is exactly the characteristic function of \(U-V\) for independent uniform unit-square vertices. The Lévy–Khintchine formula here is simply the power-series identity for a Poisson sum. Each coordinate jump is \(-1,0,+1\) with probabilities \(1/4,1/2,1/4\); the coordinates of one jump are independent. In particular the center's limiting covariance is \(\lambda I_2/2\). The Gaussian limit as \(\lambda\to\infty\) follows from \(g_0(\theta/\sqrt\lambda)=1-\|\theta\|^2/(4\lambda)+O(\lambda^{-2})\), and the position differs from the center by a bounded vector.

**5. Exact finite-time mean square and its limit.** A uniform initial direction stays uniform. The velocity correlation at lag \(k\) is exactly \(p_n^k\cos(\pi k/2)\): the same deterministic clockwise update must be selected at each of the \(k\) intervening steps to preserve directional correlation. Therefore, with \(z=ip_n\),

\[
\mathbb E\|X_n\|^2=n+2\sum_{k=1}^{n-1}(n-k)p_n^k\cos(\pi k/2)
=\frac{n(1-p_n^2)}{1+p_n^2}-2\operatorname{Re}\frac{z}{(1-z)^2}+2\operatorname{Re}\frac{z^{n+1}}{(1-z)^2}.
\]

In the critical window the three terms converge respectively to \(\lambda\), \(1\), and \(-e^{-\lambda}\cos(\pi r/2)\). This proves the moment formula without relying on weak convergence to exchange moments and limits.

## Verification
The standalone script `verify.py` computes small-time position distributions by direct state enumeration, confirms the exact finite-time mean square, and independently forms the Fourier transition matrix and high powers for all four congruence classes. It compares their characteristic functions to the three-exponential limit and their mean squares to the stated limit. All 124 checks in the supplied test configuration pass. The infinite-limit and compound-Poisson assertions are established by the matrix and probability arguments above; finite computations are supplementary.

## Relationship to prior work
Wójcik and Kalz, *The chiral random walk: A quantum-inspired framework for odd diffusion* (arXiv:2602.09920v1, first public February 10, 2026), introduce this four-direction coin and derive long-time transport coefficients for a fixed \(p<1\), alongside topological effects at \(p=1\). Their fixed-parameter Green–Kubo expression does not itself give the joint limit with \(n(1-p_n)\to\lambda\), and their full-text discussion does not state the four-residue limiting law, its Poisson orbit center, or the exact critical-window mean-square profile. Uhlig, Wójcik, Metzler, and Kalz (arXiv:2609.12680v1) use the same coin to investigate diffusion and first-passage behavior in disordered environments; their homogeneous formulas also concern fixed parameters. Earlier continuous-time cyclic random-flight literature, including Iuliano and Verasani (2024), changes direction at arrival times rather than performing rapid deterministic four-cycles interrupted by rare complete direction resets; it does not imply the present lattice critical-window characteristic function without further analysis.

## Limitations
The result is for the **classical probability evolution** of the quantum-inspired walk on an obstacle-free, infinite square lattice, not for quantum interference, coherent amplitudes, finite boundaries, or disorder. It is an iterated critical limit, not a uniform error bound for arbitrary sequences outside \(n(1-p_n)\to\lambda\). The large-\(\lambda\) Gaussian statement concerns the resulting limiting distributions (with \(\lambda\to\infty\) after \(n\to\infty\)). Neither global priority nor applicability to general four-state coins is claimed.

## References
1. J. Wójcik and E. Kalz, *The chiral random walk: A quantum-inspired framework for odd diffusion*, arXiv:2602.09920v1 (2026-02-10), https://arxiv.org/html/2602.09920v1.
2. J. Uhlig, J. Wójcik, R. Metzler, and E. Kalz, *Chirality enhances diffusion in disordered environments*, arXiv:2609.12680v1 (2026-09-11), https://arxiv.org/html/2609.12680v1.
3. A. Iuliano and G. Verasani, *A Cyclic Random Motion in R3 Driven by Geometric Counting Processes*, Methodology and Computing in Applied Probability 26, 14 (2024), https://doi.org/10.1007/s11009-024-10083-0.
