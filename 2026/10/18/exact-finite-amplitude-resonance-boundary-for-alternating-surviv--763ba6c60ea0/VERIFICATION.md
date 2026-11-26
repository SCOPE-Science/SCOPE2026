---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

The unchanged standard-library Python 3 verifier `verify.py` can be run with `python3 verify.py` in the source package. Expected output:

```
VERIFY_OK rational_identity_cases=7 global_orbit_cases=33 finite_amplitude_reversal=PASS
```

The rational checks concern the two-cycle equations and the square of the arithmetic mean, including cases of enhancement, suppression and equality. The decimal trajectories are finite corroboration; global convergence and the critical extinction case follow from the proof in RESULT.md. The survival cap at fixed \(R,h\) is not certified by the numerical trajectories. Its exact test is \(h+\delta\le R\), together with \(\delta<\sqrt{h^2-1}\) for persistence.

For the two example policies at \(R=10,h=5\), the squares of their long-run arithmetic means are \(2\sqrt5\) and \(2\sqrt{10}-5/2\), respectively; the square for the constant policy is 4. The verifier checks the sign reversal, which also follows by direct comparison of these radicals.
