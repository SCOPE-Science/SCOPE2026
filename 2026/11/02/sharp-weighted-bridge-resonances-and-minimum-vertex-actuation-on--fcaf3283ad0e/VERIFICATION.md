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

# Verification record

The analytic argument establishes the entire positive-real parameter theorem and the classification of all minimum vertex sets. The standalone `verify.py` reproduces 1,003 exact rational assertions with Python standard-library `fractions.Fraction`. It builds the actual weighted Laplacian, computes Kalman ranks, evaluates exact Dirichlet determinants and exhaustively compares the predicted list of minimum actuator sets against all subsets for eight small instances.

Executed check: `python3 verify.py` — `PASS: 1003 exact assertions`. The tests have finite scope and do not constitute an independent mathematical audit or a proof beyond the analytically treated domain. Full correctness for all positive real weights rests on the stated PBH, Dirichlet sine-mode and algebraic-integer arguments.

The method requires positive uniform bridge weights, unit pendant weights and separate unit-coordinate inputs. Numerical conditioning and extension to arbitrary unequal weights remain outside the result.
