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

The parameter conditions in Theorem 4.10 were transcribed into the proof family by family. The linear equation ranks for \(I_{01}\) through \(I_{17}\) were recomputed over the rationals. For \(I_{18}\), ten independent linear conditions leave a four-plane and the residual cubic is nonzero, giving dimension \(3\). For \(I_{19}\) and \(I_{20}\), the nonzero coordinates \(a_{20}\) and \(b_{20}\) determine the remaining restricted coefficients, giving dimension \(2\). For \(I_{21}\), ten independent linear conditions leave four variables and the two residual binomial equations are finite over \((a_{30},b_{30})\); their Jacobian is independently rank two at the explicit nonzero witness \((a_{30},b_{30},a_{03},b_{03})=(7,7,4,4)\).

The checker `artifacts/verify_isochronous_geometry.py` reproduces these finite rank checks and verifies that the free coordinates of \(I_{01}\) and \(I_{02}\) are complementary inside \(a_{21}=b_{21}=0\), so their tangent spaces span a twelve-dimensional space. Since \(a_{21}\) and \(b_{21}\) vanish on every classified family, the Zariski tangent space cannot be larger.

The published complete classification is used as a premise. Its all-order elimination and sufficiency proofs were not independently re-derived. No independent audit or external validation has been performed.
