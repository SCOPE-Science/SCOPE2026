# Metastable Wasserstein amplification through a single slow bond

## Finding
For every fixed integer \(m\ge2\), consider a path on \(2m\) vertices with jump rate \(1\) along every edge except its central edge, whose rate is \(\varepsilon\in(0,1]\), in **both** directions. All transport distances are shortest-path distances with **unit lengths on every edge**, including the slow edge. Write \(P_t^{(\varepsilon)}\) for the continuous-time Markov semigroup and
\[
\mathcal C_{m,\varepsilon}(t)=\sup_{\mu\ne\nu}\frac{W_1(\mu P_t^{(\varepsilon)},\nu P_t^{(\varepsilon)})}{W_1(\mu,\nu)},\qquad
\mathcal A_m(\varepsilon)=\max_{t\ge0}\mathcal C_{m,\varepsilon}(t).
\]
Set
\[
\lambda_m=4\sin^2\!\left(\frac{\pi}{2m}\right),\qquad
K_m=\frac4m\cos^2\!\left(\frac{\pi}{2m}\right).
\]
Then the following **two-term metastable amplification law** holds as \(\varepsilon\downarrow0\), with \(m\) held fixed:
\[
\boxed{\displaystyle
\mathcal A_m(\varepsilon)
=m-\frac{2\varepsilon}{\lambda_m}\log\frac1\varepsilon
-\varepsilon\left[\frac{(m-1)^2}{2}+\frac2{\lambda_m}(1+\log K_m)\right]
+o_m(\varepsilon).}
\]
Every maximizing time obeys
\[
\boxed{\displaystyle
 t_*(\varepsilon)=\frac1{\lambda_m}\log\frac{K_m}{\varepsilon}+o_m(1).}
\]
For each \(0<\varepsilon<1\), the semigroup has short-time transport amplification, whereas at \(\varepsilon=1\) it is nonexpansive. In particular, \(\lim_{\varepsilon\downarrow0}\mathcal A_m(\varepsilon)=m\); consequently there is **no dimension-independent upper bound** for the peak Wasserstein-one operator norms of finite, irreducible, symmetric birth–death semigroups on unit-length paths. No claim is made that the maximum has a closed elementary formula at arbitrary positive \(\varepsilon\).

## Assumptions and scope
The vertex set is \(\{0,\ldots,2m-1\}\). For an edge \(\{i,i+1\}\), let \(c_i=1\) except \(c_{m-1}=\varepsilon\). The generator on functions is
\[
(Q_\varepsilon f)(i)=c_{i-1}(f(i-1)-f(i))+c_i(f(i+1)-f(i)),
\]
where absent endpoint terms are omitted. Thus \(P_t^{(\varepsilon)}=e^{tQ_\varepsilon}\). It is symmetric with stationary measure uniform on the \(2m\) vertices, and is irreducible whenever \(\varepsilon>0\). In the Wasserstein cost \(d(i,j)=|i-j|\), the small jump rate does **not** shorten or lengthen the central geometric edge.

All asymptotic remainder statements are for fixed \(m\), not uniform as \(m\to\infty\). The maximization is over all \(t\ge0\) and all distinct probability measures \(\mu,\nu\).

## Proof
**1. Transport operator norm is a positive adjacent gradient.** Every birth–death process on a finite ordered path preserves stochastic order: couple two ordered copies independently until their first meeting, then use common randomness. Single nearest-neighbor jumps cannot reverse their order before a meeting. Hence \(P_t^{(\varepsilon)}(i,\cdot)\le_{\rm st}P_t^{(\varepsilon)}(i+1,\cdot)\). The one-dimensional Kantorovich formula and the monotone coupling therefore imply
\[
W_1(P_t^{(\varepsilon)}(i,\cdot),P_t^{(\varepsilon)}(i+1,\cdot))
=(P_t^{(\varepsilon)}x)(i+1)-(P_t^{(\varepsilon)}x)(i),\quad x(i)=i.
\]
For an arbitrary \(1\)-Lipschitz test function \(f\), its difference across any adjacent output vertices has absolute value at most the Wasserstein distance of the two corresponding kernel rows. Conversely the single test function \(x\) attains each of these distances. Therefore
\[
\mathcal C_{m,\varepsilon}(t)=\max_{0\le i<2m-1}g_i^\varepsilon(t),\quad
 g_i^\varepsilon(t):=(P_t^{(\varepsilon)}x)(i+1)-(P_t^{(\varepsilon)}x)(i)\ge0.
\]
This is an exact induced norm identity, not a random-pair estimate.

