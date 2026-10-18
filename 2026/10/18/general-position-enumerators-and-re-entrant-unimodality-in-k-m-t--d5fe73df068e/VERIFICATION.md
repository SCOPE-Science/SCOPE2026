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

# Reproducibility and evidence

Run `python3 verify.py` using standard Python 3. The script constructs the direct-product adjacency matrix, determines all forbidden induced three-vertex paths, enumerates vertex subsets, and tests one-vertex maximality directly, independently of the proposed four-type structural representation. Tested graph orders are \((3,3),(3,4),(3,5),(4,4),(4,5)\), comprising exactly 1,151,488 subsets. The script compares both size polynomials against closed expressions.

Additional exact-integer tests cover 276 factor-pair profiles with \(3\le m\le n\le25\), the predicted purity and size support, and the exact unimodality criterion for \(K_3\times K_n\) for \(3\le n\le300\). The check output is in `verification_output.txt`. No external dependency, network service, or nonstandard certificate is required.

**Scope of verification:** The code provides only finite consistency checks; it does not prove the classification for all parameter values. The general proof and the sharp coefficient-sign arguments appear in `RESULT.md`. There has been no independent scientific audit.
