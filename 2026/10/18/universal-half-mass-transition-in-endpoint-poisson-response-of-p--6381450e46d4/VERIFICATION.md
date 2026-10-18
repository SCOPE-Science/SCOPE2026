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
# Verification notes

`verify.py` uses only the Python 3 standard library. It constructs full finite Laplacian matrices and their exact rational pseudoinverses, then checks the finite clique formula and the head-reduction coefficients. It independently enumerates all zero-sum cube vertices in the small tested dimensions to confirm that the optimized linear functional equals the median formula. It also checks the stated gap bound for path, cycle, star and clique heads, the exact uniform continuum approximation over several mesh sizes, and the limiting clique regimes. The reviewed run passed 2,271 comparisons.

To repeat, place `verify.py` next to this document and run `python verify.py`. For each graph, the zero-sum forcing domain consists of vectors with all coordinates between \(-1\) and \(1\); the graph Laplacian has unit conductances and the solution is normalized to zero vertex mean. The finite script cannot establish an infinite-family assertion or a literature-priority claim; both remain matters of mathematical proof and source inspection, respectively.
