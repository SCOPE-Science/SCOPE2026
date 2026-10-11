# Exact brightness profile of the cubic threefold-projection exception
## Finding
Let \(K_\varepsilon\subset\mathbb R^3\) have support function
\[
h_\varepsilon(u)=1+\varepsilon u_1u_2u_3,\qquad u\in S^2,
\]
for any real \(\varepsilon\) for which this is a support function. Myroshnychenko--Ryabogin--Saroglou prove that this family gives the exceptional non-spherical constant-width examples whose every planar projection has threefold rotational symmetry after translation. For every unit normal \(n=(n_1,n_2,n_3)\), its brightness is
\[
b_{K_\varepsilon}(n):=\operatorname{{area}}(K_\varepsilon\mid n^\perp)
=\pi-\frac{{\pi\varepsilon^2}}4\prod_{{i=1}}^3(1-n_i^2).
\]
Hence
\[
\pi\left(1-\frac{{2\varepsilon^2}}{{27}}\right)\le b_{{K_\varepsilon}}(n)\le\pi.
\]
The upper endpoint occurs exactly for coordinate-axis normals, where the projection is the unit disk. The lower endpoint occurs exactly when \(|n_1|=|n_2|=|n_3|=1/\sqrt3\); modulo antipodal identification these are the four body-diagonal projection planes.

## Assumptions and scope
The statement is conditional only on \(h_\varepsilon\) being a support function. The source proves this for all sufficiently small \(|\varepsilon|\) (and explicitly states the positive-parameter case in its theorem). No use is made here of any larger sharp convexity interval. Projection area is ordinary Euclidean two-dimensional area, and \(n\) is always a unit vector. Opposite normals define the same projection plane.

## Proof
Fix \(n\in S^2\) and an oriented orthonormal basis \(e_1,e_2\) of \(n^\perp\). Parametrize its unit circle by
\[
u(\theta)=e_1\cos\theta+e_2\sin\theta.
\]
The source proves that the restriction of \(H(u)=u_1u_2u_3\) to every such circle contains only first and third Fourier modes. Put \(z=e_1-i e_2\). Since
\[
u(\theta)=\frac12\left(ze^{{i\theta}}+\overline z e^{{-i\theta}}\right),
\]
the coefficient of \(e^{{3i\theta}}\) in \(H(u(\theta))\) is \(z_1z_2z_3/8\). Writing the third harmonic as
\[
C\cos3\theta+D\sin3\theta,
\]
its squared amplitude is therefore
\[
R^2:=C^2+D^2=\frac1{16}|z_1z_2z_3|^2.
\]
Because \(e_1,e_2,n\) is an orthonormal basis,
\[
|z_i|^2=e_{{1,i}}^2+e_{{2,i}}^2=1-n_i^2,
\]
so
\[
R^2=\frac1{16}\prod_{{i=1}}^3(1-n_i^2).
\]
The first harmonic is exactly a translation of the planar projection and does not affect area. After translating, its support function is
\[
p(\theta)=1+\varepsilon R\cos(3\theta-\phi)
\]
for some phase \(\phi\). The planar support-function area identity gives
\[
\operatorname{{area}}=\frac12\int_0^{{2\pi}}\left(p(\theta)^2-p'(\theta)^2\right)d\theta
=\pi-4\pi\varepsilon^2R^2,
\]
which is the displayed brightness formula.

For the extremal directions put \(a_i=n_i^2\). Then \(a_i\ge0\), \(a_1+a_2+a_3=1\), and
\[
\prod_{{i=1}}^3(1-a_i)\le\left(\frac{(1-a_1)+(1-a_2)+(1-a_3)}3\right)^3=\left(\frac23\right)^3=\frac8{27}.
\]
Equality holds exactly at \(a_1=a_2=a_3=1/3\). The product has minimum zero exactly when one \(a_i=1\), i.e. for a coordinate-axis normal. In that case \(u_1u_2u_3\) vanishes identically on the corresponding coordinate plane, so the projected support function is exactly \(1\) and the projection is the unit disk.

## Verification
A symbolic checker expands the diagonal restriction, recovers third-harmonic amplitude \(R^2=1/54\), integrates the planar area formula to \(\pi(1-2\varepsilon^2/27)\), and verifies the general amplitude identity on several exact orthonormal frames. These calculations are supplementary checks; the proof above establishes the identity for every direction.

## Relationship to prior work
Myroshnychenko--Ryabogin--Saroglou identify \(u_1u_2u_3\) as the cubic exception, prove that every great-circle restriction has only first and third harmonics, and show that \(1+\varepsilon u_1u_2u_3\) yields smooth strictly convex non-spherical constant-width bodies with threefold-symmetric planar projections for sufficiently small \(|\varepsilon|\). Their inspected argument stops at the symmetry statement and does not compute the directional projection areas.

General brightness-function literature studies the map \(n\mapsto\operatorname{{area}}(K\mid n^\perp)\), including uniqueness and stability questions, but the checked sources do not state this explicit profile for the cubic exception. Recent mixed-volume work on constant-width bodies gives global and averaged projection-defect identities; it does not imply the directional product formula above without the present circle-level computation.

## Limitations
The result concerns the specific canonical cubic family \(1+\varepsilon u_1u_2u_3\), not every threefold-projection exception. It does not determine the largest admissible \(|\varepsilon|\), and it makes no reconstruction or stability claim from brightness data. The formula depends on the fixed coordinate axes appearing in the cubic harmonic.

## References
1. S. Myroshnychenko, D. Ryabogin, C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192v1 (2026).
2. S. Campi, R. J. Gardner, P. Gronchi, M. Kiderlen, *Lightness functions*, Advances in Mathematics 231 (2012), 3118--3146, DOI 10.1016/j.aim.2012.08.015.
3. M. Zwierzyński, *Mixed Volumes, the Wigner Caustic, and Isoperimetric Inequalities*, arXiv:2608.11068v1 (2026).
