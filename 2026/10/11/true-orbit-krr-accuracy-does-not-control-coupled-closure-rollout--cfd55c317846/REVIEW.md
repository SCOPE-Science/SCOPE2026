# Review: True-orbit KRR accuracy does not control coupled closure rollout

## Correctness
PASS. The source defines \(\widetilde{{\Phi}}_y:\mathbb R^{{d_x+d_y}}\to\mathbb R^{{d_y}}\), so its displayed powers are not type-defined for \(d_x>0\). Under the explicit teacher-forced repair, the Gaussian-KRR construction is self-contained: true centers are separated by \(h\), off-diagonal Gram entries are super-polynomially small, the KRR normal equations give \(O(h^5)\) true-center error, and the first coupled perturbation is placed exactly at the kernel bandwidth scale. This forces \(\widehat y_2\to e^{-1}\) and hence a resolved two-step error asymptotic to \((1-e^{-1})h/2\), not \(O(h^2)\).

## Originality
PASS. Searches by exact source identifier, theorem/equation number, KRR rollout stability, teacher-forced versus coupled error, Gaussian-bandwidth instability, and correction/erratum aliases found no published statement equivalent to this source-specific result. The closest broader literature establishes that autonomous rollout bounds require stability information; it does not imply the explicit RBF construction or diagnose equations (8) and (29) of the focal paper. Current and prior research records were checked for the source identifier and claim aliases with no overlap.

## Value
PASS. Theorem 2.1 is the paper's theoretical explanation for how KRR, interpolation, and resolved-solver errors combine. The finding isolates a substantive missing interface between teacher-forced approximation and autonomous closure deployment, gives a concrete standard-kernel mechanism rather than a purely formal objection, and identifies a direct repair: control the actual coupled unresolved error or impose off-trajectory stability.

## Closest literature and limitations
Li--Wan give general rollout bounds under domain-wide contraction/Lipschitz assumptions and explicitly distinguish one-step accuracy from autonomous rollout stability. Song--Huang--Harlim use dynamics-aware rollout validation for KRR. Neither contains the focal theorem comparison or the narrow-band Gaussian counterexample. The claim does not exclude a corrected theorem with a stronger coupled-rollout hypothesis, and it does not characterize the weakest sufficient stability condition.

Same-model review: passed. Independent audit: not yet performed.
