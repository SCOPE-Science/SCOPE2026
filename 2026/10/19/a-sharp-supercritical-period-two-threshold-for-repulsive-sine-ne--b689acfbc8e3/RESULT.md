# A sharp supercritical period-two threshold for repulsive sine networks on weighted bipartite graphs

## Finding

Let \(G=(V,E)\) be any finite, connected, undirected, bipartite graph with at least two vertices and strictly positive edge weights \(a_e\). In the co-rotating frame consider the discrete phase map on \((\mathbb R/2\pi\mathbb Z)^V\)
\[
(F_h(\theta))_i=\theta_i+h\sum_{j:\{i,j\}\in E}a_{\{i,j\}}\sin(\theta_i-\theta_j)\pmod {2\pi},\qquad h>0.
\]
Identify states differing by a common phase. Let \(L\) be the weighted graph Laplacian and let \(\lambda=\lambda_{\max}(L)\). Choose the unit, sum-zero eigenvector \(v\) for \(\lambda\), and put
\[
Q=\sum_{\{i,j\}\in E}a_{\{i,j\}}(v_i-v_j)^4>0,\qquad h_c=\frac{2}{\lambda}.
\]
The eigenspace for \(\lambda\) is one-dimensional; either choice of the sign of \(v\) is permitted.

**Sharp global period-onset theorem.** For every \(0<h\le h_c\), the edge-cosine potential decreases strictly at every non-equilibrium state. Consequently every periodic point on the common-phase quotient is fixed, and the omega-limit set of every forward orbit consists only of fixed points. The inclusion of \(h=h_c\) is part of this assertion.

For some \(\varepsilon_G>0\), every \(h\) with \(0<\mu:=h\lambda-2<\varepsilon_G\) has a locally attracting primitive period-two orbit on the quotient, centered exactly at the bipartite antiphase equilibrium \(\theta^*\). In a local sum-zero lift its two points are \(\theta^*+x_\mu\) and \(\theta^*-x_\mu\), with
\[
x_\mu=\sqrt{\frac{3\lambda\mu}{Q}}\,v+O_G(\mu^{3/2}).
\]
The distinguished one-step multiplier at either point is
\[
\rho_\mu=-1+2\mu+O_G(\mu^2),
\]
and every other quotient multiplier stays strictly between \(-1\) and \(1\) for sufficiently small \(\mu>0\). The corresponding two-step critical Floquet multiplier is \(1-4\mu+O_G(\mu^2)\). Thus \(h_c\) is the exact onset threshold of nonfixed periodic trajectories, with an attracting two-cycle immediately on the supercritical side.

## Assumptions and scope

All vertices, edges, and positive real weights are arbitrary but fixed. The graph is connected and bipartite; no regularity, tree assumption, uniform weight, or fixed size is required. The full phase update has common-phase symmetry; the theorem concerns the quotient by this circle symmetry, or equivalently a local representative in \(\mathbf 1^\perp\). The statement about strict potential descent, including its endpoint, also holds for connected positively weighted nonbipartite graphs, but the universal antiphase bifurcation statement requires bipartiteness.

Orient the edges arbitrarily and let \(B\) be the vertex-edge incidence matrix, \(A=\operatorname{diag}(a_e)\), and \(L=BAB^T\). The quotient has dimension \(|V|-1\). Bipartiteness permits a phase pattern \(\theta^*\) taking the value \(0\) on one color class and \(\pi\) on the other. Every edge is at phase opposition, making \(\theta^*\) a global potential minimum modulo common phase. Since the graph is connected, the quadratic potential at \(\theta^*\) is positive definite in the quotient directions.

The small positive range \(\varepsilon_G\) may depend on the graph and its weights; there is no claim of a uniform neighborhood over all graphs, nor any claim about all periodic points for arbitrary \(h>h_c\).

## Proof

**1. Spectral simplicity and the positive quartic.** Choose a bipartite signing \(S=\operatorname{diag}(s_i)\) with \(s_i=+1\) on one class and \(s_i=-1\) on the other. The matrix \(SLS\) is the weighted signless Laplacian: it has weighted degrees on its diagonal and positive weights on adjacent off-diagonal entries. Connectedness makes it nonnegative and irreducible. Perron–Frobenius theory therefore shows that its spectral radius is a simple positive eigenvalue. Because \(SLS\) is similar to the positive-semidefinite \(L\), this eigenvalue is \(\lambda\), the largest Laplacian eigenvalue. All other nonzero Laplacian eigenvalues are strictly between \(0\) and \(\lambda\). The \(\lambda\)-eigenvector is orthogonal to \(\mathbf 1\). Connectedness and positivity of the weights imply \(Q>0\), since \(Q=0\) would make \(v\) constant on every edge and hence globally constant.

