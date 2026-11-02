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

The companion `checker.py` is standalone Python 3 using only the standard library. Running `python3 checker.py` from the extracted artifact directory produced:

```text
CASE (3,) labelled 343 orbits 70
CASE (4,) labelled 50625 orbits 2340
CASE (2, 1) labelled 27 orbits 15
CASE (2, 2) labelled 6561 orbits 1701
ALL_CHECKS_OK
```

The program evaluates the exact rational partition sum and independently enumerates every permitted labelled relation for each four finite input profile, canonically quotients under every relevant type-preserving permutation, and checks equality. It also checks the full modal language on three worlds by computing the closure of all pairs of original and candidate truth masks under Boolean connectives and the box operations until stabilization, so that check is not restricted to a fixed modal depth. The exact proof is the finite-theory characteristic-formula argument, nonzero block row classification, invariant-target-subset counting, and Burnside grouping in `RESULT.md`. Finite tests do not prove the general parameter statement. No third-party audit, independent certification, arbitrary closure-membership decision procedure or global priority claim is supplied.
