# Sharp Mahler profile of ball–bipole hulls and its Gaussian crossover

## Finding

Let \(d\ge2\) be an integer, let \(B_2^d\) be the Euclidean unit ball, and let \(e\) be a fixed unit vector. For \(a\ge1\), define the origin-symmetric *ball–bipole hull*
\[
K_{d,a}=\operatorname{conv}\bigl(B_2^d\cup\{-ae,ae\}\bigr),\qquad t=1/a.
\]
Write \(\kappa_j=\pi^{j/2}/\Gamma(1+j/2)\), and define, for \(0<t\le1\),
\[
I_d(t)=\int_0^t(1-u^2)^{(d-1)/2}\,du,\quad
J_d(t)=\frac{(1-t^2)^{(d+1)/2}}{dt}.
\]
Its Santaló volume product, with the polar taken about the origin, is exactly
\[
\boxed{P_d(t)=\operatorname{vol}_d(K_{d,1/t})\operatorname{vol}_d(K_{d,1/t}^{\circ})
=4\kappa_{d-1}^{\,2}I_d(t)\bigl(I_d(t)+J_d(t)\bigr).}
\]
For every fixed dimension this is strictly increasing on \(0<t\le1\), with sharp range
\[
\frac{4\kappa_{d-1}^{\,2}}{d}<P_d(t)\le\kappa_d^2;
\]
the upper equality holds exactly at \(a=1\), while the lower endpoint is approached only as \(a\to\infty\). Consequently, one exact volume-product measurement uniquely reconstructs the pole ratio \(a\).

There are sharp endpoint expansions
\[
P_d(t)=\frac{4\kappa_{d-1}^{\,2}}d+
\frac{4\kappa_{d-1}^{\,2}(d-1)}{3d}\,t^2+O_d(t^4)
\quad(t\downarrow0)
\]
and, with \(h=1-t\),
\[
\kappa_d^2-P_d(1-h)
=C_d h^{(d+1)/2}+o_d\bigl(h^{(d+1)/2}\bigr),\qquad
C_d=\frac{2^{(d+1)/2}\,2\kappa_d\kappa_{d-1}(d-1)}{d(d+1)}>0.
\]
Thus the extended inverse on the closed volume-product range is optimally Hölder of exponent
\(\min\{1/2,\,2/(d+1)\}\); its individual endpoint exponents are \(1/2\) and \(2/(d+1)\), respectively.

For each fixed \(\tau>0\), put \(t=\tau/\sqrt d\). Writing
\(H(\tau)=\int_0^\tau e^{-u^2/2}\,du\), the high-dimensional crossover is
\[
\boxed{\lim_{d\to\infty}\frac{P_d(\tau/\sqrt d)}{\kappa_d^2}
=\frac2\pi H(\tau)\left(H(\tau)+\frac{e^{-\tau^2/2}}\tau\right).}
\]
This limit increases strictly from \(2/\pi\) to \(1\). For each fixed \(t>0\), however, the normalized product tends to \(1\) as \(d\to\infty\). Therefore the limits \(t\downarrow0\) and \(d\to\infty\) do not commute.

## Assumptions and scope

All bodies are nondegenerate Euclidean convex bodies in dimension \(d\ge2\). We use Lebesgue volume. The polar of a convex body \(K\) containing the origin in its interior is \(K^\circ=\{y:\langle x,y\rangle\le1\text{ for all }x\in K\}\). Central symmetry makes the origin its unique Santaló center, so the displayed origin-polar product is the Santaló volume product. The parameter \(a\) is the pole distance divided by the inscribed ball radius; because the ball radius is normalized to one, \(a\ge1\). The endpoint \(t=0\) is only a limiting parameter, not a bounded convex body.

## Proof

**1. Exact duality and volumes.** The polar of a convex hull is the intersection of polars. Because the polar of the unit ball is itself and \(([-ae,ae])^\circ=\{y:|\langle y,e\rangle|\le1/a\}\),
\[
K_{d,1/t}^\circ=B_2^d\cap\{y:|\langle y,e\rangle|\le t\}.
\]
The polar's axial slices are \((d-1)\)-balls of radius \(\sqrt{1-z^2}\). Fubini's theorem gives \(\operatorname{vol}_d(K^\circ)=2\kappa_{d-1}I_d(t)\).

On the positive axial half of \(K\), the round boundary follows the unit sphere until the tangency coordinate \(z=t\). Thereafter the meridian is the straight segment from the contact point \((t,\sqrt{1-t^2})\) to the pole \((1/t,0)\). Its radial cross-section is therefore
\[
r(z)=\begin{cases}\sqrt{1-z^2},&0\le z\le t,\\
(1-tz)/\sqrt{1-t^2},&t\le z\le1/t.
\end{cases}
\]
Integrating \(r(z)^{d-1}\) over the two symmetric halves yields
\[
\operatorname{vol}_d(K)=2\kappa_{d-1}\left(I_d(t)+
\int_t^{1/t}\left(\frac{1-tz}{\sqrt{1-t^2}}\right)^{d-1}dz\right)
=2\kappa_{d-1}(I_d(t)+J_d(t)).
\]
The product formula follows. At \(t=1\) the cone contribution is zero and \(2\kappa_{d-1}I_d(1)=\kappa_d\).

