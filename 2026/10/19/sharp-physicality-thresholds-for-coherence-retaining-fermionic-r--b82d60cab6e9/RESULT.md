# Sharp physicality thresholds for coherence-retaining fermionic reservoir resets

## Finding

Let one distinguished fermionic mode be coupled to an arbitrary nonzero bath one-particle Hilbert space \(\mathcal H_E\). For any prescribed bath covariance \(0\le B\le I_E\), define the coherence-retaining block reset
\[
\mathcal R_{B,\eta}\!\left(\begin{bmatrix}p&z\\z^*&E\end{bmatrix}\right)
=\begin{bmatrix}p&\eta z\\\eta z^*&B\end{bmatrix},\qquad 0\le\eta\le1.
\]
The input is an arbitrary gauge-invariant fermionic one-particle covariance \(0\le\Gamma\le I\). The reset preserves that physical covariance cone **for every admissible input** if and only if
\[
\boxed{\eta^2\le m(B):=\min\{\inf\sigma(B),\,1-\sup\sigma(B)\}.}
\]
Both sides are sharp, including when a spectral endpoint is not an eigenvalue. If the reference covariance has an exactly empty or filled bath mode (or merely has a spectral edge at occupation zero or one), global admissibility requires \(\eta=0\).

For a bounded bath Hamiltonian with lowest and highest one-particle energies \(\omega_-\) and \(\omega_+\), a thermal reset target \(B=(I+\exp[\beta(H_E-\mu I)])^{-1}\) with \(\beta>0\) gives the explicit sharp envelope
\[
\boxed{\eta_{\max}^2=
\frac{1}{1+\exp\{\beta\max(\omega_+-\mu,\,\mu-\omega_-)\}}.}
\]
For a symmetric tight-binding band \([-2J,2J]\), this becomes
\[
\eta_{\max}=\bigl(1+\exp[\beta(2J+|\mu|)]\bigr)^{-1/2}.
\]
At \(\beta J=3\) and \(\mu=0\), the universal covariance-admissibility ceiling is approximately \(0.04972547794\), not the entire nominal control interval. This is a **uniform-in-input** statement; particular fixed points or trajectories may remain admissible above it.

There are two further exact distinctions. If \(0<B<I\) with bounded inverses and a particular input has \(0<p<1\) and \(z\ne0\), then its output is admissible exactly when
\[
\eta^2\le\min\left\{
\frac{p}{zB^{-1}z^*},\,
\frac{1-p}{z(I-B)^{-1}z^*}
\right\}.
\]
For one bath mode of target occupation \(0<c<1\), the corresponding reset of all one-particle moments can be implemented by a **local bath qubit channel** which fixes the bath occupation and attenuates its coherence by \(\eta\) if and only if \(\eta^2\le c(1-c)\). Thus physical covariance preservation and local completely positive implementation have different sharp thresholds: at \(c=1/2\), they are respectively \(1/\sqrt2\) and \(1/2\).

## Assumptions and scope

A one-particle covariance on \(\mathbb C\oplus\mathcal H_E\) is called fermionically admissible when it is a self-adjoint positive contraction. These and only these operators define gauge-invariant quasi-free fermionic states on the associated canonical anticommutation relation algebra. The bath can be any nonzero complex Hilbert space, finite or infinite dimensional. \(B\) is bounded and satisfies \(0\le B\le I\). The interpolation parameter is real in \([0,1]\). A block \(z:\mathcal H_E\to\mathbb C\) is a bounded row operator. The thermal corollary assumes a bounded self-adjoint \(H_E\), \(\beta>0\), and chemical potential \(\mu\in\mathbb R\). The local-channel statement concerns exactly one fermionic bath mode, and only a bath-local, phase-covariant qubit channel of the stated occupation-reset and coherence-attenuation form.

## Proof

