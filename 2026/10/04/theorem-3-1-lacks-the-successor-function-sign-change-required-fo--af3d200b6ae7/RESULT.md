# Theorem 3.1 lacks the successor-function sign change required for its periodic-orbit existence argument
## Finding
Xu, Shen, and Cao study a unilateral state-dependent impulse in which the continuous flow is followed, at the lower threshold \(x=h_1\), by
\[
x^+=(1+p_1)h_1,\qquad y^+=y-\tau_1.
\]
Their Theorem 3.1 asserts existence of an order-1 periodic solution under \(h_1<(1+p_1)h_1<x_1^*\) and \(y_B-\tau_1\ge y_A\). The published proof does not establish that conclusion in the strict case.

For a phase point \(A\in N_1=\{{x=(1+p_1)h_1\}}\) whose continuous trajectory first reaches \(B\in M_1=\{{x=h_1\}}\), the model itself gives
\[
f(A)=y_{B^+}-y_A=y_B-\tau_1-y_A.
\]
The proof instead prints \(f(A)=y_B(1-p_1)-y_A\). That expression is incompatible with the stated impulse, because \(p_1\) changes the prey coordinate and the predator jump is additive.

The decisive issue is the sign argument. In case \(y_{B^+}>y_A\), the proof correctly needs a second phase point with negative successor value. It then selects \(A_1\), states \(y_{B_1}>y_B\), and its own displayed algebra concludes
\[
f(A_1)=y_{B_1}-y_B>0.
\]
Both displayed endpoint signs are therefore positive. Continuity alone cannot produce a zero between two points having the same sign. Hence the intermediate-value step in Theorem 3.1 is invalid as written.

## Assumptions and scope
The statement concerns only the proof of Theorem 3.1 for system (2.2), with the impulse rule printed in that system. It assumes the orbit segments used by the source exist and that the successor function is continuous on the interval under discussion, exactly as the source invokes. No claim is made that the theorem itself is false, that Example 4.1 is numerically incorrect, or that other periodic-orbit theorems in the article fail.

The equality case \(y_B-\tau_1=y_A\) is different: under the printed reset, it directly means \(f(A)=0\) and therefore closes an order-1 orbit if the stated orbit segment and impulse are admissible. The unresolved part is the strict case \(y_B-\tau_1>y_A\), where an actual opposite-sign successor value or a different fixed-point argument is needed.

## Proof
Let \(A=((1+p_1)h_1,y_A)\) lie on the phase set \(N_1\), and suppose its continuous trajectory reaches \(B=(h_1,y_B)\) on the impulse set \(M_1\). Applying the printed jump \(\Delta x=p_1x\), \(\Delta y=-\tau_1\) gives
\[
B^+=((1+p_1)h_1,y_B-\tau_1).
\]
Because the successor function compares the returned phase height with the starting phase height,
\[
f(A)=y_{B^+}-y_A=y_B-\tau_1-y_A.
\]
There is no multiplicative factor involving \(p_1\) in the predator coordinate. This establishes the first inconsistency in the printed calculation.

Now assume the strict case in the theorem proof, so \(f(A)>0\). The proof explicitly says it remains to find \(A_1\in N_1\) with \(f(A_1)<0\). However, after choosing \(A_1\) so that its impact point satisfies \(y_{B_1}>y_B\), the paper displays
\[
f(A_1)=y_{B_1}-y_B>0.
\]
Irrespective of the separate sign error involving \(\tau_1\) in the preceding parenthesized expression, the displayed conclusion is positive. The intermediate value theorem guarantees a zero only when continuity is combined with a sign change (or an endpoint zero). The two positive values supplied in the proof do not meet that hypothesis.

Therefore the published argument does not prove existence in the strict case. A minimal logically sufficient replacement would have to establish points \(A_-\) and \(A_+\) in a connected domain of the successor map with
\[
f(A_-)\le 0\le f(A_+)
\]
(or the reversed inequalities), with at least one strict inequality unless an endpoint is already a fixed point. The current proof supplies no such second sign.

## Verification
The reset formula was checked directly against system (2.2) in the full text. Theorem 3.1 states the condition \(y_B-\tau_1\ge y_A\); its case (3) prints both \(f(A)>0\) and, after saying a negative value is needed, \(f(A_1)=y_{B_1}-y_B>0\). Example 4.1 uses the same lower-threshold reset with \(h_1=20\), \(\tau_1=2\), and \(p_1=0.25\), and reports a periodic orbit for that numerical parameter set.

The bundled checker `verify_successor.py` replays the reset algebra and a rational witness showing that the printed multiplicative expression can differ from the model-consistent successor value. Its output is `VERIFY_OK`. The checker is only an algebraic consistency check; the general logical conclusion follows from the exact formulas above, not from finite experimentation.

## Relationship to prior work
The 2022 state-dependent harvesting paper of Tian and coauthors defines a Poincaré/successor function as returned phase height minus starting phase height and explicitly notes that an everywhere-positive successor function has no fixed point. That standard fixed-point logic is consistent with the diagnosis here: a same-sign pair does not yield a periodic orbit by the intermediate value theorem.

A closely related 2024 bilateral-intervention predator-prey study analyzes periodic solutions with successor-function methods, but it concerns a different model and does not supply the missing sign estimate for Theorem 3.1 of the 2026 source. Searches for the exact theorem, its successor formulas, and corrections or errata did not locate a published repair or an earlier statement of this proof-gap diagnosis.

## Limitations
This finding is deliberately narrow. It does not prove nonexistence of periodic solutions under the hypotheses of Theorem 3.1, and it does not rule out a repair based on additional phase-plane geometry not supplied in the printed proof. The numerical Example 4.1 can still be a valid parameter-specific orbit. The remaining mathematical question is whether the theorem's stated hypotheses alone imply a second successor value of opposite sign.

## References
1. J. Xu, H. Shen, X. Cao, “Dynamics of a modified Leslie–Gower model with dual Allee effects under unilateral and bilateral control,” AIMS Mathematics 11 (2026), 17820–17837. DOI: 10.3934/math.2026726.
2. Y. Tian et al., “The Study of a Predator-Prey Model with Fear Effect Based on State-Dependent Harvesting Strategy,” Complexity (2022), Article 9496599. DOI: 10.1155/2022/9496599.
3. Y. Tian, Y. Liu, K. Sun, “Complex dynamics of a predator-prey fishery model: The impact of the Allee effect and bilateral intervention,” Electronic Research Archive 32 (2024), 6379–6404. DOI: 10.3934/era.2024297.
