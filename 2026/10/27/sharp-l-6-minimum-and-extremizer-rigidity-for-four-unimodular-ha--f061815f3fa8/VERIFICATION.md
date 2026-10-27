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

The exact identities used by the proof are the Fourier coefficient convolution of \(P^3\), the quadratic-radical stationary point, and the strictly positive second derivative of the reduced cubic. `artifacts/verify.py` computes the Fourier coefficient Laurent expansion using only Python integers and verifies the radical substitutions exactly using rational pairs in \(\mathbb Q(\sqrt{111})\); it is a standalone executable with no third-party packages. It then checks 50 deterministic complex-coefficient evaluations and four quadrature evaluations on the 256-point circle grid. `artifacts/checker_output.txt` is the saved output from an actual run of this packaged script.

**Proof boundary:** the analytic minimization and equality classification, not grid tests, cover every continuous phase pair. The checker does not certify publication priority or independently audit the mathematics. The exact radical and constant are printed algebraically in `RESULT.md`; decimals are nonauthoritative approximations. No external validation channel has been performed.
