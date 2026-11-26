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

Sum the cited pointwise harmonic bound and use the nonpositive exact swap gains. Its guarantee decreases strictly with committee difference r, forcing r=k; equality then makes every swap and every per-voter slack vanish. With r≥2, the positive-increment estimate bounds slack below by (r−1)H_u/2−(r−1)/(u+1) when x≥y and x≥1, strictly positive for u>1. At u=1 equality requires x=y=1. The zero-additions and falling-score cases are strict for u>0, while u=0 requires x=0 or 1. Summing the neutral-swap equations by row forces equal row totals and then identical columns across rows. In the converse, with exactly 2k candidates, a committee containing t members of O with index set T has score kS+(t−1)(sum over T of d_t)/2, by counting pair approvals and subtracting half the double approvals. This confirms global optimality independently of the locality bound. The voter count is at least (3k−1)S/2. Nonnegative singleton counts require S≥(k+1)/2 for odd k, attainable with that many unit columns. For even k integrality forces each d_t even, so S≥k+1 implies S≥k+2, attained by (k+2)/2 columns of size two. Irrelevant voters cannot improve this minimum. No general converse with extra candidates is asserted.

## originality

PASS

The sharp finite ratio is already immediate from the cited lemma and prior witness; the frozen record credits both. What is distinct is the complete projected equality family and its sharp parity-sensitive minimum electorate, rather than either the approximation ratio or one construction.

## value

PASS

The minimum number of voters is a natural measure of the size of an exact worst-case PAV instance, and the prior construction motivates minimizing it. The classification determines all distinct projected equality patterns, not just a smaller example, and explains the parity obstruction in the optimum. It can be used to generate sparse worst cases and to recognize why particular ballots cannot be extremal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
