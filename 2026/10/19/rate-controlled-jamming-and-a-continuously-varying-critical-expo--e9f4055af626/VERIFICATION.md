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

# Verification record

Execute `python3 check_weighted_jamming.py` using Python 3 standard library. It tests exact rational expected terminal vacancy counts by two independent finite generators for 104 cases with part sizes at most two, checks the analytic first integrals for rational parameter choices and the unweighted special case, and compares seeded simulations of 300 depositions on 5000 vertices at each of five rate ratios against the limiting formula. All these checks passed when executed from the actual source file.

Exact finite enumeration is exhaustive only for its enumerated small graphs; it does not establish large-graph asymptotics. The theorem's infinite-volume convergence is furnished by the fluid-limit and terminal-squeeze argument in RESULT.md. The originality comparison is based on specifically described accessible primary text, with an inaccessible plausible 1986 source left as a risk. Independent validation has not been performed.
