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
# Reproducibility and limits

Run the included \(\texttt{verify\_f4\_tangent.py}\) under Python 3 with no third-party packages. It generates each of the \(349525\) nonzero ternary cubics modulo \(\mathbf F_4^\times\) by unique first-nonzero-one normalization, evaluates every form and gradient on every one of the \(21\) rational projective-plane points, computes all rational tangent-line covers, and checks the independent \(512\)-Hermitian-matrix census.

Observed output:

```text
total projective cubic equations: 349525
tangent filling (all cubics) by (points,smooth rational points): [((9, 8), 5040), ((9, 9), 280), ((10, 10), 6048)]
smooth cubic candidates: 280
non-Hermitian or singular Hermitian candidates: 0
nonsingular Hermitian matrices: 280
smooth non-filling nine-point cubic: 9 9 18
PASS
```

The finite census has explicit coverage of all normalized equations, and its correctness can be inspected/replayed. The geometric-smoothness conclusion uses the independent symbolic identity \(\nabla F_A=A^{\mathsf T}\mathbf X^{[2]}\) and invertibility of \(A\), not finite-degree point searches. Hasse–Weil for genus one bounds the rational-point number for smooth cubic candidates. Projective orbit and stabilizer use the standard nondegenerate Hermitian congruence theorem and finite unitary-group order. These are not independent external validations. No independent audit has been performed.
