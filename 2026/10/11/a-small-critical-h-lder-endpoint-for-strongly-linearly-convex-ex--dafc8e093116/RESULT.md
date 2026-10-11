# A small critical-Hölder endpoint for strongly linearly convex exhaustion

## Finding

Let
\[
D\subset\mathbb C^n,
\qquad
n\ge2,
\]
be a bounded \(\mathbb C\)-convex domain with \(C^1\) boundary. Choose \(R>0\) such that
\[
\overline D\subset B(0,R).
\]
Let \(\nu\) be the outward unit normal and define
\[
\omega_\nu(t)
=
\sup\{
|\nu(p)-\nu(q)|:
p,q\in\partial D,\ |p-q|\le t
\},
\]
together with the critical normal modulus
\[
\Lambda_\nu
=
\limsup_{t\downarrow0}
\frac{\omega_\nu(t)}{\sqrt t}.
\]

The smoothing argument of the recent modulus-of-continuity theorem has a quantitative endpoint that survives when this limit is positive but sufficiently small.

More precisely, let \(C_0>0\) be the constant in the source's collar estimate
\[
\frac{|\partial h_\delta(z)(w)|^2}{h_\delta(z)}
-
L_{h_\delta}(z;w)
-
|Q_{h_\delta}(z;w)|
\ge
-C_0\delta^2
\bigl(
\rho(A\delta)^2+2\delta
\bigr)^2
|w|^2,
\]
where
\[
\rho(r)
=
\sup_{0<t\le r}
\frac{\omega_\nu(t)}{\sqrt t},
\]
\(A>0\) is fixed by the source estimate, and the mollification scale is
\[
\tau_\delta=\delta^3.
\]

Choose
\[
0<c<\frac{1}{20(1+R^2)}
\]
and define
\[
\eta(D;c,C_0)
=
\left(
\frac{c}{C_0(1+R^2)}
\right)^{1/4}.
\]
If
\[
\Lambda_\nu<\eta(D;c,C_0),
\]
then \(D\) admits an increasing exhaustion
\[
\overline{D_j}\subset D_{j+1},
\qquad
\bigcup_{j\ge1}D_j=D,
\]
by bounded \(C^\infty\) strongly linearly convex domains.

Consequently,
\[
c_D=l_D
\]
for the Carathéodory distance and Lempert function, and
\[
\gamma_D=\kappa_D
\]
for the Carathéodory--Reiffen and Kobayashi--Royden infinitesimal metrics.

A direct corollary is a genuine critical Hölder endpoint. If the outward normal is \(1/2\)-Hölder with seminorm
\[
[\nu]_{C^{0,1/2}}
<
\eta(D;c,C_0),
\]
then the same exhaustion conclusion holds even though
\[
\frac{\omega_\nu(t)}{\sqrt t}
\]
need not tend to zero.

## Assumptions and scope

The result uses the same squared-distance regularization and perturbation scheme as the two recent primary papers on the Aizenberg approximation problem.

The constant \(C_0\) is the fixed error constant in Proposition 2.4 of arXiv:2609.35474v1. No claim is made that
\[
\eta(D;c,C_0)
\]
is optimal. It is a proof-generated sufficient threshold.

The conclusion is invariant under replacing the displayed sufficient threshold by any smaller positive one. The dependence on the containing radius \(R\) reflects the particular quadratic perturbation used in the proof, not an asserted intrinsic sharp constant.

The result does not settle arbitrary \(C^{1,1/2}\) boundaries. It proves the endpoint only under smallness of the critical normal seminorm.

## Proof

Set
\[
h(z)=\delta_D(z)^2,
\]
where \(\delta_D\) is the Euclidean distance to the boundary.

The recent modulus theorem defines
\[
\rho(r)
=
\sup_{0<t\le r}
\frac{\omega_\nu(t)}{\sqrt t}
\]
and proves, after smoothing \(h\) at scale
\[
\tau_\delta=\delta^3,
\]
that on the collar
\[
U_\delta
=
\{z\in D:\delta<\delta_D(z)<4\delta\},
\]
one has
\[
\frac{|\partial h_\delta(z)(w)|^2}{h_\delta(z)}
-
L_{h_\delta}(z;w)
-
|Q_{h_\delta}(z;w)|
\ge
-C_0\delta^2
\bigl(
\rho(A\delta)^2+2\delta
\bigr)^2
|w|^2.
\]

The source assumes
\[
\rho(r)\longrightarrow0.
\]
For the displayed defect estimate itself, that limit is not needed. Since \(\rho\) is the decreasing tail supremum of the quotient
\[
\omega_\nu(t)/\sqrt t,
\]
one has
\[
\lim_{r\downarrow0}\rho(r)
=
\Lambda_\nu.
\]

Assume
\[
\Lambda_\nu
<
\left(
\frac{c}{C_0(1+R^2)}
\right)^{1/4}.
\]
Then
\[
C_0\Lambda_\nu^4
<
\frac{c}{1+R^2}.
\]
By convergence of \(\rho(A\delta)\) to \(\Lambda_\nu\) and by
\[
2\delta\longrightarrow0,
\]
there is \(\delta_0>0\) such that, whenever
\[
0<\delta<\delta_0,
\]
\[
C_0
\bigl(
\rho(A\delta)^2+2\delta
\bigr)^2
<
\frac{c}{1+R^2}.
\]

