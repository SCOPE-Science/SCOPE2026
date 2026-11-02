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

The standalone Python 3 verifier `verify_clebsch_nonsplit.py` requires only the standard library. It reconstructs all fifteen rational coordinate-pairing lines, enumerates the prime-field projective surfaces for \(p\in\{7,11,13,17,19\}\), checks the fifteen-line union multiplicities and exact rational intersection Gram rank, and reconstructs the twelve additional Fourier lines over \(\mathbb F_{11}\).

Observed results: for \(p=7,11,13,17,19\) the surface counts are respectively 85, 199, 235, 375, 495, and the fifteen-line union counts are 85, 145, 175, 235, 265. The nonsplit prime examples \(7,13,17\) give the line-free counts 0, 60, 140, exactly \((p-3)(p-7)\). The fifteen-line intersection Gram rank is six. In the split control case \(p=11\), the twelve Fourier lines are distinct and all 27 lines cover the rational surface.

The all-prime-power mathematical conclusion relies on the written algebraic proof, not an extrapolation from these enumerations. No check was made in the excluded characteristics, nor is an independent audit claimed.
