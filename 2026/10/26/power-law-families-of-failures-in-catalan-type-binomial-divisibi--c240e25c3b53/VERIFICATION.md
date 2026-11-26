---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Here m=a+b is a unit modulo p, so s exists, q-1=mw>0, w is a p-adic unit, and bw is -1 modulo p. The base-q products mn and an have respectively digits epsilon_j(q-1) and epsilon_j aw, all in [0,q-1], with no cross-block carry. Within every occupied block the top base-p digits are all p-1, so every Lucas factor is a unit; unoccupied blocks are zero on both sides. Since epsilon_0=1, p divides bn+1 and does not divide the binomial. The digit strings of n itself have digits 0 or w, so they are distinct and strictly below q^r. At r=floor(log_q X) this gives the exact stated lower bound, at least X^delta/4. The p-adic witness closure consists exactly of the infinite choices by compactness of binary sequence space and density of finite truncations. Two choices first differing at j have distance p^(-sj); the length-r cylinders are intersections with residue-class balls of radius q^(-r). Cover by the 2^(r-1) cylinders for the dimension upper bound. Their uniform Bernoulli masses are 2^(1-r); for arbitrary small radii between successive q-powers the same cylinder bound gives a constant times radius^delta, proving the reverse bound by mass distribution.

## originality

PASS

Guo–Krattenthaler already prove qualitative infinitude under the same prime-factor hypothesis and give the seed. The supported distinct contribution is the arithmetic construction of independently selectable blocks meeting both divisibility constraints, and hence a quantitative lower count and the corresponding explicit p-adic subset. No credit is assigned for Lucas's theorem or general path-set dimension theory.

## value

PASS

The result strengthens a natural qualitative infinitude theorem by replacing isolated witnesses with a uniformly described power-law family, introducing a positive-dimensional geometric substructure. Even a nonoptimal exponent quantifies how often the failures can be guaranteed under the original hypothesis, which the earlier prime-power sequence does not achieve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
