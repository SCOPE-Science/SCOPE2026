# Self-review

## Correctness
PASS. For every \(d\ge2\), the exact average-fidelity identity gives \(F_{\mathrm{avg}}=(dF_e+1)/(d+1)\). Every unitary channel has a pure Choi state with the same eigenvalue spectrum, while \(F_e=|\operatorname{Tr}U|^2/d^2\). The identity and a traceless root-of-unity unitary therefore supply an all-dimensional same-spectrum counterexample. The two common Choi normalizations were checked separately.

## Originality
PASS for the source-specific correction, not for the classical fidelity identity. Exact-title/DOI searches, Choi-spectrum/purity aliases, and broader literature searches did not locate a prior statement correcting Appendix B.4 in the same way. Nielsen 2002 is stronger background for the correct formula but does not subsume the 2026 source-specific diagnosis.

## Value
PASS. The disputed formula confuses target-relative fidelity with spectral purity. Under one standard normalization it assigns the same perfect value to every unitary channel, including maximally coherent errors relative to the identity target. Correcting that distinction is directly relevant to the manuscript's process-tomography and teleportation-fidelity workflow.

## Closest literature and limitations
Nielsen 2002 and the Horodecki relation supply the correct background theorem. The anchor itself states that theorem correctly in its main text and pseudocode, so the error is localized to Appendix B.4. The finding does not claim that the manuscript's numerical tables used the erroneous expression, and it does not address nonunitary targets or other uses of the Choi spectrum. No public erratum was located, but search incompleteness remains a residual risk.

Self-review: passed. Independent audit: not yet performed.
