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
# Reproduction and verification

Install the pinned-minimum Python requirements in `requirements.txt` and run `python verify.py` in this directory. The included `verification_output.txt` is the output of an actual reproduction using Python with NumPy 2.3.5 and SymPy 1.14.0.

The executable evaluates four rational Cauchy integrals symbolically for a positive scale parameter, confirms equality of the two expected-error matrices after multiplying by the proposed scalar, and verifies the eigenvalue ordering. It independently uses seven deterministic 16,384-angle quadratures and 210 selected error-vector comparisons, including the isotropic boundary.

The proof is analytic and not predicated on those finite-angle quadratures. Assertions do not constitute an independent audit, and no higher-dimensional or noisy-oracle conclusions are verified. No external verification channel has been performed.
