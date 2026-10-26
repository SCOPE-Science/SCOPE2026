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

# Analytical verification and limits

For each fixed \(I_n\), the weight \(x^{-\alpha}\) is bounded above and below by positive constants, so the upper-gradient inequality gives a continuous representative on that component. For \(p>1\), the oscillation bound is the weighted Hölder estimate displayed in the proof; for \(p=1\), the direct estimate \(\operatorname{osc}_{I_n}u\le 2^{-2n\alpha}\|g\|_{X_\alpha}\) applies when \(\alpha\ge1\).

The weighted component mass is \(m_n=\log2\) at \(\alpha=1\), grows like \(2^{2n(\alpha-1)}\) for \(\alpha>1\), and is summable over \(n\) for \(\alpha<1\). These exact formulas verify both the sufficiency mechanism and the finite-norm obstruction. The alternating function is constant on each connected component, so its upper gradient is exactly zero.

No numerical experiment or external formal checker is used. The proof is analytic and its estimates are stated explicitly. The result is limited to the specified geometric interval family, the power weights, and upper gradients tested on all rectifiable curves; it does not settle capacity outerness or general quasicontinuity questions.
