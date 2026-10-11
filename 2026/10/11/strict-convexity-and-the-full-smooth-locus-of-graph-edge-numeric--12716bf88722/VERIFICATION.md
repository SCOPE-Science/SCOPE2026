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
# Reproducibility and verification

Run `python3 verify_graph_norm.py` with Python 3 standard library. The checker constructs all nonempty labeled simple graphs on two through five vertices and tests whether they have a pair of vertex-disjoint edges. In every one of the \(1094\) cases the exact graph test agrees with the star-or-triangle classification; for each of the \(985\) disjoint-edge cases it numerically checks the norm-one flat face. It also numerically probes first-order cusps and verifies elementary triangle/star spectral identities.

Observed:

`VERIFY_OK graphs=1094 matching_one=109 disjoint_matching=985 triangle_cusp=0.2500004 triangle_axis_slope=2.5e-06 cycle4_cusp=0.1381970 analytic_proof_needed=True`

The Jacobi spectral solver runs in floating point, so its positive tests are numerical consistency checks rather than exact certificates. The proof of all graph sizes, uniqueness of supporting eigenvectors, and first-order formula is analytic in RESULT.md, particularly parts (3)–(5). The cited primary paper and its first public date are available at https://arxiv.org/abs/2303.00876. The proofs are not independently validated.
