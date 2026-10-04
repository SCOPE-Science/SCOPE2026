# The post-channel global relative-entropy optimum is attained by doing nothing
## Finding
For the post-channel optimization written in arXiv:2605.16463v1, if the allowed post-processing class is trace-preserving LOCC after the noisy channel, then the maximum global relative entropy of entanglement is attained by the identity operation. For the paper's single-qubit depolarizing channel acting on one half of each Bell pair, with \(0<p<1/2\), the channel output has Bell weights \((1-p,p/3,p/3,p/3)\), and therefore
\[
\sup_{\Lambda_{\mathrm{LOCC}}} E_R\!\left(\Lambda_{\mathrm{LOCC}}(\rho_p^{\otimes n})\right)
=E_R(\rho_p^{\otimes n})
=n\bigl[1-H_2(p)\bigr].
\]
Consequently, an upper bound of the form \(nE_R(\rho_p)e^{-\kappa n}\) with \(\kappa>0\) cannot bound that same supremum. The exponentially small post-distillation ceiling asserted in Appendix C of arXiv:2605.16463v1 therefore does not follow for the displayed LOCC-after-channel optimization; the reported DEJMPS global value is a value for a particular protocol, not the optimum over all trace-preserving post-channel LOCC maps.

## Assumptions and scope
The channel is the paper's qubit Pauli depolarizing map
\[
\Phi_p(\tau)=(1-p)\tau+\frac{p}{3}\bigl(X\tau X+Y\tau Y+Z\tau Z\bigr),
\]
applied to the transmitted half of a Bell pair. The statement concerns the global relative entropy of entanglement \(E_R\), not a conditional successful-branch entanglement, a rate normalized by consumed input copies, or a separately constrained optimization requiring a prescribed output fidelity or a strict reduction in pair number. The post-processing class is exactly trace-preserving LOCC as used in the displayed monotonicity and supremum arguments of the source. If a narrower operational class was intended, it must be specified separately; the equality proved here is for the optimization actually written.

## Proof
Let \(\lvert\Phi^+\rangle\) be a Bell state and define
\[
\rho_p=(I\otimes\Phi_p)\!\left(\lvert\Phi^+\rangle\!\langle\Phi^+\rvert\right).
\]
The four states obtained by applying \(I,X,Y,Z\) to one half of \(\lvert\Phi^+\rangle\) are the four Bell states up to irrelevant phases. Hence \(\rho_p\) is Bell diagonal with eigenvalue vector
\[
\lambda(\rho_p)=\left(1-p,\frac p3,\frac p3,\frac p3\right).
\]
For \(0<p<1/2\), the largest Bell weight is \(1-p>1/2\). The closed formula for Bell-diagonal relative entropy of entanglement gives
\[
E_R(\rho_p)=1-H_2(1-p)=1-H_2(p),
\]
with base-two entropy \(H_2\). This is positive on \(0<p<1/2\).

Relative entropy of entanglement is additive when one tensor factor is Bell diagonal. Repeated application therefore gives
\[
E_R(\rho_p^{\otimes n})=nE_R(\rho_p)=n\bigl[1-H_2(p)\bigr].
\]
For every trace-preserving LOCC map \(\Lambda_{\mathrm{LOCC}}\), monotonicity gives
\[
E_R\!\left(\Lambda_{\mathrm{LOCC}}(\rho_p^{\otimes n})\right)\le E_R(\rho_p^{\otimes n}).
\]
The identity map is itself trace-preserving LOCC, so equality is attainable. Thus
\[
\sup_{\Lambda_{\mathrm{LOCC}}}E_R\!\left(\Lambda_{\mathrm{LOCC}}(\rho_p^{\otimes n})\right)=n\bigl[1-H_2(p)\bigr].
\]
If \(\kappa>0\) and \(n\ge1\), then \(e^{-\kappa n}<1\). Since \(E_R(\rho_p)>0\),
\[
nE_R(\rho_p)e^{-\kappa n}<nE_R(\rho_p),
\]
so the former cannot be an upper bound on the displayed supremum.

At the paper's numerical value \(p=0.2\), the exact single-pair value is \(E_R(\rho_{0.2})=1-H_2(0.2)=0.2780719051126377\) bits, and for four copies it is \(1.1122876204505508\) bits. These numbers are not a prediction for a particular distillation protocol; they are the exact global-\(E_R\) optimum over trace-preserving LOCC because identity LOCC attains it.

## Verification
The accompanying `verify.py` reconstructs the Bell weights, evaluates \(1-H_2(p)\), checks the \(p=0.2\) numerical values, and verifies that multiplication by \(e^{-\kappa n}\) with positive \(\kappa\) makes the proposed ceiling strictly smaller than the identity-LOCC value. The substantive proof is analytic and does not depend on floating-point computation.

The source was checked at its full arXiv HTML, especially the definition of post-distillation, the global-\(E_R\) monotonicity discussion, and Appendix C's assertion that the supremum over post protocols is bounded by an exponentially decaying quantity. A modern full-text treatment of Bell-diagonal relative entropy of entanglement was also inspected; it gives the exact Bell-diagonal formula and the additivity property used above.

## Relationship to prior work
The Bell-diagonal formula and additivity are established results; they are not claimed here as new. The finding is their implication for the specific global post-distillation optimization asserted in arXiv:2605.16463v1. That preprint states that all post-channel LOCC outputs are bounded by the noisy state's global \(E_R\), but Appendix C then replaces the optimum by an exponentially smaller expression. Because identity LOCC is in the stated class, these two steps are incompatible whenever the noisy Bell-diagonal state remains entangled.

Searches of the published published-finding corpus corpus for the source identifier, the geometric-entropy claim, Bell-diagonal relative entropy, and the depolarizing-channel post-distillation bound did not locate a result making this correction. The closest retrieved quantum-information result concerned an unrelated Werner-state Bell-inequality threshold and does not imply the global-\(E_R\) optimization equality here.

## Limitations
This finding does not prove that every physically meaningful preprocessing strategy lacks an advantage over every carefully normalized distillation task. It shows that the particular global relative-entropy benchmark used for the all-post-distillation claim is not an exponentially decaying optimum when the optimization class includes ordinary trace-preserving LOCC. A repaired comparison could impose a target fidelity, output dimension, success criterion, rate normalization, or resource accounting that excludes identity; such a repaired optimization would require a new theorem and is not analyzed here.

## References
1. G. Lyu, W. Sun, Y. Jin, H. Nan, “Pre-Channel Entanglement Shaping Achieves Fundamental Superiority over Post-Distillation: A Geometric Entropy Perspective,” arXiv:2605.16463v1 (2026).
2. R. Rubboli, M. Tomamichel, “New additivity properties of the relative entropy of entanglement and its generalizations,” arXiv:2211.12804v3 (2024), especially Section 6.1 and Proposition 10.
3. V. Vedral, M. B. Plenio, M. A. Rippin, P. L. Knight, “Quantifying Entanglement,” Phys. Rev. Lett. 78, 2275–2279 (1997), arXiv:quant-ph/9702027.
