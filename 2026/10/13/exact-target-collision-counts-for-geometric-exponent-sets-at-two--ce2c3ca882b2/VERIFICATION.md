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
The proof is a finite-carry argument valid for arbitrary parameters in the stated domain. It does not require a computational certificate.

The package includes `verify_collision.py`, a standalone Python 3 checker that directly enumerates all indexed length-\(n\) multisets for bases \(3\le b\le9\), sizes \(2\le n\le8\), and factors \(1\le q\le39\). This is \(1911\) parameter triples. Run `python3 verify_collision.py` with no external packages. The attached `verification_output.txt` records the completed check.

Boundary checks include \(C_{3,3}(4)=1\), \(C_{3,4}(4)=2\), and the divisor cases in base four. The finite checks cannot prove the universal assertion; the carry normal form and counting argument in `RESULT.md` do. An independent audit has not been performed.
