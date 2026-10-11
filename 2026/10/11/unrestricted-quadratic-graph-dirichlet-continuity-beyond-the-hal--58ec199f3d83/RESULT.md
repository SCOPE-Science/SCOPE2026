# Unrestricted quadratic-graph Dirichlet continuity beyond the half-curvature threshold

## Finding

Let
\[
B
=
\left\{
(z_1,z_2)\in\mathbb C^2:
|z_1|^2+|z_2|^2<1
\right\},
\]
fix
\[
0<a<1,
\]
and allow
\[
\varepsilon\in\mathbb C
\]
to be arbitrary.

Define the two disjoint quadratic graphs by
\[
z_2=\varepsilon z_1^2+a,
\qquad
z_2=\varepsilon z_1^2-a,
\]
or equivalently by the reduced polynomial
\[
F_{\varepsilon,a}(z_1,z_2)
=
(z_2-\varepsilon z_1^2)^2-a^2.
\]
Set
\[
\varphi_{\varepsilon,a}
=
-\log|F_{\varepsilon,a}|.
\]

Then the obstacle envelope
\[
G_{\varphi_{\varepsilon,a},B}
\]
is continuous on \(B\) for every complex \(\varepsilon\), with no curvature bound. The disk-bundle hull identities and the uniqueness statement with the fixed obstacle also hold.

The holomorphic deformation is exactly the one used in the recent source:
\[
\Phi_t(z_1,z_2)
=
\left(
(1+t)z_1,\,
z_2+\varepsilon((1+t)^2-1)z_1^2
\right).
\]
It preserves the divisor pointwise at the level of its defining polynomial:
\[
F_{\varepsilon,a}\circ\Phi_t
=
F_{\varepsilon,a}.
\]

The source assumes
\[
|\varepsilon|<\frac12
\]
in its worked example. That number is not a continuity threshold. It is instead the exact threshold for the stronger property that the whole unit sphere moves weakly outward.

More precisely, if
\[
\rho(z_1,z_2)=|z_1|^2+|z_2|^2-1,
\]
the forward normal quantity is
\[
N_\varepsilon(\xi)
=
|\xi_1|^2
+
\operatorname{Re}
\left(
2\varepsilon\xi_1^2\overline{\xi_2}
\right).
\]
On the complete sphere,
\[
N_\varepsilon\ge0
\quad\text{for all }\xi\in\partial B
\]
if and only if
\[
|\varepsilon|\le\frac12.
\]

In contrast, on the singular divisor itself one has the exact identity
\[
N_\varepsilon(\xi)
=
1-a^2
+
|\varepsilon|^2|\xi_1|^4
>
0
\]
for every
\[
\varepsilon\in\mathbb C.
\]
Thus the source's graph criterion remains valid far beyond the global outwardness threshold.

For
\[
|\varepsilon|>\frac12,
\]
the deformed domains are genuinely nonnested with the ball for all sufficiently small positive \(t\): some boundary points move inward and others outward. The envelope continuity therefore persists through the geometric transition into the nonnested regime and for arbitrarily large quadratic curvature.

## Assumptions and scope

The obstacle envelope, neighbourhood deformation, graph criterion, hull identities, and fixed-obstacle uniqueness statement are used in the sense of the recent primary source on complex Dirichlet problems with unbounded boundary values.

The polynomial
\[
F_{\varepsilon,a}
=
(z_2-\varepsilon z_1^2-a)
(z_2-\varepsilon z_1^2+a)
\]
is reduced because
\[
a>0.
\]
Its two graph components are disjoint on all of \(\mathbb C^2\).

The conclusion is an unrestricted parameter extension of the source's quadratic-graph example. It does not claim an explicit closed form for
\[
G_{\varphi_{\varepsilon,a},B}.
\]

The number
\[
1/2
\]
is proved sharp only for global outwardness of the entire unit sphere under this deformation. It is not a singular-set threshold and not a continuity threshold.

## Proof

The deformation preserves each graph. Indeed,
\[
\begin{aligned}
&\left[
z_2+
\varepsilon((1+t)^2-1)z_1^2
\right]
-
\varepsilon(1+t)^2z_1^2
\\
&\qquad
=
z_2-\varepsilon z_1^2.
\end{aligned}
\]
Hence
\[
F_{\varepsilon,a}(\Phi_t(z))
=
F_{\varepsilon,a}(z).
\]
The obstacle compatibility required by the source theorem is therefore exact.

It remains to check the boundary-normal condition only where the divisor meets the sphere.

For
\[
\rho(z)=|z_1|^2+|z_2|^2-1,
\]
the graph criterion in the source gives, on either component,
\[
N_\varepsilon(\xi)
=
|\xi_1|^2
+
\operatorname{Re}
\left(
2\varepsilon\xi_1^2\overline{\xi_2}
\right).
\]

Take
\[
\xi\in\partial B
\]
on the component
\[
\xi_2
=
\varepsilon\xi_1^2+\sigma a,
\qquad
\sigma\in\{-1,1\}.
\]
Put
\[
x=|\xi_1|^2.
\]
The sphere equation becomes
\[
1
=
x
+
|\varepsilon|^2x^2
+
a^2
+
2\sigma a
\operatorname{Re}(\varepsilon\xi_1^2).
\]
Therefore
\[
2\sigma a
\operatorname{Re}(\varepsilon\xi_1^2)
=
1-a^2-x-|\varepsilon|^2x^2.
\]

