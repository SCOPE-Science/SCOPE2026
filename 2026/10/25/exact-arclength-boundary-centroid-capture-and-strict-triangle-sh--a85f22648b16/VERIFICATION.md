---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Condition on side occupancy (probabilities p_i). Affine invariance implies the 2+1 and 1+1+1 conditional probabilities depend on occupancy alone. In barycentric unit triangle, 2+1 capture is integral_(1/2)^1 2r(2r-1)/(3r-1)^2 dr =1/9+4log2/27. For one point on each side, the three half-plane failure events are disjoint and each has volume 1/3-2log2/9; capture b=2log2/3. Thus P=3a(e2-3e3)+6b e3. Both polynomial coefficients are positive and e2,e3 strictly Schur-concave on the allowed p_i<1/2. e2>1/4 with e3>0 and equilateral equality prove sharp bounds. Independent 220000 draws on four triangle shapes matched within 1.76 binomial standard errors; quadrature checks support conditionals but do not replace proof.

## originality

PASS

Best-of-knowledge comparison of the exact mathematical statement and hypotheses with accessible primary text and Resultary; no materially inspected prior statement logically supplies the complete final claim. Inaccessible relevant texts are identified as residual risks, not automatically classified noncovering.

## value

PASS

The exact boundary sampling law resolves a natural geometric-probability statistic sensitive to triangle shape, unlike area-uniform affine-invariant sampling. Its strict ordering quantifies how a physically natural arclength distribution compares to the classic interior benchmark, including all equality and degeneration cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
