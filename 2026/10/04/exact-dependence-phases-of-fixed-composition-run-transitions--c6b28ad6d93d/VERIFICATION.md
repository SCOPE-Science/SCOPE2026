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
# Verification

The universal proof is analytic. The accompanying checker uses exact rational arithmetic and complete finite enumeration for a bounded replay range.

For every \(4\le N\le12\) and every nontrivial fixed composition, it enumerates all binary words, recomputes every transition-indicator mean and pair covariance, and checks the formulas for adjacent and disjoint pairs.

For every admissible composition through \(N=250\), it verifies the sign phase, the impossibility of zero disjoint covariance, the square-size characterization of adjacent independence, and the identity between the summed covariance field and the classical run-count variance.

Finite enumeration is not used as a proof for arbitrary \(N\). The all-\(N\) argument is the exact counting and divisibility proof in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK words_enumerated=8158 marginal_checks=501 adjacent_checks=438 disjoint_checks=1485 phase_checks=31122 nonzero_far_checks=31122 square_independence_checks=31122 variance_checks=31185`.
