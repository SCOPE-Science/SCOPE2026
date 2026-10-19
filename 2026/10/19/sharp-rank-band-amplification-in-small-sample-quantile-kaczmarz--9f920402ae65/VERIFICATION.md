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

`verify.py` requires Python 3 and the standard library. It executed successfully. Its finite checks enumerate every size-\(k\) subset for tested small populations, reconstruct exact probabilities as fractions, compare every marked set of the tested sizes against the claimed contiguous maximum, and verify exact expected-error identities. The test reported 152 distinct finite parameter/marked-count configurations. Finite-population hypergeometric probabilities at \(k=20,40,80,120\) were compared numerically against the normal-window limits for three scaled widths. These checks are diagnostic, not substitutes for the general combinatorial and central-limit arguments in the proof. The result does not assert multi-iteration instability. Independent audit has not been performed.
