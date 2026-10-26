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

# Reproducibility of finite consistency checks

The bundled `verify.py` is standard-library Python code. Run `python verify.py` using Python 3.8 or later. Its algorithm constructs the complete edge subdivision directly, executes the ordinary color-change process until fixed point and compares each initial subset against the forest/singleton criterion. It independently computes the forest coefficient enumerator. For orders 3–5 it also directly lists every fort and compares inclusion-minimal ones against the theorem using a dynamic proper-subset test; testing only immediate vertex deletion would not be sufficient.

Complete initial-set enumeration covered \(H_3\) with 64 subsets, \(H_4\) with 1,024, and \(H_5\) with 32,768. It gave minimum zero forcing numbers \(2,4,7\), corresponding minimum-set counts \(6,60,620\), total forcing-set counts \(46,566,9016\), and minimal-fort counts \(5,12,43\). At \(n=6\), 25,000 deterministically seeded random initial subsets agreed with the criterion. The last output line of an observed successful run was `VERIFICATION_OK`.

These observations verify implementation consistency only for sampled orders and are not a certificate of the infinite theorem. The proof in `RESULT.md` establishes the arbitrary-order statement without relying on these finite tests.
