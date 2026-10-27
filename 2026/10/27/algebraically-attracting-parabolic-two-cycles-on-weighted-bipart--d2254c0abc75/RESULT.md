# Algebraically attracting parabolic two-cycles on weighted bipartite phase networks

## Finding
Let \(G=(A\sqcup B,E,w)\) be any finite connected bipartite graph with strictly positive edge weights and constant weighted degree \(d_A>0\) on \(A\), and \(d_B>0\) on \(B\). Define \(\Lambda=d_A+d_B\) and the phase map on the vertex-phase torus
\[
(F_h(\theta))_i=\theta_i+h\sum_{j\sim i}w_{ij}\sin(\theta_i-\theta_j)\pmod{2\pi}.
\]
Common phase shifts are factored out. For each \(h>2/\Lambda\), a unique \(\delta\in(0,\pi)\) satisfies \(h\Lambda\sin\delta=2\delta\). The two configurations with constant phases on each color class and phase differences \(\pi+\delta\) and \(\pi-\delta\) form an exact primitive two-cycle, where the conserved phase sum determines the two class phases uniquely in a local real lift.

The cycle is hyperbolically attracting for \(2/\Lambda<h<\pi/\Lambda\); at \(h=\pi/\Lambda\) all transverse two-step multipliers are exactly \(1\), **but the cycle remains locally asymptotically attracting**, with the sharp orbitwise rate \(\operatorname{dist}(F_h^{2k}(\theta),p_+)=\Theta(k^{-1/2})\) for every sufficiently close initial phase class other than the cycle itself. For \(h>\pi/\Lambda\), every transverse two-step multiplier exceeds \(1\) and the same constructed cycle is a hyperbolic repeller. This is a sharp trichotomy for the constructed two-color cycle, not a classification of every periodic orbit of the graph map.

More precisely, at the critical value \(h=\pi/\Lambda\), in Euclidean mean-zero phase coordinates \(u\) centered at one point of the cycle, define
\[
\Psi_3(u)=\frac13\sum_{\{a,b\}\in E,\,a\in A,\,b\in B}w_{ab}(u_a-u_b)^3,
\quad Q(u)=\frac h2\nabla\Psi_3(u),\quad W(u)=\frac12\|Q(u)\|^2.
\]
The exact two-step Taylor law is
\[
F_h^2(p_++u)-p_+=u-\nabla W(u)+O(\|u\|^4),
\]
where \(W\) is a positive-definite homogeneous quartic on the mean-zero subspace. The associated distance-square law is
\[
\|F_h^2(p_++u)-p_+\|^2=\|u\|^2-8W(u)+O(\|u\|^5).
\]
On the two-color invariant circle, if \(\varepsilon_k\) is the signed difference-coordinate error at the \(2k\)-th return, then \(k\varepsilon_k^2\to\pi^{-2}\) whenever \(\varepsilon_0\ne0\) is sufficiently small.

## Assumptions and scope
The graph is finite, undirected, connected, and bipartite. Every present edge has positive reciprocal weight \(w_{ij}=w_{ji}\). The sum of incident weights equals \(d_A\) at every vertex of \(A\) and \(d_B\) at every vertex of \(B\). These constants need not agree: stars, complete bipartite graphs, even cycles, and many weighted biregular graphs qualify. There are at least two vertices.

The Laplacian \(L\) has \(L_{ii}=\sum_j w_{ij}\), \(L_{ij}=-w_{ij}\) for edges. The physical map preserves the sum of phases in a real lift and is equivariant under common phase shifts. The quotient tangent space can be represented as \(E_0=\{u\in\mathbb R^{|A|+|B|}:\sum_i u_i=0\}\). All local estimates refer to a small lift around a chosen cycle point, so no phase-wrap ambiguity enters the asymptotic statements. Hyperbolicity and attraction refer only to the quotient by uniform phase translation.

