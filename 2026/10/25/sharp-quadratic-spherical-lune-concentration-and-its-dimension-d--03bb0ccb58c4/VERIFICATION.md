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

Run `python wedge_spectral_checker.py` from a directory containing this file and the checker. The script requires Python 3 with NumPy; it makes no network requests. The expected output is included in `checker_output.txt`.

The checker independently constructs the full complexified traceless-symmetric matrix basis; it calculates concentration Gram entries by integrating conditional spherical fourth moments, rather than assuming the claimed invariant-block eigenvalues. It checks the complete predicted spectrum, eigenvalue trace, critical threshold, and two proposed Rayleigh-optimal families at 32 dimension/aperture pairs, reporting 192 assertions. The tested dimensions are \(3,4,5,8\); these finite tests cannot establish the theorem for all dimensions or all angles. The proof in `RESULT.md` is the basis for the universal conclusion.

The independence status refers only to external scientific validation, which has not occurred. No automated finite test is represented as a formal proof or external certificate.
