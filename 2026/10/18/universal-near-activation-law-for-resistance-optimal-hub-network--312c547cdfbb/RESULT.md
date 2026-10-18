# Universal near-activation law for resistance-optimal hub networks

## Finding

Let \(H\) be a finite simple graph on \(N\ge4\) peripheral vertices, both vertex-transitive and edge-transitive, of degree \(1\le d\le N-1\). Its connectedness is not required. Adjoin a universal hub to form \(G=K_1\vee H\). Independently select nonnegative conductances on every hub spoke and every edge of \(H\), at prices one and \(t>0\), respectively, under the exact budget \(B>0\). Minimize the unordered-pair effective-resistance sum \(\mathcal K\). Put \(t_c=2(N+1)/N\) and let \(T(H)\) count unordered triangles of \(H\).

For \(t\ge t_c\), the unique unrestricted optimizer is the uniform star: each spoke has conductance \(B/N\), all peripheral conductances vanish, and \(\mathcal K_*(t)=N^3/B\). For \(0<t<t_c\), every peripheral edge has strictly positive optimal conductance. The unique optimizer assigns common spoke and peripheral values \(a(t)>0\) and \(b(t)>0\).

The new quantitative assertion concerns the sharp onset just below the (previously accessible from general chord-screening theory) activation threshold. With \(\delta=t_c-t\downarrow0\) and \(x(t)=b(t)/a(t)\),
\[
 x(t)=C_{N,d}\delta+D_{N,d,T(H)}\delta^2+O_{N,H}(\delta^3),
\]
where
\[
 C_{N,d}=\frac{N^2}{4(N+1)(N-d)},
\qquad
 D_{N,d,T}=-\frac{N^3\{d^2[N(7-2N)-(N+4)d]+18NT\}}{32(N+1)^2d(N-d)^3}.
\]
Moreover,
\[
 \mathcal K_*(t)=\frac{N^3}{B}-\frac{N^5d}{16B(N+1)(N-d)}\delta^2+O_{N,H,B}(\delta^3).
\]
Thus the leading conductance activation and resistance improvement depend only on the number of leaves and their common internal degree, even for nonisomorphic and disconnected peripheral graphs; the first graph-specific term of the conductance ratio depends solely on the triangle count. In particular, the optimal resistance has a second-order, rather than first-order, gain when peripheral links become affordable.

## Assumptions and scope

An edge with zero allocated conductance is permitted; a disconnected positively weighted network has infinite objective. All graphs are simple, undirected, finite; conductance prices and budget are strictly positive. Graph automorphisms act on the permitted graph and its prices; vertex- and edge-transitivity are assumed only for the peripheral graph \(H\). The theorem classifies the unrestricted optimum, not merely allocations assumed symmetric in advance. The error terms concern fixed \(N,H,B\) and \(t\uparrow t_c\) from below, not joint large-graph limits.

## Proof

**1. Strict convexity and orbit reduction.** For a connected weighted graph on \(n=N+1\) vertices write \(L=\sum_e w_e(e_u-e_v)(e_u-e_v)^\mathsf T\), \(J=\mathbf1\mathbf1^\mathsf T/n\), and
\[
 \mathcal K=n\,\operatorname{tr}(L+J)^{-1}-n.
\]
Here \(L+J\) is positive definite. For a nonzero real symmetric perturbation \(M\), the second differential of the trace-inverse equals
\[
 2\operatorname{tr}((L+J)^{-1}M(L+J)^{-1}M(L+J)^{-1})>0.
\]
The edge-weight-to-Laplacian map is injective for simple graphs (read the off-diagonal entries). Hence \(\mathcal K\) is strictly convex in edge conductances on the connected domain. The compact budget simplex contains a positive-spoke allocation, and approach to any disconnected boundary makes \(\mathcal K\) diverge, so the minimizer exists and is unique. Invariance under peripheral vertex and edge automorphisms forces its spoke weights to be a common \(a>0\) and peripheral weights to be a common \(b\ge0\).

**2. Exact spectrum and one-dimensional objective.** Let the peripheral Laplacian spectrum, counting multiplicity, be \(0=\lambda_0,\lambda_1,\ldots,\lambda_{N-1}\); disconnected \(H\) may have additional zero entries. The weighted hub-network Laplacian has eigenvalues \(0\), \((N+1)a\), and \(a+b\lambda_j\) for \(1\le j<N\). Since \(H\) is \(d\)-regular, the budget becomes \(N(a+tdb/2)=B\). With \(x=b/a\), \(q=td/2\), and \(a=B/[N(1+qx)]\),
\[
 \mathcal K(x,t)=\frac{N}{B}(1+qx)F(x),\quad
 F(x)=1+(N+1)\sum_{j=1}^{N-1}\frac1{1+\lambda_jx}.
\]
This exact expression supplies all finite-parameter values by a unique one-variable convex-design optimization; no general elementary formula for \(x(t)\) is asserted.

**3. Critical activation.** At \(b=0\) the graph is a star with \(a=B/N\) and \(\mathcal K=N^3/B\). For one spoke, the derivative of \(\mathcal K\) is \(-N/a^2\) (its tree-cut contribution is \(N/a\)); for a prospective edge between any two leaves it is \(-2(N+1)/a^2\), by the Laplacian-pseudoinverse derivative formula \(\partial\mathcal K/\partial w_e=-n\|L^+(e_u-e_v)\|^2\). Removing \(t/N\) conductance from each spoke while adding one unit to a peripheral edge therefore has first derivative \([Nt-2(N+1)]/a^2\). The KKT criterion and strict convexity show that the uniform star is the unique global minimizer exactly when \(t\ge t_c\). Below it the unique optimum must have positive peripheral weight; edge-transitivity then gives \(b>0\) on **every** peripheral edge. The elementary chord-activation criterion is given for context and is not claimed as the novel part of this theorem.

