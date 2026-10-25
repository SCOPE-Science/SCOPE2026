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

A self-contained Python 3 checker, `verify_engel.py`, enumerates every pair of group elements and every cube in the scalar Frobenius groups over prime fields for the nine ordered parameter pairs \((7,3),(7,6),(13,3),(13,6),(13,12),(19,3),(19,6),(19,9),(19,18)\). It computes the group law and inverse, then independently counts nested-commutator and cube identities. All nine tests passed (`VERIFY_OK`).

The full proof does not extrapolate from these finite experiments: it uses the bijection \(1-s\) for each nontrivial complement element and an explicit infinite prime-power sequence to derive the limiting obstruction. The checker covers only prime-field samples, while the proof covers all finite abelian kernels satisfying the stated Frobenius hypothesis. No independently conducted audit is asserted.
