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
# Verification notes

Reproduction: use Python 3 with only the standard library and run `python checker.py`. Verified outcome: `all checks passed: 2843`.

The script checks the exact hypergeometric expected-loss expression for all support sizes \(2\le t\le12\), all possible deterministic first-bundle cardinalities, and all cardinalities of a later costly support. It enumerates affine hyperplanes on binary vector spaces of dimensions one through six and checks every unordered pair's exact retention probability.

The proof, not the finite enumeration, is used to establish the statements for arbitrary inventory size: (i) block partition for the upper bound; (ii) strictly minimized pair-adversary payoff for the lower bound; (iii) equality-induced pairwise balance; (iv) rank and affine-hyperplane arguments for sparse randomization.

Boundaries: No computational verification covers all infinite parameter values, nonbinary costs, additional agents, or adaptive adversaries. No independent audit has been performed.
