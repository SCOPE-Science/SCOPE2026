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

Run `python3 verify.py` in this directory using Python 3 and only its standard library. The program constructs the claimed power series by exact binomial-series convolution; it checks every ternary word profile through length \(9\), checks every matrix of total multiplicity at most \(12\) by independent degree and weak-connectivity criteria (corresponding to word lengths up to \(13\)), and verifies the reduced rational function identity. Successful execution prints `VERIFY_OK`.

These finite checks verify reproducibility but do not prove an infinite theorem. The latter follows from the sector classification and generating-function derivation in `RESULT.md`. The originality comparison is limited by the inaccessible full text of the expanded 2012 Markov-types paper. Independent audit has not been performed.
