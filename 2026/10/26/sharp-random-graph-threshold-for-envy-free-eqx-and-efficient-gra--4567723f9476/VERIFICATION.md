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

Run `python3 verify.py` using the Python standard library. The script exhaustively compares the two subset-cut inequalities with direct assignment of every edge to one endpoint, for all labeled simple graphs of sizes two through five. It also checks 250 reproducible additional graphs of each of sizes six and seven, and evaluates the rate constant numerically.

The program's expected final line is `CHECK_OK`. The tests cannot certify the asymptotic probability statements; those follow from the concentration, Chernoff, union-bound, and second-moment arguments in `RESULT.md`.

The exact domain is unnormalized additive binary graphical goods with simple edges. The result excludes the critical coefficient and does not establish general heterogeneous, normalized, or multigraph versions.
