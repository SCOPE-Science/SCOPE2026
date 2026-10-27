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

Run `python3 verify.py` using the Python 3 standard library. The program checks the three-arrow cycle-closure coefficients for every position through length 11 and independently computes Ewens-weighted full-permutation probabilities through length 7 at four positive rational parameters. It includes all ten degree-determining triangular nodes, and the mathematical proof explains why their exact equality and the independent degree-three lemma imply validity at every length. No numerical extrapolation is used as a substitute for this proof. Independent scientific audit has not been performed.
