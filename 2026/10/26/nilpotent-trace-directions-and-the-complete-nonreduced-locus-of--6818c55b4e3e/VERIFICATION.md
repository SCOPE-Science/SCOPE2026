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
# Verification and boundaries

Execute the standalone accompanying file as `python3 verify.py` in a Python 3 environment. It directly implements matrix multiplication modulo primes, exhaustive enumeration of \(3\times3\) matrices in small fields, the full linearized quadratic equations, and Gaussian elimination. Expected terminal marker: `VERIFY_OK_RADICAL_SQUARE_ZERO_REP_SCHEME 68`. The computed pair counts are \(148\) for \(q=2\) and \(1665\) for \(q=3\); all four tangent models were tested for \(r=2,3,4,5\) and characteristic \(2,3,5,7\).

The check is auxiliary, finite and not a proof of the universal assertions. The argument for all fields relies instead on the image/kernel dichotomy, irreducible vector-bundle incidence spaces, flag-bundle intersection, the explicit canonical-form tangent computation, and trace functions lying in the radical but not in the local defining ideal at overlap points. The scheme-level assertion is not a statement about the singular locus alone; it uses a separately exhibited infinitesimal trace witness. Independent mathematical audit has not been performed.
