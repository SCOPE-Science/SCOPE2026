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

# Reproducible mathematical checks

Run `python3 verify.py`. The program constructs balancing and Lucas-balancing numbers by the defining second-order recurrence and Lucas-cobalancing values independently from the Pell companion recurrence. For each \(1\le k\le240\), it checks the gcd of the first three square-window sums against the three proposed expressions, and checks eight additional sums per sequence are divisible by that gcd. For \(1\le k\le100\), it also checks three exact closed window identities at three starting positions. It additionally tests the key two-adic congruences at each window length. This implementation prints `PASS 240 window lengths; 7620 exact checks; all three formulas`.

Why three sums suffice: squares of these sequences satisfy the order-three recurrence with characteristic polynomial \((T-1)(T^2-34T+1)\). Hence each window-sum sequence satisfies the same monic integer recurrence; its entire gcd equals the gcd of its first three terms. The written proof independently reduces the infinite gcd using companion subsequence differences, so the program is a consistency check, not a finite substitute for a proof.

No external theorem prover or independent audit was used. The checks do not establish originality and do not exhaust unindexed papers.
