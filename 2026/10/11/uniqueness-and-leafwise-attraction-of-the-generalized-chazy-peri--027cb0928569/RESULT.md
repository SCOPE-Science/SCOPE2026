# Uniqueness and leafwise attraction of the generalized Chazy periodic cylinder

## Finding
For the generalized Chazy family with integer \(q\ge2\) and coefficient \(k=q+1\), **each negative-energy surface contains at most one periodic orbit**. Whenever that orbit exists, it is exponentially orbitally attracting within its energy surface, every bounded forward orbit on that surface converges to it, and its nontrivial Floquet multiplier is independent of energy. The known existence theorems thus imply that each negative-energy surface has exactly one such orbit for \(q=2,3\), and also for the finite range \(2\le q\le100\) covered by the published algorithmic existence result.

More precisely, if \(\gamma_h\) is the periodic orbit on \(H=-h\), where \(h>0\), and \(T_h\) is its minimal original-time period, then the three Floquet multipliers, with algebraic multiplicities, are
\[
1,\quad1,\quad\rho_q,\qquad
\rho_q=\exp\!\left(-\int_0^{T_h}|x_h(t)|^q\,dt\right)\in(0,1).
\]
The number \(\rho_q\) depends on \(q\) but not on \(h\). This is a statement about the original autonomous flow; the pair of unit multipliers is not asserted to be semisimple.

## Assumptions and scope
Fix any integer \(q\ge2\) and consider the autonomous system in \(\mathbb R^3\)
\[
\dot x=y,\qquad \dot y=z,\qquad
\dot z=-|x|^q z-(q+1)a_q(x)y^2,
\quad a_q(x)=\begin{cases}|x|^q/x,&x\ne0,\\0,&x=0.\end{cases}
\]
For even \(q\) this is polynomial, while for odd \(q\ge3\) it is continuously differentiable (not generally polynomial). Its first integral is
\[
H(x,y,z)=xz-\frac12y^2+x|x|^q y.
\]
Write \(S_h=H^{-1}(-h)\) for \(h>0\). A forward orbit is called *bounded* when its image for all positive times remains in a compact subset of \(\mathbb R^3\); bounded trajectories then exist for all positive time because this vector field is locally Lipschitz. All convergence below is convergence of the distance to the closed periodic orbit, without a claim about convergence to a particular phase point.

The uniqueness and attraction assertions are **conditional on existence** and hold for every integer \(q\ge2\). The existence input is the theorem of Llibre–Novaes–Valls for \(q=2,3\), and their separately reported algorithmic existence corollary through \(q=100\). Existence for every integer \(q>100\) follows from the later published work of Zhuang–Liu–Luo, but is not independently needed for the uniqueness proof or used to assign the date of the motivating source.

