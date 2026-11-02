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

# Reproducibility and proof boundary

Execute `python3 verify.py` from the directory containing this document and the verifier. The script has no external dependencies. It constructs the factor set directly from each word, collects all minimal absent bigrams and all absent extensions \(a u b\) whose adjacent length-one truncations both occur, and compares the *full sets* with the stated four families. It also checks the exact total count.

Observed output on the included verifier:

`VERIFY_OK exhaustive_parameter_cases=147 compared_minimal_absent_words=2104`

The parameter grid includes all positive run-length vectors through coordinate bound three for \(q=3\), through bound two for \(q=4,5\), and singleton runs for \(q=6\); powers include \(k=2,3,4\) where indicated in source. Literal enumeration is finite corroboration only. The all-parameter claim is supported by the written classification of the infinite periodic language and the finite-endpoint border argument. No external proof assistant or independent human review was used.
