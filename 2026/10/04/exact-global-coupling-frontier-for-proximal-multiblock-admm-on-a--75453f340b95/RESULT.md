# Exact global-coupling frontier for proximal multiblock ADMM on a three-state chain
## Finding

Consider the minimal scalar dynamics chain
\[
x_1=x_0,\qquad x_2=x_1
\]
with block costs
\[
f_0(x)=\frac a2x^2,\qquad
f_1(x)=-\frac a2x^2,\qquad
f_2(x)=\frac a2x^2,
\qquad a>0.
\]
Along the feasible set the objective is \(a x^2/2\), so the unique constrained minimizer is the origin.

Apply the Gauss--Seidel proximal multiblock ADMM of Li and Yuan with equal penalties \(\rho>0\) on both dynamics constraints and equal proximal parameters \(\eta>0\) on all three primal blocks. Define
\[
\chi=\frac a\rho,\qquad p=\rho\eta,
\]
and
\[
d=(\chi-2)(\chi+1),\qquad e=2\chi^2-\chi-4.
\]
Then the full five-dimensional linear iteration is Schur stable exactly when
\[
d p<3-\sqrt{\chi}
\]
and
\[
e p^2-6p-8<0.
\]

Let
\[
\chi_0=\frac{1+\sqrt{33}}4.
\]
The exact phase diagram is therefore
\[
\begin{cases}
p>0, & 0<\chi\le\chi_0,\\[2mm]
0<p<p_J(\chi), & \chi_0<\chi\le2,\\[2mm]
0<p<\min\{p_E(\chi),p_J(\chi)\}, & 2<\chi<9,\\[2mm]
\text{no stable }p>0, & \chi\ge9,
\end{cases}
\]
where
\[
p_E(\chi)=
\frac{3-\sqrt{\chi}}{(\chi-2)(\chi+1)}
\]
and, when \(e>0\),
\[
p_J(\chi)=
\frac{3+\sqrt{9+8e}}{e}.
\]

The individual primal subproblems are all strongly convex under the much weaker condition
\[
1+(2-\chi)p>0.
\]
Thus proximal convexification of every block is not sufficient for convergence of the coupled Gauss--Seidel primal-dual iteration.

A sharp example occurs at
\[
\chi=4.
\]
The middle block remains strongly convex for every
\[
0<p<\frac12,
\]
but the complete iteration is stable only for
\[
0<p<\frac1{10}.
\]
At the boundary \(p=1/10\), the decisive cubic factor is
\[
\frac{(6r-5)(5r^2-9r+5)}{25},
\]
so one root is \(5/6\) and the conjugate pair from \(5r^2-9r+5\) has modulus exactly one. For
\[
\frac1{10}<p<\frac12
\]
all primal block solves remain uniquely strongly convex while the coupled iteration has an eigenvalue modulus above one.

Even more sharply, for
\[
\chi\ge9
\]
there is no positive equal proximal parameter that makes the full iteration globally stable, although sufficiently small \(p\) still makes every individual subproblem strongly convex.

## Assumptions and scope

This is an exact linear analysis of the source algorithm on its smallest genuinely multiblock dynamics chain, with identity dynamics, scalar states, equal penalties, equal proximal parameters, and exact subproblem solves.

The problem satisfies the source paper's bounded-level structural assumption. Indeed, if a baseline penalty \(\rho^0=qa\) is chosen with \(q>1\), the Hessian of
\[
f_0(x_0)+f_1(x_1)+f_2(x_2)
+\frac{\rho^0}{2}\bigl[(x_1-x_0)^2+(x_2-x_1)^2\bigr]
\]
divided by \(a\) is
\[
\begin{pmatrix}
1+q&-q&0\\
-q&-1+2q&-q\\
0&-q&1+q
\end{pmatrix}.
\]
Its leading principal minors are
\[
1+q,\qquad q^2+q-1,\qquad q^2-1,
\]
which are positive for \(q>1\). The quadratic functions are smooth and the identity dynamics is globally smooth.

The result does not claim that the source paper's sequential parameter-selection procedure fails. That procedure permits unequal penalties and proximal parameters and is designed to guarantee convergence. The result instead gives the exact frontier of the natural equal-parameter specialization and isolates a global-coupling obstruction invisible to blockwise convexification.

## Proof

