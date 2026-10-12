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

# Reproducibility and exact finite checks

Invoke `python3 verify_italian_chain_bivariate.py` in the extracted directory; only the Python standard library is required. The checker implements a boundary-class multinomial recurrence with a saturated threshold register. It separately constructs each original bipartite adjacency matrix and directly enumerates all \(3^n\) assignments, accepting an assignment precisely when every zero-labelled vertex has open-neighborhood weight at least two.

It examines 419 profiles (383 proper chain graphs), involving 12,707,343 direct labelings. All predicted bivariate coefficients equal the direct counts. Independently, its minimum-weight checker confirms the explicit six-indicator weight-three coefficient, together with the three-versus-four minimum classification, for every proper tested profile. Representative distributions and the exact machine output appear in `verification_output.txt`.

The finite computation is a cross-check, not an infinite proof; the theorem is justified by the boundary partition and extreme-neighborhood lemma in the accompanying proof. No independent audit is claimed.
