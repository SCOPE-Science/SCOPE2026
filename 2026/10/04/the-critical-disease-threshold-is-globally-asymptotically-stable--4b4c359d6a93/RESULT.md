# The critical disease threshold is globally asymptotically stable
## Finding
For the age-structured predator--prey disease system
\[
\dot S=\Lambda-d_1S-\beta SI,\qquad
\dot I=\beta S(t-\tau_1)I(t-\tau_1)-\frac{I}{1+I}Q-d_2I,
\]
with \(Q(t)=\int_0^\infty q(t,a)\,da\), predator transport \(q_t+q_a=-d_3q\), and boundary recruitment \(q(t,0)=\frac{I(t)}{1+I(t)}\int_0^\infty h(a)q(t,a)\,da\), assume the source's nonnegative well-posed bounded solution class, positive \(\Lambda,d_1,d_2,d_3,\beta\), \(\tau_1\ge0\), and nonnegative bounded fertility \(h\in L^\infty(0,\infty)\). Then the disease-free equilibrium is globally asymptotically stable also on the omitted critical surface \(\Lambda\beta=d_1d_2\). More precisely, with \(\bar S=\Lambda/d_1\), every admissible solution satisfies \(S(t)\to\bar S\), \(I(t)\to0\), and \(\|q(t,\cdot)\|_{L^1}\to0\); in the age-profile formulation, \(s(t,\cdot)\to\Lambda e^{-d_1\cdot}\) and \(i(t,\cdot)\to0\) in \(L^1\). Hence the source's strict extinction condition sharpens from \(\Lambda\beta<d_1d_2\) to \(\Lambda\beta\le d_1d_2\). A Lyapunov--Krasovskii functional containing the delayed transmission flux and a small positive multiple of predator mass has nonpositive derivative at equality, and direct Barbalat/transport arguments identify the disease-free state as the only limiting invariant state.

## Assumptions and scope
The system is the nonnegative age-structured eco-epidemiological model printed in the cited 2026 source. The source proves well-posedness, non-negativity, and boundedness for its admissible histories. Here \(\Lambda,d_1,d_2,d_3,\beta>0\), \(\tau_1\ge0\), and \(h\ge0\) is essentially bounded. Write
\[
Q(t)=\int_0^\infty q(t,a)\,da,\qquad \bar S=\frac{\Lambda}{d_1},\qquad H=\|h\|_\infty.
\]
The critical surface is \(\beta\bar S=d_2\), equivalently \(\Lambda\beta=d_1d_2\). The conclusion concerns the source's biologically admissible bounded nonnegative solutions; it does not assert behavior for sign-changing data or for models with a different predator recruitment law.

## Proof
Choose \(c>0\) with \(cH\le1\); if \(H=0\), any \(c>0\) is allowed. Define
\[
\Phi(S)=S-\bar S-\bar S\log\!\left(\frac{S}{\bar S}\right)
\]
and the Lyapunov--Krasovskii functional
\[
W(t)=\Phi(S(t))+I(t)+\beta\int_{t-\tau_1}^t S(s)I(s)\,ds+cQ(t).
\]
For positive \(S\),
\[
\dot\Phi=-\frac{d_1}{S}(S-\bar S)^2-\beta I(S-\bar S).
\]
Integrating the predator transport equation over age and using the boundary condition gives
\[
\dot Q=\frac{I}{1+I}\int_0^\infty h(a)q(t,a)\,da-d_3Q
\le \left(\frac{HI}{1+I}-d_3\right)Q.
\]
The derivative of the delay term is \(\beta(SI-S_\tau I_\tau)\), where \(S_\tau=S(t-\tau_1)\) and \(I_\tau=I(t-\tau_1)\). Therefore
\[
\dot W\le -\frac{d_1}{S}(S-\bar S)^2+(\beta\bar S-d_2)I
-(1-cH)\frac{IQ}{1+I}-cd_3Q.
\]
At \(\beta\bar S=d_2\),
\[
\dot W\le -\frac{d_1}{S}(S-\bar S)^2-(1-cH)\frac{IQ}{1+I}-cd_3Q\le0.
\]
Thus the functional is nonincreasing. It is positive definite in the current quantities \(S-\bar S\), \(I\), and \(Q\), while the delay integral is nonnegative, giving Lyapunov stability for the admissible delay state.

