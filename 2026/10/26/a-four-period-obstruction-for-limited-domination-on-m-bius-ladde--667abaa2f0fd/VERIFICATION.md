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
# Reproducibility and checks

`verify_mobius.py` is a standalone Python 3 program requiring only the standard library. It compares an exhaustive search over all vertex subsets with an independently implemented exact transfer dynamic program for \(3\le n\le8\). The transfer represents the ladder as a two-row strip with boundary row-swapping and checks \(3\le n\le200\). It tests the closed formula at every tested size and tests the number of minimum sets whenever \(4\mid n\). The embedded `verification_output.txt` records actual execution.

The implementation checks the original vertex-neighborhood condition: every unselected vertex has at least one selected neighbor, and every selected vertex has at least two selected neighbors among its three. The transfer recurrence has no floating-point operations. The odd/even parity obstruction and the all-orders lower bound are proved symbolically in `RESULT.md`. Computation alone would not establish them beyond the tested orders.

No formal proof assistant or external audit was used, and the outputs are not represented as independent validation. The theorem does not claim exact enumeration of minimizers when \(4\nmid n\). Public source references are bibliographic evidence for comparison rather than certification of originality.
