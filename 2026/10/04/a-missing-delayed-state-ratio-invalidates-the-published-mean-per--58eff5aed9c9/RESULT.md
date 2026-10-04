# A missing delayed-state ratio invalidates the published mean-persistence estimate
## Finding
For the stochastic delayed SIRS model of Bao and Han, the published proof of its mean-persistence theorem loses a state-dependent delay ratio at the step where three negative terms are combined by AM–GM. The three positive quantities used there multiply to
\[
abA\beta e^{-\lambda\tau}\rho(t),
\qquad
\rho(t)=\frac{S(t-\tau)}{S(t)}\frac{1+\kappa I(t)}{1+\kappa I(t-\tau)},
\]
not to the state-independent quantity \(abA\beta e^{-\lambda\tau}\) appearing in the printed estimate. Because the model allows arbitrary positive continuous initial histories, the proof supplies no lower bound such as \(\rho(t)\ge 1\).

An exact admissible witness makes the failure quantitative. Set
\[
A=100,\qquad \lambda=\phi=\xi=\beta=\kappa=\sigma_1=\sigma_2=\sigma_3=1,
\qquad e^{-\lambda\tau}=\frac12,
\]
and use the current values
\[
S(t)=1000,\qquad I(t)=\frac1{100},\qquad R(t)=\frac1{101},
\]
with delayed values
\[
S(t-\tau)=\frac1{1000},\qquad I(t-\tau)=\frac1{100}.
\]
A positive continuous history joining these endpoint values exists. For the coefficients chosen in the paper's proof,
\[
a=\frac{80}9,\qquad b=\frac{16}3,
\]
and the stated persistence threshold is
\[
\widetilde{\mathcal R}_0^S=\frac{80}{21}>1.
\]
At this history \(\rho(t)=10^{-6}\). Direct substitution into the paper's displayed generator gives
\[
\mathcal L U=\frac{2486393}{90900}>0,
\]
whereas the published post-AM–GM expression gives
\[
-\frac{8761}{900}<0.
\]
Thus the asserted upper bound cannot hold on the theorem's stated class of positive histories, so that Lyapunov estimate does not prove the mean-persistence conclusion.

## Assumptions and scope
The object is the stochastic delayed SIRS system printed as system (3) in Bao and Han. All model parameters are positive. The initial history is a positive continuous function on \([ -\tau,0]\), exactly as in the source. The claim concerns only the displayed proof of the source's mean-persistence theorem and the state-independent drift estimate obtained there.

The witness sets \(\tau=\log 2\), so \(e^{-\lambda\tau}=1/2\). It also chooses \(I(t-\tau)=I(t)\) and \(R(t)=I(t)/(1+\kappa I(t))\). These choices make the surrounding simplifications in the printed estimate no stronger than needed for the counterexample; the decisive discrepancy remains the factor \(S(t-\tau)/S(t)\) inside \(\rho(t)\).

## Proof
The proof defines \(U=-a\log S-b\log I-\log R\). From the displayed stochastic system, its generator contains the negative terms
\[
-\frac{aA}S,
\qquad
-\frac{b\beta e^{-\lambda\tau}S(t-\tau)I(t-\tau)}{I(t)(1+\kappa I(t-\tau))},
\qquad
-\frac{\phi I(t)}{R(t)}.
\]
The printed estimate then reaches an AM–GM bracket with the three positive factors
\[
X=\frac{aA}{S(t)},\qquad
Y=\frac{b\beta e^{-\lambda\tau}S(t-\tau)}{1+\kappa I(t-\tau)},\qquad
Z=1+\kappa I(t).
\]
Their product is exactly
\[
XYZ=abA\beta e^{-\lambda\tau}
\frac{S(t-\tau)}{S(t)}
\frac{1+\kappa I(t)}{1+\kappa I(t-\tau)}
=abA\beta e^{-\lambda\tau}\rho(t).
\]
Therefore AM–GM yields \(-X-Y-Z\le -3(XYZ)^{1/3}\), whose right-hand side depends on \(\rho(t)\). Replacing \(XYZ\) by \(abA\beta e^{-\lambda\tau}\) requires an additional lower bound on \(\rho(t)\) that is not among the theorem's assumptions.

For the exact witness, the source's parameter choices give
\[
\lambda+\frac{\sigma_1^2}2=\frac32,\qquad
\lambda+\phi+\frac{\sigma_2^2}2=\frac52,
\]
\[
a=\frac{A\beta e^{-\lambda\tau}}{(\lambda+\sigma_1^2/2)^2(\lambda+\phi+\sigma_2^2/2)}=\frac{80}9,
\]
and
\[
b=\frac{A\beta e^{-\lambda\tau}}{(\lambda+\sigma_1^2/2)(\lambda+\phi+\sigma_2^2/2)^2}=\frac{16}3.
\]
The threshold evaluates to \(80/21\). The chosen current and delayed infected values coincide, and \(R=I/(1+I)\), so the terms immediately preceding the AM–GM bracket are compatible with the printed reductions. Exact rational substitution into the displayed generator gives \(2486393/90900\). The state-independent post-AM–GM expression used in the proof gives \(-8761/900\). Since an upper bound cannot lie below the quantity it is supposed to bound, the displayed estimate is false.

## Verification
The accompanying verifier performs all arithmetic with exact rational numbers. It checks the source-defined coefficients \(a\) and \(b\), the threshold \(80/21\), the ratio \(\rho=10^{-6}\), the exact generator value \(2486393/90900\), the printed post-AM–GM bound \(-8761/900\), and the strict violation of that bound. No floating-point computation or numerical simulation is needed.

The argument is local in state-history space: it only needs one admissible positive history on which the claimed generator inequality fails. It does not use a finite simulation to infer long-time stochastic behavior.

## Relationship to prior work
Bao and Han's earlier delayed stochastic SIRS paper uses a different persistence argument based on a transformed infected variable and population-balance identities; inspection of that proof does not supply the missing state-ratio inequality for the later model. General delayed-SIRS persistence papers cited by the source establish threshold results for their own systems, but they do not imply the specific state-independent AM–GM estimate used here.

Database and literature searches using the exact title, DOI, theorem topic, delayed-state-ratio aliases, and Lyapunov/AM–GM formulation did not locate a published correction or a result stating this exact counterexample. That negative search is not itself a novelty proof; the originality assessment rests on statement-level comparison with the inspected source and the closely related earlier Bao–Han article.

## Limitations
This finding does not prove that Theorem 4.2's persistence conclusion is false. It proves that the displayed state-independent Lyapunov upper bound, and therefore the proof based on that bound, is invalid on the stated class of positive histories. A different argument could in principle recover the theorem under the same assumptions, or an additional history-ratio condition could make an AM–GM route viable.

No claim is made about the numerical examples, the extinction theorem, or other asymptotic statements in the article.

## References
1. X. Bao and X. Han, “Dynamic behavior and numerical simulation of stochastic epidemic models with time delay,” *Discrete and Continuous Dynamical Systems - S* 18 (2025), 1923–1937, DOI 10.3934/dcdss.2024209. Early access: 2024-11-25.
2. X. Bao and X. Han, “Dynamics analysis of a delayed stochastic SIRS epidemic model with a nonlinear incidence rate,” *Stochastic Models* 41 (2025), 383–412, DOI 10.1080/15326349.2024.2401410. Published online: 2024-10-09.
