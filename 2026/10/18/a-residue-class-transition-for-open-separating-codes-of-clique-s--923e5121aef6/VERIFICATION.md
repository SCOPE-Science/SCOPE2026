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

# Finite reproducibility checks

Run `python3 verify.py` from the directory containing the included files. The program constructs the actual adjacency graph of a once-subdivided clique, enumerates every vertex subset for clique orders 3 through 6, and tests closed domination and pairwise distinct open-neighborhood signatures directly. It also tests total domination to distinguish OD from OTD codes. The four exhaustive sizes have 64, 1024, 32768, and 2097152 subsets, totaling 2131008.

The same program evaluates the claimed generating-function identity by inclusion-exclusion, the minimum-count coefficient through an independent recursion over rooted-by-smallest-vertex tree-forest components, and the minimum size for orders 3 through 11. It checks equality of every polynomial coefficient where direct enumeration was performed. The recorded terminal output is supplied in `verification_output.txt`, and execution ends with `VERIFICATION_OK direct_candidates 2131008 symbolic_orders 9`.

The empirical checks only cover the stated finite ranges. They do not prove any assertion for all graph orders. The unrestricted statements follow from the structural proof in `RESULT.md`. No third-party verification or independent audit is claimed.
