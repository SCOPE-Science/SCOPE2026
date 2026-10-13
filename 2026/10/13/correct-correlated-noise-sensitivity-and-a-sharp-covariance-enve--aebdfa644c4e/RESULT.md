# Correct correlated-noise sensitivity and a sharp covariance envelope in a stochastic SIRS model
## Finding
The source linearizes its stochastic SIRS model near the deterministic endemic equilibrium and uses a stochastic-sensitivity covariance to construct confidence ellipsoids. If the three Brownian motions have correlation matrix
\[
R=(\rho_{ij}),\qquad R\succeq0,\qquad R_{ii}=1,
\]
then the correct stationary covariance equation for the weak-noise linearization
\[
dZ=FZ\,dt+G\,dB
\]
is
\[
FW+WF^\top+GRG^\top=0.
\]

The source's Remark 3.8 instead prints
\[
FW+WF^\top+GG^\top+Q=0,
\qquad
Q_{ij}=\rho_{ij}\sigma_i\sigma_jE_i^*E_j^*,
\quad i,j=1,2,3.
\]
For this model \(G\) is diagonal with entries \(-\sigma_iE_i^*\), so
\[
Q=GRG^\top.
\]
Because every Brownian correlation matrix satisfies \(\rho_{ii}=1\), the printed expression therefore counts each diagonal noise variance once in \(GG^\top\) and again in \(Q\). A repaired version may either use \(GRG^\top\) alone or retain \(GG^\top+Q\) after redefining \(Q\) to contain only off-diagonal covariance entries.

At the paper's baseline parameter vector,
\[
\Lambda=1,\quad \mu=0.2,\quad \beta=0.1,\quad
\epsilon_d=0.05,\quad \gamma=0.1,\quad \delta=0.25,
\]
\[
\alpha=0.001,\quad
\sigma_1=0.6,\quad \sigma_2=0.8,\quad \sigma_3=0.7,
\]
the endemic equilibrium is
\[
(S^*,I^*,R^*)\approx
(3.50361582597,\ 1.01641189180,\ 0.225869309288).
\]
For the correct correlated covariance, the total first-order variance obeys
\[
\operatorname{tr}W(R)\approx
17.2747505624
+5.39530312013\,\rho_{12}
+0.537604148434\,\rho_{13}
+0.152951296895\,\rho_{23}.
\]
This affine functional has the sharp correlation-matrix range
\[
11.4947945907\le \operatorname{tr}W(R)\le23.3606091279.
\]
The maximum occurs at perfect positive correlation, while the minimum occurs when the second and third noises are perfectly anticorrelated with the first and perfectly correlated with one another.

Thus the source's qualitative statement that correlation changes the confidence ellipsoid can be sharpened substantially: at the printed baseline, correlation alone changes the total weak-noise variance by a factor of about \(2.0323\). Moreover, if the printed Eq. (3.19) is applied literally at perfect positive correlation, it gives trace \(40.6353596903\) instead of the correct \(23.3606091279\).

## Assumptions and scope
The statement concerns the first-order stochastic-sensitivity approximation used in the source. The deterministic endemic equilibrium is assumed stable, as required by the Lyapunov covariance construction. The correlation matrix \(R\) is a genuine Brownian correlation matrix: it is symmetric positive semidefinite with unit diagonal.

The disease-mortality parameter is denoted \(\epsilon_d\) here to distinguish it from the source's separate small overall noise parameter. The source's independent-noise covariance in Eq. (4.4) is unaffected, because for \(R=I_3\) the correct equation reduces exactly to
\[
FW+WF^\top+GG^\top=0.
\]

The conclusion does not assert that the Gaussian approximation is accurate for large noise or near extinction. It also does not determine the exact covariance of the full nonlinear stationary distribution.

