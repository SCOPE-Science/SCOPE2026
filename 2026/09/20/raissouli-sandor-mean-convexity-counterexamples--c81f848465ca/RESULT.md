# Quartic-profile counterexamples to Raïssouli–Sándor Problem 4(ii)

## Result

Let
\[
A(x,y)=\frac{x+y}{2},
\qquad
t=\frac{x-y}{x+y}\in(-1,1),
\]
and, for a parameter \(0<c\le 1/8\), define
\[
q_c(t)=c\,t^2(2-t^2),
\qquad
M_c^\pm(x,y)=A(x,y)\bigl(1\pm q_c(t)\bigr).
\]

Raïssouli and Sándor (2016, Problem 4(ii)) asked whether every symmetric,
homogeneous, strictly monotone mean below \(A\) must be strictly concave
and every such mean above \(A\) must be strictly convex.

**Theorem.** For every \(0<c\le 1/8\), both \(M_c^-\) and \(M_c^+\) are
\(C^\infty\), symmetric, homogeneous, strictly monotone bivariate means.
For all \(x\ne y\),
\[
M_c^-(x,y)<A(x,y)<M_c^+(x,y).
\]
Nevertheless, each of \(M_c^-\) and \(M_c^+\) is neither convex nor
concave. Hence both implications in Problem 4(ii) are false.

Thus the failure is not an isolated example: it occurs in a full
one-parameter family on each side of the arithmetic mean.

## Proof

Put \(s=x+y\). Symmetry follows because \(q_c\) is even, and homogeneity
is immediate from the scale invariance of \(t=(x-y)/(x+y)\).

For \(0<|t|<1\),
\[
0<q_c(t)
=c\,t^2(2-t^2)
\le \frac18\,2t^2
=\frac{t^2}{4}
<|t|.
\]
Since
\[
\min(x,y)=A(x,y)(1-|t|),\qquad
\max(x,y)=A(x,y)(1+|t|),
\]
we obtain, off the diagonal,
\[
\min(x,y)<M_c^-(x,y)<A(x,y)<M_c^+(x,y)<\max(x,y).
\]
On the diagonal both \(M_c^\pm\) equal \(A=x=y\). Hence both maps are
strict means.

It remains to verify strict monotonicity. Write
\[
f_\pm(t)=1\pm q_c(t),
\qquad
M_c^\pm(x,y)=\frac{x+y}{2}f_\pm(t).
\]
A direct differentiation gives
\[
\partial_x M_c^\pm
=\frac12\bigl(f_\pm(t)+(1-t)f_\pm'(t)\bigr),
\]
\[
\partial_y M_c^\pm
=\frac12\bigl(f_\pm(t)-(1+t)f_\pm'(t)\bigr).
\]
Now \(0\le q_c(t)<c\le1/8\), so \(f_\pm(t)\ge7/8\). Also
\[
q_c'(t)=4ct(1-t^2).
\]
The elementary maximum
\[
\max_{|t|\le1}|t|(1-t^2)=\frac{2}{3\sqrt3}
\]
therefore yields
\[
|f_\pm'(t)|\le \frac{8c}{3\sqrt3}
\le\frac1{3\sqrt3}<\frac15.
\]
Because \(|1\pm t|<2\),
\[
\partial_xM_c^\pm,\ \partial_yM_c^\pm
>
\frac12\left(\frac78-\frac25\right)
=\frac{19}{80}>0.
\]
Thus both means are strictly increasing in each variable and hence
strictly monotone.

Finally set
\[
\phi_\pm(x)=M_c^\pm(x,1).
\]
With \(t=(x-1)/(x+1)\), a direct calculation gives
\[
\phi_+''(x)
=
-\frac{16c(x^2-4x+1)}{(x+1)^5},
\qquad
\phi_-''(x)
=
\frac{16c(x^2-4x+1)}{(x+1)^5}.
\]
For \(x>1\), the factor \(x^2-4x+1\) is negative on
\[
1<x<2+\sqrt3
\]
and positive on
\[
x>2+\sqrt3.
\]
Consequently each one-variable section \(x\mapsto M_c^\pm(x,1)\) has
both curvature signs. Therefore neither \(M_c^+\) nor \(M_c^-\) can be
convex or concave as a bivariate function.

This proves the theorem.

## Structural explanation

For any sufficiently regular even profile \(f\) with
\[
M_f(x,y)=\frac{x+y}{2}
f\!\left(\frac{x-y}{x+y}\right),
\]
the pointwise order relative to \(A\) is controlled by the sign of
\(f-1\), while the curvature of the one-variable section
\(\phi(x)=M_f(x,1)\) is controlled by
\[
\phi''(x)
=
\frac{2}{(x+1)^3}
f''\!\left(\frac{x-1}{x+1}\right).
\]
Thus being everywhere above or below \(A\) imposes no general sign
condition on curvature. The quartic profiles \(1\pm q_c\) make this
separation explicit while preserving the mean and strict-monotonicity
constraints.

## Relation to prior literature and originality

Raïssouli and Sándor explicitly posed Problem 4(ii) in 2016 after
observing that their standard symmetric homogeneous monotone examples
below \(A\) were concave and those above \(A\) were convex. Their paper
also exhibited a nonmonotone mean that is neither convex nor concave,
so strict monotonicity is an essential part of the stated problem.

A same-year paper of Raïssouli and Rezgui characterized broad classes of
homogeneous symmetric strict monotone bivariate means, but no located
statement there supplies the order-versus-curvature implication or the
counterexamples above.

Current-status searches used the exact wording of Problem 4(ii), the
source title and DOI, the phrases “symmetric homogeneous strictly
monotone mean,” “neither convex nor concave,” and algebraically
equivalent quartic-profile expressions. No located source stated these
counterexamples or a stronger theorem that would make them immediate.
The originality assessment is therefore **to the best of our
knowledge**, not a claim of exhaustive literature coverage.

## Limitations

- The result answers Problem 4(ii) negatively but does not address
  Problem 4(i), concerning removal of the \(C^2\) assumption from the
  duality proposition.
- The construction does not classify additional hypotheses under which
  order relative to the arithmetic mean might force convexity or
  concavity.
- Equivalent prior coverage under different terminology or in weakly
  indexed literature remains a residual originality risk.


## Reproducibility

All identities used in the proof are elementary differentiations. For
the curvature calculation, substituting
\(t=(x-1)/(x+1)\) into
\(f_\pm''(t)=\pm4c(1-3t^2)\) gives the displayed formula for
\(\phi_\pm''\). The strict-monotonicity bound follows from maximizing
\(u(1-u^2)\) on \(0\le u\le1\).

## References

1. M. Raïssouli and J. Sándor,
   “Sub-super-stabilizability of certain bivariate means via
   mean-convexity,” *Journal of Inequalities and Applications*
   **2016**, 273 (2016). DOI: 10.1186/s13660-016-1212-z.
2. M. Raïssouli and A. Rezgui,
   “Characterization of homogeneous symmetric monotone bivariate
   means,” *Journal of Inequalities and Applications*
   **2016**, 217 (2016). DOI: 10.1186/s13660-016-1150-9.
