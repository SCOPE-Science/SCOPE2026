# Geometric price thresholds for shortcut links in optimally weighted paths

## Finding

Let \(P_n\) have vertices \(0,1,\dots,n-1\). Its \(i\)-th path edge joins \(i-1\) to \(i\) and has conductance \(g_i\ge0\) for \(1\le i<n\). Allow one additional nonadjacent chord \((p,q)\), \(0\le p<q-1\le n-2\), of conductance \(z\ge0\). With edge-price ratio \(t>0\), impose
\[
\sum_{i=1}^{n-1}g_i+tz=1.
\]
Among connected weighted graphs satisfying this budget, minimize the Kirchhoff index \(K=\sum_{0\le s<v<n}R_{sv}=n\operatorname{tr}L^\dagger\).

Set \(c_i=i(n-i)\), \(S_n=\sum_{i=1}^{n-1}\sqrt{c_i}\), and
\[
\Theta_{n,p,q}=\sum_{i=p+1}^{q}\sum_{j=p+1}^{q}\frac{\min(i,j)(n-\max(i,j))}{\sqrt{i(n-i)j(n-j)}}.
\]
The optimizer is unique. Its chord conductance is zero **if and only if** \(t\ge\Theta_{n,p,q}\); in that case the unique optimum is \(g_i=\sqrt{c_i}/S_n\) and \(K=S_n^2\). If \(0<t<\Theta_{n,p,q}\), the unique optimum has \(z>0\). In particular the borderline \(t=\Theta_{n,p,q}\) still has \(z=0\). The finite threshold uses known network-allocation optimality criteria; the explicit asymptotic geometry below is the new focus.

**Macroscopic chord.** Suppose \(n\to\infty\), \(p_n/n\to a\), \(q_n/n\to b\) with \(0\le a<b\le1\). Then
\[
\frac{\Theta_{n,p_n,q_n}}{n^2}\longrightarrow F(a,b)
=\int_a^b\int_a^b
\sqrt{\frac{\min(x,y)(1-\max(x,y))}{\max(x,y)(1-\min(x,y))}}\,dx\,dy.
\]
The boundary values are defined by continuity almost everywhere. This integral has an elementary closed form: put \(u_v=\arcsin\sqrt v\), \(A(u)=u-\tfrac12\sin(2u)\), \(B(u)=u+\tfrac12\sin(2u)\), and
\[
H(u)=\tfrac12u^2+\tfrac12u\sin(2u)+\tfrac12\cos(2u)+\tfrac1{16}\cos(4u).
\]
Then
\[
F(a,b)=2\left[H(u_b)-H(u_a)-A(u_a)(B(u_b)-B(u_a))\right].
\]
In particular a complete end-to-end shortcut obeys
\[
\lim_{n\to\infty}\frac{\Theta_{n,0,n-1}}{n^2}=\frac{\pi^2}{4}-2\approx0.467401100272.
\]

**Mesoscopic endpoint transition.** Assume \(\ell_n=q_n-p_n\to\infty\) and \(\ell_n/n\to0\). If \(p_n/\ell_n\to\kappa\ge0\) and \(q_n/n\to0\), then
\[
\frac{\Theta_{n,p_n,q_n}}{\ell_n^2}\longrightarrow
\Phi(\kappa)=\int_0^1\int_0^1\sqrt{\frac{\kappa+\min(u,v)}{\kappa+\max(u,v)}}\,du\,dv
=\frac43\left[\kappa+\frac12-2\kappa^{3/2}(\sqrt{\kappa+1}-\sqrt\kappa)\right].
\]
At \(\kappa=0\) the expression is interpreted continuously. It increases strictly on \([0,\infty)\), with \(\Phi(0)=2/3\) and \(\Phi(\kappa)\to1\) as \(\kappa\to\infty\). The reflected statement holds near the right endpoint: replace the depth \(p_n\) by \(n-1-q_n\). If \(\min(p_n,n-1-q_n)/\ell_n\to\infty\), then \(\Theta_{n,p_n,q_n}/\ell_n^2\to1\). Thus a chord of fixed asymptotic length relative to its distance from the boundary has a universal, nontrivial activation-price discount: \(2/3\) at an endpoint and \(1\) in the interior.

## Assumptions and scope

