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

# Verification record

The theorem is proved by Witt-coordinate transformations, analysis of possible rational coboundaries at the unique branch point, and separability of \(Q_\lambda(s)=s^4+s^2+\lambda s\) for every \(\lambda\ne0\). The finite checker does not certify that universal proof and cannot establish independent validation.

To replay the exact computational checks, run `python verify.py`. The program uses a standard-library implementation of \(\mathbb F_{2^{12}}\) with polynomial \(z^{12}+z^3+1\) and tests all field elements for the translated Witt-second-coordinate identity at the three parameters \(1\) and the two nontrivial cube roots. It also checks that the root sets of \(Q_\lambda(s)=0\) and \(Q_\lambda(s)=\lambda\) each have size four and that their union is an additive eight-element group. This computation is finite corroboration only.

The theorem concerns ordinary geometric automorphisms of marked order-four Galois covers. Isomorphisms that forget the cyclic deck group, nonclosed fields, and possible automorphism group-scheme effects are excluded. Earlier unindexed marked-cover classification remains a historical-priority risk.
