# A resistance threshold and graph-dependent critical rate for frustrated unicyclic phase maps

## Finding

Let \(G\) be a finite connected graph with one cycle, of odd length \(m+1\ge5\) (so \(m\ge4\) is even). Choose one cycle edge with weight \(w>0\), and let the remaining path edges have weights \(a_1,\ldots,a_m>0\). All attached trees, if present, have arbitrary positive weights. Define the path reciprocal sums
\[
A=\sum_{j=1}^m a_j^{-1},\qquad B_3=\sum_{j=1}^m a_j^{-3},\qquad w_c=A^{-1}.
\]
For the phase map \(\theta_i^+=\theta_i+h\sum_{j\sim i}a_{ij}\sin(\theta_i-\theta_j)\pmod{2\pi}\), the configuration with every edge **except** the distinguished edge antipodal (the distinguished edge is aligned) is the unique global energy minimizer modulo common phase **if and only if** \(0<w\le w_c\). For \(w>w_c\) it ceases to be even a local minimizer. Immediately above the threshold there are exactly two global energy minima, exchanged by reversing all phases, and their displacement is proportional to \(\sqrt{w-w_c}\).

At the threshold, fix an incidence matrix \(B\) of the spanning tree obtained by deleting the distinguished edge, oriented consecutively along the cycle path. Let \(D\) be the diagonal matrix of its edge weights, \(c\) be one on the \(m\) path edges and zero on the attached-tree edges, and write
\[
K=B^{\mathsf T}B,\qquad v=D^{-1}c,\qquad Q=v^{\mathsf T}K^{-1}v>0,
\qquad \ell=K^{-1}v/Q.
\]
Let \(z\) be the small spanning-tree phase differences measured from \(\pi\), and \(t_n=\ell^{\mathsf T}z_n\). Whenever \(0<h<1/\lambda_{\max}(L_{G,w_c})\), all sufficiently near initial configurations converge to the critical equilibrium. There is a codimension-one strong-stable manifold whose points converge exponentially. Every other sufficiently near nonstationary configuration has a definite eventual sign of \(t_n\), and satisfies
\[
\boxed{\lim_{n\to\infty}\frac{1}{n t_n^2}=\frac{h(A^3-B_3)}{3Q}};
\qquad z_n=t_n v+o(|t_n|).
\]
Thus a tree attachment can slow the critical relaxation without changing the critical weight. For an unadorned odd cycle with all \(m\) path weights equal to one,
\[
w_c=1/m,\qquad Q=m(m+1)(m+2)/12,\qquad
\lim_{n\to\infty}\frac{1}{nt_n^2}=\frac{4h(m-1)}{m+2}.
\]
The case \(m=4\) yields the coefficient \(2h\).

## Assumptions and scope

All graph weights are positive and reciprocal, the unique cycle has odd length at least five, and \(h\) is positive. The global-minimizer statements concern the potential and do not depend on \(h\). Local convergence and exact discrete-time relaxation use \(w=w_c\) and \(0<h<1/\lambda_{\max}(L_{G,w_c})\), where \(L_{G,w}=\sum_{e\in E(G)}a_e b_e b_e^{\mathsf T}\) is the usual positively weighted vertex Laplacian. The phase-translation symmetry is quotiented out. The branch classification for \(w>w_c\) is only for weights sufficiently close to \(w_c\), whereas instability of the antipodal spanning-tree configuration holds for every \(w>w_c\) when the step is sufficiently small. No all-initial-state convergence or global equilibrium census is asserted.

The spanning tree has \(N\) vertices and \(N-1\) edges. Its incidence matrix \(B\) has full column rank. The orientation makes the deleted edge's phase difference equal to the negative sum of the \(m\) oriented cycle-path differences. Reversing a pendant-edge orientation changes its coordinate sign but does not change \(A,B_3,Q\), or the statement. All local formulas use real lifts of phases near the indicated critical configuration.

## Proof

**1. Exact phase-coordinate potential.** Write each spanning-tree edge difference as \(\pi+z_e\). Since the remaining cycle path has even length \(m\), the distinguished-edge difference is \(-c^{\mathsf T}z\pmod{2\pi}\). On the quotient phase torus the potential, up to an irrelevant constant, is exactly
\[
E_w(z)=-\sum_{e\in T}\alpha_e\cos z_e+w\cos(c^{\mathsf T}z).
\]
The phase map becomes exactly \(z^+=z-hK\nabla E_w(z)\) modulo \(2\pi\). Thus \(z=0\) is fixed for all weights, and its Hessian is
\[
H_w=D-wcc^{\mathsf T}=D^{1/2}\bigl(I-wD^{-1/2}cc^{\mathsf T}D^{-1/2}\bigr)D^{1/2}.
\]
The rank-one factor has a single exceptional eigenvalue \(1-wA\). Hence the Hessian is positive definite for \(w<w_c\), positive semidefinite of corank one at \(w=w_c\), and has precisely one negative eigenvalue for \(w>w_c\). Its kernel at criticality is spanned by \(v=D^{-1}c\).

