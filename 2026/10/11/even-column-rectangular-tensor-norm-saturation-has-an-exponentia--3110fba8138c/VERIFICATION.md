---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Jensen/permutation symmetrization gives E|sum eps_j a_j|>= [binom(n,n/2)/2^n] sum|a_j|. Strictness for nonflat rows follows from a balanced sign vector with mean signed sum 0 after averaging permutations but nonzero values under swapping unequal positions. Equality of max over eps with average forces constant convolution of sign-row weights w with f(s)=|sum s_j| on antipodal cube G. For every nonempty even subset S (size 2j), integral Fourier coefficient (2(-1)^(j+1)/pi) integral_0^infty sin(t)^(2j)cos(t)^(n-2j)/t² dt is nonzero because both powers even and integral absolutely convergent. Fourier inversion forces w constant positive across all 2^(n-1) classes; converse uniform reps attains ratio, and compactness proves strict subthreshold. Independently evaluated coefficients/extremizing sums for n=2,4,6, finite only.

## originality

PASS

Best-of-knowledge mathematical comparison of the complete statement and stronger potential prior claims: The central coefficient identity and endpoint-column compression are prior work and not claimed novel; the particular finite-row saturation and classification are not consequences of the cited prior theorems without additional Fourier rigidity.

## value

PASS

Sharp exponential minimal-row threshold and complete equality classification for a natural Banach tensor norm extremum answer a genuine rectangular saturation question left by known dimension-independent 1-summing bounds; classification is structural rather than routine numeric evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