**2. Strict monotonicity.** Set \(f(t)=(1-t^2)^{(d-1)/2}\). For \(0<t<1\), direct differentiation gives
\[
I_d'(t)=f(t),\qquad J_d'(t)=-f(t)\left(1+\frac1{dt^2}\right).
\]
Consequently
\[
\frac{P_d'(t)}{4\kappa_{d-1}^{\,2}}=
\frac{f(t)}{dt^2}\,G_d(t),\quad
G_d(t)=t(1-t^2)^{(d+1)/2}-(1-dt^2)I_d(t).
\]
Here \(G_d(0+)=0\) and
\[
G_d'(t)=2t\left(dI_d(t)-t f(t)\right)>0.
\]
Indeed \(f\) decreases, whence \(I_d(t)\ge t f(t)\), and \(d\ge2\). This proves strict increase, including at the continuous endpoint \(t=1\). Expanding at \(t=0\) yields \(I_d(t)=t-(d-1)t^3/6+O_d(t^5)\) and \(J_d(t)=(dt)^{-1}-(d+1)t/(2d)+O_d(t^3)\), giving the lower limit and quadratic coefficient.

**3. Upper endpoint and inverse regularity.** Let \(h=1-t\). Since \(1-u^2=2(1-u)+O((1-u)^2)\),
\[
I_d(1)-I_d(1-h)=\frac{2^{(d+1)/2}}{d+1}h^{(d+1)/2}+o_d(h^{(d+1)/2}),
\]
while \(J_d(1-h)=2^{(d+1)/2}h^{(d+1)/2}/d+o_d(h^{(d+1)/2})\). Substitution into the exact product, using \(I_d(1)=\kappa_d/(2\kappa_{d-1})\), proves the constant \(C_d\). Both endpoint constants are nonzero, forcing inverse exponents \(1/2\) and \(2/(d+1)\). On compact interior subintervals, \(P_d'\) is positive and continuous, so its inverse is Lipschitz there. Combining interior and endpoint neighborhoods gives the asserted optimal global Hölder exponent. The exponents cannot be improved at the corresponding endpoints because of the matching asymptotics.

**4. Gaussian dimension transition.** For fixed \(\tau>0\), uniformly on \(0\le u\le\tau\),
\(\bigl(1-u^2/d\bigr)^{(d-1)/2}\to e^{-u^2/2}\). Thus
\[
\sqrt d\,I_d(\tau/\sqrt d)\to H(\tau),\qquad
\sqrt d\,J_d(\tau/\sqrt d)\to e^{-\tau^2/2}/\tau.
\]
The standard gamma ratio gives \(\kappa_{d-1}^{\,2}/\kappa_d^2\sim d/(2\pi)\), proving the crossover formula. Its derivative has the sign of
\[
B(\tau)=(\tau^2-1)H(\tau)+\tau e^{-\tau^2/2}.
\]
Since \(B(0+)=0\) and \(B'(\tau)=2\tau H(\tau)>0\), the crossover is strictly increasing. Its endpoints follow from \(H(\tau)\sim\tau\) at zero and \(H(\tau)\to\sqrt{\pi/2}\) at infinity. At each fixed \(t>0\), the Gaussian mass outside \([0,t]\) vanishes exponentially in \(d\), the cone contribution is exponentially small, and \(I_d(t)\sim\kappa_d/(2\kappa_{d-1})\). The normalized product therefore tends to one. In contrast, taking \(t\downarrow0\) first gives \(4\kappa_{d-1}^2/(d\kappa_d^2)\to2/\pi\), establishing noncommutation.

## Verification

A standalone Python 3 standard-library program, `check.py`, is provided. It exactly verifies the three-dimensional sample \(P_3(1/2)=55\pi^2/36\) using rational arithmetic, compares direct planar polygonal hull calculations with independent polar-strip integration, tests numerical monotonicity and both sharp endpoint coefficients, and checks the high-dimensional Gaussian crossover by direct quadrature. Running `python3 check.py` prints `ALL_CHECKS_PASSED`. These tests do not replace the all-dimensional analytic proof above.

## Relationship to prior work

The volume product, central polarity, ellipsoidal upper bound, and shadow-system convexity principles are classical or established; see Fradelizi–Meyer–Zvavitch (2023), Meyer–Reisner (2018), and Meyer–Reisner (2006). The existing inequalities do not by themselves give the parameter-explicit ball–bipole product, its strict one-parameter inverse, the unequal endpoint inverse exponents, or the Gaussian scale transition. A ball thickened by a **Minkowski sum** with a segment is a different family from the **convex hull** with two poles studied here; the two operations have different axial sections and different fixed-aspect high-dimensional behavior. Historical priority for this specialized family has not been independently established.

## Limitations

No claim is made for nonsymmetric or off-axis pole configurations, arbitrary ambient norms, or measurements with noise. For dimension-specific extremely small deficits from the ball, floating-point evaluation of the difference can suffer cancellation, so rigorous asymptotics come from the proof. The Gaussian statement is pointwise for fixed positive \(\tau\), not a dimension-uniform error bound. Although the literature comparison did not reveal this full profile, older special-body formulas may exist and warrant further human bibliographic review. Independent proof audit has not been performed.

## References

1. M. Fradelizi, M. Meyer and A. Zvavitch, *Volume Product*, arXiv:2301.06131 (first public version January 15, 2023), https://arxiv.org/abs/2301.06131.
2. M. Meyer and S. Reisner, *Ellipsoids are the only local maximizers of the volume product*, arXiv:1812.11607 (2018), https://arxiv.org/abs/1812.11607.
3. M. Meyer and S. Reisner, *Shadow systems and volumes of polar convex bodies*, arXiv:math/0606305 (2006), https://arxiv.org/abs/math/0606305.
