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

Run `python3 verify_toric.py` with Python 3.10 or later. It uses only the standard library. The program constructs all determinant-nonzero exponent sums directly from each Hilbert basis for \(3\le n\le24\) in characteristic zero and characteristics \(2,3,5,7,11,13,17,19,23\). All comparisons and facet-weight tests use exact integers. It checks every proposed vertex is uniquely exposed, the lower-support-function formula at a finite set of dual-cone weights, the facet-ray identities, and the strict separation of the two exceptional fans. It produced the marker:

`TORIC_NASH_ALL_PRIMES_NEWTON_SUPPORT_AND_FAN_TESTS_OK`

The general theorem is established by the determinant classification and exact optimization over all dual-cone linear forms in `RESULT.md`. Finite program tests cannot certify every parameter or characteristic; this distinction is essential. The source theorem identifying the Nash blowup with the logarithmic-Jacobian blowup is cited, rather than independently reproved. No external independent validation has been performed.
