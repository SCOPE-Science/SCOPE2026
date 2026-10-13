# Review

## Correctness
PASS. The claim is reduced to two exact identities from the source: utility is \(\frac12(1+\lambda_zC+\lambda_xV)\), and fidelity-line privacy is \(-\log(1-\lambda_x^2V)\). The entropy lower bound is Shannon's exact grouping identity applied to the two Pauli sign classes for the \(x\)-coordinate. The two-gate \(I/Z\) distribution simultaneously saturates that lower bound and maximizes the common-direction contraction \(\lambda_z\), proving both feasibility and optimality. Endpoints \(t=0\) and \(t=1\), the antipodal case \(C=0\), and the source-optimal specialization were checked separately.

## Originality
PASS. The closest older result is Bouda--Ziman's Shannon-key optimization for private qubit channels. Their perfect-private theorem already contains the one-bit endpoint, and their approximate optimization treats the whole Bloch sphere. It does not imply the pair-specific utility-constrained formula \(h_2((1-t)/2)\). The 2026 source explicitly allows key-randomness budgets but does not state or optimize Shannon entropy. Focused searches for Pauli key entropy, binary pure-state utility/privacy tradeoffs, phase-damping entropy, and approximate quantum encryption found no implication-equivalent result. Residual risk remains because the anchor is recent and the exact three-way frontier could exist under different terminology.

## Value
PASS. The source identifies key-randomness budgets as a natural hardware restriction but leaves that resource unsolved. The finding supplies a complete closed-form resource frontier in the paper's principal solvable pure-binary regime, shows that two Pauli gates suffice at every feasible point, and quantifies the exact randomness cost of moving along the privacy frontier. This is more than a parameter substitution because the lower bound is global over all four-Pauli distributions and distinguishes Shannon randomness from the source's divergence optimum.

## Closest literature and limitations
The one-bit perfect-privacy endpoint agrees with Bouda and Ziman (2007), so that endpoint is not claimed as new. Ambainis and Smith (2004) concern approximate randomization of arbitrary quantum messages rather than a fixed binary ensemble with an overlap-utility constraint. The result does not cover mixed inputs, general \(\alpha\)-\(z\) parameters, non-Pauli channels, or fixed-length one-shot key length.

Self-review: passed. Independent audit: not yet performed.
