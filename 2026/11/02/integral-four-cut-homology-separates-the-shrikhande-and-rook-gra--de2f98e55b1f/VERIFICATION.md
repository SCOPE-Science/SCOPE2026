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

# Verification and limits

Run `python3 evidence/verify.py` in an extracted package. It uses only Python 3 standard libraries. Success prints `SHRIKHANDE_ROOK_ORDINARY_4CUT_INTEGRAL_HOMOLOGY_OK` after constructing both graph presentations; proving their finite strongly regular parameters by exhaustive adjacency checks; enumerating all \(65536\) subsets of each sixteen-vertex set and independently testing the Alexander-dual criterion; checking every matching pair and face incidence, all directed-cycle constraints, signed integral Morse differentials and their chain condition; performing integer unit-pivot Smith reductions; and cross-checking every homology degree with original mod-two boundary ranks.

The finite proof covers the exact fixed graphs and cut parameter stated in the result. Its unit-pivot operations are unimodular, so no untested-prime torsion can occur. The checker does not establish a complete homotopy equivalence or cup-product structure. The literature comparison cannot rule out unindexed equivalent work, and no independent external audit is claimed.
