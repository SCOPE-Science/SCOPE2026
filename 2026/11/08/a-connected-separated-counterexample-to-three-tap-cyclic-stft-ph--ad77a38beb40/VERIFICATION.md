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

`VERIFY.py` is a complete standalone Python 3 standard-library exact-arithmetic check. Run `python3 VERIFY.py` in the extracted artifact folder. The expected output is `THREE_TAP_PERIODIC_FIBER_PASS exact_window_rows=81 dimensions=6`.

The program checks that the signals are distinct, have a zero, are 2-connected, and have matching Fourier-intensity autocorrelation polynomials for every translation at six different cycle lengths. The full mathematical scope follows instead from the three explicit short-window trinomials and the quadratic invariant equations in RESULT.md. No exhaustive or external independent verification is claimed.
