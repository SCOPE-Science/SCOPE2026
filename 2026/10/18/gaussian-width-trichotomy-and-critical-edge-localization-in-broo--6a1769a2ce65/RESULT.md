# Gaussian width trichotomy and critical edge localization in broom-tree root polytopes

## Finding
For integers \(h\ge2\), \(p\ge2\), let \(B_{h,p}\) be the broom tree formed from a hub \(v_0\), \(h\) pendant leaves \(w_1,\ldots,w_h\), and the path \(v_0v_1\cdots v_p\). With \(n=h+p+1\), let
\[
P_{h,p}=\operatorname{conv}\{\pm(e_u-e_v):uv\in E(B_{h,p})\}\subset\{x\in\mathbb R^n:\textstyle\sum_i x_i=0\}.
\]
Let \(U_{h,p}\) be a Haar-uniform intrinsic unit vector, \(W_{h,p}\) the Euclidean directional width of \(P_{h,p}\), and
\[
Y_{h,p}=\frac{\sqrt{h+p}}2 W_{h,p}(U_{h,p}).
\]
For real \(m>1\) define
\[
b_m=\sqrt{2\log m}-\frac{\log\log m+\log(4\pi)}{2\sqrt{2\log m}},\qquad
c_p=\sqrt2\,b_{2(p-1)},\qquad
s_p=\frac{\sqrt2}{\sqrt{2\log(2(p-1))}},
\]
and let \(\Delta_{h,p}=b_h-c_p\). As \(h,p\to\infty\), the following exhaustive asymptotic regimes hold whenever the indicated limit exists:

1. If \(\Delta_{h,p}\to-\infty\), then \((Y_{h,p}-c_p)/s_p\) converges in law to a standard Gumbel variable \(\mathcal G\), with \(\Pr(\mathcal G\le x)=\exp(-e^{-x})\). The path edges supply the exposed vertex with probability tending to one.
2. If \(\Delta_{h,p}\to+\infty\), then \(Y_{h,p}-b_h\) converges in distribution and in second moment to \(|Z|\) for \(Z\sim N(0,1)\). Pendant edges supply the exposed vertex with probability tending to one.
3. If \(\Delta_{h,p}\to t\in\mathbb R\), then \(Y_{h,p}-c_p\) converges in distribution and in second moment to
\[
T_t=(|Z|+t)_+=\max\{|Z|+t,0\}.
\]
The probability that an exposed vertex comes from a path edge (including the hub–path bridge) tends to
\[
q_t=\begin{cases}2\Phi(-t)-1,&t<0,\\0,&t\ge0,\end{cases}
\]
where \(\Phi\) is the standard normal CDF. Hence \(T_t\) has an atom at zero of precisely mass \(q_t\) for \(t<0\), and no atom for \(t\ge0\). The pendant-edge exposure probability tends to \(1-q_t\).

The critical window has an explicit graph-size description. For fixed \(\lambda\in\mathbb R\), taking
\[
h=\left\lfloor p^2\exp\bigl(\lambda\sqrt{\log p}\bigr)\right\rfloor
\]
gives \(\Delta_{h,p}\to\lambda/2\), so
\[
Y_{h,p}-2\sqrt{\log p}\ \Longrightarrow\ (|Z|+\lambda/2)_+.
\]
For \(\lambda<0\), the exact limiting path-exposure share and atomic mass are \(2\Phi(-\lambda/2)-1\); for \(\lambda\ge0\) this share vanishes. By contrast, \(h=\lfloor p^\alpha\rfloor\) gives the path-Gumbel regime when \(0<\alpha<2\) and the pendant-half-normal regime when \(\alpha>2\).

In the critical regime, the first two centered moments converge. Put \(a=-t>0\) when \(t<0\), and write \(\varphi\) for the standard normal density and \(\overline\Phi=1-\Phi\). Then
\[
\begin{aligned}
\mu_t=\mathbb ET_t&=\begin{cases}t+\sqrt{2/\pi},&t\ge0,\\2\bigl[\varphi(a)-a\overline\Phi(a)\bigr],&t<0,\end{cases}\\
\nu_t=\mathbb ET_t^2&=\begin{cases}1+2t\sqrt{2/\pi}+t^2,&t\ge0,\\2\bigl[(1+a^2)\overline\Phi(a)-a\varphi(a)\bigr],&t<0.\end{cases}
\end{aligned}
\]
Consequently \(\mathbb EY_{h,p}=c_p+\mu_t+o(1)\) and \(\operatorname{Var}(Y_{h,p})\to\nu_t-\mu_t^2\) whenever \(\Delta_{h,p}\to t\).

