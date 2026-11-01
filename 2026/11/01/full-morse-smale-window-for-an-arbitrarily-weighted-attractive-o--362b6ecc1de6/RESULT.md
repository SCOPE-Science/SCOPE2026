# Full Morse–Smale window for an arbitrarily weighted attractive oscillator triangle

## Finding

Consider three identical discrete-time Kuramoto/Huygens phase oscillators, with positive symmetric weights \(a_{01}=a_{02}=1\) and \(a_{12}=w>0\). Let \(\Lambda(w)=\max\{3,1+2w\}\). Modulo common rotation, the following hold for every \(w>0\) other than \(w=1/2\):

**(i)** For every \(0<h<1/\Lambda(w)\), the explicit-Euler torus map is a **Morse–Smale diffeomorphism**, without saddle-to-saddle heteroclinic orbits. Its nonwandering set consists solely of its hyperbolic fixed points; synchrony is the unique attracting fixed point. This window is maximal among positive steps for which the map is a diffeomorphism.

**(ii)** The map has four fixed phase classes for \(0<w<1/2\) and six for \(w>1/2\). Its precise fixed-point classification is as in the assumptions below, agreeing with the continuous-time equilibrium calculation of Zhao–Zhou (2024), which is not claimed as a new census.

**(iii)** For the larger step interval \(0<h<2/\Lambda(w)\), including the generally noninvertible regime, every orbit converges to a fixed phase class, and **Haar-almost every orbit converges to synchrony**. The number \(2/\Lambda(w)\) is the exact upper threshold for strict Schur stability of synchrony; no general convergence claim is made at equality or above.

The substantive addition to prior equilibrium and general gradient-descent results is the **global Morse–Smale and transverse-heteroclinic classification for all positive closing-edge strengths**, not merely a sufficiently weak closing edge.

## Assumptions and scope

