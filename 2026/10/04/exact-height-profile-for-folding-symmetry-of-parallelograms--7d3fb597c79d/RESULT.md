# Exact height profile for folding symmetry of parallelograms

## Finding

Let \(P\) be a nondegenerate Euclidean parallelogram. Let \(L\) be the length of a longest side and \(H\) the altitude to a longest side. Define the similarity-invariant normalized height
\[
h=\frac{H}{L}\in(0,1].
\]

Among all parallelograms with fixed \(h\), the folding-symmetry measure introduced by Lassak and used by Goenka, Moore, Sun, and White has the sharp minimum
\[
\boxed{
\mathcal F(h)=
\begin{cases}
\displaystyle
\frac{\sqrt{5-h^2}-\sqrt{1-h^2}}{2},
&0<h\le h_0,\\[3mm]
\displaystyle
\frac{1+h^2}{2},
&h_0\le h\le1,
\end{cases}}
\]
where \(s_0\in(0,1)\) is the unique root of
\[
s^3-2s^2-4s+4=0
\]
and
\[
h_0=\sqrt{1-s_0^2}\approx0.591829148600584.
\]

After a Euclidean similarity and, if necessary, a reflection, every such parallelogram has the form
\[
P(d,h)
=
\operatorname{conv}
\{(0,0),(1,0),(d,h),(1+d,h)\},
\]
with
\[
0\le d\le\sqrt{1-h^2}.
\]
For each fixed \(h\), the minimizing shear is unique:
\[
\boxed{
d_*(h)=
\begin{cases}
1-\mathcal F(h),&0<h\le h_0,\\[1mm]
\displaystyle\frac{1-h^2}{2},&h_0\le h\le1.
\end{cases}}
\]

At \(h=h_0\), all three fold mechanisms in the corrected parallelogram formula have exactly the same value. Thus the stability profile has a genuine phase transition between two different active-fold pairs.

The profile is strictly increasing on \((0,1]\). Moreover,
\[
\lim_{h\downarrow0}\mathcal F(h)=\frac1\varphi,
\]
where \(\varphi=(1+\sqrt5)/2\), and
\[
\mathcal F(h)
=
\frac1\varphi
+
\frac{5-\sqrt5}{20}h^2
+
O(h^4)
\qquad(h\downarrow0).
\]
This gives the sharp quadratic cost of keeping a parallelogram a positive normalized height away from the degenerate sequence that approaches the known golden-ratio infimum.

## Assumptions and scope

The folding-symmetry measure is
\[
\operatorname{Sym}_{\mathrm{fold}}(K)
=
2\sup_m\frac{\operatorname{area}(C_m)}{\operatorname{area}(K)},
\]
where \(m\) ranges over fold lines and \(C_m\) is a portion cut from \(K\) whose reflection across \(m\) remains in \(K\).

Only Euclidean similarities and reflections are used in the normalization; folding symmetry is not being treated as an arbitrary affine invariant.

The longest side is scaled to length \(1\). Choosing the acute representative of the angle between the two side directions gives
\[
d\ge0,
\]
while the other side having length at most \(1\) gives
\[
d^2+h^2\le1.
\]
Hence
\[
0\le d\le\sqrt{1-h^2}.
\]

The starting three-term formula for parallelograms is the corrected formula proved by Goenka, Moore, Sun, and White. The new statement optimizes that exact formula under the geometrically natural fixed-height constraint.

## Proof

Set
\[
s=\sqrt{1-h^2}.
\]
For the normalized parallelogram \(P(d,h)\), Goenka, Moore, Sun, and White prove
\[
\operatorname{Sym}_{\mathrm{fold}}(P(d,h))
=
\max\{A_h(d),B_h(d),C(d)\},
\]
where
\[
A_h(d)=\frac1{1-d+s},
\qquad
B_h(d)=\sqrt{d^2+h^2},
\qquad
C(d)=1-d.
\]

For fixed \(h\), both \(A_h\) and \(B_h\) are increasing on the feasible interval, while \(C\) is strictly decreasing. Therefore
\[
D_h(d)=\max\{A_h(d),B_h(d)\}
\]
is strictly increasing. At \(d=0\),
\[
D_h(0)\le1=C(0),
\]
and at \(d=s\),
\[
D_h(s)=1\ge1-s=C(s).
\]
Thus there is a unique point at which \(D_h=C\), and this point is the unique minimizer of
\[
\max\{D_h,C\}.
\]

The crossing of \(A_h\) and \(C\) is found by writing
\[
y=1-d.
\]
The equation
\[
A_h(d)=C(d)
\]
becomes
\[
y(y+s)=1,
\]
so
\[
y_A=\frac{\sqrt{s^2+4}-s}{2}
\]
and
\[
d_A=1-y_A.
\]

The crossing of \(B_h\) and \(C\) satisfies
\[
\sqrt{d^2+h^2}=1-d.
\]
Using \(h^2=1-s^2\) gives
\[
d_B=\frac{s^2}{2}
\]
and
\[
C(d_B)=\frac{1+h^2}{2}.
\]

