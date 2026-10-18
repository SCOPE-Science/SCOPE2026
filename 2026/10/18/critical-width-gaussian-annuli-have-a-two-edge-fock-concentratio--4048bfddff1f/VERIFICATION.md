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

The proof rests on four independently reconstructible ingredients: explicit radial diagonalization, an integration-by-parts recurrence, a uniform gamma-to-Gaussian approximation, and a sharp Riemann-sum/concavity argument. The recurrence sign is determined by the logarithmic mean of the two squared radial endpoints, and so determines all finite-rank optimal monomial blocks. The gamma distribution is the law of a sum of independent exponential variables, to which the standard Berry–Esseen inequality applies with rate proportional to the inverse square root of the degree. The sum-to-integral error is uniformly bounded because an optimal block contains a modal degree and comprises only order-\(\sqrt R\) nearby indices.

Run `python3 check.py` in the directory containing the standalone checker after installing the dependency in `requirements.txt`. It calculates the incomplete-gamma eigenvalues, checks finite adjacent identities, tests consecutive-block spectral ordering locally, and compares their partial sums and cutoff eigenvalues with the asserted Gaussian limits for four parameter triples and three increasing radii. It reports 128 diagnostic groups passed. These are numerical samples, not a proof of global spectral sorting or a certificate of uniform asymptotics; the analytic arguments in RESULT.md provide those conclusions.

Independent audit has not been performed. No external certification, independent validation, or claim of uniqueness of the scientific contribution is made.
