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

# Verification record

The proof is a universal symbolic argument and does not rely on finite experiments. The accompanying stand-alone `eulerian_tame_verify.py` can be executed with `python3 eulerian_tame_verify.py`. It independently constructs the Eulerian polynomials from their recurrence and tests the prime-block congruence and a full coprime-factor Hensel correction modulo \(p^2\). It also checks the exact unit-residue label of the distinguished local factor.

Actual executed ranges: \(p\in\{3,5,7,11,13\}\) and every \(0\le t\le p-2\), giving 34 complete cases. The verifier returned `VERIFY_OK full_prime_blocks= 34 including_first_Hensel_lifts_mod_p2`; one factor has degree \(p-1\) and the other degree \(t\) in each case. The code uses the Python standard library, integer arithmetic, and modular polynomial division, not floating-point approximations.

The script is not an independent mathematical audit. It tests modulo \(p^2\) and cannot establish higher-precision Hensel lifting, field nonisomorphism, or universal exhaustiveness; those claims follow from the explicit mathematical proof in `RESULT.md`. No external certification was performed.
