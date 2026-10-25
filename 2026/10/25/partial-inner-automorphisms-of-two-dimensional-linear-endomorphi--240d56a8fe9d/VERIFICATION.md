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

# Reproduction and limits

Run `python artifacts/verify.py` using a standard Python 3 environment. The script enumerates all matrix pairs and tests the domain conditions for the prime fields \(\mathbb F_2\) and \(\mathbb F_3\), and then checks the predicted full, line, and zero-only domain counts. It prints `VERIFY_OK` with sizes \(52\) and \(201\) respectively. The precise algebraic argument in `RESULT.md` establishes the all-field claim. A finite check cannot establish universality, and no independent audit or external certification was performed.