**2. Reflect across the weak bond.** The generator and initial coordinate function are equivariant under reflection \(i\mapsto2m-1-i\). Put \(z_j=j+1/2\) for \(0\le j<m\), and define the symmetric tridiagonal matrix \(R_\varepsilon\) by
\[
(R_\varepsilon v)_0=v_1-(1+2\varepsilon)v_0,\quad
(R_\varepsilon v)_j=v_{j-1}+v_{j+1}-2v_j\ (1\le j<m-1),\quad
(R_\varepsilon v)_{m-1}=v_{m-2}-v_{m-1}.
\]
For \(m=2\), only the first and last formulas are used. Writing \(e_0=(1,0,\ldots,0)\), the gradient across the central bond is **exactly**
\[
 g_{m-1}^\varepsilon(t)=2e_0^{\mathsf T}e^{tR_\varepsilon}z,
\qquad R_\varepsilon=R_0-2\varepsilon e_0e_0^{\mathsf T}.
\]
The matrix \(R_0\) is the reflecting-path generator on \(m\) points. Its eigenvalues are \(-\lambda_k\), with \(\lambda_k=4\sin^2(k\pi/(2m))\), \(0\le k<m\). An orthonormal eigenbasis is the constant vector \(m^{-1/2}{\bf1}\) and \(\sqrt{2/m}\cos(k\pi(j+1/2)/m)\) for \(k=1,\ldots,m-1\). Direct summation of this cosine basis against \(z\) yields
\[
 g_{m-1}^{0}(t)=m-\sum_{\substack{1\le k<m\\k\ \mathrm{odd}}}
 B_{m,k}e^{-\lambda_k t},\qquad
 B_{m,k}=\frac2m\cot^2\!\left(\frac{k\pi}{2m}\right)>0.
\]
In particular the central gradient increases strictly from \(1\) toward \(m\) when the bond is removed. The first decaying mode has \(\lambda_1=\lambda_m\), \(B_{m,1}=B_m\), and \(B_m\lambda_m/2=K_m\).

