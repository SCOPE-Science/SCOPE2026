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

Reproduce with `python3 verify.py` (Python 3 standard library only). The exact-integer dynamic program computes denumerants via three unrestricted coin-addition recurrences, then checks the claimed maximum for every \(a\in\{3,\ldots,120\}\) and every \(0\le p\le2a\). It also verifies explicit coefficient-triple counts using an independent direct enumerator for small instances. No floating-point or randomized computations are used.

The verifier checks \(d_a(G)\le p\), all \(d_a(G+1),\ldots,d_a(G+a)>p\), and a direct finite maximum against the formula. Monotonicity under addition of \(a\) gives the infinite bound only when combined with the mathematical proof; finite verification alone is not a proof for arbitrary \(a\). The analytic proof uses the exact finite-summand identity in `RESULT.md`, including parity and equality boundaries.

The literature comparison cites source titles and exact theorem ranges; priority beyond accessible and indexed sources is not certified. Independent audit has not been performed.
