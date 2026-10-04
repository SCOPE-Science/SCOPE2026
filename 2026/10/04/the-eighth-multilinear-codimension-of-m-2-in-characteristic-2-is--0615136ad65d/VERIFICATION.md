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

The proof reduces the claim to an exact finite rank calculation over \(\mathbb F_2\). `artifacts/verify_low_degree.py` reconstructs the full matrix-unit evaluation map for degrees \(1\) through \(7\) and returns quotient ranks \(1,2,6,23,90,340,1246\).

`artifacts/verify_rank8_forward.cpp` enumerates every one of the \(40320\) degree-eight multilinear words, groups them by first variable, and uses highest-set-bit Gaussian elimination. It returns rank \(4487\) and kernel dimension \(35833\).

`artifacts/verify_rank8_reverse.cpp` independently enumerates the same full column set in a reverse last-variable partition and uses lowest-set-bit pivots. It also returns rank \(4487\) and kernel dimension \(35833\).

These calculations are exhaustive and exact over \(\mathbb F_2\). The passage to an arbitrary infinite characteristic-two field is not inferred from testing examples: it follows because multilinearity reduces evaluations to matrix units and because the prime-field evaluation matrix has the same rank after scalar extension.

The originality assessment is literature-based and remains subject to the residual risks recorded in `AUDIT.json`.
