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

# Verification record

The explicit three-torus parametrization is an isomorphism because its three coordinates and inverse are regular Laurent expressions, and their compositions are identities. `verify.py` executes four exact symbolic algebra checks on forward coordinates and two exact inverse checks in the opposite direction. It was executed on the packaged working source using Python and SymPy and returned:

```
VERIFY_OK: forward and inverse formulas are mutual rational identities; F=4W
```

These identities verify the algebraic formulae. The geometric criterion that a full-dimensional torus in the complement implies a cluster-type log Calabi–Yau pair is Theorem 2.9 of Alves da Silva–Figueroa–Moraga; the source's Example 7.1 supplies the pair's log Calabi–Yau property. The checker does not independently prove these referenced results. Literature priority is evaluated from inspected sources and searches but cannot be guaranteed exhaustive.
