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

# Verification procedure and scope

Run `python3 verify.py` with Python 3 and its standard library. The program checks \(2240\) independently generated, rational-valued graph-and-target examples for the access-map expansion, exact inverse reconstruction, and target-wise surjectivity; it checks the optimal unit factor, the connected-star failure of a dimension-free \(\ell_\infty\) version, and a nonreciprocal directed countercomparison. The verifier uses exact rational arithmetic and asserts all identities; successful execution prints a single PASS line.

The mathematical proof is in `RESULT.md`. No finite enumeration can certify the all-graph quantifiers; the cancellation identity and the surjective greedy elimination are the proof. The algorithm may perform arithmetic with growing rational numerators and denominators; the stated polynomial bound counts arithmetic operations rather than bit complexity.

The current package reports internal consistency checks only. Independent audit has not been performed.
