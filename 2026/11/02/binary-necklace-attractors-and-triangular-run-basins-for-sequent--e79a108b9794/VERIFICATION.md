---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For the ordered (1,3) closed-neighborhood update on C_n, n>=3, the exact local identity T(a,c,b)=a if c=b, else b gives y_n=y_1 after a sweep; on x_n=x_1 the map is the one-site rotation on n-1 bits. The first-transition decomposition of nonperiodic predecessors gives r(y) and the sum of s(s+1)/2 over cyclic run lengths; convexity proves the maximal basin 1+d(d-1)/2 for primitive period d>=2. This proves 2^(n-1) periodic configurations and Mobius primitive period counts. Independent direct-update finite enumeration n=3..9 agreed with image, rotations, fibers, and orbit basins. Finite checks support but do not prove arbitrary n.

## originality

PASS

Best-of-knowledge originality: exact mathematical implication comparisons favor a non-covered surviving contribution; related special cases and premises are explicitly credited, with listed residual priority risks.

## value

PASS

This upgrades a known existence example for a single long cyclic attractor to an exact phase portrait for an infinite Boolean-dynamics family, including every orbit and its individual transient basin. Run-sensitive basin geometry can distinguish orbits of identical period; the extremal basin bound has a natural dynamical interpretation. Classical Mobius necklace counting alone is not claimed as the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