Work on the quotient \(\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2\) in coordinates \(x=\theta_1-\theta_0\), \(y=\theta_2-\theta_0\). The original update is
\[
\theta_i^+=\theta_i+h\sum_{j\ne i}a_{ij}\sin(\theta_j-\theta_i)\pmod{2\pi},\qquad h>0,
\]
with \(a_{01}=a_{02}=1\), \(a_{12}=w>0\). Define
\[
V_w(x,y)=-\cos x-\cos y-w\cos(x-y),\qquad M=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
The quotient map is \(F_{w,h}=\mathrm{id}-hM\nabla V_w\pmod{2\pi}\), namely
\[
F_{w,h}(x,y)=\bigl(x-h[2\sin x+\sin y+w\sin(x-y)],\ y-h[\sin x+2\sin y-w\sin(x-y)]\bigr)\pmod{2\pi}.
\]
Its fixed points, in the stated small-step ranges (and in fact whenever the descent bound holds), are precisely:

* \((0,0)\), a sink;
* \((\pi,0)\) and \((0,\pi)\), saddles;
* \((\pi,\pi)\), a source when \(0<w<1/2\), a saddle when \(w>1/2\);
* and, only when \(w>1/2\), \((t,-t)\) and \((-t,t)\), sources, with \(t=\arccos(-1/(2w))\).

At \(w=1/2\), \((\pi,\pi)\) is nonhyperbolic, and the Morse–Smale assertion intentionally excludes that weight. All positions and angles are interpreted modulo \(2\pi\).

## Proof

**1. Gradient, Lipschitz bound and fixed points.** The symmetric positive-definite matrix \(M\) has eigenvalues \(1,3\). The full three-oscillator potential \(U=-\sum_{i<j}a_{ij}\cos(\theta_i-\theta_j)\) has Hessian quadratic form \(\sum_{i<j}a_{ij}\cos(\theta_i-\theta_j)(v_i-v_j)^2\). Thus its Hessian operator norm is at most the largest eigenvalue \(\Lambda=\max\{3,1+2w\}\) of the positive weighted graph Laplacian. Orthogonal removal of the common rotation preserves this bound. The quotient gradient metric gives the displayed map. The stationarity equations yield \(\sin x+\sin y=0\), so either \(y=-x\) or \(y=x+\pi\) modulo \(2\pi\). In the first case \(\sin x(1+2w\cos x)=0\); in the second case \(\sin x=0\). This exhausts the listed critical points. For \(0<h<2/\Lambda\), strict descent below shows a fixed point must be critical; conversely any critical point is fixed.

**2. Fixed-point indices.** The Hessian of \(V_w\) is
\[
H=\begin{pmatrix}\cos x+w\cos(x-y)&-w\cos(x-y)\\-w\cos(x-y)&\cos y+w\cos(x-y)\end{pmatrix}.
\]
At synchrony \(MH\) has eigenvalues \(3\) and \(1+2w\). At \((\pi,0)\) and \((0,\pi)\), \(\det H=-1\). At \((\pi,\pi)\), the Hessian eigenvalues along vectors \((1,1)\) and \((1,-1)\) are respectively \(-1\) and \(2w-1\). At the two nonbinary points, these eigenvalues are \(-1/(2w)\) and \((1-4w^2)/(2w)\), both negative when \(w>1/2\). Since \(M\) is positive definite, \(MH\) has the same inertia as \(H\). Also \(\mathrm DF=I-hMH\), and \(|\lambda(MH)|\le\Lambda\). For \(0<h<1/\Lambda\), all critical points are hyperbolic with the claimed indices, and synchrony is the unique sink.

**3. Global diffeomorphism and descent.** Lift the dynamics to full phase space \(\mathbb R^3\). Since \(\mathrm{Hess}\,U\preceq\Lambda I\), the Jacobian of \(\mathrm{id}-h\nabla U\) is positive definite whenever \(0<h<1/\Lambda\). The lift is strongly monotone and hence injective. Its periodic displacement is bounded; it is proper and surjective, hence a global diffeomorphism, and descends to a diffeomorphism on the rotational quotient. The standard gradient descent inequality gives
\[
U(\theta^+)-U(\theta)\le-h(1-h\Lambda/2)\|\nabla U(\theta)\|_2^2,
\]
strictly negative off critical points for every \(0<h<2/\Lambda\). As \(U\) is bounded and the critical classes are finite, \(\|\nabla U(\theta_n)\|\to0\), successive quotient steps tend to zero, and the connectedness of the accumulation set forces each orbit to converge to one fixed point. Strict descent excludes other recurrent or nonwandering points: at a noncritical point one can choose a neighborhood whose image after any positive number of iterates lies below its initial potential level.

**4. Exact invariant-circle obstruction to saddle connections.** Two essential circles are invariant:
\[
\mathcal D=\{x=y\pmod{2\pi}\},\qquad \mathcal C=\{x+y=0\pmod{2\pi}\}.
\]
The former follows from \(F_1-F_2=0\) whenever \(x=y\), and the latter from \(F_1+F_2=0\) whenever \(y=-x\). As \(F\) is a torus diffeomorphism isotopic to the identity, its restriction to either invariant circle is a circle diffeomorphism onto that same circle, so both circles are also backward invariant. When \(w>1/2\), the unique third saddle \((\pi,\pi)\) has unstable eigendirection tangent to \(\mathcal D\) and stable eigendirection tangent to \(\mathcal C\), because the weighted metric \(M\) shares their eigendirections. Its entire global unstable manifold lies in \(\mathcal D\) and its entire global stable manifold in \(\mathcal C\). Neither of the other saddles \((\pi,0)\) or \((0,\pi)\) belongs to either invariant circle, hence neither can connect to the third saddle in either time direction. The two remaining saddles both have equal potential value \(V_w=w\), so strict descent precludes a heteroclinic connection between them. When \(w<1/2\), there are only those last two saddles, and the same potential argument excludes any saddle connection. Thus no saddle-to-saddle heteroclinics exist for any \(w\ne1/2\). All remaining possible stable/unstable manifold intersections involve a source or sink, and are automatically transverse in a two-dimensional diffeomorphism. The finite hyperbolic nonwandering set and strong transversality establish the Morse–Smale assertion.

**5. Sharp diffeomorphism range.** At synchrony, the derivative has eigenvalues \(1-3h\) and \(1-(1+2w)h\), so \(F\) has a singular derivative at \(h=1/\Lambda\). For any \(h>1/\Lambda\), the largest eigenvalue of the symmetric representative \(M^{1/2}H(x,y)M^{1/2}\) is \(\Lambda\) at synchrony and strictly negative at one of the explicitly identified sources. By continuity along a path between these points, this eigenvalue crosses \(1/h\); therefore \(\det \mathrm DF=0\) somewhere on the torus. Thus no larger positive \(h\) produces a global diffeomorphism. This maximality statement is about diffeomorphisms, not about absence of attractors or convergence beyond the threshold.

**6. Almost-everywhere synchrony beyond invertibility.** The descent argument proves convergence for all \(0<h<2/\Lambda\). Every nonsynchronous fixed point is either a hyperbolic saddle or hyperbolic source for this same full interval: negative eigenvalues of \(MH\) yield expanding multipliers \(1+h|\lambda|>1\), while positive eigenvalues yield multipliers in \((-1,1)\). The local stable set of each nonsynchronous fixed point is a smooth submanifold of dimension at most one. The determinant \(\det\mathrm DF\) is real analytic and is **not identically zero**, since at a source \(H\) is negative definite and \(\mathrm DF\) is invertible. Its zero set has Lebesgue measure zero. Off that null set \(F\) is a local diffeomorphism, so the inverse image of any null set has measure zero; the inverse image inside the critical-Jacobian set is null as well. By iteration, every countable preimage of each local stable manifold is null. This proves that all nonsynchronous attraction basins are Haar null and the synchronization basin has full Haar measure. Finally, synchrony is strictly Schur stable exactly when \(0<h<2/\Lambda\), because its two real multipliers are \(1-3h\) and \(1-(1+2w)h\). Hence its strict local stability threshold is sharp.

## Verification

Execute the standalone `verify_triangle.py` with Python and SymPy. It symbolically checks the quotient map, the two nonconstant Laplacian eigenvalues, all Hessian index identities, the eigenvalues at additional source points, and both invariant-circle identities. Rational sample weights on both sides of the transition are checked numerically against the predicted exact index lists and Schur interval. These diagnostics do **not** prove global convergence, transversality, or infinite-domain uniqueness; those follow from the analytical argument above. No external proof assistant or independent certification is asserted.

## Relationship to prior work

Buescu–D'Aniello–Oliveira (arXiv:2610.10993v1, October 7, 2026) establish Lyapunov descent, a graph-Laplacian step bound, and a Morse–Smale criterion for certain separable edge-coordinate systems, including paths, stars, and graphs with sufficiently weak added edges. Our result does not claim their descent or inverse-function method as new: it proves Morse–Smale dynamics for the **complete isosceles triangle at every positive closing-edge weight**, including regimes beyond any unspecified weak-link neighborhood. Its invariant-circle elimination of saddle connections is model specific.

Zhao–Zhou (arXiv:2407.11314, July 2024) already give the same four/six equilibrium census and corresponding continuous-flow stability classes for the isosceles Kuramoto triangle, including signed weights. This equilibrium census is explicitly prior art, not a new finding. Their work does not study an explicit-Euler map or prove a global Morse–Smale diffeomorphism across arbitrary positive closing-edge strengths. Schaeffer–McCalla (arXiv:1908.01753, August 2019) prove general large-step strict-saddle avoidance; such avoidance alone is also not claimed new. The stronger combined result here is a fully classified finite-network discrete-time Morse–Smale system for all strictly positive weights, plus a direct exact-step basin statement.

A related published finding, *Critical relaxation and an exceptional exponential circle in a discrete repulsive oscillator triangle* (published-finding corpus, 2026), treats **repulsive** weights at a degenerate weak-edge transition. It has a parabolic attracting point and no global all-weight hyperbolic Morse–Smale classification, so it does not imply the attractive theorem by a sign reversal. A repulsive-to-attractive sign reversal changes the potential's minima and the stability of the degenerate state; arbitrary fixed-point bifurcation analysis alone does not establish the invariant-circle transversality conclusion.

## Limitations

The main Morse–Smale statement excludes the degenerate weight \(w=1/2\). The longer-step interval establishes almost-everywhere convergence but does **not** assert invertibility or Morse–Smale structure there. No claim is made that synchrony ceases to have any nonlinear attracting behavior exactly at \(h=2/\Lambda\), where it has a unit-modulus multiplier. The theorem concerns identical oscillators, symmetric strictly positive sinusoidal pair interactions, three vertices, and the exact explicit Euler map; it does not extend without proof to signed, directed, heterogeneous-frequency, stochastic or larger graphs. General background results are credited rather than independently reclassified as new. The possibility of an unlocated equivalent all-weight triangle theorem remains a historical-priority risk; this is a self-review, not an independent audit.

## References

1. J. Buescu, E. D'Aniello, and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, first public October 7, 2026. https://arxiv.org/abs/2610.10993
2. X. Zhao and X. Zhou, *Critical Points, Stability, and Basins of Attraction of Three Kuramoto Oscillators with Isosceles Triangle Network*, arXiv:2407.11314, July 16, 2024; Applied Mathematics Letters 158 (2024), 109246. https://arxiv.org/abs/2407.11314
3. H. Schaeffer and S. G. McCalla, *Extending the Step-size Restriction for Gradient Descent to Avoid Strict Saddle Points*, arXiv:1908.01753, August 5, 2019; SIAM J. Math. Data Sci. 2 (2020), 1181–1197. https://arxiv.org/abs/1908.01753
4. *Critical relaxation and an exceptional exponential circle in a discrete repulsive oscillator triangle*, published-finding corpus repository (2026). https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-critical-relaxation-and-an-exceptional-exponential-circle-in-a-d--2e5d3c4aa08c
