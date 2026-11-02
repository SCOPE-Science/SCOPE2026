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

# Reproducibility and limitations

Run `python3 verify.py` with Python 3.10 or later. No third-party modules, network access, other scientific files, or hidden input data are required.

The checker constructs the simple graph directly from terminal-to-terminal paths; forms every closed-neighborhood bitmask; and computes the binary nullity by row operations. It exhaustively covers all ordered path-length vectors for four ranges: two paths with edge lengths 2–12, four paths with lengths 2–7, six paths with lengths 2–5, and eight paths with lengths 2–4. That is 12,074 exact matrix comparisons.

An additional deletion recurrence counts matchings modulo two for 139 small graphs and checks the established matching-parity criterion against the derived nullity. An exhaustive null-vector enumeration counts the entire kernel for 41 graphs with at most twelve vertices. Six explicit witnesses cover unique and nonunique cases and several distinct residue configurations. Successful completion prints `VERIFY_OK 12074`.

All computations are finite and serve only as corroboration. The infinite claim relies on the algebraic path recurrence and exact terminal constraints in `RESULT.md`. The program does not assess literature priority or provide independent mathematical review.
