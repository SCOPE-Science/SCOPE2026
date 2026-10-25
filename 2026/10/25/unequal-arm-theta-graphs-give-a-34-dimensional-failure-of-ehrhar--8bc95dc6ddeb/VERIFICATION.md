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

# Reproducibility checks

The included `verify.py` is a standard-library Python 3 program. It uses exact integer binomial coefficients and a separate exhaustive enumeration of binary orientation words and deleted-edge locations to reconstruct the spanning-tree activity polynomial. Run `python verify.py` in this directory.

The file actually executed successfully and printed `EXACT_OK dimension=34 gamma_15=-236544`. Checks include the candidate \((6,8,8,8,8)\), the equal-arm benchmark \((8,8,8,8,8)\), four smaller equal- and unequal-arm cases, and all five placements of the short path. It confirms the full 18-term gamma vector, \(h^*\) palindromicity, the first Ehrhart numerator coefficient \(42\), the coefficient-sum identity, and the exact equal-arm \(\gamma_{16}=-9799680\) reported by Ferroni.

The proof of the general finite-sum formula requires the facet-parity argument, the planar-dual spanning-tree dissection, and the Kálmán--Tóthmérész activity theorem. The finite computational comparisons do not establish any separate all-dimensional claim. Scientific priority and independent validation have not been certified.
