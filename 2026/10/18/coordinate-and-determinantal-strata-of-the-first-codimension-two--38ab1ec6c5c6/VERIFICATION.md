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

# Reproducible checks

Run `python3 verify_pnull.py` using a standard Python 3 interpreter. The script computes powers of actual strictly upper-triangular matrices, tests membership in every stated coordinate or determinantal component, compares full finite-field counts with the closed formula for \((p,q)=(2,2),(2,4),(3,3)\), and tests 400 deterministic random full matrices in each of the characteristics two, three and five. Its expected final message is `VERIFY_OK`. The two characteristic-two finite-field tests validate a boundary extension of the algebraic argument but are not asserted as part of the novel \(p\ge3\) theorem. Arbitrary-prime and arbitrary-extension conclusions are justified by the symbolic path and zero-support proof, not by exhaustive computation.

No scheme-theoretic radical calculation or independent review has been performed.
