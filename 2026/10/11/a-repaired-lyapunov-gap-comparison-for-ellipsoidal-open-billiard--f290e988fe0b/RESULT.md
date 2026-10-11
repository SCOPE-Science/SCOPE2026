# A repaired Lyapunov-gap comparison for ellipsoidal open billiards

## Finding
In the three-dimensional open-billiard family of Al Dowais and Stoyanov, the obstacles are congruent ellipsoids with semiaxes \(r,r,r/\beta\), their centers lie in one plane, and \(\beta>c_1^{-2}\). The paper proves that the two positive Lyapunov exponents are distinct, but the printed quantitative comparison contains incompatible inequalities. A coefficient comparison using only the paper's stated geometric bounds repairs the qualitative conclusion and yields an explicit valid lower bound.

Set
\[
\delta=d_0-2r_0>0,\qquad L_0=c_1^{-2},\qquad x_0=\frac{2c_1\delta}{r_0},
\]
\[
q=\min\left\{\frac{\beta}{L_0},\frac{1+\beta x_0}{1+L_0x_0}\right\},\qquad
p=\frac{1+\delta q}{1+\delta}.
\]
Because \(\beta>L_0\), both terms defining \(q\) exceed \(1\), so \(q>1\) and \(p>1\). For the two scalar recurrences used in the source proof,
\[
\Delta^{(2)}_m\ge p^{m-1}\widetilde\Delta^{(2)}_m,
\qquad
\Delta^{(4)}_m\ge q p^{m-1}\widetilde\Delta^{(4)}_m
\]
for every integer \(m\ge1\). Hence
\[
\lambda_1(\beta)-\lambda_2\ge\log p>0.
\]
This repairs the proof of the qualitative conclusion \(\lambda_1(\beta)>\lambda_2>0\) under the source's stated assumptions. It does not establish the stronger printed lower bound \(\log(\beta c_1^2)\).

## Assumptions and scope
Use the notation and hypotheses of arXiv:2610.03004v1. The obstacle-center distances satisfy \(d_0<|O_iO_j|\le1\), the radii satisfy \(r_i\le r_0<d_0/3\), and every free-flight length obeys
\[
d_i\ge d_0-2r_0=\delta>0.
\]
The source defines \(L_i=1/\langle\omega_i,\nu_i\rangle^2\) and obtains \(1\le L_i\le L_0=c_1^{-2}\). Its curvature and angle factors satisfy \(\kappa_i\ge1/r_0\) and \(\theta_i\ge2c_1\). The argument below concerns the same Gibbs measure and the same unstable directions used to define the source's exponents \(\lambda_1(\beta)\) and \(\lambda_2\).

The claim is a proof repair. It does not assert that the paper's stronger displayed lower bound is false; it asserts only that the printed argument does not establish that stronger rate and supplies a valid replacement rate sufficient for strict splitting.

## Proof
Write the source coefficients as
\[
a_i=\beta\kappa_i\theta_i,\qquad
\widetilde a_i=\kappa_iL_i\theta_i,
\]
\[
b_i=1+\beta\kappa_i d_i\theta_i,\qquad
\widetilde b_i=1+\kappa_i d_iL_i\theta_i.
\]
Let \(x_i=\kappa_i d_i\theta_i\). From the stated geometric bounds,
\[
x_i\ge\frac{2c_1\delta}{r_0}=x_0.
\]
First,
\[
\frac{a_i}{\widetilde a_i}=\frac{\beta}{L_i}\ge\frac{\beta}{L_0}.
\]
Second,
\[
\frac{b_i}{\widetilde b_i}=\frac{1+\beta x_i}{1+L_ix_i}.
\]
For \(\beta>L_0\ge L_i\), this ratio is increasing in \(x_i\) and decreasing in \(L_i\). Therefore
\[
\frac{b_i}{\widetilde b_i}\ge\frac{1+\beta x_0}{1+L_0x_0}.
\]
Thus, with the \(q\) defined above,
\[
a_i\ge q\widetilde a_i,\qquad b_i\ge q\widetilde b_i
\]
for every collision index.

The matrix products in the source give the recurrences
\[
\Delta^{(2)}_{i+1}=\Delta^{(2)}_i+d_{i+1}\Delta^{(4)}_i,
\qquad
\Delta^{(4)}_{i+1}=a_{i+1}\Delta^{(2)}_i+b_{i+1}\Delta^{(4)}_i,
\]
and the same formulas with tildes. The product initialization gives \(\Delta^{(2)}_1=\widetilde\Delta^{(2)}_1=d_1\) and \(\Delta^{(4)}_1=b_1\ge q\widetilde b_1=q\widetilde\Delta^{(4)}_1\). This is also consistent with the source's later use of \(\Delta^{(2)}_1=d_1\).

