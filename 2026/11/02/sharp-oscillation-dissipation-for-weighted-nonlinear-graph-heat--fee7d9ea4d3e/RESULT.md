# Sharp oscillation dissipation for weighted nonlinear graph heat

## Finding

Let \(G=(V,E)\) be any finite connected simple undirected graph with at least two vertices. Every vertex \(x\) has mass \(m_x>0\), every edge \(xy\) has symmetric conductance \(c_{xy}=c_{yx}>0\), and \(c_{xy}=0\) when \(xy\notin E\). Fix \(1<p<\infty\). The weighted nonlinear heat flow is
\[
 m_x\dot u_x=\sum_{z\in V}c_{xz}|u_z-u_x|^{p-2}(u_z-u_x),
\]
with the flux at zero defined to be zero. Write \(S_tu\) for its unique global solution and \(\omega(u)=\max_{x\in V}u_x-\min_{y\in V}u_y\).

For positive \(a,b\), set
\[
 \Psi_p(a,b)=
 \begin{cases}
 \min\{a,b\},&1<p\le2,\\[2pt]
 \big(a^{-1/(p-2)}+b^{-1/(p-2)}\big)^{-(p-2)},&p>2.
 \end{cases}
\]
For distinct \(x,y\), let \(N(x)\) denote the set of graph neighbors of \(x\) and define
\[
 \Lambda_{xy}(p)=c_{xy}\left(\frac1{m_x}+\frac1{m_y}\right)
 +\sum_{z\in N(x)\cap N(y)}
 \Psi_p\left(\frac{c_{xz}}{m_x},\frac{c_{yz}}{m_y}\right),
 \qquad
 \lambda_p(G)=\min_{x\ne y}\Lambda_{xy}(p).
\]

**The sharp one-input oscillation law** is
\[
 \boxed{D^+\omega(S_tu)\le-\lambda_p(G)\,\omega(S_tu)^{p-1}\quad(t\ge0).}
\]
Its coefficient is optimal in the exact sense
\[
 \boxed{\sup_{\omega(u)=1}\left. D^+_t\omega(S_tu)\right|_{t=0}=-\lambda_p(G).}
\]
For every fixed graph, masses, conductances and exponent, an explicit finite initial state attains the supremum. Thus this is an evaluated optimal nonlinear dissipation coefficient, not merely a sufficient bound.

**Topology and parameter laws.** The coefficient is strictly positive precisely when the unweighted graph diameter is at most two. It is independent of \(p\) throughout \(1<p\le2\), and nonincreasing for \(p\ge2\). If \(G\) is complete, then
\[
 \lim_{p\to\infty}\lambda_p(G)=
 \min_{x\ne y}c_{xy}\left(\frac1{m_x}+\frac1{m_y}\right)>0.
\]
If \(G\) is noncomplete and has diameter two, its high-exponent decay instead satisfies
\[
 \boxed{\lim_{p\to\infty}2^{p-2}\lambda_p(G)=
 \min_{xy\notin E}\ \sum_{z\in N(x)\cap N(y)}
 \sqrt{\frac{c_{xz}c_{yz}}{m_xm_y}}>0.}
\]
The minimum on the right runs over unordered nonadjacent vertex pairs. In particular, among diameter-two graphs the coefficient remains bounded below as the exponent grows only for complete graphs.

For unit masses and conductances, put \(\alpha_p=1\) when \(1<p\le2\) and \(\alpha_p=2^{2-p}\) when \(p>2\). The formula reduces to
\[
 \lambda_p(G)=\min_{x\ne y}\left(2\,\mathbf1_{xy\in E}
 +\alpha_p|N(x)\cap N(y)|\right).
\]
For example, \(G=K_{4,4}\) has the exact two-mode transition
\[
 \lambda_p(K_{4,4})=
 \begin{cases}2,&1<p\le3,\\4\cdot2^{2-p},&p\ge3.\end{cases}
\]
The linear diameter-two criterion and the linear Dobrushin coefficient are classical antecedents; the finding is their evaluated, sharp nonlinear weighted extension and high-exponent dichotomy.

## Assumptions and scope

The graph has finitely many vertices, no loops or multiple edges, and positive symmetric conductances on its edges. Vertex masses may be arbitrary independent positive reals. There is one real-valued vertex variable per vertex, and the exponent is common to all edges. The stated optimality concerns **one solution's vertex oscillation** and its instantaneous derivative; it is not a two-input contraction claim, nor is it a bound on maximum edge differences or total edge variation.

