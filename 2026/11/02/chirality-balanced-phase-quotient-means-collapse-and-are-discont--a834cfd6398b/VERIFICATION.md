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

The proof in `RESULT.md` is a complete analytic argument in normalized \(L^2\); it establishes all parameter ranges and equality cases independent of numerical sampling.

`verify.py` uses Python's standard library and checks exact rational Fourier-coefficient distance identities for \(\varepsilon\in\{1/10,1/4,2/3,9/10\}\), plus the exact variance identity for chirality weights \((1/4,3/4)\), \((1/2,1/2)\), and \((2/3,1/3)\). A 256-point grid checks three continuous perturbation examples and the balanced segment geometry. Run `python verify.py`; expected observed output:

`PASS: exact rational coefficient identities and 256-point Fourier quadrature`

The finite grid is not used to infer uniqueness for all shifts or dimensions: these follow from the continuous correlation identity and strict inequality \(\varepsilon>0\). Historical priority was checked against relevant literature but has not been independently certified. No external validation of this result is asserted.
