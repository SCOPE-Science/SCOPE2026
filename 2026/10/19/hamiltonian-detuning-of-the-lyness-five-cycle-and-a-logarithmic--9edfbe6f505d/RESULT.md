# Hamiltonian detuning of the Lyness five-cycle and a logarithmic high-energy rotation response

## Finding

For the positive Lyness map
\[
F_a(x,y)=\left(y,\frac{a+y}{x}\right),\qquad a>0,\quad x,y>0,
\]
let
\[
V_a(x,y)=\frac{(1+x)(1+y)(a+x+y)}{xy},\qquad r_* =\frac{11+5\sqrt5}{2}.
\]
For each **fixed** \(r>r_*\), and all \(a\) sufficiently close to \(1\), the level \(V_a=r\) is a smooth positive oval. Denote by \(\rho_a(r)\) the clockwise-positive rotation number of the restricted map, with its continuous lift normalized by \(\rho_1(r)=1/5\). Define \(H(u,v)=\log V_1(e^u,e^v)\), and let \(P(r)>0\) be the minimal physical period of the Hamiltonian flow \(\dot u=H_v,\ \dot v=-H_u\) on \(H=\log r\).

The first-order detuning law is
\[
\boxed{\rho_a(r)=\frac15+\frac{a-1}{5P(r)}+O_r((a-1)^2)},
\qquad
\boxed{\left.\partial_a\rho_a(r)\right|_{a=1}=\frac{1}{5P(r)}>0}.
\]
Its coefficients have **two sharp energy endpoints**:
\[
\boxed{\lim_{r\downarrow r_*}\left.\partial_a\rho_a(r)\right|_{a=1}
=\frac{\sqrt{(25-11\sqrt5)/2}}{10\pi}},
\qquad
\boxed{\lim_{r\to\infty}(\log r)\left.\partial_a\rho_a(r)\right|_{a=1}=\frac1{25}}.
\]
The high-energy limit concerns the already taken derivative at \(a=1\); it is not a simultaneous double-scaling assertion.

## Assumptions and scope

The parameter is real positive, and initial coordinates are strictly positive. For the detuning statement, \(r>r_*\) is fixed **before** \(a\to1\), which ensures a noncritical oval. The rotation convention is clockwise in logarithmic coordinates \(u=\log x,\ v=\log y\). In the opposite angular convention the derivative changes sign. The flow period is measured in its natural Hamiltonian time, not in iterations of the discrete map. No claim concerns nonpositive initial coordinates, singular fibers, or a uniform expansion as both \(a\to1\) and \(r\to\infty\).

## Proof

**1. Exact invariance, area form, and periodic base map.** Direct substitution gives \(V_a\circ F_a=V_a\) and \(F_a^*(dx\wedge dy/(xy))=dx\wedge dy/(xy)\). At \(a=1\), five elementary substitutions give \(F_1^5=\mathrm{id}\) on the positive quadrant. Each function \(H_a(u,v)=\log V_a(e^u,e^v)\) is strictly convex, since its first two logarithmic-sum-exponential summands each contribute a strictly positive diagonal second derivative; it is also proper. Thus all levels strictly above the unique minimum are compact smooth convex ovals. At \(a=1\) the minimum lies at \(x=y=\varphi=(1+\sqrt5)/2\) with value \(r_*\), so the asserted noncritical ovals persist as \(a\to1\). The differential of \(F_1\) at its fixed point is \(\left(\begin{smallmatrix}0&1\\-1&1/\varphi\end{smallmatrix}\right)\), whose eigenvalues have clockwise rotation angle \(2\pi/5\). Continuity on the nested ovals, together with \(F_1^5=\mathrm{id}\), forces the clockwise rotation number \(1/5\) on every oval.

**2. Exact five-iterate parameter derivative.** Write \(X=\left.\partial_a F_a^5\right|_{a=1}\). A rational differentiation of the five iterates yields the identity on the *entire* positive quadrant
\[
\boxed{X(x,y)=\frac{xy}{V_1(x,y)}\bigl(\partial_yV_1(x,y),-\partial_xV_1(x,y)\bigr)}
\]
\[
=\left(-\frac{x(x-y^2+1)}{(1+y)(1+x+y)},\,-\frac{y(x^2-y-1)}{(1+x)(1+x+y)}\right).
\]
This is verifiable by clearing the positive denominators, or exactly by `verify.py`. In \((u,v)\) coordinates it becomes \((\partial_vH,-\partial_uH)\), the Hamiltonian vector field of \(H\). The infinitesimal detuning is therefore nonzero and tangent to every noncritical level.

**3. Rotation coefficient from the actual circle motion.** Fix \(r>r_*\). Choose a smooth family of diffeomorphisms \(\Psi_a\) from the old oval \(\{V_1=r\}\) onto \(\{V_a=r\}\), with \(\Psi_1=\mathrm{id}\), e.g. follow outward logarithmic radial rays from the varying minimum. The conjugated fifth iterate \(G_a=\Psi_a^{-1}\circ F_a^5\circ\Psi_a\) satisfies \(G_1=\mathrm{id}\). Differentiating at \(a=1\), the two derivatives of the moving-frame maps cancel, giving \(\partial_aG_a|_1=X\). In the oriented Hamiltonian time coordinate \(\theta=t/P(r)\pmod1\), its lift satisfies, uniformly along the circle,
\[
G_a(\theta)=\theta+\frac{a-1}{P(r)}+O_r((a-1)^2).
\]
The translation number of an orientation-preserving lift trapped between \(\theta+c-C(a-1)^2\) and \(\theta+c+C(a-1)^2\) differs from \(c\) by at most \(C(a-1)^2\). Since the lifted rotation of the fifth iterate equals \(5\rho_a(r)-1\), the first boxed detuning identity follows, including positivity.

