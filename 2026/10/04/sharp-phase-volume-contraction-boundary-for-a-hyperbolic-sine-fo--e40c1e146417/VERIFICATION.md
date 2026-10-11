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

Direct differentiation of the actual vector field gives diagonal Jacobian entries \(\beta_1(1-\epsilon\cosh x_1)/5,-1,0,0\). Since \(\cosh x_1\ge1\), the supremum divergence is \(\beta_1(1-\epsilon)/5-1\), yielding the exact boundary and the \(-1/10\) showcase margin. Liouville's determinant formula integrates the time-varying divergence rather than freezing \(\cosh x_1\); Oseledets plus compact support gives the divergence-average Lyapunov sum. The inspected exact checker verifies coefficient reconstruction and the showcase arithmetic.

## originality

PASS

The introducing 2022 article prints the same vector field but reports \(-0.8-\epsilon\cosh x_1\) as its divergence and then treats that state-dependent quantity as a time constant in a phase-volume formula. The audited coefficient calculation shows those printed expressions are incompatible with the vector field for any positive \(\epsilon\). No checked later source was found correcting the formula or stating the sharp \(\beta_1(1-\epsilon)=5\) boundary.

## value

PASS

Although the calculus is elementary, it corrects a published dissipativity claim for a model whose chaotic and cryptographic interpretation relies on volume contraction. The corrected boundary identifies parameter regimes where instantaneous expansion occurs and prevents the erroneous all-\(\epsilon>0\) conclusion; this is substantive model validation rather than an unmotivated normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
