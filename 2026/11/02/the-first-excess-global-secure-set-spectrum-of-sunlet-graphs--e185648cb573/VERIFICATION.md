---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Domination requires one vertex from every core–leaf pair. Adding an attacking selected leaf to a core attack cannot lower its surplus: if its leaf is newly reached, its +1 pays for the only possible new negative core; if the leaf is already reached, its support is already reached too. For a core attack I the surplus is twice the number of attacked A-pairs plus the signed number of newly reached external core positions. With no A, attacking all B positions in a mixed word exposes a negative C boundary, leaving precisely the two uniform sets. With a unique A, an internal B run exposes two distinct C positions; two B runs touching the ends of the tail expose A and two negative positions if their intervening C run has length at least two. Conversely a legal tail exposes at most two negatives when A is attacked, paid by +2; without A, it exposes at most one negative and the first un-attacked core on the B-chain from that boundary toward A gives +1. This includes n=3. Labelled counting uses n possible roots times (2n-2)+(n-3) distinct tails. Independently enumerating both subset sizes of the original vertex set and checking attacks against the definition for n=3,...,8 gave minimum counts all 2 and excess counts 12,28,50,78,112,152, with exact agreement per configuration.

## originality

PASS

The distinct supported content is the complete size-n+1 cyclic-word classification and labelled count n(3n-5) for global secure sets in the all-subsets sense. The minimum value and the two uniform examples are background. None of the inspected actual statements covers the next layer with this condition.

## value

PASS

The first nonminimum size class is a natural next coefficient in a security spectrum, and the result explains exactly which selections attain it rather than tabulating a few cycles. The reduction of all-subsets attacks to charged core boundaries isolates the obstruction and applies uniformly to every cycle length. Value rests on that classification and coefficient, not on the known minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
