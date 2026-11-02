# Exact logarithmic correction at the critical Sprott M fold

## Finding

**Theorem (two-term critical relaxation).** Consider the polynomial system
\[
\dot x=-z,\qquad \dot y=-x^2-y,\qquad \dot z=a+bx+y,
\]
with \(b>0\) at the fold \(a=-b^2/4\), and put \(E=(b/2,-b^2/4,0)\). Define its global strong-stable set to consist of initial states with forward-complete trajectories converging exponentially to \(E\). Every bounded forward-complete trajectory converges to \(E\). If it does not belong to that set, then \(x(t)<b/2\) for all sufficiently large \(t\), and there is a finite, trajectory-dependent constant \(C\) such that
\[
\boxed{\displaystyle -\frac{b}{x(t)-b/2}
=t+\frac{2}{b}\log t+C+o(1)\quad(t\to\infty).}
\]
The non-exponential alternative occurs on actual nonstationary solutions near the equilibrium. The asserted contribution is the **explicit logarithmic coefficient and finite constant remainder** beyond the previously established reciprocal \(1/t\) law; global recurrence thresholds, bounded-orbit convergence, and the leading rate are known through an affine-conjugate quadratic flow.

## Scope and relation to an equivalent system

The assumptions are exactly \(b>0\), \(a=-b^2/4\); arbitrary initial data are not assumed to generate bounded, global solutions. The statement is in the original \(x\)-coordinate and original physical time. There is no claim about periodic, chaotic, or other non-equilibrium compact dynamics off the fold.

In fact, for general \(a\) and \(b>0\), the invertible affine map
\[
(X,Y,Z)=(bz-a-bx,\ -a-bx-y-z,\ x)
\]
(with determinant \(b\)) transforms this flow **without time rescaling** to
\[
\dot X=-bY,\qquad \dot Y=X+Z^2,\qquad
\dot Z=-a/b-X/b-Z.
\]
Thus it is a parameter specialization of the Zhao--Lin--Dai modified Sprott-N family \(\dot X=\alpha Y,\ \dot Y=X+Z^2,\ \dot Z=\beta+\gamma X+\delta Z\), with \((\alpha,\beta,\gamma,\delta)=(-b,-a/b,-1/b,-1)\). Its discriminant is \((b^2+4a)/b^2\). The published *Sharp recurrence threshold and critical relaxation in a quadratic chaotic flow* therefore covers the global compact-recurrence classification, bounded-orbit rigidity and the leading critical law \(t(x-b/2)\to-b\). These are context, **not newly claimed findings**. An earlier jerk classification also places Sprott M in the quadratic \(JD_2\) class and gives a sign-based no-chaos criterion. Neither inspected source supplies the explicit \((2/b)\log t\) refinement with a convergent remainder.

## Proof

Set \(u=x-b/2\), \(w=z\), and \(h=y+b^2/4+bu\). The equations at the fold become exactly
\[
\dot u=-w,\qquad\dot w=h,\qquad\dot h=-h-bw-u^2. \tag{1}
\]
The linearization has eigenvalues \(0\) and the two roots of \(\lambda^2+\lambda+b\), both strictly in the left half-plane for \(b>0\). The standard smooth center-manifold and strong-stable-foliation theorems apply. Write a smooth local center manifold as \(w=W(u)\), \(h=H(u)\). Its invariance equations are
\[
W'(u)(-W(u))=H(u),\qquad H'(u)(-W(u))=-H(u)-bW(u)-u^2.
\]
Solving successively through cubic order gives the **coordinate-specific coefficients**
\[
W(u)=-\frac{u^2}{b}+\frac{2u^3}{b^3}+O(u^4),\qquad
H(u)=-\frac{2u^3}{b^2}+O(u^4).
\]
They can also be verified by substituting into the two invariance equations and cancelling all terms through order three. Hence on the center manifold
\[
\dot u=\frac{u^2}{b}-\frac{2u^3}{b^3}+O(u^4).\tag{2}
\]
Every nonconstant center trajectory that remains near and converges to zero in forward time eventually has \(u<0\); such trajectories exist. For them put \(R=-b/u>0\), obtaining
\[
\dot R=1+\frac{2}{bR}+O(R^{-2}).\tag{3}
\]
Equation (3) first yields \(R/t\to1\), then \(R=t+O(\log t)\). Consequently
\[
\frac{d}{dt}\left(R-t-\frac2b\log t\right)
=\frac{2}{b}\left(\frac1R-\frac1t\right)+O(R^{-2})
=O\left(\frac{\log t}{t^2}\right),
\]
which is integrable. The bracket therefore converges to a finite constant, proving the asserted expansion on the center manifold.

For completeness, bounded forward orbits converge to \(E\): the exact identity \(\frac d{dt}(y+z)=-(x-b/2)^2\), boundedness, uniform continuity of \(x-b/2\), and bounded derivatives imply \(x\to b/2\) and \(z=-\dot x\to0\); the stable forced equation \(\dot y+y=-x^2\) then gives \(y\to-b^2/4\). (The global conclusion also follows directly from the previously published affine-conjugate theorem.) Stable-foliation theory gives exponential tracking of each such convergent trajectory by a center-manifold trajectory. If the tracked trajectory is the equilibrium, the original trajectory is in the global strong-stable set; otherwise it is a negative-side orbit satisfying (3). Exponential tracking changes \(-b/u\) by \(o(1)\), since \(u\asymp-1/t\). This establishes the full assertion for all bounded forward-complete trajectories.

## Verification and limits

The supplied `verify.py` checks the exact system transformation (1), the center-manifold cubic invariance coefficients and reciprocal drift (3), as well as the polynomial balance and linearization. An additional independent exact symbolic calculation checked the affine conjugacy with the published quadratic system and reconstructed the same cubic coefficients. Neither finite symbolic test replaces standard center-manifold/stable-foliation theory. The theorem assumes a bounded forward-complete orbit; it does not imply every solution is bounded, and the constant \(C\) depends on the trajectory. The coefficient is specific to the chosen original time and coordinate, not invariant under arbitrary nonlinear reparameterization. A differently worded equivalent earlier asymptotic is a residual priority risk.

## References

1. J. C. Sprott, *Some simple chaotic flows*, Physical Review E **50**, R647--R650 (1994), DOI: 10.1103/PhysRevE.50.R647.
2. R. Eichhorn, S. J. Linz, P. Hänggi, *Transformations of nonlinear dynamical systems to jerky motion and its application to minimal chaotic flows*, Physical Review E **58**, 7151--7164 (1998), DOI: 10.1103/PhysRevE.58.7151; especially the quadratic jerk class \(JD_2\) and model M in Table II.
3. H. Zhao, Y. Lin, Y. Dai, *A New Feigenbaum-Like Chaotic 3D System*, Discrete Dynamics in Nature and Society (2014), article 328143, DOI: 10.1155/2014/328143.
4. *Sharp recurrence threshold and critical relaxation in a quadratic chaotic flow*, published mathematical research record (2026), Resultary/2026, 2026/10/11/SCOPE-sharp-recurrence-threshold-and-critical-relaxation-in-a-quadrati--fbbb7113cf97.
5. J. Carr, *Applications of Centre Manifold Theory*, Springer (1981), for standard local invariant-manifold and stable-foliation results.
