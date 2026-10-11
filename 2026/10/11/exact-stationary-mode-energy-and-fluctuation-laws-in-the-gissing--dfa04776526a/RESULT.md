# Exact stationary mode-energy and fluctuation laws in the Gissinger reversal model
## Finding
Consider the Gissinger three-mode reversal system
\[
\dot Q=\mu Q-VD,\qquad
\dot D=-\nu D+VQ,\qquad
\dot V=\Gamma-V+QD,
\]
with
\[
\mu>0,\qquad \nu>0,\qquad \Gamma\in\mathbb R.
\]
For every compactly supported invariant Borel probability measure \(\pi\), the three coordinate equations sharpen from integrated balances to conditional stationary regressions:
\[
\mathbb E_\pi[VD\mid Q]=\mu Q,
\qquad
\mathbb E_\pi[VQ\mid D]=\nu D,
\qquad
\mathbb E_\pi[QD\mid V]=V-\Gamma.
\]
In particular,
\[
\mu\,\mathbb E_\pi[Q^2]=\nu\,\mathbb E_\pi[D^2].
\]
Thus, unless \(\pi\) is the equilibrium atom at \((0,0,\Gamma)\),
\[
\frac{\operatorname{RMS}_\pi(D)}{\operatorname{RMS}_\pi(Q)}
=\sqrt{\frac{\mu}{\nu}}.
\]
The conditional laws also resolve three exact fluctuation defects:
\[
\operatorname{Var}_\pi(VD)-\mu^2\operatorname{Var}_\pi(Q)
=\mathbb E_\pi[\dot Q^2],
\]
\[
\operatorname{Var}_\pi(VQ)-\nu^2\operatorname{Var}_\pi(D)
=\mathbb E_\pi[\dot D^2],
\]
and
\[
\operatorname{Var}_\pi(QD)-\operatorname{Var}_\pi(V)
=\mathbb E_\pi[\dot V^2].
\]
At the reversal parameters used in the source,
\[
\mu=\frac{119}{1000},\qquad
\nu=\frac1{10},\qquad
\Gamma=\frac9{10},
\]
every nontrivial compact stationary state therefore has
\[
\frac{\operatorname{RMS}_\pi(D)}{\operatorname{RMS}_\pi(Q)}
=\frac{\sqrt{119}}{10}.
\]

## Assumptions and scope
The measure \(\pi\) is invariant under the complete autonomous flow and is supported on a compact subset of \(\mathbb R^3\). Compact support guarantees all moments and test-function integrals used below. The positivity assumptions on \(\mu\) and \(\nu\) are needed only for the nontrivial RMS ratio and its rigidity statement; the three conditional regressions themselves remain valid for arbitrary real parameters whenever a compact invariant measure exists.

The result concerns stationary statistics of all compact recurrent components: equilibrium atoms, periodic-orbit measures, quasiperiodic measures, and chaotic invariant measures are included. It does not assume ergodicity.

The earliest verified public source used here is arXiv:1109.6569v1, submitted publicly on 29 September 2011. The source identifies the model with chaotic reversals and uses \(Q\), \(D\), and \(V\) as three interacting amplitudes. Its displayed reversal example uses \(\mu=0.119\), \(\nu=0.1\), and \(\Gamma=0.9\).

## Proof
Let \(L\) be the generator of the flow. If \(h\) is continuously differentiable, compact invariance gives
\[
\int Lh\,d\pi=0.
\]

