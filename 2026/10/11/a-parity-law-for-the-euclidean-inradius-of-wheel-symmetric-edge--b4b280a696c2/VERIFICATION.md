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
The theorem is proved symbolically in `RESULT.md`; the finite checker is corroborative.

Source-dependent checks:
- The primary source defines the polar Lipschitz polytope through edge-difference inequalities.
- Its general facet theorem represents facet normals by integer vertex labels modulo constants.
- Its wheel subsection fixes the cone label to \(0\) and gives the complete cyclic ternary facet criterion: no adjacent opposite signs and no cyclic \(000\).

Mathematical checks:
- Centering labels with \(p\) plus signs and \(q\) minus signs gives squared norm
  \[
  p+q-\frac{(p-q)^2}{m+1}.
  \]
- If both signs occur, at least two zero labels are necessary on a cycle.
- For fixed nonzero count, balancing \(p\) and \(q\) maximizes the norm.
- The optimal mixed-sign value with exactly two zeros strictly exceeds the unconstrained best one-sign value for every \(m\ge5\).
- Equality therefore forces exactly two transition zeros and one block of each sign, yielding the stated parity-sensitive contact counts.

`verify.py` enumerates every ternary outer labeling through \(m=11\), checks the wheel constraints and facet condition, and compares the exact rational maxima and maximizing-word counts with the theorem. It does not replace the arbitrary-\(m\) proof and does not assess originality.