Because \(D_h\) reaches \(C\) when the first of \(A_h\) and \(B_h\) reaches it, the minimizer is
\[
d_*(h)=\min\{d_A,d_B\}.
\]

To determine which crossing occurs first, evaluate the \(A_h=C\) condition at \(d=d_B\). With
\[
y=1-\frac{s^2}{2},
\]
one obtains
\[
y(y+s)-1
=
\frac{s}{4}
\left(s^3-2s^2-4s+4\right).
\]
Let
\[
f(s)=s^3-2s^2-4s+4.
\]
On \((0,1)\),
\[
f'(s)=3s^2-4s-4<0,
\]
while
\[
f(0)=4,
\qquad
f(1)=-1.
\]
Hence there is a unique root \(s_0\in(0,1)\).

For \(s\ge s_0\), equivalently \(0<h\le h_0\), the \(A_h=C\) crossing occurs first. Its value is
\[
\mathcal F(h)
=
y_A
=
\frac{\sqrt{s^2+4}-s}{2}
=
\frac{\sqrt{5-h^2}-\sqrt{1-h^2}}{2}.
\]
The unique optimizer is
\[
d_*(h)=1-\mathcal F(h).
\]

For \(s\le s_0\), equivalently \(h_0\le h\le1\), the \(B_h=C\) crossing occurs first. Hence
\[
\mathcal F(h)=\frac{1+h^2}{2},
\qquad
d_*(h)=\frac{1-h^2}{2}.
\]

At \(s=s_0\), the two crossing points coincide, so
\[
A_h(d_*)=B_h(d_*)=C(d_*).
\]

The second branch is plainly strictly increasing. For the first branch, regarding it as a function of \(s\),
\[
\frac{d}{ds}
\frac{\sqrt{s^2+4}-s}{2}
=
\frac12\left(\frac{s}{\sqrt{s^2+4}}-1\right)<0,
\]
while \(s=\sqrt{1-h^2}\) decreases with \(h\). Hence the first branch is also strictly increasing.

Finally, expansion at \(h=0\) gives
\[
\mathcal F(h)
=
\frac{\sqrt5-1}{2}
+
\left(\frac14-\frac{\sqrt5}{20}\right)h^2
+
O(h^4),
\]
which is the stated quadratic refinement because
\[
\frac{\sqrt5-1}{2}=\frac1\varphi
\]
and
\[
\frac14-\frac{\sqrt5}{20}
=
\frac{5-\sqrt5}{20}.
\]

## Verification

The packaged `verify.py` computes the unique threshold root by bisection and obtains
\[
s_0\approx0.806063433525370,
\qquad
h_0\approx0.591829148600584.
\]

For \(999\) interior height samples it evaluates the three published fold terms at the claimed optimizer and checks the expected equality and dominance relations on each side of the threshold. At the threshold it verifies that all three terms agree.

It also minimizes the published three-term formula over fine shear grids at representative heights, checks strict increase of the closed profile over \(10{,}000\) height samples, and verifies the limiting quadratic coefficient numerically.

The replay output is:

`VERIFY_OK parallelogram folding height profile`

These computations are consistency checks. The all-height theorem follows from the monotone-crossing proof above.

## Relationship to prior work

Nowicka studied folding symmetry for parallelograms and obtained an earlier two-candidate formula leading to the claimed lower bound \(1/2\). Goenka, Moore, Sun, and White identified an omitted fold configuration, supplied the corrected three-term formula, and proved that the true parallelogram infimum is the unattained value
\[
\frac1\varphi.
\]

Their proof reaches that infimum by fixing the shear parameter and then letting the normalized height tend to zero. It does not optimize at fixed positive height, identify the unique optimal shear as a function of height, or identify the transition where all three fold mechanisms balance.

The present result is a sharp stability refinement of that extremal theorem: normalized height measures how far the parallelogram is from the degenerate extremizing regime, and the formula gives the exact folding-symmetry penalty at every such height.

Searches using fixed-height, normalized-height, parallelogram folding symmetry, golden-ratio stability, and the two exact branch formulas did not locate an equivalent profile.

## Limitations

The result is restricted to parallelograms and to normalized height relative to a longest side. It does not give an analogous stability profile for arbitrary centrally symmetric convex bodies.

The proof depends on the corrected three-fold classification for parallelograms from Goenka, Moore, Sun, and White. That published geometric classification is treated as a premise; the new work is the exact constrained optimization and phase-transition analysis.

Because the optimization after the published formula is elementary, an unindexed observation of the same profile remains possible. No such statement was found in the inspected primary papers or targeted searches.

## References

R. Goenka, K. Moore, W. R. Sun, and E. P. White, “On Axial Symmetry in Convex Bodies,” arXiv:2309.12597, first submitted 2023-09-22; Pacific Journal of Mathematics 341 (2026), 275–303, DOI 10.2140/pjm.2026.341.275.

M. Nowicka, “On the measure of axial symmetry with respect to folding for parallelograms,” Beiträge zur Algebra und Geometrie 53 (2012), 97–103, DOI 10.1007/s13366-011-0033-y.
