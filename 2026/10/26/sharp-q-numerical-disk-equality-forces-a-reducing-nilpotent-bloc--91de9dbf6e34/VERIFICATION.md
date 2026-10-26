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

# Proof checks and limits

- Confirmed the paper's assumptions for the overlap estimate, the sharp norm coefficient, and the strict inequality of the coefficient above one on \(4/5<q<1\).
- Recomputed \(q=2h/(1+h^2)\) and checked that the two test vectors on the circle of radius \(h\) have prescribed overlap magnitude \(q\).
- Reconstructed the complex polynomial \(F(z)\), its constant term and both nonconstant coefficients using the stated inner-product convention. The maximum-modulus conclusion forces the compression's second column to vanish.
- Checked \(2cs=q\), \(\rho_qc^2=q\), the vectors at the two distinct phase choices, the normalization of both orthogonal perturbations, and the modulus-expansion argument for arbitrary complex directions in the orthogonal complement.
- Verified that the two phases span both input and output compression coordinates, obtaining *both* invariances required for reduction.
- Checked the converse from the known universal bound and the norm of the direct reducing summand.

Finite sampling is not a proof of this infinite-dimensional assertion; the proof is analytical. No claim is made at the excluded endpoints or without norm attainment. Historical-priority overlap remains subject to the risks stated in the accompanying review. Independent audit: not performed.
