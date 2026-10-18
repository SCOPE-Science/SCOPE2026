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

# Reproduction and limits

Execute `python verify_matching.py` with Python 3 and SymPy installed. The final success marker is `VERIFY_OK` after both the symbolic-chart checks and all finite-field enumerations. The checker derives the determinant equations in a full Plücker big cell; for each finite Grassmannian point it computes the Jacobian using **all** big-cell tangent coordinates (not only the enumerating row-echelon stratum coordinates). Tested cases are \(m=3\) over \(\mathbb F_2\) and \(\mathbb F_3\), and \(m=4\) over \(\mathbb F_2\); symbolic chart identities are tested for \(2\le m\le8\).

The proof, not the finite checks, establishes the result for every integer \(m\ge3\) over every algebraically closed field. The argument identifies the exact scheme-theoretic big-chart rings as \(\mathbb A^2\) times independent determinantal nodal cones, proves irreducibility with an incidence map, and uses the Jacobian criterion, normality and hook-length degree. The checker does not verify unbounded symbolic parameters, literature originality, or the unreduced Jacobian singular scheme. Independent audit: not performed.
