---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: For u with valuation s<m, summing products bc=u over each allowed b-valuation i<=s gives (s+1)(q-1)q^{m-1}; for u=0, summing all b-shell kernels plus b=0 gives q^{m-1}[m(q-1)+q]. Writing A=(a,b;c,t-a) and x=2a-t, the determinant constraint becomes 4bc=Delta-x^2, so N=sum_x H(nu(Delta-x^2)). For valuation v odd, no cancellation is possible with a square; for even v=2h, cancellation occurs only in x-shell h. Simple-root lifting (2 invertible) gives exactly two roots at each quotient if the unit residue is square, with q^h lifts at full length. Counting valuation classes proves the displayed closed four-case formulas. Independently re-enumerated every trace-det fiber of matrices over Z/3, Z/9 and Z/25, checking the discriminant sum. General finite chain rings follow by these ring-theoretic counts, not finite experimentation.

## originality

PASS

PASS (qualified): Reiner treats a given characteristic polynomial over finite F_q, while Prasad–Singla–Spallone give normal forms/centralizer enumerations only for length two. Choosuwan–Jitman–Udomkavanich count fixed determinants over chain rings, a marginal that does not supply joint trace-determinant fibers. The all-length, odd-residue discriminant valuation plus unit square-class formula is not directly given by the inspected sources or Resultary search. It is based on classical Hensel lifting and may be an unindexed special case of known local orbital-integral or characteristic-polynomial counting formulas.

## value

PASS

PASS: Joint trace-and-determinant fiber sizes are natural conjugacy-invariant distributions for random matrices over finite local rings. The complete stratification across all nilpotence lengths and both equal/mixed characteristic is useful independently of fixed-determinant marginals and length-two similarity classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
