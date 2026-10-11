# Exact centered univalence radius of the Borovikov shear

## Finding

For
\[
M>1,
\]
consider the explicit harmonic map
\[
F_M(z)
=
z+i(M-1)u_*(z),
\]
where
\[
u_*(z)
=
\frac{2}{\pi}
\operatorname{Arg}\!\left(
\frac{1-z^2}{1+z^2}
\right)
\]
uses the branch of the argument in
\[
(-\pi/2,\pi/2).
\]

Let
\[
r_M\in(0,1)
\]
be the unique solution of
\[
8(M-1)r_M
=
\pi(1-r_M^4).
\]

Then
\[
r_M
\]
is the exact largest centered univalence radius of this map:
\[
F_M
\text{ is injective on }
\mathbb D_{r_M},
\]
whereas for every
\[
r>r_M
\]
the restriction of
\[
F_M
\]
to
\[
\mathbb D_r
\]
cannot be locally univalent everywhere.

The stronger pointwise statement is
\[
\min_{|z|\le r}
J_{F_M}(z)
=
1-
\frac{8(M-1)}{\pi}
\frac{r}{1-r^4},
\qquad
0\le r<1.
\]
For every
\[
r>0,
\]
the minimum is attained uniquely at the positive real point
\[
z=r.
\]

Thus
\[
J_{F_M}(z)>0
\qquad
(|z|<r_M),
\]
and
\[
J_{F_M}(r_M)=0.
\]
There is no earlier off-axis Jacobian collapse.

Moreover, positivity of the Jacobian in the centered disk upgrades local univalence to global injectivity for this special shear: the real coordinate is unchanged by
\[
F_M,
\]
and the imaginary coordinate is strictly increasing on every vertical slice.

## Assumptions and scope

The unit disk is
\[
\mathbb D=\{z\in\mathbb C:|z|<1\},
\]
and
\[
\mathbb D_r=\{z\in\mathbb C:|z|<r\}.
\]

The map
\[
F_M
\]
is the explicit counterexample family introduced in the cited 2026 work on the harmonic Landau radius. The source proves that
\[
F_M(0)=0,
\qquad
\lambda_{F_M}(0)=1,
\qquad
|F_M(z)|<M,
\]
and locates a real-axis Jacobian zero at
\[
r_M.
\]

The present theorem concerns only this explicit family and its centered disks. It does not determine the universal harmonic Landau radius and does not claim that every harmonic Landau extremizer is a vertical shear.

The conclusion is valid for every
\[
M>1,
\]
whether or not
\[
r_M
\]
lies inside the classical holomorphic Landau disk.

## Proof

Set
\[
W(z)
=
\log\!\left(
\frac{1-z^2}{1+z^2}
\right),
\]
using the analytic logarithm whose imaginary part lies in
\[
(-\pi/2,\pi/2).
\]
The quotient has positive real part on
\[
\mathbb D,
\]
so this branch is analytic there. By definition,
\[
u_*(z)
=
\frac{2}{\pi}\operatorname{Im}W(z).
\]

Differentiation gives
\[
W'(z)
=
-\frac{4z}{1-z^4}.
\]
If
\[
W=P+iQ,
\]
then the Cauchy--Riemann equations give
\[
Q_y=P_x=\operatorname{Re}W'(z).
\]
Therefore
\[
(u_*)_y(z)
=
-\frac{8}{\pi}
\operatorname{Re}\!\left(
\frac{z}{1-z^4}
\right).
\]

Writing
\[
z=x+iy,
\]
the shear has the real-coordinate form
\[
F_M(x+iy)
=
x
+
i\bigl(y+(M-1)u_*(x,y)\bigr).
\]
Its Jacobian is consequently
\[
J_{F_M}(z)
=
1-
\frac{8(M-1)}{\pi}
\operatorname{Re}\!\left(
\frac{z}{1-z^4}
\right).
\]

Fix
\[
0<r<1.
\]
For
\[
|z|\le r,
\]
\[
\operatorname{Re}\!\left(
\frac{z}{1-z^4}
\right)
\le
\left|
\frac{z}{1-z^4}
\right|
\le
\frac{|z|}{1-|z|^4}
\le
\frac{r}{1-r^4}.
\]
The last quantity is strictly increasing with
\[
r.
\]

At
\[
z=r,
\]
all three inequalities are equalities. If
\[
r>0,
\]
equality in the triangle estimate
\[
|1-z^4|\ge1-|z|^4
\]
forces
\[
|z|=r
\]
and
\[
z^4=r^4.
\]
Among the four possibilities
\[
z\in\{r,-r,ir,-ir\},
\]
only
\[
z=r
\]
makes
\[
z/(1-z^4)
\]
positive real. Hence
\[
\max_{|z|\le r}
\operatorname{Re}\!\left(
\frac{z}{1-z^4}
\right)
=
\frac{r}{1-r^4},
\]
uniquely at
\[
z=r.
\]
This proves the exact Jacobian minimum
\[
\min_{|z|\le r}
J_{F_M}(z)
=
1-
\frac{8(M-1)}{\pi}
\frac{r}{1-r^4}.
\]

