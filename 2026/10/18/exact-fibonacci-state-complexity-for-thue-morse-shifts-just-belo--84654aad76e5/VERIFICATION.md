---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a prefix of value m and continuation length ℓ, division of c plus the continuation value by 2^ℓ gives a high-block offset independent of m and a low-block parity independent of m. At each ℓ>0, continuation value zero tests the floor offset, and value 2^ℓ−(c mod 2^ℓ) tests the ceiling offset when distinct; at ℓ=0 the empty continuation tests c. Thus equality of fingerprints is both necessary and sufficient for Nerode equivalence under the actual encoding, and all m are reachable. For c=2^k−1 the offsets are 0, 1, powers 2 through 2^(k−1), and Mersenne numbers 3 through 2^k−1. For the power-offset profile, the difference from t(m) at offset 2^i is 1 XOR the parity of the run of ones from bit i. Two adjacent differences cannot both vanish, and setting isolated ones just at prescribed zeros realizes any legal difference vector, with a higher bit beyond a zero separator freely choosing t(m). This gives 2F_(k+2) profiles for offsets through 2^(k−1). Even prefixes encode exactly the preceding Mersenne fingerprint (division by two sends even power offsets to lower powers and odd Mersenne offsets to lower Mersenne offsets with bit complement); odd prefixes encode exactly that power-offset profile (Mersenne offsets then become power offsets). Both encodings expose every required lower coordinate. Their images are disjoint for k≥2: the visible pairs (0,1) and (2,3) are both complementary for an even prefix, while for an odd prefix this would require three equal consecutive Thue–Morse bits, impossible by t(2a+1)=1−t(2a). At k=1 the four pairs 01, 11, 10, 00 occur at m=0, 1, 2, 5. Hence the exact recurrence adds 2F_(k+2) at each k≥2 and sums to 2F_(k+4)−6; the stated eleven values agree.

## originality

PASS

The exact all-k MSD-first Mersenne count is distinct in the strongest inspected comparisons. Neither an algorithmic upper bound, the finite OEIS values, the exact dyadic law, nor a least-significant-first minimization establishes it. The carry viewpoint and dyadic subcount should not be credited as novel here.

## value

PASS

This resolves an infinite, structurally natural subfamily of the exact shifted-automata question. Mersenne shifts form the complementary near-dyadic family to the known power-of-two case and require handling two distinct reachable residual families; the result predicts exact minimal sizes beyond the public finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