**2. Strict descent through the endpoint.** Define the globally periodic potential
\[
\mathcal V(\theta)=\sum_{e\in E}a_e\cos((B^T\theta)_e).
\]
Its gradient is \(g=-BA\sin(B^T\theta)\), and the map is the exact gradient step \(\theta\mapsto\theta-hg\). Along a real lift of the step,
\[
\mathcal V(\theta-hg)-\mathcal V(\theta)
=-h\|g\|^2+h^2\int_0^1(1-t)g^TD^2\mathcal V(\theta-thg)g\,dt.
\]
For every phase vector \(z\), the Hessian is \(-BA\operatorname{diag}(\cos(B^Tz))B^T\); hence
\[
g^TD^2\mathcal V(z)g\le\sum_{e\in E}a_e(b_e^Tg)^2=g^TLg\le\lambda\|g\|^2.
\]
It follows that the potential strictly decreases for \(0<h<2/\lambda\) whenever \(g\ne0\). At \(h=2/\lambda\), the resulting bound is merely nonpositive, so a separate strictness argument is essential. If \(g\ne0\), then \(g\perp\mathbf1\) and connectedness gives some edge \(e\) with \(b_e^Tg\ne0\). Along the step, \((B^T(\theta-thg))_e\) changes with nonzero speed; consequently its cosine cannot equal \(-1\) for a set of \(t\) of positive measure. This makes the first Hessian inequality strict on a set of positive measure, so the integral inequality is strict. Therefore the potential decreases strictly at every nonfixed point even at \(h=h_c\). Since \(\mathcal V\) is continuous on a compact torus quotient, a periodic orbit cannot contain a strictly decreasing step. Also, its values along an arbitrary forward orbit converge, and every accumulation point must be fixed: if an accumulation point had a strictly decreasing step, continuity would contradict the convergence of successive potential values. This proves the endpoint and omega-limit assertions.

**3. An odd local map at the antiphase state.** Write \(\theta=\theta^*+x\), with \(x\in H:=\mathbf1^\perp\) sufficiently small, and use the local lift. Since each edge difference of \(\theta^*\) is an odd multiple of \(\pi\), the centered map is exactly
\[
f_h(x)=x-hBA\sin(B^Tx).
\]
It is odd: \(f_h(-x)=-f_h(x)\). Its Taylor expansion near zero is
\[
f_h(x)=(I-hL)x+\frac h6 BA(B^Tx)^{\circ3}+O_G(\|x\|^5),
\]
where componentwise cube is denoted by the superscript \(\circ3\). A symmetric primitive two-cycle is therefore a nonzero solution of \(f_h(x)=-x\).

**4. Reduction to one scalar and exact amplitude.** Put \(\mu=h\lambda-2\), let \(P\) be the orthogonal projection on the line spanned by \(v\), and decompose \(x=yv+w\) with \(w\in H\cap v^\perp\). The two-cycle equation becomes
\[
(2I-hL)(yv+w)+\frac h6 BA(B^T(yv+w))^{\circ3}+O_G(\|yv+w\|^5)=0.
\]
At \(h=h_c\), the operator \(2I-h_cL\) is strictly positive on \(H\cap v^\perp\), because every eigenvalue there is less than \(\lambda\). The analytic implicit-function theorem applied to the projected equation yields a unique small analytic, odd function \(w=w(y,\mu)\) satisfying \(w=O_G(y^3)\). Projecting the remaining equation onto \(v\) gives
\[
0=-\mu y+\frac{h_cQ}{6}y^3+O_G(|\mu|\,|y|^3+|y|^5).
\]
Oddness makes the quotient by \(y\) analytic in \(y^2\) and \(\mu\). The implicit-function theorem yields, for every sufficiently small \(\mu>0\), a positive root with
\[
y^2=\frac{6\mu}{h_cQ}+O_G(\mu^2)=\frac{3\lambda\mu}{Q}+O_G(\mu^2).
\]
Taking the positive square root and substituting \(w=O_G(y^3)\) proves the asserted expansion of \(x_\mu\). Because \(x_\mu\ne0\) and is small, the pair \(\{x_\mu,-x_\mu\}\) is a genuine two-cycle rather than a fixed point or a torus identification.

