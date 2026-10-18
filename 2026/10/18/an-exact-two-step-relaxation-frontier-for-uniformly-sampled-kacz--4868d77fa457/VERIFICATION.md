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

# Verification and scope

From a directory containing `RESULT.md` and `verify.py`, execute `python3 verify.py` with Python 3 standard library. The exact-rational verifier directly builds the two one-step propagation pairs, enumerates the four ordered two-step products, checks the symbolic \(D_2\) entries and its determinant and trace across 1,729 rational triples, and independently evaluates the rational witness. Expected success marker:

```text
VERIFY_OK exact_two_step_matrix_cases=1729 indefinite_cases=1089 nonnegative_cases=640 witness_determinant=true witness_first_step=true witness_second_step=true
```

`verification_output.txt` contains the stdout actually produced by the bundled program. The verifier does not prove the uncountable parameter range: the analytic matrix identity, exact sign analysis, and unique-root argument in RESULT.md constitute the general mathematical proof. No external independent audit has been performed. No finite-precision or large-matrix performance experiment is asserted.
