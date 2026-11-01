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

The proof is an exact geometric argument: translate parametrization by barycentric caps, Brunn–Minkowski concavity and strictness, finite inclusion–exclusion, and normalized Dirichlet maximum-coordinate probabilities. No computational verification is used as an infinite-dimensional proof.

The self-contained standard-library program `verify_reflected_simplex.py`, run from this document's directory with `python3 verify_reflected_simplex.py`, reported `PASS 68437 exact or independently sampled checks`. It independently compares the full inclusion–exclusion formula with the two-level specialization for rational caps; checks exact endpoint and low-dimensional results; and performs randomized exclusion and Monte Carlo consistency tests. The random tests are nonexhaustive; the supplied code does not certify novelty or independent correctness.

Scientific limits: the full theorem assumes a fixed nondegenerate simplex, uniform volume measure, an exactly equal-size reflected testing simplex, and dimension at least three. The planar case and the classical Dirichlet maximum distribution are prior knowledge. The exponential estimate is an upper bound, not a sharp asymptotic.
