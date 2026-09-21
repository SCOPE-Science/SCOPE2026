# Sharp flat-torus systolic profile by modular distance

## Result

Let
\[
\mathcal M_{\rm flat}=\mathrm{PSL}_2(\mathbb Z)\backslash\mathbb H
\]
be the moduli orbifold of oriented flat two-tori up to similarity, equipped with the quotient of the curvature \(-1\) hyperbolic metric
\[
ds_{\mathbb H}^2=\frac{dx^2+dy^2}{y^2}.
\]
Let \(H\in\mathcal M_{\rm flat}\) be the hexagonal class, represented by
\[
\rho=e^{\pi i/3}=\frac12+\frac{\sqrt3}{2}i.
\]
For a flat torus \(T\), write
\[
\operatorname{SR}(T)=\frac{\operatorname{sys}(T)^2}{\operatorname{area}(T)},
\qquad
q(T)=\frac{\sqrt3}{2}\operatorname{SR}(T)\in(0,1],
\]
and let
\[
d=d_{\mathcal M_{\rm flat}}(T,H).
\]

Then the complete sharp profile at fixed modular distance is
\[
\boxed{e^{-d}\le q(T)\le M(d),}
\]
where
\[
\boxed{
M(d)=
\begin{cases}
\dfrac{3e^{-d}+e^d}{4},
&0\le d\le \log\sqrt3,\\[1.2ex]
\dfrac{1}{\cosh d+\sqrt{\sinh^2d-\frac13}},
&d\ge \log\sqrt3.
\end{cases}}
\]
Every value in this interval occurs for a flat torus at distance exactly \(d\).

Equivalently, for a prescribed normalized systolic ratio \(q\in(0,1]\), the possible distances to the hexagonal torus form the exact interval
\[
\boxed{-\log q\le d\le D(q),}
\]
where
\[
\boxed{
D(q)=
\begin{cases}
\log\!\left(2q-\sqrt{4q^2-3}\right),
&\dfrac{\sqrt3}{2}\le q\le1,\\[1.2ex]
\operatorname{arcosh}\!\left(\dfrac{3+4q^2}{6q}\right),
&0<q\le\dfrac{\sqrt3}{2}.
\end{cases}}
\]

The upper envelope has a geometric phase transition at
\[
d_0=\log\sqrt3,
\]
the modular distance from the hexagonal torus to the square torus. For \(d\le d_0\), the largest systolic ratio at fixed distance is attained by the rhombic family \(|\tau|=1\). For \(d\ge d_0\), it is attained by the rectangular family \(\operatorname{Re}\tau=0\). The lower envelope is attained by the reduced-boundary family \(\operatorname{Re}\tau=1/2\).

Near the hexagonal torus,
\[
M(d)=1-\frac d2+\frac{d^2}{2}-\frac{d^3}{12}+O(d^4).
\]
Thus the optimal Loewner deficit on the flat-torus moduli orbifold is linear, rather than quadratic, in hyperbolic distance:
\[
1-q(T)\ge \frac d2+O(d^2).
\]
The linear cusp reflects the fact that the systolic ratio is the minimum of several lattice-vector length functions meeting at the order-three orbifold point.

## Proof

### 1. Reduced coordinates and the systolic ratio

Represent a similarity class by
\[
T_\tau=\mathbb C/(\mathbb Z+\tau\mathbb Z),\qquad \tau=x+iy\in\mathbb H.
\]
Use the standard modular fundamental domain
\[
F=\{\tau:\ |x|\le1/2,\ |\tau|\ge1\}.
\]
For \(\tau\in F\), the shortest nonzero vector of \(\mathbb Z+\tau\mathbb Z\) has length \(1\), while the covolume is \(y\). Hence
\[
\operatorname{SR}(T_\tau)=\frac1y,
\qquad
q(T_\tau)=\frac{\sqrt3}{2y}.
\tag{1}
\]

The reflection \(x\mapsto-x\) preserves both the systolic ratio and distance to the hexagonal class, so it is enough to work in the half-domain
\[
F_+=\{0\le x\le1/2,\ x^2+y^2\ge1\}.
\]
This is the \((2,3,\infty)\) hyperbolic Coxeter chamber with vertices \(i,\rho,\infty\). The modular tessellation shows that, for \(\tau\in F_+\), the nearest lift of the order-three orbifold point is \(\rho\). Therefore
\[
d_{\mathcal M_{\rm flat}}([\,\tau\,],H)=d_{\mathbb H}(\tau,\rho).
\tag{2}
\]
One way to see the nearest-lift assertion is to reflect the chamber in its sides. The side opposite the type-three vertex is the perpendicular bisector between the adjacent type-three vertices; crossing a gallery of chambers toward any other type-three vertex crosses such a bisector. Thus the chamber lies in the Voronoi cell of its type-three vertex.

### 2. Hyperbolic circles about the hexagonal point

Put \(y_0=\sqrt3/2\). The upper-half-plane distance formula gives
\[
\cosh d
=
1+\frac{(x-\frac12)^2+(y-y_0)^2}{2yy_0}.
\]
After rearrangement, the hyperbolic circle of radius \(d\) about \(\rho\) is the Euclidean circle
\[
\left(x-\frac12\right)^2
+\left(y-y_0\cosh d\right)^2
=
y_0^2\sinh^2d.
\tag{3}
\]
By (1), maximizing or minimizing the systolic ratio on this circle is equivalent to minimizing or maximizing \(y\) on its intersection with \(F_+\).

The largest feasible \(y\) is always the upper intersection with \(x=1/2\):
\[
y_{\max}=y_0(\cosh d+\sinh d)=y_0e^d.
\]
Consequently
\[
q_{\min}(d)=\frac{y_0}{y_{\max}}=e^{-d}.
\tag{4}
\]

