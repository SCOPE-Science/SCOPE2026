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

# Verification

The identities in the proof may be checked symbolically: the degree-two Walsh coefficients must all vanish; their full nonzero solution support has size two; the real absolute-value identity fixes the anchor residual; coordinate basis witnesses saturate the lower bound.

Run the accompanying `verify_rademacher_anchor.py` with Python 3. It enumerates every bipartition of the sign-frame measurement rows for dimensions \(2,3,4\) and checks ranks exactly using rational arithmetic. For each dimension, a distinct-magnitude anchor succeeds while a repeated-magnitude anchor fails. The finite tests also evaluate equation (3) on explicitly generated unaugmented ambiguity families and check an equality witness.

The script does not prove higher-dimensional completeness or infinite families: those statements follow from the symbolic Walsh-orthogonality proof and exact classification in `RESULT.md`. No external audit or independent validation has been performed. The fiberwise separation law is distinguished from a global lower Lipschitz constant.
