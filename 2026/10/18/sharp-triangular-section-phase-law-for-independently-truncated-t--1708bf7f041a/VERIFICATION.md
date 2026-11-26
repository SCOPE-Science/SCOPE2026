---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independently reconstructed the graph and sign-cone argument. In barycentric coordinates the cuts are the caps lambda_i <= 1-t_i; the upper caps cannot meet because t_i+t_j<1. Thus the graph is four triangles with one connector between each pair. A partially selected triangle contributes two edges to a cut; two partial triangles are impossible for a three-edge cut; with one partial triangle the other three must all be on one side or their own connectors add at least two more crossings. This leaves only singletons, entire corner triples, and complements. A singleton cannot be separated by a plane through g: pair the original vertices on two opposite edges neither using the omitted truncated vertex, and average their midpoints, each in the retained edge segment. For a positive corner i, normalized negative original heights r_j sum to one, and the connector heights enforce r_j>q_j. Those inequalities imply every required sign since t_i<1/2, and the height map realizes every such choice. In the basis of the three w_j for j!=i the matrix of the active bounding vectors has determinant (1-sum_{j!=i} q_j) times product_{j!=i}(1-t_j), so the normals are independent and the active region is a genuine spherical triangle. Pairwise inward-halfspace angles give Girard's area and the two antipodal copies give the denominator 2 pi. At equal regular depths the argument of arccos is exactly 1/2 - 8 epsilon^2/(3/2+4 epsilon+8 epsilon^2) for t=1/4-epsilon, yielding the stated coefficient and strict quarter-depth boundary.

## originality

PASS

The variable-depth odds condition, the metric solid-angle law across independent truncations, and the regular quarter-depth onset are not covered by the strongest inspected results. The no-triangle consequence at the Archimedean one-third cut is independently covered in a distinct same-day catalogue record and receives no separate novelty credit; within-day priority is undetermined.

## value

PASS

Independent truncation depths are natural geometric shape parameters. The criterion separates the affine feasibility question from a metric probability, identifies precisely when triangle types are extinguished, and quantifies the regular critical onset. That is a reusable geometric result beyond recomputing a fixed Archimedean case or applying spherical excess alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
