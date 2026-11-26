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

At range k the k internal edges all have weight c; the outgoing edges have weight 1 and the walk starts at the last record endpoint. Absorption is almost surely finite. Solving the affine harmonic equation with the two weighted endpoint conditions gives right-exit probability (i+c)/(k+2c) from i, including k=1. Thus from either sign the next sign changes with probability c/(k+2c); the first sign is fair. With B_k(j) the proposed count mass, the recursion for the positive joint mass simplifies to [(j-1+c)/(k+2c)]B_k(j-1)=(j/(k+1))B_(k+1)(j); the negative side follows by reflection. The zero/outside masses and the initial level satisfy the boundary conditions. The two three-step paths differ by exactly the factor (1+c)/c and have positive probability for all c>0. The binomial mixture with a Beta(c,c) parameter gives the moments and weak convergence without making the original process exchangeable or claiming pathwise convergence. The frozen check_output.txt records 10002 exact-rational assertions. A separately written check returned 114 passes for c=1/2 and 2, exit widths 1–4 and record counts 1–4. To replay that bounded procedure, solve the tridiagonal exit equations in RESULT.md §1 as a linear system over fractions at those widths, then enumerate sign strings with the solved endpoint probabilities, aggregate by count and final sign, and compare masses and the stated path ratio. Frozen check.py and check_output.txt describe the larger finite check; the general result rests on the induction, not these tests.

## originality

PASS

Support is for the exact arbitrary-c finite-record beta-binomial count law and its joint final-side refinement, not for the record transition kernel, nonexchangeability, or the beta weak limit as new results. Same-model prior work gives the kernel exactly, and prior coin-turning results cover the limit and the c=1 count special case. The inspected comparisons did not establish the arbitrary-weight finite joint identity in an earlier source.

## value

PASS

At a fixed range, the right count directly measures how the explored sites are allocated between the two sides; the terminal side determines the current endpoint. An exact joint law for these observable quantities for every reinforcement level and range is a natural finite invariant, useful even in the presence of known record dynamics and limiting theorems. The count agrees with an exchangeable urn even though the signs do not, so the count and last-sign identities give genuine information not captured by the path analogy or an isolated finite test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
