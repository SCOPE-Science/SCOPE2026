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

Run `python3 verify_cube_rank4.py` with Python 3.8 or newer. The script uses only the standard library. The supplied `verify_cube_rank4_output.txt` is the output of its execution.

The integer-orbit calculation enumerates every legal split of the Hamming-coordinate classes for each dimension from one through sixteen. It builds types by set formation at each of the three remaining levels in the four-move back-and-forth game. Distinct root-type identifiers are generated only for mathematically unequal, exact finite sets. An unrelated direct enumeration of graph tuples of actual binary words agrees for each dimension from one through five.

The observed classes among dimensions one through sixteen are exactly the five singleton classes followed by the block from six through sixteen. The separate mathematical proof in `RESULT.md` establishes that fourth-vertex extension sets depend only on coordinate-type counts capped at four, that pair-extension sets depend on two coordinate counts capped at eight, and therefore that every dimension at least sixteen has the same root type. The finite calculation itself is not a proof of this unbounded statement.

Limitations: the exhaustive execution tests this program and these dimensions. No independent formal checker or external mathematical review has been conducted.
