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

For the forbidden 2-adic set E, its closure off E is the singleton 0 and its Haar measure is 1/6. A nonzero point of T^{-1}(E) outside E gives a whole cylinder containing a nonnegative integer counterexample; zero is already an input. An odd slope preserves measure, making the inclusion equality almost everywhere: any nonzero preimage of 0 has a neighborhood either inside or outside E but with a mixed preimage of E, a contradiction. Hence b=0 for an odd slope and checking the mod-8 odd classes gives a≡1. A slope 2u with u odd and b odd has preimage measure 1/4, impossible. For b even its 2-adic zero t lies in the closure of E by preimages of high forbidden cylinders, so t is 0,4,7 mod 8. The preimage of 28 mod 32 then has residue t+14/u mod 8, none of 0,4,7, contradiction. Common division by four preserves membership of the output; for the remaining slope divisible by four, outputs 1 or 2 mod 4 always pass, and 3 mod 4 needs a fixed residue 3 mod 8 (otherwise n=0 or 1 fails). This also gives the stated valuation conditions. Disjoint pair buckets give the recurrence, whose main term sums (9/64) times the geometric series of ratio 1/16; floors contribute only O(X) by geometric summation.

## originality

PASS

The supported content is the complete affine-preserver classification for the fixed ternary form, including positive intercepts and the pair density. The ordinary Legendre obstruction and the excluded-value density 1/6 are classical inputs, not originality claims. Compared indexed and published statements address different value sets or distributions and do not cover this classification and count.

## value

PASS

This is a complete arithmetic classification for a canonical classical value set, not a list of congruential examples. It separates homogeneous from positive shifts, rules out every slope of dyadic valuation one at the reduced level, and gives an exact count and limiting fraction for all positive pairs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
