# Collapse of the auxiliary strong-rotundity index and the affine-regular hexagon profile
## Finding
Let \(X\) be a real Banach space and
\[
\Pi_X=\{(x,x^*)\in S_X\times S_{X^*}:x^*(x)=1\}.
\]
García-Pacheco's local index of strong rotundity is
\[
\eta_X(\epsilon,(x,x^*))
=
d\!\left((x^*)^{-1}(\{1\}),\,B_X\setminus U_X(x,\epsilon)\right),
\qquad
0\le\epsilon\le2,
\]
and the auxiliary index introduced in the same work is
\[
\upsilon_X(\epsilon,(x,x^*))
=
\inf\left\{
1-x^*(y):
\|y\|\le1,\ \|x-y\|\ge\epsilon
\right\}.
\]
These two local indices always coincide:
\[
\boxed{
\eta_X(\epsilon,(x,x^*))
=
\upsilon_X(\epsilon,(x,x^*))
}.
\]
Thus the auxiliary quantity does not merely lie below the strong-rotundity index; it is an exact scalar representation of it.

If Birkhoff orthogonality is symmetric on \(X\), then
\[
\eta_X(\epsilon)
\ge
\max\{0,\epsilon-1\},
\qquad
0\le\epsilon\le2.
\]
In particular this applies to every Radon plane.

For the affine-regular hexagonal plane
\[
H=(\mathbb R^2,N),
\qquad
N(s,t)=\max\{|s|,|t|,|s-t|\},
\]
the estimate is sharp for the entire parameter interval:
\[
\boxed{
\eta_H(\epsilon)
=
\max\{0,\epsilon-1\}
}.
\]
Hence this canonical non-Hilbert Radon plane has a flat strong-rotundity profile on
\[
0\le\epsilon\le1
\]
and a linear profile on
\[
1\le\epsilon\le2.
\]

## Assumptions and scope
All spaces and scalars are real. For
\[
(x,x^*)\in\Pi_X,
\]
one has
\[
\|x\|=\|x^*\|=x^*(x)=1.
\]
The open ball of radius \(\epsilon\) centered at \(x\) is denoted by \(U_X(x,\epsilon)\).

Birkhoff orthogonality is
\[
u\perp_B v
\quad\Longleftrightarrow\quad
\|u+\lambda v\|\ge\|u\|
\quad\text{for every }\lambda\in\mathbb R.
\]
The structural lower bound assumes
\[
u\perp_B v\Longrightarrow v\perp_B u.
\]
In dimension two, this is the Radon-plane condition.

The affine-regular hexagon has unit ball with vertices
\[
(1,0),\ (1,1),\ (0,1),\ (-1,0),\ (-1,-1),\ (0,-1).
\]
Its dual unit ball has vertices
\[
(1,0),\ (0,1),\ (1,-1)
\]
and their negatives.

## Proof
Fix
\[
(x,x^*)\in\Pi_X
\]
and
\[
y\in B_X.
\]
Because
\[
x^*(y)\le1,
\]
every
\[
z\in(x^*)^{-1}(\{1\})
\]
satisfies
\[
\|z-y\|
\ge
x^*(z-y)
=
1-x^*(y).
\]
This lower bound is attained exactly. Define
\[
z_y
=
y+\bigl(1-x^*(y)\bigr)x.
\]
Then
\[
x^*(z_y)=1
\]
and
\[
\|z_y-y\|
=
1-x^*(y).
\]
Therefore
\[
d\!\left(y,(x^*)^{-1}(\{1\})\right)
=
1-x^*(y).
\tag{1}
\]
Taking the infimum of (1) over
\[
y\in B_X\setminus U_X(x,\epsilon)
\]
gives
\[
\eta_X(\epsilon,(x,x^*))
=
\inf\left\{
1-x^*(y):
\|y\|\le1,\ \|x-y\|\ge\epsilon
\right\}
=
\upsilon_X(\epsilon,(x,x^*)).
\tag{2}
\]

Now suppose Birkhoff orthogonality is symmetric. For
\[
y\in B_X,
\]
write
\[
y=x^*(y)x+w,
\qquad
w=y-x^*(y)x\in\ker x^*.
\]
Since \(x^*\) norms \(x\),
\[
x\perp_B w.
\]
By symmetry,
\[
w\perp_B x.
\]
Hence
\[
\|w\|
\le
\|w+x^*(y)x\|
=
\|y\|
\le1.
\tag{3}
\]
Using (3),
\[
\|x-y\|
=
\left\|
\bigl(1-x^*(y)\bigr)x-w
\right\|
\le
1-x^*(y)+\|w\|
\le
2-x^*(y).
\]
Thus
\[
\|x-y\|\ge\epsilon
\quad\Longrightarrow\quad
1-x^*(y)\ge\epsilon-1.
\]
Combining this with nonnegativity and (2) yields
\[
\eta_X(\epsilon,(x,x^*))
\ge
\max\{0,\epsilon-1\}.
\]
Taking the infimum over \(\Pi_X\),
\[
\eta_X(\epsilon)
\ge
\max\{0,\epsilon-1\}.
\tag{4}
\]

It remains to show that the affine-regular hexagon is in the symmetric-Birkhoff class and attains (4).

