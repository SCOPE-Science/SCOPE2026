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

Run the included standalone Python 3 script using `python3 verify.py` from the directory containing this file. The script uses only standard-library functionality. It separately computes convolution products of pairs of incidence-algebra elements and exhaustive idempotent sets. The final success token is `VERIFY_OK`.

The executed finite examples included the one-edge poset over \(\mathbb F_2\), a two-edge and three-edge star over \(\mathbb F_2\), the complete two-by-two bipartite poset over \(\mathbb F_2\) and \(\mathbb F_3\), an edge plus an isolated point over \(\mathbb F_3\), and a two-edge star over \(\mathbb F_4\). For each, the computed product set was equal to the predicted diagonal-support locus, every predicted element passed the constructive two-idempotent factorization, and the total equaled the subset-sum count. The script also checked over \(\mathbb F_2\) and \(\mathbb F_3\) that the three-chain nilpotent is outside all two-idempotent products but equals the given triple product.

These are finite checks only. The proofs for arbitrary fields, arbitrary height-two posets, the independence-polynomial asymptotic, and the field-independent three-chain obstruction are written in `RESULT.md`. A known primary source on restricted antichain submonoids was inspected in full text; a related 2024 paper on algebra generation by idempotents was accessible only at abstract level. The current self-review is not an independent mathematical audit.
