# Lambert-W boundary layer for high-tail Bohr–Rogosinski radii

## Finding

Fix
\[
m\in\mathbb N
\]
and
\[
0<p\le2.
\]
For each
\[
N\in\mathbb N,
\]
let
\[
R_{m,N}^{(p)}\in(0,1)
\]
be the sharp powered Bohr–Rogosinski radius determined by
\[
p\frac{1-r^m}{1+r^m}
=
\frac{2r^N}{1-r}.
\]

Then
\[
R_{m,N+1}^{(p)}>R_{m,N}^{(p)}
\]
for every \(N\), and
\[
R_{m,N}^{(p)}\longrightarrow1.
\]

Let
\[
\varepsilon_N=1-R_{m,N}^{(p)}.
\]
If \(W\) is the principal Lambert function, characterized on \((0,\infty)\) by
\[
W(x)e^{W(x)}=x,
\]
then the sharp boundary layer is
\[
N\varepsilon_N
=
2W\!\left(\frac{N}{\sqrt{pm}}\right)+o(1).
\]
Consequently,
\[
1-R_{m,N}^{(p)}
=
\frac{
2\log N
-
2\log\log N
-
\log(pm)
+
o(1)
}{N}.
\]

In particular, the convergence to \(1\) is not of pure order \(1/N\): the correct scale is
\[
\frac{\log N}{N},
\]
with a universal logarithmic correction
\[
-\frac{2\log\log N}{N}.
\]

## Assumptions and scope

The radius family is the sharp family in the powered Bohr–Rogosinski theorem for holomorphic mappings from the unit ball of a complex Banach space into the closed unit polydisc. The source theorem assumes
\[
m,N\in\mathbb N,
\qquad
0<p\le2,
\]
and proves that the displayed equation has a unique root in \((0,1)\), with that root being optimal.

The asymptotic statement here keeps \(m\) and \(p\) fixed while the tail index \(N\) tends to infinity. This is a different limit from the high-order Schwarz-map limit in which \(m\) tends to infinity with \(N\) fixed.

The conclusion concerns the exact sharp root itself, so it applies simultaneously to every setting in the source theorem having that same sharp radius equation.

## Proof

Define
\[
F_N(r)
=
p\frac{1-r^m}{1+r^m}
-
\frac{2r^N}{1-r},
\qquad
0<r<1.
\]
The first term is strictly decreasing in \(r\), and the second displayed positive quotient is strictly increasing. Hence
\[
F_N
\]
is strictly decreasing.

For fixed \(r\in(0,1)\),
\[
F_{N+1}(r)-F_N(r)
=
\frac{2r^N(1-r)}{1-r}
=
2r^N>0.
\]
At the root of \(F_N\), the function \(F_{N+1}\) is therefore positive. Since \(F_{N+1}\) is strictly decreasing and has a unique zero,
\[
R_{m,N+1}^{(p)}>R_{m,N}^{(p)}.
\]

The increasing sequence is bounded above by \(1\); write its limit as \(L\le1\). If \(L<1\), then along the roots
\[
\frac{2(R_{m,N}^{(p)})^N}{1-R_{m,N}^{(p)}}\longrightarrow0,
\]
while
\[
p\frac{1-(R_{m,N}^{(p)})^m}{1+(R_{m,N}^{(p)})^m}
\longrightarrow
p\frac{1-L^m}{1+L^m}>0,
\]
contradicting the root equation. Thus
\[
L=1.
\]

Set
\[
\varepsilon=\varepsilon_N
=
1-R_{m,N}^{(p)}
\]
and
\[
x=N\varepsilon.
\]
Since \(\varepsilon\to0\),
\[
\frac{1-(1-\varepsilon)^m}
{1+(1-\varepsilon)^m}
=
\frac{m}{2}\varepsilon
\bigl(1+O(\varepsilon)\bigr).
\]
The exact root equation therefore gives
\[
\frac{pm}{2}\varepsilon
\bigl(1+O(\varepsilon)\bigr)
=
\frac{2(1-\varepsilon)^N}{\varepsilon},
\]
or
\[
(1-\varepsilon)^N
=
\frac{pm}{4}\varepsilon^2
\bigl(1+O(\varepsilon)\bigr).
\]

Taking logarithms yields
\[
N\bigl[-\log(1-\varepsilon)\bigr]
=
2\log\frac1\varepsilon+O(1).
\]
For sufficiently small \(\varepsilon\),
\[
\varepsilon
\le
-\log(1-\varepsilon)
\le
2\varepsilon.
\]
The last two displays imply
\[
x\longrightarrow\infty
\]
and
\[
x=O(\log N).
\]
Hence
\[
N\varepsilon^2
=
\frac{x^2}{N}
\longrightarrow0.
\]

