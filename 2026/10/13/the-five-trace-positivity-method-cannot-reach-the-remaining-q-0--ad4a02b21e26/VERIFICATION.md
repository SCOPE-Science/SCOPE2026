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

Run `python3 artifacts/verify.py` from the package root. It uses only the Python standard library and exact arithmetic in \(\mathbf Q(\sqrt3)\).

The checker reconstructs the matrix \(T\) at \(q=243\), reconstructs the exact ramification ceiling \(U=921685/59049\), computes all six leading principal minors of \(UI-T\), and compares them with the embedded certificate. Strict positivity of every minor is the Sylvester certificate for \(UI-T\succ0\), which is the critical finite computation in the proof.

The checker also evaluates the source's coefficient vector \((2,4,5,5,4,2)\) as an exact Rayleigh quotient and verifies that it lies strictly below \(U\). This is a consistency check, not the proof of optimality; optimality comes from the Rayleigh-quotient formulation plus positive definiteness.

Limits: the checker verifies the exact matrix arithmetic and certificate, not the external source's algebro-geometric derivation of the five trace identities or ramification bound. Those premises are cited and were read from the source. No independent audit has been performed.
