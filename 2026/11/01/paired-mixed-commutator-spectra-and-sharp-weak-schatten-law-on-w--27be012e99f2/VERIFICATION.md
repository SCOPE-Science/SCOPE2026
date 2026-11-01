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

# Verification and limits

The analytic argument in RESULT.md gives the complete exact coefficients via normalized monomial projection and the formula \(C_{m,n}e_k=d_ke_{k+m-n}\). Since translation is unitary, the singular values are precisely the absolute diagonal coefficients, including their multiplicities. The explicit positive and negative tails, gamma log-convexity, reflected cancellation and trigamma asymptotic together establish the claimed infinite-dimensional limits.

To reproduce supplementary finite checks using a standard Python 3 installation, run `python check_harmonic_mixed.py` next to this file. The reported finite test count is 16,278. This tests several weights and degrees but is not an exhaustive proof, does not certify publication priority, and does not replace the proof in RESULT.md. The inspected literature establishes qualitative vanishing symmetry and commutator rigidity; it does not provide independent audit of the new weighted mixed-degree spectral claim. Independent mathematical audit has not been performed.