Assume for some \(i\ge1\) that
\[
\Delta^{(2)}_i\ge u_i\widetilde\Delta^{(2)}_i,
\qquad
\Delta^{(4)}_i\ge q u_i\widetilde\Delta^{(4)}_i.
\]
Then
\[
\Delta^{(2)}_{i+1}
\ge u_i\left[q\widetilde\Delta^{(2)}_{i+1}-(q-1)\widetilde\Delta^{(2)}_i\right].
\]
The source's positivity comparison gives \(\widetilde\Delta^{(4)}_i\ge\widetilde\Delta^{(2)}_i\), while \(d_{i+1}\ge\delta\). Hence
\[
\widetilde\Delta^{(2)}_{i+1}\ge(1+\delta)\widetilde\Delta^{(2)}_i,
\]
so
\[
\Delta^{(2)}_{i+1}\ge p u_i\widetilde\Delta^{(2)}_{i+1}.
\]
For the fourth component,
\[
\Delta^{(4)}_{i+1}
\ge q u_i\left(\widetilde a_{i+1}\widetilde\Delta^{(2)}_i+q\widetilde b_{i+1}\widetilde\Delta^{(4)}_i\right).
\]
Since
\[
\frac{p-1}{q-p}=\delta
\]
and
\[
\frac{\widetilde b_{i+1}\widetilde\Delta^{(4)}_i}{\widetilde a_{i+1}\widetilde\Delta^{(2)}_i}
\ge\frac{\widetilde b_{i+1}}{\widetilde a_{i+1}}
=d_{i+1}+\frac{1}{\kappa_{i+1}L_{i+1}\theta_{i+1}}
>\delta,
\]
it follows that
\[
\Delta^{(4)}_{i+1}\ge q p u_i\widetilde\Delta^{(4)}_{i+1}.
\]
Starting with \(u_1=1\), induction gives \(u_m=p^{m-1}\). Taking logarithms, dividing by \(m\), and using the source's identification of the two Lyapunov exponents with the growth rates of these products yields
\[
\lambda_1(\beta)-\lambda_2\ge\log p>0.
\]
The source separately proves \(\lambda_2>0\), so the strict ordering follows.

## Verification
The proof uses exact inequalities only. The coefficient ratio \((1+\beta x)/(1+Lx)\) has positive derivative in \(x\) when \(\beta>L\) and negative derivative in \(L\). The induction constant satisfies
\[
p-1=\frac{\delta(q-1)}{1+\delta},\qquad
q-p=\frac{q-1}{1+\delta},
\]
which gives the exact identity \((p-1)/(q-p)=\delta\) used in the fourth-component step.

The printed source proof was checked against its own stated geometry and recurrences. The source assumes only \(d_i\ge d_0-2r_0\), but later invokes \(d_i\ge d_0\). Its induction introduces a rate strictly below an auxiliary rate and then uses the larger rate in the final exponential comparison. Finally, an auxiliary quantity defined as a minimum is later treated as if it were at least one of its defining terms. These are rate-level issues rather than a mere notation change; the repaired bound above avoids all three.

## Relationship to prior work
The motivating 2026 preprint states the stronger quantitative gap and the strict splitting for this ellipsoidal family. The present result does not claim a new billiard model or a stronger theorem. Its contribution is an explicit correction of the coefficient-comparison proof under exactly the published hypotheses, with a replacement rate \(\log p\) that remains strictly positive for every stated \(\beta>c_1^{-2}\).

Earlier work on exteriors of balls proves distinct positive exponents by a different mechanism based on the frequency of suitable symbolic blocks. That spherical-obstacle argument does not supply the ellipsoidal coefficient comparison above and does not resolve the quantitative inconsistencies in the 2026 proof.

## Limitations
The result does not prove or disprove the stronger claimed estimate \(\lambda_1(\beta)-\lambda_2\ge\log(\beta c_1^2)\) by methods other than the printed comparison. It does not change the geometric hypotheses, treat noncongruent ellipsoids, or analyze exponents outside the two unstable directions considered in the source. The originality search cannot exclude equivalent unpublished or unindexed observations.

## References
1. A. Al Dowais and L. Stoyanov, *Some open billiards with distinct top Lyapunov exponents*, arXiv:2610.03004v1, first public 2026-10-02.
2. A. Al Dowais and L. Stoyanov, *Lyapunov Exponents for Open Billiards in the Exterior of Balls*, arXiv:2306.03611v8; SIAM Journal on Applied Dynamical Systems, DOI:10.1137/24M1678969.
