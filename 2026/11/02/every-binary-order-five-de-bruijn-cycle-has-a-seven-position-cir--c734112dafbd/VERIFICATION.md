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

Run `python3 checker.py` using standard Python 3.8+ (no dependencies). The check enumerates all 65536 complementary predecessor-choice maps on five-bit states, isolates 2048 full cycles, and independently enumerates exactly the same 2048 rooted cycles using four-bit Euler tours. It generates 384 eligible seven-position subsets by cyclic gap compositions and checks all 30 short circular factors for each cycle by precise bit masks. Every cycle passes; the number of optimum seven-subsets lies from 216 to 368, attained by 4 and 2 cycles respectively, with overall total 589120. Each cycle's selected optimum is separately tested via literal substrings for lengths at most five, and the two extremal examples are tested through length 32.

The proof explains why those finite loops are exhaustive; running the program is a computational replay, not a replacement for reading that reduction. Independent mathematical audit has not been performed. The claim is limited to binary order-five circular de Bruijn words and their indexed factors of lengths one through 32.