## Proof
For the linear Itô system
\[
dZ=FZ\,dt+G\,dB,\qquad dB\,dB^\top=R\,dt,
\]
Itô's product rule gives
\[
\frac{d}{dt}\mathbb E[ZZ^\top]
=
F\mathbb E[ZZ^\top]
+\mathbb E[ZZ^\top]F^\top
+GRG^\top.
\]
At a stable equilibrium, \(F\) is Hurwitz and the stationary covariance is therefore the unique solution of
\[
FW+WF^\top+GRG^\top=0.
\]

For the SIRS model, the noise coefficient at the equilibrium is
\[
G=\operatorname{diag}
(-\sigma_1S^*,-\sigma_2I^*,-\sigma_3R^*).
\]
Hence
\[
(GRG^\top)_{ij}
=
\rho_{ij}\sigma_i\sigma_jE_i^*E_j^*,
\]
because both diagonal factors of \(G\) carry the same minus sign. This is exactly the matrix denoted \(Q\) in Remark 3.8. The additional \(GG^\top\) in the printed correlated formula is therefore an extra independent-noise contribution. In particular, if \(R=I_3\), the printed formula would give \(2GG^\top\) even though the correlated model has then reduced to the independent one.

For the baseline numerical parameters and
\[
f(I)=1+\alpha I^2,
\]
the endemic equilibrium equations give
\[
S^*=\frac{(\mu+\gamma+\epsilon_d)(1+\alpha(I^*)^2)}{\beta},
\qquad
R^*=\frac{\gamma}{\mu+\delta}I^*.
\]
Using the total-population balance yields the positive root
\[
I^*\approx1.01641189180,
\]
and hence the equilibrium stated above.

The Jacobian reconstructed from the deterministic drift is
\[
F\approx
\begin{pmatrix}
-0.301536293&-0.349277581&0.25\\
0.101536293&-0.000722419&0\\
0&0.1&-0.45
\end{pmatrix}.
\]
Its eigenvalues have real parts approximately
\[
-0.166016513,\quad -0.166016513,\quad -0.420225686,
\]
so the Lyapunov equations below have unique symmetric solutions.

Let \(P\) solve the adjoint Lyapunov equation
\[
F^\top P+PF+I_3=0.
\]
Multiplying the covariance equation by \(P\), taking traces, and using cyclicity gives
\[
\operatorname{tr}W
=
\operatorname{tr}(PGRG^\top)
=
\operatorname{tr}(G^\top PGR).
\]
At the baseline,
\[
H:=G^\top PG\approx
\begin{pmatrix}
9.676088414&2.697651560&0.268802074\\
2.697651560&7.559654500&0.076475648\\
0.268802074&0.076475648&0.039007648
\end{pmatrix}.
\]
Therefore
\[
\operatorname{tr}W(R)
=
\operatorname{tr}(HR),
\]
which expands to the displayed affine law.

It remains to optimize this law over all \(3\times3\) correlation matrices. Every such matrix is a Gram matrix of unit vectors \(u_1,u_2,u_3\). Write
\[
x=u_1\!\cdot u_2,\qquad
y=u_1\!\cdot u_3,\qquad
z=u_2\!\cdot u_3,
\]
and abbreviate the three positive off-diagonal coefficients by
\[
a\approx5.39530312013,\qquad
b\approx0.537604148434,\qquad
c\approx0.152951296895.
\]
The maximum is immediate: \(x,y,z\le1\), and equality is simultaneously attainable by \(u_1=u_2=u_3\).

For the minimum, fix \(u_1,u_2\) with \(u_1\cdot u_2=x\). The optimal unit vector \(u_3\) points opposite to \(b u_1+c u_2\), giving the reduced objective
\[
a x-\sqrt{b^2+c^2+2bcx},
\qquad -1\le x\le1.
\]
Its derivative is
\[
a-\frac{bc}{\sqrt{b^2+c^2+2bcx}}.
\]
Since
\[
a>\frac{bc}{b-c},
\]
this derivative is strictly positive throughout the interval. Hence the minimum occurs at \(x=-1\). Then \(u_2=-u_1\), and the minimizing choice is \(u_3=-u_1\), giving
\[
(\rho_{12},\rho_{13},\rho_{23})=(-1,-1,1).
\]
Substitution yields the two sharp endpoint traces stated above.

