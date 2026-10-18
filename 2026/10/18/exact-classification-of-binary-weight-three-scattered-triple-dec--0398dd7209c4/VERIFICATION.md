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
# Verification record

Execute `python3 CHECK.py` with Python 3 and its standard library; no external packages, network, or randomization are necessary. The program directly forms every scattered triple by iterating all increasing triples of positions in every binary word containing exactly three ones, for all word lengths from 3 through 19. The comparison tests each of the eight deck coordinates, deck class cardinalities, exact partner transformation, and expected number of collision pairs.

The packaged `CHECK_OUTPUT.txt` gives the reproducible deterministic results: all 4,845 tested weight-three words pass, the first ambiguity occurs at length 7, and there are no classes with more than two members in the tested range.

The finite check does not certify the theorem at untested lengths. The arbitrary-length result is supported by the algebraic counting proof in `RESULT.md`. Independent audit has not been performed.
