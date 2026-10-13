# Review of A target-safe spectral-intersection upper certificate under known-readout query access

## Correctness
**PASS.** The spectral-support implications are exact in finite dimension. Strict positive support is used exactly for competitors that would defeat the target on a tie; nonnegative support is enough against competitors that lose a tie to the target. Their intersection therefore guarantees the target label. Orthogonal projection then gives a witness whose fidelity with the original input is exactly \(\sqrt{p_k}\), yielding the stated upper bound. No numerical experiment is used as proof.

## Originality
**PASS.** The current source explicitly notes that a pairwise positive-gap state need not be predicted as the named competitor in a multiclass classifier and states only an untargeted upper certificate. The closest inspected broader work treats binary quantum classifiers. Target-safe spectral intersections, equivalent score-gap formulations, and implication comparisons were searched; no checked source states the all-competitor, tie-aware projector certificate. Residual risk remains because the construction is elementary once the missing multiclass condition is recognized, and an unindexed independent observation may exist.

## Value
**PASS.** The revised source's threat model includes targeted misclassification, while its usable spectral upper bound is untargeted. The result supplies a conservative class-specific certificate under the same known-readout projector-access assumption and makes the tie rule explicit. This is operationally meaningful for target-specific robustness auditing. The certificate can be vacuous and is not claimed optimal.

## Closest literature and limitations
Guan and Huang, arXiv:2609.11637v2, provide the pairwise gap-operator construction and untargeted projector upper bound. Dowling, West, Southwell et al., DOI 10.1038/s41534-025-01129-3, provide broader adversarial-robustness guarantees in a binary classifier setting. Neither inspected source implies the multiclass all-competitor spectral intersection. The new theorem assumes pure states, unitary hidden evolution, an exact known POVM, fixed tie priority, and availability of derived binary projector readouts; it does not claim completeness or optimality.

Self-review: passed. Independent audit: not yet performed.
