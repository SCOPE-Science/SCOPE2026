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

# Verification of the graph-conditioned cycle covariance

The proof in `RESULT.md` is valid for every integer \(n\ge2\) and every simple undirected graph on \([n]\), without finite-size extrapolation. Its critical steps are the exact two-arrow partial-permutation contraction, the uniform random bijection of \(n-2\) remaining path components, and the graph degree sum \(\sum_{i=1}^{n-1}(d_i+d_{i+1})=4e-d_1-d_n\).

Run `python3 verify.py` with standard Python. Its checks, using exact rational numbers, cover every graph on \(2\le n\le5\), sampled graphs on \(n=6,7\), all admissible two-image conditionings for \(2\le n\le6\), and exact path/star identities for \(3\le n\le23\). On the saved source the result is:

`VERIFY_OK graph_cases=1352 conditional_cases=280 family_cases=63`

These computations are cross-checks, not the justification for universal validity. They do not assert historical novelty, independent audit, or an exhaustive graph test for unrestricted \(n\).
