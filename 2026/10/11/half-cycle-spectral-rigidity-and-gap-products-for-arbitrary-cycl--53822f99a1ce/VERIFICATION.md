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

# Verification of half-cycle Fourier concentration

The exact proof consists of the finite Fourier geometric-sum identity, the off-diagonal Cauchy form of the centered compression, the Cauchy determinant's nonvanishing for all distinct roots, singular-value pairing, and Cauchy--Binet. These steps prove the theorem for every integer \(N\ge1\) and every nonempty frequency mask.

The included standalone numerical checker `verification.py` is run with `python verification.py` and requires NumPy. It reconstructs every matrix from the original Fourier sum, not from the chord-product prediction. It checks every nonempty mask for \(N=1,2,3,4\) and 120 deterministic pseudorandom masks for each of \(N=5,6,7\). Executed result:

`VERIFY_OK exhaustive_n=1..4 random_n=5..7 checks=696`

The checker compares the exact predicted multiplicity with a numerical tolerance of \(10^{-9}\), verifies spectral pairing, and checks the product of the noncentral gaps against the independently evaluated chord products. Numerical tolerances and finite enumerations do not establish any asymptotic or all-size theorem; correctness rests on the proof in `RESULT.md`. The 1984 Xu--Chamzas source was not available in complete readable form during literature comparison, so the corresponding historical originality risk is not closed. Independent audit has not been performed.
