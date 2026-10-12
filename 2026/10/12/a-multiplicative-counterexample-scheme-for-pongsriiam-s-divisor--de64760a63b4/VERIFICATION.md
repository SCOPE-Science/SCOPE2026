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
Run `python3 verify.py` in the package directory.

The checker uses exact rational arithmetic for
\[
s\in\{-3,-2,-1,0,1,2,3\}
\]
and checks the appropriate explicit progression for every \(1\le n\le1000\), giving 7,000 exact progression-inequality checks. It also checks 24 algebraic template conditions covering \(ad=bc\), the prime support of \(q\), the gcd formulas, and failure of both proposed divisibility conclusions.

A successful replay prints `VERIFY_OK`. These computations are regression evidence only; the all-real, all-\(n\) result is proved symbolically in `RESULT.md`.
