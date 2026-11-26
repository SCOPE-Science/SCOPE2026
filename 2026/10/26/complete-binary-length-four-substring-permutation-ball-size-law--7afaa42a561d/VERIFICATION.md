---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the first-difference partition: when the first changed location is i≤n−3, all changes fit in [i,i+3], and conservation of the number of ones lets that window realize the same output, regardless of the original window. For later first changes, the last-triple rearrangements include the unchanged word and are all realized by fixing the preceding bit of the final window. This counts distinct outputs. Checking the two appended bits at each complement-paired suffix gives the matrix and terminal vector and exactly two initial triples per state. Independently verified the six coefficient rational functions by solving for each z-degree of (I−sA)^−1 b recursively on the zero-weight graph, rather than using the supplied determinant certificate. Zero-deficit paths reaching a permitted terminal triple consist exactly of the alternating cycle or the four rotations of 0011, giving six distinct words even at n=4. Independently enumerated overlapping local strings to confirm all rational moments and covariances, including the zero covariance at shift three and both terminal covariances; summation gives the n=4 variance 159/64 and (119n−319)/64 thereafter. The local process is three-dependent, the omitted gaps have total variance O(n^(2/3)), the retained independent centered blocks are uniformly o(sqrt(n)), and the positive long-run variance is 119/64; Lindeberg and the negligible terminal term give the claimed normalization. Replay: python3 /workspace/review-checks/binary_four.py (SymPy for the rational identities). Frozen programs and their recorded outputs were inspected, not executed.

## originality

PASS

Pass is for the evaluated four-window population law, extremal and near-extremal populations, exact variance and Gaussian limit. The per-center first-difference identity and uniform mean are directly prior. The strongest earlier catalogue analogue computes an entire distribution for a three-window burst, not four; the same-date nonbinary extremal result does not include binary length four. A later record directly matches the binary maximum and six maximizers, not the full population law. This is a literature- and catalogue-bounded conclusion.

## value

PASS

For a standard single-window permutation error model, a population histogram answers a different question than a pointwise size or a mean: it determines the exact count of centers at every ambiguity level for every length. The six periodic worst cases, polynomial counts immediately below them, and exact typical-case fluctuation scale are useful finite and asymptotic benchmarks. This value does not depend on a new mean, a coding-rate claim, or a wider alphabet generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
