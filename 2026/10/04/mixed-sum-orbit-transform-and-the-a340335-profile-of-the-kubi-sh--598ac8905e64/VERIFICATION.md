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

The bundled `verify.py` uses only the Python standard library. For the concrete Kubiś–Shelah finite-set/linear-order mixed sum it performs an object-level enumeration through `n=6`: every left subset of the fixed labeled carrier, every permutation of the right complement (its linear order), and every bipartite cross-edge bitmask are explicitly iterated. The totals are checked against
\[
a_n=\sum_{p=0}^n {n\choose p}(n-p)!2^{p(n-p)}.
\]

It then checks the specialized values against the published OEIS A340335 initial segment through `n=12`, verifies the exponential-generating-function coefficients exactly with rational arithmetic, computes the Stirling transform for all ordered tuples, and checks two synthetic specializations of the general mixed-sum transform (pure-set/pure-set and linear-order/linear-order).

Replay command: `python3 verify.py`. Expected final line: `VERIFY_OK`.
