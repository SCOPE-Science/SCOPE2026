---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For each odd prime p pick a with 2^a<p<2^{a+1}, T=2^{a+1}−1. For every odd |w|≤T a signed binary sum of 1,2,...,2^a equals w, so sign sums −p for the unweighted divisor column and +1 for the p-multiplied column partition every divisor of z=2^a p with total signed sum zero. Coprime multiplication preserves the complete divisor bipartition, giving every z+z²t, t≥0, as Zumkeller. For each sufficiently large odd N the least odd prime p∤N satisfies p≤2log N by θ(2log N)~2log N; m=z²<p⁴≤16log⁴N and r=N−z mod m is reduced since N odd and p∤N. Uniform Siegel–Walfisz for m≤(log(N/3))⁵ gives central interval prime weight N/[3φ(m)] + O(N/log⁸N), and eventually at least N/[4φ(m)]. Dividing by log N yields >N/[64log⁵N]≥N/[100log⁵N] distinct q with N−q=z(1+tz). Independently reconstructed divisor sign assignments for 61 odd primes below 300; finite tests are not evidence for prime distribution. Absolute threshold is ineffective.

## originality

PASS

Best-of-knowledge statement-level novelty: the final quantitative theorem differs from matched antecedents while known foundations are credited. Residual priority risks documented. Having infinitely many Zumkeller numbers or a single fixed progression does not imply that every sufficiently large odd N is prime plus a number in a compatible progression. Input-dependent prime avoidance plus uniform distribution supplies that implication.

## value

PASS

A published explicit prime-plus-Zumkeller conjecture had an unhandled odd residue class; the statement settles its all-sufficiently-large-odd form with quantitative unbounded representation multiplicity. The use of movable polylogarithmic moduli is simple but meaningful because it eliminates input-dependent gcd obstructions across every odd input, not just a sparse family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
