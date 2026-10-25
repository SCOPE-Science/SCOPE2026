---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Before the last car parks in vacancy k+1, previous cars split into k left and r=n−1−k right valid parking lists; signed binary interleaving sum is Gaussian binomial at q=−1, zero for even m/odd k and binom(floor m/2,floor k/2) otherwise. The last car contributes (k+1)(−1)^r. This yields exact recurrence; separating even/odd EGF gives O=(zE²)′ and E′=E³+8zE²E′+4z²E²E″. Coefficient of z^m on RHS uses only prior E coefficients with nonnegative weights, while E³ strictly positive, inductively D_{2m}>0, then O positivity yields D_{2m+1}>0. The n=1 base and D0 empty convention addressed. Independent direct brute-force preference enumeration n≤5 and signed recurrence through n≤15 reproduced values D1..D8=1,1,4,11,72,335,2944,19449. No convergence of EGF needed (formal only).

## originality

PASS

Best-of-knowledge: compared mathematical objects, parameter ranges, equivalent transforms, prior stronger results and available exact tables; the specific final theorem is not known to follow from the inspected primary and Resultary findings. Pinsky gives full mass P(σ), hence a factorial signed sum computes the probability, but no strict even-minus-odd theorem or ODE positivity in read results. Chebikin–Postnikov evaluates a q=-1 inversion sum on *preference-word* or related P-parking stats, not inversion parity of final outcome σ; cannot transfer by relabeling. A known exact PMF logically determines D_n by summation over n! outcome permutations, but its positive sign for every n is a separate theorem. Word inversions and outcome inversions differ (n=4 signed totals 5 vs 11), so q=-1 identities for the former do not cover the latter.

## value

PASS

The final outcome-permutation sign is a fundamental but nonuniform statistic of random classical parking. A universal strict even bias (not obvious from pointwise probability weights), an exact quadratic-arithmetic recurrence and a positive formal differential mechanism form a mathematically motivated and reusable parity theorem. Different preference-word inversions are explicitly excluded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
