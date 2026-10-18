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

# Verification and reproducibility

Run `python3 verify_fermat_cubic.py` in a working directory containing this file. No external packages, downloads, or proprietary services are required.

The checker independently enumerates projective points on the 27 Fermat-cubic lines in characteristics 7 and 13, confirming the 18 triples, 81 doubles and 135 intersecting line pairs in both good characteristics. It verifies the explicit 20-dimensional kernel of the Picard-class matrix over the integers, constructs the 45-component blowup dual graph, and computes the rank of the 135-by-45 incidence matrix and of the 135-by-235 extended cup-product matrix over the prime field of order 101. The exact ranks are 44 and 135 respectively.

The geometric line-intersection argument and the Deligne weight spectral sequence, not finite-field sampling, establish the characteristic-zero incidence and rational cohomology dimensions. Reduction modulo 101 proves a nonzero maximal integer minor, hence gives a rigorous lower bound that attains the full possible rank over the rationals. This does not establish integral cup-surjectivity or an integral Smith normal form.

The source paper is accessible as HTML at https://arxiv.org/html/2605.11909v2, notably Theorem 1.1, Lemma 5.3, Sections 3-6. The related 2025 mixed-Hodge paper is arXiv:2501.03202. Their known generic and general-framework statements are distinguished from the special Fermat cohomology-ring claim.
