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

The finite certificate evaluates complete three-move extension types, not a sample of formulas or a bounded collection of graph invariants. In `type_recursion.cpp`, each atomic triple diagram records all pairwise equalities and all six directed strict-containment tests. For each ordered pair, all third moves are scanned. Nested type sets are then constructed for each first move and for the empty tuple. Interning a set changes only its representation, not membership or equality.

Reproduction: `sh reproduce.sh` compiles the C++17 program, evaluates parameters 1 through 26, evaluates the structurally independent Python implementation through 12, and compares both outputs byte-for-byte with the supplied logs. The recorded replay returned `VERIFIED`. The Python version uses independent endpoint ordering and direct immutable nested sets, not the C++ bit encoding or map internals.

Sharpness is also justified analytically: strict chains of lengths up to seven have existence sentences of quantifier rank at most three, and the maximum strict chain in the rank-\(n\) root poset has \(n\) elements. For the infinite tail, the complete three-round interval game is covered by the 26-point endpoint-gap invariant, with thresholds 0, 2, 8, 26. No computation is used to infer infinitely many cases by extrapolation.

The finite verification for parameters 13 through 26 has one complete C++ implementation, with independent Python agreement for parameters through 12; both scripts and outputs are provided. The proof covers the stated strict-order signature only. Formal proof-assistant certification and independent external auditing have not been performed.
