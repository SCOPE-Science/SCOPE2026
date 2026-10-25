---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS. Grounding the hub gives B=[I_m;√t C] with cyclic difference C and A=I+t C^T C; P=B A^-1 B^T. The cyclic positive Green inverse has g_j=(q^j+q^(m-j))/(sqrt(1+4t)(1−q^m)). Its first differences are unimodal and the rim/rim block tCGC^T=I−G, yielding exact absolute row sums S=1+2√t(g0−g_floor(m/2)) and R=2(1−g0)+2√t(g0−g_floor(m/2)). As g0 strictly decreases from 1 to 1/m, the spoke/rim switch occurs exactly once. The hyperbolic x=m asinh((2√t)^-1) form proves finite strict ceiling <3 and matching lower/upper defect asymptotic 3−sup_t||P||=(2log m+2+o(1))/m; any optimizers satisfy x=log m+o(1), hence t~m²/(4(log m)²).

## originality

PASS

PASS by exact-object comparison. The same wheel graph family has a published Löwner-ellipsoid weight optimization, but its determinant criterion and t→2 exponentially are different from the canonical Hodge projector maximum-row-sum and t→∞ logarithmic boundary layer. Standard Hodge/transfer-current identity alone does not imply this singular optimal scale.

## value

PASS

PASS. Weighted wheel Hodge projections are a natural graph-statistical noise-amplification model. Their exact ℓ∞ sensitivity, rigorous spoke-to-rim switch and logarithmically tuned near-3 supremum identify a nontrivial finite-size tradeoff and an optimal conductance scale; these are independent of the familiar ℓ2 projection identity and useful for robust edge-flow reconstructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
