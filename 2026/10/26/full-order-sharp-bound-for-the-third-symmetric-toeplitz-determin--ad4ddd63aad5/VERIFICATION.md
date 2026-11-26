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

For s=1-alpha the logarithmic derivative is 1+2s omega/(1-omega). Integrating the Taylor expansion of its positive-power part and exponentiating derives a2,a3,a4, and expansion of the determinant factors it as stated. Two Schur steps on omega/z yield y=(1-r^2)b and c=(1-r^2)(d-conj(x)b^2), r=|x|, |b|=t, |d|<=1-t^2 (at r=1, Schwarz's lemma gives y=c=0). The resulting triangle majorants have maxima at r=1: independently recomputed Taylor coefficients and nonnegative deficit factorizations on 0<=r,t<=1 and 0<s<=1 in /workspace/reproductions/3.py (Python 3/SymPy) give M1=2(4+3s+2s^2)/3 and M2=2(7+6s+8s^2)/3 for the two scaled factors. The M1 deficit is strictly positive for r<1. It follows that equality in the product forces omega=xz, |x|=1; maximizing |2x-(2/3+2s+4s^2/3)x^3| forces x^2=-1. Both choices give the claimed values in both factors and integration gives the claimed functions. Radial Banach maps restrict to h_v(zeta)=zeta*phi(zeta v); since DF(z)z=(phi+Dphi(z)z)z, the support-functional condition on the reciprocal of the radial inverse derivative is exactly Re(zeta h_v'/h_v)>alpha. The factorial-normalized derivatives give the scalar Taylor coefficients. For the extremal lift phi=(1-i ell(z))^(-2s), phi is nonzero and its radial derivative multiplier is nonzero by the half-plane condition, hence DF is invertible by the rank-one formula. Its one-dimensional restrictions are starlike and it is injective since nonzero equal images must lie on the same complex line. The matching v-slice yields sharpness in each nonzero space. This checks the symmetric, not Hermitian, determinant and excludes alpha=1.

## originality

PASS

The supported advance is the sharp third-order formula on the previously unproved interval 2/3<alpha<1 and the complete scalar extremal classification. The constant, radial transfer and a sharpness witness are prior in the lower interval and are not credited as independently new there.

## value

PASS

The result completes the precise sharp parameter gap for a classical determinant under the same normalization, with no change of extremizer and an exact uniqueness analysis. The uniform proof explains why the same extremal behavior persists as alpha approaches 1; the Banach slice result transfers this improvement in each direction without claiming unrestricted Banach mapping sharpness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
