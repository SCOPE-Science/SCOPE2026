---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Every cyclic binary word gives a nonzero balanced integer circulation on the order-two de Bruijn digraph, and conversely every balanced circulation with connected positive-edge support admits a directed Euler circuit. Flow balance reduces eight threegram counts to a,b,d,f,h and c=b+f-d>=0, with length n=a+h+3b+d+2f and weight w=b+d+f+h. Partitioning exactly by whether both bridge edges b,d occur, one, or neither (single loops / two-cycle) gives five disjoint geometric generating functions in G(z,u). For fixed w>=2, free 000 loop count a admits every length above minimum; case II b=w,f=0 first appears at n=3w and is the unique profile missing at 3w-1. Geometric summation yields S_w cubic parity formulas. Independent direct word enumeration n<=14 matched predicted composition counts and thresholds w=2,3,4; unweighted n14 total 167. This finite check does not prove the infinite GF.

## originality

PASS

The unrestricted total cyclic threegram profile count was previously known and is explicitly credited. Kiah et al and Chang et al give general de Bruijn profile coding and some finite q,ell,n counts; the precise Hamming-weight-refined rational generating function and sharp all-weight stabilization are not consequences of their inspected rates. A proper sublanguage forbidding 111 is not unrestricted because 111-containing Eulerian profiles are omitted.

## value

PASS

Exact constant-composition zero-error profile capacity and sharp length beyond which each weight class stops acquiring distinct read-multisets is a natural coding-theoretic invariant. The result refines known univariate counts with a nontrivial all-weight phase threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
