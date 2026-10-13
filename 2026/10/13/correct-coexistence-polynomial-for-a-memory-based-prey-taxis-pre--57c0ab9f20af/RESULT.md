# Correct coexistence polynomial for a memory-based prey-taxis predator–prey model
## Finding
For the memory-based prey-taxis predator–prey system of Liu and Tan, the *homogeneous coexistence* equilibrium reduction printed in equations (3.4)–(3.5) is not algebraically equivalent to the stated reaction kinetics. The correct reduction is another quadratic, whose leading coefficient is **strictly positive for all positive parameters**. An explicit exact-rational parameter set has one physically admissible coexistence equilibrium that is absent from the paper's printed quadratic.

The discrepancy matters because the source uses the signs, discriminant, and vertex of its quadratic to classify coexistence branches and potential saddle-node transitions. It is not merely an algebraic change of notation: the two quadratic equations have different admissible roots.

## Assumptions and scope
The prey and predator reaction kinetics are exactly those of the source's system (1.1):
\[
\begin{aligned}
G_1(u,v)&=ru\left(1-\frac uK\right)-\frac{\alpha uv}{u+mv}-\beta_1\eta u,\\
G_2(u,v)&=\frac{\beta uv}{u+mv}-\gamma v-\beta_2v(A-u)-\beta_3\eta v-\gamma_1v^2.
\end{aligned}
\]
The constants \(r,K,\alpha,m,\beta,\gamma,\beta_1,\beta_2,\beta_3,A,\gamma_1\) are strictly positive and the stress level \(\eta\ge0\). The ratios are evaluated at \(u,v>0\), where \(u+mv>0\).

The result concerns *spatially homogeneous positive equilibria* on any domain with the paper's homogeneous Neumann boundary conditions. The diffusion, memory delay, and taxis terms vanish on such constant states. No assertion is made about nonconstant stationary patterns or stability of any branch.

## Proof
Define the prey per-capita growth balance
\[
R(u)=r\left(1-\frac uK\right)-\beta_1\eta.
\]
For a positive equilibrium, \(G_1(u,v)=0\) implies
\[
R(u)=\frac{\alpha v}{u+mv}\qquad\Longleftrightarrow\qquad
v=\frac{uR(u)}{\alpha-mR(u)}.
\]
Because \(u,v>0\), this is possible only when
\[
0<R(u)<\frac{\alpha}{m}.
\]
Conversely, for any \(u>0\) satisfying those two strict inequalities, the displayed formula supplies a finite positive \(v\) with \(G_1(u,v)=0\). If \(r\le\beta_1\eta\), the interval is empty and there is no positive coexistence equilibrium. Otherwise define
\[
U=K\left(1-\frac{\beta_1\eta}{r}\right),\qquad
L=\frac{K(r-\beta_1\eta-\alpha/m)}{r}.
\]
The admissible prey interval is \(\max\{0,L\}<u<U\), interpreted through the strict inequalities above.

Let
\[
C_1=\gamma+\beta_2A+\beta_3\eta,\qquad
\Theta=K(\alpha-mr+m\beta_1\eta),
\]
\[
T(u)=K(\alpha-mR(u))=\Theta+mr u,
\qquad Q(u)=KR(u)=K(r-\beta_1\eta)-ru.
\]
On the admissible interval, \(T(u)>0\), and
\[
v=\frac{uQ(u)}{T(u)},\qquad
u+mv=\frac{\alpha Ku}{T(u)}.
\]
Substitute these identities into the predator equilibrium condition \(G_2(u,v)/v=0\):
\[
0=\frac{\beta T(u)}{\alpha K}-C_1+\beta_2u-
\gamma_1\frac{uQ(u)}{T(u)}.
\]
Multiplying by the positive denominator \(\alpha K T(u)\) gives precisely
\[
F(u)=\beta T(u)^2-\alpha KC_1T(u)+\alpha K\beta_2uT(u)
-\alpha K\gamma_1uQ(u)=0.
\]
No inadmissible root is introduced because multiplication occurs only where \(T(u)>0\). Every root in the admissible interval recovers exactly one positive predator coordinate. The root-to-equilibrium map is therefore a bijection.

Expanding \(T(u)=\Theta+mr u\) and \(Q(u)=K(r-\beta_1\eta)-ru\) gives
\[
F(u)=A_{\rm true}u^2+B_{\rm true}u+C_{\rm true}
\]
with
\[
\begin{aligned}
A_{\rm true}&=\beta(rm)^2+\alpha Kr(m\beta_2+\gamma_1),\\
B_{\rm true}&=2\beta rm\Theta-\alpha KrmC_1
+\alpha K\beta_2\Theta-\alpha K^2\gamma_1(r-\beta_1\eta),\\
C_{\rm true}&=\beta\Theta^2-\alpha K\Theta C_1.
\end{aligned}
\]
All terms in \(A_{\rm true}\) are positive, so \(A_{\rm true}>0\) for every parameter choice in scope.

