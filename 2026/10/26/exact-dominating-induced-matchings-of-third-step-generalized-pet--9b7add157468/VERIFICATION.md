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

## Claim and proof checks

The proof reduces a dominating induced matching of \(\operatorname{GP}(n,3)\) to two families of binary vertex equations. Their Fourier determinant is checked by exact polynomial multiplication, and its non-fifth-root factor is excluded from roots of unity by irreducibility modulo two and the complete list of degree-four cyclotomic polynomials. That rules out all aperiodic solutions for arbitrary \(n\), without inferring an infinite claim from a finite scan.

## Executed standalone files

1. `verify_polynomial.py` -> `verify_polynomial.out` confirms the exact polynomial identity and exhausts all 32 five-column patterns; five survive.
2. `verify_edge_cover.py` -> `verify_edge_cover.out` independently enumerates dominating edge-neighbourhood exact covers for every \(7\le n\le50\), confirming the count of zero or five.
3. `verify_coloring.py` -> `verify_coloring.out` independently enumerates admissible cyclic outer colour words and checks all inner equations for every \(7\le n\le32\), confirming the same count.

Each script uses Python 3 standard-library facilities only. Its output is preserved separately, and its assertions reject discrepancies.

## Limits

All-order correctness rests on the mathematical argument in `RESULT.md`; finite tests are corroboration. External independent review and independent validation have not been performed. Literature comparison does not establish global publication priority and is subject to unindexed-source risk.
