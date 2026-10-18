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

# Reproduction

Run `python3 verify.py` with a standard Python 3 interpreter, without dependencies. It implements perfect edge domination directly from its definition and checks the explicit code construction independently of the symbolic proof. Exhaustive enumeration checks all \(16\) edge selections on \(Q_2\), all \(4096\) on \(Q_3\), and all \(512\) potential one-parity center sets on \(Q_4\). A direct edge-level test validates constructions for dimensions \(2,4,8\). The program returns `All checks passed.` when all assertions hold.

The unrestricted result is established in RESULT.md by the square obstruction to yellow–yellow and black–black edges, exact bipartition, divisibility and syndrome-code converse. Computational checks cannot establish a statement for all dimensions, exclude unexamined literature or constitute an independent external audit.
