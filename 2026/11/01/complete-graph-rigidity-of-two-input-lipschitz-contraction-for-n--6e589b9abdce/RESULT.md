# Complete-graph rigidity of two-input Lipschitz contraction for nonlinear discrete \(p\)-heat

## Finding
Let \(G=(V,E)\) be any finite, connected, simple undirected graph with \(|V|\ge 2\). Fix arbitrary strictly positive vertex masses \(m_v\), strictly positive symmetric edge conductances \(c_{vw}\), and an exponent \(1<p<\infty\) with \(p\ne2\). Let \(S_t\) denote the nonlinear heat flow defined in the next section. Its graph-Lipschitz seminorm is \(L_G(f)=\max_{vw\in E}|f_v-f_w|\).

The following classification is exact:
\[
 L_G(S_tu-S_tv)\le L_G(u-v)\quad\text{for every }u,v\in\mathbb R^V,\ t\ge0
 \quad\Longleftrightarrow\quad G\text{ is complete}.
\]
Indeed, on every noncomplete connected graph the failure is arbitrarily strong in the normalized *instantaneous* sense:
\[
 \sup_{u\ne v}\liminf_{t\downarrow0}
 \frac{L_G(S_tu-S_tv)-L_G(u-v)}{tL_G(u-v)}=+\infty.
\]
The supremum is taken over pairs with \(L_G(u-v)>0\); since \(G\) is connected, this excludes exactly the pairs differing by a constant. This theorem concerns *differences of two nonlinear trajectories*, not the decay of \(L_G(S_tu)\) for a single trajectory. For every exponent \(p>1\), the complete-graph implication also holds at \(p=2\); no converse is asserted at that linear exponent.

## Assumptions and scope
For each real number \(s\), define \(\phi_p(s)=|s|^{p-2}s\), with \(\phi_p(0)=0\). The autonomous system is
\[
 m_v\dot u_v(t)=\sum_{w\sim v}c_{vw}\phi_p(u_w(t)-u_v(t)),\qquad v\in V.
\]
There are no restrictions on the relative masses or conductances beyond strict positivity. All edge lengths used in the *measurement* \(L_G\) are one, independently of the heat conductances. The equivalent intrinsic shortest-path formulation is \(L_G(f)=\sup_{x\ne y}|f_x-f_y|/d_G(x,y)\). All claims concern real-valued vertex data, continuous time, finite graphs, and \(1<p<\infty\).

## Proof
**1. Well-defined flow and vertex oscillation principle.** Let
\[
 E_p(u)=\frac1p\sum_{vw\in E}c_{vw}|u_v-u_w|^p.
\]
The vector field is the negative gradient of this convex energy in the weighted Euclidean space with inner product \(\langle f,g\rangle_m=\sum_v m_vf_vg_v\). It is continuous for every \(p>1\), though it need not be locally Lipschitz for \(1<p<2\). For two solutions, monotonicity of \(\phi_p\) yields
\[
 \frac12\frac{d}{dt}\sum_v m_v(u_v-v_v)^2
 =-\sum_{xy\in E}c_{xy}
 [\phi_p(u_x-u_y)-\phi_p(v_x-v_y)]
 [(u_x-v_x)-(u_y-v_y)]\le0.
\]
This proves uniqueness. Existence follows from continuity of the finite-dimensional field, and the maximum principle or energy dissipation prevents finite-time escape; hence every solution is global and continuously differentiable in time.

Put \(\delta(t)=S_tu-S_tv\). If \(\delta_i\) is maximal among all vertices, then \(\delta_w-\delta_i\le0\) for every neighbor \(w\), whence
\[
 \dot\delta_i=\frac1{m_i}\sum_{w\sim i}c_{iw}
 [\phi_p(u_w-u_i)-\phi_p(v_w-v_i)]\le0.
\]
At a minimum the reverse inequality holds. The Dini maximum principle therefore makes \(\operatorname{osc}(\delta)=\max_i\delta_i-\min_i\delta_i\) nonincreasing on every graph.

**2. Complete graphs.** If \(G\) is complete, every pair of vertices forms an edge, and \(L_G(f)=\operatorname{osc}(f)\). Step 1 immediately proves two-input Lipschitz nonexpansivity for every \(p>1\), every choice of positive parameters, and every time.

**3. An induced three-vertex path on every other graph.** If a connected graph is not complete, choose vertices \(j,k\) at graph distance at least two, take a shortest path between them, and let \(i\) be its first interior vertex and \(k\) the vertex after \(i\) (renaming the endpoint if necessary). Thus \(ij,ik\in E\) while \(jk\notin E\). Equivalently, every connected noncomplete graph contains an induced path \(j-i-k\). Define \(h_v=d_G(j,v)\). Then \(h_j=0\), \(h_i=1\), \(h_k=2\), and \(L_G(h)=1\), because graph distances change by at most one across each edge and exactly one across \(ij\).

