# Endpoint conditions certify the continuous cyclic chain
## Finding
Consider the continuous model in Section 7 of Lian--Xue--Yuan. Under the static inequalities of their (5.15) and the terminal branch (5.18), set
\[
\kappa=1-u-v,\qquad D=v-d,
\]
and use their continuous variables
\[
R(t)=R_0e^{Dt},\qquad Y(t)=Y_0e^{-\kappa t},\qquad
E(t)=\frac{D\kappa}{\kappa R(t)+D Y(t)-1}.
\]
Recover
\[
r(t)=E(t)R(t),\qquad y(t)=E(t)Y(t),\qquad x(t)=v-r(t),
\]
and define
\[
L=r-y,\qquad A=\kappa+L=1-u-x-y,\qquad B=D-L=x+y-d.
\]
If \(s>0\) satisfies the exact endpoint equations
\[
R(s)=R_f,\qquad Y(s)=Y_f
\]
from (7.3), then all pointwise feasibility requirements imposed in Section 7 hold on the whole interval \([0,s]\):
\[
E>0,\quad x>0,\quad y>0,\quad 1-x-y>0,\quad A>0,\quad B>0,
\]
and the denominator \(\kappa R+D Y-1\) never vanishes. Moreover, \(A\) is strictly increasing, whereas \(B\), \(x\), and \(y\) are strictly decreasing.

Thus an exact solution of the two endpoint equations is automatically pathwise feasible. The infinitely many trajectory inequalities do not require separate sampling or interval certification.

## Assumptions and scope
The parameters \(u,v,c,d\) satisfy the strict inequalities used in (5.15) of the source:
\[
0<u<v<d<1-u,\qquad u+v>d,
\]
\[
0<c<v,\qquad c+d<1-u,\qquad d(\kappa+D)>\kappa c,
\]
with \(\kappa=1-u-v\) and \(D=v-d\). The terminal parameters are on the source's branch (5.18), so the endpoint coordinates \(R_f,Y_f\) are those obtained from the terminal state \((x,y)=(u,v)\).

The theorem is conditional on exact satisfaction of the endpoint equations. It does not certify the rounded decimal parameters printed in the source, does not assert optimality of the continuous objective, and does not establish convergence of finite chains to the continuous model.

## Proof
Put
\[
Q(t)=\kappa R(t)+D Y(t)-1.
\]
The source assumptions imply
\[
\kappa>0,\qquad D<0,\qquad \kappa+D>0.
\]
At \(t=0\),
\[
r(0)=v-c>0,\qquad y(0)=d>0,
\]
\[
E(0)=d(\kappa+D)-\kappa c>0,
\]
\[
A(0)=1-u-c-d>0,\qquad B(0)=c>0.
\]
In particular \(Q(0)=D\kappa/E(0)<0\).

We first exclude a denominator singularity without assuming any of the differential sign conclusions below. Since
\[
\frac{R(t)}{Y(t)}=\frac{R_0}{Y_0}e^{(D+\kappa)t},
\]
the ratio \(R/Y\) is strictly increasing. Exact endpoint matching and the source definitions (5.19) give
\[
\frac{R(s)}{Y(s)}=\frac{R_f}{Y_f}=\frac{v-u}{v}<1.
\]
Hence \(R(t)<Y(t)\) for every \(0\le t\le s\). Moreover, on the terminal branch (5.18), the source computes
\[
E_f=\frac{(1-\tau)(3d^2-3d+1)}{1+\tau+\tau^2}>0,
\]
so
\[
Q(s)=\kappa R_f+D Y_f-1=\frac{D\kappa}{E_f}<0.
\]
Direct differentiation gives
\[
Q'(t)=D\kappa\bigl(R(t)-Y(t)\bigr)>0
\]
on \([0,s]\). Thus \(Q(t)\le Q(s)<0\) throughout the interval. The denominator never vanishes, and therefore
\[
E(t)=\frac{D\kappa}{Q(t)}>0
\]
for all \(t\in[0,s]\). Since \(R,Y>0\), this also gives \(r,y>0\) on the whole interval.

With global regularity established, differentiation gives
\[
E'=-LE,\qquad r'=rB,\qquad y'=-yA.
\]
Consequently
\[
L'=rB+yA,\qquad A'=rB+yA,\qquad B'=-(rB+yA),
\]
and
\[
A+B=\kappa+D.
\]

Now \(A\) cannot cross from positive to nonpositive. Indeed, if \(A=0\), then
\[
B=\kappa+D>0
\]
and therefore
\[
A'=rB>0.
\]
Hence \(A(t)>0\) throughout \([0,s]\).

At any zero of \(B\), the identity \(A+B=\kappa+D\) gives \(A=\kappa+D>0\), and therefore
\[
B'=-yA<0.
\]
Thus every zero of \(B\) would be a crossing from positive to negative. Exact endpoint matching gives \((x(s),y(s))=(u,v)\), so
\[
B(s)=u+v-d>0.
\]
Starting from \(B(0)=c>0\), a zero would force \(B\) negative afterward and a later return to positive would require a zero with nonnegative derivative, which is impossible. Hence \(B(t)>0\) on \([0,s]\).

It follows that
\[
A'=rB+yA>0,\qquad B'=-(rB+yA)<0,
\]
and
\[
x'=-rB<0,\qquad y'=-yA<0.
\]
Exact endpoint matching gives \(x(s)=u>0\) and \(y(s)=v>0\), hence \(x,y>0\) on the whole interval. Finally,
\[
1-x-y=u+A>0.
\]
This proves all claimed feasibility inequalities and monotonicities.

## Verification
The accompanying `verify.py` differentiates the rational-exponential definitions symbolically and checks the identities
\[
E'=-LE,\quad r'=rB,\quad y'=-yA,\quad A'=rB+yA,\quad B'=-(rB+yA),\quad A+B=\kappa+D.
\]
It also checks the stated initial identities algebraically. The checker is supplementary: the global denominator argument and sign proof above are analytic.

## Relationship to prior work
Lian--Xue--Yuan derive the finite recurrence and a finite-step sign-control lemma in Section 5, then introduce the continuous model in Section 7. For their displayed continuous numerical candidate they explicitly report that quadrature and node checks do not establish pathwise feasibility or optimality, and they list the pointwise inequalities that must hold throughout the interval. The result here shows that, conditional on exact endpoint matching, those pathwise inequalities follow from the continuous flow and endpoint signs; the continuous feasibility problem reduces to certification of the two endpoint equations.

The finite-step lemma in Section 5 is related but does not itself imply this continuous statement: a limiting argument would require a justified passage to the continuous curve, while the proof here works directly with the Section 7 formulas.

## Limitations
No claim is made that the rounded decimal candidate printed in arXiv:2609.06558v1 satisfies the endpoint equations exactly. No lower bound for a finite non-separable family is improved here. Attainability of the continuous candidate, optimality of its objective value, and convergence from finite chains remain open under this result.

## References
1. Yanlu Lian, Fei Xue, Qihui Yuan, *Non-Separable Homothetic Triangles, Part I: Constructions and Lower Bounds*, arXiv:2609.06558v1, 2026. In particular Sections 5 and 7.
