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

# Finite mathematical verification

Run `python3 verify_cube_matching.py` from this directory with Python 3 (standard library only). The code builds the ordinary matching complex from the cube edge list, including the empty face; checks the augmented face vector and the four binary boundary ranks; verifies all signed integer double-boundary cancellations; reconstructs all \(48\) graph symmetries; evaluates their signed Lefschetz traces; and checks the character decomposition into \(\mathbb Q_\varepsilon\) and the inflated three-dimensional \(S^{(2,1,1)}\).

Observed results from the packaged program:

```text
EXACT_RATIONAL_HOMOLOGY_VERIFIED [1, 12, 42, 44, 9] [1, 11, 31, 9]
ALL_48_SIGNED_LEFSCHETZ_TRACES_VERIFIED
FULL_S4_TIMES_C2_MODULE_VERIFIED {"('(4)', 1)": 1, "('(2,1,1)', 0)": 1}
CENTRAL_INVERSION_TRACE_VERIFIED 2
QUOTIENT_H2_INVARIANTS_VERIFIED {'full_group': 0, 'even_flips': 1}
ALL_CUBE_MATCHING_SYMMETRY_CHECKS_PASSED
```

The proof converts modular rank lower bounds to exact characteristic-zero ranks using \(\partial^2=0\) and dimension upper bounds. The finite verifier does not claim an integral homology lattice classification, infinite-family result or independent external audit.
