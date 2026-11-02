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

# Reproducibility and limits
Run `python3 CHECK.py` using Python 3.9 or newer. The checker requires only the standard library. It creates the twenty graph vertices as subsets of a five-element set, lists the thirty inclusion edges, and reconstructs the \(190\), \(540\), and \(375\) unordered cubical cells and both signed boundary maps.

A complete sparse elimination of the integer second boundary reduced modulo \(3\) yields rank \(340\). The independent topological upper bound \(340\) comes from eleven fundamental graph cycles of length at most ten, which each admit a stationary second particle; together these give an equivariant first-homology isomorphism over \(\mathbb Q\). The checker establishes connectivity and these cycle lengths. It then checks exact differential equivariance under every one of the \(240\) group elements, reconstructs all fourteen character values, uses rim-hook character orthogonality to recover each named Specht summand, and verifies rational quotient dimensions.

A successful run ends in `DESARGUES_B2_FULL_S5_C2_SPECHT_CHECKS_OK`. The rank lower bound modulo \(3\) is not on its own a rational rank equality; both bounds are needed and supplied. There is no claim of an integral Smith-normal-form computation or independent external verification.
