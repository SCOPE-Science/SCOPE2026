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
The proof was checked by reconstructing the oriented-partition bijection and the two modular steps that force each adjacent coefficient pair. The boundary inequalities used are exactly \(S<2p\) and \(S+1<2p\), with \(S=2^{a+1}-1\).

`verify.py` independently counts bounded signed-coefficient solutions for small upper-strip cases and converts oriented counts to unordered counts. It also tests a lower-strip example where the formula fails, so the script checks both positive instances and scope sensitivity.

The computation is finite evidence only; the infinite theorem rests on the proof, not on enumeration.
