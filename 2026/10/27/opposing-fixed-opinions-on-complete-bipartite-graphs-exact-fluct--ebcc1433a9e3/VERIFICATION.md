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

# Reproducibility and verification

The standalone `verify_voter.py` uses only the Python standard library. Running `python3 verify_voter.py` from the same directory independently forms the lumped Markov generator, solves rational stationary equations by Gaussian elimination and compares the mean and second moment with the theorem for every \(1\le m,n\le5\) (25 cases). It then checks 55 exact beta moments by a separate rising-factorial formula against the stationary generator moment recurrence for five rational partition ratios.

Observed result: `PASS: 25 independent finite-chain exact stationary comparisons`; `PASS: 55 beta-law moment recursion checks`.

The arbitrary-size variance and weak-limit beta law are proved analytically in RESULT.md. Finite tests do not certify all graph sizes or provide an independent mathematical review. The proof's limiting moment argument assumes both part sizes diverge and the ratio remains strictly between zero and one. Independent scientific audit has not been performed.
