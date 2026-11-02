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

# Computational verification and boundaries

Running `python artifacts/check_windmill.py` with SymPy and NumPy gives:

```text
PASS: exact 3x3 and 5x5 characteristic polynomials, three completed-square optimizations, and all pair-type sharp optimizers for 1..8 petals.
```

The test explicitly constructs skew adjacency commutators and verifies their characteristic polynomials algebraically, independent of floating-point tests. Direct singular-value computations for one through eight petals verify the displayed extremal functions at each available pair type. Exhaustiveness over arbitrary petal count is established in the analytical restriction/extension proof, not claimed from finitely many evaluations. The arguments also require the precise unweighted adjacency-Dirac convention.