## Proof
**1. Spectral endpoint.** Counting weighted edges in both classes gives \(|A|d_A=|B|d_B\). The Laplacian has positive eigenvalues on \(E_0\). Its largest eigenvalue is exactly \(\Lambda=d_A+d_B\): the signless Laplacian \(D+W_G\) is diagonally similar to \(L\) across a bipartite sign matrix and has a strictly positive eigenvector with entries \(d_A\) on \(A\), and \(d_B\) on \(B\), both with eigenvalue \(\Lambda\). Connectivity makes the signless Laplacian irreducible, so Perron–Frobenius identifies this eigenvalue as the spectral radius. Thus \(0<\lambda_j\le\Lambda\) for all quotient Laplacian eigenvalues.

**2. Exact two-color orbit.** Write \(n=|A|+|B|\). Fix mean-zero representatives with values \(|B|d/n\) on \(A\) and \(-|A|d/n\) on \(B\); their class-phase difference is \(d\). Under one phase update, the difference evolves as
\[
 d\longmapsto d+h\Lambda\sin d\pmod{2\pi}.
\]
The mean stays fixed, by antisymmetry of edge forces. For \(d_\pm=\pi\pm\delta\) the two values are exchanged without an integer winding exactly when \(h\Lambda\sin\delta=2\delta\). The function \(2\delta/\sin\delta\) increases strictly from \(2\) to infinity on \((0,\pi)\), because \(\sin\delta-\delta\cos\delta>0\). Hence this symmetric branch exists uniquely for every \(h>2/\Lambda\) and is primitive (its points are distinct).

**3. Exact transverse Floquet classification.** All edges at either orbit point have phase difference congruent to \(\pi\pm\delta\), so the two Jacobians are the same matrix
\[
DF_h(p_\pm)=I-h\cos\delta\,L.
\]
The quotient two-step multipliers are therefore \((1-h\cos\delta\,\lambda_j)^2\), with \(\lambda_j\) running over the positive eigenvalues of \(L\), including multiplicity. For \(0<\delta<\pi/2\),
\[
0<h\Lambda\cos\delta=2\delta\cot\delta<2.
\]
Every quotient multiplier lies strictly inside the unit circle. At \(\delta=\pi/2\), equivalently \(h=\pi/\Lambda\), all Jacobians are the identity. For \(\delta>\pi/2\), \(\cos\delta<0\), and all transverse multipliers exceed one. This proves the sharp hyperbolic regimes and locates the fully parabolic endpoint.

**4. The critical two-step normal form.** Fix the mean-zero representative \(p_+\) with edge differences from \(A\) to \(B\) equal to \(3\pi/2\), and let \(p_-=F_h(p_+)\) at \(h=\pi/\Lambda\). For every oriented edge \(a\in A,b\in B\), the sine of its difference is \(-\cos(u_a-u_b)\) near \(p_+\), and \(+\cos(u_a-u_b)\) near \(p_-\). Taylor expansion gives, in the same real mean-zero chart,
\[
F_h(p_++u)=p_-+u+Q(u)+O(\|u\|^4),\qquad
F_h(p_-+u)=p_++u-Q(u)+O(\|u\|^4).
\]
There are no cubic terms, because sine at quadrature is an even analytic function of the displacement. Substitution and the quadratic nature of \(Q\) yield
\[
F_h^2(p_++u)=p_++u-DQ(u)Q(u)+O(\|u\|^4).
\]
As \(Q=(h/2)\nabla\Psi_3\), its derivative is symmetric and \(DQ(u)Q(u)=\nabla[\|Q(u)\|^2/2]=\nabla W(u)\). This proves the asserted quartic-gradient normal form.