Set \(\rho=1\) by scaling; then \(a=\chi\) and the proximal Hessian coefficient is \(1/p\). For the state
\[
z_k=(x_0^k,x_1^k,x_2^k,\lambda_0^k,\lambda_1^k),
\]
the exact sequential subproblem solutions are
\[
x_0^+
=
\frac{x_1+\lambda_0+x_0/p}{\chi+1+1/p},
\]
\[
x_1^+
=
\frac{x_0^+ +x_2-\lambda_0+\lambda_1+x_1/p}
{-\chi+2+1/p},
\]
\[
x_2^+
=
\frac{x_1^+-\lambda_1+x_2/p}{\chi+1+1/p},
\]
followed by
\[
\lambda_0^+=\lambda_0+x_1^+-x_0^+,\qquad
\lambda_1^+=\lambda_1+x_2^+-x_1^+.
\]

The endpoint block Hessians are always positive. The middle block Hessian is positive exactly when
\[
1+(2-\chi)p>0.
\]

Direct elimination gives the characteristic polynomial as the product of a quadratic and a cubic. Up to positive leading factors, the quadratic is
\[
Q(r)
=
[1+(1+\chi)p]r^2-(2+\chi p)r+1.
\]
Its three quadratic Jury quantities are
\[
Q(1)=p,\qquad
Q(-1)=4+(1+2\chi)p,\qquad
[1+(1+\chi)p]-1=(1+\chi)p,
\]
so \(Q\) is Schur stable for every \(\chi,p>0\).

The remaining cubic is
\[
P(r)=A r^3+b r^2+3r-1,
\]
where
\[
A=1+3p-dp^2,\qquad
b=(\chi^2-2)p^2-3p-3.
\]
For a cubic with constant coefficient \(-1\), the first Schur step requires \(A>1\) and reduces stability to the quadratic
\[
R(r)=A_2r^2+B_2r+C_2,
\]
where
\[
A_2=A^2-1,\qquad
B_2=Ab+3,\qquad
C_2=3A+b.
\]
Exact factorization gives
\[
A-1=p(3-dp),
\]
\[
A_2-C_2
=
p^2\bigl[(dp-3)^2-\chi\bigr],
\]
\[
A_2+B_2+C_2
=
\chi p^2(2+3p-dp^2),
\]
\[
A_2-B_2+C_2
=
p(dp-3)(ep^2-6p-8),
\]
and
\[
C_2=p\bigl[6-(2\chi^2-3\chi-4)p\bigr].
\]

Combining \(A>1\) with \(A_2-C_2>0\) gives exactly
\[
dp<3-\sqrt{\chi}.
\]
Under this inequality, \(dp-3<0\), so
\[
A_2-B_2+C_2>0
\]
is equivalent to
\[
ep^2-6p-8<0.
\]
The remaining quadratic Jury inequalities are automatic. If \(d\le0\), then
\[
2+3p-dp^2>0.
\]
If \(d>0\), the first inequality gives \(dp<3\), hence
\[
dp^2<3p
\]
and again \(2+3p-dp^2>0\).

For \(A_2+C_2>0\), if
\[
h:=2\chi^2-3\chi-4\le0,
\]
then \(C_2>0\). If \(h>0\), write \(s=\sqrt{\chi}\). The condition \(h>0\) implies \(s>3/2\), and
\[
6d-h(3-s)
=
s(2s^4-3s^2+3s-4)>0,
\]
because the bracket is positive at \(s=3/2\) and strictly increasing thereafter. The first stability inequality therefore implies \(hp<6\), so again \(C_2>0\). Thus the two displayed inequalities are necessary and sufficient.

The piecewise phase diagram follows by inspecting the signs of \(d\) and \(e\). The positive root of
\[
e=0
\]
is
\[
\chi_0=\frac{1+\sqrt{33}}4.
\]
For \(e\le0\), the second condition is automatic for \(p>0\). For \(e>0\), it is equivalent to \(p<p_J(\chi)\). The first condition is automatic through \(\chi=2\), gives \(p<p_E(\chi)\) for \(2<\chi<9\), and becomes impossible for \(\chi\ge9\).

## Verification

The standalone script `artifacts/verify_multiblock_admm_frontier.py` uses exact rational arithmetic. For several rational \((\chi,p)\) pairs it constructs the full five-dimensional iteration matrix directly from the sequential ADMM updates, computes its exact characteristic polynomial by the Faddeev--LeVerrier recurrence, and checks the quadratic-times-cubic factorization.

