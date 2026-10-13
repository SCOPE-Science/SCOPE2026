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

Run `python3 verify.py` beside `certificate.json`.

For every positive \(m,n\) with \(m+n\le5\), the first engine enumerates every double-occurrence word on the labeled vertex set and accepts exactly those whose alternation graph is \(K_{m,n}\).

The second engine independently generates all rotations of \(ABA^RB^R\) over all part permutations. The two complete sets must agree.

The verifier checks \((m+n)m!n!\) linear representants in every tested case. For \(m+n\ge3\), it also checks exactly \(m!n!/2\) cyclic classes and directly tests every representant for absence of square factors. The exceptional \(K_{1,1}\) case is checked separately.

The infinite classification itself is proved combinatorially in `RESULT.md`; the finite replay is a cross-check, not a substitute for that proof. Independent audit has not been performed.