For every initial state the system has a unique global continuously differentiable solution. Indeed the vector field is continuous and is the negative mass-metric gradient of the convex energy \(\frac1p\sum_{xy\in E}c_{xy}|u_x-u_y|^p\). Monotonicity gives uniqueness; at any maximal or minimal vertex the time derivative has the sign required to keep every coordinate between its initial minimum and maximum, giving global boundedness and continuation.

## Proof

**1. Sharp two-weight scalar minimization.** Put \(q=p-1>0\). For any \(a,b>0\),
\[
 \min_{0\le s\le1}\{a(1-s)^q+bs^q\}=\Psi_p(a,b).
\]
For \(q\le1\), the function is concave (linear at \(q=1\)), and its minimum is attained at an endpoint, giving \(\min\{a,b\}\). For \(q>1\), strict convexity gives the unique minimizer
\[
 s=\frac{a^{1/(q-1)}}{a^{1/(q-1)}+b^{1/(q-1)}},
\]
and substitution yields the displayed power-mean expression. This also proves continuity at \(p=2\).

**2. The two-extreme-vertex bound.** Fix any nonconstant state \(u\) and select arbitrary maximizer \(x\) and minimizer \(y\), so \(u_x-u_y=\omega>0\). Write \(u_z=u_y+s_z\omega\) for every \(z\), with \(0\le s_z\le1\). In the difference \(\dot u_x-\dot u_y\), the direct edge \(xy\), if present, contributes exactly
\[
 -c_{xy}\left(\frac1{m_x}+\frac1{m_y}\right)\omega^{p-1}.
\]
Every common neighbor \(z\) contributes
\[
 -\omega^{p-1}\left[\frac{c_{xz}}{m_x}(1-s_z)^{p-1}
 +\frac{c_{yz}}{m_y}s_z^{p-1}\right],
\]
which is bounded above by minus its scalar minimum \(\Psi_p\). Every neighbor of \(x\) that is not a neighbor of \(y\) contributes a nonpositive term; likewise for exclusive neighbors of \(y\). No further terms occur. Consequently,
\[
 \dot u_x-\dot u_y\le-\Lambda_{xy}(p)\omega^{p-1}
 \le-\lambda_p(G)\omega^{p-1}.
\]
For differentiable finite-dimensional paths, the upper right derivative of the oscillation is the maximum of \(\dot u_x-\dot u_y\) over active maximizing/minimizing pairs. This proves the claimed differential inequality at nonconstant states. At constant states, the flow remains constant and the inequality is an equality.

**3. Sharpness.** Choose a pair \(x,y\) attaining the minimum \(\lambda_p(G)\), and prescribe \(u_x=1\), \(u_y=0\). For each common neighbor \(z\), choose \(u_z\) to be the scalar minimizer from Step 1, with weights \(c_{xz}/m_x\), \(c_{yz}/m_y\). Put \(u_z=1\) on the other neighbors exclusive to \(x\), put \(u_z=0\) on those exclusive to \(y\), and choose any value in \([0,1]\) for all remaining vertices. Then \(\omega(u)=1\) and
\[
 \dot u_x-\dot u_y=-\lambda_p(G).
\]
The global inequality from Step 2 bounds the Dini derivative above by the same number, while this active pair bounds it below. Therefore the Dini derivative is exactly \(-\lambda_p(G)\) and no larger universal dissipation coefficient is possible. Ties among other extrema do not alter this conclusion.

**4. Integrating the sharp differential coefficient.** Let \(a=\omega(u)\). Scalar comparison gives
\[
 \omega(S_tu)\le
 \begin{cases}
 \big[\max\{0,a^{2-p}-(2-p)\lambda_p(G)t\}\big]^{1/(2-p)},&1<p<2,\\[3pt]
 a e^{-\lambda_2(G)t},&p=2,\\[3pt]
 \big[a^{2-p}+(p-2)\lambda_p(G)t\big]^{-1/(p-2)},&p>2,
 \end{cases}
\]
where the last expression is defined to be zero for \(a=0\). In particular, when \(1<p<2\) and \(\lambda_p(G)>0\), consensus occurs no later than \(a^{2-p}/((2-p)\lambda_p(G))\). The **coefficient** in the differential inequality is sharp; this does not assert that each graph's integrated time bound is attained.

**5. The diameter criterion.** For any distinct pair, \(\Lambda_{xy}(p)>0\) if and only if \(x\) and \(y\) are adjacent or have a common neighbor, because all masses and present conductances are positive. The finite minimum \(\lambda_p(G)\) is therefore positive exactly when every pair is at distance at most two. If the diameter exceeds two, a minimizing pair with neither adjacency nor common neighbors produces a state with zero initial oscillation decay, though subsequent evolution may reduce its oscillation.

