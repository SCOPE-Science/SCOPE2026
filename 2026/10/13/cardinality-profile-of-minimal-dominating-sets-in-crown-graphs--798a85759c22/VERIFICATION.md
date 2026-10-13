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

The all-\(n\) proof is the symbolic case analysis in `RESULT.md`. The standalone checker is a finite, independent consistency test: for each \(3\le n\le9\), it enumerates all nonempty vertex subsets, tests domination directly from the edge relation, tests inclusion-minimality by deleting each selected vertex, and compares the resulting family with the claimed structural criterion and coefficient formula.

Replay command:

`python verification/crown_minimal_domination_check.py`

Observed output:

`VERIFY_OK n_range=3..9 subset_checks=349497 minimal_checks=1568 classification_checks=349497 coefficient_checks=19 enumerator=n*x^2+6*C(n,4)*x^4+2*x^n upper_domination=n oeis_total_match=A289121 max_order=18`

The finite range does not certify the theorem for larger \(n\); that scope is supplied by the proof. The database comparison at \(x=1\) confirms only the aggregate total and is not a novelty certificate.
