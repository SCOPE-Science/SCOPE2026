# Sharp volume-deficit asymptotics for extremal Reuleaux solids of revolution

## Finding
For every odd integer \(n\ge3\), let \(C_n\subset\mathbb R^2\) be the regular Reuleaux \(n\)-gon of width one, and let \(K_n\subset\mathbb R^3\) be the convex solid obtained by rotating \(C_n\) about a reflection-symmetry axis through a vertex. Each \(K_n\) is an extreme point (modulo translations) of the Minkowski-convex set of three-dimensional constant-width-one bodies by Hynd's theorem. The sequence approaches the radius-\(1/2\) ball in the Hausdorff metric, but remains extreme for every finite \(n\).

Its sharp volume deficit satisfies
\[
\boxed{\lim_{\substack{n\to\infty\\n\text{ odd}}} n^2\left(\frac{\pi}{6}-\operatorname{vol}_3(K_n)\right)=\frac{\pi^3}{48}.}
\]
Equivalently, \(\operatorname{vol}_3(K_n)=\pi/6-\pi^3/(48n^2)+o(n^{-2})\), through odd indices.

## Assumptions and scope
The planar regular Reuleaux \(n\)-gon is bounded by alternating circular arcs of radius one and vertices whose normal-angle intervals all have angular length \(\pi/n\). Its \(n\)-fold rotational symmetry and constant width imply that, with the origin at its dihedral center, its planar support \(h_n\) is even about a vertex axis, and \(h_n(\theta+\pi)=1-h_n(\theta)\). Angles \(\theta\) are measured from the chosen symmetry axis. The three-dimensional support of the body of revolution is \(h_n(\theta)\), where \(\theta\in[0,\pi]\) is the colatitude of its outer normal. Volumes are ordinary Euclidean volumes.

Define \(f_n(\theta)=h_n(\theta)-1/2\). The curvature-radius equation \(h_n+h_n''\in\{0,1\}\) is valid almost everywhere, with no singular part because the support function is continuously differentiable. Specifically,
\[
f_n''(\theta)+f_n(\theta)=g(n\theta),\qquad g(t)=\begin{cases}-1/2,&|t|<\pi/2\pmod {2\pi},\\+1/2,&\pi/2<|t|<\pi\pmod {2\pi} .\end{cases}\]
Changes at the finitely many endpoints are immaterial. The function \(f_n\) is even and \(2\pi/n\)-periodic, and has zero mean; it also satisfies \(f_n(\pi-\theta)=-f_n(\theta)\) for odd \(n\). These properties remove all translational solutions of the curvature equation.

