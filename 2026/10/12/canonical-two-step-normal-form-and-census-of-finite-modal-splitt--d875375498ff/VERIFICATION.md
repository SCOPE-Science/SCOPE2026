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

# Reproducible verification

Run `python3 verify.py` with a standard Python 3 interpreter. It prints `VERIFY_OK` after checking every directed relation on at most four labeled vertices, including relations with self-loops. The test for the modal height identity is absence of three-step walks; the SI check enumerates all nonzero modal congruence ideals rather than inferring SI from the proposed normal form. An independent constructor produces the expected canonical structures and tests exact set equality. For each qualifying graph, all vertex permutations determine the isomorphism canonical form; the resulting orbit count is compared with the separate Burnside sum.

Observed exhaustive relation spaces have sizes \(2,16,512,65536\); qualifying labeled classes have sizes \(1,2,15,124\), with \(1,1,3,8\) isomorphism classes. Formula evaluations for \(5\le n\le8\) produce labeled counts \(1525,26106,618695,20279288\) and isomorphism counts \(24,77,283,1182\).

The all-\(n\) conclusion is deductive, through finite modal duality, congruence ideals, intrinsic graph layering, product counting and Burnside's lemma. Computer checks are finite corroboration, not formal infinite verification. No independent audit has been conducted.
