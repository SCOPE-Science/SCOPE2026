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

For u²+v²=w², dividing by gcd(u,v) keeps integer w (valuation argument) and yields coprime legs with support in {p,q}. Primitive opposite parities force 2 in the prime set. If odd leg were 1, a²+1 lies between squares; otherwise odd leg q^b and even 2^a. Factoring (w−2^a)(w+2^a)=q^(2b) with odd coprime factors implies smaller factor 1 and hence (q^b−1)(q^b+1)=2^(a+1). Consecutive powers of two 2 apart are 2 and4, so q^b=3,a=2. Thus only primitive (3,4), all box obstruction edges are scaled by 2^i3^j and move exponent coordinates by (+2,−1). Each line a+2b=t forms a path of length L_t, giving independent size ∑ceil(L_t/2) and all optimizer choices ∏_{even positive L_t}(L_t/2+1). Computing odd L_t counts for R=S=n yields the claimed mod-four quasi-polynomial and density 1/2; other prime supports have no edges and F=RS. Independently enumerated exact Pythagorean pair graphs for all 10 prime supports from {2,3,5,7,11}, rectangle sizes 1≤R,S≤6 (360 comparisons) and brute independence for cells ≤16; every checked graph matched. Universal theorem uses proof, not finite testing.

## originality

PASS

Best-of-knowledge PASS for the complete two-prime obstruction graph, arbitrary rectangular exponent cutoffs and all maximum independent sets. The recent Xiao prime-power-box papers study increasing number of prime coordinates and an asymptotic admissible-set bound; their statements cannot be specialized to exact fixed rank two counts. Primitive (3,4,5) arithmetic is classical and not presented as novel.

## value

PASS

An exact complete classification of an especially natural low-rank slice of the current prime-power-box extremal problem, including the exceptional prime support, graph structure, sharp sizes, and optimizer multiplicities. The mod-four quasi-polynomial and rectangular formula make the finite arithmetic invariant reusable even though the result does not solve higher rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