It remains to prove attraction at the nonhyperbolic equality. Boundedness gives \(I(t)\le M\). Since
\[
\dot S\ge\Lambda-(d_1+\beta M)S,
\]
\(S\) is eventually bounded away from zero. The preceding dissipation identity makes
\[
\int_0^\infty \frac{(S(t)-\bar S)^2}{S(t)}\,dt<\infty.
\]
The integrand is uniformly continuous because \(S\), \(S^{-1}\), and \(\dot S\) are bounded for large time. Barbalat's lemma therefore yields \(S(t)\to\bar S\). The equation for \(I\) shows \(\dot I\) is bounded, hence \(\ddot S=-d_1\dot S-\beta(\dot S I+S\dot I)\) is bounded. Since \(S\) has a finite limit, the usual derivative form of Barbalat's lemma gives \(\dot S(t)\to0\). The susceptible equation then gives
\[
\beta S(t)I(t)=d_1(\bar S-S(t))-\dot S(t)\longrightarrow0,
\]
so \(I(t)\to0\). Consequently, for all sufficiently large \(t\), \(HI(t)/(1+I(t))\le d_3/2\), and the comparison inequality for \(Q\) yields exponential decay \(Q(t)\to0\). Since \(q\ge0\), \(Q(t)=\|q(t,\cdot)\|_{L^1}\).

Finally, in the source's age-profile reformulation, the susceptible transport component has mortality \(d_1\) and boundary input \(\Lambda-\beta SI\to\Lambda\). The characteristic formula and dominated convergence therefore give \(s(t,\cdot)\to\Lambda e^{-d_1\cdot}\) in \(L^1\). Nonnegativity gives \(\|i(t,\cdot)\|_{L^1}=I(t)\to0\). Hence the full disease-free age profile is globally attracting, and the Lyapunov estimate supplies stability.

The same derivative formula contains the extra nonpositive term \((\beta\bar S-d_2)I\) when \(\Lambda\beta<d_1d_2\), so the closed threshold is \(\Lambda\beta\le d_1d_2\).

## Verification
The symbolic checker `verify.py` reconstructs the differentiated functional before imposing the critical relation and verifies the exact identity
\[
\dot W_0=-\frac{d_1}{S}(S-\bar S)^2+(\beta\bar S-d_2)I-\frac{IQ}{1+I},
\]
where \(W_0\) is the functional without the \(cQ\) term. It also verifies the algebraic cancellation of the delayed flux. The remaining \(cQ\) estimate uses only \(0\le\int hq\le H Q\). The checker is a verification aid; the infinite-time conclusion is established analytically above rather than by finite simulation.

## Relationship to prior work
The motivating 2026 paper states global asymptotic stability of the disease-free equilibrium for the strict inequality \(\Lambda\beta<d_1d_2\) and instability for \(\Lambda\beta>d_1d_2\), leaving equality unstated. An earlier 2026 paper by Yan, Jin, Yuan, and Fu prints the same transmission/predator structure and the same strict split, so it also does not cover equality. General delayed and age-structured epidemic papers do sometimes treat a critical reproduction threshold, but the inspected statements concern different state spaces and do not include this coupled age-structured predator recruitment equation. The present argument is source-specific: the predator predation term and predator boundary recruitment are combined with the delayed transmission flux in one Lyapunov--Krasovskii balance.

## Limitations
The result uses the source's established bounded nonnegative solution class and the bounded nonnegative fertility kernel. It does not prove a convergence rate for \(I\) on the critical surface, does not address the endemic or positive equilibria, and does not extend automatically to sign-changing fertility, unbounded fertility kernels, or altered incidence/predator recruitment. The literature comparison cannot exclude an unindexed equivalent theorem, although targeted searches found no same-model equality result.

## References
1. D. Yan, Y. Jin, Y. Yuan, and X. Fu, “Asymptotic Analysis of an Age-Structured Predator–Prey Model with Two Time Delays and Disease in the Prey Species,” *International Journal of Bifurcation and Chaos* 36 (2026), 2650097. DOI: 10.1142/S0218127426500975. First verified public date: 2026-02-28.
2. D. Yan and H. Cao, “Rich dynamics of an age-structured predator-prey model with double time delays and prey-infection,” *Evolution Equations and Control Theory* 25 (2026), 234–261. DOI: 10.3934/eect.2026089. Published online 2026-07-31; primary MSC 92D25.
3. C. C. McCluskey, “Global stability for an SEI epidemiological model with continuous age-structure in the exposed and infectious classes,” *Mathematical Biosciences and Engineering* 9 (2012), 819–841. DOI: 10.3934/mbe.2012.9.819.
4. “Global stability of an epidemic model with delay and general nonlinear incidence,” *Applied Mathematics and Computation* (2011), DOI record indexed under PMID 21077711; the critical case is treated for a different delayed SIR framework.