For a background \(a\in\mathbb R^V\) and \(\varepsilon>0\), set \(U=a+\varepsilon h\), \(V=a\), and
\[
 B_{a,\varepsilon}:=
 \frac{(F(U)-F(V))_i-(F(U)-F(V))_j}{\varepsilon},
 \qquad F_v(x)=\frac1{m_v}\sum_{w\sim v}c_{vw}\phi_p(x_w-x_v).
\]
Since the edge \(ij\) is maximally stretched by \(U-V=\varepsilon h\), and both trajectories are \(C^1\) at time zero,
\[
 \liminf_{t\downarrow0}
 \frac{L_G(S_tU-S_tV)-\varepsilon}{t\varepsilon}
 \ge B_{a,\varepsilon}.
\]
Indeed, the seminorm is at least the oriented edge difference \((S_tU-S_tV)_i-(S_tU-S_tV)_j\), which equals \(\varepsilon\) at time zero.

**4. Superquadratic case.** For \(p>2\), take \(a_k=R>0\) and \(a_z=0\) at every other vertex. Since \(jk\notin E\), the only edge incident to \(i\) or \(j\) having a nonzero background difference is \(ik\). All other contributions to \(B_{a,\varepsilon}\) are \(O(\varepsilon^{p-2})\). Consequently, for each fixed \(R>0\),
\[
 \lim_{\varepsilon\downarrow0}B_{a,\varepsilon}
 =\frac{(p-1)c_{ik}}{m_i}R^{p-2}.
\]
This tends to infinity as \(R\to\infty\); choosing \(R\) and then \(\varepsilon\) gives an arbitrarily large positive instantaneous rate.

**5. Subquadratic case.** For \(1<p<2\), choose \(a_i=a_k=0\), \(a_j=1\), and choose pairwise distinct values greater than \(3\) at all remaining vertices. Because \(jk\notin E\), the only edge incident to \(i\) or \(j\) with zero background difference is \(ik\). On that edge the change in its flux towards \(i\) is \(c_{ik}\varepsilon^{p-1}/m_i\). On every other edge incident to \(i\) or \(j\), the background gradient is nonzero, so \(\phi_p\) is differentiable there and the flux variation is \(O(\varepsilon)\). Therefore
\[
 B_{a,\varepsilon}
 =\frac{c_{ik}}{m_i}\varepsilon^{p-2}+O(1)
 \longrightarrow+\infty\qquad(\varepsilon\downarrow0).
\]
Again the displayed lower bound proves unbounded normalized instantaneous expansion. The two cases establish the converse and finish the classification. \(\square\)

## Verification
The standalone file `verify_universal_pheat.py` can be run as `python verify_universal_pheat.py` using Python 3 with NumPy and SciPy. It tests 78 weighted noncomplete graph/exponent witnesses spanning paths, cycles, complete bipartite graphs, a near-clique and a wheel; it checks an exact rational weighted three-vertex witness at exponent \(3\); and it integrates 132 complete-graph solution-pair/time samples. These are finite diagnostics. The universal quantifiers, the infinite rate, and the subquadratic non-Lipschitz regime are established by the proof, not by numerical extrapolation.

## Relationship to prior work
Mugnolo's 2012 preprint, *Parabolic theory of the discrete p-Laplace operator*, develops weighted nonlinear graph-heat semigroups and proves order preservation and vertex \(\ell^\infty\) nonexpansivity (Proposition 3.9). This gives the oscillation principle above but does not imply edge-Lipschitz contraction on a noncomplete graph, because \(L_G\) can be strictly smaller than vertex oscillation. The complete-graph implication is consequently a direct consequence of that known comparison framework. The new part of the result is the **converse on every noncomplete finite connected graph, with arbitrary positive masses and conductances, and the unbounded instantaneous obstruction** obtained from an induced three-vertex path. Hua and Mugnolo's 2014 continuation studies time regularity and long-time behavior, rather than a graph-topology characterization of two-input edge-Lipschitz stability. Linear heat-flow gradient estimates and graph-curvature characterizations concern \(p=2\) and therefore do not settle the nonlinear assertion.

## Limitations
No assertion is made about one-input decay \(L_G(S_tu)\) on arbitrary graphs, about the linear exponent \(p=2\) on noncomplete graphs, about continuous metric graphs, infinite graphs, graph-directed flow, a weighted *metric* Lipschitz seminorm, or any fixed-positive-time uniform amplification. The infinite supremum is exclusively an instantaneous normalized rate. The numerical diagnostics are not a formal proof and independent scientific assessment has not been conducted.

## References
1. D. Mugnolo, *Parabolic theory of the discrete p-Laplace operator*, arXiv:1207.1996, first posted 2012-07-09, https://arxiv.org/html/1207.1996v3, especially Proposition 3.9 and Section 3.
2. B. Hua and D. Mugnolo, *Time regularity and long-time behavior of parabolic p-Laplace equations on infinite graphs*, arXiv:1410.1584, first posted 2014-10-06, https://arxiv.org/html/1410.1584v1.
3. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875, first posted 2017-12-04, https://arxiv.org/abs/1712.00875 (linear comparison context only).