### 3. The upper envelope before the square torus

The hyperbolic distance from \(\rho\) to \(i\) along the geodesic \(|\tau|=1\) is
\[
d_0=\int_{\pi/3}^{\pi/2}\frac{d\theta}{\sin\theta}
=\log\sqrt3.
\tag{5}
\]
For \(0\le d\le d_0\), the lowest feasible point of (3) lies on \(|\tau|=1\). Write it as \(\tau=e^{i\theta}\) with \(\pi/3\le\theta\le\pi/2\). Along this geodesic,
\[
d=\log\!\left(\sqrt3\tan\frac{\theta}{2}\right),
\]
so
\[
\tan\frac{\theta}{2}=\frac{e^d}{\sqrt3},
\qquad
y_{\min}=\sin\theta
=\frac{2\sqrt3\,e^d}{3+e^{2d}}.
\]
Therefore
\[
q_{\max}(d)
=\frac{y_0}{y_{\min}}
=\frac{3e^{-d}+e^d}{4}.
\tag{6}
\]

### 4. The upper envelope after the square torus

For \(d\ge d_0\), the circle (3) reaches the boundary \(x=0\). Its lower Euclidean branch is outside \(F_+\), so the first feasible point is the upper intersection with \(x=0\):
\[
y_{\min}
=
\frac12\left(
\sqrt3\cosh d+\sqrt{3\sinh^2d-1}
\right).
\]
Hence
\[
q_{\max}(d)
=
\frac{1}{\cosh d+\sqrt{\sinh^2d-\frac13}}.
\tag{7}
\]
Equations (6) and (7) agree at \(d_0=\log\sqrt3\), where the extremal torus is square.

For every \(d\), the feasible part of the circle (3) in \(F_+\) is a connected arc. Since \(q=y_0/y\) is continuous, every value between the two endpoint extrema occurs. This proves the fixed-distance profile.

### 5. Exact inverse profile

The function \(M(d)\) is strictly decreasing from \(1\) to \(0\). Inverting its first branch gives
\[
e^d=2q-\sqrt{4q^2-3}
\]
for \(\sqrt3/2\le q\le1\), which is the first branch of \(D(q)\).

On the second branch the extremizer is \(\tau=iy\). Since \(q=y_0/y\), one has \(y=\sqrt3/(2q)\), while direct use of the hyperbolic distance formula gives
\[
\cosh d=\frac{y^2+1}{\sqrt3\,y}
=\frac{3+4q^2}{6q}.
\]
This gives the second branch of \(D(q)\). Finally, (4) is equivalent to \(d\ge-\log q\). All bounds are attained by the boundary families already identified.

## Relation to prior work

Loewner's classical torus inequality gives
\[
\operatorname{SR}(T)\le\frac{2}{\sqrt3},
\]
with equality at the hexagonal flat torus; the first published reference is Pu's 1952 paper. Horowitz, K. Katz and M. Katz later obtained an isosystolic defect involving the variance of the conformal factor for a general Riemannian torus. That remainder measures nonflatness inside a fixed conformal description and is different from the shape-moduli distance considered here.

Fortier Bourque, Martínez-Granado and Vargas Pallete explicitly identify flat-torus similarity moduli with \(\mathbb H/\mathrm{PSL}_2(\mathbb Z)\), record that for reduced \(\tau\) the systolic ratio is \(1/\operatorname{Im}\tau\), and note the unique strict maximum at the hexagonal class. Those facts are the direct starting data for the present profile.

Searches under flat-torus systolic stability, Hermite-invariant stability, modular-surface systole, hyperbolic distance to the hexagonal lattice, and equivalent binary-quadratic-form language did not locate the two-sided fixed-distance profile, its exact inverse, or the rhombic-to-rectangular phase transition above. The originality claim is therefore only to the best of our knowledge. Because the derivation is elementary once reduced modular coordinates are used, equivalent older geometry-of-numbers or modular-surface folklore remains a material possibility.

## Limitations

- The theorem concerns flat two-tori up to similarity, not arbitrary Riemannian metrics on the torus.
- Distance uses the curvature \(-1\) quotient hyperbolic metric on the modular orbifold. Other normalizations, including conventions for the genus-one Teichmüller metric, rescale the distance.
- The result controls the systolic ratio as a function of moduli distance; it does not bound other geometric quantities such as diameter or covering radius.
- Originality is asserted only to the best of our knowledge, with residual folklore risk from classical reduction theory and the geometry of numbers.

## Reproducibility

Starting with a reduced parameter \(\tau=x+iy\), check \(\operatorname{SR}=1/y\). Use the standard upper-half-plane distance formula to derive (3), then optimize the vertical coordinate on the circle subject to \(0\le x\le1/2\) and \(x^2+y^2\ge1\). The three boundary pieces \(x=1/2\), \(|\tau|=1\), and \(x=0\) give all sharp families. No numerical computation is required for the proof.

## References

1. P. M. Pu, *Some inequalities in certain nonorientable Riemannian manifolds*, Pacific J. Math. 2 (1952), 55--71. https://doi.org/10.2140/pjm.1952.2.55
2. C. Horowitz, K. Usadi Katz, M. G. Katz, *Loewner's torus inequality with isosystolic defect*, arXiv:0803.0690. https://arxiv.org/abs/0803.0690
3. M. Fortier Bourque, D. Martínez-Granado, F. Vargas Pallete, *The extremal length systole of the Bolza surface*, Annales Henri Lebesgue 7 (2024), 1409--1455. https://doi.org/10.5802/ahl.223
4. D. Calegari, J. Louwsma, *Immersed surfaces in the modular orbifold*, arXiv:1003.1532. https://arxiv.org/abs/1003.1532
