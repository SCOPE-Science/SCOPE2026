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

Execute `python verify_theta_biclique.py` from this directory. The checker uses only Python 3's standard library (`fractions` and `itertools`), assembles the exact local mass and stiffness matrices, inverts each step matrix with rational Gauss–Jordan elimination, constructs the independent projector expression, and compares every matrix entry exactly. It also tests row sums and signs against the stated necessary-and-sufficient scalar criterion.

Replay result: `VERIFIED exact rational spectrum, row sums, and sign classification for 2952 matrices`.

The tested domain is \(1\le p,q\le5\), excluding \(p=q=1\), ten rational values of \(\theta\), and a deterministic set of nonnegative rational normalized time steps, including each nonzero lower endpoint and values on either side. Exact arithmetic has no rounding tolerances. The general infinite-family proof is in RESULT.md; no finite checker tests all real time steps or all graph sizes.

The source-comparison scope and inaccessible-source risk are recorded in AUDIT.json. The status block above reports no independent audit; the mathematical checks reported here are self-review only.
