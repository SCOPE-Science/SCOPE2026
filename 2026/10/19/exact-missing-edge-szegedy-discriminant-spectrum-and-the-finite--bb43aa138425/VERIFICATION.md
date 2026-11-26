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

Absorbing marked columns give I_m and no marked-to-unmarked reciprocal entries. For uniform redistribution the distinct ordinary pairs have entry p and ordinary-defect pairs have a. The defect antisymmetric vector has eigenvalue zero, ordinary contrasts have eigenvalue -p with dimension b-1, and the remaining two orthonormal indicator vectors yield the compression with off-diagonal sqrt(2b)*a and ordinary diagonal (b-1)p, exhausting all dimensions. Its characteristic polynomial at L=(b+1)p is 2m/[(n-1)^2(n-2)], and L-lambda_- is positive. This proves the shift including m=0; the denominator tends to 1 for fixed m and to 1-alpha for proportional marking. Independently summing entries on the old uniform vector gives D_R=[2p+4b(p-a)]/k, equivalent to the claimed square-root formula. Since the ordinary and defect row sums differ for every b>=1 (use sqrt(1+1/(n-2))<1+1/[2(n-2)]), the Rayleigh inequality is strict. The square-root difference squared is asymptotic to 1/(4n), giving the extra 1/2 in the fixed-m coefficient. At k=2 the unmarked block vanishes and no strict comparison is claimed. Read frozen RESULT.md, VERIFICATION.md and verify.py; not a fresh execution. The recorded finite NumPy comparisons corroborate, but do not prove, the exact argument. No quantum search probability is established.

## originality

PASS

The missing-link model, old-vector deficit and its asymptotic are already in Giordano–Martin-Delgado. The symmetric decomposition is a standard quotient technique. The record's supported distinct conclusion is the exact actual discriminant shift and its sharp fixed-marked discrepancy from the quoted perturbative expression. The original paper mixes qualified first-order wording with a Proposition 4 heading and an all-orders inference; its exactly evaluated quantity is a Rayleigh quotient. Do not characterize every statement in that paper as an assertion of exact eigenvalue equality.

## value

PASS

The simple exact reduction resolves a concrete interpretive problem in a published perturbative model. At fixed marked count the usual old-vector estimate is wrong at leading order, even though it gives the right power for positive marked count; without marks it spuriously predicts a shift at all. This changes the phase coefficient and provides an exact benchmark for that physically motivated kernel, rather than merely restating a quotient principle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
