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

The packaged checker `verify_parity_dichotomy.py` is a finite algebraic sanity check, not a substitute for the analytic proof.

It verifies the following reproducible consequences of the formulas:

- the upper- and lower-boundary prefactors cancel the regular part for odd factor count and double it for even factor count;
- for \(m=3\), the Laurent coefficients and jump normalization give exactly \(-1/(8\pi^2\sqrt6)\) for \(\delta_0''\) and \(-1/(4\sqrt6)\) for \(\delta_0\), matching the published formula with \(Q=6\);
- the leading origin coefficient is nonzero for the tested odd dimensions and corresponds to derivative order \(m-1\);
- representative square-root ratios satisfy the exact Pell-type integer separation identity used in the Diophantine estimate.

The replay output ends with `VERIFY_OK`. The infinite support and convergence claims rely on the proof in `RESULT.md`, not on finite enumeration.
