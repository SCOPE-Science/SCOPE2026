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

Run `python3 verify.py` with Python 3. The script uses only the standard library.

It independently implements the descendant definition for binary length-four words, scans every subset of the 16-word space, and recomputes the maximum size and every maximum code. It then checks the five normalized forms containing 0000, equality with the full translation orbit of the canonical representative, the Hamming-distance profile, the XOR index, and the orbit/stabilizer under all 16 translations and 24 coordinate permutations.

Expected final line:

`VERIFY_OK vertices=16 maximum=5 labeled_maxima=16 normalized_maxima=5 translation_orbit=16 natural_group=384 stabilizer=24 hamming_profile=2x6,3x4 xor_index=true maxima_sha256=243c8672229ef0d1ab8c6599b28cebfcf77356c939433924a2f0647c4c1a5145`
