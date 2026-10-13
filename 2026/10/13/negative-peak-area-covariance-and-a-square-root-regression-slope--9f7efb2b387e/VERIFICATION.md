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

# Verification of finite and analytic checks

The analytic proof begins from an explicit first-return decomposition and derives exact bivariate generating-function identities. Elementary formal coefficient extraction and the Narayana peak moments yield the displayed formula for every integer \(n\ge1\). The central-binomial-product inequality verifies the strict sign for \(n\ge2\), and Stirling's formula yields the sharp regression scale. These universal arguments are independent of numerical testing.

Execute `python3 verify_dyck.py` using Python's standard library. The verifier exhaustively generates every Dyck word for \(1\le n\le12\) and reconstructs heights and peaks directly. It checks exact rational counts, peak mean and variance, area mean, mixed first moment, negative covariance and all semilength boundary cases: a total of \(290{,}511\) distinct excursions. A successful completion emits `EXACT_DYCK_VERIFICATION_PASS enumerated_paths=290511`.

Finite checking does not establish general n by itself. No independent audit, priority certification, or nonlinear-regression proof is claimed.
