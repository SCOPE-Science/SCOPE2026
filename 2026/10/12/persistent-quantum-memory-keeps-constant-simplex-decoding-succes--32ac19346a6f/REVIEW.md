# Self-review

## Correctness
PASS. The proof starts from the exact published \(B=1\) success formula, derives the modulus and phase asymptotics with the correct \(2^{k-1}\) and \(2^{k/2}\) scalings, and independently applies the source's QC Fano branch at \(Q=2k\). The fully random endpoint \(p=1/2\) is evaluated exactly. Finite computations only corroborate the analytic argument.

## Originality
PASS. The decisive source comparison is arXiv:2610.03659v1 itself: it proves reliable decoding only for fixed \(p<1/16\) with a growing number of register pairs, while its exact \(B=1\) formula is used for finite-size plots at small error rates and is not converted into the full \(p<1/2\) asymptotic separation. Five published-result semantic searches, formula-alias web searches, and the current/prior own ledgers found no implication-equivalent statement. The older quantum-data-gathering framework is broader in architecture but does not imply this noisy simplex asymptotic.

## Value
PASS. The finding delineates a meaningful robustness regime distinct from reliable decoding: one persistent-memory pair keeps a strictly positive exact-message probability for every nontrivial BSC, while all same-resource classical-memory QC receivers vanish. The explicit limiting curve and its quadratic collapse at \(p=1/2\) quantify the boundary.

## Closest literature and limitations
The closest literature is the anchor itself, followed by the sequential coherent-discrimination framework of Blume-Kohout, Croke, and Zwolak. This result is not a decoder optimality theorem and does not extend the source's success-tending-to-one theorem beyond \(p<1/16\). Very recent or differently phrased unindexed work remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
