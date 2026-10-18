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

# Reproducible checks and boundaries

Run `python3 verify.py` from the directory containing the supplied standalone script. It depends only on the Python standard library and uses exact rational arithmetic. The script exhaustively enumerates all tournaments with \(3\le n\le6\), with counts of \(8\), \(64\), \(1024\), and \(32768\) respectively. It independently computes cyclic triangles by oriented triples and tests all of: the centered score identity; pairwise covariance zero for all distinct centered quadratic scores; their variances; unconditional cycle moments; zero linear score covariance; conditional first and second moments for every attainable score; and exactly \(1/n\) explained variance.

The general theorem is established by the elementary all-parameter proof in `RESULT.md`. Exhaustive finite enumeration is not a proof for arbitrarily large \(n\). The computation does not assess publication priority. The result neither claims a full conditional distribution nor independence of the quadratic vertex-score terms. External independent review has not been performed.
