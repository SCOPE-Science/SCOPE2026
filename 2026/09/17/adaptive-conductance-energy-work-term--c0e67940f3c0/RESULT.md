# Exact conductance-work correction to an adaptive bioelectric Lyapunov balance

## Result

Consider a finite undirected graph with symmetric edge conductances \(G_{ij}(t)=G_{ji}(t)\ge 0\) and voltage dynamics
\[
C\dot V_i=-f(V_i)+\sum_{j\in\mathcal N(i)}G_{ij}(t)(V_j-V_i)+F_i(t),
\]
where \(C>0\), \(U'=f\), and \(F_i\) collects all non-gradient voltage forcing. Define the instantaneous network energy
\[
E(V,G)=\sum_i U(V_i)+\frac12\sum_{(i,j)\in\mathcal E}G_{ij}(V_i-V_j)^2,
\]
with each undirected edge counted once.

### Theorem — exact balance for time-dependent conductances

Along every differentiable trajectory,
\[
\boxed{
\frac{dE}{dt}
=-C\|\dot V\|_2^2
+\sum_i F_i\dot V_i
+\frac12\sum_{(i,j)\in\mathcal E}\dot G_{ij}(V_i-V_j)^2.}
\]
Thus time-dependent coupling contributes an explicit **conductance-work term**
\[
W_G:=\frac12\sum_{(i,j)\in\mathcal E}\dot G_{ij}(V_i-V_j)^2.
\]
The exact instantaneous descent criterion is
\[
\sum_iF_i\dot V_i+W_G\le C\|\dot V\|_2^2,
\]
with strict inequality for strict descent.

For the model of Cortés-Poza (2026),
\[
F_i=\Gamma_i+I_i^{\rm ext}+W_i,
\]
and the conductances obey
\[
\tau_G\dot G_{ij}
=\alpha_G\sigma(V_i)\sigma(V_j)
+\beta_G\frac{R_i+R_j}{2}
+\gamma_G\frac{\varepsilon_i+\varepsilon_j}{2}
-\lambda_GG_{ij}.
\]
Consequently, the paper's Eq. (39),
\[
\dot E=-C\|\dot V\|^2+\sum_i\Gamma_i\dot V_i,
\]
is the fixed-conductance, zero-external-input, zero-wound specialization of the exact balance; it is not an identity for the adaptive full system as written. Theorem 1 of that paper remains valid in its stated fixed-\(G\) setting.

### Counterexample — adaptation alone can increase the instantaneous energy

Take a graph of two cells joined by one edge. Use the symmetric cubic from the source model,
\[
f(V)=aV(V^2-b^2),\qquad b=1.5,
\]
and set all non-gradient voltage forcing to zero at the state under consideration. Let
\[
V_1=-x,\qquad V_2=x,\qquad 0<x<b,
\]
and choose
\[
G=\frac a2(b^2-x^2)>0.
\]
Then both voltage derivatives vanish exactly:
\[
\dot V_1=\dot V_2=0.
\]
With \(R_i=\varepsilon_i=0\), the adaptive edge law reduces to
\[
\tau_G\dot G=\alpha_G\sigma(-x)\sigma(x)-\lambda_GG.
\]
Because the logistic sigmoid satisfies \(\sigma(-b)\sigma(b)>0\), while \(G\to0\) as \(x\to b^-\), every \(\alpha_G>0\) admits \(x\) sufficiently close to \(b\) for which \(\dot G>0\). At such a state,
\[
\dot E=\frac12\dot G(2x)^2>0,
\]
even though \(\dot V=0\). Thus adaptive conductance can inject energy by changing the landscape itself; slow adaptation does not give a sign theorem because the dissipative voltage term can vanish while \(W_G\) remains positive.

Using the nominal values employed in the source model/code,
\[
a=1.2,\quad b=1.5,\quad \alpha_G=0.30,\quad
\lambda_G=0.10,\quad \tau_G=5,
\]
with the implementation's conductance sigmoid slope \(k=3\), choose \(x=1.49\). Then
\[
G=0.01794,
\]
\[
\dot V_1\approx-6.94\times10^{-18},\qquad
\dot V_2\approx 6.94\times10^{-18},
\]
\[
\dot G\approx3.1258\times10^{-4},\qquad
\dot E\approx1.3879\times10^{-3}>0.
\]
The compact verification artifact reproduces these values directly.

## Proof

Differentiate the energy, remembering that both \(V\) and \(G\) vary:
\[
\frac{dE}{dt}
=\sum_i f(V_i)\dot V_i
+\sum_{(i,j)\in\mathcal E}G_{ij}(V_i-V_j)(\dot V_i-\dot V_j)
+\frac12\sum_{(i,j)\in\mathcal E}\dot G_{ij}(V_i-V_j)^2.
\]
Symmetry of the undirected conductances gives
\[
\sum_{(i,j)\in\mathcal E}G_{ij}(V_i-V_j)(\dot V_i-\dot V_j)
=\sum_i\dot V_i\sum_{j\in\mathcal N(i)}G_{ij}(V_i-V_j).
\]
Therefore
\[
\frac{dE}{dt}
=\sum_i\dot V_i\left[f(V_i)+\sum_jG_{ij}(V_i-V_j)\right]+W_G.
\]
Rearranging the voltage equation yields
\[
f(V_i)+\sum_jG_{ij}(V_i-V_j)=-C\dot V_i+F_i,
\]
which proves the boxed identity.

For the two-cell state, oddness of \(f(V)=aV(V^2-b^2)\) and the chosen value of \(G\) give
\[
-f(x)+G(-2x)=ax(b^2-x^2)-2Gx=0,
\]
and the equation for \(-x\) vanishes similarly. The stated sign of \(\dot G\) follows by continuity as \(x\to b^-\), and the energy-rate conclusion is then immediate from the exact balance.

## Consequences for the 2026 morphogenesis model

The source paper correctly proves Lyapunov descent for the **pure bioelectric subsystem with fixed conductances**. Later, however, Eq. (39) is described as the energy rate "in the full model," and numerical full-model plots interpret monotone energy traces through that two-term decomposition. Because the full model explicitly evolves \(G_{ij}(t)\), the conductance-work term is required by the chain rule. External electrical forcing and the wound contribution likewise enter the exact voltage-work term when present.

Accordingly, the source paper's reported monotone trajectories remain valid numerical observations for those runs, but monotonicity is not structurally certified by the displayed Eq. (39) or by the fixed-\(G\) theorem. A correct full-model dissipativity test must monitor
\[
\Gamma\cdot\dot V+I^{\rm ext}\cdot\dot V+W\cdot\dot V+W_G
\]
rather than \(\Gamma\cdot\dot V\) alone. The identity also clarifies the paper's open Problem 7: an exact Lyapunov functional for the adaptive system must either absorb the work performed by the evolving couplings or establish a compensating sign/estimate for that work.

## Limitations

This result corrects the derivative of the specific instantaneous energy \(E(V,G)\); it does not prove that no different composite Lyapunov function exists for the full hybrid model. It does not invalidate the fixed-conductance Theorem 1. The counterexample is an instantaneous state-space obstruction to a global monotonicity theorem, not a claim that the published nominal regeneration trajectories exhibit an observed energy increase. Discrete occupancy/morphology updates can introduce additional nonsmooth bookkeeping if one attempts to extend a continuous-time energy law across those events. The numerical values in the artifact use the public implementation's sigmoid slope and parameterization; the analytic counterexample does not depend on those particular numerical values beyond positive voltage-driven adaptation.

## References

1. Y. Cortés-Poza, *A hybrid mathematical framework for morphogenesis and regeneration*, Journal of Mathematical Biology 93, 43 (2026). https://doi.org/10.1007/s00285-026-02459-2
2. Public implementation accompanying the paper, repository state inspected at commit `2b53a08fe096394496b482cecef39b695b500ed7`. https://github.com/YuririaCP/bioelectricity/tree/2b53a08fe096394496b482cecef39b695b500ed7
