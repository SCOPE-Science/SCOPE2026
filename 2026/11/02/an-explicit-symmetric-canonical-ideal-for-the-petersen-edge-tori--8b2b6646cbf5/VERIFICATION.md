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

The Petersen graph is connected and has no triangles or four-cycles. Two disjoint odd cycles must partition its ten vertices, so a joining edge exists and the edge semigroup is normal. Alternating sums along even walks give all vertex-coordinate differences (an odd closed detour adjusts parity), and adding an edge gives the full even-sum lattice. For the coordinate facets, deleting 45 leaves the five-cycle 12,34,15,24,35 and every remaining vertex attaches to this cycle; transitivity handles all deletions. Independent sets are intersecting families of two-subsets. A singleton leaves a bipartite six-vertex remainder, a pair a nonempty three-vertex remainder, and a three-element star a one-vertex remainder. The other triple type is the triangle on three labels, namely N(v) for the complementary pair; it and each four-element star have full coverage and connected cross-edge graph. Hence the facet criterion gives exactly the stated 25 inequalities. Normal canonical interior monomials are 1+b with b>=0 and even sum 2r, and their minimality is exactly nonremovability of any positive-support edge. The canonical module is Cohen–Macaulay; graded local duality gives top local cohomology dual to R, with end degree 0, so regularity is 10 and no minimal generator after degree 10 is possible. An independent exact stars-and-bars enumeration with tight-facet forbidden edges gave interior/minimal counts (1,1), (15,0), (130,10), (760,0), (3345,0), (11953,0) and verified the ten closed-neighborhood offsets. The rank-ten ring gives projective dimension nine; label permutations act on the displayed generators as claimed, with the characteristic-zero two-subset module decomposing by the Young rule.

## originality

PASS

The h-vector, type, nonlevelness, and even the numerical generator-degree distribution are covered or implied by prior almost-Gorenstein data. The supported additional claim is the determination of the actual monomials as the unit exponent vector and its ten closed-neighborhood offsets, and thus the concrete permutation action in this realization. The closest inspected sources do not identify that ideal or action.

## value

PASS

The Petersen graph is a standard, symmetric nonbipartite example whose ordinary normal edge ring is already studied as almost Gorenstein but not level. Giving the exact canonical ideal as monomials, rather than recalculating type or graded data, identifies the selected symmetric realization and permits subsequent explicit equivariant or algebraic computations. The relevant invariant and graph are natural independently of the finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
