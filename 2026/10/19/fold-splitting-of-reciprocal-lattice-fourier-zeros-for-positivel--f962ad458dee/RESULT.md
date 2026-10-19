# Fold splitting of reciprocal-lattice Fourier zeros for positively weighted triangles

## Finding
Let \(T=\{(x,y)\in\mathbb R^2:x\geq0,\ y\geq0,\ x+y\leq1\}\) and use the angular-frequency Fourier convention
\[
F_\varepsilon(\xi,\eta)=\int_T(1+\varepsilon g(x,y))e^{-i(\xi x+\eta y)}\,dx\,dy.
\]
Here \(g\in L^\infty(T;\mathbb R)\) and \(\varepsilon\in\mathbb R\). For integers \(m,n\) with \(mn(m-n)\ne0\), set \(\lambda_{m,n}=2\pi(m,n)\) and
\[
u_{m,n}=\operatorname{Re}\int_Tg(x,y)e^{-2\pi i(mx+ny)}\,dx\,dy.
\]
**Local fold theorem.** If \(u_{m,n}\ne0\), there is a neighborhood \(U_{m,n}\) of \(\lambda_{m,n}\) and a threshold \(\varepsilon_{m,n}>0\) such that, whenever \(0<|\varepsilon|<\varepsilon_{m,n}\), the following exhaustive alternatives hold:

* If \(\varepsilon u_{m,n}<0\), \(F_\varepsilon\) has exactly two real-frequency zeros in \(U_{m,n}\), both simple as zeros of the map \((\operatorname{Re}F_\varepsilon,\operatorname{Im}F_\varepsilon):\mathbb R^2\to\mathbb R^2\). Their locations are
\[
(\xi_\pm,\eta_\pm)=\lambda_{m,n}\bigl(1\pm\sqrt{-2\varepsilon u_{m,n}}\bigr)+O_{m,n,g}(|\varepsilon|).
\]
* If \(\varepsilon u_{m,n}>0\), there are no real-frequency zeros in \(U_{m,n}\).

For the affine perturbation \(g(x,y)=a x+b y\), with real constants \(a,b\), the unfolding coefficient is exactly
\[
u_{m,n}=-\frac{an-bm}{(2\pi)^2mn(m-n)}.
\]
Thus the pair/no-pair decision is the sign of \(\varepsilon(an-bm)/[mn(m-n)]\) whenever \(an-bm\ne0\). If \(an=bm\), the original node itself remains an *exact* zero for every \(\varepsilon\); no assertion about additional nearby zeros is made in that degenerate case.

