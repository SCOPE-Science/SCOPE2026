# A hard prey-feasibility barrier in a harvested herd-behavior predator-prey DAE

## Finding

Consider the differential-algebraic system
\[
x'(t)
=
x(t)\bigl(1-x(t-\tau_1)\bigr)
-\sqrt{x(t)}\,y(t)
-e(t)x(t),
\]
\[
y'(t)
=
-d\,y(t)^2
+b\sqrt{x(t-\tau_2)}\,y(t),
\]
\[
0
=
e(t)\bigl(p\,x(t)-c\bigr)-m,
\]
with
\[
m>0.
\]

The algebraic equation gives, at every finite point of a classical solution,
\[
e(t)
=
\frac{m}{p\,x(t)-c}.
\]
Therefore every finite continuous solution that begins with
\[
e(0)>0
\]
lies on the branch
\[
x(t)>\frac{c}{p},
\qquad
e(t)>0
\]
for as long as that classical solution exists.

The level
\[
x=\frac{c}{p}
\]
is a singular barrier. A continuous trajectory cannot pass from
\[
x>\frac{c}{p}
\]
to
\[
x<\frac{c}{p}
\]
while keeping \(e\) finite and satisfying the algebraic constraint.

The source's Figure 6(a) is therefore incompatible with the printed DAE as a finite classical trajectory. Its caption states that the prey dies out and the harvest effort fluctuates wildly from the initial values
\[
0.2,\quad 0.5,\quad 1.2,
\]
and the plotted harvest-effort curve enters the negative half-plane. Starting from the positive-effort branch, neither prey extinction nor finite negative effort can be reached without encountering the singular manifold first.

For the source parameters
\[
c=0.02,
\qquad
p=2500,
\]
the barrier is
\[
\frac{c}{p}
=
8\times10^{-6}.
\]

There is also a direct initial-consistency diagnostic. If the source's Figure 6 triples are read in the model order
\[
(x,y,e),
\]
then with
\[
m=604.33,
\qquad
p=2500,
\qquad
c=0.02,
\]
the algebraic equation requires
\[
e_0
=
\frac{604.33}{2500(0.2)-0.02}
\approx
1.208708348333933
\]
for
\[
x_0=0.2,
\]
and
\[
e_0
=
\frac{604.33}{2500(0.8)-0.02}
\approx
0.302168021680217
\]
for
\[
x_0=0.8.
\]
The displayed value
\[
e_0=1.2
\]
therefore has algebraic residuals
\[
-4.354
\]
and
\[
1795.646,
\]
respectively.

## Assumptions and scope

The barrier statement assumes a finite continuous classical solution of the printed differential-algebraic system, with the algebraic equation enforced at every time.

The source explicitly assumes
\[
e(0)>0.
\]
Under that assumption and
\[
m>0,
\]
the initial state must satisfy
\[
p\,x(0)-c>0.
\]

The conclusion does not forbid a numerical code from stepping from one side of the singular manifold to the other. It says that such a discrete jump cannot represent a continuous finite classical trajectory of the stated DAE through the singularity.

The conclusion also does not assert that prey extinction is biologically impossible under another harvesting model. A regime-switching rule, inequality-constrained effort model, or different economic closure could permit different behavior.

## Proof

From
\[
e(t)\bigl(p\,x(t)-c\bigr)=m
\]
and
\[
m>0,
\]
neither factor on the left can vanish at a finite classical state.

At the initial time,
\[
e(0)>0
\]
implies
\[
p\,x(0)-c>0,
\]
and hence
\[
x(0)>\frac{c}{p}.
\]

Suppose a finite continuous classical solution later reached
\[
x(t_1)\le\frac{c}{p}.
\]
Continuity of \(x\) would give a first time \(t_*\) with
\[
x(t_*)=\frac{c}{p}.
\]
At that time the algebraic equation would read
\[
0=m,
\]
which is impossible because
\[
m>0.
\]
Equivalently,
\[
e(t)
=
\frac{m}{p\,x(t)-c}
\]
diverges as the positive branch approaches the singular level.

