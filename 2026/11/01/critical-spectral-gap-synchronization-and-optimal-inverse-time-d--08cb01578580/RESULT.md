# Critical spectral-gap synchronization and optimal inverse-time disagreement decay

## Finding
Let \(G\) be any finite connected undirected simple graph with \(N\ge2\) vertices and combinatorial Laplacian \(L\), algebraic connectivity \(\lambda_2>0\). Let \(\mu>0\), \(\omega\in\mathbb R\), and \(c\ge0\). For all complex initial states, including zero components and arbitrary phases, consider
\[
\dot z_i=(\mu+i\omega-|z_i|^2)z_i-c\sum_{j=1}^N L_{ij}z_j.
\]
Put \(m=N^{-1}\sum_i e^{-i\omega t}z_i\), \(S(t)=\sum_i|e^{-i\omega t}z_i-m|^2\), and \(\delta=c\lambda_2-\mu\).

**Endpoint theorem.** At the exact spectral-gap threshold \(\delta=0\), every initial condition gives a globally defined solution and
\[
 S'(t)\le-2\delta S(t)-\frac{S(t)^2}{2N}.
\]
In particular, **at the exact threshold**,
\[
 S(t)\le\frac{2NS(0)}{2N+tS(0)}.
\]
At the threshold the only rotating-frame equilibria are the zero vector and the synchronous circle \(w_1=\cdots=w_N=\sqrt\mu e^{i\phi}\). Every solution converges in the rotating frame to exactly one of these equilibria, and all initial conditions outside a Lebesgue-null subset converge to a point of the nonzero synchronous circle. Thus almost every solution approaches one common full-amplitude synchronized motion (periodic when \(\omega\ne0\), stationary when \(\omega=0\)), even without a phase-sector or positive-amplitude initial restriction. At and above the boundary, complete synchronization of the complex coordinates holds for **every** initial condition, including those converging to zero.

The inverse-time rate is optimal in order as a graph-uniform endpoint estimate. A strictly above-threshold exponential disagreement bound is a standard strong-coupling consequence of the same energy estimate; it is included only for context, not claimed as new. Below the threshold, no unconditional graph-uniform synchronization theorem can hold. On the two-vertex edge, \(\lambda_2=2\); below \(2c=\mu\) there are nonzero antisynchronous equilibria, while at \(2c=\mu\) antisynchronous trajectories satisfy
\[
S(t)=\frac{2|a_0|^2}{1+2|a_0|^2t}\quad\text{for }(z_1(0),z_2(0))=(a_0,-a_0),\ \omega=0.
\]
Consequently a universal exponential decay statement cannot hold at the equality boundary, and the inverse-time order of the upper bound is attained. The **specific contribution assessed here** is the all-initial-state quantitative endpoint estimate and its sharpness in decay order; almost-global convergence and strict strong-coupling synchronization have earlier precedents.

## Assumptions and scope
All edges are undirected, unweighted, and time-independent; all oscillator growth rates, nonlinear coefficients and frequencies are identical. The term "convergence in the rotating frame" means \(w_i(t)=e^{-i\omega t}z_i(t)\) has a limit in \(\mathbb C\). A synchronous limit with amplitude zero is included in the unconditional synchronization statement. Almost-everywhere convergence to the **nonzero** synchronized circle is with respect to \(2N\)-dimensional Lebesgue measure on \(\mathbb C^N\). The result does not cover nonidentical frequencies, directed/repulsive couplings, or phase-only reduced models.

