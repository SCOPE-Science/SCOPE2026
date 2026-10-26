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

# Reproducibility checks and boundaries

Run `python3 verify.py` in a Python 3 environment with SymPy installed. Output on the checked copy was:

```
VERIFY_OK cases=45 integer_snf=28 prime_rank_comparisons=180
```

The program constructs all multiset-deletion multiplicity matrices and interlacing binary matrices directly for \(1\leq r\leq n\leq9\), checks balanced integer margins and the specified unit-triangular binary minor, and computes row ranks over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\). For \(n\leq7\), it computes true integer Smith normal forms with SymPy and compares prime-power-combined invariant factors to the proposed diagonal decomposition.

Finite computations do not prove the infinite theorem. The general proof uses two exact integral transformations, whose correctness can be checked without executing code: (1) a lexicographically unit-triangular maximal minor for the binary relation; (2) an invertible integral linear coordinate change on every homogeneous polynomial degree turning the deletion derivation into one coordinate derivative. At \(r=n\), the direct one-by-one matrices are \([n]\) and \([1]\); at \(r=1\), all empty-multiset and maximum-symbol conventions are included.

An independent mathematical audit has not been performed. The claim does not extend to arbitrary balanced weightings, and priority cannot be certified solely by absence of search matches.
