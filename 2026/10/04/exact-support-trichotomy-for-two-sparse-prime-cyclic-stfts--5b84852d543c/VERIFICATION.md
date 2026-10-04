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

The proof was replayed at the level of translation rows. For each \(x\), the row \(V_gf(x,\cdot)\) is the Fourier transform of \(f\overline{T_xg}\). Two-point supports give either four one-point intersections or three intersections of sizes \(1,2,1\). In the latter case the only possible Fourier zero comes from a two-term polynomial, and multiplication by the nonzero support difference permutes the \(p\)-th roots of unity.

The accompanying `verify.py` constructs the STFT directly for every pair of two-point supports for \(p\in\{5,7,11,13\}\). For unaligned support differences it verifies support \(4p\). For aligned differences it tests a generic equal-coefficient choice with support \(3p\) and a sign choice satisfying the root-of-unity condition with support \(3p-1\). It also verifies explicit witnesses for all three values. The script prints `VERIFY_OK`.

The finite replay is not used as proof of the universal classification. It checks the formulas and boundary examples against direct STFT computation.
