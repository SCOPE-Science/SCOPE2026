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

# Computational verification and scope

The included `verify.py` uses only the Python standard library. It independently constructs the linear system for an unrestricted \(n\times n\) endomorphism \(D\) of the basis of \(N_n(k)\) to satisfy the derivation identity on every basis pair. For prime fields it computes the rank over \(\mathbb F_p\); for characteristic zero it computes the rank over \(\mathbb Q\) with exact fractions. It also substitutes every explicit homogeneous candidate generator into the original product and tests the Leibniz rule coefficient by coefficient.

Run `python3 verify.py` in the directory holding `verify.py`. The actual executed result was:

```
NOVIKOV_DERIVATION_CENSUS_OK positive_characteristic_cases= 65 characteristic_zero_cases= 7 extra_mod_four_cases=2
```

The modular cases cover all \(2\le n\le14\) for \(p\in\{2,3,5,7,11\}\). Characteristic zero covers \(2\le n\le8\). Further characteristic-two dimension checks cover \(n=16\) and \(n=17\), straddling the exceptional boundary. The program checks the true full linear system independently of the dimensions predicted by the abstract splitting argument; no floating-point arithmetic is involved. These finite tests do not prove the general formulas. The all-dimension proof and its exact hypotheses are in `RESULT.md`.

No full automorphism-group classification or computer-assisted infinite certificate is asserted. The verification does not assess publication priority or constitute independent external auditing.
