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

# Verification of uniform bulk moments

The exact probability construction, moment calculations, uniform Stirling estimate and fixed-part probability limit are proved in `RESULT.md`. The accompanying `verify_bipartite_covariance.py` separately reconstructs the actual convex hull from complete extreme-potential lists and star-triangulates its boundary. It evaluates the volume and all entries of the zero-sum Euclidean covariance using rational simplex integrations.

The original run executed `python verify_bipartite_covariance.py` from the same source subsequently embedded in the package, with Python 3 and SciPy available. It printed `PASS` for each of eight configurations: \((p,q)=(2,2),(2,3),(3,2),(3,3),(2,4),(4,2),(3,4),(4,3)\), and ended with `EXACT_BIPARTITE_BULK_MOMENTS_PASS 8 cases`. Every resulting equality was an exact integer/rational comparison. Floating-point methods select the hull simplices; the determinants, volumes, and moment evaluations do not rely on floating point.

The program does not provide an exhaustive verification for unbounded dimension or an independent audit. In particular, these eight cases are evidence of consistency only; the proofs in `RESULT.md` carry the arbitrary-dimensional conclusions. Public publication dates and nearby mathematical statements were compared in primary sources; an unindexed equivalent formula remains a bibliographic risk.
