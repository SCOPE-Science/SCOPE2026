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

# Verification and limits

The proof uses the open-access defining-halfspace theorem (Heuer–Striker, arXiv:2012.09901, Theorem 4.6) and the distinct-facet theorem (Theorem 4.8). For every row prefix of length \(j\), the unweighted Frobenius norm of the coefficient vector is \(\sqrt j\), with the column analogue \(\sqrt i\). Exact containment yields the shifted prefix inequalities. The radius bound is attained by a constant matrix. Equality analysis and strict-slack witnesses certify both the affine-hull formula and the universally tangent facet counts.

The package includes `check_pasm_incenters.py`. Run with `python check_pasm_incenters.py` (Python standard library only). The tested shapes \(2\le m,n\le40\) passed (1521 shapes, 45682 active labeled inequalities), using 70-digit decimal arithmetic and a tolerance of \(10^{-55}\) only for rounding of radical values. The checker is finite evidence and does not claim an exhaustive search or independent validation. Some redundancy creates two labels for the same facet at the upper-left matrix entry.

No independent mathematical audit or external certification is claimed.
