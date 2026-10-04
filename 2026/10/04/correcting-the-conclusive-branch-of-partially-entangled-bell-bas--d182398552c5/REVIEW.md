# Same-model review

## Correctness

**PASS.** The four measurement states are orthonormal, so their inverse basis transformation fixes the three-qubit decomposition uniquely. The corrected branch maps have singular values \(x/\sqrt2\) and \(y/\sqrt2\). A successful reversing Kraus operator must satisfy \(KD=cU\) and \(K^\dagger K\le I\), forcing \(|c|^2\le y^2/2\) per branch; an explicit filter attains equality. The source's displayed Eq. (9) pair fails Kraus completeness for interior \(y/x\).

## Originality

**PASS, narrowly scoped to the correction.** General conclusive-teleportation and measurement-reversal results already cover the least-singular-value principle and therefore support the repaired \(2y^2\) probability. They are not claimed as new. Targeted searches did not locate an erratum or paper identifying that arXiv:quant-ph/0010113v1's final displayed decomposition and POVM pair are internally inconsistent. The accepted claim is the source-specific diagnosis and complete repair.

## Value

**PASS.** The defect is not cosmetic: the probability printed by the source tends to \(1/2\) as the measurement basis becomes product, whereas the corrected faithful-teleportation probability must and does tend to zero. The source explicitly frames the measurement-entanglement choice as an optimization trade-off, so correcting the success law changes the quantitative resource curve on which that question depends.

Same-model review: passed. Independent audit: not yet performed.
