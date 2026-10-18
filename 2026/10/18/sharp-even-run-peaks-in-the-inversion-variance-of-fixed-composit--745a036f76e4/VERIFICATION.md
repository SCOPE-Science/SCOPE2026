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

Run `python3 verification/verify.py` under Python 3 with no dependencies beyond the standard library. The observed execution returned `136004 exact assertions passed`.

The checker exhausts all fixed-composition binary words with symbol counts each from one to eight. It verifies each conditional mean, each variance and each feasible run-stratum size against its rational formula. For symbol counts through twenty-three it separately computes projected staircase-matrix second moments from the independent-composition identity. For counts through thirty-nine it checks the three gap factorizations and their positive signs.

All rational comparisons are exact. These computations do not certify infinitely many pairs of counts: the mathematical proof rests on the uniform-composition moment identity, projection norms, orientation weighting and positive algebraic factorizations in the accompanying proof. Earlier literature can contain implicit consequences not resolved by finite computation or keyword searching. No independent audit or external validation was conducted.
