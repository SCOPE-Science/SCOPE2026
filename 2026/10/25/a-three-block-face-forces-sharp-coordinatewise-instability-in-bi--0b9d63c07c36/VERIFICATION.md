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
# Verification of the three-block Birkhoff boundary sensitivity

Run `python3 verify.py` using only Python 3's standard library. The checker reconstructs the edges and exact rational potential and verifies all vertex Kirchhoff equations, the kernel row's zero-divergence constraints, the diagonal term, the six grouped absolute masses, the closed norm and strict threshold for nineteen family members. It independently constructs and grounds the graph Laplacian, solves it exactly for \(m=2,3,4,5,6\), and compares all potentials. It also checks the polynomial identity and positivity at forty-one large integer parameters. The recorded outcome is `EXACT_CHECKS_OK 3625`.

The executable finite verification supports reproducibility but is not an exhaustive test of arbitrarily large \(m\). The all-parameter certificate is the explicit potential table checked algebraically by the graph-neighbor formula and the positive-coefficient gap polynomial in RESULT.md. No independent audit has been conducted.
