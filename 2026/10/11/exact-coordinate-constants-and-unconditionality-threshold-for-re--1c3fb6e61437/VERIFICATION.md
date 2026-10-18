---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The displayed tree mass-flow norm was reconstructed, with leaf flux c_i-c_{i+1}, spine flux c_{i+1} and the terminal branch. The molecular unit-ball reduction is valid for real free spaces; alternating sign changes attain 1+tail/a_l, while alternating selected starts attain the parity sum, with no lost terminal term. Nested 1-Lipschitz retractions give a monotone Schauder basis. Finite-section constants increase to infinite ones. Uniformly bounded tails imply N a_{l+N} <= sum_{i=l+1}^{l+N} a_i <= B a_l, hence q=1/2 for N>2B; block contraction implies bounded tails by geometric summation. An independently written checker evaluated all signs and selectors over molecules and solved the full Lipschitz-dual linear programs for three strictly decreasing rational combs (n=3,4,5), matching tree norms and both exact constants. The finite checks corroborate, rather than prove, the infinite equivalence.

## originality

PASS

Best-of-knowledge: the precise coordinate-multiplier constants and uniform block-decay characterization for this specific one-point-comb nearest-predecessor basis are not covered by the inspected general retractional-basis, tree-space, weighted-Cantor interval-projection or Dirac-diagonal results.

## value

PASS

PASS: Sharp unconditional and selector norms and a necessary-and-sufficient quantitative decay threshold resolve a natural question about a canonical monotone retractional basis. The surprising conditional examples coexist with the known l1-isomorphism of the ambient free space; this is a precise useful basis-level distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
