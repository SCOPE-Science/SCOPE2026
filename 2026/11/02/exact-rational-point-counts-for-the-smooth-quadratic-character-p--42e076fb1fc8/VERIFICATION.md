---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

With m=(q-1)/2 and p≥5, x^m=chi(x) in Fq. Four character signs sum to an integer in [-4,4]; vanishing mod p is equivalent to integer zero. Write A_q=1+(q-1)#C and use Fourier character orthogonality to extract [T^0] of a four-fold convolution. For nonzero frequencies Fourier factors are u+chi(t)beta G, G²=chi(-1)q; split epsilon=±1, use exact Laurent coefficients [T^0] f0^4, u^4, u²beta², beta^4. Independent symbolic algebra verified both all-q polynomial coefficient identities, yielding 3(q-1)^2/8 or 3(q²-4q+11)/8 by q mod4. Coordinate-axis signs force no points when chi(-1)=+1 and exactly [0:1:-1] and permutations when chi(-1)=-1. Smoothness/geometric integrality follow the reconstructed derivative/Frobenius contradiction, p>3. Direct brute enumeration over thirteen prime fields corroborated; extension fields included analytically, not independently enumerated in this run.

## originality

PASS

The originating Asgarli–Ghioca–Yip full article explicitly proves smoothness and the blocking/nonblocking behavior for exactly this polynomial, including existence of axis points in the q=3(mod4) case. Its inspected Section 7.2 Claims 7.2/7.3 does NOT give either all-q exact total rational-point count. The related 2022/2023 statistical plane-curve article does not determine this family-specific cardinality. Standard Gauss sums are prior ingredient; a historical equivalent count remains possible.

## value

PASS

The cardinality of the rational point set is an essential quantitative invariant of a natural exceptional smooth blocking curve family. The exact two-congruence formulas show asymptotic density 3/8 and the sharp axis-incidence dichotomy, strengthening simple blocking/nonblocking existence without claiming a zeta function for fixed curves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
