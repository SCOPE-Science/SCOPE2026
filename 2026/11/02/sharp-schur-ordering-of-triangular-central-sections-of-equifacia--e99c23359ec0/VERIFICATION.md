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
# Reproducibility and verification

Run `python3 check_sections.py` with Python 3. The accompanying script has no nonstandard Python dependencies and uses a fixed seed for reproducibility. The actual package script was extracted and executed; output:

```
SPHERICAL_EDGE_CROSSING_AND_ARCSINE_IDENTITIES_PASSED 1000
CENTRAL_SECTION_AND_HALF_NORMAL_TRIANGLE_EQUIVALENCE_PASSED 12000
STRICT_SCHUR_BALANCING_AND_UNIQUE_REGULAR_BENCHMARK_PASSED 10000
NONDEGENERATE_HESSIAN_AND_UNIVERSAL_BOUNDARY_CUSP_PASSED
INDEPENDENT_HAAR_NORMAL_MONTE_CARLO_PASSED 4x80000
ALL_CHECKS_PASSED
```

These checks compare the scalar-product angle formula to the arcsine expression on 1000 random parameter triples, the two exact geometric and Gaussian sign criteria on 12000 further triples, 10000 nontrivial pairwise balancing operations, and the local expansions. A separate direct Haar-normal Monte Carlo samples 320000 orientations for four shapes. Finite checking cannot establish the strict inequality for all shapes, the asymptotic statements for arbitrary small parameters, or novelty. Those conclusions rest on the written proof and literature comparison.

No independent audit has been undertaken. 
