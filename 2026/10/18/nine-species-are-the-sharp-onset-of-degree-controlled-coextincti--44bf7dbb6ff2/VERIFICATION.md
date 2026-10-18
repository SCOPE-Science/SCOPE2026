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

# Reproduction and evidence

Run `python3 verify_coextinction_variance.py` from the directory containing this document. The program requires only Python 3 standard-library modules. It enumerates the small bipartite incidence matrices with each row and column nonempty, grouped by both guilds' degree multisets. It checks all histogram pairs and verifies polynomial divisibility by \(q(1-q)^2\). An independent inclusion-exclusion count certifies that no labeled incidence matrices were skipped. The three small cases yield \(2161,41503,16081\) matrices and \(5,48,17\) distinct within-margin union-histogram comparisons.

For the nine-species witness it checks both bipartite graphs are connected, reproduces the degree multisets and union histograms, and evaluates the complete \(2^5\)-outcome independent-failure distribution for \(q=1/4,1/2,3/4\). All observed moment differences equal \(2q^2(1-q)^2(1-2q)\) exactly. The accompanying mathematical argument proves the all-parameter identity; the finite rational evaluations alone would not suffice.

This verification is deterministic and pertains only to the stated static independent-failure model. It does not test empirical pollinator dynamics, alternate biological persistence rules, or bibliographic exhaustiveness. Independent scientific audit has not been performed.
