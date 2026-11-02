# Exact all-time Wasserstein amplification and an asymptotically maximal distortion on bridge-barbell graphs

## Finding

For every integer \(m\ge3\), take two vertex-disjoint unit-edge complete graphs on \(m\) vertices, choose one distinguished vertex in each, and join the two distinguished vertices by one additional unit edge. Denote the resulting bridge-barbell graph by \(B_m\), and denote its shortest-path metric by \(d\). Its continuous-time random walk has generator \(Qf(x)=\sum_{y\sim x}(f(y)-f(x))\) and transition semigroup \(P_t=e^{tQ}\). Define the optimal Wasserstein-one amplification

\[
\mathcal C_m(t)=\sup_{\mu\ne\nu}\frac{W_1(\mu P_t,\nu P_t)}{W_1(\mu,\nu)},\qquad t\ge0,
\]

where the supremum runs over probability laws on the vertices, and \(W_1\) uses \(d\). Set

\[
\Delta_m=\sqrt{m^2+4m-4},\quad
\lambda_{\pm}=\frac{m+2\pm\Delta_m}{2},\quad
A_m=\frac{\Delta_m+5m-6}{2\Delta_m}.
\]

Then, **for all \(t\ge0\)**,

\[
\boxed{\mathcal C_m(t)=A_m e^{-\lambda_-t}-(A_m-1)e^{-\lambda_+t}.}
\]

For every \(t>0\), the only maximizing unoriented edge is the joining bridge. Its two endpoint Dirac laws attain the global amplification. There is exactly one positive maximizing time,

\[
\boxed{t_m^*=\frac1{\Delta_m}\log\!\left(\frac{(A_m-1)\lambda_+}{A_m\lambda_-}\right),}
\]

and \(\mathcal C_m(t_m^*)>1\). As \(m\to\infty\),

\[
t_m^*=\frac{2\log m-\log3}{m}+O\!\left(\frac{\log m}{m^2}\right),\qquad
\max_{t\ge0}\mathcal C_m(t)=3-\frac8m+O\!\left(\frac{\log m}{m^2}\right).
\]

In particular, for every fixed \(t>0\), \(\mathcal C_m(t)\to3\), whereas \(\mathcal C_m(0)=1\). The limiting maximal factor \(3\) saturates the elementary diameter bound \(\mathcal C_m(t)\le\operatorname{diam}(B_m)=3\).

## Assumptions and scope

The graph is finite, simple, and connected. Every edge has length and symmetric jump rate equal to one; the walk is not normalized by vertex degree. The two cliques have the **same** size \(m\ge3\), and their connecting bridge is the unique edge between the cliques. Probability measures and \(W_1\) are defined on the entire \(2m\)-vertex set. No assertion is made for differing clique sizes, weighted edges or other Markov generators.

## Proof

**1. Reduce to edges.** For any connected graph, duality gives

\[
W_1(\mu,\nu)=\sup_{\operatorname{Lip}(f)\le1}\sum_x f(x)(\mu(x)-\nu(x)).
\]

The Lipschitz constraint is equivalent to \(|f(x)-f(y)|\le1\) along each edge. By linearly interpolating differences along paths (or, dually, decomposing zero-mass signed measures into edge molecules), the induced operator norm is therefore

\[
\mathcal C_m(t)=\max_{xy\in E(B_m)}W_1(P_t(x,\cdot),P_t(y,\cdot)).
\]

Graph symmetries leave three edge types: the bridge, a bridge-endpoint-to-other-clique-vertex edge, and an edge between two nondistinguished vertices of a clique.

**2. An exact transport norm.** Write \(a,b\) for the bridge endpoints, \(U,V\) for the nondistinguished vertices of the two cliques. For any signed \(z\) with \(\sum_xz_x=0\), define \(T=\sum_{x\in\{a\}\cup U}z_x\). Every admissible potential is independently determined by \(f(a)-f(b)\in[-1,1]\), the values \(f(u)-f(a)\), and \(f(v)-f(b)\), with each local collection (including zero) of diameter at most one. Maximizing each contribution separately yields the exact formula

\[
\boxed{\|z\|_{\rm KR}=|T|+\frac12\left(\sum_{u\in U}|z_u|+\left|\sum_{u\in U}z_u\right|\right)+\frac12\left(\sum_{v\in V}|z_v|+\left|\sum_{v\in V}z_v\right|\right).}
\]

Indeed, for real coefficients \(h_1,\ldots,h_k\), the support function of \(\{(g_i):\operatorname{diam}(\{0,g_1,\ldots,g_k\})\le1\}\) is \(\max(\sum_{h_i>0}h_i,-\sum_{h_i<0}h_i)=(\sum|h_i|+|\sum h_i|)/2\).

**3. Bridge-edge response.** By antisymmetry under exchange of the two cliques, the signed law \(z_t=P_t(a,\cdot)-P_t(b,\cdot)\) has respective values \(x(t)\) at \(a\) and \(-x(t)\) at \(b\), and \(y(t)\) at each vertex of \(U\), \(-y(t)\) at each vertex of \(V\). Directly from the generator,

\[
x'=-(m+1)x+(m-1)y,\quad y'=x-y,\qquad x(0)=1,\ y(0)=0.
\]

The positive off-diagonal entries give \(x(t)>0\) and \(y(t)>0\) for \(t>0\). Diagonalizing this system gives

\[
y(t)=\frac{e^{-\lambda_-t}-e^{-\lambda_+t}}{\Delta_m},\quad
x(t)=\frac{(1-\lambda_-)e^{-\lambda_-t}+(\lambda_+-1)e^{-\lambda_+t}}{\Delta_m}.
\]

