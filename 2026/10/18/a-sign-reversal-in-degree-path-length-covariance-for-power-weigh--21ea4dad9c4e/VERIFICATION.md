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

Run `python3 verify.py` using standard-library Python 3. The code compares direct weighted enumeration of every parent-choice tree with the exact conditional-martingale covariance formula at all n=3,...,7, i<n, and alpha=-2,-1,0,1,2 (100 independent exact-rational identities); 99 sign checks and five additional limit/constant checks total 204. The program was executed against its actual packaged path successfully.

These finite checks do not establish a theorem at arbitrary real alpha or infinite n; these are shown analytically in RESULT.md. The public scientific literature provides the original weighted tree model and known total-path-length innovation structure; neither an independent proof audit nor an independent novelty assessment has taken place.
