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

Execute `python3 verify.py` in a directory containing the standalone program from this package. The program uses only the Python standard library. It constructs multiplication in prime and quadratic-extension fields, builds each adjoint matrix from the actual Lie brackets, computes centralizer kernels by full finite-field row reduction, enumerates all commuting ordered pairs from these kernels, and counts commuting ordered triples by computing the common centralizer of each pair. It does not use the closed formula when constructing its matrix kernels. Its separately computed totals are compared with the claimed formula.

Observed complete counts:

| Field | Ordered commuting pairs | Ordered commuting triples |
|---|---:|---:|
| \(\mathbb F_2\) | 10 | 22 |
| \(\mathbb F_4\) | 76 | 316 |
| \(\mathbb F_3\) | 105 | 339 |
| \(\mathbb F_9\) | 7281 | 66249 |
| \(\mathbb F_5\) | 21625 | 186125 |

Expected marker: `WITT_ALL_ARITY_POINT_COUNT_OK`.

The computation establishes only these finite instances and the direct single-element adjoint-nullity spectra checked along the way. The proof in `RESULT.md` supplies the infinite-field-family and arbitrary-arity argument. No independent audit has been performed.
