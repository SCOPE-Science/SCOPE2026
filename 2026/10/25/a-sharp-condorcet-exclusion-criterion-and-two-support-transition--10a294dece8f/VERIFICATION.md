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

The proof derives the attacker-copy scores by direct conditional enumeration and by the identity \(\int_0^1(r+td)^2\,dt\). It proves strict convexity, the self-play value \(1/3\), the necessary and sufficient exclusion inequality, and the piecewise symmetric formula. No external certificate is asserted.

Run `python3 verify.py` from the folder containing this file and the script. The script uses only `fractions` and `itertools`; its actual execution produced these two outputs:

```
PASS 10788 exact attacker-score comparisons; finite checks corroborate the algebraic proof
PASS 1866 exact general-profile Condorcet-exclusion tests
```

These bounded checks are not proofs of the universal quantifiers. The exact symbolic reductions and strict-convexity argument in `RESULT.md` supply the mathematical proof. The general exclusion criterion is restricted to profiles in which the middle alternative is the strict Condorcet winner. The already-known general uniqueness result and the implicit boundary witness in Shah's lower-bound construction are not independently rediscovered claims.
