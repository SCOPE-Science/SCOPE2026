---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Uniform simplex expansion of the sum and power-exponential one-coordinate CDF agree at order x^n and differ at order x^(n+beta). Their normalized signed coefficient is R_n(beta)-1 where R_n=product_{k=2}^n(1+beta/k)/(n!)^(beta/n). Log R is strictly concave with positive derivative at 0 and tends to minus infinity, hence exactly one positive root. AM-GM gives kappa_2=2, kappa_n>2 for n>=3. At n=3 the rigorous exact integer bounds imply 2<kappa_3<21/10<lambda_3. For beta>1 convexity and an all-components-large event give matching sum survival exponent -n^(1-beta); max survival exponent -C_n^(-beta). On the indicated interval signs oppose. Independent Python exact-integer checks of inequalities and bisection kappa_3~2.0629223972, lambda_3~2.191268131 corroborate (not replace) proof.

## originality

PASS

Best-of-knowledge beyond Okamura 2026 nonidentity and leading-origin/tail comparisons: the signed next-order origin coefficient, unique all-n phase boundary, and a proved open n=3 interval with opposite endpoint CDF signs were not in the inspected source. Failure of equality of distributions does not entail failure of both stochastic orders.

## value

PASS

Sum and calibrated maximum are natural aggregate versus extreme-risk statistics. The sharp lower-tail bias threshold, and a nonempty interval in which both possible usual stochastic orders fail, provide a structural phenomenon not reducible to observing nonidentical laws or a numerical CDF plot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
