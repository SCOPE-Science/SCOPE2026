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

For k>=3, a fresh fourth vertex meeting all three sets is obtained by a one-element replacement in X. If X meets both other sets, retain up to two witnesses, then there are k+1 choices of added element and at most two forbidden equalities. If it misses one other set, add one of that set's k elements and retain a witness for the intersecting set; the replacement cannot equal the disjoint set and at most one choice equals the other set. If X misses both, their intersection has size at least k-1 in its complement, so add a common element. To be adjacent only to X, choose among the k+1 k-subsets of its complement; each of Y and Z rules out at most one choice, by equality or by missing its sole element outside X, which cannot both occur for the same set. For adjacency to two specified vertices, their union must have size k+1: the unique candidate is its complement. It is already selected if the third vertex is that complement, and otherwise is adjacent to the third vertex precisely for the top triple. Pair labels are recoverable from adjacency and the rank-one common-neighbor test (including equality repetitions among the chosen points); the top bit is exactly the all-three adjacency extension in the all-E case. To verify the symbolic table, the four Venn capacities for the third set give the stated integer interval for t, and comparison of endpoints yields |v-w|<=k-u and k-u-1<=v+w<=k+u. Cells AA, AI, AE, EE are feasible exactly at u=k-1, u>=1, u<=1, u>=k-2, respectively. II and IE are always feasible for k>=3: set v=w=floor(k/2) for II, and v=max(1,u-1), w=k-1 for IE. Symmetry supplies the other cells. Top and star both extend any E pair by symmetry and explicit constructions. The distinct-pair extension signatures therefore separate in 1,2,3,4,5 counts, and the five complete rank-two types, not just counts, agree across k>=5. Equality repetitions add a uniform repeated-pair type in the tail, since rank-one types for {X,Z} use the same three available pair labels and codegree test. Vertex transitivity then gives the four-round result. The representative bound follows from strict increase of the binomial orders. Along two successive edges the endpoint sets differ by at most one replaced element; closing an odd walk in 2r+1 steps requires r>=k to reach a disjoint neighbor of the start, proving unbounded odd girth. Independent replay `python3 /workspace/branches/independent_checks.py 4` works directly with subset neighborhoods through k=6 and agrees, including equality of complete distinct-pair type sets at 5 and 6. Frozen checker and recorded output inspected, not executed.

## originality

PASS

The distinct claim is the sharp cross-k rank-four partition along n=2k+1. Published catalogue work already settles the lower-rank partition on this family. The strongest same-rank related record works at fixed subset size three, sharing the single graph KG(7,3) but not comparing any two different odd graphs. Neither that slice nor the broader lower-rank result supplies the k=3,4 rank-four separations or the k>=5 equality.

## value

PASS

The natural odd-graph family retains an unbounded graph invariant, odd girth, while its first-order rank-four types stabilize. The exact cross-k cutoff and optimal within-family representative size quantify that gap. This goes beyond the already known lower-rank classification and identifies the precise extension patterns that matter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
