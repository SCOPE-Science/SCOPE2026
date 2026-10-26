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

The analytic proof uses normal-ordered Weyl displacement matrix elements and the fact that associated Laguerre polynomials of successive degrees form a polynomial basis. The radial blind space is given explicitly by divisibility by the monic polynomial of squared sampling radii (and by the extra factor at zero imposed by the trace constraint). No finite computation is treated as proof of the arbitrary-cutoff result.

Executable verification: run `python verify.py` with dependencies from `requirements.txt`. The checker tests 72 exact rational-radius block ranks with cutoffs from zero through seven, constructs a distinct positive-density pair at cutoff three invisible on two prescribed circles, compares 45 Weyl matrix elements with independent position-space quadrature, and tests half-circle Fourier reconstruction. Results are recorded verbatim in `verify_output.txt`. The numerical quadrature discrepancy was below \(6\times10^{-16}\) on these test cases.

Limitations: the proof assumes exact complex measurements and known trace, and gives no uniform condition number as radii approach each other. Scientific priority remains subject to independent literature assessment. Independent audit has not been performed.
