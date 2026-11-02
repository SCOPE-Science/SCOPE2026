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

# Reproduction checks

All code uses only Python 3's standard library. Place `lattice_verify.py`, `structural_verify.py`, `certificates.json`, and `results.json` together and execute `python structural_verify.py`, `python lattice_verify.py`, and `python structural_verify.py` again. The first invocation verifies the original embedded lower-bound certificates before regeneration; the second exhaustively recomputes finite upper and lower ranks and rewrites certificates and tabulations; the last replays the regenerated certificates. Compare the regenerated `certificates.json` bytewise with the original if exact reproducibility is required.

`lattice_verify.py` enumerates convex subsets as differences of nested order ideals, calculates their exact counts for widths one through ten, and computes the classical Littlestone recurrence over **every** candidate first query and both answer classes. The recorded version-space state counts are respectively 9, 63, 321, 1306, 4560, 14460, 43780, 132542, 416789, and 1390695 for widths one through ten. Each computation terminates with a completed root rank and therefore is an exhaustive finite calculation, not a time-limited search. The program independently compares its ideal-difference enumeration with all subsets passing the order-betweenness test for widths through eight.

`structural_verify.py` independently generates order-convex sets by directly testing all triples of comparable elements, checks **all** subsets of support sizes zero through four for widths one through eight, and confirms all coefficients against actual shattering traces. It also validates every query, split, and terminal witness in the four stored complete adaptive trees, with 256, 256, 512, and 512 leaves for widths seven, eight, nine, and ten.

The universal count, shattered-support criterion, exact polynomial, adaptive lower bound and leading asymptotic are proved mathematically in `RESULT.md`. The exact adaptive ranks through width ten are proved by exhaustive recurrence with the supplied code and certificate checks. No finite computation is used to infer an unproved all-width rank formula. Independent external audit has not been performed.