## Proof
**1. Conservation, regularity, and leaf topology.** Put \(f(x)=|x|^q\); then \((xf(x))'=(q+1)f(x)\), including at \(x=0\). Direct differentiation gives
\[
\frac{dH}{dt}=x\dot z+(q+1)f(x)y^2+xf(x)z=0.
\]
The regularity \(q\ge2\) makes the vector field at least \(C^1\). As \(\partial_zH=x\), a critical point of \(H\) has \(x=0\), then \(\partial_yH=-y\) forces \(y=0\); consequently all critical points lie in \(H=0\). Likewise every equilibrium has \(y=z=0\), hence lies in \(H=0\). Thus every \(S_h\) is a smooth invariant surface without equilibria.

The smooth triangular coordinate transformation \(w=z+f(x)y\) takes \(H\) to \(xw-y^2/2\). With \(U=x+w\) and \(V=x-w\), the equation \(H=-h\) becomes
\[
V^2+2y^2-U^2=4h.
\]
For arbitrary \(U\in\mathbb R\), a complete angular parameter is
\[
V=\sqrt{U^2+4h}\cos\theta,\qquad
 y=\frac{\sqrt{U^2+4h}}{\sqrt2}\sin\theta,
\quad \theta\in\mathbb R/(2\pi\mathbb Z).
\]
Hence \(S_h\) is diffeomorphic to a cylinder \(\mathbb R\times S^1\).

**2. Strict surface-area contraction and uniqueness.** Let \(\Omega=dx\wedge dy\wedge dz\). Since \(dH\ne0\) on \(S_h\), choose an area form \(\omega_h\) on that surface by the coarea identity \(dH\wedge\omega_h=\Omega\). More explicitly, in a tubular neighborhood use \(N=\nabla H/|\nabla H|^2\) and restrict \(\iota_N\Omega\) to \(S_h\); choose its orientation so that \(\omega_h\) is positive. The field is tangent to \(S_h\) and
\[
\mathrm{div}_{\mathbb R^3}X=\partial_x y+\partial_y z+\partial_z\dot z=-|x|^q.
\]
Conservation of \(H\), together with the coarea relation and the ambient Liouville identity, implies the exact identity on \(S_h\)
\[
\mathcal L_X\omega_h=-|x|^q\omega_h.
\]
If a contractible periodic orbit existed, it would bound a disk in \(S_h\). If two distinct noncontractible periodic orbits existed, their disjoint embedded circles would bound a compact annulus in \(S_h\). In either case denote this nonempty compact region by \(R\). Cartan's formula and Stokes' theorem give
\[
-\int_R|x|^q\omega_h
=\int_R\mathcal L_X\omega_h
=\int_{\partial R}\iota_X\omega_h=0,
\]
since \(X\) is tangent to the periodic boundary and \(\omega_h(X,X)=0\). The left-hand side is strictly negative: the open interior of \(R\) cannot lie in the one-dimensional intersection of \(S_h\) with \(x=0\). Contradiction. This excludes contractible cycles and proves at most one periodic orbit on each leaf.

**3. Floquet multipliers and leafwise attraction.** The return-map derivative transverse to a periodic orbit \(\gamma_h\) *within* \(S_h\) is the Liouville contraction of its area form over one circuit:
\[
\rho_q=\exp\!\left(\int_0^{T_h}\mathrm{div}_{S_h}X(\gamma_h(t))\,dt\right)
=\exp\!\left(-\int_0^{T_h}|x_h(t)|^q\,dt\right).
\]
The integral is strictly positive because a periodic orbit cannot remain in the plane \(x=0\) (the orbit would otherwise be an equilibrium). Hence \(0<\rho_q<1\), establishing local exponential orbital attraction within \(S_h\).

For the full three-dimensional variational monodromy, one unit multiplier is tangent to the autonomous flow; a second unit multiplier occurs in the quotient normal to \(S_h\), because \(dH\) is a first integral with \(dH\ne0\). The remaining multiplier is the one-dimensional return derivative \(\rho_q\). These three numbers are the full algebraic spectrum, without a claim of diagonalizability at the unit multiplier.

**4. Independence of energy.** The original equations are covariant under
\[
(x(t),y(t),z(t))\mapsto
(\lambda x(\lambda^q t),\lambda^{q+1}y(\lambda^q t),\lambda^{2q+1}z(\lambda^q t)),
\qquad\lambda>0.
\]
This scales \(H\) by \(\lambda^{2q+2}\). By uniqueness, it maps the sole cycle on \(H=-1\) to the sole cycle on \(H=-h\) for \(\lambda=h^{1/(2q+2)}\). Consequently
\[
T_h=h^{-q/(2q+2)}T_1,\qquad
\int_0^{T_h}|x_h(t)|^q\,dt=\int_0^{T_1}|x_1(t)|^q\,dt.
\]
This proves energy independence of \(\rho_q\). The period power law already follows from the scaling used in the existence literature and is included only to normalize the new multiplier claim.

**5. Bounded forward trajectories.** If \(S_h\) contains its periodic orbit and another initial point has a bounded positive semiorbit, the latter has a nonempty compact \(\omega\)-limit set in \(S_h\). There is no equilibrium on \(S_h\). Poincaré–Bendixson applied to the planar cylindrical surface therefore makes this \(\omega\)-limit set a periodic orbit. By step 2 it is \(\gamma_h\), so the distance to \(\gamma_h\) tends to zero. This is conditional on boundedness; it does not prove all trajectories on the noncompact cylinder are bounded.

## Verification
The embedded `check_chazy.py` carries out symbolic checks of \(X(H)=0\), \(\mathrm{div}X=-|x|^q\), and the anisotropic covariance for multiple even and odd integer instances on both half-lines, plus an explicit numerical positivity test for the amplitude exponent. It is a finite algebraic diagnostic, not a substitute for the arguments for all \(q\), the topology argument, or Poincaré–Bendixson. Run with `python check_chazy.py` after installing SymPy as indicated by `requirements.txt`.

## Relationship to prior work
Llibre, Novaes, and Valls (2023; arXiv:2307.00087, Theorem 1 and Corollary 1) establish the existence of an invariant cylinder of periodic orbits for \(q=2,3\) and through \(q=100\) using an algorithmic test, working on the same negative-energy surfaces. Their proof is existential through a trapping construction and root counts; the relevant statements and proof do not provide the global uniqueness, leafwise basin, or exact energy-invariant Floquet multiplier established here. The original Geronimi–Feix–Leach (1999) work reported numerical cycle observations. Zhuang, Liu, and Luo (2024) prove existence for all positive integer \(q\) at \(k=q+1\), according to its abstract; its full text was not available for a definitive novelty comparison, which leaves a genuine priority risk.

## Limitations
There is no bound proving that arbitrary forward trajectories on noncompact \(S_h\) remain bounded. The result gives no numerical closed form for \(\rho_q\), and does not assert full three-dimensional asymptotic stability: first-integral conservation prevents attraction across energy surfaces. It does not establish existence for the excluded \(q=1\) regularity case or independently reproduce the earlier computational existence certificates for \(q=4,\ldots,100\). No priority claim is made against inaccessible literature, especially the full Zhuang–Liu–Luo article.

## References
1. J. Llibre, D. D. Novaes and C. Valls, *Existence of a cylinder foliated by periodic orbits in the generalized Chazy differential equation*, **Chaos** 33 (2023), 073104. First arXiv version posted 2023-06-30: https://arxiv.org/abs/2307.00087 ; doi:10.1063/5.0138309.
2. C. Géronimi, M. R. Feix and P. G. L. Leach, *Periodic solutions and associated limit cycle for the generalised Chazy equation* (1999), doi:10.1007/BFb0105938.
3. Z. Zhuang, C. Liu and J. Luo, *On the periodic behavior of the generalized Chazy differential equation*, **Chaos** 34 (2024), 113106, doi:10.1063/5.0209050. Only public abstract inspected; full-text priority comparison unresolved.
