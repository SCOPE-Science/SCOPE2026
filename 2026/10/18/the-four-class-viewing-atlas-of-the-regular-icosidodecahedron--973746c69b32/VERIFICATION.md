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

# Verification of the viewing-chamber atlas

Running `python3 checker.py` from the package directory uses standard-library only integer arithmetic in the quadratic ring of the golden ratio. It reconstructs all 32 face normals, 16 distinct great circles, all 90 arrangement intersection rays and their exact multiplicities, then exhaustively tests all 65,536 candidate sign words. It checks exactly 152 feasible chambers in the asserted four classes, 240 two-sided border keys, 60 ten/twelve boundaries and 180 twelve/fourteen boundaries; the refined 60/60/120 adjacency partition is also checked. The checker prints `EXACT_CERTIFICATE_OK` and `COVERAGE: 2^16 sign patterns exhausted; Z[phi] sign & angle tests only`.

The combinatorial certificate relies on the proven fact that all extreme rays of each pointed three-dimensional closed sign cone are intersections of two boundary planes. This statement supplies the exhaustiveness argument absent from mere finite sampling. The analytical spherical-excess identities can be directly checked using the displayed trigonometric definitions; no numeric quadrature or randomized simulation enters acceptance.

The program does not certify historical priority, publication, independence, or behaviour on exceptional projection directions. Independent scientific audit has not been performed.
