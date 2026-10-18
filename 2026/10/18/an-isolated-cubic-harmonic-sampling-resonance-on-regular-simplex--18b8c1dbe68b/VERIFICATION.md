---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification scope

A complete symbolic argument establishes the cubic Gegenbauer Gram decomposition for every integer \(m\ge5\). The three candidate eigenvalues were additionally compared by exact polynomial simplification against the adjacency-algebra expressions, giving three zero rational-function differences. The nonnegative eigenspace multiplicities sum to \(\binom m2\), and the zero criterion follows from the factor \((m-8)^2\) under the stated integer-domain hypothesis.

For reproducibility, run `python check_cubic_simplex.py` using Python 3 standard library. The script builds the whole normalized zonal matrix with exact rational entries, checks one nonzero vector from each of the three invariant spaces, the trace, the singularity criterion, and the \(m=8\) projection identity. The following tested list passed: \(m\in\{5,6,\ldots,19,24,28,32,40\}\), 19 exact cases. The script is finite corroboration only; it cannot prove the all-integer claim or historical novelty.

The full 1977 primary paper was inaccessible for a direct content comparison. Scientific originality remains subject to independent expert evaluation. No independent audit was performed.
