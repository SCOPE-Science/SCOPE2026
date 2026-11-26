---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Use P=diag(u,v), u=1-ah, v=1-bh, and Q=P+K with K=tJ, t=ch, J the skew unit rotation. Uniform sampling yields four times the IID-minus-RR matrix as the sum of the Gram matrices of P² and Q² minus those of PQ and QP. Expand with A=P², B=PK, C=KP, E=K²=-t²I: Q²=A+B+C+E, PQ=A+B, QP=A+C. The surviving terms are 2AE+E²+B^TC+C^TB because B+C is skew; B^TC=C^TB=t²uvI. Thus 4D=t⁴I+2t²uvI-2t²P², giving the displayed polynomial. For 0<h<1/b the y coefficient is positive and the x coefficient has its only positive-step zero at h_*=2(b-a)/(2a(b-a)+c²). Its placement inside the interval is equivalent to c²>2(b-a)², with all-direction weak RR dominance at equality and strict away from the x axis there. Substitution at the three rational steps gives all the recorded diagonal entries. The example Frobenius bound sqrt(45)/2<4 ensures h<1/l at 1/10 and 1/4; the contraction defects have positive leading minors (for Q their determinants are 1421/40000 and 65/1024, respectively).

## originality

PASS

The exact common-saddle simultaneous-SGDA risk matrix and the sharp all-direction crossover for one uncoupled and one coupled component remain distinct after comparing the closest formulations. Credit earlier directional and step-size reversals in minimization and opposite-coupling saddle games as material related coverage; the generic possibility of reshuffling underperformance and the four-path expectation identity are not new claims.

## value

PASS

This is a minimal and motivated test of whether common saddle, strong curvature and stable component maps suffice for a uniform finite-epoch sampling order. They do not even as h tends to zero. Moreover the exact cutoff and the same-instance contractive crossover show that increasing rather than decreasing the step can restore the desired pointwise ordering. That is a useful quantitative boundary, not just an arbitrary two-by-two multiplication or a claim of asymptotic superiority.

The dated certificate retains the supplied scientific assessment, sources and limitations.
