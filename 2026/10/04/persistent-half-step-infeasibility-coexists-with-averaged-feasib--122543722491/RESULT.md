# Persistent half-step infeasibility coexists with averaged feasibility in the OPCGM disk witness
## Finding

Consider
\[
g(z)=\frac12(\|z\|^2-1)\le0,\qquad F(z)=(0,1),
\]
and exact-QP OPCGM--Lipschitz from \(x_0=(1,0)\), with \(\alpha=1\), constant \(0<\eta<1\), and inactive safeguard. Put
\[
u=-F=(0,-1),\qquad h_t=x_{t+1/2}.
\]
Then
\[
g(h_t)>0\quad(t\ge0),\qquad g(x_t)<0\quad(t\ge1).
\]
Moreover,
\[
\|h_{t+1}-u\|^2\le \rho(\eta)\|h_t-u\|^2,
\qquad
\rho(\eta)=1-\frac{\eta^2(4-\eta)(2-\eta)}{4(1+\eta)^2}<1.
\]
Thus
\[
h_t\to(0,-1),\qquad x_t\to(0,-(1-\eta)).
\]
For
\[
\bar h_T=\frac1T\sum_{t=0}^{T-1}h_t
\]
one has
\[
\|\bar h_T-(0,-1)\|=O(T^{-1}),
\qquad
[g(\bar h_T)]_+=O(T^{-1}).
\]

Thus the source paper's canonical curved-constraint witness has perpetual pointwise half-step infeasibility but no positive asymptotic feasibility floor for averaged half-steps.

## Assumptions and scope

The claim concerns exact quadratic-program subproblems and constant \(0<\eta<1\). The velocity-norm cap and Euclidean safeguard are inactive along this trajectory. The interval includes the source theorem's conservative constant-step regime. No claim is made for inexact QP solves, variable steps, other constraints, or a universal averaged-feasibility theorem for all primal-QP methods.

## Proof

Let \(h\) be a half-step, set
\[
s=\|h\|^2,\qquad d=\|h-u\|^2,
\]
and suppose \(s>1\) with negative second coordinate. The active linearized disk constraint is
\[
g(h)+h^{\mathsf T}w\le0.
\]
The exact QP solution is the Euclidean projection of \(u\) onto this half-space:
\[
w=u-\lambda h,\qquad
\lambda=\frac{h^{\mathsf T}u+g(h)}s=1-\frac d{2s}.
\]
Along the trajectory \(0<\lambda<1\). Since \(h=x+\eta u\),
\[
x^+=x+\eta w=ch,\qquad
c=1-\eta+\frac{\eta d}{2s}.
\]

Because \(x=h-\eta u\) and \(\|x\|\le1\),
\[
(1-\eta)s+\eta d\le1+\eta-\eta^2,
\qquad
1<s\le(1+\eta)^2.
\]
Using the upper bound for \(d\) in \(c\),
\[
sc^2-1\le \frac{P_\eta(s)}{4s},
\]
where
\[
P_\eta(s)=(1-\eta)^2s^2+2(\eta^3-2\eta^2-1)s+(\eta^2-\eta-1)^2.
\]
This polynomial is convex in \(s\), and
\[
P_\eta(1)=\eta^2(\eta-2)(\eta+2)<0,
\]
while
\[
P_\eta((1+\eta)^2)=
\eta^2(\eta+2)(\eta^3+2\eta^2-4\eta-4)<0
\]
for \(0<\eta<1\). Hence \(sc^2<1\), so \(x^+\) lies strictly inside the disk.

For the next half-step \(h^+=x^++\eta u\), direct expansion gives
\[
\|h^+\|^2-1=
\frac{\eta^2d(2(s+1)-d)+4(1-\eta)s(s-1)}{4s}.
\]
Since
\[
d\le(\sqrt s+1)^2<2(s+1),
\]
the right side is positive. Thus \(h^+\) is strictly outside.

The base point is
\[
h_0=(1,-\eta),\qquad \|h_0\|^2=1+\eta^2>1.
\]
Induction proves the strict outside/inside alternation for all iterations.

Now write
\[
d_t=\|h_t-u\|^2,\qquad s_t=\|h_t\|^2.
\]
Exact expansion yields
\[
\frac{d_{t+1}}{d_t}=1+\frac{\eta B_t}{4s_t},
\]
where
\[
B_t=(2-\eta)d_t+(2\eta-6)s_t+2\eta-2.
\]
Since
\[
d_t=\|x_t-(1-\eta)u\|^2\le(2-\eta)^2,
\qquad
1<s_t\le(1+\eta)^2,
\]
and \(2\eta-6<0\),
\[
B_t\le(2-\eta)^3+4\eta-8=-\eta(4-\eta)(2-\eta).
\]
Thus
\[
d_{t+1}\le\rho(\eta)d_t.
\]
This proves \(h_t\to u\). Since
\[
c_t=1-\eta+\frac{\eta d_t}{2s_t}\to1-\eta,
\]
also \(x_{t+1}=c_th_t\to(1-\eta)u\).

Finally,
\[
\|h_t-u\|\le\sqrt{d_0}\,\rho(\eta)^{t/2},
\]
so
\[
\|\bar h_T-u\|
\le
\frac{\sqrt{d_0}}{T(1-\sqrt{\rho(\eta)})}.
\]
Because \(g(u)=0\) and \(g\) is smooth near \(u\), this implies \([g(\bar h_T)]_+=O(T^{-1})\).

## Verification

The bundled script `artifacts/verify_opcgm_disk.py` uses exact rational arithmetic to replay representative trajectories. It checks strict half-step infeasibility, strict full-step feasibility, the exact next-half-step identity, and the stated contraction bound. This finite replay is a consistency check only; the proof above establishes the all-iteration statement.

## Relationship to prior work

Yao, Jolaoso, Shehu, and Yao introduce OPCGM--Lipschitz and prove that the first half-step is infeasible on exactly this unit-disk, constant-field witness. Their Remark 4.6 explicitly asks whether the averaged half-step can become asymptotically feasible and reports only numerical evidence that it does. The present calculation resolves that question for the canonical witness: every individual half-step remains infeasible, yet their average approaches the feasible boundary with \(O(T^{-1})\) violation.

The earlier CGM paper of Zhang, He, and Muehlebach develops a single-step primal velocity-projection method for functionally constrained variational inequalities. It does not contain the two-QP OPCGM--Lipschitz correction or this trajectory law.

Targeted database searches for the algorithm, witness, averaged half-step, and boundary convergence returned no statement implying this result.

## Limitations

This is a complete analysis of one canonical witness, not a universal averaged-feasibility theorem. It does not rule out a positive averaged-feasibility lower bound on another constrained variational inequality, and it does not settle the broader open problem for all primal-QP methods. The proof assumes exact QP solves and constant \(\eta\).

## References

1. Y. Yao, L. O. Jolaoso, Y. Shehu, J.-C. Yao, *Primal Methods for Constrained Variational Inequalities: Optimal Rates, Feasibility Trade-offs, and Lower Bounds*, arXiv:2609.32981v1, 2026.
2. L. Zhang, N. He, M. Muehlebach, *Primal methods for variational inequality problems with functional constraints*, Mathematical Programming, 2025, DOI: 10.1007/s10107-025-02206-3.
