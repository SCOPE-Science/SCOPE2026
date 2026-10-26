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
# Exact verification
Run `python3 verification.py` from the extracted scientific package. The standalone program checks polynomial arithmetic in \(\mathbb F_3[u]\) without external dependencies, including the exact product of the six factors, their Rabin irreducibility criteria, \(g\mid(u^{91}-1)\), separability, and comparison of the resulting Frobenius-orbit counts for several extension degrees. Its successful output is `VERIFY_OK factor_degrees=1,3,6,6,6,6 cycle_type=1^1 3^1 6^4 reduced=28`.

The universal tangent-intersection divisor and the correspondence of bitangents with hyperflexes are established symbolically in the proof in `RESULT.md`. Modular arithmetic checks do not replace those all-point geometric arguments. The polynomial verifier was executed successfully against the bytes of this package during preparation. Independent mathematical validation has not been performed.