Identify functionals with Euclidean coefficient vectors. Let
\[
J(a,b)=(-b,a).
\]
The dual unit ball of \(H\) is
\[
B_{H^*}
=
\operatorname{conv}\{\pm(1,0),\pm(0,1),\pm(1,-1)\}.
\]
Applying \(J\) to these six vertices gives exactly the six vertices of \(B_H\). Hence
\[
J(B_{H^*})=B_H.
\tag{5}
\]
For completeness, (5) gives Birkhoff symmetry directly. If
\[
u\perp_B v,
\]
there is a norming functional \(f\in S_{H^*}\) with
\[
f(u)=1,
\qquad
f(v)=0.
\]
In the Euclidean identification, \(v\) is parallel to \(Jf\). By (5), both \(v\) and \(Jf\) are unit vectors on the same line, so
\[
v=\sigma Jf
\]
for some
\[
\sigma\in\{-1,1\}.
\]
Also \(Ju\in S_{H^*}\). The functional
\[
g=\sigma Ju
\]
satisfies
\[
g(v)=1,
\qquad
g(u)=0.
\]
Therefore
\[
v\perp_B u.
\]

Finally choose
\[
x=(1,0),
\qquad
x^*(s,t)=s.
\]
For
\[
0\le\epsilon\le1,
\]
take
\[
y_\epsilon=(1,\epsilon).
\]
Then
\[
N(y_\epsilon)=1,
\qquad
N(x-y_\epsilon)=\epsilon,
\qquad
1-x^*(y_\epsilon)=0.
\]
Equation (2) gives
\[
\eta_H(\epsilon)\le0,
\]
so
\[
\eta_H(\epsilon)=0.
\]

For
\[
1\le\epsilon\le2,
\]
take
\[
y_\epsilon=(2-\epsilon,1).
\]
Then
\[
N(y_\epsilon)
=
\max\{2-\epsilon,1,|1-\epsilon|\}
=
1,
\]
and
\[
N(x-y_\epsilon)
=
N(\epsilon-1,-1)
=
\epsilon.
\]
Moreover
\[
1-x^*(y_\epsilon)
=
\epsilon-1.
\]
Thus
\[
\eta_H(\epsilon)
\le
\epsilon-1.
\]
Together with (4),
\[
\eta_H(\epsilon)
=
\epsilon-1.
\]
This completes the profile.

## Verification
The universal identity
\[
\eta_X=\upsilon_X
\]
is verified analytically by the explicit nearest point
\[
z_y=y+\bigl(1-x^*(y)\bigr)x
\]
on the supporting hyperplane.

The symmetric-Birkhoff lower bound is analytic as well: the projection
\[
P=I-x\otimes x^*
\]
has norm at most \(1\) whenever Birkhoff orthogonality is symmetric, because
\[
P y\perp_B x
\]
and therefore
\[
\|Py\|\le\|y\|.
\]

The bundled `verify.py` independently checks the affine-regular-hexagon geometry. It verifies that the quarter-turn \(J\) maps the six dual vertices exactly onto the six primal vertices, checks the norming-functional reversal underlying Birkhoff symmetry on canonical edge and vertex families, and verifies both explicit witness families for every rational grid point
\[
\epsilon=\frac{k}{200},
\qquad
0\le k\le400.
\]
The grid is a reproducibility check only; the continuum statement follows from the displayed formulas.

## Relationship to prior work
García-Pacheco introduced \(\eta_X\) as the index of strong rotundity and later introduced the auxiliary quantity \(\upsilon_X\). The defining paper proves
\[
2\delta_X(\epsilon,x)
\le
\upsilon_X(\epsilon,(x,x^*))
\le
\eta_X(\epsilon,(x,x^*)).
\]
It also computes
\[
\eta_X(\epsilon)=\frac{\epsilon^2}{2}
\]
for Hilbert spaces.

The exact equality
\[
\upsilon_X=\eta_X
\]
follows from the affine-hyperplane distance formula (1), so the auxiliary index collapses to the strong-rotundity index for every norming pair in every real Banach space.

A 2024 follow-up on the core of the unit sphere again records only
\[
0\le\upsilon_X\le\eta_X\le2
\]
and derives special situations where both quantities vanish or both equal \(2\). The inspected follow-up therefore does not supply the universal identity.

Targeted public-research searches under the exact index name, the \(\eta_X\)-\(\upsilon_X\) comparison, Radon-plane terminology, and affine-regular-hexagon aliases returned no covering statement. The closest indexed hexagonal results compute Banach--Mazur, isosceles von Neumann--Jordan, or angle-modulus invariants rather than the strong-rotundity index.

The exact hexagonal profile is notably different from the Hilbert profile: it vanishes through unit separation and then grows linearly, whereas a Hilbert space has the quadratic law
\[
\epsilon^2/2.
\]

## Limitations
The identity
\[
\eta_X=\upsilon_X
\]
is fully general, but the lower bound
\[
\eta_X(\epsilon)\ge\max\{0,\epsilon-1\}
\]
uses symmetric Birkhoff orthogonality.

The exact non-Hilbert profile is proved only for the affine-regular hexagonal plane. The result does not classify the strong-rotundity index on all Radon planes or all polyhedral Banach planes.

Bibliographic and semantic searches cannot prove absolute novelty. An equivalent observation may exist in general approximation-theory language as a distance-to-affine-hyperplane formula without being stated for García-Pacheco's indices.

## References
1. F. J. García-Pacheco, “The index of strong rotundity,” AIMS Mathematics 8 (2023), 20477–20486, doi:10.3934/math.20231043. Published 25 June 2023. Mathematics Subject Classification: 46B20.
2. A. Campos-Jiménez and F. J. García-Pacheco, “The core of the unit sphere of a Banach space,” AIMS Mathematics 9 (2024), 3440–3452, doi:10.3934/math.2024169.
