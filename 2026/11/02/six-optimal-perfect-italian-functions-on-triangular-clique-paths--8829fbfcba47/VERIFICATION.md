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

# Verification

Execute `python3 verify.py` from the directory containing the included standalone checker; it uses only the Python standard library and downloads nothing.

The checker reconstructs the 27 possible columns, all 729 ordered column pairs, and exact transitions using the open-neighborhood zero-vertex equation. It evaluates every state and every tied minimizer with arbitrary-precision integers, and asserts equality of the entire length-14 state vector with the length-13 vector shifted by one unit of weight. Both include precisely 306 reachable pair states; all 423 other states are unreachable. The normalized length-13 vector has SHA-256 `0bdb58621f1fc0b6e856772936a4aa4ba48fd51886d2e1d3f9d27cafbd2db188`.

It verifies all exact optimum/count pairs \((n+2,6)\) for \(4\le n\le14\). The transition commutes with a uniform shift of all state costs, so the finite full-vector equality proves the same minimum and count for all larger lengths by induction. The program also builds six periodic witnesses independently through length 49 and exhaustively searches all vertex-by-vertex assignments of weight at most the claimed optimum for lengths 4, 5 and 6, using graph adjacency rather than the column dynamic program.

Expected terminal marker: `VERIFY_OK`. Computational tests of a few lengths alone are **not** the infinite proof; the full-state shift identity plus algebraic commutation supplies that step. The state-shift equality and all six witness constructions are rechecked by the standalone program from first principles. No independent audit has yet been performed.
