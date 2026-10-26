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

The reproducible source file `verify.py` checks the theorem against the direct defining condition, not against a secondary implementation of the claimed part-size formulas. It builds adjacency masks, decides whether every vertex omitted from a candidate set has a unique omitted neighbor witnessed by a selected vertex, enumerates ordinary unlabeled set partitions, and derives valid omission pairs from that direct test. Only after independently verifying the isolate-free and deficiency hypotheses does it compare partition counts to the matching–triangle formula.

Execute `python verify.py` beside `verification.out`. The recorded complete output confirms 14, 21, and 29 integer-partition profiles at orders seven, eight, and nine; five ten-vertex graph profiles; and 244 qualifying deterministic random graphs of orders seven and eight, totaling 313 unrestricted-scope test graphs. As a boundary control, the excluded graph \(K_{3,3}\) has 16 two-block and 48 three-block super-coalition partitions. No exhaustive claim is made for all graphs of unrestricted order, and finite checks are not used as an infinite proof.

The mathematical proof in `RESULT.md` proves the universal result for every graph satisfying the stated assumptions. No independent external audit, formal proof certification, or priority determination is claimed.
