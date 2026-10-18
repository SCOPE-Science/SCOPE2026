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

# Verification and reproducibility

Run `python3 verify.py` with a standard-library Python 3 interpreter. The script directly enumerates every labeled undirected graph for orders four, five, and six with rational probabilities \(1/5\), \(1/2\), and \(9/10\). It constructs induced four-cycles (and, separately, induced paths on four vertices), degree counts, and exact expectations using `fractions.Fraction`, then verifies the conditional-degree covariance formula against brute-force moments. For the four-cycle/degree-two pair it additionally checks the simplified formula and its three density-dependent signs at six vertices. The script requires no third-party packages or previously generated data.

Analytical checks: the proof verifies the conditional role averaging for all motif vertices, the strict log-sum-exp convexity, the endpoint divergence, the exact cubic maximum \(4/27\), and the fixed-order falling-factorial expansion. Enumerating graphs of order at most six cannot certify any claim for all \(n\), nor does it establish the limiting expansion; those conclusions rely on the written analytic proof.
