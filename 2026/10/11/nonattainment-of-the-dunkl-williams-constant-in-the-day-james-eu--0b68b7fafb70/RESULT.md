# Nonattainment of the Dunkl--Williams constant in the Day--James Euclidean--sup plane
## Finding
Let \(X=\ell_2-\ell_\infty\) be the real Day--James plane
\[
\|(s,t)\|_{2,\infty}=
\begin{cases}
\sqrt{s^2+t^2},&st\ge0,\\
\max\{|s|,|t|\},&st\le0.
\end{cases}
\]
Its Dunkl--Williams constant is the known value \(DW(X)=2\sqrt2\), but the defining supremum is not attained: there are no nonzero distinct \(x,y\in X\) for which
\[
\frac{\|x\|+\|y\|}{\|x-y\|}
\left\|\frac{x}{\|x\|}-\frac{y}{\|y\|}\right\|
=2\sqrt2.
\]
Equivalently, in the unit-sphere formula
\[
DW(X)=
\sup_{\substack{u,v\in S_X\\u+v\ne0}}
\frac{\|u+v\|}
{\min_{0\le t\le1}\|(1-t)u+tv\|},
\]
every admissible quotient is strictly smaller than \(2\sqrt2\), although an explicit sequence of such quotients converges to \(2\sqrt2\).

## Assumptions and scope
The scalar field is real. The norm is the Day--James norm
\[
\|(s,t)\|_{2,\infty}=
\begin{cases}
\sqrt{s^2+t^2},&st\ge0,\\
\max\{|s|,|t|\},&st\le0.
\end{cases}
\]
The Dunkl--Williams constant is
\[
DW(X)=
\sup_{\substack{x,y\ne0\\x\ne y}}
\frac{\|x\|+\|y\|}{\|x-y\|}
\left\|\frac{x}{\|x\|}-\frac{y}{\|y\|}\right\|.
\]
The numerical value \(DW(X)=2\sqrt2\) is due to Mizuguchi, Saito, and Tanaka. The new assertion is nonattainment of that sharp value.

## Proof
Mizuguchi, Saito, and Tanaka prove the equivalent unit-sphere representation
\[
DW(X)=
\sup_{\substack{u,v\in S_X\\u+v\ne0}}
\frac{\|u+v\|}
{\min_{0\le t\le1}\|(1-t)u+tv\|}.
\]
They also introduce, for a unit vector \(p\) and a Birkhoff--James orthogonal direction \(q\), an auxiliary quantity \(m(p,q)\), and prove
\[
DW(X)=2\sup_{p\in S_X}M(p),
\qquad
M(p)=\sup_{q\perp_B p}m(p,q).
\]
Their frame reduction shows that every value \(m(p,q)\) is bounded above by \(M(e)\) at some extreme point \(e\) of the two-dimensional unit ball.

For the present Day--James plane, the extreme-point calculation is explicit. Put
\[
a^2+b^2=1,\qquad \frac1{\sqrt2}<a<1,\qquad b>0,
\]
\[
p_a=(a,b),\qquad q_a=(b,-a),\qquad w=(1,-1).
\]
The source proves that all extreme-point contributions reduce, up to isometries and endpoint limits, to
\[
m(p_a,q_a)
\quad\text{and}\quad
m(w,p_a).
\]
If \(a\le2b\), then
\[
m(p_a,q_a)=\frac1a<\sqrt2.
\]
If \(a>2b\), then
\[
m(p_a,q_a)<a+b<\sqrt2.
\]
The other branch satisfies
\[
m(w,p_a)=a(a+b)<\sqrt2.
\]
The omitted endpoints are also strict. At
\[
p=\left(\frac1{\sqrt2},\frac1{\sqrt2}\right)
\]
the unique Birkhoff direction is proportional to
\[
\left(\frac1{\sqrt2},-\frac1{\sqrt2}\right),
\]
and the equal-level symmetry gives \(m=1\). At the axis endpoints, direct evaluation of the equal-level pairs likewise gives \(m=1\). The corner \(w=(1,-1)\) is covered by the continuous branch above, whose compact closure has maximum strictly below \(\sqrt2\).

