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
The embedded `verify_equal_pair_alabama.py` uses two independent exact implementations of Hamilton's method: integer quotient/remainder arithmetic and `fractions.Fraction` arithmetic. It verifies the modular residue characterization and closed count for every coprime \(a>c>0\) with \(a\le40\), comprising 489 primitive equal-pair cases, and checks one-period translation of allocations.

Replay command:

`python3 verify_equal_pair_alabama.py`

Expected leading output:

`VERIFY_OK`

The finite replay is a cross-check of the algebraic proof, not a finite-to-infinite inference. It also checks \((3,3,1)\), \((7,7,2)\), and \((9,9,1)\) as concrete parity/period anchors.
