---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

On sunlet C_n∘K_1 (n≥3), an initially white leaf prevents its initially blue center from forcing along the cycle until adjacent cycle centers are already blue; only initially blue leaves B can start center-to-center forces. Encode initially both-white centers E and build cyclic B–E alternating graph H_S. Every component containing E is removable exactly when a degree-one B endpoint exists; fully alternating even rings have none. Weighted three-letter closed-walk transfer on the source five-state matrix, correcting the two fictitious walks per alternating cyclic word, yields trace(T^n)−4[z(1+z)]^{n/2} on even n and the stated rational series with a=z(z+2), b=2z(z+1), c=z²(1+z)². Formal extraction gives minimum counts 4(2^{n/2−1}−1) for even n and 3n2^{(n−3)/2} for odd n (minimum size ceil(n/2)). Independent brute zero forcing over all 2^{2n} initial sets n=3..8 matched the H_S criterion, the polynomial and minimum counts, and an independent symbolic 5×5 trace determinant check passed. General all-n result rests on combinatorial induction/transfer, not finite run.

## originality

PASS

Boyer et al arXiv:1801.08910 full primary 23-page PDF defines zero-forcing polynomials and evaluates other families (including threshold-block graphs); its examined enumerations do not imply the exact sunlet/cycle-corona polynomial or B/E criterion. The known Z(S_n)=ceil(n/2) gives the minimum degree but not its multiplicity or full polynomial. Row 2012 studies cutvertex/unicyclic zero-forcing numbers, not known full coefficient enumerations; complete Row article unavailable and distinct naming is a residual risk. Targeted Resultary sunlet/corona/zero-forcing polynomial searches returned neighboring fan/friendship/chain results, not sunlets. O PASS best-of-knowledge.

## value

PASS

The zero-forcing polynomial is a natural standard enumeration invariant. Solving its complete sequence for an infinite unicyclic graph family is significantly more than the previously known minimum; explicit even/odd counts of minimal forcing sets, and a static forbidden alternating-path description, provide exact structural information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
