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

# Finite verification and reproducibility

Run \(\texttt{python3 verify.py}\) from a directory containing the accompanying standalone \(\texttt{verify.py}\). The output recorded in \(\texttt{verification-output.txt}\) was obtained from that source file.

The verifier uses breadth-first-search graph distances and the exact geodesic equality for every unordered selected triple. It enumerates all \(\sum_{n=3}^{9}2^{2n}=349504\) subsets across seven sunlet graphs, then determines inclusion-maximality by testing every available one-vertex extension. The tested maximal-set size distributions agree with the theorem for \(4\le n\le9\); the excluded \(n=3\) case is reported separately. It also checks the cycle-matching edges and the explicit witness's geodesic condition for \(4\le n\le40\).

All finite checks passed. Finite testing does not establish the infinite theorem, does not certify bibliographic priority, and is not an independent audit; the proof is in the accompanying RESULT.md.
