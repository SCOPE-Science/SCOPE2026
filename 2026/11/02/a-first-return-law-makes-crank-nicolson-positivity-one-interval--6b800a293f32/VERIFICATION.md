---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For any finite irreducible row Markov generator Q and state i, decompose occupation at i into Exp(a_i) sojourn followed by independent post-departure first-return excursion T_i. Laplace renewal gives R_s[ii]=1/(1+a_i E[s(1-exp(-T_i/s))]); T_i>0, finite mean. Since s(1-exp(-t/s))=int_0^t exp(-u/s)du strictly increases in s>0, R_s[ii] strictly decreases 1->pi_i for all irreducible directed nonreversible chains. R_s is nonnegative row-stochastic as inverse M matrix and C_h=2 R_{h/2}-I, so positivity iff every diagonal >=1/2; therefore unique initial [0,h*] interval with no reentrant positivity. Nonuniform directed n-cycle special case Q=a(P-I), R_s[ii]=1/(1+r+...+r^{n-1}); unique root sum_{j=1}^{n-1}r^j=1 and h*=2r/(a(1-r)), h3=(1+sqrt5)/a, limit 2/a. Independently reconstructed R_s and killed-chain first-return Laplace transforms over exact rational matrices for three genuinely nonreversible CTMCs, 3 s parameters each; all diagonal identities agree. Infinite proof depends on regeneration, not on this finite check.

## originality

PASS

The precise published predecessor proves identical diagonal positivity criterion and single interval only under detailed balance, explicitly leaves nonreversible case unresolved; target closes it by a first-return renewal argument. This is not a rediscovery of general M-matrix or renewal facts. Relevant classical positivity-radius theory concerns method-wide worst cases, not fixed-generator sharp no-reentrance. Historical priority qualified by possible earlier specialization of Markov renewal and Cayley transform theorems.

## value

PASS

Positivity restoration at a larger numerical timestep is a genuine stability question for directed finite Markov generators. A universal no-reentrance classification without reversibility is strong structural content; exact directed-cycle thresholds make the result testable and reveal graph-size trend. Explicitly excludes reducible chains, internal stages and floating-point rounding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