**5. Full quotient stability.** At both points of the symmetric cycle, the Jacobian is the same real symmetric matrix,
\[
Df_h(x_\mu)=Df_h(-x_\mu)
=I-hBA\operatorname{diag}(\cos(B^Tx_\mu))B^T.
\]
Its simple eigenvalue continuing the \(v\)-mode satisfies, by first-order symmetric eigenvalue perturbation,
\[
\rho_\mu=1-h\lambda+\frac h2\sum_{e\in E}a_e(b_e^Tv)^2(b_e^Tx_\mu)^2+O_G(\|x_\mu\|^4)
=-1+2\mu+O_G(\mu^2).
\]
Every other quotient eigenvalue converges to \(1-2\lambda_j/\lambda\), which lies strictly in \((-1,1)\), since \(0<\lambda_j<\lambda\). Thus every one-step eigenvalue at the cycle has modulus less than one for sufficiently small positive \(\mu\). The derivative of the return map is the square of that Jacobian, proving local attraction. At the antiphase fixed point the principal quotient multiplier is instead \(1-h\lambda=-1-\mu\), proving its loss of stability when \(\mu>0\). The critical return multiplier is \(\rho_\mu^2=1-4\mu+O_G(\mu^2)\).

Together Steps 2–5 show that the first possible parameter for nonfixed periodic orbits is exactly \(h_c\), and that an attracting primitive two-cycle exists at every sufficiently nearby parameter above it.

## Verification

The standalone `verify.py` constructs seven independent connected positively weighted bipartite graphs: a single edge, two weighted paths, a weighted star, a weighted even cycle, and two complete bipartite graphs. It computes the Laplacian and quartic, solves the symmetric two-cycle equation by a Newton method restricted to the sum-zero subspace at four supercritical parameters per graph, checks the amplitude and multiplier expansions, and numerically samples strict potential descent at the endpoint. The exact output of the reviewed program is:

`VERIFY_OK: 7 connected positive-weight bipartite graphs, 3689 checks`

These numerical experiments neither prove the all-graphs theorem nor replace the analytic endpoint argument, spectral simplicity, or implicit-function proof. NumPy is needed to replay the verifier.

## Relationship to prior work

Buescu, D'Aniello, and Oliveira (2026, arXiv:2610.10993v1), *Morse–Smale dynamics in discrete Huygens networks*, develop the same sinusoidal graph map and prove strict descent and exclusion of nontrivial periodic points when \(0<h<2/\lambda\). Their tree results show that the antiphase equilibrium loses linear stability above this threshold, but do not establish the existence, attraction, or exact amplitude of a new cycle. The present theorem closes the endpoint for sine interactions and shows that, for **every** connected positively weighted bipartite graph (including graphs with cycles), the first loss of antiphase stability coincides with an actual stable period-two birth.

Litman (2026, arXiv:2604.20446v1), *The Origin of Edge of Stability*, gives a general local variational reduction and square-root branching criterion for gradient-descent two-cycles. Its Corollary 2.5 subsumes the abstract local-branching mechanism used here; that general mechanism is **not** claimed as new. What is established specifically for these networks is the automatic simplicity of the critical eigenmode for all weighted connected bipartite graphs, its strictly signed quartic coefficient, the full transverse stability and explicit graph-dependent amplitude, and the strict global endpoint with no other nontrivial periods. Hofmann (2026, arXiv:2607.04993v1) treats gradient-descent maps and period doubling in polynomial and machine-learning models rather than the weighted sine-network threshold.

## Limitations

The bifurcating two-cycle is proved attracting **on the common-phase quotient**. The full system necessarily has a neutral common-phase direction. The local branch depends on a graph-dependent smallness bound for \(\mu\); no classification of distant attractors, further period doublings, or all stable cycles for large steps is asserted. The proof does not extend its universal conclusion to frustrated nonbipartite graphs, where the two-color antiphase minimum does not exist. The mechanism uses classical local bifurcation methods, so its priority must be assessed against any earlier equivalent sine-network specialization, including unpublished or unindexed work. Independent validation remains to be carried out.

## References

1. J. Buescu, E. D'Aniello, and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, 7 October 2026. https://arxiv.org/html/2610.10993v1
2. E. Litman, *The Origin of Edge of Stability*, arXiv:2604.20446v1, 22 April 2026. https://arxiv.org/html/2604.20446v1
3. T. Hofmann, *The Map Behind the Flow: Finite-Step Gradient Descent as a Dynamical System*, arXiv:2607.04993v1, 6 July 2026. https://arxiv.org/abs/2607.04993
