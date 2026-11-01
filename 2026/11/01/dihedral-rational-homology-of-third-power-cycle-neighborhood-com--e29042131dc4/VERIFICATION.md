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

Run `python verify.py` with Python 3 and SymPy. The standalone program reconstructs all maximal open-neighborhood simplices for cyclic orders from 13 to 25, checks each prescribed elementary-collapse pair for every translation, reconstructs the periodic exact Laurent-polynomial boundary matrices, checks the explicit Smith-minor certificates and verifies the signed fixed-chain character tables. The recorded output is in `verification_output.txt`.

The proof for all higher cyclic orders uses the stated radius-six local-incidence lemma: any coface of a set containing zero must be contained in one of the six neighborhoods centered at offsets one, two or three in either direction; the possible vertices lie in the 13 distinct residues from negative six to positive six. Thus the finite local calculation is an exhaustive symbolic verification of every universal collapse identity. Tensoring with \(\mathbb Q[t,t^{-1}]/(t^n-1)\) and the exact polynomial minor identities supply the universal homology calculation.

The checks do not address integral torsion, independent mathematical validation, or publication-priority certainty. A potentially overlapping publicly indexed nonequivariant note was available only as a research-record summary; its complete full text was not retrieved.