The source instead prints, with \(C_2=\beta_2-\gamma_1\),
\[
A_{\rm src}=\beta(rm)^2+\alpha Kr C_2,
\qquad B_{\rm src}=2\beta rm\Theta-\alpha KrmC_1
-\alpha K^2(r-\beta_1\eta)C_2,
\]
and \(C_{\rm src}=C_{\rm true}\). These are not the coefficients derived from the stated predator equation. In particular, the source permits a negative \(A_{\rm src}\), but no negative quadratic leading coefficient arises from the actual kinetics.

For the concrete positive parameter choice
\[
(r,K,\alpha,m,\beta,\gamma,\beta_1,\beta_2,\beta_3,A,\gamma_1,\eta)
=\left(2,2,2,1,\frac43,\frac14,1,1,\frac12,1,\frac32,\frac12\right),
\]
one has \(R(u)=3/2-u\), \(T(u)=1+2u\), and the admissible interval \(0<u<3/2\). Direct substitution gives
\[
F(u)=\frac23(u-1)(38u+7),\qquad
f_{\rm src}(u)=\frac23(2u^2-u-7).
\]
The first has exactly one root in the admissible interval, namely \(u=1\), with
\[
v\big|_{u=1}=\frac{u(3-2u)}{1+2u}\bigg|_{u=1}=\frac13.
\]
Direct evaluation of both original reaction rates gives \(G_1(1,1/3)=G_2(1,1/3)=0\). The printed quadratic has roots
\[
\frac{1\pm\sqrt{57}}4;
\]
the positive one exceeds \(3/2\) and the negative one is outside the interval. Thus it misses the exact coexistence state.

There is also an independent consistency comparison with the paper's numerical baseline (6.1): substituting its numerical parameters into the correct and printed quadratics gives, respectively,
\[
F(u)=\frac{27}{50000}(1212u^2-272u-135),
\]
\[
f_{\rm src}(u)=\frac9{50000}(696u^2+2774u-405).
\]
Their positive roots are approximately \(0.4643156045\) and \(0.1410097041\). The paper reports \(u^*\approx0.4643\), consistent with the true reduction rather than its printed coefficients. This secondary check does not depend on the constructed exact-rational example.

## Verification
The standalone script `verification/verify.py` uses SymPy exact polynomial algebra to verify the identity between the original reaction equations and the new scalar polynomial, confirm all three coefficients, replay the exact counterexample and its admissible interval, and reconstruct both quadratics at the source's numerical parameters. Its output is `VERIFY_OK` when all assertions pass. The symbolic derivation above supplies the universal proof; numerical root approximations are supporting checks only.

## Relationship to prior work
The motivating article studies memory-based prey-taxis and environmental stress and uses its Section 3 coexistence polynomial as part of an equilibrium and bifurcation classification. Equations (1.1), (3.1), and (3.2) in that article determine the exact positive-equilibrium relation used here, while equation (3.5) lists the different coefficients. Its numerical coexistence value in Section 6 agrees with the corrected reduction. The comparison is internal to the published paper, not an assertion that finding stationary states by scalar elimination is a novel technique.

Cao, Cai, and Luo (2022) and Kong and Lv (2025) study positive steady states and prey-taxis effects for different ratio-dependent predator–prey kinetics. Those broader works establish the mathematical motivation for reliable coexistence classifications but do not supply the specific coefficient identities for Liu and Tan's 2026 environmental-stress model. In particular, the present result is not a claim of a general new existence theorem for all prey-taxis systems.

## Limitations
The result corrects the homogeneous equilibrium reduction for the reaction kinetics printed in (1.1). It does **not** prove or disprove the reported numerical Turing–Hopf patterns, nor does it reassess the paper's derivations involving time-delay phases or nonlinear normal forms. Its explicit rational counterexample proves a classification error without making a claim about a particular parameter range's full nonlinear dynamics. No spatially varying steady states are classified.

## References
1. D. Liu, X. Tan, “Memory-based prey-taxis and environmental stress shape spatiotemporal predator-prey dynamics,” *AIMS Mathematics* **11** (2026), 17880–17916. DOI: 10.3934/math.2026729.
2. Q. Cao, Y. Cai, Y. Luo, “Nonconstant positive solutions to the ratio-dependent predator-prey system with prey-taxis in one dimension,” *Discrete and Continuous Dynamical Systems B* **27** (2022), 1397–1420. DOI: 10.3934/dcdsb.2021095.
3. L. Kong, F. Lv, “Global Bifurcation in a General Leslie Type Predator–Prey System with Prey Taxis,” *Axioms* **14** (2025), 238. DOI: 10.3390/axioms14040238.
