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

The mathematical proof is in `RESULT.md`. The accompanying `verify.py` uses exact `fractions.Fraction` arithmetic to test the algebraic identity for the first-mode continuum polynomial at five rational inputs. It uses floating-point trigonometry only for finite checks: it brackets and bisects interpolated first-mode roots at degrees 100, 200 and 500, checks the next-order formula against those finite examples, and computes all nonneutral modes at the two neighboring integer sizes. An actual invocation returned `VERIFY_OK; finite mode checks=7242; kappa=9.031187279142; A=-2.105354538616`.

The script does not certify the exact transcendental numbers, prove uniform inequalities, or check an infinite set of degree parameters. Those conclusions are analytical, not consequences of finite experiments. The closed-source published works cited in the proof were not reproduced, and the published claims used for prior comparison are distinguished from the new finite-size classification. Independent audit was not performed.