For the positive-density family \(g(x,y)=x\), the nodal indices that split for small \(\varepsilon>0\) are precisely those with \(m(m-n)>0\). Define
\[
L_R=\{(m,n)\in\mathbb Z^2:mn(m-n)\ne0,\ m^2+n^2\leq R^2\},\quad L_R^+=\{(m,n)\in L_R:m(m-n)>0\}.
\]
Then
\[
\#L_R^+=\tfrac34\pi R^2+O(R),\qquad
\#L_R=\pi R^2+O(R),\qquad
\lim_{R\to\infty}\frac{\#L_R^+}{\#L_R}=\frac34.
\]
For each fixed finite \(R\), the perturbation can be taken sufficiently small that each original node in \(L_R^+\) gives exactly two nearby simple zeros, while each node in its complement gives none. The order of these two limits is essential.

## Assumptions and scope
The triangle is closed, but boundary values have no effect on its integrals. The Fourier transform has **no volume normalization**; \(\int_T1=1/2\). The symbols \(\xi,\eta\) are angular frequencies; consequently the original nodal lattice has spacing \(2\pi\). The perturbation is real and bounded, not necessarily smooth; compact support makes its Fourier transform real analytic in frequency. For \(|\varepsilon|\|g\|_\infty<1\), the density \(1+\varepsilon g\) is strictly positive almost everywhere. The theorem is local at each fixed node, and its smallness threshold need not be uniform over an unbounded set of indices.

## Proof
Write
\[
A(z)=\int_0^1e^{-izx}\,dx=\frac{1-e^{-iz}}{iz},\qquad
F_0(\xi,\eta)=\frac{A(\xi)-e^{-i\eta}A(\xi-\eta)}{i\eta},
\]
interpreting removable singularities by continuity. With \(k=2\pi m\), \(\ell=2\pi n\), and \(d=k-\ell\), the assumptions ensure that \(k,\ell,d\) are all nonzero, and \(F_0(k,\ell)=0\). At every nonzero integer multiple of \(2\pi\), \(A'(z)=1/z\); direct differentiation therefore gives
\[
\partial_\xi F_0(k,\ell)=\frac{i}{kd},\qquad
\partial_\eta F_0(k,\ell)=-\frac{i}{\ell d}.
\]
In particular the full real Jacobian at this zero has rank one. Along its real tangent-kernel direction \((k,\ell)\), the exponential factors in the displayed formula for \(F_0\) expand to yield the *universal* radial second derivative
\[
F_0\bigl(k(1+t),\ell(1+t)\bigr)=\frac{t^2}{2}+O_{m,n}(t^3).
\]
The vanishing of the first derivative here also follows from the two displayed first derivatives.

Let \(G=\widehat{g\mathbf1_T}\) and introduce local real coordinates \((t,s)\) by
\[
(\xi,\eta)=(k(1+t),\ell(1+t)+s).
\]
Because \(k\ne0\), these are valid coordinates, and because
\[
\left.\partial_s\operatorname{Im}F_0\right|_{t=s=0}=-\frac1{\ell d}\ne0,
\]
the real-analytic implicit-function theorem uniquely solves \(\operatorname{Im}(F_0+\varepsilon G)=0\) as \(s=h(t,\varepsilon)\) near \((0,0)\). It gives \(h(0,0)=0\) and \(\partial_t h(0,0)=0\). Every zero of \(F_\varepsilon\) sufficiently near \((k,\ell)\) must consequently lie on this graph.

Define the remaining real equation
\[
R(t,\varepsilon)=\operatorname{Re}F_\varepsilon\bigl(k(1+t),\ell(1+t)+h(t,\varepsilon)\bigr).
\]
The preceding derivatives and \(\operatorname{Re}\partial_\eta F_0(k,\ell)=0\) yield
\[
R(t,\varepsilon)=\frac{t^2}{2}+\varepsilon u_{m,n}
+O_{m,n,g}\bigl(|t|^3+|\varepsilon t|+\varepsilon^2\bigr).
\]
For fixed \(m,n,g\), the \(t\)-second derivative of \(R\) is strictly positive in a sufficiently small closed rectangle centered at \((0,0)\). Hence each fixed-\(\varepsilon\) section has one interior critical point, a strict minimum, and positive values on two fixed small boundary points when \(\varepsilon\) is small. Its minimum is \(\varepsilon u_{m,n}+O(\varepsilon^2)\), since the critical point is \(O(\varepsilon)\). This proves exactly two zeros if \(\varepsilon u_{m,n}<0\) and no zeros if \(\varepsilon u_{m,n}>0\). Solving the quadratic leading term gives the stated square-root expansions. At the two roots, \(\partial_tR=\pm\sqrt{-2\varepsilon u_{m,n}}+O(\varepsilon)\ne0\), and together with \(\partial_s\operatorname{Im}F_\varepsilon\ne0\) this makes both full real Jacobians nonsingular.

If \(g=ax+by\), differentiation under the integral gives \(G=i(a\partial_\xi F_0+b\partial_\eta F_0)\); inserting the displayed derivatives gives
\[
G(k,\ell)=-\frac{a}{kd}+\frac{b}{\ell d}
=-\frac{an-bm}{(2\pi)^2mn(m-n)}.
\]
This number is real. Its vanishing implies \(F_\varepsilon(k,\ell)=F_0(k,\ell)+\varepsilon G(k,\ell)=0\) identically for every \(\varepsilon\). The affine sign test now follows from the general theorem.

For \(g=x\), the splitting region is \(m(m-n)>0\), the union of two open planar wedges of total opening angle \(3\pi/2\). Integer lattice points in a fixed-angle sector of radius \(R\) equal its Euclidean area up to \(O(R)\), by comparing unit lattice squares to the sector and bounding the boundary strip. Removing the three forbidden lines affects only \(O(R)\) points. This gives both lattice counts and the ratio \(3/4\). A finite set of nodes has a common admissible perturbation threshold by taking the minimum of its finitely many local thresholds.

## Verification
The accompanying `verify_triangle.py` independently evaluates the Fourier-integral formula and its frequency derivatives at several lattice nodes at high precision, checks the universal radial quadratic coefficient and the affine unfolding coefficient, locates both roots with their predicted square-root scale in split cases, and exactly enumerates lattice-sector signs for increasing radii. Execute with `python3 verify_triangle.py` and `mpmath` installed. The analytic implicit-function argument and the unit-square lattice estimate, **not** these finite numerical checks, establish the claims for all admissible nodes and bounded perturbations.

## Relationship to prior work
Fuglede's original 1974 spectral-set paper proved the non-spectrality of a triangle, using the exactly discrete zero set of its **unweighted** Fourier transform. Kolountzakis (1999) extended the non-spectrality conclusion to nonsymmetric convex bodies, and Kolountzakis (2025, Section 4) explicitly reconstructs the triangle's unweighted nodal lattice and its spectral meaning. Those facts are taken as known. The assertion here is not another characterization of the unweighted zero set: it is the precise **local real-zero bifurcation** under positive-density perturbations, including a coefficient-dependent two/no-zero decision, its universal square-root speed, and a three-quarter nodal-density law. The known finite-cyclic zero classifications and Fourier-zero estimates for higher-dimensional bipyramids concern different measures and do not imply this local triangle unfolding.

## Limitations
The statement excludes the degenerate case \(u_{m,n}=0\) from its local counting dichotomy, except for the exact protected-node observation for affine weights. It does not give a threshold uniform in \((m,n)\), classify zeros that might occur away from neighborhoods of the original lattice, or assert existence or nonexistence of weighted Fourier bases. The fourth-moment and global sampling problems for the perturbed measure are not addressed. Independent mathematical audit and independent publication-priority review remain unperformed. The original 1974 paper's complete text was not accessible during comparison; its triangle calculation was checked through a detailed later reconstruction, leaving a specifically identified originality risk.

## References
1. B. Fuglede, “Commuting self-adjoint partial differential operators and a group theoretic problem,” *Journal of Functional Analysis* **16** (1974), 101–121. DOI: https://doi.org/10.1016/0022-1236(74)90072-X.
2. M. N. Kolountzakis, “Non-symmetric convex domains have no basis of exponentials,” arXiv:math/9904064, first posted 1999-04-14; published in *Illinois Journal of Mathematics* **44** (2000), 542–550. https://arxiv.org/abs/math/9904064.
3. M. N. Kolountzakis, “Fuglede's conjecture on orthogonal bases of exponentials,” arXiv:2509.05782, first posted 2025-09-06, especially Section 4. https://arxiv.org/abs/2509.05782.
