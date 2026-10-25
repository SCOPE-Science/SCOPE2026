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

# Reproduction and limits

Run `python checker.py` with Python 3. The script enumerates all atomic assignments to zero, one or two variables in every once-marked cycle from size 1 to 20 and iterates existential type refinement through quantifier rank 7; each refined type represents the Boolean closure of all formulas of that rank with the specified free variables. It verifies that the full sentence-type classes match the theorem. Independently it checks each explicit cutoff construction for thresholds 1 through 14 on cycle lengths 1 through 34. The theorem for unbounded ranks and sizes is established by the explicit formulas and two-pebble strategy in RESULT.md, not by enumeration. Source priority is not formally certified; independent audit is not performed.
