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

# Reproduction and verification

Run `python3 verify.py` (Python 3.9 or newer; standard library only) from the directory containing this file. The program independently derives the required set of linear-one-run words, the exact set of circular-one-run words, and an Eulerian host for each \(2\le k\le18\). It asserts that every predicted cyclic factor occurs exactly once, and that the host length is \(k^2-k+2\).

For \(2\le k\le14\), an independently implemented bitmask minimum-cost assignment solves the exact degree-imbalance transportation problem, checking the formula \((k-1)(k-2)/2\) without reusing the explicit matching construction. For \(2\le k\le11\), a separate memoized edge-mask walk enumerator counts all prescribed-edge rooted Eulerian tours and confirms \(2^{k-2}\). For \(2\le k\le5\), exhaustive enumeration of every cyclic host rooted at the required factor \(0^k\) excludes all lengths below the proved optimum and verifies the precise set and number of optimal hosts.

Expected output:

`VERIFY_OK construction_k=2..18 assignment_k=2..14 rooted_euler_counts_k=2..11 exhaustive_all_shorter_hosts_k=2..5`

All reported checks were executed on the included `verify.py` with the displayed output. The finite search does not establish the universal lower bound or tree-count formula; these follow from the written de Bruijn-flow and BEST-theorem proofs. A standard system Python runtime is the only dependency. The source code creates no files and requires no network access.