**3. First-order slow-mode perturbation.** Because the reflecting Laplacian \(-R_0\) has a simple zero eigenvalue separated from the others, the smallest eigenvalue \(\beta_0(\varepsilon)\) of \(-R_\varepsilon\), its spectral projection, and the remaining spectral modes vary analytically for small positive \(\varepsilon\). If \(\alpha_0(\varepsilon)\) denotes the coefficient of the slowest exponential in \(g_{m-1}^\varepsilon(t)\), then
\[
 \beta_0(\varepsilon)=\frac{2\varepsilon}{m}+O_m(\varepsilon^2),\qquad
 \alpha_0(\varepsilon)=m-\frac{(m-1)^2}{2}\varepsilon+O_m(\varepsilon^2).
\]
Here is an explicit check of the less immediate second coefficient. Normalize the positive slow eigenvector to have coordinate mean one and write \(v_\varepsilon={\bf1}+\varepsilon q+O_m(\varepsilon^2)\). Its first-order eigen-equation is \(R_0q=2(e_0-m^{-1}{\bf1})\), with \(\sum_jq_j=0\). Solving the reflecting discrete Poisson equation gives
\[
 q_j=-\frac{(m-1)(2m-1)}{3m}+2j-\frac{j(j+1)}m.
\]
Therefore \(\sum_jq_jj=m(m^2-1)/12\), and using
\[
 \alpha_0(\varepsilon)=\frac{2v_\varepsilon(0)\sum_j v_\varepsilon(j)(j+1/2)}{\sum_j v_\varepsilon(j)^2}
\]
gives \(\alpha_0'(0)=mq_0+2m^{-1}\sum_jq_jj=-(m-1)^2/2\). For the next mode, \(\beta_1(\varepsilon)=\lambda_m+O_m(\varepsilon)\) and \(\alpha_1(\varepsilon)=-B_m+O_m(\varepsilon)\). All remaining zero-order spectral coefficients either vanish or decay with rates strictly exceeding \(\lambda_m\).

**4. The global peak comes from the central bond.** At \(\varepsilon=0\), the walk splits into two reflecting uniform-rate paths. For any edge strictly inside either half, its gradient is at most \(1\) at all times, because the reflecting nearest-neighbor heat semigroup has a positive, substochastic discrete-gradient semigroup. This bound remains \(1+O_m(\varepsilon)\), uniformly over all \(t\ge0\), for small \(\varepsilon\): the vertex generator is a finite real-symmetric analytic matrix family; at \(\varepsilon=0\) it has a two-dimensional zero eigenspace (piecewise constants), annihilated by every within-half gradient. The perturbed slow spectral projector contributes only \(O_m(\varepsilon)\) to these gradients, uniformly in time. The remaining stable spectral subspace has a gap bounded below independently of small \(\varepsilon\); its heat operator differs from that at zero by \(O_m(\varepsilon)\) uniformly in time by the finite-dimensional Duhamel formula and analytic spectral projection. On the other hand, the central gradient at \(t\asymp\log(1/\varepsilon)\) tends to \(m>1\). Hence for all sufficiently small \(\varepsilon\), every global maximizing pair is the central neighboring pair, and \(\mathcal A_m(\varepsilon)=\max_t g_{m-1}^\varepsilon(t)\).

**5. Optimize the two competing time scales.** Let \(\lambda=\lambda_m\), \(B=B_m\), and set \(t=\lambda^{-1}\log(1/\varepsilon)+s\). For bounded real \(s\), the eigenexpansion from steps 2–3 gives, uniformly on bounded \(s\)-sets,
\[
 g_{m-1}^\varepsilon(t)=m-\frac{2\varepsilon}{\lambda}\log\frac1\varepsilon
 +\varepsilon\left[-\frac{(m-1)^2}{2}-2s-Be^{-\lambda s}\right]+o_m(\varepsilon).
\]
The omitted faster modes contribute \(o_m(\varepsilon)\), including modes with zero coefficient at \(\varepsilon=0\). The bounded-\(s\) limiting objective is strictly concave and uniquely maximized at
\[
 s_*=\frac1\lambda\log\frac{B\lambda}{2}=\frac1\lambda\log K_m.
\]
For completeness, global maximizers cannot escape this logarithmic window: at fixed bounded times the central gradient stays a positive distance below \(m\); on intermediate growing times the leading fast deficit \(B e^{-\lambda t}\) penalizes times much smaller than \(\lambda^{-1}\log(1/\varepsilon)\), while slow-mode decay \((2\varepsilon)t\) penalizes times much larger. On times beyond \(\varepsilon^{-1/2}\), the slow eigenvalue already produces a deficit of order at least \(\sqrt\varepsilon\), and the stable modes are exponentially negligible; this is much larger than the candidate \(O_m(\varepsilon\log(1/\varepsilon))\) deficit. These comparisons follow uniformly from the separated finite-dimensional eigenexpansion and establish tightness of the centered maximizing times. Evaluating the strictly concave limiting objective at \(s_*\), using \(Be^{-\lambda s_*}=2/\lambda\), gives both boxed asymptotic formulas.

**6. Nonexpansive boundary and arbitrarily large peaks.** Direct differentiation at time zero yields \((g_{m-1}^\varepsilon)'(0)=2(1-\varepsilon)\). Thus every \(0<\varepsilon<1\) produces \(\mathcal C_{m,\varepsilon}(t)>1\) for sufficiently small positive \(t\). When \(\varepsilon=1\), each edge-gradient solves a finite Dirichlet heat equation with row sums nonpositive, so \(\mathcal C_{m,1}(t)\le1\). Because \(\mathcal A_m(\varepsilon)\to m\) at each fixed \(m\), choosing successively larger \(m\) gives unbounded transient amplification over the stated class, although every individual positive-rate chain mixes and its operator norm tends to zero as \(t\to\infty\).

## Verification
Run `python check_slow_path.py` with Python 3, NumPy, and SciPy installed. The standalone checker builds the **full** \(2m\)-state generator independently of the reduced \(m\)-state matrix. It checks one-dimensional optimal transport by cumulative distribution sums, the adjacent-pair norm, the reflection formula, the unperturbed Fourier expansion, and the predicted maximizing-time and peak-height asymptotics. It makes 2,290 finite comparisons and assertions on the stated test grids, including \(m=2,\ldots,9\) and positive bridge rates down to \(10^{-6}\). Those checks do **not** replace the analytical argument or certify every parameter.

For example, at \(m=3\), one has \(\lambda_3=K_3=1\), so
\[
 t_*(\varepsilon)=\log(1/\varepsilon)+o(1),\qquad
 \mathcal A_3(\varepsilon)=3-2\varepsilon\log(1/\varepsilon)-4\varepsilon+o(\varepsilon).
\]
At \(m=2\), the corresponding formula is \(2-\varepsilon\log(1/\varepsilon)-3\varepsilon/2+o(\varepsilon)\).

## Relationship to prior work
Chafaï and Joulin, *Intertwining and commutation relations for birth–death processes* (2013), prove general stochastic-monotonicity and gradient/Feynman–Kac identities. Their Corollary 3.1 explicitly characterizes Wasserstein Lipschitz semigroup norms in terms of an auxiliary process. We use the same general phenomenon, but do not claim this operator-norm reduction or general birth–death intertwining as new. Münch and Wojciechowski (first arXiv release December 4, 2017) link graph curvature to heat-semigroup Lipschitz decay and include birth–death chains; their results do not state this two-well peak expansion. Landim, Loulakis and Mourragui (arXiv first released March 28, 2017) provide general metastable-well limit theory rather than a sharp global Wasserstein norm for this weak-link path. Münch (2019) establishes transport/heat inequalities for nonnegative Ollivier curvature, not the log-amplification coefficients in a negatively curved weak-link path.

The mathematical novelty assessed here is the **global peak amplitude and time at two asymptotic orders** for the specified symmetric finite path, including the explicit \(\varepsilon\log(1/\varepsilon)\) coefficient and order-\(\varepsilon\) correction, and its unbounded-in-dimension consequence. General semigroup, gradient, and spectral-perturbation principles are precedents, not inventions of this finding. Semantically equivalent older weak-link birth–death calculations remain a historical-priority risk.

## Limitations
The little-oh terms are for fixed \(m\) and \(\varepsilon\downarrow0\); no joint large-\(m\), small-\(\varepsilon\) uniformity is proved. The geometry is unit-edge path distance, **not** the resistance or rate-weighted distance. Only symmetric jump rates and a single central slow edge are considered. No elementary closed formula for \(\mathcal A_m(\varepsilon)\) at arbitrary finite positive \(\varepsilon\) is asserted. The initial rising slope and all-time limiting decay do not establish the precise number of local extrema at arbitrary \(\varepsilon\). The 2013 general intertwining result is acknowledged as prior art. Human/independent mathematical verification has not been performed.

## References
- F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (first posted 2017-12-04), https://arxiv.org/abs/1712.00875.
- D. Chafaï and A. Joulin, *Intertwining and commutation relations for birth–death processes*, Bernoulli 19 (2013), 1855–1879, arXiv:1011.2331, https://arxiv.org/abs/1011.2331.
- C. Landim, M. Loulakis and M. Mourragui, *Metastable Markov chains: from the convergence of the trace to the convergence of the finite-dimensional distributions*, arXiv:1703.09481 (first posted 2017-03-28), https://arxiv.org/abs/1703.09481.
- F. Münch, *Non-negative Ollivier curvature on graphs, reverse Poincaré inequality, Buser inequality, Liouville property, Harnack inequality and eigenvalue estimates*, arXiv:1907.13514 (first posted 2019-07-31), https://arxiv.org/abs/1907.13514.
