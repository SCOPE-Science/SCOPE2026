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
# Reproducible finite checks

Run the source files as described in `RESULT.md`. The C++17 checker iterates all \(\binom{34}{t-1}\) families with a specified missing triple and \(1\le t\le8\). It computes independent vertex-incidence masks, detects five-set coverage and upper-four-shadow cardinalities, and asserts all listed covering counts, the relevant minimum shadow sizes and every equality witness shape. Eight-triple families have four-shadow at least \(16\), hence larger missing families cannot reach score \(22\).

A separately written Python verifier enumerates normalized feasible families through \(t=7\) and compares every equality witness with all thirty-five balanced bipartitions. The expected terminal messages are `CERTIFICATE_OK maximum_cliques=77 normalized_optima=5 labeled_optima=35` and `PYTHON_CHECK_OK normalized_optima 5 all_bipartite_templates 35 score 22`.

Both programs have been run successfully. They verify an exact finite theorem but do not constitute an external audit or establish historical priority. They do not rely on any files other than the supplied source files and standard language libraries.
