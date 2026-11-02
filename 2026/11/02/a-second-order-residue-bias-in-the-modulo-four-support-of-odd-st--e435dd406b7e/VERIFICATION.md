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

Running `python3 verify.py` with a standard Python 3 interpreter performs two independent finite arithmetic tests:

1. Expands the exact generating series \(\sum_{j\ge0}q^{2j+1}\prod_{h<j}(1+q^{2h+1})^2\) modulo \(4\) up to weight \(1400\). It checks all \(700\) positive odd indices against the source's prime-exponent support classification and the odd-coefficient square criterion.
2. Computes the exceptional indices \(1\le n\le40000\) by factorizing \(3n-1\), and separately by enumerating both disjoint prime-power-square parametrizations. It compares the sets, not just their cardinalities, confirms no duplicate representations, and checks all four residue classes.

Expected deterministic output:

```
VERIFY_OK coeffs_odd_n=700 direct_indices=20000 index_limit=40000 residues={1: 899, 3: 1138, 5: 893, 7: 954}
```

The program uses exact integer arithmetic and does not evaluate the analytic constants. In particular, finite verification cannot prove an asymptotic formula or exclude previously published equivalent coverage. The infinite results follow from the paper's coefficient-support theorem, the explicit proof in `RESULT.md`, and fixed-modulus prime number theory.