## Assumptions and scope
The graph has exactly \(h+p+1\) distinct vertices, \(h\) true pendant leaves and a handle of \(p\) edges. The polytope uses unweighted standard roots and the inherited Euclidean metric on the zero-coordinate-sum subspace. A random direction is uniform on that subspace's unit sphere. All asymptotic assertions concern integer sequences \(h,p\to\infty\); the three limits are conditional on the behavior of the *specified* gap \(\Delta_{h,p}\). No claim is made about an arbitrary graph sequence, nonuniform edge weights, non-Euclidean norms, or sequences for which the gap has no limit. "Exposed vertex" means the almost surely unique maximizer of the linear functional given by the random direction; antipodal root vertices are counted separately but grouped here by their underlying edge.

Every tree-root polytope with \(n\) vertices is a \((n-1)\)-dimensional crosspolytope under an invertible linear map, with \(2(n-1)\) vertices, \(2^{n-1}\) facets, and the same intrinsic volume \(2^{n-1}\sqrt n/(n-1)!\). Thus the fluctuation and exposure transitions here are Euclidean rather than changes in face lattice or lattice volume.

## Proof
**Step 1: exact Gaussian reduction.** Give the graph vertices independent standard Gaussian labels \(G_x\). Orthogonally project \(G\) to the zero-sum hyperplane and let \(R=\|\Pi G\|/\sqrt{n-1}\). Then \(R^2\) has law \(\chi^2_{n-1}/(n-1)\), the normalized projection direction is uniform, and central symmetry gives the exact coupled identity
\[
Y_{h,p}=R^{-1}H_{h,p},\qquad H_{h,p}=\max_{uv\in E(B_{h,p})}|G_u-G_v|.
\]
Set
\[
S_h=\max_{1\le j\le h}|G_{w_j}-G_{v_0}|,\quad
L_p=\max_{2\le j\le p}|G_{v_j}-G_{v_{j-1}}|,\quad
J=|G_{v_1}-G_{v_0}|.
\]
Then \(H_{h,p}=\max(S_h,L_p,J)\). The first two variables are *exactly independent*, since their Gaussian label sets are disjoint. The bridge \(J\) is tight while \(\max(S_h,L_p)\to\infty\) in probability, so \(\Pr(J>\max(S_h,L_p))\to0\). This controls both the width and the identity of the maximizing edge.

**Step 2: the hub extreme.** Let \(Z=G_{v_0}\), and let \(M_h^+=\max_jG_{w_j}\), \(M_h^-=\max_j(-G_{w_j})\). Both Gaussian maxima satisfy \(M_h^\pm-b_h\to0\) in \(L^2\), by the normal maximum tail estimates and the displayed \(b_h\). Because
\[
S_h=\max\{M_h^+-Z,M_h^-+Z\},
\]
and the maximum map is Lipschitz in the sup norm, \(S_h-b_h-|Z|\to0\) in \(L^2\). The hub coordinate therefore induces an order-one half-normal fluctuation that does not vanish in the extremal limit.

**Step 3: the handle extreme at both scales.** Let \(q=p-1\) and \(X_j=(G_{v_{j+1}}-G_{v_j})/\sqrt2\) for \(j=1,\ldots,q\). This is a stationary centered Gaussian sequence with unit variances, adjacent covariance \(-1/2\), and independence at index gaps at least two. Here \(L_p=\sqrt2\max_{j\le q}|X_j|\).

At threshold \(u_q(x)=b_{2q}+x/\sqrt{2\log(2q)}\), the expected number of exceedances \(\sum_{j\le q}\mathbf1_{\{|X_j|>u_q(x)\}}\) tends to \(e^{-x}\). For adjacent indices and any choice of two signs, the signed sum has variance at most three, hence
\[
\Pr(|X_j|>u,|X_{j+1}|>u)\le4\exp(-2u^2/3).
\]
The adjacent-pair sum is \(O(q^{-1/3}(\log q)^C)\to0\), while the dependency-neighborhood sum of products of single-site exceedance probabilities is \(O(q^{-1})\). The elementary local-dependence Poisson approximation therefore gives a Poisson limit with mean \(e^{-x}\), which proves
\[
\frac{L_p-c_p}{s_p}\Longrightarrow\mathcal G.
\]
For the coarser second-moment estimate, split the indices into even and odd classes. Within each class the \(X_j\) are independent. The maximum of \(\lfloor q/2\rfloor\) independent absolute standard Gaussians, after multiplication by \(\sqrt2\), differs from \(c_p\) by a quantity tending to zero in \(L^2\): its own normal extreme-value center differs from \(c_p\) by \(o(1)\). Since the overall maximum is the maximum of the even and odd maxima, it follows that \(L_p-c_p\to0\) in \(L^2\).

