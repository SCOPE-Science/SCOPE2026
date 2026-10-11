---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstruction of the source linearization gives the modal delayed coefficient \(S_k=-a_{12}\chi v_*\mu_k>0\): the retained taxis term \(-\chi v_*\Delta \widetilde u(t-\tau)\) becomes \(+\chi v_*\mu_k\widetilde u_k(t-\tau)\) on \(\Delta\phi_k=-\mu_k\phi_k\), and the 2-by-2 determinant therefore contributes \(-a_{12}\chi v_*\mu_k e^{-\lambda\tau}\). At \(\lambda=i\omega\), the real/imaginary equations imply the positive-sine branch under \(P_k,S_k,\omega>0\). Replacing the printed \(R_k=-S_k\) and using \(\arccos(-c)=\pi-\arccos(c)\) proves an exact \(\pi/\omega_k\) shift; squaring explains why the frequency polynomial is unchanged. The zero mode is correctly excluded. The bundled exact-rational replay checks determinant and branch bookkeeping but is not used as the universal proof.

## originality

PASS

Best-of-knowledge originality survives a fresh comparison. The generic determinant sign is prior art, but the audited claim is the source-specific diagnosis that Liu–Tan’s printed scalar coefficient has the opposite sign from their own linearized operator and that their printed Hopf-delay branch is therefore displaced by exactly half a period. Resultary and exact-title/DOI/sign searches did not locate a prior correction making that implication. The strongest methodological predecessor corroborates the determinant sign without identifying the 2026 source inconsistency.

## value

PASS

An exact half-period displacement of the analytical Hopf-delay branches changes a central bifurcation/stability threshold while leaving the frequency polynomial unchanged, sharply localizing a substantive source error. This is mathematically motivated and useful for anyone reusing the paper’s delay threshold; it is not a cosmetic sign convention or routine normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
