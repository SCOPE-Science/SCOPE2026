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

# Reproduction and mathematical limits

Run `python3 verify.py` with Python 3 and no third-party packages. The script exhausts the 81 fixed points and confirms that the ten quadratic functions \(t_i^2\) and \(2t_it_j\) span a 10-dimensional subspace, disjoint from the five-dimensional affine functions. It verifies the starting isogeny's reduced Gram matrix is zero and its image is a nine-point totally isotropic plane. Its final output must contain `VERIFY_OK`.

The computation tests only the finite-character algebra. The complete characteristic-zero statement additionally uses established abelian variety Rosati theory, the finite quotient line-bundle descent lemma, semipositivity of Hermitian forms, finite pullback numerical functoriality, and the Mori dream nef-polyhedrality implication. All these steps are explicitly argued in `RESULT.md`; no machine proof, external expert certification, or independent audit is claimed.
