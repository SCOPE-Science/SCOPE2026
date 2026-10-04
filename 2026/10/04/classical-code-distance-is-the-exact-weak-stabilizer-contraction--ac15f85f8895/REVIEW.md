# Same-model review

## Correctness
PASS. The critical source lemma was read in full: a weak measurement of stabilizer \(S\) multiplies the isotypical component \(W_g^{\mathbb C}\) by \(\zeta^{\sigma_S(g)}\). The arbitrary schedule is diagonal in the same orthogonal decomposition, so its eigenvalue is the product of the elementary factors, exactly \(\zeta^{\operatorname{wt}(u^{\mathsf T}G)}\). Full row rank identifies those words with a binary linear \([L,r]\) code, and the largest nontrivial eigenvalue is therefore \(\zeta^{d(C_G)}\). Rank deficiency correctly yields an untouched nontrivial sector. The bundled checker confirms endpoint and \(r=3\) finite examples, but the general proof does not depend on enumeration.

Risk: this is an exact statement for the measurement superoperator and its Hilbert--Schmidt decomposition, not for the complete interleaved open-system evolution.

## Originality
PASS. The closest literature was compared at the implication level. Dominy et al. provide the weak-channel character formula and analyze only the full stabilizer group and a minimal generating set. Ashikhmin, Lai, and Brun use classical linear codes to design redundant stabilizer measurements for correction of classical syndrome-bit errors. Ouyang uses classical code distance to make projective measurements robust to corrupted classical outcomes. None of the inspected full texts states the exact weak nonselective spectrum \(\zeta^{\operatorname{wt}(u^{\mathsf T}G)}\) for arbitrary coded schedules or the resulting equality between worst-sector contraction exponent and binary minimum distance.

The underlying syndrome-measurement code construction and the classical \([4,3,2]\) parameter are explicitly treated as prior work. Residual risk remains that a differently phrased or unindexed source already observes the same weak-channel correspondence.

## Value
PASS. The anchor work leaves a natural resource gap between a cheap generator-only schedule and an exponentially larger full-group schedule. The theorem gives a complete design principle at fixed elementary-measurement count: use a largest-distance binary linear code. It also yields a minimal intermediate gain with immediate interpretation, since for \(r=3\) one additional distinct stabilizer changes the worst factor from \(\zeta\) to \(\zeta^2\). This is a motivated structural result rather than an arbitrary code-table lookup.

Limitations: measurement strength is common across observables; hardware-weighted cost is not modeled; and full dynamical Zeno bounds for arbitrary schedules are not claimed.

Same-model review: passed. Independent audit: not yet performed.