It follows that
\[
(1-\varepsilon)^N
=
\exp\!\left(
-x+O(N\varepsilon^2)
\right)
=
e^{-x}(1+o(1)).
\]
Substitution into the root equation gives
\[
\varepsilon^2 e^x
=
\frac4{pm}(1+o(1)).
\]
Since
\[
\varepsilon=\frac{x}{N},
\]
we obtain
\[
x^2e^x
=
\frac{4N^2}{pm}(1+o(1)).
\]
Taking the positive square root,
\[
\frac{x}{2}e^{x/2}
=
\frac{N}{\sqrt{pm}}(1+o(1)).
\]
The principal Lambert function is increasing and satisfies
\[
W(y(1+o(1)))-W(y)=o(1)
\qquad
(y\to\infty),
\]
so
\[
\frac{x}{2}
=
W\!\left(\frac{N}{\sqrt{pm}}\right)+o(1).
\]
Therefore
\[
N(1-R_{m,N}^{(p)})
=
2W\!\left(\frac{N}{\sqrt{pm}}\right)+o(1).
\]

Finally, the standard large-argument expansion
\[
W(y)=\log y-\log\log y+o(1)
\]
gives
\[
N(1-R_{m,N}^{(p)})
=
2\log N
-
2\log\log N
-
\log(pm)
+
o(1),
\]
which is the second formulation.

## Verification

The proof uses only the source's exact sharp-root equation and elementary asymptotic estimates.

The monotonicity check is exact: increasing \(N\) replaces \(r^N\) by the smaller quantity \(r^{N+1}\) at every fixed \(0<r<1\), while the root function remains strictly decreasing in \(r\).

The limit \(R_{m,N}^{(p)}\to1\) is forced by the root equation itself. Any limiting value strictly below \(1\) would leave the left-hand side bounded away from zero while the right-hand side tends to zero exponentially.

For the boundary-layer calculation, the only approximations are
\[
\frac{1-(1-\varepsilon)^m}
{1+(1-\varepsilon)^m}
=
\frac m2\varepsilon(1+O(\varepsilon))
\]
for fixed \(m\), and
\[
N\log(1-\varepsilon)
=
-N\varepsilon+O(N\varepsilon^2).
\]
The logarithmic form of the exact equation first proves
\[
N\varepsilon=O(\log N),
\]
so
\[
N\varepsilon^2\to0
\]
before the exponential approximation is used. Thus there is no circular asymptotic assumption.

Numerical root checks for representative values of \(p\), \(m\), and large \(N\) were used only as consistency checks; the theorem is proved for every fixed admissible \(p,m\).

## Relationship to prior work

Hamada, Honda, and Kohr prove the sharp powered radius equation used here for mappings into the polydisc and for the corresponding JB*-triple formulation. Their article discusses the limiting classical Bohr radius obtained by sending the Schwarz-map order to infinity in a special case, but does not give a large-\(N\) boundary-layer rate for the sharp radius.

Kayumov, Khammatova, and Ponnusamy proved the scalar \(p=1\) predecessor. They explicitly state
\[
R_{m,N}\longrightarrow1
\qquad
(N\to\infty),
\]
but do not quantify this convergence. The present result sharpens that qualitative limit and extends the asymptotic description across the full powered range
\[
0<p\le2
\]
of the later Banach-space theorem.

A 2026 refinement of the Banach-space inequalities studies a different improved functional whose sharp equation fixes the tail start at its first index. Its full text does not contain the large-tail asymptotic derived here.

The nearest published Bohr and Bohr–Rogosinski results found in targeted searches concern different radius families, finite sections, or different limiting parameters; none implies the Lambert-\(W\) high-tail law above.

## Limitations

The theorem is a fixed-\(m\), fixed-\(p\) asymptotic. Joint limits in which \(m\), \(p\), and \(N\) vary together can have different scaling profiles and are not covered.

Only the first two asymptotic levels are stated:
\[
2\log N
\quad\text{and}\quad
-2\log\log N-\log(pm).
\]
Further terms can be obtained by combining higher-order expansions of the root equation and of \(W\), but they are not needed for the claimed boundary layer.

The originality comparison covered the full lead article, the full scalar predecessor available through its publisher, the full closely related 2026 refinement, and targeted searches for equivalent Lambert-\(W\), high-tail, and sharp-radius formulations. Literature using substantially different notation remains a residual risk.

## References

1. H. Hamada, T. Honda, and M. Kohr, *Bohr–Rogosinski radius for holomorphic mappings with values in higher dimensional complex Banach spaces*, Analysis and Mathematical Physics 15 (2025), Article 64, DOI: 10.1007/s13324-025-01061-x.
2. I. R. Kayumov, D. M. Khammatova, and S. Ponnusamy, *Bohr–Rogosinski phenomenon for analytic functions and Cesáro operators*, Journal of Mathematical Analysis and Applications 496 (2021), 124824, DOI: 10.1016/j.jmaa.2020.124824.
3. L. Zeng and L. Xiong, *Improved Bohr-Rogosinski radius for holomorphic mappings with values in complex Banach spaces*, arXiv:2609.28357v1 (2026).
