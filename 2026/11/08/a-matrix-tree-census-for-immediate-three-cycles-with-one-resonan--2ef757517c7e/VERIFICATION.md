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

# Verification and scope

The general proof is in `RESULT.md`. Checks below are finite tests and do not purport to establish the infinite theorem. Replay the two included scripts with Python 3, `networkx==3.6.1` and `sympy==1.14.0`. The accompanying `.out` files are exact captured stdout from the scripts.

`python check_single_resonance.py` tests all connected labelled simple graphs on three to six vertices by computing every distinct simple cycle and comparing a direct three-phase weighted enumeration to an exact matrix-tree determinant after contracting the sole cycle of length divisible by three. It also checks that all graphs with no such cycle have zero three-cycle phase configurations.

`python check_direct_chip.py` uses the original chip-firing update alone, enumerating every state in the mathematically justified box \(0\le x_v<2d_v\), and verifies eight graph examples. Both densities are included. The check covers a theta graph with three internally disjoint path lengths \(2,3,4\), a non-cactus with a unique resonant cycle, and includes a two-triangle multiple-resonance boundary case.

Exactness limits: enumeration through six vertices and the eight selected larger test graphs is finite; unexamined graphs, other temporal periods, and transient dynamics are not computationally certified. The proof, rather than the tests, supplies the all-order generalization.