**4. Spectral moments and universal onset.** Put \(f(x,t)=(1+tdx/2)F(x)\). Regularity of \(H\) gives
\[
 \sum_{j=1}^{N-1}\lambda_j=Nd,\quad
 \sum_{j=1}^{N-1}\lambda_j^2=Nd(d+1),\quad
 \sum_{j=1}^{N-1}\lambda_j^3=Nd^3+3Nd^2-6T(H).
\]
The last identity is the trace expansion of \((dI-A_H)^3\), using \(\operatorname{tr}A_H^3=6T(H)\). At \((x,t)=(0,t_c)\), direct differentiation gives
\[
 f_x(0,t)=\frac{N^2d}{2}(t-t_c),\quad
 f_{xx}(0,t_c)=2(N+1)d(N-d)>0,
\]
\[
 -\partial_tf_{xx}(0,t_c)=(N+1)Nd^2,
 \qquad \frac12 f_{xxx}(0,t_c)=3(N+1)\{d^3+(1-2N)d^2+6T(H)\}.
\]
Analyticity and the implicit-function theorem yield a unique stationary branch \(x=C\delta+D\delta^2+O(\delta^3)\) for small \(\delta>0\). Matching coefficients of \(f_x=0\) gives
\[
 C=\frac{N^2d/2}{2(N+1)d(N-d)}=C_{N,d},
 \qquad
 D=-\frac{(N+1)Nd^2C+3(N+1)[d^3+(1-2N)d^2+6T(H)]C^2}{2(N+1)d(N-d)},
\]
which simplifies to the stated \(D_{N,d,T(H)}\). Uniqueness of the global optimum and strict positive curvature identify this stationary branch with the optimizer. Inserting \(x=C\delta+O(\delta^2)\) into \(\mathcal K=(N/B)f\) yields the asserted quadratic resistance improvement. The \(D\)-terms cancel in the quadratic calculation; the first dependence on triangles is in the next coefficient of \(x\).

## Verification

The standalone `verify.py` uses exact SymPy rational matrix inversions and symbolic differentiation. It checks 120 identities on eight leaf graphs, including an irregular path, a single optional chord, cycles, disjoint triangles, a matching, and a clique. It checks the star first variation with heterogeneous optional directions, the eigenvalue reduction, the first three relevant derivatives, and the triangle-sensitive coefficient. Run `python verify.py` with SymPy installed. Its expected terminal line is `VERIFY_OK 120 exact rational/symbolic identities on 8 graph families`. Finite computations corroborate but do not prove the universal quantifiers.

For a concrete comparison with equal \(N=6\) and \(d=2\), take peripheral graphs \(C_6\) and \(K_3\sqcup K_3\). Both have \(t_c=7/3\) and \(C_{N,d}=9/28\), yet their triangle counts are zero and two, giving different quadratic terms in the optimal conductance ratio. At \(t=2\) and \(B=1\), the latter graph has \(x=(\sqrt7-2)/6\) and exact minimum \(128+32\sqrt7\), below the star value \(216\); the former has a different interior optimum. The exact example is corroborative, not a premise of the proof.

## Relationship to prior work

Ghosh, Boyd, and Saberi introduced strict convexity, the Laplacian trace-inverse formulation, and necessary-and-sufficient conductance optimality conditions for total effective-resistance minimization. Their 2006 conference paper and expanded 2008 article explicitly analyze tree and barbell networks (and, in the expanded article, wheels). Those general results supply the optimization framework and imply the ordinary star-versus-chord screening criterion after evaluating the star gradient. The present contribution is **not** that criterion: it is the universal critical scaling, its exact resistance curvature, and the first triangle-sensitive correction for every vertex- and edge-transitive peripheral graph, including disconnected ones.

Johnson and Chertkov studied cost-aware resistive-network and power-grid design with combinatorial sparsification, but their inspected formulation develops iterative algorithms rather than this local phase-transition asymptotic for transitive hub networks. Fixed-weight windmill resistance formulas and discrete graph-augmentation models concern related quantities, not this all-size optimized near-critical expansion. No relevant database or inspected primary source was found to state the combined degree-universal, triangle-sensitive onset law. Novelty is a qualified literature comparison, not a proof of bibliographic uniqueness.

## Limitations

This analysis concerns the exact minimum of **total pairwise effective resistance**, not spectral-gap maximization or fastest-mixing stochastic kernels. It does not assert a closed formula for optimal \(x(t)\) at every subcritical price, nor classify the full positive-chord optimizer for arbitrary non-transitive \(H\). Its topology independence is only through the stated orders of a local expansion. The universal activation threshold itself is already available from general optimality/chord-screening arguments; any originality assessment should rest on the refined spectral-moment asymptotics. Some specialized literature may be incompletely indexed; independent validation has not been performed.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of MTNS 2006, Kyoto, July 24–28, 2006 (session TuP12.2), https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf.
2. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review **50** (2008), 37–66, DOI 10.1137/050645452, https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf.
3. J. K. Johnson, M. Chertkov, *A Majorization-Minimization Approach to Design of Power Transmission Networks*, arXiv:1004.2285 (first posted 13 April 2010), https://arxiv.org/abs/1004.2285.
4. M. Predari, L. Berner, R. Kooij, H. Meyerhenke, *Greedy optimization of resistance-based graph robustness with global and local edge insertions*, Social Network Analysis and Mining **13** (2023), Article 130, DOI 10.1007/s13278-023-01137-1 (different discrete augmentation model).
