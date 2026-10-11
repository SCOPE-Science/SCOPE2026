---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In a terminal two-coloring, a color class missing both universal vertices dominates only if it equals all of the independent part. Hence Alice wins exactly when the two universal vertices have different colors, or when they have the same color and every independent vertex has the opposite color. The four parity/starting-player strategies in the proof are exhaustive pairing strategies: the player controlling the universal pair can force opposite colors in the winning parity and Bob can force equal universal colors plus a mixed independent part in the losing parity. Hartnell--Rall's even-minimum-degree bound gives the global palette upper bound two because \(\delta=2\), while one color is trivially winnable. The ordinary partition \(\{u\},\{v\},W\) gives domatic number three and \(\delta+1\) is the matching upper bound. The packaged exact minimax verifier was read and independently confirms both starting conventions through \(n=7\); the infinite proof is the pairing argument.

## originality

PASS

Hartnell--Rall determine exact values for complete bipartite graphs and provide the minimum-degree upper bounds, but \(K_{1,1,n}\) is non-bipartite and the exact starting-player parity reversal is not implied by those formulas. English--Swan gives broader later bounds/comparisons but targeted searches found no exact theorem for this split graph. Resultary returned no same-invariant family result.

## value

PASS

The family is the simplest non-bipartite complete-multipartite extension of the complete-bipartite benchmark, and it cleanly isolates a starting-player effect: the two game values swap with parity while the ordinary domatic number remains three. That is a motivated infinite game-theoretic classification rather than a small computational table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
