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

# Exact arithmetic verification

The companion file `verify_klein_flex_tangents.py` is a complete, standalone Python 3 program requiring only the standard library. Executing `python3 verify_klein_flex_tangents.py` produced `VERIFY_OK`.

The program reconstructs all 24 Klein flex points in \(\mathbb Z[\zeta_7]\) and checks both the quartic and normalized Hessian equations. It checks tangency, performs the integral tangent-vector normalization, and tests **all** \(2024\) unordered line triples. Each integer norm is computed as a six-by-six exact multiplication-matrix determinant using Bareiss elimination. The resulting nine-value norm distribution, recorded in RESULT.md, has prime support only \(\{2,7\}\). It therefore gives a universal good-prime nonconcurrence proof, not a sampled-prime heuristic.

The program then applies every one of the six Galois automorphisms \(\zeta_7\mapsto\zeta_7^a\), determines the corresponding exact permutation of the 24 tangent lines, and counts the fixed unordered pairs. It confirms the 276-point orbit distribution \(1^{\times3},3^{\times7},6^{\times42}\), and fixed-pair counts \(276,3,3,3,3,24\) for \(a=1,2,3,4,5,6\). The Frobenius theorem and Dirichlet densities follow mathematically from this complete action.

The verifier is an exact finite certificate, not an external formal certification. Its arithmetic logic and the Bézout/smoothness reductions still require ordinary mathematical scrutiny. No independent audit has been performed, and no claims are made in characteristics two, three or seven.
