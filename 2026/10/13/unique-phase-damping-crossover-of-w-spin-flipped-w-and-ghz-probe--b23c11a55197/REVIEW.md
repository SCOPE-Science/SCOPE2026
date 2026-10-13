# Scientific review

## Correctness — PASS
The dephased state is explicitly reconstructed from Hamming distances within two disjoint weight sectors, and its commuting uniform/orthogonal blocks yield the SLD QFI without hidden basis truncation. A differentiated exact QFI ratio has a strictly negative derivative for all \(n\ge3\) and \(0<z\le1\), forcing a unique interior crossing; endpoint values are handled separately. A uniform-for-fixed-parameter expansion and monotone bracketing prove the sharp \(np_c(n)\to1/2\) limit. The independent computational-basis verifier returns `VERIFY_OK 207`. Numerical checks are not offered as an infinite proof.

## Originality — PASS, residual priority risk
Sudha et al. (arXiv:2601.23043, §III.2) give the same channel and numerical probe comparisons but no all-size formula or unique analytic GHZ/W–spin-flipped-W longitudinal crossover. Li and Ren (Phys. Rev. A 107, 012403, §III.C) give noisy optimized-axis QFI in the three- and four-qubit examples, which differs logically and numerically from fixed-axis \(J_z\) QFI; their noiseless state analysis and prior qualitative robustness are credited. Ren and Li (Results in Physics 53, 106954) study loss of qubits and dephased **reduced** states; Ma et al. (Phys. Rev. A 84, 022302) treat GHZ rather than the W–spin-flipped-W crossover. Searched mathematical research records and published-literature variants revealed no equivalent theorem. The risk of an unindexed or implicit earlier formula remains; search failure is not a proof of priority.

## Value — PASS
The source explicitly studies this probe comparison under phase damping, while the three- and four-qubit literature reports axis-optimized values that cannot answer longitudinal sensing. An exact, strict, all-size crossover provides a reproducible architecture-choice boundary, and the \(1/n\) threshold identifies the relevant weak-noise scaling regime in which the QFI remains of quadratic order. This is a constrained physical decision, not a merely rephrased normalized quantity.

## Boundary and limitations
All statements hold only for the two specified probe families, independent phase damping, and \(J_z\) encoding. In particular, the theorem does not compare globally optimized collective-axis QFI, which earlier literature explicitly studies; and at complete dephasing both probes have zero directional QFI. Priority risk persists for broader unindexed literature. No independent review has been conducted.

Self-review: passed. Independent audit: not yet performed.
