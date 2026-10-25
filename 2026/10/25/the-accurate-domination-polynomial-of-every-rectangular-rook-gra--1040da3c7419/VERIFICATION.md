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

Run `python3 verify.py` from the folder holding the embedded files, using Python 3's standard library. Expected final line: `VERIFY_OK`; the recorded program output is included in `verification-output.txt`.

The program derives rook adjacency from coordinate equality, independently evaluates ordinary domination on each actual vertex subset, then enumerates disjoint equal-cardinality competitors directly. The direct-definition comparison covers 10,064 subsets from seven labeled boards: \(2\)-by-\(2\) through \(2\)-by-\(6\), plus \(3\)-by-\(3\) and \(3\)-by-\(4\). It finds 3,946 accurate sets and checks every claimed coefficient on these boards.

A separate all-subsets structural and enumerative comparison covers an additional 1,409,024 subsets of boards of sizes \(3\)-by-\(5\), \(4\)-by-\(4\), \(3\)-by-\(6\), and \(4\)-by-\(5\). For these larger boards the competitor condition is tested through the proved structural rule, not by searching rival subsets. A further exact integer-arithmetic evaluation checks the coefficient minimum and predicted minimum multiplicity on 95 parameter pairs (\(2\le p\le11\), \(p\le q\le15\)).

**Scope of verification:** The classification and universal polynomial follow from the proof, not from finite enumeration. No outside proof certification or independent mathematical audit has been performed. The 2022 source identified in the relationship-to-prior-work section was not fully inspectable; its priority risk remains unresolved.
