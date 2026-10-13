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

The accompanying dependency-free `check.py` computes the degree-\(N-4\) component of the Chern-class quotient as an exact integer bivariate polynomial, integrates it by Schubert alternant extraction and independently by localization with rational arithmetic at distinct weights \(0,1,\dots,N-1\). It checks \(N\in\{6,8,10,12\}\), normalizes the top Schubert class, and constructs each full Betti table and primitive middle rank. Running it during this assessment yielded `GRASSMANNIAN_CY_BETTI_EXACT_OK`.

Uniform correctness does not follow from checking these four values alone; the all-even-\(N\) argument is the exact bundle identity, Schubert integration, Gauss–Bonnet, weak Lefschetz and Poincaré duality in `RESULT.md`. No computer algebra library, external artifact, unexamined path or numerical approximation is needed. No external or independent audit has been performed.
