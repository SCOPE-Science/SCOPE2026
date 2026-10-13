# The predator-extinction Floquet multiplier collapses to pure mortality in a weighted-harvesting Allee model
## Finding
For the impulsive predator-prey model
\[
\dot x=rx\left(1-\frac{x}{K}\right)-\frac{axy}{1+aqx},
\qquad
\dot y=e\psi(y)\frac{axy}{1+aqx}-\mu y,
\]
with weighted harvesting
\[
\Delta x=-p_1E_lx,\qquad
\Delta y=-p_2E_ly+\tau_l
\]
at \(\eta x+(1-\eta)y=h_l\), the source assumes \(\psi(0)=0\).

Set \(\tau_l=0\), and assume
\[
0<h_l<\eta K,\qquad 0<p_1E_l<1,\qquad
0\le p_2E_l<1,\qquad \mu>0.
\]
On \(y=0\), the prey follows the logistic equation and forms a finite harvesting cycle with
\[
x(0^+)=\frac{(1-p_1E_l)h_l}{\eta},\qquad
x(T^-)=\frac{h_l}{\eta}.
\]
Its period is
\[
T=\frac1r\log\!\left(
\frac{\eta K-(1-p_1E_l)h_l}
{(1-p_1E_l)(\eta K-h_l)}
\right)>0.
\]

The exact convergence ratio is
\[
\rho=(1-p_2E_l)e^{-\mu T}.
\]
Therefore \(0<\rho<1\) for every biologically admissible \(p_2\), so the predator-extinction periodic orbit is orbitally asymptotically stable throughout its finite-cycle existence region. The threshold
\[
\bar p_2=\frac{p_1h_l}{\eta K-(1-p_1E_l)h_l}
\]
printed in Theorem 2.1 is not a stability threshold.

For the source's Example 3.1 prey parameters,
\[
r=2,\quad K=100,\quad \eta=0.6,\quad h_l=30,\quad
p_1=0.3,\quad E_l=2,\quad \mu=1,
\]
one has \(T=\log 2\) and \(\bar p_2=0.1875\). Keeping those parameters but taking \(p_2=0.1<\bar p_2\) gives
\[
\rho=(1-0.1\cdot2)e^{-\log2}=0.4<1.
\]
This directly contradicts the source's subthreshold-instability assertion.

## Assumptions and scope
The result uses the source's Allee condition \(\psi(0)=0\). Near \(y=0\), the predator recruitment term is higher than linear order, so rare predators decay continuously at rate \(\mu\) and are multiplied by \(1-p_2E_l\) at each harvest.

The strict condition \(h_l<\eta K\) is required for a finite hitting time. At \(h_l=\eta K\), after any nontrivial prey harvest the logistic solution starts below \(K\) and approaches \(K\) only as \(t\to\infty\); the finite periodic impulse cycle therefore degenerates.

The result does not assert nonexistence of positive order-1 cycles. A positive cycle shown numerically by the source may coexist with the stable boundary cycle.

## Proof
Put
\[
\kappa=1-p_1E_l\in(0,1).
\]
The source's travel-time formula is
\[
T=\frac1r\log\!\left(
\frac{\eta K-\kappa h_l}{\kappa(\eta K-h_l)}
\right).
\]
Hence
\[
\frac{\eta K-\kappa h_l}{\eta K-h_l}
=\kappa e^{rT}.
\]

The source's displayed convergence ratio is
\[
\rho=(1-p_2E_l)
\frac{\eta K-\kappa h_l}{\eta K-h_l}
\exp\!\left[
\int_0^T\left(-\frac{rx(t)}K-\mu\right)dt
\right].
\]
Along the predator-free logistic flight,
\[
\frac{d}{dt}\log x=r-\frac{rx}{K}.
\]
Therefore
\[
\int_0^T\left(-\frac{rx(t)}K-\mu\right)dt
=\log\frac{x(T^-)}{x(0^+)}-(r+\mu)T
=-\log\kappa-(r+\mu)T.
\]
The exponential factor is thus
\[
\kappa^{-1}e^{-(r+\mu)T}.
\]
Substitution gives
\[
\rho=(1-p_2E_l)e^{-\mu T}.
\]
Since \(T>0\), \(\mu>0\), and \(0\le p_2E_l<1\), one has \(0<\rho<1\).

There is an independent transverse derivation. Because \(\psi(0)=0\), linearizing the predator equation on \(y=0\) gives
\[
\delta\dot y=-\mu\,\delta y.
\]
At a harvest,
\[
\delta y^+=(1-p_2E_l)\delta y^-.
\]
One cycle therefore has the same multiplier \((1-p_2E_l)e^{-\mu T}\).

The source correctly notes that the inequality producing \(p_2>\bar p_2\) is only sufficient after discarding the exponential attenuation, but immediately then asserts the converse \(p_2<\bar p_2\Rightarrow\rho>1\). The exact cancellation shows that this converse never occurs in the finite-cycle regime.

## Verification
The bundled `verification/verify.py` evaluates the source's period and unsimplified convergence ratio independently, compares it with \((1-p_2E_l)e^{-\mu T}\), and checks the identity on several admissible parameter sets.

For Example 3.1 it verifies
\[
T=\log2,\qquad \bar p_2=0.1875,\qquad
\rho(0.1)=0.4,\qquad \rho(0.2)=0.3.
\]
The proof is analytic; these computations are supplementary.

## Relationship to prior work
Xu and Zou (2026) derive the same predator-free cycle, travel time, and unsimplified convergence ratio. They label \(p_2>\bar p_2\) sufficient but not necessary, then assert instability below the same threshold. The exact logistic integral resolves that internal contradiction and removes the threshold.

Zhu, Wang, and Ouyang (2021) develop a general state-dependent impulsive predator-prey framework using successor functions and an analogue of the Poincaré criterion. Their general theory supplies stability machinery but does not specialize the Xu-Zou weighted threshold or derive the pure-mortality multiplier.

Yu and Huang (2023) study another weighted-harvesting predator-prey model and obtain a genuine predator-harvesting stability threshold for its predator-extinction cycle. Its boundary predator equation has a nonzero linear growth contribution, unlike the Xu-Zou Allee model where \(\psi(0)=0\). Thus that earlier threshold theorem does not imply this result.

## Limitations
The result concerns only the semi-trivial periodic orbit with \(\tau_l=0\) and \(0<h_l<\eta K\). It does not classify positive cycles or their basins.

Theorem 2.2(1) begins by using the claimed instability of the semi-trivial cycle to obtain a successor-function sign. Since that premise is false, the published proof of case (1) is not established by the stated argument. This does not prove that the positive cycle is absent.

At \(h_l=\eta K\), the hitting time diverges; no finite-period Floquet statement is made at that boundary.

## References
1. J. Xu, T. Zou, “Dynamics of a predator-prey model with the Allee effect for the predator induced by weighted harvesting strategy,” AIMS Mathematics 11 (2026), 578–593. DOI: 10.3934/math.2026025.
2. X. Zhu, H. Wang, Z. Ouyang, “The state-dependent impulsive control for a general predator-prey model,” Journal of Biological Dynamics 16 (2022), 354–372; first published online 5 June 2021. DOI: 10.1080/17513758.2021.1937721.
3. X. Yu, M. Huang, “Dynamics of a Gilpin-Ayala predator-prey system with state feedback weighted harvest strategy,” AIMS Mathematics 8 (2023), 26968–26990. DOI: 10.3934/math.20231380.
