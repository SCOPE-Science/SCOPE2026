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
# Reproduction and limits

Run `python3 verify_chord.py` from the same directory as this file. The script uses only the Python standard library. The actual run returned `ALL_RIGHT_LUNE_SECTION_LAW_CHECKS_PASSED`, with 240,000 Gaussian-derived isotropic plane normals; sample mean was 1.57029013 and theoretical mean is 1.57079633. The program checks the derived CDF against a one-dimensional integral, derivatives and symmetry, and compares 120 independent section lengths with a separate angular clipping calculation on each great circle.

The proof is independent of finite empirical checks. The only excluded section orientations have zero Haar measure. No external or independent audit was performed; historical priority is provisional. The test cannot establish the absence of older identical results.
