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

In Hopf coordinates the complex exact-degree harmonic basis consists of torus weights (a,b) with |a|+|b|<=ell and parity, Jacobi factor P_s^(|a|,|b|)(0). Along winding (1,2) the surviving characters have frequencies a+2b. The outer range ell<=|k|<=2ell is present at s=0, and three congruence cases cover the central range, including explicit ell=16,k=0 rescue P_5^(4,2)(0)=42/32. Only ell=1,2 zero mode and ell=4 ±3 holes remain. Sampling characters on N-th roots aliases precisely mod N, proving exact rank. Independent Chebyshev Laurent-positivity recurrence checked all degrees ell<=84 and exact Jacobi consistency; the unrestricted claim depends on the complete arithmetic case split.

## originality

PASS

Explicit S3 Hopf/Jacobi harmonic basis is standard, but the fixed (1,2) cyclic rank and frequency support require an all-degree Jacobi nonvanishing argument and discrete aliasing analysis absent from inspected bases/S2 bandlimited sampling sources. Best-knowledge PASS with SU2 matrix coefficient equivalence risk.

## value

PASS

The (1,2) Clifford circle is a natural coupled-angular-frequency orbit in S3. Its complete all-degree Fourier frequency support and every finite cyclic sampling rank establish sharp identifiability and the striking failure of monotone interpolation (N=6 ranks 6,5,6), rather than merely rephrasing a basis decomposition. Other winding types/conditioning are outside scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