**1. Universal upper bound on input correlations.** For any \(0\le\Gamma\le I\), functional calculus gives \(\Gamma-\Gamma^2\ge0\). Its distinguished-mode diagonal entry is \(p-p^2-zz^*\ge0\), hence \(\|z\|^2\le p(1-p)\). In particular \(z=0\) if \(p\in\{0,1\}\).

**2. Sufficiency.** For \(0<p<1\), the two Schur-complement tests for \(0\le\mathcal R_{B,\eta}(\Gamma)\le I\) are
\[
B-\frac{\eta^2}{p}z^*z\ge0,
\qquad
I-B-\frac{\eta^2}{1-p}z^*z\ge0.
\]
Because \(z^*z\le p(1-p)I\), these follow from \(B\ge\eta^2 I\) and \(I-B\ge\eta^2 I\). The cases \(p=0,1\) follow from \(z=0\). Thus \(\eta^2\le m(B)\) is sufficient without assumptions on the discarded input bath block \(E\).

**3. Necessity and spectral boundaries.** For a bath unit vector \(v\) and \(p\in(0,1)\), take the physical rank-one projector onto \(\sqrt p\oplus\sqrt{1-p}\,v\). Its cross block is \(z=\sqrt{p(1-p)}\langle v,\cdot\rangle\). The lower Schur complement of the output requires \(\langle v,Bv\rangle\ge\eta^2(1-p)\), and the upper complement requires \(1-\langle v,Bv\rangle\ge\eta^2p\). If \(\eta^2>\inf\sigma(B)\), choose \(v\) with expectation below \(\eta^2\) and then \(p>0\) sufficiently small to violate the first inequality. If \(\eta^2>1-\sup\sigma(B)\), choose \(v\) near the top spectral edge and \(p<1\) sufficiently close to one to violate the second. Approximate spectral vectors suffice for infinite baths. Hence the bound is necessary and sharp.

**4. Individual-input criterion.** With bounded positive inverses of \(B\) and \(I-B\), Schur complementing first the two fixed environment blocks gives the scalar conditions \(p-\eta^2zB^{-1}z^*\ge0\) and \(1-p-\eta^2z(I-B)^{-1}z^*\ge0\). Dividing by the positive quadratic forms proves the claimed exact statewise test. When \(z=0\), every \(\eta\) is statewise admissible. The singular-target case is governed instead by the operator Schur tests in step 2, including their range conditions; the inverse formula is not asserted there.

**5. Thermal spectral envelope.** The Fermi occupation \(f_{\beta,\mu}(\omega)=(1+e^{\beta(\omega-\mu)})^{-1}\) strictly decreases in energy for positive \(\beta\). Functional calculus yields \(\inf\sigma(B)=f_{\beta,\mu}(\omega_+)\) and \(1-\sup\sigma(B)=1-f_{\beta,\mu}(\omega_-)\). Taking the smaller gives the displayed formula. For the semi-infinite nearest-neighbor tight-binding bath \(\sigma(H_E)=[-2J,2J]\). For a length-\(d\) open chain the exact half-bandwidth is instead \(2J\cos(\pi/(d+1))\), and the stated limit follows as \(d\to\infty\).

**6. Distinct local quantum-channel threshold.** For one bath qubit, let \(\Lambda_{c,\eta}\) act on an arbitrary qubit density operator by
\[
\Lambda_{c,\eta}\!\left(\begin{bmatrix}a&w\\\overline w&b\end{bmatrix}\right)
=\begin{bmatrix}(1-c)(a+b)&\eta w\\\eta\overline w&c(a+b)\end{bmatrix}.
\]
Its unnormalized Choi matrix, ordered by output and input computational bits, is
\[
J=\begin{bmatrix}1-c&0&0&\eta\\0&1-c&0&0\\0&0&c&0\\\eta&0&0&c\end{bmatrix}.
\]
The output partial trace of \(J\) is the identity, so trace preservation is automatic. Complete positivity is equivalent to positivity of its only nontrivial \(2\times2\) principal block, i.e. \(\eta^2\le c(1-c)\). This proves necessity and provides an explicit channel whenever the inequality holds. The tensor-product map that is identity on the distinguished mode and \(\Lambda_{c,\eta}\) on the bath preserves the system occupation, fixes the bath occupation at \(c\), and scales the bilinear cross expectation by \(\eta\). This is an implementation of the **second-moment action**, not a claim that the many-body output is always Gaussian or that a many-mode implementation follows by tensoring these maps.

