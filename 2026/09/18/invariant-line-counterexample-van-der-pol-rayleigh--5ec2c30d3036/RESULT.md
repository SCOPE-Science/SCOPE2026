# Invariant-line obstruction to a Van der Pol–Rayleigh limit-cycle conjecture

## Statement

Consider the planar system studied by Lu and Zhang,
\[
\dot x=y,\qquad
\dot y=-x-ay-(\alpha x^2-xy+\beta y^2)y,
\tag{1}
\]
with \(\alpha,\beta>0\). Their Conjecture 5.1 states that if
\[
a<0,\qquad 0<\alpha\beta<\frac14,
\]
then (1) has exactly one limit cycle, stable and hyperbolic.

The conjecture is false.

**Theorem.** Suppose \(0<\alpha\beta<1/4\). Let \(m>0\) solve
\[
\beta m^2-m+\alpha=0,
\tag{2}
\]
and set
\[
a=-\left(m+\frac1m\right).
\tag{3}
\]
Then the straight line
\[
L_m=\{(x,y):y=mx\}
\]
is invariant for (1), and system (1) has no periodic orbit.

Equivalently, the invariant-line obstruction occurs on the two parameter sheets
\[
\alpha\beta a^2+(\alpha+\beta)a+(\alpha-\beta)^2+1=0,
\tag{4}
\]
or
\[
a_\pm=
\frac{-(\alpha+\beta)\pm|\alpha-\beta|\sqrt{1-4\alpha\beta}}
     {2\alpha\beta}.
\tag{5}
\]
Every value in (5) is negative.

A particularly simple counterexample is
\[
\boxed{\alpha=\beta=\frac1{10},\qquad a=-10}.
\]
Here
\[
m_\pm=5\pm2\sqrt6
\]
both satisfy (2)-(3), so there are two invariant lines through the origin and there is no limit cycle.

## Proof

Put
\[
H(x,y)=y-mx.
\]
On the line \(H=0\), where \(y=mx\),
\[
\begin{aligned}
\dot H
&=\dot y-m\dot x\\
&=x(-1-am-m^2)-m(\alpha-m+\beta m^2)x^3.
\end{aligned}
\]
Conditions (2) and (3) make both coefficients vanish, hence \(\dot H=0\) on \(L_m\). Thus \(L_m\) is invariant. Along it,
\[
\dot x=mx,
\]
so every nonzero orbit on \(L_m\) is nonperiodic.

System (1) has only one finite equilibrium: \(\dot x=0\) gives \(y=0\), and then \(\dot y=0\) gives \(x=0\). If a nonconstant periodic orbit \(\Gamma\) existed, its planar Poincaré index would be \(+1\); therefore the interior of \(\Gamma\) would contain an equilibrium. The unique finite equilibrium is the origin, so \(0\) would lie inside \(\Gamma\).

Any Jordan curve whose interior contains the origin intersects every complete line through the origin, in particular \(L_m\). But a trajectory of the smooth vector field (1) cannot cross the distinct invariant trajectory set \(L_m\): uniqueness of solutions forbids such an intersection away from the equilibrium, while a nonconstant periodic orbit cannot pass through the equilibrium itself. This contradiction excludes periodic orbits.

To obtain (4), eliminate \(m\) from
\[
m^2+am+1=0,\qquad \beta m^2-m+\alpha=0.
\]
Their resultant is
\[
\alpha\beta a^2+(\alpha+\beta)a+(\alpha-\beta)^2+1.
\]
Its discriminant as a quadratic in \(a\) is
\[
(\alpha-\beta)^2(1-4\alpha\beta),
\]
giving (5). Alternatively, negativity follows directly from (3), since \(m>0\).

For \(\alpha=\beta=1/10\), (2) becomes
\[
m^2-10m+1=0,
\]
whose roots are \(5\pm2\sqrt6\), and (3) gives \(a=-10\) for both.

## Relation to the source paper

Lu and Zhang prove that (1) has at most one limit cycle and isolate the region
\[
a<0,\qquad 0<\alpha\beta<1/4
\]
as the remaining difficult regime. They prove existence and uniqueness for sufficiently small negative \(a\), then state Conjecture 5.1 for the whole region. The explicit point
\[
(\alpha,\beta,a)=\left(\frac1{10},\frac1{10},-10\right)
\]
lies strictly inside that conjectured parameter regime but has no limit cycle.

The obstruction is not a boundary case such as \(\alpha=0\) or \(\beta=0\): it occurs for strictly positive \(\alpha,\beta\) on codimension-one sheets inside the unresolved region.

## Prior literature and originality boundary

Chen, Fang and Zhang (2025) study the more general Rayleigh–Liénard family
\[
\dot x=y,\qquad
\dot y=-x-(b_1+b_2x^2+b_3xy+b_4y^2)y
\]
and state in the abstract that they complete the classification of invariant algebraic curves when \(b_3\ne0\). That family contains (1). Consequently, existence or classification of invariant algebraic straight lines in this family is **not** claimed as new here.

The contribution claimed here is narrower: the invariant-line condition above gives a no-periodic-orbit obstruction in the parameter regime of Lu–Zhang Conjecture 5.1 and yields an explicit continuum of counterexamples to that 2026 conjecture. Targeted searches found no correction, comment, or later source explicitly recording this contradiction.

The complete text of the 2025 Advances in Mathematics paper was not inspected. Because it treats exactly the ambient four-parameter family, it is the strongest residual originality risk: its full theorem may contain the straight-line parameter condition, and possibly consequences not visible in the accessible abstract. The present originality claim therefore does not include the invariant-line classification itself and remains to the best of our knowledge.

## Limitations

This result disproves the universal statement of Conjecture 5.1 but does not classify the complement of the obstruction sheets. It does not determine whether a unique stable limit cycle exists for all remaining parameters with \(a<0\) and \(0<\alpha\beta<1/4\), nor does it locate other possible global bifurcation surfaces.

The no-periodic-orbit conclusion uses only the exact invariant line, uniqueness of solutions, the uniqueness of the finite equilibrium, and the planar index property of periodic orbits. No numerical simulation is used as evidence.

## References

1. Y. Lu and R. Zhang, *Global dynamics of a modified hybrid Van der Pol-Rayleigh oscillator II*, Electronic Journal of Differential Equations 2026, No. 25, 1–17. DOI: https://doi.org/10.58997/ejde.2026.25
2. H. Chen, L. Fang and X. Zhang, *Invariant algebraic curves of a class of Rayleigh-Liénard systems*, Advances in Mathematics 483 (2025), 110667. DOI: https://doi.org/10.1016/j.aim.2025.110667
