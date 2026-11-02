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

# Verification of the quartic harmonic restriction-rank theorem

The evidence is the explicit sign-parity and subset-incidence proof in `RESULT.md`, together with the independent exact finite-field checker `artifacts/check_rank.py`. The checker constructs scaled evaluations of a spanning harmonic basis in the all-even and two-odd-coordinate sectors, accounts separately for the four-odd-coordinate monomials, and performs row reduction over each of two prime fields, without floating point. To replay, execute `python3 artifacts/check_rank.py` using Python 3's standard library.

The check was actually run and returned `PASS: 22 exact modular rank checks; all observed ranks match the proved formula.` The eleven parameter pairs include general values and representatives of each of the four exceptional mechanisms: the support-size-three squarefree loss, the pair-sector resonance, the scalar even resonance, and the sum-zero even resonance. Finite-field calculations are corroboration only; they cannot establish an infinite parameter theorem by enumeration. Nor is the checker a formal proof system. The independent audit status remains not performed.
