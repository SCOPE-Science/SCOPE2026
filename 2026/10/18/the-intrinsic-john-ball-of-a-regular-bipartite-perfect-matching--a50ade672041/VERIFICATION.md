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
# Verification scope

The proof gives an all-dimensional analytical certificate based on the orthogonal cycle-space projection and John's two contact identities. For each coordinate edge \(e\), the normalized outward contact vector is \(-P\varepsilon_e/\sqrt{D/m}\), with positive weight \(D/m\). The weighted contact centroid vanishes and the weighted covariance equals the identity of the affine tangent space; these are exact matrix identities.

The bundled checker `check_john.py`, replayed with Python 3, uses only exact fractions and completed successfully on `C6`, `K33`, `C8`, `crown4=Q3`, `crown5`, and `Q4`. It independently solves reduced graph incidence systems and checks tangency, vertex sums and projection identities. Finite checks are not a proof of the universal claim. The conclusion assumes equal edge effective resistances and is about the perfect-matching equality face, not all matching polytopes. Independent mathematical validation has not been performed.
