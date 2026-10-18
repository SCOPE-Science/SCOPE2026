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

# Reproducible checks

Run `python3 verify_pcf_rook.py` in the directory containing this file. Python 3.9 or newer is sufficient; no third-party libraries are needed.

The program independently implements both the original open-neighborhood multiplicity test and the proved row/column palette characterization. For all \(1\le m\le n\le13\), it constructs a coloring with the claimed number of colors and verifies that the coloring is proper and proper conflict-free (91 pairs). It also completely enumerates proper arrays for 16 small dimension/palette triples; 156,563 proper arrays are examined, including 129,519 proper conflict-free arrays. It confirms both the equivalence of the tests and the predicted existence or nonexistence at each tested palette size.

A finite enumeration is not a proof for infinitely many parameters. The unrestricted theorem uses the combinatorial proof in `RESULT.md`, including the missing-color conservation argument and the cyclic-group construction. No external audit was performed.
