---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For Brownian generator d²/dx² the time-changed zero-start cycle is the integral of |B|^alpha up to the first hit of ±L. The even Feynman–Kac solution of u''=s|x|^alpha u with u(±L)=1 yields the reciprocal hypergeometric transform. Its linear term gives m=L^p/[p(p-1)], p=alpha+2, and expansion of the reciprocal at zero gives Var(Z)=1/(b+1) after normalizing Z=cycle/m. The Bessel product F_b(z)=prod_k(1+z/zeta_{b,k}) identifies Z as a sum of independent exponentials of rates zeta_{b,k}. This gives a continuous nonlattice law, exponential moments below the first rate, and an exact logarithmic survival exponent -zeta_{b,1} by a first-term lower bound and Chernoff bounds. On z>-zeta_{b,1}, (log F_b)'=sum_k 1/(z+zeta_{b,k}) strictly decreases from infinity to zero, so the analytic SCGF inverse has increasing slopes from zero to infinity. The exponentially tilted renewal kernel has mass one and finite mean; e^(-lambda u) P(Z>u) is continuous and exponentially bounded because lambda>-zeta_{b,1}. The key renewal theorem yields the claimed SCGF for every real tilt. Gärtner–Ellis gives the good rate at speed t/m, with the zero-current value also verified by the survival event. Strict convexity on the effective domain follows from strict increase of the optimizing tilt, and the exact upper-tail limit follows by continuity of the good rate and monotonicity above one. The modified Bessel asymptotic gives lambda(theta)~theta²/(4b); bounding it between nearby quadratics and maximizing gives I_b(j)~b j². The positive-power coefficients at every order >=2 increase strictly with b, forcing a smaller positive-tilt SCGF for larger b; evaluating the second transform at the first model's positive optimizer proves strict rate ordering for every j>1. The standard renewal mean and variance asymptotics apply to this continuous law with exponential moments, giving the Fano factor. An independent rational check reproduced the moment normalization and coefficient ordering (four b values, orders 2–12); at j=1.5 reproduced rates ranged from 0.172791253322 at b=1/2 to 0.206209753518 at b=3/4. These are corroboration only. The frozen verifier was inspected, not run; its reported 286 checks are not formal verification or independent attestation.

## originality

PASS

The cycle transform and mean are covered, and the count SCGF mechanism is standard renewal theory. The supported distinct claim is the explicit normalized reset-count deviation profile, notably its strict all-upper-tail rate comparison in sluggishness. None of the checked closest results supplies that comparison or the full count profile. Priority is not certified.

## value

PASS

At each model's own mean reset rate, the theorem contrasts the cost of both moderately and arbitrarily elevated currents, not just their local variance. It resolves which process is exponentially less likely to sustain any fixed j>1, and separates the physical clock scale from shape effects by giving both sharp rate edges. This is useful specifically for the threshold-reset observable; it does not assert an ordering at equal unnormalized currents or for the lower tail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
