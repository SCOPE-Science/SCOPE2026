# Sharp two-cycle threshold and critical decay on weighted bipartite phase networks

## Finding
Let \(G\) be any finite, connected, undirected, positively weighted bipartite graph with at least two vertices. The explicit synchronous sine-coupling map has a **sharp, graph-spectral global obstruction** to prime period two: no distinct two-cycle exists on the phase torus at or below \(h_*=2/\lambda\), where \(\lambda\) is the largest weighted graph-Laplacian eigenvalue. Immediately above this threshold, the synchronous fixed circle loses transverse stability and a locally unique, normally attracting, checkerboard-sign two-cycle is born. Its amplitude is determined explicitly by a fourth-power edge energy. At the critical step itself, synchrony remains locally attracting, with a universal inverse-time squared-distance law for all nearby points outside the local strong-stable manifold. These are three parts of one sharp transition theorem, rather than separate claims.

More precisely, choose an arbitrary oriented edge incidence matrix \(B\), positive diagonal edge-weight matrix \(W\), and let \(L=B^\top W B\). Write \(\lambda=\lambda_{\max}(L)>0\), let \(v\) be a unit \(\lambda\)-eigenvector, and put
\[
S_4=\sum_{e\in E(G)}w_e\bigl((Bv)_e\bigr)^4>0,\qquad h_*=\frac{2}{\lambda}.
\]
The vector \(v\) has strictly opposite signs on the two parts of the bipartition. For all sufficiently small \(\delta=h-h_*>0\), the two-cycle in the mean-zero phase section consists of \(\pm u_h\), with
\[
u_h=\lambda\sqrt{\frac{3\delta}{S_4}}\,v+O(\delta^{3/2}),\qquad
\|u_h\|^2=\frac{3\lambda^2}{S_4}\delta+O(\delta^2).
\]
It is transversely exponentially attracting. At \(h=h_*\), for all sufficiently close initial phase configurations not on the local codimension-one strong-stable manifold,
\[
\lim_{t\to\infty}t\left\|\theta_t-\frac{\mathbf1^\top\theta_0}{n}\mathbf1\right\|^2
=\frac{3\lambda}{2S_4}.
\]
Here \(t\) counts discrete iterations and the difference is taken using the nearby unwrapped representative; trajectories on the strong-stable manifold converge exponentially.

## Assumptions and scope
The graph has \(n\ge2\) vertices, positive symmetric edge weights, is connected and bipartite, and is otherwise arbitrary (not necessarily a tree, regular, equally weighted, or bounded degree). The phase map is
\[
F_h(\theta)=\theta-hB^\top W\sin(B\theta)\pmod{2\pi\mathbb Z^n},\qquad h>0,
\]
where \(\sin\) is applied componentwise; equivalently its \(i\)-th component is \(\theta_i-h\sum_{j\sim i}w_{ij}\sin(\theta_i-\theta_j)\). This map is a discrete-time phase model, not a continuous-time ODE. It preserves the real mean phase on every lifted orbit and commutes with uniform phase rotation. Statements about sinks are therefore transverse to the common-rotation circle, or equivalently on \(\mathbf1^\perp\) close to synchrony. For the global period-two exclusion, "two-cycle" means a pair of *distinct actual points on the full phase torus*, with no restriction to a local neighborhood. For the local limit formula, choose the natural lift close to a synchronous real vector; the iterates stay in that lift's local neighborhood.

## Proof
**1. Spectral simplicity and sign pattern.** Let \(A\) be the weighted adjacency matrix and \(D\) the diagonal weighted-degree matrix. If \(S\) is the diagonal matrix taking \(+1\) and \(-1\) on opposite color classes, then \(SLS=D+A\). This signless Laplacian is entrywise nonnegative and irreducible because \(G\) is connected. Perron--Frobenius gives a simple top eigenvalue \(\lambda\) and a strictly positive eigenvector for \(SLS\). Thus \(v\), after choosing sign, has strictly opposite signs on the two color classes and is orthogonal to \(\mathbf1\). Since \(G\) is connected, \(S_4>0\). All other positive Laplacian eigenvalues are strictly below \(\lambda\).

