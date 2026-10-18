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

# Exact verification

Run `python3 verify_paley13_ind2.py` using Python \(3.10\) or newer. This verifies the actual labeled graph and simplex rule. The enumerator tests all \(8192\) subsets by induced degree and a separate connected-component traversal, verifies every lower face lies in a tetrahedron, constructs the complete signed integral boundary matrix, and uses integer row/column operations with explicit unit pivots. It also checks the triangular presentation of \(\pi_1\) by eliminating all \(66\) generators and checks \(\partial_2\partial_3=0\).

Expected mathematical invariants: \((f_0,f_1,f_2,f_3)=(13,78,143,78)\); \(78\) tetrahedral facets; triangular-relator closure \(33\to66\) generators killed; integral third boundary with \(76\) unit invariant factors and \(2\) zero columns; reduced homology \(\widetilde H_2\cong\mathbb Z\), \(\widetilde H_3\cong\mathbb Z^2\), all other reduced integral homology zero. The exact homotopy consequence follows from the simply connected two-skeleton and the integral three-cell attaching map, as justified in `RESULT.md`.

Checks do not establish results for different Paley graph orders or independence parameters. The code uses no probabilistic searches and no external certificate or mathematical package. Publication priority and external audit have not been certified.
