# A degree-sharp rescue threshold for obligate mutualism with self-cubic crowding

## Finding
Fix any finite connected simple undirected \(d\)-regular graph with \(n\ge2\) vertices and \(1\le d<n\), and positive \(a,b,c,k\). In the model defined below, write \(R=cd-b\). A locally asymptotically stable strictly positive equilibrium exists **if and only if** \(R>0\) and
\[
 k<k_*=\frac{4R^3}{27a^2}.
\]
It can then be chosen homogeneous: the larger positive root \(s_+\) of \(-a+Rs-ks^3=0\) is an asymptotically stable coexistence level. The smaller positive root \(s_-\) is linearly unstable. If \(R\le0\), or \(R>0\) and \(k>k_*\), every nonnegative solution converges to extinction. At \(k=k_*\), the sole nonzero equilibrium is homogeneous at \(s_*=3a/(2R)\); it is not asymptotically stable, since initial conditions strictly below it on the homogeneous line go to extinction. Every initial condition satisfying \(x_i(0)\ge s_*\) for all \(i\), with at least one strict inequality, converges to that critical equilibrium, and its mean \(m(t)=n^{-1}\sum_i x_i(t)\) obeys the **exact amplitude law**
\[
\lim_{t\to\infty}t(m(t)-s_*)=\frac1R.
\]
Writing \(A\) for graph adjacency and \(\lambda_2(A)<d\) for its second-largest eigenvalue, the deviation \(z=x-m\boldsymbol1\) satisfies
\[
 \limsup_{t\to\infty}\frac{\log\|z(t)\|}{t}\le-cs_*\bigl(d-\lambda_2(A)\bigr),
\]
when \(z(t)\) is not identically zero; for an exactly synchronous orbit, \(z=0\) and the bound is interpreted as automatic. Thus the existence threshold depends only on degree, whereas transverse relaxation registers network topology.

## Assumptions and scope
Populations evolve in the nonnegative orthant under
\[
 \dot x_i=x_i\Bigl[-a-bx_i+c\sum_{j\sim i}x_j-kx_i^3\Bigr],\qquad i=1,\ldots,n.
\]
The intrinsic rate \(-a\) is negative for every species; neighbor terms are purely mutually beneficial; \(-bx_i\) represents pairwise self-crowding; and the only higher-order addition is the one-species term \(-kx_i^3\) in the *per-capita* rate (equivalently, \(-kx_i^4\) in population growth). No mixed-species higher-order coefficients are tuned. The graph is simple, undirected, connected, and regular. Parameters are time-independent and strictly positive. The maximal-solution comparison below gives boundedness and global forward existence for every finite nonnegative initial state.

## Proof
Let \(F(s)=-a+Rs-ks^3\), with \(R=cd-b\). For the coordinate maximum \(M(t)=\max_i x_i(t)\), a maximizing vertex has \(\sum_{j\sim i}x_j\le dM\), hence its upper right Dini derivative satisfies \(D^+M\le MF(M)\). A scalar comparison with \(\dot u=uF(u)\) proves forward boundedness. If \(R\le0\), then \(F(s)<0\) for all \(s>0\). If \(R>0\), its unique positive maximum occurs at \(s_0=\sqrt{R/(3k)}\) and equals \(-a+(2R/3)\sqrt{R/(3k)}\). This is positive, zero or negative precisely when \(k<k_*\), \(k=k_*\), or \(k>k_*\). In the strict-negative cases the scalar upper solution tends to zero, so every population does too.

