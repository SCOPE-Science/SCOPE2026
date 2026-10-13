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

The theorem bounds classical unequal-degree-pair NODF for binary ecological interaction matrices containing exactly three rows, \(n\ge4\) columns, precisely \(n+2\) interactions, and no zero row or column.

The proof directly checks the exhaustive column-degree-excess split into either one degree-three column or two degree-two columns. The latter case separates the two possibilities of intersection size one or two. Equality can occur only when every degree-one column meets the common row of the two distinct degree-two columns, yielding the claimed single optimum shape and count \(3n(n-1)\).

The embedded script `verify_sparse_nodf.py` uses only the Python standard library and exact rational arithmetic. For every \(2\le n\le7\), it generates every admissible matrix and calculates the NODF numerator by two independently implemented methods: bitmasks and set intersections. Their scores are checked for exact equality for all \(63{,}906\) matrices. The script checks the maximum and equality shapes for \(4\le n\le7\), validates the stated Ferrers comparison, and tests the symbolic inequalities through \(n=100\).

Run:

`python3 verify_sparse_nodf.py`

Its first output line must be `VERIFY_OK`.

Finite enumeration is not treated as a proof of the infinite family. The universal result relies on the structural case proof. No external audit or independent validation has been performed.
