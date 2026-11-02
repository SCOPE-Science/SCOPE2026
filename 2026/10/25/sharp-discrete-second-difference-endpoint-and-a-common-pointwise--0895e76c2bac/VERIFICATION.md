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

PASS. Zero extension of a length-d complex sequence gives N=d+2 curvature values b=Delta^2 a characterized exactly by two vanishing moments sum b=sum r b=0. The candidate symmetric b* has plus-one outside integer knots u=floor(N/4)+1, v=N-floor(N/4), minus-one strictly between, fractional tau=(N-4 floor(N/4)-2)/2 at knots (always in [-1,1]); it obeys moments and reconstructs a positive symmetric a*. For each coordinate ramp h_j(r)=(j-r+1)_+, subtraction of its affine chord across u,v produces a sign pattern matching b* at all nonzero sites, giving |a_j|<=a_j*||b||infty simultaneously for all complex a. Summing ramps gives quadratic W and W-chord=(r-u)(r-v)/2. This proves sharp l1 constant, dual monic quadratic discrete LAD minimum 2C_d, and elementary sums yield the four exact formulas by d mod 4, asymptotic C_d/d^3 ->1/32. Independent scipy LP over all coordinate functionals for each d=1..24 ran 300 optimizations and reproduced exact predicted maxima and common pointwise extremizer; finite evidence supports but does not replace proof.

## originality

PASS

PASS qualified: Hindov–Nitzan–Olsen–Rydhe solve all derivative orders for different right-hand exponent 2, and furnish a sign-preserving left-inverse theorem used as acknowledged general context, but their read main theorem does not give the exact l_infty second-difference four-class constant and simultaneous pointwise optimizer. Older discrete spline / LAD quadrature results may still provide equivalent formulas.

## value

PASS

PASS. The exact zero-extended second-difference l1-versus-linfty sharp embedding is a naturally motivated open endpoint relative to the source all-order l2 result. A full four-class length formula, sharp boundary effects, explicit least-absolute-deviation dual and a single extremizer optimal for every coordinate provide useful discrete optimal-recovery data. A natural complete support-length family need not solve arbitrary higher differences to be valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
