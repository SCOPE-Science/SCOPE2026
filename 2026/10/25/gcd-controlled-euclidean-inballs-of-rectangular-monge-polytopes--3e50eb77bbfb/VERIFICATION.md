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

# Reproducible exact checks

Run `python3 monge_rectangular_exact_check.py` with Python 3. The script uses only the standard library and constructs rational optimal-transport dual certificates for every ordered pair of dimensions from 2 to 12. It checks the interval-overlap margins, spanning-forest support and its connected-component count, strictly positive dual slack at every unused cell, exact unit adjacent mixed differences, equality of the certificate mass to the positive quadrant-weight sum, and the square and two-row closed forms. Its expected final line is `RECTANGULAR_MONGE_CERTIFICATES_OK cases= 121`.

Additional development checks (not dependencies of the proof): the full gcd formula was checked for 1,156 pairs of dimensions from 2 to 35 by integer arithmetic; direct independent Chebyshev linear programs agreed with the closed formula for six rectangular and square sizes. These are finite checks only and do not certify the universal theorem. The proof of the all-dimensions statement, including the attainability lemma and center-space dimension argument, is in `RESULT.md`.

Independent audit has not been performed.
