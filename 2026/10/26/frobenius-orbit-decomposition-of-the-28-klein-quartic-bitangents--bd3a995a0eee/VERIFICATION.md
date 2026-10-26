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

# Exact reproduction

Run `python klein_bitangent_verify.py` in an environment with SymPy. It recomputes the exact elimination, modular factor irreducibility, squarefreeness, unique rational pair and rational line identity. Expected last line: `VERIFY_OK; irreducible orbit degrees 1,3,6,6,6,6; GF5 bitangent (u,v)=(-1,-1)`.

The computational certificate is finite and exhaustive: degree-28 separable eliminant roots, nonvanishing leading coefficients and the independent algebraic theorem of 28 bitangents together prove completeness. It does not certify originality or perform an independent audit. Source comparisons are recorded separately in the review metadata.