Fix an arbitrary continuous function \(\phi\) on the compact \(Q\)-projection of the support and choose a continuously differentiable antiderivative \(H\) with \(H'(Q)=\phi(Q)\). Then
\[
LH=\phi(Q)(\mu Q-VD).
\]
Stationarity for every such \(\phi\) yields
\[
\mathbb E_\pi[VD\mid Q]=\mu Q.
\]
The same argument with functions of \(D\) and of \(V\) gives
\[
\mathbb E_\pi[VQ\mid D]=\nu D
\]
and
\[
\mathbb E_\pi[QD\mid V]=V-\Gamma.
\]

There is also a single quadratic coboundary for the mode energies:
\[
L\left(\frac{Q^2+D^2}{2}\right)
=\mu Q^2-\nu D^2.
\]
Its stationary expectation gives
\[
\mu\,\mathbb E_\pi[Q^2]=\nu\,\mathbb E_\pi[D^2].
\]
If both second moments vanish, then \(Q=D=0\) almost surely. Invariance on that axis reduces the remaining equation to \(\dot V=\Gamma-V\). The only bounded complete trajectory of this scalar equation is \(V\equiv\Gamma\), so the only compact invariant probability with zero mode energy is the atom at \((0,0,\Gamma)\). For every other compact stationary state both second moments are positive, giving the stated RMS ratio.

For the fluctuation identities, the first regression says that the residual
\[
R_Q=VD-\mu Q=-\dot Q
\]
has zero conditional mean given \(Q\). Hence it is orthogonal in \(L^2(\pi)\) to every square-integrable function of \(Q\), in particular to \(Q-\mathbb E_\pi[Q]\). The law of total variance therefore gives
\[
\operatorname{Var}_\pi(VD)
=\mu^2\operatorname{Var}_\pi(Q)+\mathbb E_\pi[R_Q^2]
=\mu^2\operatorname{Var}_\pi(Q)+\mathbb E_\pi[\dot Q^2].
\]
The other two regressions give, identically,
\[
VQ-\nu D=\dot D
\]
and
\[
QD-(V-\Gamma)=\dot V,
\]
with each residual conditionally centered on its conditioning coordinate. Applying the same variance decomposition proves the remaining two identities.

## Verification
The standalone checker `verification.py` was replayed from its packaged path. It symbolically verifies the generator identity
\[
L\left(\frac{Q^2+D^2}{2}\right)=\mu Q^2-\nu D^2,
\]
the three residual identities underlying the conditional projections, and the exact source-parameter ratio
\[
\frac{119/1000}{1/10}=\frac{119}{100}.
\]
The stored output is `VERIFY_OK`.

No finite trajectory experiment is used as a proof. The conditional-expectation step uses invariance against arbitrary one-coordinate test functions, and the fluctuation identities use exact \(L^2\) orthogonality.

## Relationship to prior work
Gissinger's original paper introduces the three-mode quadratic model, analyzes its fixed points and bifurcation regimes, and numerically studies chaotic reversals and crisis-induced intermittency. The public arXiv text gives the exact equations and the parameter set used for the reversal attractor. Targeted document-wide searches did not locate invariant-measure, time-average, mean-square, or energy-balance statements matching the theorem above.

A later fractional-order study treats the same geomagnetic-field model through existence and uniqueness, equilibrium stability, Lyapunov spectra, fractional-order chaotic dynamics, and control. Its accessible abstract does not state a stationary conditional regression, an exact RMS locking law, or the three variance defects; the complete article was not used to make a whole-document noncoverage claim.

Targeted semantic searches for the exact model, stationary moments, conditional expectations, the \(Q\)-to-\(D\) RMS ratio, and time-average energy balance returned no same-object result implying the theorem. The closest indexed results concern different vector fields such as the Rikitake dynamo, Rössler, Genesio, Rabinovich--Fabrikant, and several newer quadratic flows. Those analogies do not imply the Gissinger identities because their generators and mode couplings differ.

## Limitations
The result is a stationary constraint, not an existence or uniqueness theorem for a chaotic invariant measure. It does not determine reversal frequencies, residence-time distributions, Lyapunov exponents, or basin geometry.

The RMS formula concerns compact stationary states and should not be read as a pointwise amplitude relation along transients. The three variance defects measure mean-square coordinate speeds but do not by themselves classify all equality cases separately.

Literature indexing is not exhaustive. An equivalent identity could exist in unindexed or differently notated work on low-order geodynamo models. The later fractional-order article was compared at abstract level only, so it remains a specific access-limited residual risk rather than evidence of whole-document noncoverage.

## References
1. C. Gissinger, “A new deterministic model for chaotic reversals,” arXiv:1109.6569v1, first public submission 29 September 2011; later published in *The European Physical Journal B* 85, 137 (2012), DOI 10.1140/epjb/e2012-20799-5.
2. A. Al-khedhairi, A. E. Matouk, and I. Khan, “Chaotic dynamics and chaos control for the fractional-order geomagnetic field model,” *Chaos, Solitons & Fractals* 128, 390–401 (2019), DOI 10.1016/j.chaos.2019.07.019.
