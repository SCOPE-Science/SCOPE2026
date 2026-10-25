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

Run `python check.py` using Python 3 without external libraries. The program enumerates every matrix in each stated small finite-field instance, computes the actual commutator and nilpotency index, and checks the predicted number of commuting nilpotents and regular nilpotents for every nilpotent Jordan partition. For regular nilpotents, it independently evaluates every allowed polynomial in that matrix to count the fibers \(A=f(B)\). It does not infer general validity from finite enumeration.

Replayed result: `ALL_REGULAR_NILPOTENT_CENTRALIZER_CHECKS_PASSED shapes=18 nilpotent_centralizer_elements=5192 regular_pairs=3293 uniform_poly_fibers=31`.

Mathematical generality follows from the proof in `RESULT.md`: rank sequences of powers, standard finite-module endomorphism structure, Fine–Herstein nilpotent counts, and an exact centralizer-orbit fiber calculation. The original published articles and the independent-review channel are not reproduced or certified here.