## Proof
**Step 1: exact volume identity.** For any axisymmetric convex constant-width-one body whose planar profile support is \(h(\theta)=1/2+f(\theta)\), with \(f(\pi-\theta)=-f(\theta)\), \(f'(0)=f'(\pi)=0\), and piecewise absolutely continuous derivative, the standard support-Jacobian formula gives
\[
V=\frac{2\pi}{3}\int_0^\pi h(h+h'')(h+h'\cot\theta)\sin\theta\,d\theta.
\]
This follows by writing the surface normal as \((\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta)\); the two principal radii are \(h+h''\) and \(h+h'\cot\theta\), so \(3V=\int h\,dS\). The formula extends from smooth convex support functions to the present piecewise \(C^2\), globally \(C^1\) functions by intervalwise integration and approximation. In the integral, the combined second-derivative terms satisfy
\[
\int_0^\pi h^2(h''\sin\theta+h'\cos\theta)d\theta=-2\int_0^\pi h(h')^2\sin\theta d\theta,
\]
while
\[
\int_0^\pi hh''h'\cos\theta d\theta=\tfrac12\int_0^\pi h(h')^2\sin\theta d\theta-\tfrac12\int_0^\pi(h')^3\cos\theta d\theta.
\]
The latter cubic integral vanishes under \(\theta\mapsto\pi-\theta\) because \(h'=f'\) is even and \(\cos\theta\) is odd. Likewise \(\int f\sin\theta\), \(\int f^3\sin\theta\), and \(\int f(f')^2\sin\theta\) vanish. Expanding the remaining terms yields the **exact** identity
\[
\frac{\pi}{6}-V=\frac{\pi}{2}\int_0^\pi\bigl((f')^2-2f^2\bigr)\sin\theta\,d\theta.\tag{1}
\]

**Step 2: scale the alternating curvature.** Put \(F_n(t)=n^2f_n(t/n)\). Then \(F_n\) is even, mean-zero and \(2\pi\)-periodic and satisfies
\[
F_n''(t)+n^{-2}F_n(t)=g(t).\tag{2}
\]
The Fourier series \(g(t)=-\frac2\pi\sum_{j\ge1,\,j\text{ odd}}\frac{(-1)^{(j-1)/2}}{j}\cos(jt)\) and the absence of a mean or first-translation harmonic imply
\[
F_n(t)=-\frac2\pi\sum_{j\ge1,\,j\text{ odd}}\frac{(-1)^{(j-1)/2}}{j(n^{-2}-j^2)}\cos(jt).
\]
Its coefficients and differentiated coefficients are dominated uniformly by summable multiples of \(j^{-3}\) and \(j^{-2}\) for \(n\ge3\). Hence \(F_n\to F\) in \(C^1\) as \(n\to\infty\) through odd integers, where \(F\) is the even, mean-zero periodic solution of \(F''=g\). In particular \(F_n\) and \(F_n'\) are uniformly bounded, \(f_n=O(n^{-2})\), and \(f_n'(\theta)=n^{-1}F_n'(n\theta)\).

**Step 3: compute the periodic energy.** Since \(F''=g\), evenness and periodicity give
\[
F'(t)=\begin{cases}-t/2,&0\le t\le\pi/2,\\(t-\pi)/2,&\pi/2\le t\le\pi,\end{cases}
\]
with an odd, \(2\pi\)-periodic extension. Consequently its mean-square derivative is
\[
\langle(F')^2\rangle=\frac1\pi\left(\int_0^{\pi/2}\frac{t^2}{4}\,dt+\int_{\pi/2}^\pi\frac{(t-\pi)^2}{4}\,dt\right)=\frac{\pi^2}{48}.\tag{3}
\]
For any continuous periodic \(w\) and any continuous \(\psi\) on \([0,\pi]\), averaging over rapidly oscillating periods gives \(\int_0^\pi w(n\theta)\psi(\theta)d\theta\to\langle w\rangle\int_0^\pi\psi(\theta)d\theta\). Uniform \(C^1\) convergence allows \(w=(F_n')^2\) in this formula. With \(\psi(\theta)=\sin\theta\), this yields
\[
\lim_{\substack{n\to\infty\\n\text{ odd}}}n^2\int_0^\pi(f_n'(\theta))^2\sin\theta\,d\theta=\frac{\pi^2}{48}\cdot 2=\frac{\pi^2}{24}.
\]
The remaining contribution \(n^2\int_0^\pi f_n(\theta)^2\sin\theta\,d\theta=O(n^{-2})\) tends to zero. Substitute in (1) to obtain the claimed constant \(\pi^3/48\). The uniform bound \(f_n=O(n^{-2})\) gives the asserted Hausdorff convergence of \(K_n\) to the radius-\(1/2\) ball. Hynd's theorem supplies extremality of each finite \(K_n\), independently of the asymptotic calculation.

## Verification
The included Python verification script independently evaluates the exact Fourier support identity (1) by integration for several odd \(n\) and independently computes volume by integrating the disks that define the rotated Reuleaux polygon. It compares both approaches and the rescaled deficit against \(\pi^3/48\). It is numerical evidence, not the proof of the infinite limit. The analytic argument above proves the limit and all normalization factors. Run \(`python3 verification/reuleaux_volume_check.py`\) after installing NumPy and SciPy.

## Relationship to prior work
Hynd, *On extreme constant width bodies in \(\mathbb R^3\)*, publicly posted January 28, 2025, proves that solids generated by rotating symmetric planar Reuleaux polygons are extreme. That is a prior theorem, not claimed here. The classical support-Jacobian identity and periodic Fourier analysis are standard tools. The new assertion isolates the exact asymptotic volume gap along the canonical regular odd-polygon sequence. This is not an arbitrary parameter slice: it quantifies an explicit sequence of extreme constant-width solids approaching the unique volume-maximizing ball. Published works about the planar area, polar moment or Estermann measure of regular Reuleaux polygons do not supply this three-dimensional volume asymptotic. Literature searches found no coincident statement; this cannot establish absolute historical priority.

## Limitations
The asymptotic is only along odd orders for regular planar Reuleaux polygons rotated about vertex-reflection axes. It does not assert monotonicity of the deficits, sharp stability among all extreme bodies, a next asymptotic coefficient, or general bounds for asymmetric Reuleaux polygons. The source theorem of extremality and the new volume asymptotic have separate proofs. Historical priority is provisional; an older geometric formula may imply the coefficient without using this formulation. Independent mathematical validation has not been performed.

## References
1. R. Hynd, *On Extreme Constant Width Bodies in \(\mathbb R^3\)*, arXiv:2501.16940, first posted 2025-01-28. Open-access journal version: *Discrete & Computational Geometry* (2025 online), DOI 10.1007/s00454-025-00779-6.
2. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, Cambridge University Press, support measures and volume formula.
3. H. Martini, L. Montejano and D. Oliveros, *Bodies of Constant Width: An Introduction to Convex Geometry with Applications*, Springer, 2019.
