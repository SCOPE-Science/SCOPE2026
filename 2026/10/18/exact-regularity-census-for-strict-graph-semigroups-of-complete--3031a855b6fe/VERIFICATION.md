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

# Reproduction and limits

The standalone `verify.py` uses Python 3 and no third-party modules. From a directory containing the file, execute `python3 verify.py`. It independently constructs graph edges from the part sizes, enumerates all graph matchings and independent images, evaluates exact rank counts of all maps, regular maps and idempotents, and separately compares them with the integer coefficient formulas. It also tests direct existence of an element `g` with `f g f = f` for every strict map `f` on four specified profiles.

Observed checks: 15 finite profiles passed all rank counts and semigroup regularity classification. The four direct inner-inverse checks passed: \((1,2,2)\) gives 81/81 regular maps, \((2,1,1,1)\) gives 58/70, \((1,1,2,2)\) gives 167/215, and \((2,2,2)\) gives 253/253. The exact counts for \((2,2,3)\) are 1021 total, 877 regular and 133 idempotents. The verifier cross-checks integer formulas on larger profiles, without claiming to enumerate all possible infinite part profiles.

The full all-parameter conclusion is proved by combinatorial counting and an explicit construction of the inner inverse in `RESULT.md`; finite enumeration does not establish an infinite theorem. The asymptotic is a separate symbolic leading-term argument, not an extrapolation from the finite samples. No independent audit has been performed.
