---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Mobius inversion of the gcd(a,n)=1 indicator gives C_a(N)=sum_(d|a)mu(d)*floor(N/d). Inclusion--exclusion of the common pair gcd gives J_a(N)=sum_(d<=N,(d,a)=1)mu(d)*C_a(floor(N/d))^2. Independent arithmetic checks give C_6(10)=3, C_3(4)=3 and J_3(4)=5, J_5(6)=13, so finite inequalities 3/10<1/3, 5/9<6/pi^2, 13/36<96/(25*pi^2) strictly hold. A separate direct pair enumeration matched Mobius counts on 176 (a,N) parameter pairs. For fixed a, periodicity yields C_a(M)/M->phi(a)/a, and absolute domination by d^-2 allows interchange of Mobius sum and N->infinity, producing the stated Euler product. The limit is fixed-a, not uniformly simultaneous in a and N.

## originality

PASS

Original source propositions explicitly assert the finite-uniform inequalities, but use invalid independence/multiplication of divisibility probabilities. The correction is not covered by those false statements. Standard Mobius inversion is prior mathematical machinery; the new contribution is identifying three exact counterexamples to the specific published probability bounds and replacing their proof mechanism while preserving the fixed-a limit.

## value

PASS

These lower bounds feed into a published repeated-sampling estimate for a continuous-variable period-finding proposal; correcting their finite-cutoff scope addresses a concrete logical dependency, rather than an arbitrary coprime-count exercise. It does not invalidate the quantum algorithm or physical distribution analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
