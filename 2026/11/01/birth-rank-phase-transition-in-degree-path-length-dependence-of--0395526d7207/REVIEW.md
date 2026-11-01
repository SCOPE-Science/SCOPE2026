# Self-review

**Correctness: PASS.** The independent parent-choice coupling gives an exact local covariance: forcing vertex \(t\) to attach to \(j\) changes the depth of the entire descendant subtree, whose conditional expected final size is \(n/t\). Summation, finite harmonic identities, and one reciprocal-square difference prove the covariance formula and single sign switch. Euler–Maclaurin-scale elementary expansions establish the \(\sqrt{n/\log n}\) boundary. The finite enumerations in `verify.py` independently check the formulas but do not assert infinite certification.

**Originality: PASS (qualified).** An earlier root-only identity is recovered at birth rank one, but root-only coverage does not imply the birth-rank-dependent transition or its location. Janson's inspected abstract concerns the degree-frequency process, not this mixed statistic. published-finding corpus searches for nonroot degree, total path length, and rank threshold found no direct equivalent in the returned summaries. Direct inspection of every older monograph and paywalled article was not possible; undetected equivalents are a residual priority risk.

**Mathematical value: PASS.** The birth-rank crossover is a natural qualitative distinction in random recursive-tree genealogies: the same local structural statistic changes the sign of its association with global path cost as the vertex ages. The nontrivial \(\sqrt{n/\log n}\) scale and exact finite-size formula make the statement useful for degree–depth dependence and age-profile analyses rather than being a mere isolated small-number calculation.

Independent coverage, broad universal tree models, and full joint laws are not claimed.

Self-review: passed. Independent audit: not yet performed.
