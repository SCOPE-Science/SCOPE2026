---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For 1<p<2 and equal-strength rank-one A=a x*, B=b y*, Gram factorization gives denominator eigenvalues 1±c and numerator squared singular-value product (1-c²)(1-d²), trace bounded by 2+2cd. Because p/2 lies in (1/2,1), maximizing phase and then strictly concave output overlap yields d=tanh((p/(2-p))atanh(c)). The remaining derivative equation tanh u+tanh(gamma u)=2tanh(pu) has one positive root by the monotone hyperbolic auxiliary ratio, with endpoints quotient 1. Implicit-root expansion yields kappa(p-1)^2-kappa(p-1)^3. I independently bracketed all positive derivative zeroes over 0.001..10 for p=1.05,1.2,1.5,1.9 and computed maximizing constants 1.000522932,1.007324966,1.036414357,1.08692083, consistent with unique interior maximizer. Finite scanning does not establish uniqueness; source monotonicity proof does.

## originality

PASS

Qiu 2026 proves the unrestricted optimum for p>=2 and exhibits analytic counterexamples to the proposed sub-two formula, including rank-one reductions. The assessed statement concerns exact global optimization across both equal-strength rank-one overlaps for every 1<p<2 and its sharp trace-endpoint expansion, not the unrestricted p<2 constant. Pang and Zeng–Liu–Ratnavelu independently refute earlier unrestricted conjecture. A direct theorem implying full optimization was not identified in bounded indexed searches; alternative rank-one optimization not ruled out.

## value

PASS

Equal-strength rank-one matrices are a natural extremal test family for a prominent failed unrestricted Schatten inequality. Exact maximizers and the quadratic trace-endpoint scale provide a rigorous sharp lower benchmark for the still-open unrestricted problem, not an arbitrary rebranding of a numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
