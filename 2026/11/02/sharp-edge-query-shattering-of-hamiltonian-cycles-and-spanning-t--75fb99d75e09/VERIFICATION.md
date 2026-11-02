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

# Reproducibility and proof boundaries

The theorem's all-order VC bound is proved by explicit degree-deficit and Hamiltonian cycle arguments in `RESULT.md`; no experiment or unexplained finite observation is used in that deduction.

Run `python3 verify_2factors.py` and `python3 verify_hamilton.py` in a directory also containing `independent_2factors.py`, `certificate.json` and `hamilton_certificate.json`. The scripts use only the Python standard library. The primary two-factor generator visits every subset of exactly \(n\) edges of the complete graph and retains it if every degree is two. The primary Hamiltonian generator enumerates cyclic orders modulo reversal. Every claimed VC-support count is obtained by complete trace-set enumeration and the hereditary pruning of unshattered supports.

The depth checker on any finite version space \(V\) accepts depth \(d\) precisely when a query has both child spaces accepting depth \(d-1\), with the cardinality obstruction \(|V|<2^d\) applied first. For order seven, the all-edge symmetry allows the depth-seven upper bound to be reduced to rejecting depth six after a fixed positive first edge. This was checked with 176 visited depth states in the two-factor class and 86 in the Hamiltonian class. The certificates contain complete lower-bound trees: 31 internal nodes and 32 distinct terminal witnesses at order six; 63 internal nodes and 64 distinct terminal witnesses at order seven, for each concept family. For smaller orders they contain the corresponding complete trees.

The independent checker generates all two-factors by decomposing permutations into cycles of length at least three, extracts the connected subfamily, computes all shattered supports by refining the hypothesis fibers for each newly appended edge query, and replays every certificate path against an independently generated edge mask. It separately excludes depth six in the positive branch of the seven-vertex classes using every query edge. The two generators and the two VC-census approaches are algorithmically different, although the review remains within one scientific assessment and is not an independent external audit.

The class sizes are 1, 3, 12, 70 and 465 for two-factors, and 1, 3, 12, 60 and 360 for Hamiltonian cycles at orders three through seven. The upper bound for online depth six at order six follows independently from positive-first-query branch sizes 28 and 24, both less than 32. The depth-seven upper bound at order seven is an exhaustive finite computation; the statements do not extrapolate it beyond that order.

No result beyond the mathematical and finite ranges explicitly specified is verified. Historical novelty cannot be certified by keyword search alone.
