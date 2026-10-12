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

# Verification of the deterministic one-step residual bound

The proof in `RESULT.md` is symbolic for every real SPD matrix and every admissible sketch. The reproducibility checker uses only Python's standard library:

```sh
python3 verify.py
```

It computes the sketched scalar minimizer and true residual from the specified matrices, verifies **two exact rational** equality witnesses for \(\kappa=9\), with \(\varepsilon=3/5\) and \(4/5\), and checks the eigenvalues of their sketch Grams via exact trace and determinant. It independently constructs **56 floating-point** equality cases over eight condition numbers and seven distortions and checks **10,500** random SPD residual/sketch cases against the theorem. Successful execution prints `VERIFY_OK`. The numerical tests do not establish a universal theorem; the analytic proof independently proves the necessary and sufficient bound.

The code is deterministic, seeded locally, and uses no network or compiled packages. It does not verify publication originality or finite-precision behavior. The scientific assertion is restricted to the true residual after the first sketched step in exact arithmetic. No independent audit is claimed.
