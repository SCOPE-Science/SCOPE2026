# The correlated-noise sensitivity formula double-counts Brownian variance
## Finding
For the correlated-noise extension of the stochastic SIRS sensitivity calculation in Huang, Du, and Liang (2026), let \(R=(\rho_{ij})\) be the correlation matrix of the Brownian vector, so \(d\langle B_i,B_j\rangle_t=\rho_{ij}\,dt\) and necessarily \(\rho_{ii}=1\). At the stable endemic equilibrium \(E^*=(S^*,I^*,R^*)\), the diffusion matrix in the small-noise linearization is
\[
G=-\operatorname{diag}(\sigma_1S^*,\sigma_2I^*,\sigma_3R^*).
\]
The stationary covariance \(W\) of the linearized fluctuation must satisfy
\[
FW+WF^\top+GRG^\top=0.
\]
Remark 3.8 instead prints
\[
FW+WF^\top+GG^\top+Q=0,
\qquad
Q_{ij}=\rho_{ij}\sigma_i\sigma_jE_i^*E_j^*.
\]
With the displayed definition of \(Q\), one has exactly \(Q=GRG^\top\). Hence the printed equation adds \(GG^\top\) once too often. The corrected equation is
\[
FW+WF^\top+Q=0.
\]
Equivalently, one may retain the term \(GG^\top\) only if the added correlation correction has zero diagonal:
\[
FW+WF^\top+GG^\top+Q_{\mathrm{off}}=0,
\quad
(Q_{\mathrm{off}})_{ii}=0,
\quad
(Q_{\mathrm{off}})_{ij}=\rho_{ij}\sigma_i\sigma_jE_i^*E_j^*\ (i\ne j).
\]

A sharp consistency check is the independent limit \(R=I\). Then \(Q=GG^\top\), so the printed Remark 3.8 equation becomes \(FW+WF^\top+2GG^\top=0\). Since \(F\) is Hurwitz in the sensitivity calculation, the continuous Lyapunov equation has a unique solution. If \(W_{\mathrm{ind}}\) solves Eq. (3.16), then the printed correlated formula therefore gives
\[
W_{\mathrm{printed}}=2W_{\mathrm{ind}}.
\]
Because the paper's confidence-ellipsoid half-axis lengths are proportional to \(\varepsilon\sqrt{\mu_i}\), where \(\mu_i\) are eigenvalues of \(W\), the independent-limit half-axis lengths obtained from Remark 3.8 are spuriously larger by exactly \(\sqrt{2}\).

## Assumptions and scope
The claim assumes the standard definition of a correlated Brownian vector: \(R\) is symmetric positive semidefinite and has unit diagonal. It uses the paper's own stable-endemic-equilibrium setting for stochastic sensitivity, so the drift Jacobian \(F\) is Hurwitz and the stationary Lyapunov equation has a unique solution. The source model has multiplicative mortality noise, and after scaling by the common small-noise amplitude its equilibrium diffusion matrix is diagonal as displayed above.

The result corrects only the covariance equation in Remark 3.8 and its implied confidence-domain geometry for correlated noise. It does not challenge the independent-noise covariance equation (3.16), the stochastic threshold, positivity, extinction, or stationary-distribution results. If the authors intended \(\rho_{ij}\) in the additive correction to denote only off-diagonal correlations, then \(Q_{ii}=0\) must be imposed; that is not the matrix \(Q\) printed in Remark 3.8, where \(dB_i(t)dB_j(t)=\rho_{ij}dt\) and \(i,j=1,2,3\).

## Proof
Write the linearized small-noise fluctuation as
\[
dz=Fz\,dt+G\,dB,
\]
with quadratic covariation \(d\langle B\rangle_t=R\,dt\). Applying Itô's product rule to \(zz^\top\) gives
\[
d(zz^\top)=Fzz^\top\,dt+zz^\top F^\top\,dt+G\,dB\,z^\top+z\,dB^\top G^\top+G\,dB\,dB^\top G^\top.
\]
Taking expectations annihilates the martingale terms and uses \(dB\,dB^\top=R\,dt\), yielding
\[
\frac{d}{dt}M(t)=FM(t)+M(t)F^\top+GRG^\top,
\quad M(t)=\mathbb E[z(t)z(t)^\top].
\]
At stationarity this is the claimed Lyapunov equation.

