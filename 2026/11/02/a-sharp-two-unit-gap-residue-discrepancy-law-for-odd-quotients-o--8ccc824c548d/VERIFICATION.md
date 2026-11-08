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

The existing RESULT.md supplies the unique decomposition px=(pt+1)k+y and gap condition y>k. Writing k=pq+r, y=p(t−s)−r gives q+s≤t−1 when 0≤r≤(p−1)/2 and q+s≤t−2 otherwise. For interior q+s≤t−2, reflection in the t×t square and uniform differences mod d=gcd(p,t) give exactly t(t−1)/2 contributions per class, even when p is composite. Boundary q+s=t−1 splits into even and odd r and two consecutive intervals of lengths tE,tO, giving the full formula. At t=2 and p≥5 these supports overlap but fail to cover all p classes, proving sharpness; summing counts gives genus. CRITICAL REPAIR: the frozen proof says “for p=3, O=0”; mathematically O=1, so its given proof for the p=3 discrepancy is false. Reconstructed full RESULT.md with E=O=1 and a complete p=3 residue case split t mod 3: when t≡0 the two indicators vanish, when t≡1 they select different single classes, and when t≡2 their missing classes differ; thus discrepancy≤1. All unchanged conclusions now follow. Independent checker evaluated 228 histograms including composite p, and p=3 for every t through 499, all agreeing; no finite test substitutes for the corrected universal proof.

## originality

PASS

Shor studies exact equidistribution of semigroup gaps for arithmetic Apéry families, not an explicit two-indicator entire histogram for this quotient; Cabanillas gives general quotient invariants/genus and algorithms, but inspected full PDF theorem statements do not directly imply every residue count; Liu gives generator descriptions and quotient generating functions rather than the asserted exact bounded-discrepancy statement. Known membership and genus are expressly excluded from novelty. A sufficiently specialized application of general generating functions might imply the formula, but no decisive prior coverage identified in the inspected full texts.

## value

PASS

The exact familywide residue histogram gives a dimension-free discrepancy bound and sharpness across all odd p, including nonprime moduli, a natural fine distribution refinement beyond genus or Frobenius number. The arithmetic p=3 exception is a genuine boundary classification, not an artificial finite example. Repair removes an invalid normalization without changing the relevant mathematical invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
