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

In the orthonormal monomial basis the rows become a_k*zeta_j^k/sqrt(S_0) and k*a_k*zeta_j^k/sqrt(S_2) after unit-modulus scaling of the ordinary derivative rows. Factoring columns and rows out of the confluent Vandermonde gives the eighth power of each pairwise angular distance. Hadamard equality forces the first n-1 node power sums to vanish, so Newton identities give precisely the regular n-gon. The value comparator has the analogous regular 2n-gon equality case. The log-radius derivatives are governed by the degree means, each strictly increasing by its positive variance; their endpoint means bracket the desired roots. A unitary DFT in each set of rows pairs columns j and j+n, including the j=0 block. Near t=n the lost Poisson tails, also with each fixed degree-moment factor, are exponentially small. Thus the stationarity means are mu_0=t+O(exp(-cn)) and mu_2=t+2-1/(t+1)+O(exp(-cn)); this gives the stated two radii. At t_V the exact same-radius quotient times 4^n tends to 1 since S_2/S_0=n^2-1/4+o(1). At t=t_V+s the Hermite log-derivative tends uniformly for bounded s to -2-2s; integrating to s=t_H-t_V tending to -1 gives a gain of 1 in log determinant, hence factor e. The limit is for det(M* M) and under separate finite-space row normalization on one circle, not a condition-number or unrestricted planar result.

## originality

PASS

Credit classical confluent Vandermonde and circle Fekete arguments, and do not claim the value-only optimum as new. The closest finite first-jet determinant result uses different row normalization and has a different radial optimum. The specifically supported addition is the exact common-circle design for independently normalized finite-space value and derivative functionals, including its sharp optimized comparison to distinct value sites. No equivalent covering result was identified in the checked evidence.

## value

PASS

The comparison holds measurement count and row norms fixed while changing co-location, so the exponential determinant loss answers a concrete finite sampling design question. The sharp e multiplier comes from optimizing a genuine one-unit radius shift and cannot be read from the angular Vandermonde alone. The full block spectrum also enables follow-up analysis without claiming that the determinant optimizer minimizes conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
