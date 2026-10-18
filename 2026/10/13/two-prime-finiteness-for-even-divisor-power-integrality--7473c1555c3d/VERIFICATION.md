---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Multiplicativity of σ_k gives σ_k(2^ap^b)=S_{k,a}·Σ_{j=0}^b p^{kj}, with S odd and the p-geometric factor ≡1 mod p. For even k, p^k≡1 mod8 and LTE/factorization yields v₂(Σ_{j=0}^b p^{kj})=v₂(b+1); hence divisibility iff 2^a|(b+1) and p^b|S. Then b≥2^a−1; if a≥2k, elementary 2^a−1≥k(a+1) and p≥3 imply p^b≥3^{2^a−1}>2^{k(a+1)}>S_{k,a}, contradiction. So a≤2k−1, making the sieve finite. At k=2, a≥2 impossible by size; a=1 forces S=5 and (p,b)=(5,1), yielding n=10. Independent exact divisibility/valuation and factorization tests for k=2,4 (solutions 10,34) corroborate the proof, not the entire infinite family by computation.

## originality

PASS

Classical multiplicative-function identities and LTE receive no novelty credit. OEIS A046762 lists k=2 examples including 10 but not the across-all-even-k two-prime finite classification. Luca–Ferdinands (2006) gives infinitely many even solutions without the two-prime restriction; Cai–Chen–Zhang (2013) treats fixed-multiplier σ₂ equations and some σ₃ prime-support cases. These do not logically imply uniform finiteness for n=2^a p^b when multiplier varies. Best-of-knowledge PASS with full short 2006 note unavailable and possibility of known two-prime arithmetic lemma.

## value

PASS

The integrality condition n|σ_k(n) is a classical arithmetic question and the restriction to two distinct prime factors isolates a natural minimal-support obstruction to unrestricted infinitude. Explicit valuation and size arguments yield an effective finite decision procedure for every even k and determine its first nontrivial instance exactly; not simply reproducing OEIS values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