**2. No nontrivial period two for \(0<h\le h_*\), even on the torus.** Let \(d_i=\sum_{j\sim i}w_{ij}\). The Rayleigh quotient gives \(d_i\le\lambda\). Every lifted one-step displacement obeys \(|F_h(\theta)_i-\theta_i|\le h d_i\le2\) for \(h\le h_*\). Hence the lift of a torus two-cycle satisfies \(F_h^2(\theta)_i-\theta_i=2\pi k_i\) with absolute value at most \(4<2\pi\), so \(k_i=0\): it is an exact real two-cycle. Put \(x=\theta\), \(y=F_h(x)\), \(d=y-x\). Then \(d\perp\mathbf1\), \(y=x-hg(x)\), \(x=y-hg(y)\), where \(g(z)=B^\top W\sin(Bz)\). Subtracting yields \(g(y)-g(x)=2d/h\). Taking the scalar product with \(d\) and integrating along the line from \(x\) to \(y\),
\[
\frac2h\|d\|^2
=\sum_e w_e (Bd)_e^2\int_0^1\cos\bigl((Bx)_e+s(Bd)_e\bigr)\,ds
<\sum_e w_e(Bd)_e^2\le\lambda\|d\|^2
\]
for every \(d\ne0\). Strictness follows because connectedness forces some nonzero edge difference and the cosine cannot equal one identically over its nontrivial argument interval. Thus \(2/h<\lambda\), contradicting \(h\le2/\lambda\). The conclusion also excludes nontrivial lifted two-cycles and holds, by this argument, for *any* connected positively weighted graph; bipartiteness is needed for the next steps.

**3. Exact birth of an antipodal two-cycle.** Work on the mean-zero subspace \(H=\mathbf1^\perp\), where the synchronous point is zero. Oddness of \(F_h\) implies that a two-cycle \(\{u,-u\}\) is equivalent to \(F_h(u)=-u\), i.e.
\[
0=(2I-hL)u+\frac h6 B^\top W(Bu)^{\odot3}+O(\|u\|^5).
\]
Write \(u=av+z\) with \(z\in H\cap v^\perp\). At \(h=h_*\), the restriction of \(2I-h_*L\) to that orthogonal complement is invertible, so the analytic implicit-function theorem determines a unique odd \(z=z(a,h)=O(a^3)\) for \(h\) near \(h_*\). Projection onto \(v\) leaves
\[
0=a\left[-\lambda(h-h_*)+\frac{S_4}{3\lambda}a^2+O(a^4+|h-h_*|a^2)\right].
\]
The implicit-function theorem in \(a^2\) produces exactly one positive-amplitude branch for \(h>h_*\) close enough, and none for \(h<h_*\) close enough. The points \(u_h\) and \(-u_h\) are distinct modulo the torus lattice when \(h-h_*\) is small. The branch formula in the Finding follows. The reduction also gives the local uniqueness of the antipodal two-cycle branch; standard one-dimensional flip reduction rules out other two-cycle branches in a sufficiently small neighborhood.

**4. Transverse stability.** The lifted Jacobian is the symmetric matrix
\[
J_h(u)=I-hB^\top W\operatorname{diag}(\cos(Bu))B.
\]
Since \(J_h(-u)=J_h(u)\), the two-step derivative is \(J_h(u)^2\). Simple-eigenvalue perturbation gives its near-critical one-step eigenvalue
\[
-1+2\lambda(h-h_*)+O((h-h_*)^2),
\]
so its square is \(1-4\lambda(h-h_*)+O((h-h_*)^2)<1\). The remaining mean-zero eigenvalues converge to \(1-2\lambda_j/\lambda\in(-1,1)\), proving transverse exponential attraction for small positive \(h-h_*\). The full phase map also has its unavoidable neutral common-rotation direction. At \(h<h_*\), synchrony itself is transversely linearly attracting; for \(h>h_*\), it is unstable.

