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
# Verification

The universal certificate is the analytic proof in `RESULT.md`. Its critical steps are:

1. For \(m\ge3\), the explicit singleton polynomial
\[
P_m(\theta)=1+\sec\!\left(\frac{\pi}{2m}\right)\cos\theta+\frac{(-1)^m}{m}\tan\!\left(\frac{\pi}{2m}\right)\cos(m\theta)
\]
is nonnegative on the entire circle. The transformed Chebyshev expression is the gap from the tangent at \(\cos(\pi/(2m))\), and the proof verifies global support of that tangent.
2. The zero set of \(P_m\) is exactly \(\pi\pm\pi/(2m)\). At those contacts the \(m\)-th harmonic vanishes.
3. The added \(n\)-th harmonic vanishes at both contacts exactly when \(\cos(n\pi/(2m))=0\), equivalently \(n\equiv m\pmod{2m}\). Contact evaluation then forces the singleton bound.
4. Off resonance, the explicit perturbation
\[
R(\theta)=\cos\theta+\frac{2\cos(\pi/(2m))}{(-1)^n\cos(n\pi/(2m))}\cos(n\theta)
\]
is strictly positive at both contacts. Continuity plus compactness gives a sufficiently small positive perturbation parameter and hence strict improvement.

The script `artifacts/verify.py` performs bounded numerical checks of these formulas, the contact values, the resonance equivalence, and representative perturbations. Those checks are corroborative only; no finite enumeration is treated as proof for unbounded \(m\) or \(n\).
