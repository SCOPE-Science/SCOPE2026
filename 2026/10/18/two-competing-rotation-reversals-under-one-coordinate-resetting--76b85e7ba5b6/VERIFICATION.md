---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The positive spring matrix contracts the homogeneous evolution exponentially; each reset is a nonexpanding projection. The stochastic convolution from the infinite past exists in second moment by this bound, is stationary, and synchronous coupling gives uniqueness and convergence of the quadratic expectations for finite-second-moment starts. With A=2a+r, the stationary equations give u=2(T_x-cv)/A, w=(T_y-cv)/b, and (a+b+r-2c²/A-c²/b)v=-c(2T_x/A+T_y/b). Multiplication by bA produces the stated strictly positive D. Stationary product balance for XY (Y has no jump and the independent noises have no mixed covariation) gives J_all=-2(cu+bv). The chord from (X,Y) to (0,Y) contributes XY, so Poisson compensation gives J_jump=rv and flow=all-jump. Independent symbolic elimination and expansion reproduce all three currents, the equal-bath ratio and the limits. For T_y<T_x the flow numerator has positive leading coefficient and negative constant, hence exactly one positive root, the reported r_f; for T_y≥T_x its linear coefficient is positive and constant nonnegative. The affine factor for the full rate starts negative and rises through zero only at T_x<T_y<2T_x, giving the claimed r_a. The equality endpoints and r>0 signs in all four sectors follow immediately; there is no assertion of a finite reversal at T_y=2T_x.

## originality

PASS

Pass is for the pair of separate signed-area laws and mutually exclusive reversal sectors for Poisson projection onto X=0, not for the Brownian gyrator, stochastic area, moment closure, or resetting-induced reversal generically. The closest inspected claims share either the reset geometry or the observable, not their combination; the later fixed-point paper overlaps specifically in the continuous area observable but with a different moment balance and reversal mechanism.

## value

PASS

The choice of whether to include the actual reset movement in a signed-area measurement changes even the sign at equal temperatures and changes which temperature sector permits a reversal. The exact complete sign classification and cancellation of nonzero continuous transport by chords in the fast-reset limit quantify this observable dependence. This is a meaningful comparison for pathwise versus between-reset measurements, even though the moment technique is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
