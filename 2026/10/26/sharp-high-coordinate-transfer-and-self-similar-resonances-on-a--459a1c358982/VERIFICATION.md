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

# Verification and reproducibility

Execute `python3 verify_transfer.py` with Python 3 standard library only. A reference execution reports `PASS: 142 finite computational cross-checks. (All-dimensional optimality rests on the written proof.)`.

The checker constructs direct Walsh-character eigenvalue sums for finite cubelike Hamiltonians and compares them to a distinct product-amplitude implementation. It checks infinite-tail truncation using the analytical estimate \(\pi^2/(3\,4^{R+1})\), verifies the exact bit occupations at the dyadic resonances, and numerically optimizes the analytical near-resonance formula for increasing target indices.

The infinite-dimensional formula is proved using norm convergence and the classical sine-duplication product. The global optimal-time uniqueness is established analytically by localization, strict log concavity, and an implicit-function argument. These infinitely quantified claims are not certified by finite numerical enumeration. The exact parameter regime and all limitations are in `RESULT.md`.
