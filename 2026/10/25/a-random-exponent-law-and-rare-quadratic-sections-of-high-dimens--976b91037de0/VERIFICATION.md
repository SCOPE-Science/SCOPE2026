---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For generic hyperplane H separating K of the m simplex vertices, each section vertex is a crossed edge and exactly V=K(m-K). Independently verified direct crossed-edge enumeration for synthetic finite samples. A Gaussian vector with centered radius R and order statistics gives the correctly width-tilted Crofton law E[(1/R)int f(K(s)(m-K(s))) ds]/E(W/R), not uniform normal plus uniform offset. Its exact expectation is binom(m,2) E|Z1-Z2|/E range=binom(m,2)/(sqrt(pi) mu_m). Gaussian range endpoints at ±sqrt(2log m), concentration R/sqrt(m)->1 and width tilt in L1 yield a limiting uniform offset U in [-1,1]. Mills tail and binomial concentration imply log V/log m -> 2-U^2; for fixed 0<a<1/4, empirical central quantiles give an interval of length 2q_a+o_L2(1), and ratio to Gaussian range proves sqrt(2 log m) Pr[V>=a m^2]->q_a and the conditional marked law. No inference of infinite asymptotics from simulations.

## originality

PASS

Existing Gaussian mean-width results for regular simplices and probability laws for Haar CENTRAL sections lack translation conditioning; results on hypercube affine sections involve a different body; general combinatorial bounds on section vertex counts do not determine Crofton probabilities. These primary and indexed results do not imply the three stated affine-section asymptotic laws at fixed m and in the m→∞ limit. Priority is best-of-knowledge.

## value

PASS

The number of vertices in random sections is a canonical geometric-probability statistic; the sharp nonconstant random polynomial exponent, exact mean, and 1/sqrt(log m) rare high-complexity law quantify a strong mean-versus-typical discrepancy not captured by known central-section results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