It also verifies the exact Schur-factor identities, the \(\chi=4,\ p=1/10\) boundary factorization, and a point in the open region where every primal subproblem is strongly convex but the cubic fails the necessary-and-sufficient Schur test.

The finite replay is a consistency check only. The all-parameter result is the algebraic Schur proof above.

## Relationship to prior work

Li and Yuan define the proximal multiblock ADMM analyzed here for dynamics-chain constraints and provide a Lyapunov-based procedure that chooses penalties and proximal parameters successively to guarantee convergence. Their analysis is deliberately general and sufficient; it does not give an exact spectral phase diagram for equal parameters on a minimal quadratic chain. The present result quantifies why controlling each block subproblem separately is insufficient.

Ke, Ma, and Zhang study direct three-block ADMM on separable quadratic programs with a single linear constraint from a matrix-computation viewpoint, but their stated quadratic block matrices are positive semidefinite and their displayed method has no per-block proximal term. Their setting therefore does not contain the weakly convex middle block with the source algorithm's proximal regularization.

Chen, Cui, and Han establish convergence results for direct three-block ADMM with one weakly convex and two strongly convex objective functions. Their method is the direct extension rather than the proximal Gauss--Seidel dynamics-chain iteration used here, so their linear-rate theory does not determine this five-state characteristic polynomial or the equal-parameter frontier.

Cipolla and Gondzio give a linear-algebra interpretation of randomized multiblock ADMM for strongly convex quadratic programming, emphasizing Gauss--Seidel accuracy inside an inexact augmented-Lagrangian viewpoint. Their objective Hessian is positive definite and their randomized/inexact framework is different from the nonconvex three-state proximal recurrence here.

Zhang, Song, Cai, and Han propose an extended proximal three-block ADMM for nonconvex problems, but their algorithm updates the third primal variable twice per iteration and adds proximal terms only to the first two blocks. It is therefore not statement-equivalent to the Li--Yuan recurrence.

Targeted published-research database searches using the method name, three-state chain, weakly convex middle block, strong-convexity gap, Schur stability, spectral radius, and the derived curvature/penalty thresholds returned no statement implying the two-inequality frontier above.

## Limitations

The result is exact for one scalar identity-dynamics family with equal penalties and equal proximal parameters. It is not a robust stability theorem for arbitrary dynamics, unequal parameters, higher-dimensional noncommuting blocks, or nonlinear subproblems.

The equal-parameter obstruction does not contradict the source's convergence theorem, whose parameter-selection procedure is asymmetric and sufficiently conservative by design.

A 2018 paper on three-block separable quadratic ADMM is highly relevant historically. Its accessible material confirms a convex positive-semidefinite quadratic setting and a nonproximal iteration, but complete theorem-level text was not obtainable through the available lawful access route during this review. This remains a residual historical-originality risk, although those stated hypotheses do not cover the negative-curvature middle block or the proximal recurrence analyzed here.

## References

1. B. Li, Y.-x. Yuan, *Convergent Proximal Multiblock ADMM for Nonconvex Dynamics-Constrained Optimization*, arXiv:2506.17405v1, 2025; Optimization, 2026, DOI: 10.1080/02331934.2026.2725054.
2. X. Chen, C. Cui, D. Han, *Convergence of Three-Block ADMM for Weakly Convex Optimization Problems*, SIAM Journal on Imaging Sciences 18(1), 2025, DOI: 10.1137/24M1684669.
3. S. Cipolla, J. Gondzio, *A linear algebra perspective on the random multi-block ADMM: the QP case*, Calcolo 60, 54, 2023, DOI: 10.1007/s10092-023-00546-0.
4. K. Zhang, H. Song, X. Cai, D. Han, *An extended proximal ADMM algorithm for three-block nonconvex optimization problems*, Journal of Computational and Applied Mathematics 391, 2021, DOI: 10.1016/j.cam.2021.113681.
5. Y. Ke, C. Ma, H. Zhang, *Convergence of ADMM for Three-Block Separable Quadratic Programming Problems with Linear Constraints*, East Asian Journal on Applied Mathematics 8(3), 2018, DOI: 10.4208/eajam.240817.010318.
