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

The analytic argument covers every positive integer \(k\), every (possibly infinite) serial, transitive, Euclidean frame, every Boolean valuation, and every formula in the stated language. The principal checks are: (1) derive the identical successor cluster, (2) enumerate all constant-on-support propositional Boolean functions and recover every nonsingleton support, (3) inductively show nested \(\Delta\) formulas respect singleton-support collapse, (4) construct characteristic formulas from separating tests, and (5) use the full-support formula \(\Psi_k\) to prove optimality of the bound.

Reproducibility: run `python3 checker.py` from the package directory, using Python 3.10 or later. The script performs exact finite checks of cut-test profile equivalences and canonical KD45 model representations through three variables, deterministic tests of nested formulas through two variables, and exhaustive support checks of the full-support detector. It does not implement symbolic induction or constitute an external proof assistant. No independent audit has been conducted.
