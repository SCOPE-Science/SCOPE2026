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

Run `python verify_double_star.py` under Python 3.9 or later. The source file and `verification_output.txt` contain the executed code and observed terminal output.

The first loop constructs the two centers and their pendant leaves, computes all graph distances, checks each proposed coloring for every ordered parameter pair \(1\le a,b\le14\) and every \(2\le k\le N\), confirms strict packing distances between equal colors, and verifies every broadcast-dominating partition part. There are 3,136 such profiles.

The second independent test exhaustively scans three vertex-status choices—label one, label two, or a unique high label—and enumerates all all-low dominating groups for \(a,b\le4\), \(a+b\le6\). Since the graph diameter is three, distinct high-status vertices necessarily have distinct labels, so no possible \(k\)-palette coloring is omitted from this reduced search. It checks the predicted palette equality for 58 profiles. These checks do not themselves certify infinitely many graphs.

The mathematical proof in `RESULT.md` is independent of the finite tests. In particular, the classification of independent dominating sets, the two-label-two-leaf contradiction, and the explicit upper constructions are stated for all positive integer pendant counts. No external audit was performed.
