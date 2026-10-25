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

Run `python3 verify.py` in the directory containing the companion files; no external dependencies are needed. The script computes every rook-graph open neighborhood from the adjacency definition. Memoized exact search checks the maximum legal sequence length on all \(22\) boards with \(2\le p\le5\), \(p\le q\le8\). For boards \((2,2)\), \((2,3)\), \((2,5)\), \((3,3)\), \((3,4)\), and \((4,4)\), an independent legal-prefix enumerator checks the incidence-forest condition and the uncovered-cell formula for every reachable selected subset. The results are in `verification-output.txt`.

The analytic proof in `RESULT.md` covers every integer \(2\le p\le q\), not only the enumerated cases. Finite testing cannot establish its universal conclusion or publication priority; the relevant combinatorial case analysis and the known skew-forcing duality must be assessed directly. No independent audit has been performed.
