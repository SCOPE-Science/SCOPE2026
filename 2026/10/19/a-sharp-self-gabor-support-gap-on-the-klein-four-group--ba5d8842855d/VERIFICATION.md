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

Run `python3 scripts/verify_pauli_gap.py` after extracting both files from this package. The verifier needs only the Python standard library. It constructs the full 16-by-16 integral symplectic Fourier matrix, examines **all** support subsets containing the origin of sizes four through six, and produces the rank counts and positive-support classifications recorded in `verification-output.txt`. Rank tests modulo 65537 certify characteristic-zero lower bounds; exact integer cofactors and full residual comparisons certify the actual one-dimensional kernel cases. The 45 two-dimensional kernels are supplied by explicit independent Lagrangian indicator solutions. A rational nonstabilizer witness and its Fourier eigenidentity are recomputed exactly.

The mathematical argument additionally uses purity of a rank-one projector and elementary Pauli/Clifford geometry; no separate machine certification of these identities is asserted. The certificate proves the finite classification only, not a theorem for general orders or numerical robustness. Independent audit has not been performed.
