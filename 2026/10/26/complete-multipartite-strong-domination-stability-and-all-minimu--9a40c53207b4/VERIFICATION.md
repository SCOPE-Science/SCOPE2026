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
# Reproducible verification

Run `python3 verify_strong_stability.py` with an ordinary Python 3 interpreter. The program has no nonstandard dependencies.

The program directly constructs complete multipartite graphs as bitmask adjacency lists and computes each strong domination number from the defining quantifiers: all selected-subset sizes are considered in increasing order, and vertex degrees are recalculated in each residual graph. For every profile of at least two parts and total order \(3\) through \(11\), it verifies the original strong domination number, that no smaller deletion changes it, and that the **entire** family of minimum changing deletion subsets is exactly as predicted. It also separately tests that proper deletions of complete graphs do not change their value.

Expected terminal lines are recorded verbatim in `verify_output.txt`. The finite checker is corroborative only; the infinite result and uniqueness claims are established by the part-size lemma and complete case split in `RESULT.md`.

The 2026 manuscript's balanced graph assertions are not used as premises: the minimal example \(K_{2,2,2}\to K_{1,2,2}\) changes its strong domination number from \(2\) to \(1\) in a single vertex deletion. The same effect persists for arbitrary numbers of size-two parts.

No external independent audit or human verification is implied by these tests.
