---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For b>0, gamma>0, m>0 and identical endpoint baths, the six-dimensional Ornstein–Uhlenbeck drift is dissipative with no nonzero zero-dissipation invariant subspace (the pinned chain is Hurwitz). Sum/difference of endpoint coordinates reduce nonequilibrium covariance to eight Sylvester equations; their determinant is 4D(m)/m^2 and their cross-momentum entry gives K=gamma[1+gamma^2(b+1)m]/[2D(m)]. Direct algebra gives 1/K(m)-1/K(m*)=2gamma(b+1)^3(m-m*)^2/[1+gamma^2(b+1)m], m*=1+b/(b+1)^2. This positive-square identity verifies positivity and unique global optimum for every positive m,gamma,b; derivative also verifies strict increase then decrease. Independently solved the FULL 6-by-6 stationary covariance (not merely the reduced solver) at four exact rational b,gamma,m triples and symbolically verified the inverse-conductance square with independent SymPy algebra. Distinguish the finite covariance checks from the unrestricted polynomial proof.

## originality

PASS

Best-of-knowledge priority judgment: close primary sources and published indexed findings are compared by mathematical statement, not just titles. Known general/ingredient results are credited; the precise asserted complete result is not shown to be covered by the material actually examined. Explicit source-access and possible stronger-result residual risks remain and do not become fabricated negative bibliographic claims.

## value

PASS

A pinned three-site chain with one tunable inertial defect is the smallest symmetric nontrivial thermal transport problem. The bath-independent optimum and its exact resistance penalty distinguish center-mass optimization from generic Green-function conductance formulas and give a sharp physically interpretable benchmark for harmonic defects. The all-positive-parameter classification is not merely a restatement of the Green-function method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