**6. The exponent laws.** For \(p\le2\), \(\Psi_p(a,b)=\min(a,b)\). For \(p\ge2\) its representation as a minimum of \(a(1-s)^{p-1}+bs^{p-1}\) makes it nonincreasing in \(p\). For \(p>2\), writing \(r=p-2\), one has
\[
 \log\!\left(2^r\Psi_p(a,b)\right)
 =-r\log\!\left(\frac{a^{-1/r}+b^{-1/r}}2\right)
 \longrightarrow\frac12(\log a+\log b).
\]
Thus \(2^{p-2}\Psi_p(a,b)\to\sqrt{ab}\), whereas \(\Psi_p(a,b)\to0\). On a complete graph every pair has a strictly positive direct-edge contribution and the claimed finite limit follows. On a noncomplete graph of diameter two, the finite collection of nonadjacent-pair coefficients has the stated positive square-root limit after scaling; every adjacent-pair coefficient diverges under the same scaling. Taking the minimum over this finite collection proves the second limit.

## Verification

The included standalone script `verify_graph_oscillation.py` uses exact rational arithmetic for the full right-hand-side derivative and explicit minimizing witnesses at \(p=2,3\). It checks 490 sharpness identities, 3,920 randomly selected rational-state derivative inequalities, and the positive-coefficient/diameter equivalence on 27,475 connected labeled graph instances on at most six vertices. It also checks 1,750 inequalities for other real exponents numerically. The random generator is seeded; the script uses only the Python standard library.

Run it with `python3 verify_graph_oscillation.py`. Its finite tests are reproducibility diagnostics; the universal statements for all graph sizes, masses, conductances and real exponents follow from Steps 1–6, not from extrapolation.

## Relationship to prior work

Mugnolo's 2012 preprint develops the well-posed nonlinear discrete heat semigroup and comparison principles. Hua and Mugnolo's 2014 preprint studies time regularity and extinction for related graph flows. Gaubert and Qu's 2013 preprint studies Hopf-oscillation/Dobrushin contraction for nonlinear consensus and explicitly treats graph \(p\)-Laplacian flows in Example 6.5. Its estimates use local Jacobian contraction on restricted sets of configurations, rather than the evaluated sharp homogeneous **one-solution** oscillation-derivative coefficient above. De Pasquale, Smith, Bullo and Valcher give a general seminorm semicontraction framework and the already-known **linear** adjacency/common-neighbor topological criterion; this antecedent is not claimed novel here.

The new statement fixes a full nonlinear weighted graph equation, evaluates the exact sharp coefficient through scalar two-weight minimization, constructs equality witnesses, and gives its exponent-dependent topology and high-exponent laws. General semicontraction theorems are compatible frameworks, but their existence alone neither evaluates this coefficient nor supplies its equality witnesses. Literature coverage cannot be excluded outside the inspected sources and indexed searches.

## Limitations

The flow is real-valued, finite-dimensional, undirected, symmetric and uses one common exponent. Nothing here supplies optimal **fixed-time** oscillation envelopes for each particular graph: only the instantaneous coefficient is exactly optimal. The diameter-at-most-two requirement characterizes positivity of this particular first-derivative coefficient, **not** eventual convergence or finite-time consensus on all connected graphs. The classical linear topology criterion is prior art. Graphs of diameter greater than two may still converge to consensus, and finite-time convergence for the subquadratic exponent is not excluded. No claim is made about directed, signed, infinite, or time-dependent graphs, or about two-solution Lipschitz contraction.

## References

- Delio Mugnolo, *Parabolic theory of the discrete p-Laplace operator*, arXiv:1207.1996, first version 2012-07-09, https://arxiv.org/abs/1207.1996.
- Stéphane Gaubert and Zheng Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, arXiv:1302.5226, first version 2013-02-21, https://arxiv.org/abs/1302.5226 (especially Section 6 and Example 6.5).
- Bobo Hua and Delio Mugnolo, *Time regularity and long-time behavior of parabolic p-Laplace equations on infinite graphs*, arXiv:1410.1584, first version 2014-10-06, https://arxiv.org/abs/1410.1584.
- Giulia De Pasquale, Kevin D. Smith, Francesco Bullo and M. Elena Valcher, *Dual Seminorms, Ergodic Coefficients and Semicontraction Theory*, arXiv:2201.03103, first version 2022-01-09, https://arxiv.org/abs/2201.03103 (Sections V–VI).
