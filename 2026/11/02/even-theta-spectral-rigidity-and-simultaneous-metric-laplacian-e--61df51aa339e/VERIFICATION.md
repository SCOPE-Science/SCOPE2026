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

# Reproducibility and scope

Run `python verify.py` with Python 3.10 or later and SymPy installed. The verifier builds the unweighted graph directly from the three defining paths, constructs its ordinary Laplacian, and compares the exact symbolic determinant with the proposed reflection-block factorization for every even \(r\in\{2,4,\ldots,24\}\). It independently computes exact polynomial greatest common divisors, root multiplicities, and all-pairs shortest paths. It checks that the small exceptional graphs admit a three-vertex resolving set but no two-vertex resolving set, and that \(\{a,w_1\}\) resolves for all tested larger even lengths. Every tested graph is bipartite.

Observed output ended:

`VERIFY_OK EVEN_THETA r=2,4,...,24 exact_spectral_factorizations, multiplicities, metric_bases`

The infinite-range result does **not** rely on these finitely many tests. The analytic steps are the symmetry decomposition, the two explicit continuants, the algebraic exclusion of common roots, and the direct formulas for distance pairs. No independent audit or external formal certification has been performed. No test is claimed for weighted graphs or arbitrary theta path-length triples.
