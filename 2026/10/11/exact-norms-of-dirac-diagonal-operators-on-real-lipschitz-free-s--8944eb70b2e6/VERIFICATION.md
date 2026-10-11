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

# Reproducibility and proof limits

`verification/dirac_multiplier_checker.py` uses only standard Python 3 and exact rational arithmetic. Its direct enumeration of all line-intersection vertices was compared with the asserted antipodal three-pair formula for 7000 choices of integral triangle distances and integer symbols. The final line was `DIRAC_MULTIPLIER_LOCAL_EXACT_OK 7000`.

`verification/global_lp_stress.py` uses Python 3 and SciPy to solve both signs of the full global Lipschitz linear program for 720 deterministic randomly generated connected shortest-path metrics with 3--8 points and varied real symbol values. The final line was `DIRAC_MULTIPLIER_GLOBAL_LP_OK 720`.

The global tests are finite numerical linear programs, not infinite-metric proofs and not formal certificates. The general claim is established by the molecule norming description, McShane extension, and explicit extremal evaluation on a three-point Lipschitz polytope. Failure of any numerical solver would not imply a counterexample. Proof assumptions and the treatment of bounded versus unbounded maps appear in `RESULT.md`.
