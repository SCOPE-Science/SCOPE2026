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

# Reproduction of mathematical identities

Install the versions in `requirements.txt`, then execute `python verify.py` in the same directory. The script performs exact symbolic evaluations of \(J_p\) and \(J_p^{\mathrm{ac}}\) for \(p=1,2,3\), verifies all three weighted fractions and six finite-sample totals at several sizes, and separately integrates the six angular integrals using high-precision quadrature. The successful terminal marker is `ALL_SYMBOLIC_AND_QUADRATURE_CHECKS_PASSED`.

The proof of the infinite-family result is in `RESULT.md`: it establishes the beta height law and the product-density reduction before invoking the evaluated trigonometric integrals. Exact symbolic and numerical checks of integrals are additional reproducibility evidence; they do not themselves certify geometry, general independence, or historical novelty. The included code has no access to the original random samples and asserts no independent audit.
