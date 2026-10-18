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

# Verification evidence

The standard-library program `verify.py` was executed from the accompanying package and returned `VERIFY_OK p,q,N triples 338 limit 0.791253218706 C4 0.013591922944`.

For each coprime pair with \(1\le p,q\le6\) and each tested resolution, the program forms every transition probability from **independent preimage clipping** using exact rational numbers; it checks the Markov-row and stationary-column sums. It then compares the resulting entropy with the separate affine-cell plus crossing-cell formula and checks the exact-period recursion numerically after exact probability construction. The explicit five-residue example is checked at ten representatives of each of the three stated congruence classes.

The proofs of universal periodicity, the exact expression for the limiting entropy, and the sign of the overshoot are symbolic in `RESULT.md`. Floating-point logarithms in the program are consistency checks only, not interval certificates or proofs of an infinite assertion.

The normalizing domain is \([0,1]\), all entropy logarithms are natural, and the chain independently resamples uniformly in each cell at each step. No claims are made for other partitions or for deterministic observations without such resampling. Independent audit has not been performed.
