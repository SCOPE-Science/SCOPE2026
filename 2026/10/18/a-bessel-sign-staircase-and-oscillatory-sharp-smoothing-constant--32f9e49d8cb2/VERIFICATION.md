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

# Reproducibility and verification

`check.py` uses only the Python 3 standard library. From the directory containing this file and `check.py`, run `python3 check.py`. The check reports 134 finite numerical assertions: Fourier-quadrature heat kernel evaluations, signed second-difference and total-variation consistency, Bessel crossing brackets and ordering, and large-time oscillatory coefficient tests. This is a finite independent computational cross-check, not proof of all-time or all-integer-order claims.

The analytic proof's critical verification paths are: the Bessel recurrence and Riccati derivative identity; the sign crossing and uniqueness for each integer Bessel order; discrete telescoping of the signed mass; the stationary Fourier expansion at large time with Gaussian-dominated differentiated remainders; and the control of integer-rounding displacement at switching boundaries. All are detailed in `RESULT.md` and require no external data files.

The first public reference date is supported by arXiv:math/0206089 (2002-06-09). Historical priority is conditional on the inspected sources; the 2021 Abadias et al. comparison text was inspected in its publicly accessible author arXiv manuscript (arXiv:2401.16377, Theorem 4.3(iii) and Section 7.2), and an independent literature audit has not occurred.