For the source diffusion matrix, define \(h=(\sigma_1S^*,\sigma_2I^*,\sigma_3R^*)\). Since \(G=-\operatorname{diag}(h)\),
\[
(GRG^\top)_{ij}=h_i\rho_{ij}h_j
=\rho_{ij}\sigma_i\sigma_jE_i^*E_j^*=Q_{ij}.
\]
Thus the source's \(Q\) is already the complete diffusion covariance, not merely a cross-correlation correction.

Finally take \(R=I\). The corrected equation becomes exactly Eq. (3.16), while the printed Remark 3.8 equation contains \(2GG^\top\). By linearity and uniqueness of the Lyapunov solution for Hurwitz \(F\), doubling the forcing doubles \(W\). Eigenvalues therefore double and the ellipsoid half-axis lengths increase by \(\sqrt{2}\).

## Verification
The accompanying `verifier.py` uses exact rational arithmetic only. It checks a three-dimensional Hurwitz example with diagonal \(F=-I\), a nontrivial positive-definite rational correlation matrix, and diagonal \(G\). It verifies that the corrected covariance solves \(FW+WF^\top+GRG^\top=0\), that the source-style forcing is larger by exactly \(GG^\top\), and that at \(R=I\) the source-style covariance is exactly twice the independent covariance. Running the file prints `VERIFY_OK`.

The proof above is symbolic and does not depend on the illustrative verifier example. The decisive source consistency check is also exact: Eq. (3.16) and Remark 3.8 coincide only if the added matrix has zero diagonal, whereas the printed definition gives \(Q_{ii}=\sigma_i^2(E_i^*)^2\).

## Relationship to prior work
Huang, Du, and Liang derive the independent-noise sensitivity equation \(FW+WF^\top+GG^\top=0\) in Eq. (3.16), then state the correlated-noise extension in Remark 3.8 as \(FW+WF^\top+GG^\top+Q=0\) with \(Q_{ij}=\rho_{ij}\sigma_i\sigma_jE_i^*E_j^*\). Their model equations also show that the equilibrium diffusion amplitudes are \(\sigma_1S^*\), \(\sigma_2I^*\), and \(\sigma_3R^*\). These statements together force the correction above.

The paper cites Bashkirtseva, Ryashko, and Ryazanova (2017) for stochastic-sensitivity confidence domains. That work supplies background for the method, but the accessible bibliographic record and abstract do not state the source-specific correlated-noise formula corrected here. Exact-title, DOI, covariance, and Remark-3.8 searches located the 2026 article and its mirrors but no published correction or result already stating this independent-limit inconsistency.

## Limitations
This is a local small-noise covariance correction at a stable endemic equilibrium. It does not establish how large-noise stationary distributions behave under correlated forcing, nor does it reanalyze the paper's extinction or ergodicity thresholds. Singular correlation matrices are allowed by the covariance identity, but the paper's separate nondegeneracy assumptions may exclude some such cases from other theorems. The literature search cannot rule out an unindexed or unpublished correction. The 2017 stochastic-sensitivity article was not lawfully available in full text during this review; its abstract was inspected, and the present correction does not rely on any unverified claim from it.

## References
1. J. Huang, J. Du, H. Liang, “Dynamics and stochastic sensitivity technique of a stochastic SIRS epidemic model,” *AIMS Mathematics* 11(3) (2026), 6720–6743. DOI: 10.3934/math.2026278.
2. I. Bashkirtseva, L. Ryashko, T. Ryazanova, “Stochastic sensitivity technique in a persistence analysis of randomly forced population systems with multiple trophic levels,” *Mathematical Biosciences* 293 (2017), 38–45. DOI: 10.1016/j.mbs.2017.08.007.
