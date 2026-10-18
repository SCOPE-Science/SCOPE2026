# Mathematical review

## Correctness
**PASS.** For one uniform permutation, differentiating the normalized cycle-weighted Ewens measure at its uniform parameter gives covariance with cycle count. The precise insertion step partitions sites into those forcing a record, preventing it and leaving it unchanged. Differentiation cancels the inhomogeneous terms; the finite product gives the exact positionwise formula. Positivity, variance normalization, and terminal-position asymptotics follow without uncontrolled approximations. `verify.py` independently executes 1,720 exact assertions, including every permutation of each size from two through nine. These experiments corroborate but do not replace the proof.

## Originality
**PASS on inspected evidence, with residual priority risk.** Kabluchko–Marynych (2021) establish the well-known marginal records/Stirling relation, not this same-permutation covariance. Gnedin (2007) explains that record-weighted and cycle-weighted Ewens distributions are linked by a bijection, which cannot directly identify joint statistics on the original permutation. Dubach (2025) gives marginal record asymptotics, not the finite cross moments. The closest published inversion–cycle covariance formula concerns different indicators and cannot imply the prefix-maximality covariance without further calculation. An equivalent historical joint generating-function formula could exist; its absence is not proved. No independence or external validation is claimed.

## Value
**PASS.** The exact local/global dependence of two equally distributed yet different canonical permutation statistics is a motivated natural invariant. Every record position has positive or zero cycle covariance; the whole dependence is asymptotically concentrated at the last position, and the correlation decays at an explicit scale. These statements explain rather than merely re-label a classical marginal law.

## Limitations and relevant sources
The proof applies only to uniformly random permutations. The supporting source first appeared in May 2021. Closest inspected papers: Kabluchko–Marynych, arXiv:2105.11365; Gnedin, *Coherent random permutations with record statistics* (2007); Dubach, *A geometric approach to conjugation-invariant random permutations* (2025). Independent scholarly priority assessment has not been performed.

Self-review: passed. Independent audit: not yet performed.
