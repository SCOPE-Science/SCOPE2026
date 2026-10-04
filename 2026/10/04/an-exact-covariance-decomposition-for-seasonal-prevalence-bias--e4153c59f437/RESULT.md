# An exact covariance decomposition for seasonal prevalence bias
## Finding
Consider the seasonal SIRI system
\[
\begin{aligned}
\dot S&=bK-\overline{\beta}(t)IS-bS,\\
\dot I&=\overline{\beta}(t)IS+\overline{\lambda}(t)IR-(\alpha+b)I,\\
\dot R&=\alpha I-\overline{\lambda}(t)IR-bR,
\end{aligned}
\]
with continuous positive \(\omega\)-periodic coefficients and \(S+I+R=K\). Write
\[
\beta=\langle\overline{\beta}\rangle>0,\qquad
\lambda=\langle\overline{\lambda}\rangle,
\]
where \(\langle f\rangle=\omega^{-1}\int_0^\omega f(t)\,dt\), and define
\[
\operatorname{Cov}(f,g)=\langle fg\rangle-\langle f\rangle\langle g\rangle.
\]
If \((S,I,R)\) is any strictly positive \(\omega\)-periodic solution and \((S^*,I^*,R^*)\) is any positive equilibrium of the averaged system, then
\[
\boxed{\langle I\rangle-I^*=\frac{bK}{\beta}\left(\left\langle\frac1S\right\rangle-\frac1{S^*}\right)-\frac1{\beta}\operatorname{Cov}(\overline{\beta},I)}.
\]
Consequently, \(\langle I\rangle=I^*\) holds exactly when
\[
bK\left(\left\langle\frac1S\right\rangle-\frac1{S^*}\right)=\operatorname{Cov}(\overline{\beta},I).
\]
There is also the companion balance
\[
\boxed{\beta(\langle S\rangle-S^*)+\lambda(\langle R\rangle-R^*)+\operatorname{Cov}(\overline{\beta},S)+\operatorname{Cov}(\overline{\lambda},R)=0}.
\]

## Assumptions and scope
The claim uses exactly the seasonal SIRI equations above, positive constants \(b,K,\alpha\), continuous positive periodic rates, a strictly positive periodic orbit, and a positive equilibrium of the coefficient-averaged autonomous system. Strict positivity of \(S\) and \(I\) is used only to divide by these variables and integrate logarithmic derivatives. No small-seasonality assumption, harmonic forcing assumption, or perturbation expansion is used. The result applies separately to each positive averaged equilibrium when backward bifurcation creates more than one.

## Proof
Divide the susceptible equation by \(S(t)>0\):
\[
\frac{d}{dt}\log S=\frac{bK}S-\overline{\beta}(t)I-b.
\]
Averaging over one full period annihilates the logarithmic derivative, so
\[
\langle\overline{\beta}I\rangle=bK\left\langle\frac1S\right\rangle-b.
\]
By the covariance definition,
\[
\langle\overline{\beta}I\rangle=\beta\langle I\rangle+\operatorname{Cov}(\overline{\beta},I).
\]
At a positive equilibrium of the averaged system, its susceptible equation gives
\[
\beta I^*=\frac{bK}{S^*}-b.
\]
Subtracting the last two identities proves the boxed prevalence-bias formula and its equality criterion.

For the companion identity, divide the infected equation by \(I(t)>0\):
\[
\frac{d}{dt}\log I=\overline{\beta}(t)S+\overline{\lambda}(t)R-(\alpha+b).
\]
Period averaging gives
\[
\beta\langle S\rangle+\lambda\langle R\rangle+\operatorname{Cov}(\overline{\beta},S)+\operatorname{Cov}(\overline{\lambda},R)=\alpha+b.
\]
The positive averaged equilibrium satisfies \(\beta S^*+\lambda R^*=\alpha+b\). Subtraction gives the second boxed balance.

## Verification
The derivation is an exact period-integration argument. The accompanying standard-library checker verifies the algebraic subtraction identities using exact rational arithmetic, including a nonzero covariance witness. No finite computation is used as evidence for existence, uniqueness, or stability of periodic solutions.

## Relationship to prior work
Liu, Li, Zhang, and He prove that the periodic and averaged systems have the same basic reproduction number and then compare the averaged endemic equilibrium with the mean of a positive seasonal orbit numerically. Their constrained simulations report very small mean-state deviations in one parameter regime and noticeably larger recovered-class deviation in another, concluding that approximation by the averaged equilibrium is not guaranteed in general. The two identities above address that specific comparison analytically: the infected-prevalence error is exactly a reciprocal-susceptible level term minus a transmission-prevalence covariance term, while the second balance records the corresponding transmission and reinfection covariance constraint.

The general periodic-epidemic threshold theory of Wang and Zhao concerns next-infection operators and threshold dynamics. It does not imply these source-specific mean-prevalence identities, which use the nonlinear susceptible and infected equations on a positive periodic orbit rather than the disease-free linearization.

## Limitations
The identities do not prove that a positive periodic solution exists for parameter regimes not already covered by separate persistence results, do not select among multiple positive averaged equilibria, and do not give a universal sign for \(\langle I\rangle-I^*\). A sign conclusion requires information about \(\langle S^{-1}\rangle\) and \(\operatorname{Cov}(\overline{\beta},I)\). They also do not justify replacing the periodic orbit by an averaged equilibrium outside the stated equality condition.

## References
1. F. Liu, M. Li, F. Zhang, and R. He, “Threshold Dynamics of a SIRI Model with Reinfection: Averaged and Periodic Systems and Application to Tuberculosis Data,” *Mathematics* 14 (2026), 953. DOI: 10.3390/math14060953.
2. W. Wang and X.-Q. Zhao, “Threshold dynamics for compartmental epidemic models in periodic environments,” *Journal of Dynamics and Differential Equations* 20 (2008), 699–717. DOI: 10.1007/s10884-008-9111-8.
