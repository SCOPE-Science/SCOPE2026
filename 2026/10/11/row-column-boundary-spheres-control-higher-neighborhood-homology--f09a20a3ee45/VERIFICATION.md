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

Checked the exact open-neighborhood convention N(i,j)=row_i\{(i,j)} union column_j\{(i,j)}. Every edge is witnessed, no full row or column is; every mixed face of size >=3 has a unique witness center because two points identify one leg and a third identifies the opposite coordinate. Thus center simplices intersect outside the core nowhere, and their common intersection J_ij with K0 consists precisely of the full A and B leg simplices and (m-1)(n-1) cross edges. Contracting the two disjoint simplex legs reduces J_ij to a graph with two vertices and that many parallel edges, a wedge of (m-1)(n-1)-1 circles. The cofiber of J into its contractible center simplex is its suspension; the quotient wedges over mn centers, proving the relative 2-spheres. Relative homology vanishes from degree 3 onward and yields integral H_k(K0)=H_k(K) for k>=3 by the long exact sequence. The high-degree core chain complex is a direct sum of row and column oriented boundary simplices; row permutations permute generators and column permutations induce sign on row boundaries, vice versa for columns. Independently enumerated mixed triangles/unique centers and cofiber counts on 3x4 and 4x4 boards: respectively 108/60 and 288/128. These finite checks do not prove the general statement.

## originality

PASS

Matsushita's same-graph calculation concerns CLOSED neighborhoods (center included), not the open Lovász complex, and has different higher homology. Published open rook-graph 4x4 integral homology gives only that particular board and zero H>=3. Published K_2 square K_n homotopy classification has only two rows, outside m,n>=3. The complete high-degree all-board integral/permutation-module formula and relative cofiber construction are not logically supplied by those results.

## value

PASS

The explicit all-parameter cofiber formula and integral signed symmetry modules identify previously unaccounted higher-dimensional cycles for a canonical graph-product family. They distinguish open from closed neighborhood topology and determine natural free homology in degrees where simpler finite-board computations are silent. The exact representation information is independently useful in equivariant topological combinatorics, even though low-degree torsion/homotopy remains unclassified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
