---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The maximal noncoprime run has length J(n)−1, and CRT exactly identifies a run with a cover by one residue class per prime. A prime at least 11 can cover at most one position in a block of length at most 11 and can be assigned to any one uncovered position. I independently scanned the coprimality pattern over each small-support period (rather than enumerating tuples of chosen classes), minimizing the uncovered count over all cyclic starts. For S in order ∅,{3},{5},{7},{3,5},{3,7},{5,7},{3,5,7}, the first failed lengths for an odd five-prime support are 6,8,7,6,9,8,7,11; each immediately preceding length has exactly the required minimum and at length 11 all eight minima exceed the large-prime budget. The same independent check on odd four-prime supports gives 5,6,5,5,7,6,5,7. This also verifies the direct covering argument for even inputs: in the 3-and-5 case a length-six witness uses {1,4} mod 3 and {0,5} mod 5, while a cover at length seven requires an overlap between the maximal classes of these two primes. For odd a, among odd integers 2j+1 coprimality to a is equivalent to coprimality of j+2^{-1} mod a, proving J(2a)=2J(a); prime exponents do not matter. Replay: python3 /workspace/branches/audit-5.py.

## originality

PASS

Verified prior work gives the extremal value 14, requirements on maximizing supports, and the covering and parity-doubling tools. The distinct supported claim is the exact support-resolved rule for all five-prime inputs, especially the nonmaximal strata and invariance under arbitrary replacements beyond 7. The inspected prior statements do not determine their sharp thresholds.

## value

PASS

The exact Jacobsthal gap measures how long a segment can avoid reduced residues. For the natural fixed support size five, the result sharpens a single known worst-case bound to an exact rule even for arbitrarily large prime factors, and identifies the complete spectrum with sharp witnesses and exclusions. This is a structural dependence on small primes, not pointwise tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
