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

# Verification and scope

## Analytical obligations
The exact thresholds follow from necessary and sufficient vertex containment inequalities. The middle-phase antiderivative is valid only after verifying \(t-r<-1/2<x_L<t<x_R<t+r<1\), and it yields the strict local identity \(I_r(t)=M(r)-2(t-t_*)^2\). Global uniqueness uses the known concavity of \(\sqrt{I_r(t)}\), while vertical strictness uses positive-length neighborhoods around equal-half-width crossing points. These arguments quantify all real \(r>0\); there is no reliance on finite enumeration for universality.

## Independently constructed numerical checks
Run `python verify_overlap.py` using Python 3's standard library. It reconstructs the intersection by half-plane clipping in polygon-vertex coordinates rather than integrating the analytic formulas. The verified execution printed:

`TRIANGLE_DIAMOND_PROFILE_OK radii=11 translations=1980 strict_local=16`

The code tests radii on both sides of both exact thresholds, 1,980 reproducibly sampled translations, 16 perturbations of the middle optimum, and the exact equal-circumradius center comparison. Floating-point tolerances are stated in the code. These are corroborating finite computations, not substitutes for the proof.

## Scientific and historical limits
The theorem concerns a specified orientation of an equilateral triangle and a square; allowing relative rotations is outside scope. A complete historical-priority search of all pre-digital specialized literature is not claimed. Independent scientific audit has not been performed.
