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

# Computational verification

The C++ program `check_total_bondage.cpp` independently builds all edges of \(P_n\square P_4\) for \(n\in\{5,7,8\}\), uses a complete sixteen-mask row transfer for total domination after each deletion, exhausts all deletions of one, two and three edges, and rejects deletion sets leaving any isolated vertex. Its exact output is embedded as `check_output.txt`. It also checks an explicit upper-bound witness for each of the three grids, including the increased total-domination number.

The Python program `check_optimal_sets.py` first enumerates every optimum total dominating set of each intact grid; there are respectively \(256\), \(121\), and \(2916\). It then determines which admissible edge deletions destroy **all** those sets by inspecting selected-neighbor edge clauses at each vertex. This equivalence follows from monotonicity of total domination under edge removal. Its exact output is `check_optimal_sets_output.txt` and matches the C++ census across all nine rows.

Both programs were executed. Exhaustiveness is justified by the finite mask state space and the explicit loops over all edge combinations, not by incomplete sampling or elapsed-time cutoffs. The results depend on the included algorithms being implemented correctly; they have not been formally verified in a proof assistant or independently externally audited. No assertion is made for untested grid lengths or four-edge-cut counts.