All homogeneous states remain homogeneous and solve \(\dot s=sF(s)\). When \(k<k_*\), \(F\) has exactly two positive simple roots \(s_-<s_+\). At the homogeneous equilibrium \(s\boldsymbol1\), the Jacobian is
\[
 J_s=s\,[cA-(b+3ks^2)I],
\]
with largest eigenvalue \(s(R-3ks^2)=sF'(s)\): this is positive at \(s_-\) and negative at \(s_+\). Undirected regularity makes the spectrum real with adjacency largest eigenvalue \(d\), proving instability and exponential asymptotic stability, respectively.

At equality \(k=k_*\), factorization gives \(F(s)=-k(s-s_*)^2(s+2s_*)\), where \(s_*=3a/(2R)\). Any nonzero equilibrium with maximum coordinate \(M>0\) must satisfy \(0\le MF(M)\), forcing \(M=s_*\). At a maximum vertex, equality forces all its neighbors to equal \(s_*\); connectedness propagates this property to every vertex, proving the only nonzero equilibrium is \(s_*\boldsymbol1\). The dynamics are cooperative on positive states because off-diagonal partial derivatives along edges equal \(cx_i>0\). A solution starting componentwise above \(s_*\boldsymbol1\), and strictly above in at least one coordinate, is strictly above it in every coordinate at any positive time by irreducible strong comparison. A synchronous scalar solution started at the initial maximum bounds it above and tends to \(s_*\); thus all coordinates approach \(s_*\). Synchronous initial conditions below \(s_*\) instead decrease to zero, proving non-stability of the critical state.

For the critical asymptotic coefficient, let \(m=n^{-1}\sum_i x_i\) and \(z=x-m\boldsymbol1\). At the critical equilibrium the Jacobian is \(J_*=cs_*(A-dI)\), which has a simple zero eigenvalue along \(\boldsymbol1\), while all orthogonal eigenvalues are at most \(-cs_*(d-\lambda_2(A))<0\). Since the synchronous subspace is invariant and the actual solution tends to \(s_*\boldsymbol1\), the mean-free variation obeys \(z'=J_*z+o(\|z\|)\) *after projection onto the mean-free subspace*. For each \(\varepsilon>0\), eventually \(\frac12\frac{d}{dt}\|z\|^2\le[-cs_*(d-\lambda_2(A))+\varepsilon]\|z\|^2\); this gives the stated spectral logarithmic bound.

At positive times the minimum is strictly above \(s_*\); comparisons with the critical scalar equation from that time give \(m-s_*\asymp t^{-1}\). Averaging the vector field around the synchronous state gives \(m'=mF(m)+O(\|z\|^2)\): the first-order deviations cancel because the graph is regular and undirected. At \(s_*\), \(F(s_*)=F'(s_*)=0\) and \(\tfrac12(sF(s))''|_{s=s_*}=-R\). Therefore \(\dot\delta=-R\delta^2+O(\delta^3)+O(e^{-\eta t})\), with \(\delta=m-s_*>0\) and \(\eta>0\). As \(\delta\asymp1/t\), the reciprocal satisfies \((1/\delta)'=R+o(1)\). Integration yields \(t\delta\to1/R\).

Finally, for \(k=k_*\) the nonzero equilibrium is not locally asymptotically stable because arbitrarily close synchronized initial conditions below it go to extinction. For \(k>k_*\), positive equilibria are absent. Combined with the stable upper branch for \(k<k_*\), these facts establish the sharp if-and-only-if criterion.

## Verification
The accompanying `VERIFY.py` (with `sympy>=1.12`) independently checks the cubic tangency and factorization, the radial critical quadratic coefficient, the comparison threshold for sample degrees, and the exact Jacobian eigenvalues on the complete four-vertex graph. These algebraic checks support the displayed identities; the global statements follow from the preceding comparison and differential-inequality proofs, not from finite numerical experiments. Reproduce with `python VERIFY.py` after installing the listed dependency.

For example, set \(a=b=c=k=1\), \(n=4\). On the complete graph (degree three), \(R=2\) and \(k_*=32/27>1\); the upper coexistence equilibrium is \(s_+=1\), with eigenvalues \(-1,-5,-5,-5\), while the lower equilibrium is \((\sqrt5-1)/2\). On the four-cycle (degree two), \(R=1\) and \(k_*=4/27<1\), so all positive solutions become extinct. On the four-vertex complete graph at \(k=32/27\), the critical equilibrium is \(s_*=3/4\), and \(t(m-3/4)\to1/2\) for the stated above-threshold initial data.

## Relationship to prior work
Çelik, Isoldi, Portakal and Zucal (2026), arXiv:2609.09286v1, Theorems 3.1 and 4.2, study sign-pattern obstacles for pairwise Lotka–Volterra coexistence and show stabilization is possible using suitably chosen general higher-order interactions. The present result specializes the scientific question but restricts the remedy to **one identical self-only quartic mortality term per species**, obtains an exact, necessary-and-sufficient degree threshold, global extinction on the other side, and the degenerate threshold's amplitude and spectral relaxation. Their general existence statement neither supplies these restrictions nor the if-and-only-if degree threshold as stated. Gibbs et al., *When can higher-order interactions produce stable coexistence?* (2024), analyze different higher-order interaction models; its principal mixed-species terms do not establish this self-only regular-graph threshold. Classical cooperative-system theory supplies comparison and monotonicity methods and can subsume abstract portions of the argument; this result is an explicit ecological specialization, not a new general comparison theorem.

## Limitations
The critical-law assertion covers componentwise-above-threshold initial conditions, not all mixed-side initial conditions. The claim does not classify possible nonhomogeneous equilibria in the bistable case. It does not apply to weighted, directed, or nonregular graphs, heterogeneous parameters, density-independent immigration, or stochastic extinction. The new result proves mathematical properties of a stylized self-crowding model; it does not establish that quartic density regulation is empirically appropriate in every ecological system. A 1986 paper by Hal L. Smith on deterministic cooperating species was identifiable but its full text was inaccessible, so broader theoretical subsumption remains a genuine originality risk; no independent audit has been performed.

## References
1. T. Ö. Çelik, V. A. Isoldi, I. Portakal and G. Zucal, *Stable Coexistence in Ecologies and Games*, arXiv:2609.09286v1, first posted 2026-09-08, https://arxiv.org/abs/2609.09286 .
2. Gibbs et al., *When can higher-order interactions produce stable coexistence?* (2024), https://doi.org/10.1111/ele.14458 .
3. H. L. Smith, *On the Asymptotic Behavior of a Class of Deterministic Models of Cooperating Species*, SIAM J. Appl. Math. 46 (1986), DOI:10.1137/0146025 (full text not inspected).
4. Y. Meng, S. Horvát, C. D. Modes and P. A. Haas, *Impossible ecologies: Interaction networks and stability of coexistence in ecological communities*, arXiv:2309.16261, https://arxiv.org/abs/2309.16261 .
