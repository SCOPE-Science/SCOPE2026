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
On any interval where the denominator in \(E\) is nonzero, differentiation gives
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

First, \(A\) cannot cross from positive to nonpositive. Indeed, if \(A=0\), then
\[
B=\kappa+D>0
\]
and therefore
\[
A'=rB>0.
\]
Hence \(A(t)>0\) as long as the solution exists.

At any zero of \(B\), the identity \(A+B=\kappa+D\) gives \(A=\kappa+D>0\), and therefore
\[
B'=-yA<0.
\]
Thus, once \(B\) crosses zero, it can only cross from positive to negative and can never return to positive values. Exact endpoint matching recovers \((x(s),y(s))=(u,v)\), so
\[
B(s)=u+v-d>0.
\]
It follows that \(B(t)>0\) throughout \([0,s]\).

Now \(A'>0\) and \(B'<0\). Also
\[
x'=-rB<0,\qquad y'=-yA<0.
\]
Exact endpoint matching gives \(x(s)=u>0\) and \(y(s)=v>0\), hence \(x,y>0\) on the whole interval. Furthermore
\[
1-x-y=u+A>0.
\]

It remains to exclude a denominator singularity. On every interval of existence, \(A>0\) and \(B>0\) imply
\[
-\kappa<L<D.
\]
Thus \(L\) is bounded, and the scalar equation \(E'=-LE\) keeps \(E\) finite and strictly positive on every finite subinterval. Since
\[
\kappa R+DY-1=\frac{D\kappa}{E},
\]
the denominator stays strictly negative and cannot vanish. This also prevents finite-time loss of the continuous representation before \(s\), completing the proof.

## Verification
The accompanying `verify.py` differentiates the rational-exponential definitions symbolically and checks the identities
\[
E'=-LE,\quad r'=rB,\quad y'=-yA,\quad A'=rB+yA,\quad B'=-(rB+yA),\quad A+B=\kappa+D.
\]
It also checks the stated initial identities algebraically. The checker is supplementary: the global sign argument above is the proof.

## Relationship to prior work
Lian--Xue--Yuan derive the finite recurrence and a finite-step sign-control lemma in Section 5, then introduce the continuous model in Section 7. For their displayed continuous numerical candidate they explicitly report that quadrature and node checks do not establish pathwise feasibility or optimality, and they list the pointwise inequalities that must hold throughout the interval. The result here shows that, conditional on exact endpoint matching, those pathwise inequalities follow from the flow identities and endpoint signs; the continuous feasibility problem reduces to certification of the two endpoint equations.

The finite-step lemma in Section 5 is related but does not itself imply this continuous statement: a limiting argument would require a justified passage to the continuous curve, while the proof here works directly with the Section 7 differential identities.

## Limitations
No claim is made that the rounded decimal candidate printed in arXiv:2609.06558v1 satisfies the endpoint equations exactly. No lower bound for a finite non-separable family is improved here. Attainability of the continuous candidate, optimality of its objective value, and convergence from finite chains remain open under this result.

## References
1. Yanlu Lian, Fei Xue, Qihui Yuan, *Non-Separable Homothetic Triangles, Part I: Constructions and Lower Bounds*, arXiv:2609.06558v1, 2026. In particular Sections 5 and 7.
