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
# Verification

The theorem is proved for arbitrary finite connected chain graphs by an exact structural determination of mutually maximally distant pairs and an exact maximum-independent-set argument in the resulting strong resolving graph.

`verify.py` is an independent finite cross-check. It generates every positive canonical chain-graph profile through order \(9\), builds the graph from the block data, and recomputes all-pairs distances. It then:

1. compares every unordered vertex pair against the claimed mutually-maximally-distant classification;
2. enumerates all vertex subsets below and at the predicted optimum;
3. tests the literal strong-resolution condition using shortest-path distance equalities;
4. confirms that no smaller strong resolving set exists; and
5. checks the exact number of minimum bases against the product-sum formula.

Replay command:

`python3 verify.py`

Expected output:

`VERIFY_OK profiles=255 subset_checks=70490 mmd_checks=7423 basis_checks=2829 max_order=9`

The finite computation does not establish the infinite theorem by itself. It is a boundary and implementation check for the structural proof. The public-source comparison does not constitute an exhaustive proof of novelty; residual bibliographic risks are recorded in `AUDIT.json`.