Now perturb the regularization by
\[
\widetilde h_\delta
=
h_\delta-c\delta^2(1+|z|^2).
\]
Edigarian's perturbation lemma gives
\[
\begin{aligned}
&
\frac{|\partial\widetilde h_\delta(z)(w)|^2}
{\widetilde h_\delta(z)}
-
L_{\widetilde h_\delta}(z;w)
-
|Q_{\widetilde h_\delta}(z;w)|
\\
&\qquad
\ge
\frac{|\partial h_\delta(z)(w)|^2}{h_\delta(z)}
-
L_{h_\delta}(z;w)
-
|Q_{h_\delta}(z;w)|
+
\frac{c\delta^2}{1+R^2}|w|^2.
\end{aligned}
\]
Combining the two inequalities gives a strictly positive lower bound
\[
\delta^2
\left[
\frac{c}{1+R^2}
-
C_0
\bigl(
\rho(A\delta)^2+2\delta
\bigr)^2
\right]
|w|^2
>
0
\]
on \(U_\delta\).

This is exactly the positivity needed in the source proof to show that the relevant smooth superlevel component has strongly linearly convex boundary.

The rest of the exhaustion construction is unaffected by replacing the little-Hölder condition with the present small critical condition. The required approximation of \(h\) uses only
\[
|h_\delta-h|
\le
C\delta\tau_\delta
\]
and
\[
\frac{\tau_\delta}{\delta}
=
\delta^2
\longrightarrow0.
\]
The collar inclusions, regularity of the level boundary, nesting of the connected components, and exhaustion of \(D\) then proceed verbatim.

Finally, if \(\nu\) is \(1/2\)-Hölder with seminorm \(M\), then
\[
\omega_\nu(t)\le M\sqrt t
\]
and therefore
\[
\Lambda_\nu\le M.
\]
Thus every sufficiently small critical Hölder seminorm satisfies the hypothesis.

## Verification

The full text of arXiv:2609.35474v1 was inspected at Theorem 1.1, the definition of
\[
\rho(r),
\]
Lemma 2.3, Proposition 2.4, Proposition 2.5, and the final exhaustion step.

The full text of arXiv:2607.26696v1 was inspected at its primary classification, the squared-distance regularization, Lemma 2.4, Proposition 2.5, and the completion of the exhaustion proof.

The critical calculation is an implication comparison rather than a numerical experiment. The source collar defect is
\[
-C_0\delta^2
\bigl(
\rho(A\delta)^2+2\delta
\bigr)^2,
\]
while the perturbation contributes
\[
\frac{c\delta^2}{1+R^2}.
\]
The new condition is exactly a sufficient strict inequality between those two limiting coefficients.

No finite sampling, numerical optimization, or unproved regularity assertion is used.

## Relationship to prior work

Edigarian's July 2026 theorem proves the exhaustion result for boundaries of class
\[
C^{1,\alpha},
\qquad
\alpha>\frac12.
\]
Its proof gains a power of \(\delta\) because the smoothing error is
\[
o(\delta^2)
\]
in that range.

Gupta's September 2026 theorem replaces the power condition by the more flexible hypothesis
\[
\frac{\omega_\nu(t)}{\sqrt t}
\longrightarrow0.
\]
Its Proposition 2.4 makes the critical error coefficient explicit in terms of the tail quotient
\[
\rho(r).
\]

The present result identifies the next regime already supported by that estimate: the quotient may converge to a nonzero value, provided that value is small enough for the positive quadratic perturbation to dominate it.

This is not implied by the published statements, which require either
\[
\alpha>\frac12
\]
or little-Hölder decay at the critical exponent. Targeted searches under critical \(1/2\)-Hölder, small seminorm, square-root modulus, and Aizenberg-exhaustion formulations did not locate a theorem with this quantitative endpoint.

## Limitations

The threshold is sufficient and proof-dependent, not asserted sharp.

The argument does not settle large \(C^{1,1/2}\) seminorms or arbitrary critical Hölder boundaries.

The constant depends on the smoothing estimate and on the radius used in the quadratic perturbation. A more intrinsic or optimal endpoint constant would require additional geometry.

## References

1. N. Gupta, *Strongly linearly convex exhaustion of a class of \(\mathbb C\)-convex domains*, arXiv:2609.35474v1, 2026.
2. A. Edigarian, *Strongly linearly convex exhaustion of \(\mathbb C\)-convex domains with \(C^{1,\alpha}\) boundary*, arXiv:2607.26696v1, 2026.
3. D. Jacquet, *\(\mathbb C\)-convex domains with \(C^2\) boundary*, Complex Variables and Elliptic Equations 51 (2006), 303--312.
4. P. Pflug and W. Zwonek, *Exhausting domains of the symmetrized bidisc*, Arkiv för Matematik 50 (2012), 397--402.
