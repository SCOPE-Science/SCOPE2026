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

The proof was checked in four independent layers.

1. Equality data are global: an \(r\)-tuple determines a set partition of the variable indices. Choosing \(t\) blocks that coincide with distinct parameters gives exactly \(\binom bt(m)_t\) possibilities.
2. After pinning, \(s=b-t\) new labeled blocks remain. In one named order there are exactly \((m+s)!/m!=(m+1)^{\overline s}\) linear extensions of the fixed parameter order; the generic age lets the \(n\) orders vary independently.
3. Quantifier elimination turns those finite diagrams into complete types, so no additional first-order identifications occur.
4. The dp-rank upper bound is forced by the resulting \(O(m^{nr})\) type growth, while the lower bound is witnessed by \(nr\) pairwise-inconsistent interval rows with arbitrary cross-row choices realized by the finite-extension property.

The bundled `artifacts/verify.py` performs a separate finite replay: it directly enumerates equality partitions, parameter pinning maps, and order-extension permutations for small \(m,n,r\), compares the result to the formula, and checks the displayed low-dimensional polynomials. Expected final output: `VERIFY_OK`. Finite enumeration is not used as proof of the infinite dp-rank statement.
