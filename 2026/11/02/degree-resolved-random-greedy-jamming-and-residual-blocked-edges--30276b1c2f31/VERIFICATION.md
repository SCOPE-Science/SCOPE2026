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

# Verification

The all-order identity is derived directly by a rooted labeled-tree generating-function decomposition and a continuous arrival-time root recursion. The residual blocked-edge count is converted pathwise to a degree-weighted accepted-vertex count. The order-one finite-size coefficient follows from the singular expansion of \(T(z)\) at \(z=e^{-1}\), not numerical fitting. Concentration uses bounded-radius approximation via decreasing-time paths and two-root local limits for uniform Cayley trees.

Run `python checker.py` with Python 3; the script uses only the standard library. Its two structurally different verification algorithms (root-first recursion and explicit priority-order enumeration) make 38 exact rational assertions and passed in the recorded test. Prüfer-tree exhaustive ranges are \(n=2,\ldots,7\) for the root-degree bivariate formula and \(n=2,\ldots,6\) for explicit priority enumeration of the residual blocked-edge count. For \(n=7\), the edge expectation is checked using the independently enumerated root-degree law rather than every possible vertex order.

The checker does not prove the infinite claims; the proof is in `RESULT.md`. Neither an independent mathematical audit nor comprehensive priority certification has been performed. All findings are conditional on the graph and priority model stated there.
