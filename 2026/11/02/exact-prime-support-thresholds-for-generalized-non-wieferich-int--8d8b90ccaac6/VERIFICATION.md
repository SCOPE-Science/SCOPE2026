---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every odd p, d_p=ord_p(b) divides p-1; the odd-prime lifting-the-exponent identity gives v_p(b^(d_p u)-1)=h_p+v_p(u). Thus ord_(p^a)(b)=d_p p^max(0,a-h_p), and L=ord_n(b) is the CRT lcm. The exact p-valuation of L equals max(max_q v_p(d_q), max(0,a_p-h_p)); hence v_p(b^L-1)=max(t_p,a_p) and the quotient valuation max(0,t_p-a_p). This proves all exponent bounds and the first power without a finite cutoff. Independent integer tests of modular quotient p-adic valuations in 2489 base/odd-modulus pairs corroborate; no claims for even moduli/noncoprime bases.

## originality

PASS

The exact fixed-prime-support upper orthant and least qualifying power refine prior global non-Wieferich counting and specific squarefree criteria. LTE/CRT and a known multiplicative-order ratio identity are classical, but the explicit cross-prime threshold is not stated in the primary works read; its mathematical content is a global classification for every support rather than a new lifting lemma. Best-of-knowledge PASS with substantial risk of an old implicit derivation.

## value

PASS

The order-based non-Wieferich integer condition is a natural published arithmetic classification problem. The exact threshold for every fixed odd-prime support and first qualifying power provides a complete answer to an invariant not decided by global density theorems, even though it is derived by elementary lifting/CRT rather than deep machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