**2. Global, including equality.** For any real lifts \(z_1,\ldots,z_m\), telescoping the successive points \(1,e^{iz_1},e^{i(z_1+z_2)},\ldots,e^{i(z_1+\cdots+z_m)}\) on the unit circle and then applying weighted Cauchy–Schwarz gives
\[
1-\cos(c^{\mathsf T}z)\ \le\ A\sum_{j=1}^m a_j(1-\cos z_j).
\]
Consequently \(E_w(z)-E_w(0)\ge(1-wA)\sum_j a_j(1-\cos z_j)+\sum_{e\notin\text{path}}\alpha_e(1-\cos z_e)\). For \(w<w_c\), equality forces all tree-edge deviations to vanish modulo \(2\pi\). At \(w=w_c\), equality in weighted Cauchy–Schwarz would require all successive unit-circle increments to be positive real multiples of one common nonzero complex vector. Because \(m\ge2\) and all weights are positive, a nonzero common increment would produce at least three distinct collinear points on the unit circle, which is impossible. Hence equality again forces every tree-edge deviation to be zero. Conversely \(w>w_c\) makes \(H_w\) indefinite and therefore precludes a local minimum at the origin. This proves the if-and-only-if global threshold, including the degenerate boundary.

**3. The symmetry-breaking minima.** The potential is analytic and satisfies \(E_w(-z)=E_w(z)\). At \(w=w_c\), its unique global minimum on the compact quotient torus is \(0\), and all transverse Hessian eigenvalues are positive. Lyapunov–Schmidt reduction along \(v\) (with a chosen transverse coordinate complement) produces an even scalar reduced energy whose expansion, for small \(s\) and \(w-w_c\), is
\[
\mathcal E_w(s)-\mathcal E_w(0)
=\frac{A(1-wA)}2s^2+\frac{A^3-B_3}{24}s^4
+O\bigl((w-w_c)^2s^2+|w-w_c|s^4+s^6\bigr).
\]
Here \(A^3>B_3\) because the sum \(A\) contains at least two strictly positive terms. The reduced derivative divided by \(s\) has exactly one positive zero in \(s^2\) near zero when \(w>w_c\), besides the solution \(s=0\); the two nonzero states are minima exchanged by \(z\mapsto-z\). They satisfy
\[
s^2=\frac{6A(wA-1)}{A^3-B_3}+O\bigl((w-w_c)^2\bigr),\qquad
z_e^{\pm}=\pm s\,a_e^{-1}+O(s^3)
\]
for path edges, and \(z_e^{\pm}=O(s^3)\) for pendant edges. Compactness plus uniqueness of the minimum at criticality excludes any further global minima for nearby \(w>w_c\).

**4. Exact critical time asymptotics.** At \(w=w_c\), linearization of \(z^+=z-hK\nabla E_{w_c}(z)\) has one simple neutral eigenvalue along \(v\) and strictly stable eigenvalues transverse to it. Indeed, \(KH_{w_c}\) is similar to the positive-semidefinite matrix \(K^{1/2}H_{w_c}K^{1/2}\); its nonzero eigenvalues are at most \(\lambda_{\max}(L_{G,w_c})\), and the stipulated step places all noncenter multipliers strictly between zero and one. The center manifold and its strong-stable foliation are smooth. The exact odd reflection symmetry permits an odd center parametrization \(z=t v+O(t^3)\), with center coordinate \(t=\ell^{\mathsf T}z\) because \(\ell^{\mathsf T}v=1\) and \(\ell^{\mathsf T}KH_{w_c}=0\). Taylor expansion of the gradient gives
\[
\nabla E_{w_c}(tv)=\frac{t^3}{6}\bigl(A^2c-Dv^{\odot3}\bigr)+O(t^5),
\quad v^{\mathsf T}\nabla E_{w_c}(tv)=\frac{A^3-B_3}{6}t^3+O(t^5).
\]
Projecting one update by \(\ell\) therefore gives the one-dimensional center recurrence
\[
t^+=t-\frac{h(A^3-B_3)}{6Q}t^3+O(t^5).
\]
Its cubic coefficient is strictly positive. Standard invariant-foliation estimates transfer the center asymptotic to every sufficiently near orbit except those on its exponentially contracting strong-stable leaf. In particular the nonexceptional coordinate retains a definite sign for all large \(n\), tends to zero, and
\[
\frac1{t_{n+1}^2}-\frac1{t_n^2}=\frac{h(A^3-B_3)}{3Q}+O(t_n^2).
\]
Cesàro averaging proves the stated \(1/(nt_n^2)\) limit; stable transverse components contribute \(o(t_n)\). Strong-stable initial states decay exponentially. The equilibrium is locally asymptotically stable at the critical parameter, but not exponentially stable in general.

