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
The proof starts from the classical Pluecker formulas
\[
D=d(d-1),\qquad F=3d(d-2),\qquad B=\frac12d(d-2)(d-3)(d+3).
\]
After dividing by \(d\), each pairwise gcd is reduced symbolically using consecutive-integer coprimality, reduction modulo \(3\), and a two-adic case split modulo \(4\).

The only possible common factor left by the normalized dual-degree and flex counts is \(3\). In the sole residue class where that factor occurs, the normalized bitangent count is nonzero modulo \(3\), proving that the normalized triple is primitive.

The bundled checker evaluates the exact formulas through degree ten thousand and verifies the triple gcd and all pairwise formulas. Finite computation is regression evidence only; the proof is the symbolic arithmetic reduction.