All conductances are nonnegative, all networks must be connected, and all edge prices and the budget are strictly positive. The graph is the simple path plus one nonadjacent candidate edge. The Laplacian \(L\) uses conductances as edge weights; \(L^\dagger\) is its Moore–Penrose pseudoinverse. The price ratio \(t\) is the amount of budget spent per unit chord conductance. The shortest possible chord spans two path edges. The result does not assume symmetry of the conductances or of the chord position. Finite and asymptotic assertions quantify over every admissible parameter sequence satisfying the displayed hypotheses.

## Proof

**1. Path optimum.** On a tree each unordered vertex pair uses a unique path, so exchanging the order of the pair sum and the edge sum yields \(K=\sum_{i=1}^{n-1}c_i/g_i\). With \(z=0\), the Cauchy–Schwarz inequality and \(\sum g_i=1\) give
\[
K\ge\left(\sum_i\sqrt{c_i}\right)^2=S_n^2,
\]
with equality if and only if \(g_i=\sqrt{c_i}/S_n\). In particular all path conductances at the path optimum are positive.

**2. Marginal value of a chord.** Let \(b=e_p-e_q\). Increasing its conductance from zero to \(z\) changes the Laplacian by \(zbb^{\mathsf T}\). The rank-one inverse identity on the zero-sum subspace gives
\[
K(g,z)=K(g,0)-\frac{z}{1+zR_{pq}(g)}\,n\,b^{\mathsf T}(L(g)^\dagger)^2b.
\]
Equivalently, the coefficient \(n\,b^{\mathsf T}(L(g)^\dagger)^2b\) is the sum of squares of voltage differences across chord terminals induced by unit-current injections at each unordered pair \((s,v)\). On a path the latter voltage difference is \(\sum_{i\in[p+1,q]\cap[s+1,v]}g_i^{-1}\), up to an irrelevant sign. Hence
\[
-\left.\frac{\partial K}{\partial z}\right|_{z=0}
=\sum_{i=p+1}^{q}\sum_{j=p+1}^{q}\frac{\min(i,j)(n-\max(i,j))}{g_i g_j}.
\]
The coefficient counts the unordered injection pairs that traverse both edges \(i,j\). At the path optimum, \(g_i=\sqrt{c_i}/S_n\), this is \(S_n^2\Theta_{n,p,q}\).

**3. Global activation criterion and uniqueness.** On connected networks, \(K=n\operatorname{tr}[(L+\mathbf1\mathbf1^{\mathsf T}/n)^{-1}]-n\), and the inverse-trace is strictly convex as a function of a positive-definite matrix. For a simple graph, different edge conductances give different Laplacians because each edge has a unique off-diagonal position, so \(K\) is strictly convex in its vector of edge conductances. The feasible set is convex on its connected domain. At the path optimum the gradient for path edge \(i\) is \(-c_i/g_i^2=-S_n^2\), so the budget multiplier is \(S_n^2\). The one-sided chord KKT residual is therefore
\[
-S_n^2\Theta_{n,p,q}+tS_n^2=S_n^2(t-\Theta_{n,p,q}).
\]
Convexity makes this residual's nonnegativity necessary and sufficient for global optimality of the path allocation. Strict convexity makes it unique even at equality. If the residual is negative, the unique optimum cannot lie on \(z=0\), since the path allocation is then its only feasible boundary minimizer. Existence follows from compactness and the divergence of \(K\) toward disconnected limits.