On the same graph,
\[
\begin{aligned}
N_\varepsilon(\xi)
&=
x
+
2|\varepsilon|^2x^2
+
2\sigma a
\operatorname{Re}(\varepsilon\xi_1^2)
\\
&=
1-a^2
+
|\varepsilon|^2x^2.
\end{aligned}
\]
Since
\[
0<a<1,
\]
this is strictly positive, uniformly in the graph sign and with no bound on \(\varepsilon\).

The source's graph proposition therefore applies to every parameter. Since the unit ball has neighbourhood plurisubharmonic barriers everywhere and its closure is polynomially convex in \(\mathbb C^2\), the source's continuity, hull, and fixed-obstacle uniqueness theorems give all stated analytic conclusions.

We now identify what the source's bound
\[
|\varepsilon|<\frac12
\]
actually controls.

For an arbitrary sphere point, fix
\[
x=|\xi_1|^2,
\qquad
|\xi_2|=\sqrt{1-x}.
\]
The phase of
\[
\varepsilon\xi_1^2\overline{\xi_2}
\]
can be chosen freely, so
\[
\min
N_\varepsilon(\xi)
=
x
-
2|\varepsilon|x\sqrt{1-x}
=
x\left(
1-2|\varepsilon|\sqrt{1-x}
\right)
\]
at that value of \(x\).

If
\[
|\varepsilon|\le\frac12,
\]
then this quantity is nonnegative for every
\[
0\le x\le1.
\]
Conversely, if
\[
|\varepsilon|>\frac12,
\]
choose \(x>0\) small enough that
\[
2|\varepsilon|\sqrt{1-x}>1.
\]
The phase minimizing the real part then gives a point with
\[
N_\varepsilon<0.
\]
The opposite phase gives a point with
\[
N_\varepsilon>0.
\]

Finally,
\[
\left.
\frac{d}{dt}
\rho(\Phi_t(\xi))
\right|_{t=0}
=
2N_\varepsilon(\xi).
\]
Thus when
\[
|\varepsilon|>\frac12,
\]
one boundary point moves strictly into the ball and another moves strictly outside it for every sufficiently small positive \(t\). Since both images lie on
\[
\partial\Phi_t(B),
\]
the domains
\[
B
\quad\text{and}\quad
\Phi_t(B)
\]
are incomparable under inclusion.

This proves both the unrestricted continuity statement and the exact geometric meaning of the half-curvature threshold.

## Verification

The recent primary source was inspected at its main continuity theorem, the graph deformation criterion, and its explicit quadratic-graph example. The example assumes
\[
|\varepsilon|<\frac12
\]
after bounding the boundary normal term by
\[
(1-2|\varepsilon|)|\xi_1|^2.
\]

The new calculation does not replace that bound by another estimate. It substitutes the exact graph equation and the exact sphere equation into the same normal quantity, producing
\[
1-a^2+|\varepsilon|^2|\xi_1|^4.
\]
This is positive for the entire parameter plane.

The global threshold computation is also exact: phase minimization on a sphere fibre gives
\[
x\left(1-2|\varepsilon|\sqrt{1-x}\right).
\]
Its sign on all
\[
0\le x\le1
\]
changes exactly at
\[
|\varepsilon|=\frac12.
\]

No numerical experiment is used.

## Relationship to prior work

The October 2026 source develops a local deformation criterion for unbounded Perron–Bremermann problems and illustrates it with two disjoint quadratic graphs in the unit ball. In that example it assumes
\[
|\varepsilon|<\frac12
\]
and uses a global lower bound on the sphere to conclude that the singular boundary is avoided.

The present result shows that this parameter restriction is stronger than the theorem needs. On the actual singular graphs, the boundary relation cancels the potentially negative cross term and leaves a strictly positive expression for every \(\varepsilon\).

The distinction is geometrically substantive. The same value
\[
1/2
\]
is the sharp boundary between global outward motion and genuinely nonnested domain motion, while the analytic Dirichlet conclusion has no corresponding finite threshold.

Targeted searches for the exact polynomial, quadratic-graph deformation, arbitrary-\(\varepsilon\) parameter range, and equivalent Perron–Bremermann formulations located the recent source itself but no independent statement of this unrestricted extension.

A previous result from the same source computed an exact finite-obstacle envelope for coordinate powers on the ball. That finding concerns a different obstacle, a different singularity regime, and no graph deformation; it neither states nor implies the present parameter extension.

## Limitations

The result is specific to the quadratic graph pair
\[
z_2=\varepsilon z_1^2\pm a.
\]
For higher-degree graph pairs the normal expression no longer has the same exact cancellation, and a separate parameter analysis is needed.

No explicit formula for the unbounded obstacle envelope is claimed.

The result does not optimize deformation rates or quantify a modulus of continuity for the envelope.

## References

1. H. H. Dao and Q. D. Nguyen, *Complex Dirichlet problem with unbounded boundary values*, arXiv:2610.00914v1, 2026.
2. H. J. Bremermann, *On a generalized Dirichlet problem for plurisubharmonic functions and pseudoconvex domains*, Transactions of the American Mathematical Society 91 (1959), 246–276.
3. J. B. Walsh, *Continuity of envelopes of plurisubharmonic functions*, Journal de Mathématiques Pures et Appliquées 59 (1980), 195–217.
