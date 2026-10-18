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

# Reproducibility and verification

The source-level derivation is in `RESULT.md`, Sections "Proof" and "Assumptions and scope". In the canonical basis, the identity \(A(z_1,z_2)=(a\overline{z_1}+b\overline{z_2},-b\overline{z_1}+a\overline{z_2})\) and \(c^2=a^2+b^2\) allows the exact one-dimensional constrained optimization.

The standalone file `check.py` uses Python standard library only. Running `python3 check.py` checks 6 nonnegative parameter pairs (including both degenerate endpoints), 7 complex \(q\) values, both analytically constructed extremizers, their mutual Gram constraints, and 200 random admissible pairs per case. Its tests are finite-floating-point diagnostics, not proofs; see the analytic derivation for arbitrary parameters and quantifiers.

The most relevant publication comparison was against Kołaczek–Müller (2025, arXiv:2508.04347v1), Kołaczek–Müller (2024), and Majumdar–Müller (2026, arXiv:2610.16823v1, Section 6). The last source was released after the first eligible 2025 motivating source and is a comparison, not the dated origin of the claim. Earlier equivalent theorems may still exist. No independent audit or expert validation has been performed.
