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

The theorem is proved analytically for every admissible \(m,n,t,q\). The finite checker is corroborative only and is not used to infer any unbounded statement.

`artifacts/verify.py` constructs matching-deleted bicliques directly. It enumerates every admissible non-crown profile with total order at most \(9\) and \(m\le4\), tests each \(q\) from \(2\) through \(m+1\), enumerates proper colorings up to color-name permutation, and computes color-dominating vertices from closed neighborhoods.

Replay command:

`python3 artifacts/verify.py`

Observed output:

`ALL CHECKS PASSED; profiles=66; canonical_colorings_checked=24043; max_order=9`

The checker covers both realized values \(2\le q\le m\) and the first non-realized value \(q=m+1\) for each tested graph. The universal proof rests instead on the mixed-shore color-class lemma and the shore-purity obstruction.
