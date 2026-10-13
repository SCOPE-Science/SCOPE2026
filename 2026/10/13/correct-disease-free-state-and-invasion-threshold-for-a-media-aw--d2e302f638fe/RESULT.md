# Correct disease-free state and invasion threshold for a media-aware SQEIAR model

## Finding

The dimensional SQEIAR model has susceptible and quarantined-susceptible equations
\[
S'=-\beta e^{-(m_1I+m_2A)/N}\frac{S(I+\theta A)}N-pS+\lambda Q+\Lambda-\mu S,
\]
\[
Q'=pS-(\lambda+\mu)Q.
\]
At disease absence, solving these equations gives
\[
N_*=\frac{\Lambda}{\mu},
\qquad
S_*=\frac{\Lambda(\lambda+\mu)}{\mu(p+\lambda+\mu)},
\qquad
Q_*=\frac{p}{\lambda+\mu}S_*.
\]
Thus \(Q_*>0\) whenever \(p>0\).

In the source's scaled variables,
\[
\widetilde S_*=\frac{\widetilde\lambda+1}{\widetilde p+\widetilde\lambda+1},
\qquad
\widetilde Q_*=\frac{\widetilde p}{\widetilde p+\widetilde\lambda+1},
\qquad
\widetilde N_*=1.
\]
The point printed in Section 3,
\[
(\widetilde Q,\widetilde E,\widetilde I,\widetilde A,\widetilde R,\widetilde N)
=(0,0,0,0,0,1),
\]
is not an equilibrium when \(p>0\), since the printed scaled equation gives
\[
\widetilde Q'=\widetilde p
\]
there.

The infected states are \(E,I,A\). With
\[
s_*=\frac{S_*}{N_*}=\frac{\lambda+\mu}{p+\lambda+\mu},
\]
the correct next-generation decomposition at the true disease-free equilibrium is
\[
F=\begin{pmatrix}
0&\beta s_*&\beta\theta s_*\\
0&0&0\\
0&0&0
\end{pmatrix},
\]
\[
V=\begin{pmatrix}
\sigma+\mu&0&0\\
-\sigma\rho&\gamma_I+\mu_I+\mu&0\\
-\sigma(1-\rho)&0&\gamma_A+\mu
\end{pmatrix}.
\]
Therefore
\[
\mathcal R_0=
\frac{\beta(\lambda+\mu)\sigma}{(p+\lambda+\mu)(\sigma+\mu)}
\left(
\frac{\rho}{\gamma_I+\mu_I+\mu}
+
\frac{\theta(1-\rho)}{\gamma_A+\mu}
\right).
\]

The source instead includes \(Q\), a susceptible quarantine class, in a four-state next-generation construction. Its displayed linearized matrix called \(F\) has first row
\[
(-\widetilde p,-\widetilde p,-\widetilde p,-\widetilde p),
\]
so it is not nonnegative and does not satisfy the new-infection construction cited by the paper.

At the source's Table 2 parameters,
\[
\mathcal R_0=0.2281211174\ldots
\]
for \(\beta=0.09\), and
\[
\mathcal R_0=1.6475414038\ldots
\]
for \(\beta=0.65\). The corresponding transmission threshold is
\[
\beta_c=0.3945272626\ldots.
\]

## Assumptions and scope

The claim concerns the deterministic equations printed as model (2.1), with positive demographic and transition rates and \(0\le\rho\le1\). The media coefficients do not enter \(\mathcal R_0\) because the media attenuation factor equals one at the disease-free equilibrium.

No claim is made that every downstream theorem or every numerical trajectory is false. In particular, the two showcased values of \(\beta\) remain on the same qualitative sides of one after correction.

## Proof

With \(E=I=A=R=0\), the two disease-free balance equations are
\[
0=pS-(\lambda+\mu)Q,
\]
and
\[
0=\Lambda-(p+\mu)S+\lambda Q.
\]
Their sum gives
\[
S+Q=\frac{\Lambda}{\mu}.
\]
Solving yields the stated \(S_*,Q_*\). This alone proves that the source's zero-quarantine scaled point is not a disease-free equilibrium when \(p>0\).

Linearizing the infected equations at the true disease-free state gives \(J_I=F-V\) with the displayed matrices. Since \(F\) has one nonzero row, \(FV^{-1}\) has rank one and its trace is its unique nonzero eigenvalue. Direct multiplication yields the stated \(\mathcal R_0\).

A direct determinant expansion gives
\[
\det(-J_I)=
(\sigma+\mu)(\gamma_I+\mu_I+\mu)(\gamma_A+\mu)(1-\mathcal R_0).
\]
Thus \(\mathcal R_0=1\) is exactly the infected linearization's invasion boundary.

The cited next-generation framework defines \(F_i\) as rates of appearance of new infections in infected compartments and proves that the derivative matrix \(F\) is nonnegative. A transfer of susceptible people into quarantine is not a new infection, and a matrix with negative entries cannot be the required \(F\).

## Verification

The bundled checker uses exact rational arithmetic for the values printed in Table 2. It verifies the disease-free susceptible-quarantine balance, the determinant factorization, the two corrected reproduction numbers, and the value of \(\beta_c\).

No finite computation is used to prove the threshold formula; the arithmetic replay only checks the stated constants.

## Relationship to prior work

The primary source is Shi, Gao, Zhou, and Li. It explicitly labels the zero-quarantine scaled point as disease-free, displays the four-state next-generation construction, and reports the values \(0.3438\) and \(2.4833\).

Van den Driessche and Watmough provide the next-generation framework cited by that paper. Their construction separates infected from uninfected compartments, defines new-infection rates epidemiologically, requires the resulting \(F\) matrix to be nonnegative, and defines the threshold by \(\rho(FV^{-1})\).

Targeted searches by title, DOI, reproduction-number language, quarantine-compartment aliases, negative-\(F\) terminology, and corrected threshold values did not locate a published correction of the source.

A separate earlier result concerning the same article corrects its optimal-control adjoints. That result concerns Hamiltonian differentiation in the controlled system and does not state or imply the disease-free-state and invasion-threshold correction here.

## Limitations

The finding corrects the threshold of the printed model, not unpublished implementation code. It does not re-run the complete numerical study.

Because the corrected values at \(\beta=0.09\) and \(\beta=0.65\) remain below and above one, respectively, the finding does not reverse those two displayed stability classifications.

Downstream quantitative threshold and sensitivity claims require re-evaluation with the corrected \(\mathcal R_0\), but no blanket conclusion about every downstream result is made.

## References

1. X. Shi, X. Gao, X. Zhou, Y. Li, “Analysis of an SQEIAR epidemic model with media coverage and asymptomatic infection,” AIMS Mathematics 6 (2021), 12298–12320. DOI: 10.3934/math.2021712.
2. P. van den Driessche, J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” Mathematical Biosciences 180 (2002), 29–48. DOI: 10.1016/S0025-5564(02)00108-6.
