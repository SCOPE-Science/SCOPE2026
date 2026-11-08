---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The identity exp(2πif_μ(s))=(z−μ)/(z(1−μz)) converts antipodal two-cycle condition into z^5−μz^4+μz−1=(z−1)(z⁴+(1−μ)(z³+z²+z)+1). The reciprocal quartic gives w²+(1−μ)w−(1+μ)=0, two w roots in (−2,2), hence four antipodal nonfixed points. All DT have positive entries and determinant one, so every fixed point of T² is nondegenerate (positive 2×2 determinant-one matrices have trace>2). Compact continuation from cat map count |det(A²−I)|=5 and unique fixed point proves two-cycle exhaustiveness. The +/- orbit derivatives agree and their exact Poisson kernels give the stated arcosh exponents, separation, linear μ onset and distinct square-root μ→1 laws. Direct torus double iteration and full Jacobian eigenvalue checks were performed for five μ; they are corroborative, not the global proof.

## originality

PASS

Best-of-knowledge independent search and theorem-level comparison. Transfer-operator resonances and numerical local expansion profiles are different invariants from explicit eigenvalues on each of the two primitive period-two cycles. A general trace identity can encode aggregate orbit data but not directly supply the two individual radical exponents without orbit isolation. General Anosov structural stability ensures period-two count, not this algebraic classification or exact multiplier splitting and endpoint ratio. A stronger-looking operator theorem lacks a demonstrated implication to the explicit orbitwise expressions. The new burden is solving the reciprocal quartic and evaluating both orbit Jacobians. No direct theorem-to-corollary implication of full closed-form exponents was identified from inspected prior statements. An unsuccessful search alone is not evidence of priority. Actual primary material read and remaining limits below.

## value

PASS

A complete orbit-resolved prime-two spectrum is a natural exact periodic-dynamical invariant for the analytically specified nonlinear Anosov deformation. The strict splitting, first-order gap, and differing singular-edge scaling are not recoverable from general hyperbolicity or from an unweighted count of periodic points; precise local instability is useful in trace/periodic-orbit studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
