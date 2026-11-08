---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Reconstructed tilted 3x3 generator Q+diag(k,−k,Dk²) from model; independent SymPy determinant equals stated cubic and substitution λ(k)=L2k²+L4k⁴ makes coefficients through k⁴ vanish. L2=[c+b(b+2)D]/[(b+2)(b+c)]>0 and L4=c P(D)/[(b+2)^3(b+c)^3], with P=b(b+2)^3 D²−b(b+2)(4+3b+c)D+b(b+2)−c(b+c). Finite irreducible Markov spectral projection gives κ2=2tL2+O(1), κ4=24tL4+O(1), hence limit t kurt=6L4/L2². Quadratic discriminant=b(b+2)^2(b+c)^2(8+5b)>0, upward opening, constant term crosses at c*=(sqrt[b(8+5b)]−b)/2. Two positive roots only c<c*, b=c=r iff r<2; at b=c=1 independent exact simplification gives (27D²−24D+1)/(3D+1)². Passive occupation-time asymptotic Var[T0]/t=2bc/(b+c)^3 forces the positive D² term; an independent check of the source renewal transform agrees. Infinite limit derived analytically, not finite semigroup checks.

## originality

PASS

Best-knowledge PASS specifically for CORRECTED global sign-phase formula and switching threshold; source already derives model renewal transform and prints an asymptotic kurtosis formula, but the latter has an inconsistent D² coefficient (for equal active/passive rates its term vanishes although occupation-time variance forces positive). Thus exact source formulas contain the data in principle, but the full correct sign classification is not a simple substitution into source display. Risk of competing correction remains.

## value

PASS

A physically natural fourth-cumulant phase diagram for a tractable Markov intermittent transport model: a precise two-crossing (positive–negative–positive) kurtosis signature and exact switching threshold, despite strictly increasing long-run diffusivity. The negative and positive excess-kurtosis regimes distinguish migration mechanisms that second moments cannot identify. Natural full parameter classification, not chosen small slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
