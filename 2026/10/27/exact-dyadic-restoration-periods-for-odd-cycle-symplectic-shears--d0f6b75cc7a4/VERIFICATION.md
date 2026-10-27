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

The self-contained `verify.py` checks the exact finite-modulus periods for odd circumferences 3 through 25 and dyadic exponents 1 through 10, using cyclic Laurent polynomial matrices and exact integers. It tests each predicted exponent, each possible proper prime divisor, the mod-four projector identity, the mod-eight order plateau, and nonidentity modulo sixteen. It executed successfully with output `VERIFY_OK odd_cycle_lengths=12 moduli=1..10 checks= 416`.

The uniform all-odd-length theorem is established by the characteristic-two splitting argument, exact Laurent-polynomial congruence modulo four, idempotence modulo two, and a two-adic lifting lemma; finite tests are corroboration. Other graph couplings, even circumferences, non-dyadic moduli and primitive point-orbit statistics are not verified.
