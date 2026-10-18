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

# Verification of the exact star-voter calculation

Run `python3 verify_star_voter.py` with Python 3 standard library only. The program creates the transient Markov generator with \(k\in\{1,\ldots,n\}\) discordant leaves and solves it by exact rational elimination for \(2\le n\le12\) and seven positive rational center rates at each \(n\). It compares initial \(k=n\) and \(k=1\) times against the proved formulas.

For \(2\le n\le5\), the program independently constructs the full \(2^{n+1}-2\)-state generator of all nonunanimous assignments, retaining vertex identities. Its results for the two single-dissenter configurations agree at all 28 tested rate/size combinations. The reduced tests total 77. Arithmetic and asserted identities are rational and exact.

The program checks uniqueness thresholds algebraically for eleven star sizes and reproduces the exact example \(n=4,c=3\). The analytical backward-equation and martingale arguments in RESULT.md, not the finite executions, establish the unrestricted theorem.

Limitations: no stochastic simulation, external certification, or independent mathematical audit has been performed.
