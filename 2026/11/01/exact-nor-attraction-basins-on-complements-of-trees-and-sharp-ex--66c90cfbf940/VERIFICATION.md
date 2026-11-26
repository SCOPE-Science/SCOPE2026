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

For the symmetric closed-neighborhood relation of T, A is contained in F(B) iff B is contained in F(A), giving F^3=F. A leaf singleton maps to its edge and is not periodic, proving sharpness for every n. Two centers' closed neighborhoods intersect in their shared edge if adjacent, their unique middle vertex if distance two, or nothing otherwise. Thus all image states are full, empty, edge pairs, singleton centers, or closed stars. In the nonstar case an edge pair gets precisely itself and its leaf endpoints as predecessors; an internal singleton of degree d gets the subsets of its closed star of size at least three and pairs of neighbors, totaling 2^(d+1)-2d-2, while its closed star gets only the center singleton. The full state has just the empty predecessor, so subtraction supplies the empty fiber and the distinguished basin. A star's isolated complement center is always set; each singleton leaf support yields two fixed predecessors, and all other leaf supports enter the stated center/full cycle. For nonstars the degree excesses sum to n-2 and have at least two positive parts. The strictly increasing increments of 2^(e+2)-2e-4 force the minimizing partition into ones, and by transferring units to the largest part the maximizing partition (n-3,1). These determine the path and the broom, including their coincidence at n=4. The lower bound 2^(n-1)-3 strictly beats 2^(n-1)-2n+3 for the other two-cycles and beats every fixed basin. An independent set-based replay, python3 /workspace/review_work/reproduce_2.py, exhausts all nonisomorphic trees of orders 4–8 (45 trees, 7808 states) and checks the basins, time bound, and each extremal equality condition. The frozen Python checker explicitly asserts only global min/max in its extrema section, not every equality case; the reconstructed proof supplies all-orders claims.

## originality

PASS

Credit is for the complete tree-complement basin census and its largest-basin extremizers, not the known fixed-point correspondence or the general period restriction. The closest inspected equivalent dynamics and indexed exact-basin result do not supply the degree-dependent tree-complement formulas.

## value

PASS

A short period says little about the fate of a random starting state. This complete classification quantifies that difference: even the other two-cycles and all fixed points can be individually common or rare according to the tree degrees, yet one cycle strictly dominates in every tree. The exact path/broom/star comparison resolves how fixed-order tree shape controls that basin and is not provided by a generic period bound or fixed-point count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
