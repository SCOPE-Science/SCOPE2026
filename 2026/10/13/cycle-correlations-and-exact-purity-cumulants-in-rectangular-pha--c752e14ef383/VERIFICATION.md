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

# Reproducibility and exact checks

The theorem is proved analytically using Haar phase orthogonality; finite verification is only a consistency check. Run `python3 artifacts/verify.py` with Python 3 and the standard library. The checker creates zero-frequency Laurent coefficients for the centered purity and obtains second and third moments using integer arithmetic and exact rational normalization. It tests dimensions \((2,2)\), \((2,3)\), \((3,2)\), \((3,3)\), \((3,4)\), \((4,3)\), as well as the full centered product over triangles and four-cycles for \(m=2,3\). All required equalities are strict integer or rational comparisons; no tolerance, Monte Carlo approximation or external dependency is used.

The exact count check is bounded to those specified dimensions, and it neither enumerates all dimensions nor certifies originality. The closed-form claims for arbitrary \(d,m\ge2\) depend on the written torus-coordinate proof and all-cycle phase-balance argument, not on extrapolation from the checker. There is no claim of a central limit theorem or of independent external validation.
