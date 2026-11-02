---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The explicit phi(t)=e^-t(1+13t/20+t²/6) is continuous/integrable under both norms. Independently symbolically differentiated six-cone hexagonal Fourier F_z=2z²(Q+3z²)/(z²(z²+Q)²+p), Q=xi²-xi*eta+eta², p=xi²eta²(xi-eta)², and reproduced the exact polynomial P(Q,p) over ((1+Q)²+p)^3. The algebraic invariant 4Q³-27p=(xi+eta)²(2xi-eta)²(xi-2eta)² yields 0<=p<=4Q³/27. For Q<=21, P decreases in p over the allowed interval and endpoint factorization is positive; for Q>=21, discriminant is negative and p² leading coefficient positive. This is an all-frequency analytic proof of strictly positive density and hence strict Bochner PD. Independently obtained Fourier square section G_square(0,sqrt T)=4(T-9)(T-11)/(15(T+1)^4), negative exactly -4/219615 at T=10. Thus not square PD and not a square-positive-preserving m2 mixture. No finite-frequency scan is claimed as a proof.

## originality

PASS

Best-of-knowledge PASS for an explicit separating hexagonal radial kernel outside the earlier sufficient square/m2-mixture class. Xu (2015) gives positive-definiteness sufficiency but accessible abstract does not claim necessity; the original package connects it to an open question. The Fourier density positivity and negative square section provide an actual counterexample not included in the inspected 2015 abstract or the Resultary findings. Full Xu paper and Berens–Xu source could not be materially read here, including Oxford PDF storage blocker, so historical risk is clearly retained rather than declared resolved.

## value

PASS

An explicit globally certified positive Fourier-density hexagon-norm radial function that ceases to be positive definite under the affinely square/ell1 norm separates natural cones of radial positive-definite functions and gives a direct counterexample to necessity of a commonly used sufficient representation. The analytic global polynomial inequality is nonroutine; a single exact witness can be valuable without a complete cone classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
