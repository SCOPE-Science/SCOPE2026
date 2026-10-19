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

The mathematical proof uses an \(L^2\)-convergent Fourier series for the logarithmic circle potential, orthogonality of doubling-map frequencies, absolutely summable correlations, and exact trigonometric coboundaries at two couplings. The accompanying script tests rational polynomial identities, exact residue tables, and convergence against the closed-form \(\pi^2/3\) coefficient. The computation is a check rather than a substitute for the infinite-series proof.

Run `python3 verify.py` with an ordinary Python 3 standard-library installation; the script prints `VERIFY_OK` after its assertions. No external audit, physical off-diagonal simulations, or exhaustive literature certification is asserted. The result does not imply pointwise uniformly bounded Lyapunov sums, a central limit theorem, or attraction to the diagonal.
