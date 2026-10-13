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

The symbolic proof reduces singularity detection to the equations \(4z_i(S+t z_i^2)=0\). For \(t\ne0\), any singular point has \(k\in\{1,2,3,4\}\) nonzero coordinates with equal nonzero square and therefore \(t=-k\). This is an exhaustive argument, not a finite parameter scan.

`verify.py` then checks the finite consequences of that reduction. It enumerates the projective support/sign representatives and obtains counts \(4,12,16,8\); evaluates the gradient equations; constructs the affine three-variable Hessians and obtains determinants \(64,-512,2304,-8192\); checks \(Q=k\ne0\) at normalized node representatives, which certifies transverse smoothing by the pencil parameter; and checks that \(68+4+12+16+8=108\).

The discriminant degree \(108\) is proved independently of the code: the discriminant is the resultant of four cubic partial derivatives, with resultant degree \(27\) in each input's coefficients. No claim is made about a local primary decomposition at the double quadric beyond the resulting intersection multiplicity \(68\).
