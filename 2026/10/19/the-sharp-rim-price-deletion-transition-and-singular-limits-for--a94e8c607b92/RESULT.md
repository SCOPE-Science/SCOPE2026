# The sharp rim-price deletion transition and singular limits for resistance-optimal wheels

## Finding

Let \(n\ge3\), \(B>0\), and \(t>0\). In the wheel \(W_{n+1}=K_1\vee C_n\), choose a nonnegative conductance on **each edge independently**. Each spoke costs one unit per unit conductance; each rim edge costs \(t\) units. Under total expenditure \(B\), minimize the **total effective resistance** \(\mathcal R=\sum_{u<v}R_{uv}\), with \(\mathcal R=+\infty\) for disconnected conductance supports.

The optimizer exists and is unique. It assigns a common conductance \(a\) to every spoke and \(b\) to every rim edge. Set \(A=B/n\), \(x=a/A\), \(y=b/A\), and \(t_c(n)=2(n+1)/n\). Its complete finite-size classification is

\[
  t\ge t_c(n)\quad\Longleftrightarrow\quad (x,y)=(1,0).
\]

For \(0<t<t_c(n)\), the optimum has \(x>0\), \(y>0\), \(x+ty=1\), and \(y\) is the unique root in \((0,1/t)\) of

\[
\frac{t}{(n+1)(1-ty)^2}
=\sum_{k=1}^{n-1}\frac{\delta_k-t}{[1+(\delta_k-t)y]^2},
\qquad \delta_k=4\sin^2(\pi k/n).
\]

At the finite-size transition the rim conductance vanishes *linearly*:

\[
 y_n(t)=\frac{n^2}{4(n-2)(n+1)}[t_c(n)-t]
     +O_n([t_c(n)-t]^2),\qquad t\uparrow t_c(n).
\]

At each fixed \(t>0\), as \(n\to\infty\), the optimal normalized spoke and rim weights converge to

\[
(x_\infty,y_\infty)=
\begin{cases}
\left(\frac{2}{4-t},\frac{2-t}{t(4-t)}\right),&0<t<2,\\
(1,0),&t\ge2.
\end{cases}
\]

The corresponding resistance has the limit

\[
\lim_{n\to\infty}\frac{B\mathcal R_n^*(t)}{n^3}
=\begin{cases}\frac12\sqrt{t(4-t)},&0<t<2,\\1,&t\ge2.\end{cases}
\]

The cheap-rim and large-network limits do **not** commute. For each fixed \(n\ge3\), as \(t\downarrow0\),

\[
 x_n(t)\to1,\qquad
 y_n(t)\sim \sqrt{\frac{(n+1)(n^2-1)}{12t}},
\]

whereas \(\lim_{t\downarrow0}\lim_{n\to\infty}x_n(t)=1/2\), while \(\lim_{n\to\infty}\lim_{t\downarrow0}x_n(t)=1\).

## Assumptions and scope

The graph is the simple undirected wheel on \(n+1\) vertices, \(n\ge3\). The center is adjacent to every rim vertex, and rim vertices form one simple cycle. Conductances are real and nonnegative, with a separate decision variable for each edge. Prices are exactly \(1\) for each spoke and \(t>0\) for each rim edge. The budget is exactly \(B>0\); allowing an upper-budget inequality gives the same optimum, because positive common scaling strictly decreases resistance. Resistances are computed for the associated undirected electrical network; disconnected supports are inadmissible (infinite objective). No discrete-time mixing or spectral-gap optimum is claimed.

## Proof

**1. Convexity, existence, and unrestricted uniqueness.** Write \(N=n+1\), \(L(g)=\sum_e g_e z_ez_e^{\mathsf T}\) for incidence vectors \(z_e\), and \(M(g)=L(g)+\mathbf1\mathbf1^{\mathsf T}/N\). For connected supports \(M(g)\) is positive definite and

\[
 \mathcal R(g)=N\operatorname{tr}L(g)^+
 =N\left(\operatorname{tr}M(g)^{-1}-1\right).
\]

For a nonzero real edge perturbation \(d\), set \(D=\sum_e d_ez_ez_e^{\mathsf T}\). The wheel has no parallel edges, so \(D\ne0\): its off-diagonal entries recover the individual \(d_e\). Along a segment of connected conductance vectors,

