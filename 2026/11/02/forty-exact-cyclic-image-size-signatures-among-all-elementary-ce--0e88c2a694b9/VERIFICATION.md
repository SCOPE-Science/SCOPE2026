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

# Reproducibility

From the folder containing the files, execute `python3 verify.py`. The command requires only Python's standard library and prints `VERIFY_OK` after all checks pass. It constructs the Boolean de Bruijn relations and their reachable semigroup for each of the 88 standard symmetry-class representatives, builds the exact deterministic two-letter transition graph, and tests the 48 within-signature pair equalities through each applicable Cayley–Hamilton dimension bound. It checks the 40-class histogram and that no pair of distinct signatures agrees at every length up to six. As a separate small-case cross-check it directly enumerates every input ring for all 256 elementary rules at lengths 1 through 11.

The companion `classification.json` lists the 40 groups and 48 checked pair bounds. The script deterministically recreates its data and displays its digest; the JSON file is descriptive, not an input assumption. The maximum certificate comparison degree is 4,750 and the largest relation-state graph has 2,375 states. Infinite equality is deduced algebraically, not extrapolated from the direct brute-force checks. Independent review and further comparison against potentially unindexed historical literature remain open.
