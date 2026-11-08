---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For every n>=3, prices p_i>0 and budget B>0, the first passage along the unique forward arc has expectation sum h_j with h_j=1/r_j. The maximum over ordered distinct pairs is sum h_j minus min h_j. The continuous strictly increasing level function sum(1-p_i/c)_+ has a unique solution c, and weights lambda_i=(1-p_i/c)_+ sum to one. Averaging omitted-edge sums gives T>=sum (1-lambda_i)h_i; Cauchy-Schwarz and exact budget give T>=M^2/B for M=sum p_i/sqrt(max(p_i,c)). The claimed positive h_i=(M/B)*sqrt(max(p_i,c)) attains all inequalities; strict Cauchy equality plus budget saturation gives uniqueness for every price tie. For (1,1,Q) the level c gives Q=2 breakpoint. Independent check sampled 200 price-budget cases and 1000 feasible competitors; proof is unrestricted.

## originality

PASS

Qualified PASS for the explicit all-price cost-pooling solution and global positive optimizer uniqueness on a directed Markov cycle, with an explicit material priority risk from general PERT convex resource allocation.

## value

PASS

PASS: Exact unique positive optimal control for a natural first-passage minimax problem, explicit observable price pooling and a sharp single-price transition, usable to design directed cyclic networks without numerical optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