\[
 \frac{d^2}{ds^2}\operatorname{tr}(M+sD)^{-1}
 =2\operatorname{tr}\!\big((M+sD)^{-1}D(M+sD)^{-1}D(M+sD)^{-1}\big)>0.
\]

Indeed the trace equals \(2\operatorname{tr}[(M+sD)^{-1/2}Z^2(M+sD)^{-1/2}]\) for the nonzero symmetric \(Z=(M+sD)^{-1/2}D(M+sD)^{-1/2}\). Strict convexity follows. The feasible conductance simplex is compact, a positive star is feasible, and as connected allocations approach disconnection a positive Laplacian eigenvalue tends to zero, forcing \(\mathcal R\to\infty\). Hence a unique optimum exists. The dihedral automorphism group acts transitively on spokes and separately on rim edges, preserving both cost and objective. Uniqueness forces uniform conductances \(a\) and \(b\) in those classes, even though no symmetry was imposed on decision variables. The hub would be isolated if \(a=0\), so \(a>0\).

**2. Fourier reduction and the finite-size threshold.** On the rim-constant/hub subspace the only nonzero eigenvalue is \((n+1)a\). The \(n-1\) orthogonal rim Fourier modes have eigenvalues \(a+\delta_k b\), with \(\delta_k=4\sin^2(\pi k/n)\), \(1\le k\le n-1\). Since \(n(a+tb)=B\), write \(a=A(1-ty)\), \(b=Ay\), where \(A=B/n\) and \(0\le y<1/t\). Thus

\[
 \mathcal R=\frac{N}{A}f_{n,t}(y),\qquad
 f_{n,t}(y)=\frac1{(n+1)(1-ty)}
 +\sum_{k=1}^{n-1}\frac1{1+(\delta_k-t)y}.
\]

Every denominator is positive on this domain. Strict convexity of this scalar function follows from the second derivative of each reciprocal (or step 1), and \(f_{n,t}(y)\to\infty\) as \(y\uparrow1/t\). Its derivative is

\[
 f'_{n,t}(y)=\frac{t}{(n+1)(1-ty)^2}
 -\sum_{k=1}^{n-1}\frac{\delta_k-t}{[1+(\delta_k-t)y]^2}.
\]

Using \(\sum_{k=1}^{n-1}\delta_k=2n\),

\[
 f'_{n,t}(0)=\frac{n^2}{n+1}t-2n.
\]

Hence the strictly convex function minimizes at \(y=0\) exactly when \(t\ge2(n+1)/n\); otherwise it has one positive interior critical point, giving the displayed equation. In particular, equality in the cost threshold still has the **unique** star optimum.

For the one-sided expansion, the trigonometric identity \(\sum_{k=1}^{n-1}\delta_k^2=6n\) yields

\[
 f''_{n,t_c}(0)=2\bigg[\frac{t_c^2}{n+1}
 +\sum_{k=1}^{n-1}(\delta_k-t_c)^2\bigg]=4(n-2)>0.
\]

