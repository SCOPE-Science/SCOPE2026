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

For Σ⊂Z₃ with digits 0,1, x∈Σ and 31x∈Σ iff each carry c and digit b∈{0,1} has (31b+c) mod3∈{0,1}, next c′=floor((31b+c)/3). Starting c=0 gives exactly ten reachable carries 0,1,3,4,5,10,11,12,14,15; each can reach the zero carry loop and so every counted prefix is indefinitely extendible. The explicit ten-state adjacency A satisfies the exact integer coordinate identity (A⁵−A⁴−A−I)1=0; propagation by A^k establishes a_n=a_(n−1)+a_(n−4)+a_(n−5) for all n≥5, first terms 1,2,3,5,7 and rational generating function (1+z)(1+z²+z³)/(1−z−z⁴−z⁵). Positive primitive growth gives beta>1 unique root t⁵−t⁴−t−1=0 and the Abram–Lagarias p-adic path-set dimension log₃(beta). Independently rebuilt all ten carry states/edge count and checked the exact all-state vector identity; separately enumerated admissible modulo-3^n prefixes for n≤10. The finite vector identity itself, not numerical extrapolation, certifies all lengths.

## originality

PASS

Abram–Lagarias (2013/14) establish general finite carry automata, Perron dimension, and two structured multiplier families; Abram–Bolshakov–Lagarias (2015) give two further families. M=31=(1011)_3 does not belong to those listed families, and neither inspected source states the ten-state coordinate annihilator, order-five recurrence or exact quintic for it. General algorithmic computability is fully prior work, so novelty is restricted to the nontrivial explicitly evaluated natural irregular multiplier; a preexisting table or more general recurrence could cover it.

## value

PASS

The multiplier 31=(1011)_3 is a natural first separated/gapped ternary three-one multiplier beyond consecutive-digit and endpoint-one structured families. The unexpected ten-state to order-five collapse is an exact interpretable prefix-complexity invariant and Hausdorff dimension, useful to later classifications or benchmark algorithms. An exact self-contained specific value need not imply a new generic algorithm; this is narrow but mathematically motivated rather than arbitrary brute-force slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