## Proof
Set \(w_i=e^{-i\omega t}z_i\) and \(u_i=w_i-m\), so \(\sum_i u_i=0\) and \(S=\sum_i|u_i|^2\). Write \(F(v)=|v|^2v\). The identity
\[
\operatorname{Re}\{\overline{x-y}(F(x)-F(y))\}=\tfrac12(|x|^2+|y|^2)|x-y|^2+\tfrac12(|x|^2-|y|^2)^2\ge\tfrac14|x-y|^4
\]
holds for any complex \(x,y\) (since \(|x|^2+|y|^2\ge\frac12|x-y|^2\)). Differentiating the centered energy and using \(\sum_i u_i=0\),
\[
\frac12S'=\mu S-c\langle u,Lu\rangle-\sum_i\operatorname{Re}\{\bar u_i[F(w_i)-F(m)]\}.
\]
By the Laplacian Poincaré inequality \(\langle u,Lu\rangle\ge\lambda_2 S\) and Cauchy–Schwarz, \(\sum_i|u_i|^4\ge S^2/N\). This gives the claimed logistic differential inequality. Grönwall and integration of the reciprocal differential inequality yield the exponential and rational estimates, respectively (the zero case is invariant). The polynomial vector field is globally forward-complete because \(R=\sum_i|w_i|^2\) satisfies \(R'\le2\mu R-2R^2/N\), by \(\langle w,Lw\rangle\ge0\) and \(\sum_i|w_i|^4\ge R^2/N\).

The rotating-frame equation is the negative gradient (with real coordinates) of the polynomial potential
\[
V(w)=\sum_i\left(\tfrac14|w_i|^4-\tfrac\mu2|w_i|^2\right)+\tfrac c2\sum_{\{i,j\}\in E}|w_i-w_j|^2.
\]
It satisfies \(\dot V=-\sum_i|\dot w_i|^2\). Every bounded trajectory of an analytic finite-dimensional gradient flow converges to a *single* critical point, by the classical Łojasiewicz gradient convergence theorem (reference below). Because the differential inequality forces \(S\to0\), any limiting equilibrium is spatially constant. The scalar stationary equation \((\mu-|m|^2)m=0\) leaves only \(m=0\) or \(|m|=\sqrt\mu\), as claimed.

At the origin the real linearized eigenvalues are \(\mu-c\lambda_j(L)\), each with multiplicity two. The constant graph mode contributes two strictly positive eigenvalues \(\mu\), at both \(\delta>0\) and \(\delta=0\); all other eigenvalues are nonpositive. The local center-stable manifold theorem confines all sufficiently small forward orbits converging to the origin to a manifold of codimension two (or a subset thereof). The full basin of the origin lies in the countable union of time-integer preimages of that manifold; smooth finite-time flow maps are local diffeomorphisms on their domains. Hence the origin's basin has Lebesgue measure zero. The remaining trajectories converge to a point of the synchronized circle. At the circle, one angular eigenvalue is zero because of global phase invariance; all transverse eigenvalues are strictly negative: \(-2\mu\), \(-c\lambda_j\), and \(-2\mu-c\lambda_j\) for \(j\ge2\). Thus trajectories converging to the circle do so exponentially after entering its normal-hyperbolic neighborhood.

For the two-vertex graph, \((a,-a)\) is invariant and obeys \(\dot a=(\mu-2c-|a|^2)a\). For \(2c<\mu\), any \(a\) of modulus \(\sqrt{\mu-2c}\) gives an antisynchronous equilibrium. At \(2c=\mu\), \(\dot a=-|a|^2a\), solved by \(a(t)=a_0/(1+2|a_0|^2t)^{1/2}\); the formula for \(S\) follows.

## Verification
Run \(\texttt{python3 verify.py}\) in a standard Python 3 installation; it uses only the standard library. It checks the nonlinear monotonicity identity on deterministic complex samples, tests the centered differential inequality on a complete three-node graph and a path of three nodes, and numerically integrates representative trajectories with fourth-order Runge–Kutta to compare their centered energy with the theoretical bounds. It also checks the analytic two-vertex critical and subcritical solutions against direct numerical integration. These finite diagnostics are **not** substitutes for the proof of the all-graph and all-time claims.

## Relationship to prior work
Chen and Hsiao (arXiv:2601.10234, first posted 2026-01-15), especially Lemma 2.2 and Theorem 3.1, analyze the same connected-graph Stuart–Landau equation for **small** positive coupling and require a positive-amplitude barrier and sectorial initial phases. The present theorem gives a complementary **strong-coupling** all-initial-state statement, includes the exact critical boundary and a sharp inverse-time boundary example, and identifies the measure-zero amplitude-death exception. These are not implications of that source's stated hypotheses. Millán, Poyato, Reynolds and Tudisco (arXiv:2510.05243, first posted 2025-10-06) develop the homogeneous-frequency general-population problem, proving phase convergence for strictly sectorial data and studying a real-valued gradient reduction. Their Theorem 2.7 and Section 5 do not impose the present spectral-gap threshold or provide the global complex-state critical-time bound. Gallo, Tian, Lambiotte and Carletti (arXiv:2507.12322) give master-stability criteria for synchronization of matrix-weighted networks via *linearization near synchronized solutions*, not an all-initial-condition global attractor theorem. Chung and Slotine (arXiv:1004.5366, 2010) previously proved almost-global synchronization of coupled Hopf oscillators on balanced graphs for any positive coupling and gave a threshold for global exponential synchronization. Neither broad phenomenon is claimed here as new. The available abstract does not give an endpoint inverse-time bound or sharpness example; the full text could not be retrieved, leaving a specific historical priority risk about possible coverage of this endpoint rate. The algebraic contraction device is an application of classical monotonicity and spectral-gap arguments, and the convergence and center-stable manifold principles are established general theory rather than claimed innovations.

## Limitations
This is a sufficient graph-spectral threshold, **not** a necessary threshold for each specific graph; the optimality example only establishes sharpness over the class of finite connected graphs. The exponential bound need not have the optimal decay constant for a fixed graph. The almost-everywhere statement excludes the origin's stable set, which can contain nonzero antisynchronous configurations. The theorem assumes equal frequencies and identical cubic nonlinearities. The strict supercritical synchronization and almost-everywhere convergence are prior phenomena rather than newly discovered claims. The priority comparison is necessarily limited to indexed and inspected literature; no claim of independently verified novelty or independent audit is made.

## References
1. K.-W. Chen and T.-Y. Hsiao, *Global Complete Synchronization in Networks of Identical Stuart–Landau Oscillators* (later versions titled *Synchronization and Hopf Bifurcation in Stuart–Landau Networks*), arXiv:2601.10234, first publicly submitted 2026-01-15, https://arxiv.org/abs/2601.10234 .
2. A. P. Millán, D. Poyato, D. N. Reynolds, F. Tudisco, *Synchronization of coupled Stuart-Landau oscillators: How heterogeneity can facilitate synchronization*, arXiv:2510.05243, first submitted 2025-10-06, https://arxiv.org/abs/2510.05243 .
3. A. Gallo, Y. Tian, R. Lambiotte, T. Carletti, *Global Synchronization in Matrix-Weighted Networks*, arXiv:2507.12322, first submitted 2025-07-16, https://arxiv.org/abs/2507.12322 .
4. S. Łojasiewicz, *Une propriété topologique des sous-ensembles analytiques réels*, Les Équations aux Dérivées Partielles (1963); see standard expositions of the Łojasiewicz gradient convergence theorem.
5. J. Carr, *Applications of Centre Manifold Theory*, Springer, 1981 (classical center-stable manifold theorem).
6. S.-J. Chung and J.-J. Slotine, *On Synchronization of Coupled Hopf-Kuramoto Oscillators with Phase Delays*, arXiv:1004.5366, first submitted 2010-04-29, https://arxiv.org/abs/1004.5366 .