**4. Macroscopic limit.** The normalized summand is the bounded kernel
\[
k(x,y)=\sqrt{\frac{\min(x,y)(1-\max(x,y))}{\max(x,y)(1-\min(x,y))}},\quad 0<x,y<1.
\]
It lies in \([0,1]\) and is continuous away from the boundary. Split the Riemann sum into an interior square and a boundary strip; ordinary Riemann convergence holds on the first, and the contribution of the second is bounded by its area. This proves convergence to \(F(a,b)\), including endpoint cases. For \(x\le y\), substitute \(x=\sin^2u\), \(y=\sin^2v\). The transformed measure is \(A'(u)B'(v)\,du\,dv\), where \(A'(u)=2\sin^2u\) and \(B'(u)=2\cos^2u\). Thus \(F=2\int_{u_a}^{u_b}A'(u)[B(u_b)-B(u)]\,du\). Integration by parts and the identity \(H'(u)=A(u)B'(u)\) give the stated closed form and the endpoint constant \(F(0,1)=\pi^2/4-2\).

**5. Boundary layer.** Write \(i=p_n+r\), \(j=p_n+s\), where \(1\le r,s\le\ell_n\), and divide the double sum by \(\ell_n^2\). If \(p_n/\ell_n\to\kappa\) and \(q_n/n\to0\), the normalized summands converge away from a measure-zero corner to \(\sqrt{[\kappa+\min(u,v)]/[\kappa+\max(u,v)]}\); they are bounded by one, so the corresponding Riemann sums converge. The double integral equals \(4\int_0^1[\sqrt{(\kappa+1)(\kappa+u)}-(\kappa+u)]\,du\), which simplifies to the displayed formula. For any \(u<v\), the integrand is strictly increasing in \(\kappa\), proving strict increase of \(\Phi\). Dominated convergence gives its large-\(\kappa\) limit one; direct evaluation at zero gives two thirds. Reflection of path indices yields the right-boundary law. When both endpoint depths dominate \(\ell_n\), each kernel summand tends uniformly to one and therefore the normalized sum tends to one.

This completes the exact finite activation classification and the new macroscopic and mesoscopic asymptotic price laws.

## Verification

The standalone `verify.py` uses rational Gauss–Jordan inversion to verify the rank-one Kirchhoff-index update for 112 exact parameter instances on paths with \(3\le n\le8\), several chords, and two rational positive shortcut conductances. It additionally checks the finite \(n=3,4\) threshold identities, the explicit macroscopic primitive, the end-to-end constant, the finite-size convergence at \(n=400,1000\), and several mesoscopic endpoint/bulk scaling comparisons. Run `python3 verify.py`; successful execution prints `VERIFY_OK 112 exact rank-one identities; continuum and boundary checks`. Exact finite checks are consistency evidence; the proof above establishes claims for all admissible sizes and sequences.

## Relationship to prior work

Ghosh, Boyd, and Saberi established the convex allocation problem, the general KKT optimality principle, and the path optimum proportional to \(\sqrt{i(n-i)}\), including its broad large-network scaling. Consequently, the finite marginal/KKT threshold **is not claimed as an independent novel optimization principle**: it is derived here from their established framework. Johnson and Chertkov studied cost-dependent electrical-network design with linear conductance penalties; their general design framework likewise does not by itself provide the explicit path-chord geometry profile in the theorem. Research on fixed-base-graph Kirchhoff-index edge insertion studies a distinct fixed-conductance or cardinality-constrained problem. The mathematical contribution assessed here is the continuous endpoint-dependent critical-price profile \(F\), the universal short-chord boundary layer \(\Phi\), and the distinction between the endpoint coefficient \(2/3\) and bulk coefficient one, not the existence of a convex formulation or of a differentiable sensitivity.

## Limitations

The theorem addresses a single candidate shortcut on a weighted path, not multiple shortcuts, directed networks, nonlinear edge costs, or the exact optimal positive chord conductance when the chord activates. The asymptotic statements concern the activation-price threshold, not convergence rates of a numerical solver. Possible equivalent specialized calculations in older optimal electrical-network or resistance-distance literature remain an originality risk. A related modern fixed-graph augmentation preprint was available for abstract-level comparison but not fully inspectable, so no claim is made that its entire contents lack the formula. The early shorter 2006 conference version of the 2008 reference has only a month-resolved first-public record in the accessed evidence; the bibliography gives the exact verified online date for the cited journal text rather than manufacturing a day in 2006. No independent scientific audit has been performed.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1), 37–66 (2008), DOI: 10.1137/050645452. Verified online publication: 2008-02-01. Earlier short version: Proceedings MTNS, Kyoto, July 2006. Primary full-text source: https://www.web.stanford.edu/~boyd/papers/eff_res.html .
2. J. K. Johnson, M. Chertkov, *A Majorization–Minimization Approach to Design of Power Transmission Networks* (2010), arXiv:1004.2285, 2010-04-13. https://arxiv.org/abs/1004.2285 .
3. M. Predari, L. Berner, R. Kooij, H. Meyerhenke, *Greedy Optimization of Resistance-based Graph Robustness with Global and Local Edge Insertions*, arXiv:2309.08271 (2023). https://arxiv.org/abs/2309.08271 .
4. R. Bhoite et al., *Budget-Constrained Graph Augmentation for Robust Network Design via Kirchhoff Index Minimization*, arXiv:2609.29790 (2026). https://arxiv.org/abs/2609.29790 .
