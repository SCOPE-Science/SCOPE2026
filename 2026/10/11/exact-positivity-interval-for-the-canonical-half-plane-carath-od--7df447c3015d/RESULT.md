# Exact positivity interval for the canonical half-plane Carathéodory component

## Finding

For
\[
|\lambda|=1,
\]
consider the normalized convex half-plane map
\[
f_\lambda(z)=\frac{z}{1-\lambda z}.
\]
Let
\[
h_\alpha[f_\lambda]
\]
denote the \(\alpha\)-Carathéodory component introduced in the cited 2026 paper.

For real
\[
\alpha,
\]
the function
\[
h_\alpha[f_\lambda]
\]
belongs to the Carathéodory class exactly when
\[
0\le\alpha\le1.
\]

More precisely, define
\[
m_\lambda(\alpha)
=
\inf_{|z|<1}
\operatorname{Re}
h_\alpha[f_\lambda](z).
\]
Then
\[
m_\lambda(0)=1,
\]
\[
m_\lambda(\alpha)
=
\frac{1-\alpha}{2}
\qquad
(0<\alpha<1),
\]
and
\[
m_\lambda(1)=0.
\]

For
\[
0<\alpha\le1,
\]
the infimum is not attained. It is approached along points satisfying
\[
\lambda z\to1.
\]

Thus the source's pointwise positivity conjecture is true for this canonical half-plane family throughout
\[
[0,1],
\]
and that interval is maximal among real parameters for this family.

At the endpoint
\[
\alpha=1,
\]
pointwise positivity remains strict inside the disk, but there is no positive uniform floor. Therefore the source's positive-minimum formulation is not equivalent to its pointwise formulation on the canonical example.

## Assumptions and scope

The source defines an \(\alpha\)-Carathéodory component for normalized convex functions and formulates pointwise positivity conjectures on
\[
0\le\alpha\le1.
\]
It also introduces a fourth formulation using the minimum of the real part and states that formulation as equivalent on the same interval.

The source's first numerical example is
\[
f(z)=\frac{z}{1-z},
\]
followed by its rotations
\[
f_\lambda(z)=\frac{z}{1-\lambda z},
\qquad
|\lambda|=1.
\]
For these maps it gives an explicit rational expression for the component and reports numerical random-point minima.

The result here is exact for that entire rotated half-plane family. It does not settle the source's pointwise conjecture for every normalized convex function.

For
\[
\alpha\notin[0,1],
\]
the same rational expression is used as a real-parameter continuation only to determine the maximal interval on which the canonical family remains a holomorphic Carathéodory function.

## Proof

Put
\[
w=\lambda z
\]
and
\[
\beta=1-\alpha.
\]
Because multiplication by
\[
\lambda
\]
is a disk rotation, it is enough to study the function
\[
H_\alpha(w)
=
\frac{
1-(1-\beta)w-\beta^2w^2
}{
(1+w)(1-\beta w)
}.
\]

First assume
\[
0<\alpha<1,
\]
so
\[
0<\beta<1.
\]
There are no poles in the open unit disk.

On the unit circle, write
\[
w=e^{it},
\qquad
w\ne-1,
\qquad
x=\cos t.
\]
Direct simplification gives
\[
\operatorname{Re}H_\alpha(e^{it})
=
\frac{
\beta\bigl(\beta^2+3-2(\beta+1)x\bigr)
}{
2\bigl(\beta^2+1-2\beta x\bigr)
}.
\]
Differentiating with respect to
\[
x
\]
gives
\[
-\frac{
\beta(1-\beta)^2
}{
\bigl(\beta^2+1-2\beta x\bigr)^2
},
\]
which is strictly negative. Hence the boundary real part decreases as
\[
x
\]
increases, and its smallest finite boundary limit occurs at
\[
x=1.
\]
There,
\[
\lim_{w\to1}
\operatorname{Re}H_\alpha(w)
=
\frac{\beta}{2}.
\]

The boundary point
\[
w=-1
\]
is a pole, so it must be controlled separately. The exact partial-fraction identity is
\[
H_\alpha(w)
=
\beta
+
\frac{(1-\beta)(\beta+2)}
{(\beta+1)(1+w)}
-
\frac{1-\beta}
{(\beta+1)(1-\beta w)}.
\]
For
\[
|w|<1,
\]
\[
\operatorname{Re}\frac{1}{1+w}>\frac12.
\]
Moreover, as
\[
w\to-1
\]
from inside the disk, the last term remains bounded. In fact,
\[
\liminf_{w\to-1}
\operatorname{Re}H_\alpha(w)
\ge
\frac{\beta}{2}
+
\frac{2\beta}{(\beta+1)^2}
>
\frac{\beta}{2}.
\]

Apply the harmonic minimum principle to the real part on the disk with a small cap around
\[
-1
\]
removed, then let the cap shrink. The preceding boundary calculation gives
\[
\operatorname{Re}H_\alpha(w)
>
\frac{\beta}{2}
\]
throughout
\[
|w|<1.
\]
Since radial points
\[
w=r
\]
with
\[
r\to1^-
\]
approach the boundary value
\[
\beta/2,
\]
the exact infimum is
\[
\inf_{|w|<1}\operatorname{Re}H_\alpha(w)
=
\frac{\beta}{2}
=
\frac{1-\alpha}{2}.
\]

