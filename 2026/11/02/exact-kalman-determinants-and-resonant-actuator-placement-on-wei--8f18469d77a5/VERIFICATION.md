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

# Reproducibility of the weighted-fan theorem

`verify_fan.py` is dependency-free Python. Execute `python3 verify_fan.py` in the extracted package to reconstruct the graph Laplacian, Krylov matrices and exact determinant and PBH rank comparisons. One source-package replay reported `PASS 30141 finite exact and supplementary checks`.

Exact rational calculations use integer-scaled weighted adjacency/Laplacian entries, fraction-free Bareiss determinants, and rational Gaussian elimination. For integer-scaled Laplacian \(bL_n(a/b)\), the homogeneity of the square Krylov determinant is \(b^{n(n+1)/2}\); the verifier explicitly removes this factor before comparing to the claimed formula. Tests include the hub, all path locations, rational spoke values, and true rational collision cases; zero-mode and pair gcd criteria are checked at additional sizes.

**Scope of verification.** These are finite checks. The exact theorems for every \(n\ge3\) and \(t>0\) are proved analytically by orthogonal decomposition, Chebyshev polynomial products, modular arithmetic, and PBH. The checker does not certify inaccessible literature, novelty, least-energy controllability, arbitrary independent spoke weights, or any independent audit. The included input is source text and can be rerun without internet access.
