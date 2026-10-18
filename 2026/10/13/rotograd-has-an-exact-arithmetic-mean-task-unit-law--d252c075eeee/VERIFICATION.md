---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For the source-form first-order RotoGrad update at matched states with nonzero current and initial task gradients, if each task objective is multiplied from initialization by s_k>0, G'_k=s_kG_k and (G^0)'_k=s_k G_k^0. Thus unit directions U'_k=U_k and relative-norm weights alpha'_k=alpha_k. Since C=sum alpha_k||G_k||, p_k=alpha_k||G_k||/C is a probability vector and exactly C'/C=sum p_ks_k (bounded between min and max scales). The backbone update vector C sum U_k is multiplied by this mean. The individual head gradients and rotation losses/gradients are each homogeneous of degree one in s_k because the rotation target is normalized and the feature gradient is held constant under rotation differentiation. For common scale s, both displayed first-order learning rates divided by s cancel all gradient scaling at each step, giving full trajectory equivalence by induction. For independent unequal scales and two nonzero head gradients one common scalar learning rate cannot reproduce both, as it would require r s_i=r s_j=1. Independently constructed 350 trials compare gradients and weighted mean on matched vectors. Zero sum U gives zero backbone vector; do not assert a defined geometric direction there. Proof excludes adaptive optimizers, loss pre-normalization beyond source form, and state comparisons after divergent task-specific updates.

## originality

PASS

The full defining Javaloy–Valera RotoGrad paper supplies the gradient normalization, magnitude target, head and rotation updates (Algorithm 1) but does not itself articulate the simultaneous positive task-unit transformation for all three update channels, nor the exact scalar compensability conditions. Later Dual-Balancing introduces another method treating loss-unit disparities. The calculation is elementary but source-specific, correctly scoped, and a useful explicit diagnostic for a multi-objective algorithm; an implicit implementation remark remains a priority risk.

## value

PASS

Independent task-loss units are an intrinsic methodological issue in multi-task learning, precisely the domain RotoGrad addresses. The exact law distinguishes the normalized direction, shared magnitude, task-specific head/rotation timescales, and global versus nonuniform learning-rate compensation at fixed states. This identifies a concrete dynamical sensitivity of the defining algorithm and clarifies which claimed homogenizations are unit-invariant, rather than an arbitrary arithmetic reformulation or benchmarking promise. It does not assert novel optimizer design or empirical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
