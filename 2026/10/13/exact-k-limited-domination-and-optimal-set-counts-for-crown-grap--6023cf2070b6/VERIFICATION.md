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

The bundled `verification/verify.py` evaluates the claimed formula independently of the prose proof. It enumerates all feasible support-size/intersection profiles for every \(3\le n\le50\) and \(1\le k\le n-1\), computes the exact number of minimum sets from multinomial support counts, and compares both quantities with the closed formulas. It also directly enumerates every pair of vertex subsets on the two shores for \(3\le n\le6\), testing domination and the \(k\)-limited condition from adjacency.

The replay output is bundled as `verification/replay.txt`. These are finite stress tests only; the infinite theorem is established by the exact support proof in `RESULT.md`.
