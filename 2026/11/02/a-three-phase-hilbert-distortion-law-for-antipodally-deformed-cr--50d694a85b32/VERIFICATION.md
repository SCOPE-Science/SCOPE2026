---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS. For n≥3, 1≤t≤3 q=t², symmetrizing an arbitrary noncontracting Euclidean embedding by simultaneous permutations and side swap preserves distortion and gives squared-distance variables (a,b,c) with 4≤a≤4T,1≤b≤T,q≤c≤qT. Centered Gram constraints imply |b−c|≤a and (n−1)a≤(n−1)b+c. Combining constraints gives T≥4(n−1)/(n−1+q), T≥4(n−2)/n, T≥q(n−2)/(2(n−1)). Explicit correlated regular simplex copies parameterized by ρ=(b−c)/a attain each branch, with ρ=−1 for plateau and large-q, and meet all lower/upper constraints at q_−=2(n−1)/(n−2),q_+=8(n−1)/n. Independently optimized the 4-variable orbit LP (a,b,c,T) at 24 points and checked attained Gram constraints. All q real in [1,9] follow analytically; boundary cases n=3 and q=1,9 included.

## originality

PASS

PASS at best knowledge for the interpolating metric family and two internal sharp phase boundaries. The t=3 crown graph endpoint is covered by established diameter-three distance-regular results, and t=1 complete-bipartite endpoint is not a new independent claim.

## value

PASS

PASS. Complete bilipschitz Hilbert distortion for a natural continuous matched-pair deformation between complete-bipartite and crown graph metrics; a nondegenerate constant plateau with two exact breakpoints is an independently meaningful geometric invariant not implied by knowing the unweighted endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
