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

# Reproduction and scope

Run `python3 checker.py` using Python 3 and only the standard library. The checker independently computes scattered subsequence deck vectors by dynamic programming, groups all length-3 through length-34 weight-three words, confirms exact partner-map fibers and the rational-coefficient formula, directly enumerates all index triples for a smaller length range, and checks four-deck separation as a supplementary consistency test. A successful run prints `VERIFIED_OK`.

Checked observed values (length, doubletons, distinct three-decks) begin with \((3,0,1),(4,0,4),(5,0,10),(6,0,20),(7,1,34),(8,2,54),(9,4,80),(10,6,114)\). The all-length theorem is proved algebraically in RESULT.md; testing finitely many words cannot by itself establish it. All statements concern scattered patterns with multiplicity and exactly three ones. Historical priority outside inspected sources remains uncertain.
