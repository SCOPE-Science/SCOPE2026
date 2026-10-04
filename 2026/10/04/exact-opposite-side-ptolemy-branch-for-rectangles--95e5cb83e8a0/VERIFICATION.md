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
The proof was checked from the packaged formulas, not from numerical sampling.

The bundled `verify.py` symbolically confirms four identities used in the proof:

1. the square-root comparison
\[
\Phi_h(q)^2-(q^2+H^2-h^2)^2=4H^2h^2;
\]
2. the derivative of the reduced function with respect to \(v^2\);
3. the derivative of the final one-variable function;
4. the exact difference
\[
1+\frac{t^2}{4}-Q(t)^2=\frac{t^2}{4(t^2+1)}.
\]

The analytic sign conditions are stated in `RESULT.md`: \(0\le v\le u\le L\), \(H>0\), and \(t\ge2\) in the final comparison. The checker is diagnostic only and is not used to infer an infinite theorem from finite experiments.

Unproved here: the exact unrestricted Ptolemy constant of a rectangle and all side-occupancy classes other than two points on each of a fixed pair of opposite sides.