Therefore
\[
x(t)>\frac{c}{p}
\]
for every time on which the finite classical solution exists. The denominator remains positive, so
\[
e(t)>0
\]
throughout the same interval.

Since
\[
0<\frac{c}{p},
\]
a trajectory starting on this branch cannot continuously reach
\[
x=0.
\]
Likewise it cannot attain a finite negative value of \(e\), because the sign of
\[
e=\frac{m}{p\,x-c}
\]
cannot change without the denominator passing through zero.

This proves the barrier and the incompatibility with a plotted trajectory that reaches prey extinction and finite negative harvest effort.

The initial-consistency calculations are obtained by substituting the source parameter values directly into
\[
e_0=\frac{m}{p\,x_0-c}.
\]

## Verification

The bundled `verify.py` uses exact rational arithmetic for every source-parameter calculation.

It verifies
\[
\frac{c}{p}
=
\frac{1}{125000}
=
8\times10^{-6},
\]
and, for the two prey initial values shown in Figure 6,
\[
e_0(0.2)
=
\frac{60433}{49998}
\approx
1.208708348333933,
\]
\[
e_0(0.8)
=
\frac{223}{738}
\approx
0.302168021680217.
\]

For the displayed harvest-effort value
\[
e_0=1.2,
\]
the exact residuals of
\[
e_0(p\,x_0-c)-m
\]
are
\[
-\frac{2177}{500}
=
-4.354
\]
and
\[
\frac{897823}{500}
=
1795.646.
\]

These computations verify the numerical diagnostics only. The noncrossing result is the algebraic-continuity proof above and does not rely on a finite experiment.

## Relationship to prior work

Meng and Meng introduce the delayed herd-behavior predator-prey DAE studied here. Their system contains the algebraic economic constraint
\[
e(p\,x-c)=m,
\]
their initial assumptions require positive initial effort, and their Figure 6 interprets one numerical trajectory as prey extinction accompanied by strongly varying harvest effort.

Singular differential-algebraic bioeconomic predator-prey models and feasibility-region analysis are established prior topics. Meng and Wu study a different singular predator-prey DAE with nonlinear predator harvesting and analyze singularity-induced bifurcation. Li, Chen, and Ye study another bioeconomic DAE with nonlinear prey harvesting. Those works establish the broader methodology and are not claimed as new here.

The source-specific contribution is the exact viability consequence of the particular algebraic closure
\[
e(p\,x-c)=m
\]
and its direct conflict with the reported Figure 6 extinction/negative-effort trajectory.

## Limitations

No simulation source code is available for inspection. The finding therefore concerns the trajectory as presented and interpreted in the article, not the internal implementation that produced the plot.

The initial-condition residual calculation assumes that the three values in the Figure 6 caption are listed in the model order
\[
(x,y,e).
\]
The hard barrier itself does not depend on that interpretation.

The result does not audit the paper's local bifurcation calculations away from the singular manifold and does not claim novelty for general DAE feasibility theory.

## References

1. X.-Y. Meng, F.-L. Meng, “Bifurcation analysis of a special delayed predator-prey model with herd behavior and prey harvesting,” AIMS Mathematics 6 (2021), 5695–5719. DOI: 10.3934/math.2021336.
2. X.-Y. Meng, Y.-Q. Wu, “Bifurcation analysis in a singular Beddington-DeAngelis predator-prey model with two delays and nonlinear predator harvesting,” Mathematical Biosciences and Engineering 16 (2019), 4031–4052. DOI: 10.3934/mbe.2019133.
3. M. Li, B. Chen, H. Ye, “A bioeconomic differential algebraic predator-prey model with nonlinear prey harvesting,” Applied Mathematical Modelling 42 (2017), 17–28. DOI: 10.1016/j.apm.2016.09.029.