The implicit-function theorem applied to \(f'_{n,t}(y)=0\) at \((t_c,0)\) gives \(dy/dt=-n^2/[4(n-2)(n+1)]\), proving the linear law.

**3. Fixed-price large-network limit.** For any \(x>0\), set \(y=(1-x)/t\). Standard Riemann-sum convergence gives

\[
 \frac{f_{n,t}(y)}n\longrightarrow
 \int_0^{2\pi}\frac{d\vartheta}{2\pi[x+4y\sin^2(\vartheta/2)]}
 =\frac1{\sqrt{x(x+4y)}}.
\]

The integral identity follows by \(u=\tan(\vartheta/2)\) on the two half-arcs (or direct partial fractions). To pass minimizers through the limit, note that \(x_n\to0\) would make the normalized Fourier sum diverge: on every arc \([\varepsilon,2\pi-\varepsilon]\) its liminf dominates the integral of \(t/[4\sin^2(\vartheta/2)]\); as \(\varepsilon\downarrow0\) these lower bounds diverge. But the feasible point \(x=1,y=0\) has normalized value tending to \(1\). Thus minimizers remain away from \(x=0\) and compact uniform convergence applies. The limiting minimizer uniquely maximizes

\[
 x\left(x+\frac{4(1-x)}t\right),\qquad 0<x\le1.
\]

Elementary differentiation yields \(x_\infty=2/(4-t)\) for \(0<t<2\), and \(x_\infty=1\) for \(t\ge2\); \(y_\infty=(1-x_\infty)/t\). Substitution proves the claimed resistance limit because \(B\mathcal R/n^3=(n+1)f_{n,t}/n^2\).

**4. Singular cheap-rim limit at fixed order.** Fix \(n\). Taking the feasible trial \(y=t^{-1/4}\) as \(t\downarrow0\) shows that \(f_{n,t}^*\to1/(n+1)\). Since always \(f_{n,t}\ge1/[(n+1)x]\) with \(x\le1\), the optimal \(x_n(t)\to1\). All rim-mode terms must vanish; hence \(y_n(t)\to\infty\). At the interior optimum the critical-point equation then implies

\[
 t\,y_n(t)^2\longrightarrow
 (n+1)\sum_{k=1}^{n-1}\frac1{\delta_k}=
 \frac{(n+1)(n^2-1)}{12}.
\]

For completeness, the last trigonometric identity follows by taking the first two logarithmic derivatives at \(z=1\) of \(P(z)=(z^n-1)/(z-1)=\prod_{k=1}^{n-1}(z-e^{2\pi i k/n})\), then using \(1/\delta_k=1/(1-\zeta_k)-1/(1-\zeta_k)^2\). This proves the singular square-root law and, together with step 3, the noncommuting spoke-budget limits.

## Verification

The bundled `wheel_price_verify.py` is a standalone Python 3 program using only the standard library. It constructs finite wheel Laplacians over exact rational numbers, inverts the shifted matrices, compares the resulting trace with the independent Fourier formula, tests sharp boundary derivatives and unique scalar roots, and samples both asymptotic regimes. Executed on the files embedded in this package, it reported **187 passed checks**. Additional independent unconstrained-edge numerical minimizations on small wheels agreed with the analytical optimizer at well-conditioned test points, but are neither certificates of global optimality nor used as proof. All universal statements are established analytically above; numerical limits and finite cases are illustrations only.

## Relationship to prior work

Ghosh, Boyd, and Saberi introduced convex conductance allocation minimizing total effective resistance and in their *Minimizing Effective Resistance of a Graph* explicitly reduced the **equal-unit-price wheel** to a one-variable spectral objective (their section 5.2, equation (38)). That general framework, wheel spectrum, equality-of-symmetric-edges argument, and equal-price case are prior work, not new claims here. The present claim makes the rim conductance price an arbitrary independent positive parameter, derives the sharp all-orders deletion threshold (including its equality case), gives exact transition slope, and proves both the fixed-price thermodynamic limit and the singular cheap-rim noncommutation. None of these parameter-dependent phase and order-of-limits statements appears in the inspected equal-price wheel treatment. The general theory provides a route to their derivation but does not itself supply the stated explicit classifications.

Other work on heterogeneous-cost Kirchhoff-index network augmentation and cost-dependent resistance allocation has overlapping motivations but different or more general formulations. The claim is not that wheel resistance minimization was previously unknown; nor does an unsuccessful search prove uniqueness in the literature. The originality assessment is limited by unavailable full texts of a small number of recent broadly related preprints.

## Limitations

The graph must be a simple wheel, the budget linear, and edge prices constant within each of the two wheel edge orbits. The resistance criterion is the sum of pairwise **electrical** resistances, not maximum resistance, finite-horizon controllability cost, fastest continuous-time spectral gap, or discrete-time mixing. The uniqueness proof relies on simple-edge injectivity and undirected connected networks; it is not stated for arbitrary graph topologies. Small-order and large-order limits are distinct; the asymptotic formulas require the specified order of limits.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, Proc. 17th International Symposium on Mathematical Theory of Networks and Systems (Kyoto, 24–28 July 2006); expanded in *SIAM Review* **50** (2008), 37–66, DOI: 10.1137/050645452. Open author PDF: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf. In particular, §5.2 and Eq. (38).
2. E. Lovisari, F. Garin, S. Zampieri, *Resistance-Based Performance Analysis of the Consensus Algorithm over Geometric Graphs*, *SIAM J. Control Optim.* **51** (2013), 3918–3945, DOI: 10.1137/110857428. Related resistance/consensus motivation, not the priced-wheel optimum.
