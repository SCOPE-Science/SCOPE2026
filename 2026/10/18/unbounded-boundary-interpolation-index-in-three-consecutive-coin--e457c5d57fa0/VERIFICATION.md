---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Substitution T=x+y+z and s=k+3+r-T into (2k+1)x+(2k+2)y+(2k+3)z=(2k+1)(k+3+r)+1 yields y+2z=(2k+1)s+1. Nonnegative x,y,z force s>=0 and (2k+3)s<=2(k+3+r)-1<=4k+3<2(2k+3), hence s=0 or1. These yield precisely C=(k+2+r,1,0) and D_j=(j,2(r+1-j),k-r+j) for 0<=j<=r+1. Exactly C,D_0,D_(r+1) are boundary. Projection of homogeneous solution lattice to (x,y) is kernel modulo c=2k+3 of a surjective homomorphism, index c; determinant of boundary differences is (r+1)c, yielding lattice index r+1. Unique barycentric coefficients give denominator (r+1)/gcd(j,r+1) and D_1 has unbounded denominator. Direct small-k exhaustive nonnegative solution enumeration corroborates; the proof is universal.

## originality

PASS

Prior He–Shiue–Venkat discusses boundary interpolation and Binner has an earlier counterexample to a different cardinality formulation. This theorem neither claims first disproof nor contradicts unrestricted rational coefficients: it computes a sharp unbounded integral normalization index in a sparse uniform consecutive-denomination family. Best-of-knowledge PASS with material unread full §3 risk.

## value

PASS

Integer versus rational boundary interpolation is a natural question in 3-variable Frobenius fibers; a precise saturation-index obstruction even with exactly one solution on every edge is a motivated, unbounded structural phenomenon, not merely a small numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