Finally, Lyapunov solutions depend linearly on their forcing covariance. Thus, at perfect positive correlation,
\[
W_{\mathrm{printed}}
=
W(R_+)+W(I_3),
\]
which gives the stated trace inflation.

## Verification
The bundled script `verification/verify.py` reconstructs the endemic equilibrium from the printed parameters, forms the analytic Jacobian and diagonal noise matrix, solves the \(3\times3\) Lyapunov equations by a standard-library Gaussian-elimination routine, and reproduces the source's independent-noise covariance to the printed precision.

It then computes the adjoint matrix \(P\), the affine trace coefficients, both sharp correlation extrema, and the literal printed correlated covariance under perfect positive correlation. It checks
\[
W_{\mathrm{printed}}=W(R_+)+W(I_3)
\]
numerically and prints `VERIFY_OK` on success.

The optimization over the correlation elliptope is proved analytically above; no random search over correlation matrices is used as a substitute for the proof.

## Relationship to prior work
The motivating paper derives the independent-noise Lyapunov equation and uses its stochastic-sensitivity matrix to construct a confidence ellipsoid. Remark 3.8 proposes a correlated-noise extension and explicitly states \(Q_{ij}=\rho_{ij}\sigma_i\sigma_jE_i^*E_j^*\) for \(i,j=1,2,3\), but it does not analyze the correlation elliptope or quantify the range of confidence-ellipsoid variance.

Cai, Cai, and Mao (2019) study an SIS model with two correlated Brownian motions and explicitly represent the correlated noises through linear combinations of independent Brownian motions. Their model concerns extinction and persistence in a one-dimensional infected-population equation; it does not contain the 2026 SIRS stochastic-sensitivity matrix or the sharp trace envelope derived here.

Yuan, Wu, Lan, and Wang (2020) present the standard stochastic-sensitivity covariance equation
\[
FW+WF^\top=-GG^\top
\]
for independent driving noise and use it to construct confidence domains in a producer-grazer model. That framework supports the covariance interpretation used here, but it does not state the source-specific correlated-noise correction or optimize the 2026 SIRS covariance over all admissible correlations.

The present result is therefore limited to two source-specific additions: correcting the covariance forcing in the correlated extension and giving the sharp baseline variance range over the full correlation elliptope.

## Limitations
The trace is only one scalar measure of covariance size. Correlation also changes the principal axes and determinant of the covariance matrix; those quantities are not optimized here.

The endpoint correlation matrices are singular and correspond to perfectly correlated or anticorrelated Brownian components. They are valid correlation matrices, and nonsingular correlation matrices can approximate them arbitrarily closely.

The calculation is a weak-noise local Gaussian approximation. It does not replace nonlinear stationary-distribution analysis for finite noise and does not modify the source's independent-noise stochastic threshold or extinction/persistence theorems.

## References
1. J. Huang, J. Du, H. Liang, “Dynamics and stochastic sensitivity technique of a stochastic SIRS epidemic model,” AIMS Mathematics 11 (2026), 6720–6743. DOI: 10.3934/math.2026278.
2. S. Cai, Y. Cai, X. Mao, “A stochastic differential equation SIS epidemic model with two correlated Brownian motions,” Nonlinear Dynamics 97 (2019), 2175–2187. DOI: 10.1007/s11071-019-05114-2.
3. S. Yuan, D. Wu, G. Lan, H. Wang, “Noise-Induced Transitions in a Nonsmooth Producer–Grazer Model with Stoichiometric Constraints,” Bulletin of Mathematical Biology 82 (2020), 55. DOI: 10.1007/s11538-020-00733-y.
