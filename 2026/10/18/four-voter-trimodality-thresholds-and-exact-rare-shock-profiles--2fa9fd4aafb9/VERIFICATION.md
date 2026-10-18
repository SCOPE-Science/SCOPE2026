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
# Reproducibility and limits

Run the included standard-library script using `python verify.py`. It constructs the finite-chain transition probabilities, solves the unique stationary row with exact rational elimination, and checks all stated finite identities.

The executed replay passed: 32,580 rational four-voter parameter tests of the ratio identities and strict-modal inequalities; the explicit five-point stationary distribution; every displayed absorbing-chain Green inverse identity for populations four through eleven and all admissible interior sources; and exact finite rare-shock examples through eleven voters. The verification is deterministic and requires no third-party packages or network services.

The program checks finitely many rational parameters and populations. The global analytic inequalities, existence at all fixed population sizes, asymptotic limiting distribution and sharp minimal-size proof are mathematical deductions in `RESULT.md`; they are not claimed as established by exhaustive testing. The scientific historical-priority comparison has residual literature-coverage uncertainty. No independent scientific audit has been performed.
