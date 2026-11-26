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

In the linear zero-indexed model, each weight-two output has exactly the three distinct parents (a,b),(a,b+1),(a+1,b+1), so exactly one has sum 0 modulo 3. For a weight-one output at t, each of the three parents listed at RESULT.md line 27 can yield t (deleting the earlier one shifts the later one by one); the listed parent sums are consecutive including both endpoints. The residue counts are choose(N₀,2)+N₁N₂, where Nᵢ are the class sizes, giving the displayed floor. At n=3, 101 covers all three outputs. For the lower bound, the gaps identify weight-two deletion with decrementing one positive coordinate. At v=−1/2 the asserted q=q₀−r is nonnegative: for zero, one or two vanishing coordinates the respective lower bounds are 1/12, 1/3−1/24, 7/12−5/24; at the origin q=1/3. In an interior input the three q₀ descendant weights sum to 1 by v^(s−1)+2v^s=0. If one input coordinate vanishes, the excess over 1 is [v^(b−1)+v^(c−1)]/12 and each of the two corrections contains the corresponding positive part; for two zero coordinates the sole descendant has weight at most 5/6. To sum q₀, count d−s occurrences of each fixed coordinate s and use ∑(d−s)v^s=d/(1−v)−v(1−v^d)/(1−v)² for s=0,…,d−1. For r, sum the six ordered pairs of distinct face/coordinate labels: each contributes ∑max(v^s,0)/12, including corners with multiplicity. The correction is <2/3 and the q₀ deficit from N/3 is ≤5/18. Thus any cover has integer size strictly greater than N/3−1, hence at least floor(N/3). This verifies the universal certificate in RESULT.md lines 35–71. The supplied rational script and recorded finite output were inspected, not independently executed.

## originality

PASS

The supported new result is the exact restricted covering minimum, with a dual certificate valid for every length. The numerical sequence is already tabulated as OEIS A001840 shifted by two, but its inspected interpretations do not give the deletion-covering inequality. A same-day indexed record on the very same weight-two inputs concerns disjoint deletion shadows, not covers. The closest inspected general deletion-covering results concern unrestricted strings rather than the attainable fixed-weight output universe.

## value

PASS

The model is a natural constrained deletion-covering problem: cover every attainable received word using as few weight-two transmitters as possible. The simple residue construction gives an optimum code, but optimality is not explained by a degree count or the already tabulated floor sequence. The explicit boundary-corrected certificate closes the all-length lower bound for a nonuniform incidence problem and gives an exact benchmark distinct from unique-decoding codes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
