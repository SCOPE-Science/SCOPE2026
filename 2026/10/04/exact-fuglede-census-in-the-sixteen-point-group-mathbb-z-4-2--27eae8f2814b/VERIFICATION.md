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
# Verification
The bundled `verify.py` uses only Python's standard library. It represents \(1,i,-1,-i\) as integer pairs, so every Fourier zero decision is exact. It enumerates every nonempty subset of \(\mathbb Z_4^2\), every normalized spectrum or tiling-complement candidate of an admissible size, and all affine maps induced by the \(96\) invertible \(2\times2\) matrices over \(\mathbb Z/4\mathbb Z\) and \(16\) translations.

The reviewed replay returned:

`VERIFY_OK total=2155 size_counts=16,120,1244,774,1 affine_orbits=1,2,8,7,1 GL2Z4=96`

The verifier proves only this finite group statement. It does not extrapolate the result to other moduli or dimensions.
