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

# Reproduction and checks

The analytic proof and normalization conventions appear in `RESULT.md`. Run the standalone Python 3 checker with `python verify.py` in the extracted package directory. It uses the standard library and prints `PASS 302 checks`.

The checker numerically integrates the Green-resolvent stationary density for multiple source laws, validates the boundary flux equation and interior differential equation away from atoms, checks normalization, and evaluates the unique root of the one-variable optimality equation. Separate samples check zero asymmetry and sharp bound limits. Derivative signs, uniqueness and all-parameter sharpness are analytic and are **not** inferred from finite sampling.

The first public source is arXiv:2402.16403 dated 2024-02-26. The physical membrane convention and entropy definitions follow DOI:10.1103/PhysRevResearch.6.023283, especially eqs. (4.1) and (4.5). No independent scientific audit is represented by these checks.
