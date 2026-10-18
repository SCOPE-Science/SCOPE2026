---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification details

Build the included `verify_p11.cpp` with C++17 and optimizations, then execute. Its deterministic exact-arithmetic enumeration of six affine support representatives checks all \(6\binom{120}{3}\) normalized zero-row seed triples and every resulting Fourier evaluation. It confirms six orbit sizes \(55,110,110,55,110,22\), no noncollinear rank-deficient triples, six-zero coefficient rays per representative \(1210,605,3025,0,605,0\), and total \(532400\).

Actual completed execution reported:

`VERIFY_OK exact cyclotomic census: 462 supports; six affine orbits; 532400 sharp projective rays`

`TOTAL_PROJECTIVE_RAYS=532400`

The finite calculation is exhaustive, not sampled. The proof of its comprehensiveness uses four independent zeros, the prime Fourier minor theorem, and the absence of noncollinear rank-three degeneracies (also checked exactly). A directly constructed six-zero witness was checked separately, and its zero set for the first orbit is \(\{(0,0),(1,0),(2,5),(3,5),(5,4),(9,1)\}\).

All integer coefficients stay small enough for signed 16-bit arithmetic (each determinant has at most \(48\) terms, and a Fourier sum has at most five such minors; the maximum possible absolute sum is below \(32767\)). No independent external audit was performed. This does not claim conclusions for other primes.
