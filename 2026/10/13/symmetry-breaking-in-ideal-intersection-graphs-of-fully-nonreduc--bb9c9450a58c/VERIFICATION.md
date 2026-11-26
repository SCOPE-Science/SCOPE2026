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

Each local chain has ell_i+1 ideals and intersection is nonzero iff the active supports intersect. Removing zero and the ring gives the advertised vertex total and weights, with only the full-support weight reduced by one. Closed neighborhoods are the unions of all support cells meeting the given support. Distinct supports have different such unions, detected by a singleton support in their symmetric difference. In the quotient the degree 2^r−2^(r−|S|)−1 determines |S|; the singleton neighbors of a larger set determine its elements. Thus quotient automorphisms are coordinate relabelings, and for r≥2 the singleton weights force exactly the length-preserving relabelings. They lift as an action by permuting exponent coordinates, proving the split extension, not just its order. The kernel is exactly all independent internal permutations. One may omit at most one vertex per cell from a base; when every cell has size at least two, keeping the other vertices fixes all cells setwise and then pointwise. The full-support cell of W=P−1 vertices is strictly largest for r≥2 (every proper-support weight is at most P/2). Every distinguishing coloring needs W colors. For each proper-cell size k, 1≤k<W, there are at least W palettes of size k by the binomial bound, and fewer than W proper cells overall. Choosing different palettes and coloring each cell injectively destroys both block and internal symmetries. For r=1 the graph is K_{ell_1−1}, including K_1 with Det=0 and D=1. The singleton-size wording must be read with that boundary in mind: the sole cell for r=1 has weight ell_1−1. Inspected the frozen checker and recorded cases; the proof rather than these examples establishes arbitrary tuples.

## originality

PASS

The support-cell geometry and the standard twin argument for the base size are prior or immediate from prior structure and are not credited as distinct. The supported contribution is the exact weighted action for arbitrary nonfield chain lengths and the corresponding sharp distinguishing number, including unequal and repeated lengths and the full-support puncture. A very close preprint on nonzero component graphs treats the unpunctured equal-coordinate model and gives the analogous full-support bound there; it does not give the weighted, punctured ideal graph theorem.

## value

PASS

Gives the full symmetry and sharp palette size for a natural infinite family with unequal and repeated chain lengths. The indexed weights explain which coordinate symmetries persist, and the exact D+1 yields the product of the local chain lengths without identifying the residue fields. The value lies in the weighted action and sharp distinguishing invariant, not the previously known cell architecture or immediate base-size observation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
