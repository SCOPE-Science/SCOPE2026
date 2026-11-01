---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

PASS. Direct normalized Szegő-kernel summation gives ber(T)=sup_{0<=r<1}r|a+br²|/(1+r²). The operator norm is max(|a|,|b|); a gauged positive half-line Jacobi matrix with alternating weights has numerical radius (|a|+|b|)/2 by row-sum upper bound and long blocks. For |a|>=|b| the r=1/2 witness is strictly stronger; for |b|>=|a| the r=sqrt(2)-1 and boundary r->1 witnesses have envelopes meeting uniquely at a/b=-(4sqrt(2)-5). Differentiating the extremal radial profile confirms both constants, the unique equality family and the fully attained Berezin disk via interior r=sqrt(2)-1. Independently tested 6006 complex coefficient phases and 1500 radial sample points; finite grids corroborate but do not prove infinite-dimensional sharpness.

## originality

PASS

PASS best-of-knowledge: the two simultaneous SHARP lower testing constants and common complex equality family for periodic Hardy shifts are a motivated independent computation beyond pre-existing centered Berezin-disk geometry or ordinary numerical-radius identities. Some range geometry is explicitly prior, not claimed new.

## value

PASS

PASS. Sharp simultaneous norm and numerical-radius constants quantify the loss in testing an infinite Hardy shift only on normalized Szegő kernels. Rigidity of a common complex extremizer, even with cancellation of alternating weights, is an independently meaningful operator-theoretic fact, not just an unmotivated restricted slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
