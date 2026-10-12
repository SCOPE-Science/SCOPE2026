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

The theorem is proved symbolically in `RESULT.md`; the computation here is only a finite consistency check.

The infinite proof has three exhaustive stages. First, any even \(a\) with \(6\le a\le2n-4\) produces an explicit witness, using one formula for \(a\le n+1\) and a reflected formula for \(a\ge n+2\). Second, once only \(2,4,2n-2,2n\) remain possible, two explicit witness patterns eliminate three of the four triples. Third, for \(\{2,2n-2,2n\}\), parity forces a two-two split and then forces a cross-sum larger than \(2n\).

`verify.py` exhaustively enumerates every three-even set and every four-tuple witness for \(6\le n\le12\), checks that the unique witness-free triple is always \(\{2,2n-2,2n\}\), and checks all displayed constructive formulas for \(6\le n\le200\). Its stored output is `verification_output.txt`.

No finite cutoff is used to infer the theorem for arbitrary \(n\).
