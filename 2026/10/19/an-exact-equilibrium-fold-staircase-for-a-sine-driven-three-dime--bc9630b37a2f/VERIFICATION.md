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

Eliminating y for x nonzero forces z to satisfy cz^2-dz-(ag/k)x^2=0; the sign of sin(x)/x selects exactly one quadratic root on each half-wave. At x=0 only (0,0,d/c) remains; nonzero multiples of pi cannot occur. For N=u|z|, uN'/N is 2+d/s on the negative branch and 2-d/s on the positive branch. On the first lobe u cot(u)<1; on later lobes the derivative of u cot(u) minus the elasticity is at most 1/2-u+1/u<0. This gives one interior nondegenerate minimum before each midpoint, with no duplication other than the stated reflection pair and the correct count at equality. The transverse minor is k(2cz-d) and is nonzero; reduced derivatives in u and b give a quadratic equilibrium fold and a singular full Jacobian, without a dynamical saddle-node assertion. Writing u=L-delta yields u tan(delta)=2+O(1/u), hence delta=2/L+O(L^-2). Expanding u|z| and 1/|sin(u)| gives the alternately signed linear threshold term; T_m=A pi^2 m^2+O(m) confines all count uncertainty, including equalities, to a bounded window. For the baseline, u>=7/2 on negative sine lobes is excluded by N_+ >= A u^2 + D u>10, and pi<u<7/2 by |sin(u)|<1/2; u>=2pi on positive lobes is excluded by N_- >= A u^2 - D u>10. Independently solving the baseline equation after substituting z=-10 sin(u)/u into the quadratic gave u=2.593336204649302275, y=-0.967775202592809262, z=-2.009766470845745569.

## originality

PASS

The audited distinct claim is the global all-positive-parameter branch classification, not the vector field or scalar fold calculus. The related conservative-limit fold concerns a boundary where three parameters vanish, and the most similar exact sine census is for a different vector field. Neither gives the positive-parameter infinite fold count or its asymptotics. Ramar's inaccessible full text remains a specific limitation of this best-of-knowledge decision.

## value

PASS

The count is for all of R^3 and all positive forcing amplitudes, with exact handling of threshold equality, not a search window or a single fixed-parameter root tally. The one-fold-per-lobe mechanism, asymptotic threshold spacing and unbounded sqrt(b) census provide a reusable classification of a motivated nonlinear system. The exact baseline count tests a specific literature parameter set without attributing any claim about attractors or stability to the census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
