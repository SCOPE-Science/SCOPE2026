# The printed exponential-synapse phase kernel is not periodic
## Finding
For the periodically spiking Izhikevich neuron used by Cheng and Campbell, let \(T>0\) be one spike period and let the synaptic gate satisfy
\[
\dot s=-\beta s,\qquad s\mapsto 1\ 	ext{{at each presynaptic spike}},\qquad \beta>0.
\]
If the postsynaptic phase is represented by \(t\in[0,T)\) and the presynaptic oscillator is shifted by \(\phi\in[0,T)\), then the gate entering the phase interaction is
\[
s_\phi(t)=\exp\left[-\beta\bigl((t+\phi)\bmod T\bigr)\right].
\]
Equivalently,
\[
s_\phi(t)=
\begin{{cases}}
 e^{-\beta(t+\phi)},&0\le t<T-\phi,\\
 e^{-\beta(t+\phi-T)},&T-\phi\le t<T.
\end{{cases}}
\]
Equation (23) of arXiv:2610.04025v1 prints only the first branch, \(e^{-\beta(t+\phi)}\), over the full integration interval. That expression cannot be the periodic synaptic gate used in the phase reduction.

Indeed, with
\[
W(t)=\bar Z^v(t)\bigl(\bar v(t)-v_{{\rm syn}}\bigr),
\]
the literal printed equations (22)--(23) give
\[
H_{{\rm print}}(\phi)=-\frac1T\int_0^T W(t)e^{-\beta(t+\phi)}\,dt
=Ae^{-\beta\phi}
\]
for a constant \(A\). Hence
\[
H_{{\rm print,odd}}(\phi)=H_{{\rm print}}(\phi)-H_{{\rm print}}(-\phi)
=-2A\sinh(\beta\phi).
\]
Unless \(A=0\), this function is not \(T\)-periodic and has no zero at the anti-phase point \(\phi=T/2\). If \(A=0\), it is identically zero and supplies no stability information. Both alternatives contradict the structural periodicity of the phase interaction and the paper's use of a nontrivial anti-phase equilibrium.

Thus the wrap-around reset is not optional bookkeeping: it is required for the printed phase-reduction formula to represent the stated hybrid synapse. This conclusion concerns the formula as printed, not the unseen numerical implementation.

## Assumptions and scope
The statement uses exactly the single-exponential synapse and reset rule printed in equations (21)--(23) of arXiv:2610.04025v1. One presynaptic spike occurs per period \(T\), the gate decays exponentially between spikes, and each spike resets the gate to \(1\). The phase offset is represented in time units after the paper sets \(\Omega=1\).

The claim does not assert that the numerical figures are wrong. The reported figures may have been generated with a periodic implementation even though equation (23) omits the second branch. Nor does the claim address the iPRC boundary-value problem, the single-cell bifurcation analysis, or the validity of first-order phase reduction itself.

## Proof
Choose phase origin immediately after a presynaptic spike. During one period the unshifted gate is \(s(t)=e^{-\beta t}\) for \(0\le t<T\), followed by the reset \(s(T)=1\). Therefore its periodic extension is
\[
s(t)=e^{-\beta(t\bmod T)}.
\]
A phase shift by \(\phi\) replaces \(t\) by \(t+\phi\), yielding
\[
s_\phi(t)=e^{-\beta((t+\phi)\bmod T)}.
\]
For \(0\le\phi<T\), the single wrap point inside \([0,T)\) occurs at \(t=T-\phi\), giving the displayed two-branch formula.

Now substitute the literal printed equation (23) into equation (22). Every dependence on \(\phi\) factors out:
\[
H_{{\rm print}}(\phi)
=-e^{-\beta\phi}\frac1T\int_0^T
\bar Z^v(t)\bigl(\bar v(t)-v_{{\rm syn}}\bigr)e^{-\beta t}\,dt
=Ae^{-\beta\phi}.
\]
The odd part is therefore \(-2A\sinh(\beta\phi)\). For \(A\ne0\), it cannot be periodic and its only real zero is \(\phi=0\), so it cannot possess the anti-phase zero forced by a periodic odd interaction at half a period. For \(A=0\), it vanishes identically. Thus the printed one-branch expression is incompatible with the phase model's own periodic structure in all cases.

The corrected gate is periodic by construction. Substitution into equation (22) gives a periodic interaction function because shifting \(\phi\) by \(T\) leaves \((t+\phi)\bmod T\) unchanged.

## Verification
The check is symbolic and uses no simulation. The source was inspected at the general weak-coupling equations, the statement that \(H\) is periodic, the anti-phase equilibrium argument, the hybrid reset rule \(s_i\mapsto1\), and equations (22)--(23). The contradiction is obtained by direct substitution and factorization.

As an independent boundary check, at \(t=T-\phi\) the presynaptic oscillator spikes. The physical gate must jump from \(e^{-\beta T}\) immediately before the spike to \(1\) immediately after it. The printed \(e^{-\beta(t+\phi)}\) instead remains continuous and equals \(e^{-\beta T}\), proving locally that the reset has been omitted.

## Relationship to prior work
Standard phase-reduction literature for integrate-and-fire and hybrid oscillators treats the phase variable cyclically. Cheng and Campbell cite Ladenbauer et al. for discontinuous-neuron phase reduction and state explicitly that their interaction function is periodic. The present observation is narrower: it identifies the missing periodic reset in their displayed single-exponential synaptic formula and derives the contradiction that results if that formula is used literally.

Targeted searches for the paper identifier, the equation-23 formulation, periodic wrap-around exponential synapses, and Izhikevich phase-interaction corrections did not locate a published correction or an implication-equivalent result. The closest literature found develops phase reduction for related integrate-and-fire models but does not discuss this 2026 displayed formula.

## Limitations
The authors' numerical code was not publicly identified in the inspected source, so this result cannot determine whether the implementation used the correct periodic wrap-around. The agreement between their phase-model plots and full-model simulations may indicate that the omission is typographical. The finding therefore corrects the reproducible mathematical specification, not the reported numerical conclusions.

## References
Cheng, X. and Campbell, S. A., *Stability of Phase-locked States of Weakly Coupled Izhikevich Neurons*, arXiv:2610.04025v1, 2026.

Ladenbauer, J., Augustin, M., Shiau, L., and Obermayer, K., *Impact of Adaptation Currents on Synchronization of Coupled Exponential Integrate-and-Fire Neurons*, PLOS Computational Biology 8(4):e1002478, 2012, DOI:10.1371/journal.pcbi.1002478.
