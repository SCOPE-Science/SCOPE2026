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

The exact survival function gives f_b(t)=log((b+1)/b)-log(1-t)-(b+2)t^2/2 for t in [0,1). For b<=2 derivative is nonnegative; for b>2 only interior local minimum is at t_+=(1+sqrt((b-2)/(b+2)))/2, with positive endpoint f(0) and divergence at t->1. Envelope differentiation gives H'(b)=-1/[b(b+1)]-t_+^2/2<0; H(2+)=log 3-1/2>0 and H->-infinity. Thus exactly one threshold and explicit failure above. Supports eps>=0 including endpoint outside compact support; one-sided only. Independently solved H=0 at b=3.7534772184455018261094865454351.

## originality

PASS

Best-of-knowledge, implication-based comparison of exact theorem and primary findings; not a guarantee of globally exhaustive prior art. Neither standard Chernoff inequalities nor the prior variance-matched Bernstein correction entails precise if-and-only-if b<=3.753477218... for exact probabilities; prior stronger MGF claim is false for asymmetric beta without ruling out this weaker one-sided tail.

## value

PASS

Natural sharp one-sided variance-scale Gaussian tail question for a canonical asymmetric beta family: a nontrivial exact transition explains when the positive Bernstein correction can be omitted and supplies explicit failure deviations. Its exact b_star boundary is not a renaming of MGF sub-Gaussianity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
