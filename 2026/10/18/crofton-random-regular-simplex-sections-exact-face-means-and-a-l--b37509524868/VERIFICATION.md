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

# Mathematical verification

Run `python3 verify.py` using only the Python standard library. Actual completed execution printed `VERIFY_OK` after checking the face formula for every rank and face index in dimensions three through twelve, checking Gaussian spacing and expected-range integral identities, and comparing predicted mean face counts against Crofton-weighted calculations over 33,000 independently sampled Gaussian normals. Numerical quadrature uses fixed endpoints and midpoint integration. These tests are finite and approximate where stated; exact all-dimensional validity, Gaussian range asymptotics, and the distributional exponent law require the analytical proof in `RESULT.md`. The scope is invariant affine slicing of regular simplices only, with no quantitative distributional convergence rate. No independent scientific audit was performed.
