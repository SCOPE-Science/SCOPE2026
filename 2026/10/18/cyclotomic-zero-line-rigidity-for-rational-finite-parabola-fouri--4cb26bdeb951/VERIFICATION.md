---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Prime cyclotomic irreducibility makes a rational polynomial Σ_j d_j ζ^j vanish exactly when all p coefficients d_j coincide. At a=0,b≠0 the exponent permutes the field, hence vanishing is equivalent to f being constant; at (0,0) the sum must vanish. At a≠0 the quadratic exponent has only (p+1)/2 distinct outputs; at least one aggregate d_j=0, forcing all to zero and hence cancellation on every pair {t,s−t}, s=−b/a, plus zero at fixed point s/2. Two reflection-odd centers give invariance under a nonzero translation, forcing a nonzero f to be constant and simultaneously odd, impossible. Reflection uniqueness yields all four shapes. Sign support 2r can be balanced but nonreflection-odd (one origin zero), balanced reflection-odd (a unique p-point line), or unbalanced (zero zeros); counting support and reflection orbits yields the displayed binomial formulas. Independently enumerated all 3^5−1=242 and 3^7−1=2186 nonzero {-1,0,1} arrays, applying exact integer exponent bucket sums at every Fourier frequency: for p=5 classes 0:190,1:10,4:2,5:40, and p=7 classes 0:1792,1:210,6:2,7:182. The complete all-prime proof uses irreducibility and orbit counting, not the finite enumerations.

## originality

PASS

Best-of-knowledge PASS after comparing to Li’s 2026 finite-parabola paper: the prior sharp p+k−2 even-support complex bound is acknowledged; the rational four-shape classification and full prime/sign census are not a direct consequence of the abstract’s unrestricted-complex maximum, since a maximum over a larger coefficient class does not fix the rational subset image. However the original/updated Li preprint has zero-set rigidity machinery and could state or imply a rational-data corollary in unread sections; that is a material risk, not a claim of whole-text exclusion. Published Resultary finite-parabola records concentrate on complex small-support or ring-extension phenomena, not the exact arithmetic coefficient field of this theorem.

## value

PASS

This is a field-sensitive arithmetic rigidity fact for a natural Fourier transform, with a full classification for every input rather than only extremizers. The exact labeled sign-class sizes and rational-vs-complex sparsity gap are natural invariants useful when signals use rational or one-bit amplitudes; their intrinsic motivation precedes the computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
