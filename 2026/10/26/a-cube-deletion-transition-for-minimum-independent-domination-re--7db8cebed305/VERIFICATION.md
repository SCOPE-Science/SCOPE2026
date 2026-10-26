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

Run `python3 verify.py` (Python 3.8 or later, standard library only) to reconstruct each test tree, enumerate all vertex subsets independently, classify their independence and dominating status, retain minimum-cardinality solutions, and compute all token-slide edges by comparing set symmetric differences with graph edges.

Cases: \(2\le s\le6\), \(0\le t\le3\), 20 distinct trees. Total candidate subsets: 163680. Total minimum sets examined: 258. Total edges in the resulting reconfiguration graphs: 625. The test compares the exact sets and edge sets with the theorem's three explicit forms; `verification_output.txt` stores the observed output. The additional \(s=2\) case tests the boundary, though the theorem is stated for \(s\ge3\).

The computation cannot establish the unrestricted theorem or bibliographic originality. The proof in `RESULT.md` independently establishes all claimed infinite formulas and geometric consequences.