**5. Critical relaxation.** At \(h=h_*\), the synchronous point on \(H\) has one multiplier \(-1\), while every other multiplier lies strictly within the unit disk. The analytic odd center-manifold reduction has scalar coordinate \(a_t\) and normal form
\[
a_{t+1}=-a_t+\beta a_t^3+O(a_t^5),\qquad \beta=\frac{S_4}{3\lambda}>0.
\]
The coefficient is unaffected by the stable slaving terms because the first such terms have order three and \(v^\top Lz=0\). Along any nonzero sufficiently small center trajectory, the reciprocal-square increment is \(a_{t+1}^{-2}-a_t^{-2}=2\beta+O(a_t^2)\). Hence \(t a_t^2\to1/(2\beta)\). Stable transverse fibers decay exponentially toward a center trajectory; the local strong-stable manifold is precisely the exceptional codimension-one set for which the center amplitude vanishes asymptotically. Since \(\|\theta_t-\overline\theta_0\mathbf1\|^2=a_t^2(1+o(1))\), the claimed critical limit follows. This rate is not an exponential-stability claim.

**6. Explicit graph check.** For the unweighted complete bipartite graph \(K_{2,3}\), \(\lambda=5\), \(S_4=25/6\), and \(h_*=2/5\). Its attracting two-cycle satisfies \(\|u_h\|^2=18(h-2/5)+O((h-2/5)^2)\), while at criticality every generic nearby orbit obeys \(t\|\theta_t-\overline\theta_0\mathbf1\|^2\to9/5\). Its two color classes move with opposite signs and respective leading absolute phase amplitudes in ratio \(3:2\).

## Verification
The accompanying standalone program `checks/verify.py` reconstructs four nonisomorphic weighted bipartite examples and unweighted \(K_{2,3}\), checks the predicted near-critical amplitude against the exact antipodal two-cycle equation, computes the full Jacobian spectrum and transverse multipliers, and verifies convergence of the normalized critical decay constant in direct iterations. The program is a finite numerical corroboration only. Steps 1--5 give an analytical proof for every finite connected positively weighted bipartite graph, with no size bound.

## Relationship to prior work
Buescu, D'Aniello, and Oliveira (2026) analyze discrete Huygens phase-network maps, Laplacian-dependent Lyapunov/invertibility thresholds and Morse--Smale dynamics in a smaller step-size region, especially for paths and a three-leaf star. Their available abstract does not state the graph-uniform global no-two-cycle threshold, post-threshold attracting branch, or critical decay law. The complete 25-page source was not accessible at inspection time; this comparison is provisional against its uninspected details. Earlier exact calculations for an even cycle under an equivalent antiphase gauge already give special-case two-cycles, not the all-weighted-bipartite-graph theorem. Standard Laplacian and Kuramoto-network treatments supply the matrix framework rather than the claimed sharp dynamical transition. See References.

## Limitations
The result excludes prime period two **only** for \(0<h\le h_*\); it does not exclude higher periods, quasiperiodicity, or chaotic dynamics, nor does it classify remote two-cycles above \(h_*\). The creation and attraction statement is local in phase space and local in \(h-h_*\); it is not a global-basin theorem. The checkerboard sign property and simple largest eigenvalue require the stated bipartite, connected, positive-weight hypotheses. The critical decay law excludes the local strong-stable manifold. Linear algebra and finite numerical tests do not establish literature priority; independent review, particularly of full 2026 primary text and broader older work, remains unperformed.

## References
1. J. Buescu, E. D'Aniello, and H. M. Oliveira, *Morse-Smale dynamics in discrete Huygens networks* (2026), arXiv:2610.10993, publicly submitted 2026-10-07, https://arxiv.org/abs/2610.10993.
2. K. Xi, Z. Wang, A. Cheng, H. X. Lin, J. H. van Schuppen, and C. Zhang, *Synchronization of Coupled Phase Oscillators with Stochastic Disturbances and the Cycle Space of the Graph*, SIAM Journal on Applied Dynamical Systems 22 (2023), 1030--1052, https://doi.org/10.1137/22M1489502.
3. F. Bauer, F. M. Atay, and J. Jost, *Synchronization in discrete-time networks with general pairwise coupling*, Nonlinearity 22 (2009), 2333--2351, https://doi.org/10.1088/0951-7715/22/10/001.
4. P. N. McGraw and M. Menzinger, *Analysis of nonlinear synchronization dynamics of oscillator networks by Laplacian spectral methods*, Physical Review E 75 (2007), 027104, https://doi.org/10.1103/PhysRevE.75.027104.
