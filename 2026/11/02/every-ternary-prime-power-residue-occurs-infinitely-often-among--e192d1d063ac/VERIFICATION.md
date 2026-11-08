---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For k≥1, L=k+2, sparse ternary digits indexed n_{k;v,t}=Σ_{i=1}^v 2⋅3^{Li}+Σ_{i=v+1}^{v+t}3^{Li} are widely separated. A factorial-unit recurrence modulo 3^k splits into disjoint length-k digit windows; doubling has exactly v carries, so ν_3(binomial(2n,n))=v and its unit is d_k^v c_k^t. Since n≡0 mod3^k, the Catalan denominator n+1 is unit≡1, yielding C_n≡3^v d_k^v c_k^t mod3^k. Direct binomial product gives c_k≡2 mod9 (k≥2), and LTE implies c_k has unit-group order 2⋅3^{k−1}; d_k is unit by one-carry count. Hence all nonzero valuations v<k and zero v≥k are attained and infinitely repeated by increasing t through full orders. Independent integer binomial tests computed c,d and exact order for k=1..4; source finite verifier was inspected but not treated as universal proof.

## originality

PASS

Best-of-knowledge originality of the final exact statement, with actual published-result comparisons rather than title matching; no inspected source mathematically implies the full stated result. Inaccessible closely related texts are explicitly retained as priority risks; failed search is not novelty proof.

## value

PASS

Constructive uniform resolution of Rowland–Yassawi’s explicitly posed forbidden-residue question for every 3^k, with infinitely many witness indices. Natural 3-adic density statement is stronger than isolated fixed-modulus tables and gives a reusable factorial-unit sparse-digit technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
