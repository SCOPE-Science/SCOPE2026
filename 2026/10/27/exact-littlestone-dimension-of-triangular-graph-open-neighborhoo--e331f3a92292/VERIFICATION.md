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

# Reproducibility and verification

Execute `python3 verify_triangular.py --check witness_trees.json` with Python 3 and no additional packages. The verifier constructs every edge of each complete graph of order two through eleven and independently evaluates adjacency as exactly one shared endpoint; a memoized complete binary splitting recurrence reports Littlestone dimensions \(0,1,1,3,3,4,4,4,4,4\). It then parses two full binary-tree certificates for order five (depth three, eight paths) and order seven (depth four, sixteen paths), directly recalculating every path's predictions from its concrete witness hypothesis.

The included transcript `verification_output.txt` has a final `ALL_CHECKS_PASS` line. These checks are finite and do not establish the all-order upper bound; that rests on the star-plus-one lemma and first-positive-branch decomposition in RESULT.md. The verification assumes standard finite sets and ordinary open-neighborhood adjacency; no external certification or independent audit is claimed.
