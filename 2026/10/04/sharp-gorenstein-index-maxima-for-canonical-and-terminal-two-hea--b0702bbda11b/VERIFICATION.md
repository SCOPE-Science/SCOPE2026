---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The unit charts are smooth; the canonical character on each heavy chart has order w/gcd(w,S), with w=a,b and S=r+a+b. The lcm of those two orders is L/gcd(L,S), where L=lcm(a,b). There are no pseudoreflections because r≥2. For d=b−a>0 the b-chart age of class j (1≤j<b) is (r−d)j/b+ceil(dj/b); j=1 gives the necessary bound, and all j give sufficiency. In the a-chart, if dj<a the age is (r+d)j/a; otherwise rj≥dj≥a under the b-chart bound. The strict test uses d<r and a<r+d; necessity of the latter follows from j=1 if a≥r+d. For d=0 the nontrivial chart ages are rj/a. This proves both triangles including the unit-weight cases. In u=r−d, v=r+d−a, the product ab=(2r−u−v)(3r−2u−v) is strictly decreasing in each variable on the feasible region. Bounding it at (3,0), (2,1), (1,3) and (0,4) discards everything except the eight listed corner points. The u=0 and v=0 points have b|S and a|S respectively; (1,1) has L=6(r−1). All are strictly below (2r−3)(3r−4) for r≥3. At (1,2), b−a=r−1, gcd(a,b)=1, S−3a=2 with a odd, and S−2b=1. Thus the product is attained with no cancellations, uniquely and in the terminal triangle. Direct substitution confirms the nine r=2 indices and unique terminal maximizer (2,3). The supplied script and its recorded output are finite regression evidence only; the review uses the exact argument, not an execution of the script.

## originality

PASS

Credit the known structural index and age criteria and the distinct indexed exact triangle. The supported distinct result is the sharp all-r optimization of the anticanonical Cartier index with a unique terminal maximizer, not the parameter triangle or the Gorenstein subclass.

## value

PASS

This gives an exact obstruction to making the anticanonical divisor Cartier at a fixed multiple in a natural singularity-constrained family in every dimension. The product bound alone selects the wrong weights; local Cartier cancellations determine the sharp answer and explain why strengthening canonical to terminal does not reduce it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
