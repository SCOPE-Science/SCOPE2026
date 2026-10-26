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

The reproducible check is `python3 verify.py` (Python standard library). It evaluates the two-parameter independent-chain mex recurrence on a 31-by-31 grid of states, the centre-preserving residual recurrence on 420 states, and the exact star formula through 27 leaves. It also constructs the labelled vertex–edge incidence poset of each star with 1 through 8 leaves and computes option nimbers directly by exhaustive maximal-element deletion. Every checked comparison succeeds with `VERIFY_OK`.

These are finite computations. The infinite statements instead follow from the two case-split mex inductions in `RESULT.md`; no computer enumeration is used as an infinite-proof substitute. The experiment does not certify historical priority, mathematical independence, or arbitrary host-graph extensions.
