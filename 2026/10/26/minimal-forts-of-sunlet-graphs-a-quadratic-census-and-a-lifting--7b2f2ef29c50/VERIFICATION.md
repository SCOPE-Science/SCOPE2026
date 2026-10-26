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

Running `python verify.py` under Python 3 reproduces `verification_output.txt`.

The direct routine constructs \(C_n\circ K_1\) as a graph, checks the original outside-vertex fort condition on all \(2^{2n}-1\) nonempty subsets for \(3\le n\le9\), and filters inclusion-minimal sets by containment. It independently generates canonical supports and checks equality of the entire collections, rather than comparing only totals. Those tests cover exactly 349,497 subsets and confirm counts \(6,6,15,14,28,26,45\).

For \(10\le n\le18\), a separate exhaustive rim-support test evaluates the connected-support property for all \(2^n-1\) nonempty \(X\) and compares the predicted count. The direct six-cycle source comparison independently verifies the fort predicate for both the lifted configuration and its strict subfort and checks all proper subsets of the proposed original cycle fort.

These finite checks do not prove the unrestricted theorem. The mathematical justification is the canonical-leaf lemma, the component-union criterion, and counting intervals in the step-two cyclic order in `RESULT.md`. No expert or independent validation was performed.