The transport-norm formula gives \(C_{\rm bridge}=x+3(m-1)y\), which simplifies to the stated two-exponential expression.

**4. Competing edges.** The difference of two nondistinguished vertices of the same clique is an eigenvector of \(Q\) with eigenvalue \(-m\). Hence \(C_{\rm peripheral}=e^{-mt}\).

For an edge from \(a\) to \(u\in U\), introduce

\[
E=e^{-mt},\quad B=\frac{e^{-\lambda_-t}-e^{-\lambda_+t}}{\Delta_m},\quad
d=\frac{(\lambda_+-m)e^{-\lambda_-t}+(m-\lambda_-)e^{-\lambda_+t}}{\Delta_m}.
\]

Direct decomposition of its initial molecule into the reflection-symmetric, antisymmetric and peripheral-contrast invariant spaces shows that the signed evolved law has total left-clique mass \(-B\), value \(-[d+(2m-3)E]/[2(m-1)]\) at \(u\), value \(-[d-E]/[2(m-1)]\) at every other vertex of \(U\), and value \([d-E]/[2(m-1)]\) at every vertex of \(V\). For completeness, the auxiliary two-component evolution with first entry \(d\) obeys \(d'=-md+2c\), \(c'=(m-1)d-2c\), \((d(0),c(0))=(1,0)\). Positivity of this system implies \(d(t)>e^{-mt}=E\) for \(t>0\) by variation of constants. The transport-norm formula now gives

\[
C_{\rm core\text{-}peripheral}(t)=B+d.
\]

Since \(B>0\) and \(d>E\) for \(t>0\), this exceeds the peripheral-edge value. A direct subtraction yields

\[
C_{\rm bridge}(t)-C_{\rm core\text{-}peripheral}(t)
=\frac{3m-5}{\Delta_m}(e^{-\lambda_-t}-e^{-\lambda_+t})>0.
\]

Therefore the bridge alone maximizes every positive-time Wasserstein contraction/amplification ratio.

**5. Peak and asymptotics.** The parameters satisfy \(0<\lambda_-<\lambda_+\), \(A_m>1\) and \(\mathcal C_m'(0)=2m-4>0\). Solving \(\mathcal C_m'(t)=0\) gives the displayed positive \(t_m^*\). The derivative is initially positive and eventually negative; its two exponential terms cross exactly once, proving the peak is unique. Elementary expansions give

\[
\Delta_m=m+2-\frac4m+O(m^{-2}),\quad
\lambda_-=\frac2m+O(m^{-2}),\quad
\lambda_+=m+2+O(m^{-1}),\quad
A_m=3-\frac8m+O(m^{-2}).
\]

They imply the displayed time and peak expansions. For fixed positive time, the slow exponential approaches one and the fast exponential approaches zero, so the amplification approaches three. Finally, for arbitrary laws \(\mu,\nu\), \(W_1(\mu P_t,\nu P_t)\le3\operatorname{TV}(\mu P_t,\nu P_t)\le3\operatorname{TV}(\mu,\nu)\le3W_1(\mu,\nu)\). This proves the universal diameter upper bound and its asymptotic sharpness.

## Verification

The accompanying `verifier.py` constructs the graph and shortest-path distances independently by breadth-first search; builds the rate-one graph generator; evaluates matrix exponentials; solves primal optimal-transport linear programs; and compares the three edge-orbit values and their global maximum against the formulas. It also checks strict ordering, peak uniqueness by sample comparisons, and large-size asymptotics. Executing `python verifier.py` with NumPy and SciPy produces `VERIFICATION_OK 254 independent LP/heat/predicted-edge/peak/asymptotic checks`. These finite checks supplement the symbolic proof; no finite test is offered as a proof for all sizes or times.

## Relationship to prior work

Münch and Wojciechowski (arXiv:1712.00875v1, 2017-12-04) establish general heat-semigroup, transport and Ollivier-curvature equivalences; those are foundational rather than an explicit optimal all-time bridge-barbell law. Cheng, Li and Wu (arXiv:1907.11036v1, 2019-07-25) study general \(W_1\)-exponential convergence criteria on graphs, not the exact time-dependent amplification of the present graph. Banerjee et al. (arXiv:2208.03471v1, 2022-08-06) analyze one-step graph Markov contraction and transport in a different setting. This result concerns the explicit *optimal* all-time amplification with its maximizing edge, peak law, and sharp limiting factor, not a general curvature criterion or a spectral-gap estimate.

## Limitations

The classification holds only for equal-sized, unweighted cliques linked by one unit-rate, unit-distance edge, under the unnormalized continuous-time graph Laplacian. The first public dates cited are dates of motivating references, not a publication date for this theorem. An older mathematically equivalent formula under different operator-norm terminology remains a residual literature-priority risk. Mathematical verification described here is not an independent audit.

## References

1. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875v1 (2017-12-04), https://arxiv.org/abs/1712.00875.
2. L. Cheng, R. Li and L. Wu, *Ricci curvature and W1-exponential convergence of Markov processes on graphs*, arXiv:1907.11036v1 (2019-07-25), https://arxiv.org/abs/1907.11036.
3. P. Banerjee, A. Karhadkar, Y. Wang, U. Alon and G. Montúfar, *Oversquashing in GNNs through the lens of information contraction and graph expansion*, arXiv:2208.03471v1 (2022-08-06), https://arxiv.org/abs/2208.03471.
