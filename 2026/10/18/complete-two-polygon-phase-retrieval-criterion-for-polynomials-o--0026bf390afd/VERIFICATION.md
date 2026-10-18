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

# Verification and limits

Run the included standalone file with `python3 verify.py`, using Python with NumPy. The observed completion is:

`VERIFY_OK 5784 deterministic finite comparisons; tested degrees 1 through 8`

The checker uses a fixed pseudorandom seed for complex coefficient vectors and independently compares the measured regular-grid discrete Fourier coefficients to direct polynomial autocorrelation coefficients. It also recovers the extreme Fourier coefficient from the two circle grids, checks rank \(4d\) of the real Hermitian intensity measurement map for the tested degrees, and verifies both explicit ambiguity constructions. Numerical comparisons use displayed absolute-plus-relative tolerances.

The universal mathematical proof is in `RESULT.md`. These finite trials neither prove the theorem at higher degrees nor establish historical priority. The only singular-value conditioning claim concerns a normalized two-dimensional Fourier demixing subsystem, not the full nonlinear recovery problem. Independent audit has not been performed.