## Verification

Run `python verification/check.py` after installing `verification/requirements.txt`. The deterministic checker independently assembles random complex admissible one-particle covariances and bath targets, verifies the sharp universal interior and boundary, constructs rank-one counterexamples above each bound, verifies the individual-input Schur conditions, computes eigenvalues of the one-mode Choi matrix, and tests thermal edge formulas. It passed 2028 assertions using NumPy. These finite tests support but do not replace the analytic proofs in steps 1–6. The physicality threshold concerns all possible input covariances, not just states produced by a particular reset trajectory.

## Relationship to prior work

Kumar, Lazarides, and Ala-Nissila (arXiv:2604.17152v1, Sec. II.3, equations (14)–(15)) define this precise coherence-retaining SPDM reset, analyze fixed-point coherence/heat tradeoffs, and allow nominal \(0\le\eta\le1\). Those equations are **prior work**; the present finding addresses the separate sharp question of when the covariance update preserves fermionic one-particle physicality for all inputs and what the thermal spectral edges imply. Vieira, Lazarides, and Ala-Nissila (arXiv:2012.04083v1, Sec. III) introduced the general class of elementwise SPDM reset rules, including the coherence-preserving endpoint, but did not give this spectral necessary-and-sufficient criterion. Kumar, Lazarides, and Ala-Nissila (arXiv:2603.15554v1, Sec. II.2 and Sec. IV) develop a CP-safe continuous-time embedding for correlation-erasing resets; that construction is not the finite-step coherence-retaining map analyzed here. The proof uses standard Schur complements and the usual qubit Choi criterion, neither of which is claimed novel in isolation.

## Limitations

Global covariance preservation is weaker than the existence of a completely positive quantum channel realizing the complete many-body Gaussian dynamics. The explicit bath-local channel construction is only for one bath mode and implements second moments; it does not establish the physical implementation of a many-mode coherence-retaining reset. Conversely, failure of the uniform bound does **not** imply that any specific fixed-point state, restricted initial-state family, or entire simulated trajectory is nonphysical. The theorem does not reassess any paper's numerical fixed-point calculations. The spectral envelope requires a bounded bath Hamiltonian, and the finite-chain endpoint must not be confused with its infinite-chain limit. The checker is finite-dimensional and numerical; the Hilbert-space extension is analytic.

## References

1. J. Kumar, A. Lazarides, and T. Ala-Nissila, *Thermodynamics of Coherence-Selective Quantum Reset Protocols*, arXiv:2604.17152v1, first posted 18 April 2026. https://arxiv.org/html/2604.17152v1
2. J. P. P. Vieira, A. Lazarides, and T. Ala-Nissila, *Quadratic Models for Engineered Control of Open Quantum Systems*, arXiv:2012.04083v1, first posted 7 December 2020. https://arxiv.org/html/2012.04083v1
3. J. Kumar, A. Lazarides, and T. Ala-Nissila, *Interaction-Enabled Hartree Fixed Points in Fermionic Resetting Dynamics*, arXiv:2603.15554v1, first posted 16 March 2026. https://arxiv.org/html/2603.15554v1
4. E. Greplová and G. Giedke, *Degradability of Fermionic Gaussian Channels*, Phys. Rev. Lett. 121, 200501 (2018), arXiv:1604.01954. https://arxiv.org/abs/1604.01954