**Step 4: spherical normalization at the fine scale.** Set \(d=n-1=h+p\). Gaussian maximal inequalities give \(\mathbb EH_{h,p}^4=O((\log n)^2)\), while the inverse chi-square moment formulas imply \(\mathbb E(R^{-1}-1)^4=O(d^{-2})\). By Cauchy–Schwarz,
\[
\mathbb E|Y_{h,p}-H_{h,p}|^2
=O(\log n/d).
\]
As \(d\ge p\), this is \(o(s_p^2)\) as well as \(o(1)\). Thus the Gaussian and intrinsic spherical statements have the same limits at both prescribed scales.

**Step 5: competition and localization.** Combine Steps 2–4 with
\[
H_{h,p}=\max\{b_h+|Z|+o_{L^2}(1),\ c_p+o_{L^2}(1),\ J\}.
\]
If the difference of centers tends to either infinity, the appropriate component wins with probability tending to one; the finer handle Gumbel statement applies in the negative regime because the pendant competition event has vanishing probability. If \(\Delta_{h,p}\to t\), the max map gives \(Y-c_p\to\max(|Z|+t,0)\) in \(L^2\). The sign of \(|Z|+t\) selects the winning edge family except on a zero-probability boundary, proving the exposure shares. Direct integration of the half-normal density gives the displayed moments. Finally, with \(h=\lfloor p^2e^{\lambda\sqrt{\log p}}\rfloor\), expansion of the explicit Gaussian centers gives \(b_h-c_p\to\lambda/2\) and \(c_p-2\sqrt{\log p}\to0\).

## Verification
The accompanying dependency-free-in-data Python checker `VERIFY.py` (using NumPy and SciPy for computation) verifies the exact support-function reduction by direct signed-vertex maximization and independently checks the tridiagonal Gaussian covariance structure. On its fixed random seed it passes 3,600 finite support and width identities and 9,454 exact covariance-entry identities, three analytical half-normal atomic-mass sampling diagnostics, and three path-dominated scale sanity checks involving 550 samples each. Run `python VERIFY.py` in a Python environment with NumPy and SciPy. The finite checks corroborate exact identities; the limiting Gumbel, half-normal, critical atom, and exposure probability assertions follow from the preceding analytic proof, not from simulation.

## Relationship to prior work
D'Alì, Delucchi and Michałek (arXiv:1910.05193, original 2019 version) place tree symmetric edge polytopes within the metric/Kantorovich–Rubinstein polytope framework and explicitly identify their crosspolytope equivalence. D'Alì, Juhnke-Kubitzke and Koch (arXiv:2307.04933) prove regular-matroid equivalence for the larger class. Braun and Bruegge (arXiv:2201.13303) analyze facets of sparse-graph symmetric edge polytopes. These structural and face-count results do not provide directional-width distributions or the probability of exposing a root from a specified graph branch. Standard stationary-Gaussian extreme-value theory, described for instance by Hashorva and Weng (arXiv:1312.2151), supplies the known Gumbel mechanism for weakly dependent maxima. Its ingredients are used, not claimed as new. Earlier leading-order mean-width results for tree-root polytopes do not imply the order-one critical law, its atom, its limiting variance, or the edge-family exposure split. The present contribution is precisely that graph-parametrized crossover and geometric localization.

## Limitations
This is an asymptotic theorem for unweighted broom trees, not a global extremal width theorem over trees, and the critical limit's atom concerns a centered width distribution, not any atomic mass at a vertex in the finite-dimensional sphere. The Gumbel regime establishes weak convergence but does not assert fine-scale moment convergence. The reported provenance and comparisons do not constitute an independent mathematical audit or a proof of absolute bibliographic novelty. Equivalent earlier formulations in broader Gaussian moving-average extremal-process literature remain possible.

## References
1. A. D'Alì, E. Delucchi and M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193 (first public version 2019-10-11), Sections 1–2 and Example 2.3. https://arxiv.org/abs/1910.05193.
2. A. D'Alì, M. Juhnke-Kubitzke and M. Koch, *On a Generalization of Symmetric Edge Polytopes to Regular Matroids*, arXiv:2307.04933 (first public version 2023-07-10), Sections 1 and 3–4. https://arxiv.org/abs/2307.04933.
3. B. Braun and K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303 (first public version 2022-01-31), Sections 1–2. https://arxiv.org/abs/2201.13303.
4. E. Hashorva and Z. Weng, *Limit Laws for Maxima of Contracted Stationary Gaussian Sequences*, arXiv:1312.2151 (2013), Introduction and Section 1. https://arxiv.org/abs/1312.2151.
