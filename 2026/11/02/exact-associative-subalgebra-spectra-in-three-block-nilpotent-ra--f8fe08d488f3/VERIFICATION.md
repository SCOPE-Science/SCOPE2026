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

The theorem was checked by a direct proof: all subspaces containing the one-dimensional square are automatically subalgebras, and every avoiding subalgebra is a graph over a pairwise zero-product subspace. An orthogonal-pair enumeration followed by a linear Goursat parametrization gives the formula and proves that the dimension bound is sharp.

The included `CHECK.py` enumerates RREF subspaces and tests the original associative multiplication, independently of Goursat classification, for eight field/dimension cases: \((r,q)=(1,2),(1,3),(1,4),(1,5),(2,2),(2,3),(2,4),(3,2)\). The last line of the observed successful execution was `GENERALIZED_HEISENBERG_SUBALGEBRA_OK`. The computed data appear in `RESULT.md`; direct exhaustive checks are finite evidence, not a proof for all \(r\) or \(q\).

Limitations: no verification over nonfields, no enumeration of integral suborders, and no external independent mathematical audit. Prior-literature comparison has publication-priority uncertainty, recorded in `AUDIT.json`.
