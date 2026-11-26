# Exact optimal hopping at prescribed squeezing in an aligned squeezed-bath dimer

## Finding

For every finite, prescribed bath squeezing \(r>0\), the smallest partially transposed symplectic eigenvalue of the stationary two-mode Gaussian state has a unique minimizer over nonnegative coherent hopping \(J\). With damping rate \(\gamma>0\), bath occupation \(\bar n\), and \(y=2\bar n+1\), it is
\[
J_*(r)=\frac{\gamma}{2}\sqrt{1-\tanh(2r)},\qquad
2\widetilde\nu_-(r,J_*)=\frac{y}{\sqrt{1+\tanh(2r)}}.
\]
Thus at this prescribed squeezing some hopping produces positive stationary logarithmic negativity if and only if \(y^2<1+\tanh(2r)\). If this inequality holds, \(J_*\) is also the unique maximizer of logarithmic negativity, and the maximum is \(\frac12\log_2(1+\tanh(2r))-\log_2 y\). Otherwise the logarithmic negativity vanishes at every hopping, though the eigenvalue minimizer is still unique. For \(1<y<\sqrt2\), the condition on prescribed squeezing is equivalently \(r>\frac14\log(y^2/(2-y^2))\), where \(\log\) denotes the natural logarithm. The equality case is not entangled. For \(r=0\), \(2\widetilde\nu_-=y\) at all hoppings, so uniqueness is not asserted.

## Model and scope

Two resonant harmonic modes in the common rotating frame have Hamiltonian \(H=J(a_1^\dagger a_2+a_2^\dagger a_1)\). They are coupled to independent Markovian local squeezed thermal baths of identical phase locked to this frame, equal squeezing \(r\ge0\), equal thermal occupation \(\bar n\ge0\), and equal energy damping rate \(\gamma>0\). Vacuum quadrature variance is \(1/2\) and \(\hbar=1\). The steady-state logarithmic negativity is \(\max\{0,-\log_2(2\widetilde\nu_-)\}\). Unaligned, laboratory-fixed, or unequal baths are not included.

## Proof

Under these assumptions the aligned-phase stationary solution of Ayoub, Castillo-Gonzalez and Bittner, Eqs. (2)–(8), (12), gives, with \(K=\cosh(2r)\), \(S=\sinh(2r)\), and \(\mu=\gamma^2/(\gamma^2+4J^2)\),
\[
\frac{2\widetilde\nu_-}{y}=\sqrt{K^2-\mu^2 S^2}-S\sqrt{\mu(1-\mu)}.
\]
For fixed \(r>0\), put \(t=S/K\in(0,1)\). The hopping parameterizes \(0<\mu\le1\) bijectively. Dividing the last display by \(K\), a sharp lower bound follows from the identity
\[
1-t^2\mu^2-\bigl(\sqrt{1-t}+t\sqrt{\mu(1-\mu)}\bigr)^2
=t\bigl(\sqrt{1-\mu}-\sqrt{(1-t)\mu}\bigr)^2.
\]
Both quantities whose squares are compared are nonnegative. The bound is attained only at \(\mu=(2-t)^{-1}\). Thus the normalized eigenvalue at the minimum is \(K\sqrt{1-t}=(1+t)^{-1/2}\), and solving for \(J\) gives the asserted hopping. At \(r=0\) the stationary formula gives \(2\widetilde\nu_-=y\). For \(r>0\), strict entanglement is feasible precisely when the minimum satisfies \(2\widetilde\nu_-<1\). On the positive-negativity branch the logarithm is strictly decreasing in \(2\widetilde\nu_-\), proving the optimizer and maximal value there. Solving \(\tanh(2r)>y^2-1\) gives the stated threshold. □

## Verification

The proof is an exact equality with a nonnegative remainder, valid over the full parameter domain. The retained `verify.py` (dependencies in `requirements.txt`) contains complementary finite checks of the stationary covariance using a quadrature Lyapunov solver, the partially transposed eigenvalue, and the minimum against sampled couplings. It also contains tests for auxiliary calculations not asserted here. Those numerical tests are not needed for uniqueness or the exact threshold.

## Relationship to prior work

Ayoub, Castillo-Gonzalez and Bittner, *Phase-Reference Control of Steady-State Entanglement in Open Quantum Systems*, [arXiv:2605.03978v1](https://arxiv.org/abs/2605.03978v1), give the model, the stationary eigenvalue, and qualitative optimization behavior; the stationary eigenvalue formula is not a contribution here. [*Phase detuning restores steady-state entanglement beyond the aligned-squeezing ceiling*](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-phase-detuning-restores-steady-state-entanglement-beyond-the-ali--e52661c21447) optimizes an effective squeezing variable at fixed hopping, by adjusting the relative phase. In contrast, this result holds the phase and the squeezing fixed and optimizes the hopping; the two optimizations have different constraints. The claim is restricted to the exact finite-resource hopping prescription and its sharp feasibility test. No priority claim is made about the joint resource supremum or effective-squeezing limit profiles.
