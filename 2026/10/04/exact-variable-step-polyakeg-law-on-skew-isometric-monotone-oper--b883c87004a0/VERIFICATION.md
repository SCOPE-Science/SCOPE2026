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

From \(J^{T}=-J\) and \(J^{T}J=I\), one gets \(J^2=-I\), \(\langle v,Jv\rangle=0\), and \(\|Jv\|=\|v\|\). Writing \(e=x-x_\star\) and \(s=L\gamma\), the extrapolated point is \(\hat e=(I-sJ)e\), \(F(\hat x)=L(J+sI)e\), and the Polyak projection coefficient is exactly \(\alpha=\gamma/(1+s^2)\). Hence \(e^+=(I-sJ)e/(1+s^2)\) and \(\|e^+\|^2=\|e\|^2/(1+s^2)\). The source critical-condition ratio is exactly \(s\), so admissibility is \(s\le A\). For bounded positive \(s_k\), the infinite product tends to zero exactly when \(\sum_k s_k^2=\infty\). The package exact-rational verifier independently reproduces the one-step identity and finite products in the canonical quarter-turn model.

## originality

PASS

Best-of-knowledge PASS. The 2026 PolyakEG paper supplies the algorithm, the local critical condition, and general convergence bounds, and mentions planar rotation as a canonical monotone example, but its inspected full text does not give the exact skew-isometry update matrix, variable-step product law, or the square-summability if-and-only-if criterion. Resultary returned related exact skew-rotation rates for FRB/RFB, a different method, not PolyakEG.

## value

PASS

The exact skew-isometry family is a mathematically motivated stress test for rotational monotone problems. The equality identifies the sharp admissible step, the exact contraction factor, and a nontrivial variable-step convergence boundary \(\sum s_k^2=\infty\), which is more informative than a finite experiment or generic big-O bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
