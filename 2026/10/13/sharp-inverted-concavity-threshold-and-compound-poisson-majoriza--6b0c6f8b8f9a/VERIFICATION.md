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

For F_alpha(x)=1-(1+log(1+x))^-alpha, density alpha/[(x+1)(1+log(1+x))^(alpha+1)], the sign of derivative of x^2 f is sign B(x)-alpha with B(x)=((x+2)log(1+x)+2)/x. Direct algebra gives B_prime=q/x^2 and q_prime=x^2/(1+x)^2>0 with exactly one root; B blows up at x=0 and infinity. Unique minimum alpha*=(y+1/y)/2 where y-2-1/y=2 log y; independently solved y=5.635674835727276..., alpha*=2.906557937512901.... This is necessary/sufficient inverted-concavity for every alpha>0, equality allowed. Chen–Hu–Shneer–Zou Theorem 3 makes this precisely universal-in-lambda CP majorization for continuous ess-inf-zero severities. For larger alpha, the two roots split as (y-1) +/- y sqrt(2(alpha-alpha*)) + O(alpha-alpha*). For G(u)=F(z/u), G"(u)= (x^2 f(x))′|_{x=z/u}/u^2; negative local curvature produces positive one-jump CDF reversal at balanced vs unequal positive weights, dominating O(lambda^2) multi-jump remainder. Independent alpha=4 example gives Delta=0.002165083438733132..., positive for 0<lambda<0.0003982448427653; this is finite corroboration of exact proof.

## originality

PASS

Best-of-knowledge PASS: Chen et al. already proved the full general criterion (Proposition 2, Theorem 3) and calculated the same log-Pareto derivative (Appendix A Example 6), but only established sufficient alpha<=2. Submitted scalar minimization yields necessary/sufficient alpha<=2.90656, postcritical geometry and explicit CP reversal. It must not claim general characterization as new; a separately published optimization of that already displayed derivative remains an originality risk.

## value

PASS

Log-Pareto is explicitly a studied infinite-mean severity; finding complete admissible alpha range for risk aggregation moves the prior provable family frontier 2 to exact 2.9065579 and gives a physical low-intensity two-weight reversal above it. The exact family boundary and failure mechanism are mathematically motivated despite being a specialization of a known general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