The defining equation for
\[
r_M
\]
is equivalent to
\[
\frac{8(M-1)}{\pi}
\frac{r_M}{1-r_M^4}
=
1.
\]
Since
\[
r/(1-r^4)
\]
is strictly increasing,
\[
J_{F_M}(z)>0
\]
for every
\[
|z|<r_M,
\]
while
\[
J_{F_M}(r_M)=0.
\]

It remains to prove global injectivity in
\[
\mathbb D_{r_M}.
\]
Suppose
\[
F_M(z_1)=F_M(z_2),
\qquad
z_j=x_j+iy_j.
\]
Because
\[
\operatorname{Re}F_M(x+iy)=x,
\]
we have
\[
x_1=x_2=x.
\]
For this fixed
\[
x,
\]
define
\[
Y_x(y)
=
y+(M-1)u_*(x,y).
\]
On the connected vertical slice
\[
\{y:x^2+y^2<r_M^2\},
\]
\[
Y_x'(y)
=
1+(M-1)(u_*)_y(x,y)
=
J_{F_M}(x,y)
>
0.
\]
Hence
\[
Y_x
\]
is strictly increasing, so
\[
Y_x(y_1)=Y_x(y_2)
\]
implies
\[
y_1=y_2.
\]
Thus
\[
z_1=z_2,
\]
and
\[
F_M
\]
is injective on
\[
\mathbb D_{r_M}.
\]

Finally, every centered disk
\[
\mathbb D_r
\]
with
\[
r>r_M
\]
contains the point
\[
r_M.
\]
At that point the Jacobian vanishes. By Lewy's theorem, a one-to-one harmonic map must have nonvanishing Jacobian at every interior point. Therefore
\[
F_M
\]
cannot be univalent on any such larger disk. This establishes the exact centered univalence radius.

## Verification

The critical derivative was reconstructed from the analytic logarithm rather than inferred from the real-axis formula:
\[
(u_*)_y(z)
=
-\frac{8}{\pi}
\operatorname{Re}\!\left(
\frac{z}{1-z^4}
\right).
\]
Restricting this identity to
\[
z=x>0
\]
recovers the source formula
\[
(u_*)_y(x,0)
=
-\frac{8x}{\pi(1-x^4)}.
\]

The disk maximum was checked by two independent descriptions. The elementary modulus estimate gives
\[
\operatorname{Re}\!\left(
\frac{z}{1-z^4}
\right)
\le
\frac{r}{1-r^4},
\]
while the convergent expansion
\[
\frac{z}{1-z^4}
=
\sum_{n=0}^{\infty}z^{4n+1}
\]
shows directly why positive real alignment is the extremizing direction.

Global injectivity uses no general shear theorem. It follows from the special triangular coordinate structure
\[
F_M(x+iy)
=
x+iY_x(y)
\]
and strict positivity of
\[
Y_x'(y).
\]

The only obstruction used beyond the explicit calculation is Lewy's classical theorem that an injective planar harmonic map has nonvanishing Jacobian.

## Relationship to prior work

Borovikov's counterexample paper identifies the real-axis zero
\[
r_M
\]
and uses it to prove failure of local univalence. Its proof evaluates the Jacobian only on the real axis and does not state that the Jacobian stays positive throughout the whole centered disk before
\[
r_M.
\]
It also does not prove that the map is globally injective on that disk.

The result here completes the geometry of the explicit counterexample family: the first Jacobian collapse over every centered disk occurs exactly on the positive real axis, and the triangular shear structure rules out global collisions before that collapse.

The original Liu--Luo--Luo work supplies the conjectural Landau-radius setting, while Lewy's theorem supplies the classical local obstruction at a vanishing Jacobian. Neither source contains the full centered-radius classification of this explicit 2026 shear.

Targeted searches for the map
\[
F_M,
\]
its real-axis fold equation, off-axis Jacobian collapse, and exact centered univalence radius did not locate a published statement implying this classification.

## Limitations

The theorem is exact for the explicit family
\[
F_M
\]
only. It does not determine the universal harmonic Landau radius at finite
\[
M.
\]

The phrase “largest centered univalence radius” refers to disks centered at the origin. No maximality is asserted among arbitrary simply connected subdomains.

The proof exploits the fact that the real coordinate of
\[
F_M
\]
is exactly
\[
x.
\]
A general harmonic perturbation need not admit the same vertical-fiber argument.

## References

1. M. Borovikov, *A Counterexample to the Liu-Luo-Luo Conjecture on the Harmonic Landau Radius*, arXiv:2609.39676v1, first posted 30 September 2026.
2. M.-S. Liu, L.-F. Luo, and X. Luo, *Landau--Bloch type theorems for strongly bounded harmonic mappings*, Monatshefte für Mathematik 191 (2020), 175--185.
3. H. Lewy, *On the non-vanishing of the Jacobian in certain one-to-one mappings*, Bulletin of the American Mathematical Society 42 (1936), 689--692.
