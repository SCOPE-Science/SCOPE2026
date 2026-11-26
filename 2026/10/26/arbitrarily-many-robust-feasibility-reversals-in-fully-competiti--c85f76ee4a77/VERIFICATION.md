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

For an isolated pair the stated inverse gives two positive coordinates below c and above b only. At c and b a coordinate is zero; at sqrt(bc) the rows are proportional but the right-hand sides are not, so no exceptional positive solutions fill the gap. The disjoint pair gaps interlace the listed witnesses. At a gap midpoint the designated numerator is -1/2 and the determinant is 1/4, so that coordinate is -2 before coupling. All witness matrices are nonsingular; the positive and negative coordinate margins persist under small positive off-block coupling and then on an open neighborhood in the zero-diagonal off-diagonal parameter space. The resolvent bound is valid since M(n-1)epsilon<=1/8 and the numerator is at most delta/16. Invertibility and the strict signs persist on alpha-intervals about the witnesses, and the negative intervals separate the positive components regardless of behavior at other singular parameters. Each early Jacobian has a saddle block (negative determinant); the remaining blocks have either a saddle or two eigenvalues with negative real parts, and a singleton has eigenvalue -1. The hyperbolic splitting and an unstable direction survive perturbation. At the final witness the symmetric part is positive definite by strict diagonal dominance: paired rows have within-pair symmetric coefficient < b_k and cross sum < 1/2; a singleton's row sum is (n-1)epsilon<1 for n>=3 under the imposed coupling bound. The relative-entropy Lyapunov derivative is strictly negative off equilibrium, and its sublevel sets are compact inside the positive orthant, proving convergence from every strictly positive initial state. This does not claim stability within entire components.

## originality

PASS

Re-entrant feasibility for uniform self-limitation, the sufficiently-large-alpha feasibility tail, two-species exclusion versus coexistence, and standard diagonal Lyapunov reasoning are not credited as new. The closest inspected primary result shows finite reversals and a random-community asymptotic. The distinct claim is the deterministic, growing component lower bound on an open set with all off-diagonal competition entries positive, with a stability contrast at selected witnesses. It is not given by the identified finite examples or the general final-threshold method. This is a best-of-knowledge assessment.

## value

PASS

The construction shows that one scalar diagonal loading can generate arbitrarily complicated feasible sets even in completely connected competitive communities, in contrast to finite reversals or typical behavior in a random ensemble. Strict sign margins distinguish a robust parameter-space phenomenon from isolated singularities. The instability/global-attraction contrast prevents interpreting the early positive solutions as robust dynamical coexistence and makes the witnesses useful for separating feasibility from stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