**4. Near-center limit.** The logarithmic-coordinate Hessian of \(H\) at \((\log\varphi,\log\varphi)\) has determinant
\[
\det D^2H=\frac{25-11\sqrt5}{2}>0.
\]
The positive period of the local Hamiltonian oscillator therefore tends to \(2\pi/\sqrt{\det D^2H}\) as \(r\downarrow r_*\). Applying Step 3 gives the stated first endpoint.

**5. High-energy action and exact leading coefficient.** Let \(z=\log r\) and
\[
A(z)=\operatorname{area}\bigl\{(u,v)\in\mathbb R^2:H(u,v)\le z\bigr\}.
\]
The function \(H\) differs by a bounded amount from the homogeneous piecewise-linear convex function
\[
L(u,v)=\max(0,u)+\max(0,v)+\max(0,u,v)-u-v.
\]
Indeed \(L\le H\le L+\log12\). The polygon \(\{L\le1\}\) has consecutive vertices \((-1,0),(0,-1),(1,0),(1,1),(0,1)\) and exact area \(5/2\). Homogeneity implies
\[
\frac52(z-\log12)^2\le A(z)\le\frac52 z^2 \quad(z>\log12),
\]
so \(A(z)=(5/2)z^2+O(z)\). Because \(H\) is convex, Minkowski interpolation of its convex sublevel sets and the planar Brunn–Minkowski inequality imply that \(\sqrt{A(z)}\) is concave for \(z>\log r_*\). The asymptotic slope of this concave function is \(\sqrt{5/2}\); by monotonicity of secant slopes, its derivative tends to that slope. It follows that \(A'(z)\sim5z\). The coarea formula and the unit-speed relation along a Hamiltonian level, \(|X_H|=|\nabla H|\), yield the exact action-period identity
\[
A'(z)=\oint_{H=z}\frac{ds}{|\nabla H|}=P(e^z).
\]
Consequently \(P(r)\sim5\log r\); substituting in Step 3 gives the sharp high-energy response coefficient \(1/25\).

## Verification

The self-contained companion `verify.py` uses exact rational symbolic computations to check the parameter-dependent first integral, preservation of the logarithmic area form, global five-periodicity at \(a=1\), the exact derivative vector field, tangency to the first integral, the equilibrium value, the Hessian determinant and the tropical pentagon area. It also checks the limiting centered rotation derivative numerically for shrinking detunings. Running `python verify.py` returns `VERIFY_OK`. The infinite-energy estimate and the circle rotation perturbation are proved above; the finite checker does not certify those infinite limits.

## Relationship to prior work

The Lyness five-cycle is classical. Cima, Gasull and Mañosa (2008) study invariant quantities and rational Lie-symmetry vector fields for Lyness maps; these ingredients and global five-periodicity are not asserted to be new. Bastien, Mañosa and Rogalski (2012) analyze positive invariant ovals and rotation numbers, including their limiting behavior. Hone and Kouloukas (2023; first public arXiv 2021) view the family as a symplectic deformation of the five-cycle. The present fixed-energy parameter derivative tied to the five-iterate Hamiltonian field, and its sharp large-energy logarithmic prefactor, are the particular claims assessed here, not integrability or the existence of the rotation number itself.

## Limitations

This is a first-order response at a single resonant parameter \(a=1\), not a closed formula for \(\rho_a(r)\) at arbitrary parameters. The asymptotic \(1/(25\log r)\) controls the derivative after setting \(a=1\); it does not establish uniformity over growing \(r\). The global positivity domain is essential for convexity and area finiteness. The 2004 monograph-era article by Bastien and Rogalski and earlier work surrounding Zeeman's monotonicity problem remain plausible sources of overlooked equivalent formulas; priority is not independently certified.

## References

- A. Cima, A. Gasull and V. Mañosa, *Some properties of the k-dimensional Lyness' map*, arXiv:0801.4360 (first posted 2008-01-28), J. Phys. A 41 (2008), 285205. https://arxiv.org/abs/0801.4360
- G. Bastien, V. Mañosa and M. Rogalski, *On periodic solutions of 2-periodic Lyness difference equations*, arXiv:1201.1027 (first posted 2012-01-04). https://arxiv.org/abs/1201.1027
- A. Hone and T. Kouloukas, *Deformations of cluster mutations and invariant presymplectic forms*, arXiv:2107.11866 (2021), J. Algebr. Comb. 57 (2023), 763–791. https://arxiv.org/abs/2107.11866
- F. Beukers and R. Cushman, *Zeeman's monotonicity conjecture*, J. Differential Equations (1998). https://doi.org/10.1006/jdeq.1997.3359