**5. Positive definiteness and the sharp rate.** For \(a\in A\),
\[
Q_a(u)=\frac h2\sum_{b\sim a}w_{ab}(u_a-u_b)^2\ge0.
\]
If \(Q(u)=0\), positivity of each weight forces \(u_a=u_b\) on every edge; connectivity makes \(u\) constant, so \(u=0\) in \(E_0\). Thus \(W(u)>0\) for every nonzero mean-zero \(u\). Compactness of the unit sphere in \(E_0\) gives \(c\|u\|^4\le W(u)\le C\|u\|^4\) for positive constants depending on the graph. Euler's identity for the quartic gives \(u\cdot\nabla W(u)=4W(u)\), and hence
\[
\|u_{k+1}\|^2=\|u_k\|^2-8W(u_k)+O(\|u_k\|^5).
\]
For a sufficiently small ball this decreases the squared distance by two-sided positive multiples of its square. The orbit stays in that ball and tends to zero. The derivative of the return map at zero is the identity, so the return map is locally one-to-one; a nonzero nearby orbit never lands exactly on zero. Setting \(s_k=\|u_k\|^2\), the two-sided bounds \(c_1s_k^2\le s_k-s_{k+1}\le C_1s_k^2\) imply that the positive increments of \(1/s_k\) are bounded above and below by positive constants for all sufficiently large \(k\). Thus \(s_k=\Theta(k^{-1})\), and \(\|u_k\|=\Theta(k^{-1/2})\) for every nonzero nearby initial phase class.

**6. Exact scalar leading coefficient.** On the invariant two-color manifold the difference update at \(h=\pi/\Lambda\) is \(f(d)=d+\pi\sin d\). Expanding the second return at \(d=3\pi/2+\varepsilon\) gives
\[
 f^2(3\pi/2+\varepsilon)-3\pi/2
 =\varepsilon-\frac{\pi^2}{2}\varepsilon^3+O(\varepsilon^4).
\]
Consequently \(\varepsilon_{k+1}^{-2}-\varepsilon_k^{-2}\to\pi^2\). Since the first steps are towards zero on both sides, summation gives \(k\varepsilon_k^2\to\pi^{-2}\), which independently witnesses that the exponent \(1/2\) cannot be increased.

## Verification
The standalone `verify_parabolic_cycle.py` included in the package tests four different connected positively weighted biregular bipartite graphs (a star, an unequal biclique, a nonconstant-weight four-cycle, and a six-cycle). It numerically recomputes the exact two-cycle and graph spectral formula, compares the cubic return with the gradient-quartic normal form at four scales per graph, and checks contraction and the trichotomy at five amplitudes per graph. Symbolic differentiation verifies the universal scalar cubic coefficient. See `verification_output.txt` for the exact executed output. The all-graph positivity and asymptotic rate follow from the analytic proof, not from these finite tests.

## Relationship to prior work
Buescu, D'Aniello, and Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (public October 7, 2026), develop the graph-gradient phase model and show descent for \(0<h<2/\lambda_{\max}(L)\), excluding nonfixed periodic orbits there. Buescu and Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1 (public October 14, 2026), prove almost-global fixed-twist convergence in this descent interval and give exact fixed-twist multipliers. Both are fully consistent with the cycles here, which first arise on its boundary and persist beyond it. Neither inspected article proves attraction at the fully parabolic upper two-cycle endpoint.

A previously recorded calculation for symmetric sinusoidal stars identifies the same constructed period-two branch and its identity-multiplier boundary, but does **not** determine nonlinear attraction or its convergence exponent there. That star case is not presented as a new independent construction here; the new mathematical assertion is the graph-universal positive-definite quartic return mechanism, sharp nonlinear endpoint attraction, and corresponding rate across weighted biregular bipartite graphs. Generic one-dimensional flip and parabolic-map normal forms do not by themselves supply positive definiteness in all quotient directions of an arbitrary connected weighted graph.

## Limitations
The cycle is only the particular no-winding, class-constant symmetric branch; other high-step periodic orbits may exist. The graph must be connected, positively weighted, bipartite, and weighted-biregular. The algebraic rate is local and is established after quotienting a uniform phase. At the upper endpoint the attraction is nonhyperbolic and need not be robust under arbitrary perturbations of graph weights that destroy biregularity. Only the exact scalar leading coefficient on the two-color invariant manifold is specified; the direction-dependent coefficient for arbitrary transverse approaches is not classified. Historical priority beyond the inspected literature and the available indexed comparison remains subject to independent assessment.

## References
1. J. Buescu, E. D'Aniello, H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, first posted 2026-10-07, https://arxiv.org/html/2610.10993.
2. J. Buescu, H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1, first posted 2026-10-14, https://arxiv.org/html/2610.19953.
