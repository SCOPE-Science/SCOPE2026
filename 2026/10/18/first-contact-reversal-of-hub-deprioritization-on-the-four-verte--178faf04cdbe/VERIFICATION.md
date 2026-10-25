---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Neutral reproductive values π=(1,2,2,1)/6 define a voter-model fixation martingale. Differentiating neighbor fitness weighting gives explicit active-edge drift; duality reduces quadratic moments under the sum of single-cooperator/single-defector laws to six two-lineage survival probabilities Q^t 1. Coalescence on finite connected P4 makes ρ(Q)<1 and sums the full infinite-time periodic drift via (I−Q³)^−1. The cost contribution is −4c/21; three distinct benefit coefficients are 12920/259077, 1730/37011 and 11981/259077. Reversal swaps L,R, exhaustive six permutations cover all cases. Independent rational SymPy inversion of the exact 6×6 Q reproduces all six benefit/cost coefficients, three b/c thresholds, and signs at (4,1). The source also uses separate 14 transient-state differentiation. Analytic finite absorbing-chain inversion justifies sufficiently weak δ>0, not large δ or derivative-equality endpoints.

## originality

PASS

Meng–McAvoy–Li (2024/25) gives a general temporal-network coalescent criterion and empirical low-degree-first heuristic; it does not identify the explicit three-class P4 phase-zero counterexample. The general equation can be specialized algorithmically, but exact rational ordering and minimal graph witness require nontrivial exact six-state calculation and a small-graph symmetry argument. The result rebuts a heuristic, not a published universal theorem.

## value

PASS

A rigorous minimal connected-graph reversal to a motivated scheduling heuristic is a worthwhile sharp boundary: it identifies assumptions (single-edge snapshots, phase of introduction) where a commonly recommended design principle reverses. Exact rational thresholds make a reusable diagnostic beyond an arbitrary four-vertex numerical curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