Hence
\[
M(e)<\sqrt2
\]
for every extreme point \(e\). By the frame-reduction inequality, no unit-sphere quotient can equal \(2\sqrt2\). Indeed, equality in the unit-sphere quotient would force the intermediate \(m\)-value in the proof of the representation to be \(\sqrt2\), and then the frame reduction would force some extreme point \(e\) to satisfy \(M(e)\ge\sqrt2\), a contradiction.

It remains to exhibit sharp approximation. Choose
\[
\frac1{\sqrt2}<a<1,\qquad b=\sqrt{1-a^2},
\qquad a\le2b.
\]
The source gives
\[
m(p_a,q_a)=\frac1a.
\]
More explicitly, take any
\[
\mu\ge\frac{a+b}{a-b},
\qquad
\lambda=-\mu+\frac{2b}{a},
\qquad
r=\mu a-b,
\]
and define
\[
u=\frac{p_a+\lambda q_a}{r},
\qquad
v=\frac{p_a+\mu q_a}{r}.
\]
The source's equal-level formulas give \(\|u\|=\|v\|=1\). The segment joining \(u\) and \(v\) has minimum norm \(1/r\), while
\[
\|u+v\|=\frac{2}{ar}.
\]
Therefore the unit-sphere quotient is exactly
\[
\frac{2}{a}.
\]
Taking \(a\downarrow1/\sqrt2\) yields quotients converging to \(2\sqrt2\), but every finite member remains strictly smaller.

Finally, if the original defining quotient were attained at nonzero distinct \(x,y\), set
\[
u=\frac{x}{\|x\|},
\qquad
v=-\frac{y}{\|y\|},
\qquad
t=\frac{\|y\|}{\|x\|+\|y\|}.
\]
Its value is
\[
\frac{\|u+v\|}{\|(1-t)u+tv\|},
\]
which is at most the corresponding unit-sphere quotient with the denominator minimized over \(t\). Attainment of the global value would therefore force attainment in the unit-sphere formula, already ruled out.

## Verification
The proof uses the complete extreme-point and Birkhoff-direction reduction from the cited full text, together with the source's exact branch formulas.

The strictness mechanism is explicit:
\[
\frac1a<\sqrt2
\quad\text{for}\quad
a>\frac1{\sqrt2},
\]
and the second branch is strictly bounded by \(a+b<\sqrt2\). The corner branch is also strictly below \(\sqrt2\). Endpoint checks give \(m=1\).

The approximating sequence is exact rather than numerical: for every admissible \(a\), the displayed unit pair has quotient \(2/a\), which tends monotonically to \(2\sqrt2\) as \(a\downarrow1/\sqrt2\).

## Relationship to prior work
Mizuguchi, Saito, and Tanaka introduced the calculation framework used here and proved
\[
DW(\ell_2-\ell_\infty)=2\sqrt2.
\]
Their proof contains the exact strict branch inequalities and the limiting supremum needed for the present argument, but it states the value rather than the nonattainment conclusion; searches within the complete accessible text for attainment or maximizing-pair terminology found no such statement.

Tanaka's later paper develops the frame of the unit ball as a general tool for Dunkl--Williams calculations and confirms the two-dimensional extreme-point role, but it does not specialize to this nonattainment question.

A 2026 preprint titled “Some results on the Dunkl-Williams constant” is a residual comparison risk. The accessible summary says that it compiles formulas and computes values for several two-dimensional spaces, specifically mentioning \(\ell_2-\ell_1\) and a dodecagonal example. The full text was not inspected in this run, so no claim is made that it excludes the present nonattainment statement.

## Limitations
The result is specific to the real Day--James plane \(\ell_2-\ell_\infty\). It does not classify all maximizing sequences, only proves nonattainment and provides one explicit sharp sequence.

The 2026 compilation preprint remains a bibliographic residual because only summary-level material was available in the checked evidence. This does not affect the proof, which depends only on the complete 2013 source and direct endpoint calculations.

## References
1. H. Mizuguchi, K.-S. Saito, and R. Tanaka, “On the calculation of the Dunkl--Williams constant of normed linear spaces,” *Open Mathematics* 11 (2013), 1212--1227, DOI 10.2478/s11533-013-0238-4; published online 2013-04-26.
2. R. Tanaka, “On the frame of the unit ball of Banach spaces,” *Open Mathematics* 12 (2014), 1700--1713, DOI 10.2478/s11533-014-0437-7.
