---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Solving the first EMA under \(g_t=(-1)^{t-1}G\) gives \(m_t=(-1)^{t-1}aG(1-(-\beta_1)^t)\) with \(a=(1-\beta_1)/(1+\beta_1)\). Squaring removes the alternating sign, so the bias-corrected second EMA tends to \(a^2G^2+\varepsilon/(1-\beta_2)\). The raw-gradient control has the exact denominator \(G^2+\varepsilon/(1-\beta_2)\). The ratio and its derivative in \(G^2\) are therefore correct, including the zero-damping cancellation and the factor nineteen at \(\beta_1=0.9\). An independent long recurrence replay at the source table parameters matched the closed-form amplitude to better than \(10^{-10}\).

## originality

PASS

Best-of-knowledge originality survives. The complete AdaMomentum text was searched for alternating/oscillatory-gradient analysis and contains none; it motivates replacing raw squares with momentum squares through loss-curve smoothing and proves convergence/generalization results instead. LaProp studies a different momentum/adaptivity coupling and instability regime. Resultary returned no implication-equivalent periodic-response theorem.

## value

PASS

A pure alternating signal is the canonical highest-frequency diagnostic for a momentum filter. The exact result exposes a non-obvious cancellation in the optimizer actually introduced by the source, quantifies the signal-to-damping crossover, and shows that nominal first-moment smoothing can disappear after adaptive normalization. This is a motivated optimizer-dynamics boundary rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
