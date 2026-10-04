# The ready-to-eat food reservoir shifts the listeriosis invasion threshold
## Finding
For the listeriosis-only subsystem in Koutou, Kouanda and Ouédraogo (2026), the ready-to-eat food variables cannot be dropped from the disease-free state. The model itself imposes the food balance \(F_u+F_c=F\), with \(F>0\) in the biological state space. Therefore the published point
\[
(\Lambda/\mu,0,0,0,0)
\]
is not an equilibrium when \(F>0\): substituting it into the \(F_u\) equation gives \(F_u'=p_fF>0\).

The clean-food disease-free equilibrium is instead
\[
E_0=(\Lambda/\mu,0,0,F,0).
\]
Write
\[
k=\mu+\delta_l+\gamma_l,\qquad q=p_f-\alpha_4F.
\]
When \(q>0\), define
\[
\mathcal R_F=
\frac{\beta_l\xi_l\Lambda}{\mu d_Bk}
\left(1+\frac{\alpha_3F}{q}\right).
\]
Then \(E_0\) is locally asymptotically stable on the biological manifold \(F_u+F_c=F\) when \(\mathcal R_F<1\), and it is unstable when \(\mathcal R_F>1\). At \(\mathcal R_F=1\) the linearization has a zero eigenvalue; no nonlinear classification is claimed.

This differs from the published threshold
\[
\mathcal R_0^L=\frac{\beta_l\xi_l\Lambda}{\mu d_Bk},
\]
which omits the contaminated-food feedback path \(I_l\to B\to F_c\to I_l\).

An exact admissible witness is
\[
\Lambda=\mu=\beta_l=\xi_l=d_B=F=\alpha_4=1,\quad
\delta_l=\gamma_l=1,\quad p_f=2,\quad \alpha_3=3.
\]
For this choice,
\[
\mathcal R_0^L=\frac13<1,\qquad
\mathcal R_F=\frac43>1.
\]
Thus the published threshold predicts stability while the corrected linearization is unstable.

## Assumptions and scope
The claim concerns the listeriosis-only ordinary differential equation in Section 4 of the cited paper. All parameters used in the witness are positive. The total food amount is fixed by the model's biological region \(F_u+F_c=F\). The theorem above assumes \(q=p_f-\alpha_4F>0\), which makes the clean-food contamination mode linearly dissipative before infection feedback is added.

No claim is made here for the critical case \(q=0\), for global dynamics, or for the full listeriosis–meningitis co-infection system. If \(q<0\), the clean-food equilibrium already has a positive food-contamination eigenvalue and is therefore unstable independently of the corrected infection threshold.

## Proof
On \(F_u+F_c=F\), eliminate \(F_u=F-F_c\). At the clean-food state \(E_0=(\Lambda/\mu,0,0,F,0)\), the susceptible perturbation is downstream of the infected/environmental variables. The decisive linear block in \((I_l,B,F_c)\) is
\[
A=
\begin{pmatrix}
-k & a & a\alpha_3\\
\xi_l & -d_B & 0\\
0 & F & -q
\end{pmatrix},
\qquad
a=\frac{\beta_l\Lambda}{\mu}.
\]
Its characteristic polynomial is
\[
P(\lambda)
=(\lambda+k)(\lambda+d_B)(\lambda+q)
-a\xi_l(\lambda+q)-a\alpha_3\xi_lF.
\]
Writing
\[
P(\lambda)=\lambda^3+A_1\lambda^2+A_2\lambda+A_3,
\]
gives
\[
A_1=k+d_B+q,
\]
\[
A_2=kd_B+kq+d_Bq-a\xi_l,
\]
and
\[
A_3=kd_Bq-a\xi_lq-a\alpha_3\xi_lF
=kd_Bq(1-\mathcal R_F).
\]

Suppose \(\mathcal R_F<1\). Then \(A_3>0\), and in particular \(a\xi_l<kd_B\). Hence
\[
A_2=(kd_B-a\xi_l)+q(k+d_B)>0.
\]
Moreover,
\[
A_1A_2-A_3
=(k+d_B)(kd_B-a\xi_l)
+q(k+d_B)(k+d_B+q)
+a\alpha_3\xi_lF>0.
\]
The cubic Routh–Hurwitz conditions therefore hold, so every eigenvalue of \(A\) has negative real part. The remaining susceptible direction has eigenvalue \(-\mu<0\), proving local asymptotic stability on the food-total manifold.

If \(\mathcal R_F>1\), then \(A_3=P(0)<0\), while \(P(\lambda)\to+\infty\) as \(\lambda\to+\infty\). Therefore \(P\) has a positive real root and \(E_0\) is unstable.

For the exact witness above, \(k=3\) and \(q=1\), so
\[
P(\lambda)=\lambda^3+5\lambda^2+6\lambda-1.
\]
Its negative constant term gives the positive real eigenvalue directly.

## Verification
The accompanying `verifier.py` uses only exact rational arithmetic. It checks the food-balance defect at the published point, reconstructs the corrected threshold, expands the characteristic polynomial coefficients, and verifies the exact witness
\[
\mathcal R_0^L=\frac13,\qquad \mathcal R_F=\frac43,\qquad
P(\lambda)=\lambda^3+5\lambda^2+6\lambda-1.
\]
The proof of the general stability criterion is symbolic and does not rely on finite numerical experiments.

## Relationship to prior work
Koutou, Kouanda and Ouédraogo formulate the listeriosis-only model with \(F_u\) and \(F_c\), define \(\lambda_l=\beta_l(B+\alpha_3F_c)\) and \(\lambda_f=B+\alpha_4F_c\), and elsewhere impose \(F_u+F_c=F\). Their Section 4 nevertheless states the disease-free point with both food compartments zero and gives a threshold that contains only the \(I_l\leftrightarrow B\) loop.

Chukwu and Nyabadza (2020) study a different ready-to-eat-food listeriosis model and explicitly introduce a food-contamination threshold. That work supports the general mathematical importance of food contamination as an independent feedback mechanism, but it does not analyze the 2026 system above or imply the factor
\[
1+\frac{\alpha_3F}{p_f-\alpha_4F}.
\]

## Limitations
This result is a correction of the local disease-free equilibrium and its local invasion threshold for the listeriosis-only subsystem. It does not establish a corrected endemic-equilibrium classification, a corrected bifurcation diagram, or global stability. The case \(q=0\) is intentionally excluded because the clean-food contamination direction is then nonhyperbolic. Literature searches found no source-specific published correction, but an unindexed or differently phrased correction remains possible.

## References
1. O. Koutou, C. A. K. Kouanda, A. Ouédraogo, “Mathematical Analysis of a Co-Dynamics Model of Listeriosis and Bacterial Meningitis Starting From Ready-to-Eat Foods,” *International Journal of Analysis and Applications* 24 (2026), 160. DOI: 10.28924/2291-8639-24-2026-160.
2. C. W. Chukwu, F. Nyabadza, “A Theoretical Model of Listeriosis Driven by Cross Contamination of Ready-to-Eat Food Products,” *International Journal of Mathematics and Mathematical Sciences* (2020), Article 9207403. DOI: 10.1155/2020/9207403.
