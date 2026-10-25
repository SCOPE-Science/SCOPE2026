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

# Verification details

Run `python verify.py` with NumPy installed. The program constructs the \(N\times M\) zero–one incidence array directly by enumerating finite field nonzero labels, the zero-divisor support, and coordinate-equality neighborhoods. Because only equality of nonzero coordinates matters, each field is represented by a set of \(q_i-1\) arbitrary labels plus zero; changing labels by negation is an independent row permutation of the graph. It computes the integer Gram matrix, its complete numerical eigenvalues, the exact theoretical eigenvalue multiset, rank, and edge-count trace.

The actual run completed with `SPECTRUM_VERIFY_OK 188 finite product sizes` for 188 tuples with two, three or four factors. Spot checks include \(\mathbb F_3^3\), producing the Gram multiset \(\{66,8,8,8,2,2,2,0\}\), and \(\mathbb F_3^4\), producing eigenvalues \(640\) once, \(26\) four times, \(8\) six times, \(2\) four times, and zero once. Floating diagonalization is checked against exact integer predictions with absolute tolerance \(5\times10^{-8}\) and rank tolerance \(10^{-6}\).

The parameter-family theorem does not rely on numerical diagonalization: its general proof follows from exact character orthogonality and finite support sums. The verifier does not independently establish priority and is not an exhaustive search over all ring families. Independent mathematical audit remains unperformed.
