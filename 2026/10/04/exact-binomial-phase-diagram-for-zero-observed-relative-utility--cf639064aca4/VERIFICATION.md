---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

For n≥2 and q,t in (0,1), with all predictions p_i=q, the treat-all decision is chosen iff q≥t. On A_n={1≤S_n≤n−1}, the observed relative utility is zero exactly when S_n/n≥t in the treat-all branch and S_n/n≤t in the treat-none branch. Summing the Bin(n,q) law, divided by P(A_n)=1−q^n−(1−q)^n, yields both exact integer-bounded tail formulas, including equality conventions. Independently recomputed exact rational cases against the original benchmark net-benefit definition; all matched. For fixed q≠t, standard binomial Chernoff/Stirling estimates give exception exponent D(t||q); at q=t, binomial CLT yields 1/2, and for q_n=t+c/√n a triangular-array CLT gives Φ(|c|/√(t(1−t))). Endpoint exclusion has vanishing probability at the limiting regimes. The checks are diagnostics, not the proof of asymptotics.

## originality

PASS

The motivating 2026 paper identifies the surprising perfect-probabilities/zero-relative-utility phenomenon for the fixed q>t limit. The audited theorem supplies the exact finite conditional binomial probabilities, q<t mirror branch, the off-critical KL rate and root-n crossover. These conclusions are not explicitly established by the accessible source abstract, but inaccessible full text prevents a decisive whole-paper noncoverage claim. Best-of-knowledge O judgment is retained with a substantial named access risk and without asserting that the index search completed.

## value

PASS

The source phenomenon is a specifically motivated risk-prediction interpretability issue, not an arbitrary probability exercise: perfectly calibrated constant predictions may receive zero observed utility with very high probability. The exact finite-sample conditional probability and the sharp threshold-local crossover quantify the sample sizes and risk/threshold separations at which the paradox appears. This is a natural, independently usable exact diagnostic invariant despite the standard binomial techniques and narrow iid model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
