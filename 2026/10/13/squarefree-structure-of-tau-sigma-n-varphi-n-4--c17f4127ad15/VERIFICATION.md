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

The proof in `RESULT.md` is unrestricted.

The attached `verify.py` checks every squarefree integer
\[
1\le n\le500{,}000.
\]
It factors \(n\), computes \(\sigma(n)\) and \(\varphi(n)\) exactly, factors their sum to compute its divisor count, and compares direct membership with the theorem's predicate.

For composite hits it additionally checks that
\[
n=2q
\]
with both \(q\) and \(2q+1\) prime.

The finite replay is corroborative only. The infinite classification and counting identity follow from the symbolic proof.
