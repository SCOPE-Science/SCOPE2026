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

# Verification of the Harshad-base classification

Run `python3 verify.py` using Python 3 and its standard library. The expected message is:

`VERIFY_OK: 195 odd primes exhaustively tested through 1200; 9-base prime witness 21523361; Fermat and perfect-fourth boundaries`

The program computes ordinary digit sums independently for every base \(1\le b\le2p\) of every odd prime \(p\le1200\); it compares exact sets, not merely counts, with the proposed classification. It independently establishes primality of \(21523361\) by trial division through its square root, checks that \(2p-1=3^{16}\), verifies all nine asserted Harshad bases and tests the smaller Fermat and perfect-fourth boundary examples.

The universal assertion is proved in RESULT.md from a complete classification of the digit-sum divisors \(1,2,p\). The finite checker neither substitutes for the classification argument nor proves infinite prime density. The density estimate follows from at most \(\sqrt{2X}\) integer square-root possibilities and \(O(\log\log X)\) possible Fermat-prime indices, compared against \(\pi(X)\gg X/\log X\).

No independent mathematical audit has been performed.
