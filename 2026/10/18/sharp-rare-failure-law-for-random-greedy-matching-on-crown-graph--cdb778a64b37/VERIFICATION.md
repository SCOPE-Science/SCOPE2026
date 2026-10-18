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

The reproducible `verify.py` program requires only Python 3.10+ and no third-party packages. Run `python3 verify.py` in the folder containing the files; compare stdout with `verification_output.txt`.

The two exact enumerators are algorithmically distinct: one uses the size/intersection state, and the other retains actual labeled unmatched-vertex subsets. They agree for starting crown graphs of orders \(2n\) with \(2\le n\le7\). Separate brute-force scans of uniformly ordered edges cover \(n=2,3\). Exact rational checks of the potential-drift and factorial-second-moment identities cover every allowable state with \(2\le r\le30\).

The proof of the limit \(\lim_{n\to\infty}nq_n=2\) is analytic and relies on a supermartingale with a factorial-moment bound. No finite computation is presented as an infinite certificate. Independent external validation has not been performed.
