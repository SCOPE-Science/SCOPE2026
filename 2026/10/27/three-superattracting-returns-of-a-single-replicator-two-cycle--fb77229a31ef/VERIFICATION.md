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

The endpoints are fixed, and summing the log-odds increment over an interior two-cycle forces mean b. The exact centered solution with points b±d is obtained at A_b(d), strictly increasing in d by the positive artanh series, with range (2/[b(1−b)],∞) for b<1/2. The derivative factors in the cycle multiply to (1−A_b q(b−d))(1−A_b q(b+d)). At birth the factors tend to −1 each; at d→b the low-point factor tends to 1 while the other tends to −∞. At b=12/25, independent rational arithmetic confirms log(253/3)∈(4,5) at d=2/5, with factors of opposite sign, and log(2303/3)<7 at d=23/50, with both factors positive. Thus the signs alternate in the four ordered regions. The intermediate value theorem gives three disjoint interior zeros, whose distinct finite intensity values lie above 625/78; a zero derivative of the second iterate gives local superattraction. The strictly signed interior witnesses persist for b near 12/25, and both endpoint limits have the requisite sign throughout that neighborhood.

## originality

PASS

The branch, birth threshold, multiplier formula, and superstable period-two parameter curves are not new. The supported distinct finding is the exact analytic lower bound of three zero-multiplier intensities at one fixed nonsymmetric equilibrium and throughout an open neighborhood. The closest inspected earlier statements concern either a −1 crossing or numerical/large-coupling superstable curves, not a certified fixed-equilibrium triple return.

## value

PASS

The exact witness disproves monotonicity of the signed multiplier on a unique, continuously followed period-two branch, without switching among coexisting cycles or relying on plots. Its robustness in equilibrium makes the triple critical return a feature of this family rather than an isolated numerical coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