**5. What pendant trees change.** There is a centered vertex potential \(p\) satisfying \(B^{\mathsf T}p=v\) and \(\sum_i p_i=0\); this is unique. Linear algebra gives \(Q=\sum_i p_i^2\). Adding one new leaf to vertex \(r\) with any positive edge weight adds a new zero component to \(v\), so the new leaf has the same first-order center displacement as vertex \(r\). With \(N\) original vertices and \(\bar p=0\), re-centering yields exactly
\[
Q_{\mathrm{new}}-Q_{\mathrm{old}}=\frac{N}{N+1}p_r^2\ge0.
\]
The cycle sums \(A\) and \(B_3\) do not change. Thus the threshold remains identical but the physical-time cubic coefficient decreases whenever the chosen attachment vertex has nonzero center displacement. This is why weighted hanging trees matter dynamically although they do not contribute to the edge-frustration threshold.

## Verification

The embedded `verify.py` reproduces the rank-one kernel, rational values of \(A,B_3,Q\), cubic projection identities and sign of nearby Hessian eigenvalues for four graphs (odd cycles of lengths three, five and seven, with three and two pendant edges in the latter test cases). The triangle is a cross-check of published prior work, not part of the claimed new parameter range. The program also runs 3,000 deterministic sampled angle inequalities per graph, checks the exact attachment law, and iterates the critical discrete map up to 160,000 steps for three representative cases. The printed numerical values of the inverse-square rate approach the exact graph-dependent coefficient. Run `python verify.py` with Python, NumPy and SymPy. Finite tests are diagnostics and do not establish any universally quantified assertion; those rest on Steps 1–5.

## Relationship to prior work

Buescu, D'Aniello and Oliveira (arXiv:2610.10993v1, sections 2–3 and 5.5) give the potential/gradient-map structure, sufficient graph-Laplacian step bounds and the frustration constraint for odd cycles. Their inspected theorems do not specify this sharp one-edge threshold, two chiral minimizing branches or tree-dependent critical inverse-square coefficient. A previously recorded result on a discrete **triangle** with one weak edge studies the critical center relaxation and its logarithmic corrections; here the new claim is explicitly restricted to **odd cycles of length at least five** and allows arbitrary positive cycle weights and pendant trees. Its threshold depends only on the cycle's inverse edge weights while its critical coefficient depends on the entire tree via \(Q\), a distinction absent from the triangle statement. The landscape analysis of Ling, Xu and Bandeira (arXiv:1809.11083v2) treats an attractive synchronization energy and dense or random graphs rather than this frustrated sparse weighted family. Standard center-manifold theory supplies the type of algebraic decay once the cubic coefficient is computed; it does not itself supply the graph-specific coefficient or global sharp boundary. Older studies of Josephson and antiferromagnetic XY loops could potentially imply pieces of this theorem; no exhaustive bibliographic exclusion is claimed.

## Limitations

The statement treats one distinguished weak edge on a single odd cycle of length at least five, with positive reciprocal sinusoidal couplings. No claim is made about graphs with multiple cycles, directed weights, disorder in intrinsic frequencies, or other interaction laws. The near-threshold branch assertion is local in the coupling parameter; away from threshold there may be other local or global minima not classified here. The critical rate concerns only a neighborhood of the specified critical equilibrium, and exceptional strong-stable points can relax exponentially. The numerical verifier checks finitely many instances and is not an independent audit.

## References

1. J. Buescu, E. D'Aniello and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (first public 2026-10-07), https://arxiv.org/pdf/2610.10993, especially sections 2, 3 and 5.5.
2. S. Ling, R. Xu and A. S. Bandeira, *On the Landscape of Synchronization Networks: A Perspective from Nonconvex Optimization*, arXiv:1809.11083v2 (2019), https://arxiv.org/pdf/1809.11083.
3. *Critical relaxation and an exceptional exponential circle in a discrete repulsive oscillator triangle*, published-finding corpus record `2026/10/11/SCOPE-critical-relaxation-and-an-exceptional-exponential-circle-in-a-d--2e5d3c4aa08c`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-critical-relaxation-and-an-exceptional-exponential-circle-in-a-d--2e5d3c4aa08c (indexed summary only inspected).
4. D. A. Wiley, S. H. Strogatz and M. Girvan, *The size of the sync basin*, Chaos 16 (2006), 015103 (as cited in Reference 1; no full-text comparison performed).
