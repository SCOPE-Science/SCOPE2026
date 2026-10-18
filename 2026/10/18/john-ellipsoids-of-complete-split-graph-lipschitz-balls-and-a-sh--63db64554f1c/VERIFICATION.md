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

# Finite exact checks and proof dependencies

The standalone `verify.py` is written entirely in the Python standard library and uses `fractions.Fraction` (no floating-point tolerances). Invoke `python3 verify.py` in the folder containing this document. It completed with the output:

```
EXACT_CHECKS_PASS parameter_pairs= 342 cross_edges= 43263 screened= 136 boundary_tangent= 17 active= 189 matrix_identity_cases= 42
```

The script checks the proposed exact weights, total design mass, edge-support bounds, and eigenvalue identities for every parameter pair with \(3\le p\le20\), \(2\le q\le20\). It independently constructs full ambient-space projection and Laplacian matrices for \(42\) pairs with \(p,q\le8\), verifying \(dSL=I_H\) as an exact matrix identity. It also checks the two-constraint stationarity equations with their nonnegative boundary multiplier.

The universal mathematical proof does not rely on the finite enumeration. Its nonstandard steps are the explicit two-orbit edge weights, spectral decomposition of their weighted Laplacian, exact tangent inequalities, determinant-versus-trace extremality for *all* translated ellipsoids, and strict comparison with the bipartite reference. These are supplied in RESULT.md. No mechanized infinite proof, independent scientific audit, or external certification was performed.
