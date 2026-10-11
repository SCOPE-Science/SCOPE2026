# An equilibrium balance invalidates two published stability arguments
## Finding
Consider the predator–prey–additional-food system
\[
\begin{aligned}
\dot x&=\frac{rx}{1+kA_0y}-r_0x-r_1x^2-\frac{\alpha A_0xy}{(1+ax)(1+by)},\\
\dot A&=\lambda(1-A_0)y-\beta A-\phi Ay,\\
\dot y&=\frac{c_1\alpha A_0xy}{(1+ax)(1+by)}+c_2\phi Ay-\delta y-ey^2,
\end{aligned}
\]
with the source assumptions that the model parameters are positive and \(0\le A_0\le1\). Let \(E^*=(x^*,A^*,y^*)\) be any strictly positive equilibrium.

The equilibrium equation for the additional-food variable gives exactly
\[
A^*=\frac{\lambda(1-A_0)y^*}{\beta+\phi y^*}.
\]
Since \(A^*>0\) and \(y^*>0\), necessarily \(A_0<1\). Because \(\beta>0\),
\[
0<A^*<\frac{\lambda(1-A_0)}{\phi}.
\]
Hence the first inequality in the published sufficient condition (4.16),
\[
\frac{\lambda(1-A_0)}{\phi}<A^*,
\]
can never hold at a strictly positive equilibrium.

The same balance gives
\[
\phi A^*-\lambda(1-A_0)
=-\frac{\lambda(1-A_0)\beta}{\beta+\phi y^*}<0.
\]
In the proof of Theorem 6 the source chooses
\[
L_1=\frac{L_2c_2\phi}{\phi A^*-\lambda(1-A_0)},
\]
while explicitly requiring \(L_1,L_2>0\). Since \(L_2,c_2,\phi>0\), the displayed choice actually has \(L_1<0\). Therefore the proposed function has a negative quadratic coefficient in the \(A\)-direction and is not positive definite near \(E^*\). The ensuing Sylvester-criterion step cannot establish the claimed global asymptotic stability from (4.17).

## Assumptions and scope
The conclusion concerns the exact system (2.3) and strictly positive equilibria under the source's positive-parameter assumptions. No uniqueness assumption is needed for the algebraic obstruction: every positive equilibrium satisfies the same additional-food balance. The result distinguishes statements from proofs. It does not claim that the Routh–Hurwitz condition (4.15) is wrong, nor does it construct an unstable parameter set satisfying (4.17); it shows that the auxiliary criterion (4.16) is empty and that the stated Lyapunov proof of Theorem 6 cannot work with its prescribed coefficient.

## Proof
At equilibrium, the second equation of system (2.3) is
\[
0=\lambda(1-A_0)y^*-A^*(\beta+\phi y^*).
\]
Solving for \(A^*\) yields
\[
A^*=\frac{\lambda(1-A_0)y^*}{\beta+\phi y^*}.
\]
If \(A_0=1\), the right-hand side is zero, contradicting \(A^*>0\); hence \(A_0<1\). Dividing by the positive quantity \(\lambda(1-A_0)/\phi\) gives
\[
\frac{A^*}{\lambda(1-A_0)/\phi}
=\frac{\phi y^*}{\beta+\phi y^*}<1,
\]
proving the strict reverse of the first inequality in (4.16).

For Theorem 6,
\[
\phi A^*-\lambda(1-A_0)
=\lambda(1-A_0)\left(\frac{\phi y^*}{\beta+\phi y^*}-1\right)
=-\frac{\lambda(1-A_0)\beta}{\beta+\phi y^*}<0.
\]
Thus the denominator in the published formula for \(L_1\) is negative. Its numerator \(L_2c_2\phi\) is positive under the proof's own stated assumptions, so \(L_1<0\). Holding \(x=x^*\) and \(y=y^*\) while varying \(A\), the displayed candidate satisfies
\[
V(x^*,A,y^*)=\frac{L_1}2(A-A^*)^2<0
\]
for every \(A\ne A^*\) sufficiently near \(A^*\). Hence it is not positive definite and cannot serve as the asserted Lyapunov function.

## Verification
The accompanying checker symbolically substitutes the equilibrium identity and verifies both sign formulas. It also verifies that the published \(A\)-quadratic contribution is negative exactly when \(L_1>0\), whereas the prescribed formula forces \(L_1<0\). The checker uses exact symbolic algebra and contains no numerical approximation.

## Relationship to prior work
The source itself states the positive-equilibrium equations, including
\[
A^*=\frac{\lambda(1-A_0)y^*}{\beta+\phi y^*},
\]
then later gives (4.16) and the Lyapunov coefficient used in Theorem 6. The new contribution is the implication comparison across those parts of the same paper: the equilibrium identity reverses the first inequality in (4.16) and fixes the sign of the coefficient in Theorem 6. Exact-title, DOI, formula-alias, stability-condition, and proof-correction searches did not locate an erratum or another source stating this obstruction. Search nonappearance is not treated as proof of novelty.

## Limitations
This result invalidates a sufficient condition and a particular published proof, not necessarily the underlying stability conclusions. The local Routh–Hurwitz criterion (4.15) may still certify stability for some parameter sets, and Theorem 6 could conceivably be true on some region by a different argument. No claim is made about the paper's Hopf calculations or numerical bifurcation diagrams beyond the dependence of any theorem invocation on the corrected stability logic.

## References
Reshma K P and Ankit Kumar, “Stability and bifurcation in a predator-prey system with effect of fear and additional food,” *AIMS Mathematics* 9(2) (2024), 4211–4240, DOI 10.3934/math.2024208. Relevant material: system (2.3), equilibrium equations (4.4), condition (4.16), and Theorem 6 with its Lyapunov coefficient.
