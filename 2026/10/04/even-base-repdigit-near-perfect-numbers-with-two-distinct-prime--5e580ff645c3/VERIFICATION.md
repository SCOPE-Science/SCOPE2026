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
Run `python3 verify.py`.

The checker first verifies representative members of both symbolic families directly from the defining relation
\[
\sigma(N)=2N+d.
\]
It then exhausts every repeated-digit integer with even base \(2\le g\le30\), digit length \(2\le n\le5\), and nonzero digit \(1\le a<g\). For each integer it factors exactly, requires two distinct prime factors, computes \(\sigma(N)-2N\), and tests whether that value is a proper divisor.

The exhaustive finite box contains exactly five matches, all predicted by the theorem, and none has three or more digits.

The computation is only a regression. The all-even-base theorem is proved symbolically in `RESULT.md` using the published two-prime near-perfect classification, parity, Ljunggren's theorem, and a size argument.

A successful replay prints `VERIFY_OK`.
