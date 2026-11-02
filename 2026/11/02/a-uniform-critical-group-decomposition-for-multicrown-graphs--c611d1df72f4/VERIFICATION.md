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

# Reproducibility and scope

Run `python verify_snf.py` with SymPy installed. The code independently builds weighted graph Laplacians for all \(n=3,\ldots,12\) and \(k=0,\ldots,8\) and checks 90 complete Smith invariant-factor lists against the proposed direct-sum presentation. Expected terminal summary: `SMITH_FORM_ALL_PASS 90 cases n=3..12 k=0..8`.

Run `python verify_treecount.py` using Python's standard library. It constructs its own reduced Laplacians and computes 88 exact integer determinants for all \(n=3,\ldots,13\) and \(k=0,\ldots,7\), comparing against the matrix-tree product. Expected terminal summary: `MATRIX_TREE_ALL_PASS 88 cases n=3..13 k=0..7`.

The finite checks use separate arithmetic algorithms: integer Smith normal form and fraction-free Bareiss determinants. Neither establishes the all-parameter result by itself. The all-parameter certification is the explicit elementary integral presentation reduction in `RESULT.md`; the scripts detect implementation and low-parameter mistakes rather than replacing that proof. No formal proof assistant or independent scholarly audit has been used.
