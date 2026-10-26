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

# Reproducibility and scope

Run `python3 verify_fan_forts.py` with Python 3.10 or later. It uses only the standard library and does not access external data.

The verifier implements the original fort condition directly on each labeled fan and tests minimality by comparing all fort subsets, independently of the proposed path-word and minimal-domination construction. It exhausts all nonempty subsets for \(2\le n\le16\), totaling \(262{,}121\) tested candidates, then asserts equality of the **full families**, not just their cardinalities. It expands the two displayed rational series by exact integer recurrence for \(n\le100\) and checks the initial coefficients against the exhaustive enumeration. This second computation establishes only algebraic consistency, not the all-length theorem.

`verification_output.txt` stores the actual successful execution result from the packaged scientific checker. No independent audit or external certification is claimed. The infinite classification and enumeration rely on the four-step mathematical argument in `RESULT.md`.
