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

On a loopless even clique, nonbalanced nonunanimous states reach the majority consensus in one update, and balanced configurations complement with no fixed point: closed two-cycles pair distinct complements. On odd order 2r+1, a one-vote layer has r+1 independent tied agents while the initially minority agents are forced to the other color. For each critical row, a=2^(-r-1) is the swap probability and also the direct consensus probability for the current majority; b=(r+1)a is the stay probability. Since a+b<1, these layers are transient and all other nonunanimous states stabilize the next round. Color symmetry gives minority win a/(1-b+a), and the first-step time is 1+(a+b)E+1-2a-b. Its solution 2+b/(1-a-b) strictly decreases from 4 at r=1 to 2; the reversal probability is asymptotic to 2^(-r-1). Conditioning on the binomial count, including the endpoint masses and the even-layer zero entry time, gives both Bernoulli-start formulas for all p.

## originality

PASS

The original explicitly credits the published triangle special case and the independent fair-tie model. In fact the primary source already implies both the triangle's reversal probability 1/3 and its mean 4. The distinct contribution is the all-clique classification, exact critical formulas on larger odd cliques, and sharp upper bound over that family, not rediscovery of K3 or invention of the tie rule.

## value

PASS

The natural dense benchmark has a nontrivial parity distinction: balanced even cliques enter deterministic blinking immediately, whereas odd cliques stabilize to consensus and can reverse a strict majority only at the one-vote margin. The exact exponentially decreasing reversal probability and sharp bounded mean are quantitative benchmarks on an unbounded family, rather than a routine rediscovery of the triangle or an empirical small-size fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
