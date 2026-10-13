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

# Exact symbolic check

Execute `python verify.py` after installing the Python dependency from `requirements.txt` (SymPy). The program constructs every graph \(K_n\) with \(t\) pairwise disjoint edges removed, forms the line graph adjacency relations from intersecting base edges, and calculates the exact integer Laplacian. For every integer \(n\in\{4,5,6,7,8,9\}\) and \(0\le t\le\lfloor n/2\rfloor\), it compares all coefficients in the direct characteristic polynomial with the derived factorization after polynomial cancellation. It additionally compares the Kirchhoff cofactor determinant for instances having no more than 26 line-graph vertices, and the characteristic-polynomial derivative for all tested instances, against an independently evaluated weighted incidence spanning-tree expression.

The actual completed run reported:

`VERIFY_OK cases= 24 orders=4..9 all_matching_sizes=0..floor(n/2)`

This finite check is exhaustive only within the stated 24 graph parameters and is **not** an exhaustive check for all orders. The displayed unrestricted theorem requires the symbolic determinant decomposition and discriminant proof in `RESULT.md`. No machine-formal proof or independent validation is asserted.
