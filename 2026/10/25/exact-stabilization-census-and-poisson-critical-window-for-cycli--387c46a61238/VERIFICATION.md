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

The attached standalone Python 3 program `verify.py` was executed and returned:

```
VERIFY_OK independent_configuration_tests 8184 matrix_count_tests 55 sharp_maximum_tests 10
```

It enumerates all binary configurations on rings of sizes \(3\) through \(12\), independently simulates the cellular automaton until it revisits a state, compares exact transient lengths with the proposed run-length law, and verifies exact integer matrix-trace census counts at 55 parameter pairs. It also checks the sharp worst-case count of \(2n\) configurations at each size.

The tests are finite: correctness for all ring sizes and the Poisson asymptotic require the analytic arguments in `RESULT.md`. The same-source literature comparison and these local checks are not independent scholarly validation. No independent audit has been performed.
