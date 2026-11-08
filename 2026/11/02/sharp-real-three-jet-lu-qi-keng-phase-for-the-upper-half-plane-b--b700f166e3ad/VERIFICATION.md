---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

With K(z,w)=-1/[pi(z-conj(w))^2], factorial derivatives in the canonical Riesz family and real coefficient vector (1,a,b) cancel odd powers and give F(t)=1+6(b-a^2)t^2+30b^2t^4. Independently summed all nine factorial terms symbolically and verified equality. Every t with Im(t)<0 occurs as reciprocal of z-conj(w). The quadratic in t² has discriminant 36[(a²-b)²-(10/3)b²]; nonnegative case is equivalent to a²>=b+sqrt(10/3)|b| because the opposite branch is impossible for a²>=0. Real positive t² roots are excluded; nonreal conjugate t² yield exactly two simple attainable lower-half-plane roots. Handles b=0, a=b=0 and equality real double roots; does not count fixed-w-slice zeros.

## originality

PASS

The published canonical Gram-kernel derivative representation is acknowledged. Its pure-jet and factorial families, and the related published two-jet or separated-jet results, do not classify the full normalized real three-jet (1,a,b) discriminant and restoration threshold.

## value

PASS

The first fully populated real second-order differential-evaluation family exhibits a sharp positive-definite-kernel zero-freeness transition and restoration by a first derivative. The exact threshold is a natural low-dimensional Lu Qi-Keng classification, beyond merely checking a special numeric coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
