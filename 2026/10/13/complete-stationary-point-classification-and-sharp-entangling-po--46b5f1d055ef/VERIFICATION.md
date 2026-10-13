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
# Reproducibility and verification

Install the dependency declared in `requirements.txt`, then run `python verify_spin1.py` from the extracted package directory. This command was executed against the actual packaged verifier and returned `VERIFY_OK`.

The verifier constructs the \(9\times9\) spin-one tensor Hamiltonian from its raising, lowering and diagonal spin operators. Exact rational/symbolic arithmetic checks that its three spectral projectors are orthogonal idempotents with ranks \(1,3,5\) and sum to identity. It computes the realignment and partial-transpose fourth moments, checks the six-term trigonometric phase formula exactly as a Laurent polynomial, verifies the phase-alignment root-exclusion factorization, and tests exact stationary values/Hessians and their periodic companions.

The program verifies explicit identities and does not by itself establish the absence of other stationary points. That inference rests on the analytic sign argument in `RESULT.md`: at every noncorner critical point the necessary polynomial difference would have to be zero, whereas all three factors on the right of its displayed factorization are strictly positive on \([-1,1]\). Likewise, global extremality requires the analytic exhaustion and compactness argument, not finite sampling. The full phase formula was also independently published in the cited earlier literature. This package has undergone self-review only; independent audit has not been performed.
