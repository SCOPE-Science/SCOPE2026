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

# Verification instructions
Run `python3 CHECK_HOMOLOGY.py` and `python3 CHECK_CHARACTERS.py` from the directory containing the embedded files. Both programs use only the Python standard library. The first checks mod-two reduced homology on seven complete finite instances. The second computes signed simplicial Lefschetz numbers for each element of four root-preserving automorphism groups: 8+12+48+72=140 instances, comparing against the monodromy-augmentation formula. Both scripts were executed successfully on their actual embedded paths.

These experiments verify finite instances and signed character predictions, not an unrestricted theorem or integral torsion-freeness. The unrestricted statements follow from the explicit link deformation and integral Mayer–Vietoris and join Künneth arguments in `RESULT.md`. No independent audit has been carried out.