At
\[
\alpha=0,
\]
one has
\[
\beta=1,
\]
and the rational expression cancels to
\[
H_0(w)\equiv1.
\]
Hence
\[
m_\lambda(0)=1.
\]

At
\[
\alpha=1,
\]
one has
\[
\beta=0,
\]
so
\[
H_1(w)=\frac{1-w}{1+w}.
\]
This is the standard Cayley transform of the disk onto the right half-plane. Therefore
\[
\operatorname{Re}H_1(w)>0
\]
for every
\[
|w|<1,
\]
but
\[
\inf_{|w|<1}\operatorname{Re}H_1(w)=0
\]
as
\[
w\to1.
\]

It remains to show maximality of
\[
[0,1].
\]
If
\[
\alpha<0,
\]
then
\[
\beta>1,
\]
and the factor
\[
1-\beta w
\]
vanishes at
\[
w=\beta^{-1}\in\mathbb D.
\]
The numerator does not vanish there, so the component has an interior pole.

If
\[
1<\alpha\le2,
\]
then
\[
-1\le\beta<0.
\]
At the boundary point
\[
w=i,
\]
the finite boundary real part is
\[
\operatorname{Re}H_\alpha(i)
=
\frac{
\beta(\beta^2+3)
}{
2(\beta^2+1)
}
<0.
\]
By continuity, the real part is negative at interior points sufficiently close to
\[
i.
\]

If
\[
\alpha>2,
\]
then
\[
\beta<-1,
\]
and again
\[
1-\beta w
\]
has a zero
\[
w=\beta^{-1}\in\mathbb D
\]
without cancellation.

Thus the exact real parameter interval for Carathéodory membership of the canonical half-plane family is
\[
[0,1].
\]

## Verification

The boundary formula was independently checked by combining
\[
H_\alpha(w)
\]
with its conjugate on
\[
|w|=1
\]
and replacing
\[
w+w^{-1}
\]
by
\[
2\operatorname{Re}w.
\]

Its derivative simplifies exactly to
\[
-\frac{
\beta(1-\beta)^2
}{
\bigl(\beta^2+1-2\beta x\bigr)^2
}.
\]
Thus no numerical minimization is used.

The partial-fraction identity was expanded back to the original rational function. It shows that the exceptional boundary pole at
\[
-1
\]
cannot create a lower limiting value.

The endpoint formulas
\[
H_0\equiv1
\]
and
\[
H_1(w)=\frac{1-w}{1+w}
\]
are exact.

Representative numerical evaluations for interior points agree with the formula
\[
(1-\alpha)/2
\]
as the radial boundary infimum, but these computations are consistency checks only.

## Relationship to prior work

Grigoriciuc introduces the \(\alpha\)-Carathéodory component and formulates the main pointwise positivity conjecture for normalized convex functions. The paper's canonical example is
\[
z/(1-z),
\]
followed by its rotations. For these examples it gives the same rational formula used above, but the positivity evidence reported there is numerical sampling rather than an exact minimization.

The same article introduces a fourth formulation based on a strictly positive minimum of the real part and describes it as equivalent to the pointwise conjectures on
\[
[0,1].
\]
The exact endpoint calculation above shows that the distinction between pointwise positivity and a positive uniform floor matters already for the canonical example:
\[
H_1
\]
is strictly positive in real part at every disk point, while its infimum is zero.

Earlier work on extension operators establishes geometric inclusion and extension results at relevant endpoint parameters, but it does not give the exact real-part profile of this component for the canonical half-plane family.

Targeted literature searches for the source formula, the rotated half-plane family, the exact infimum, and the maximal parameter interval did not locate an implication-equivalent published statement.

## Limitations

The theorem treats the canonical half-plane family and its rotations, not every convex function.

The endpoint observation distinguishes pointwise positivity from a positive uniform floor; it does not disprove the source's main pointwise positivity conjecture.

The outside-
\[
[0,1]
\]
classification concerns the real-parameter continuation of the explicit canonical formula and does not assert that every auxiliary extension construction in the source is intended outside its original parameter range.

The theorem gives the exact infimum, not an attained minimum, for
\[
0<\alpha\le1.
\]

## References

1. E. Ş. Grigoriciuc, *A conjecture related to convex functions on the unit disc: numerical approach and extension results*, Journal of Analysis 34 (2026), 2013--2037, DOI: 10.1007/s41478-026-01067-z.
2. E. Ş. Grigoriciuc, *New subclasses of univalent mappings in several complex variables: extension operators and applications*, Computational Methods and Function Theory 23 (2023), 347--374, DOI: 10.1007/s40315-022-00467-z.
3. H. Hamada, G. Kohr, and M. Kohr, *Roper--Suffridge type extension operators for univalent mappings revisited*, Journal of Mathematical Analysis and Applications 548 (2025), 129763, DOI: 10.1016/j.jmaa.2025.129763.
