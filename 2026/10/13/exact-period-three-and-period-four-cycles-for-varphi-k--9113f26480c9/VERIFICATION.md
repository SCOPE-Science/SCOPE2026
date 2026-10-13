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

The symbolic proof is the primary verification. The executable regression test enumerates cycles reached from every prime at most \(k^2/2\) for each \(1\le k\le180\), using the focal paper's theorem that every cycle contains a prime in that range. It then checks that every exact three-cycle agrees with the closed classification and every exact four-cycle satisfies one of the two classified forms.

The run returned `VERIFY_OK` with 123838 starting-prime orbit checks, 3 exact period-three cycles, 39 exact period-four cycles, 1502 direct converse checks for alternating parameter tuples, and 24 Bertrand-family checks.

These finite checks do not establish the infinite theorem. They are designed to catch algebraic sign, boundary, primality-pattern, and parameterization errors. The proof itself establishes the universal quantifiers.
