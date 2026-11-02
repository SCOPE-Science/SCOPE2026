---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For the exact Aliev tetrahedron Δ, vertex evaluations of integral u=(a,b,c) are 0,(s+a)/2,(s+b)/2,(s+c)/2 with s=a+b+c. Setting x_i=s+u_i is a bijection onto integer triples with sum divisible by four, inverse u_i=x_i-s. Thus twice the lattice width is the integer range of 0,x1,x2,x3. A nonzero u cannot have range <=1: all x_i then lie in {0,1} or {-1,0}; their sum lies between -3,3 and divisible by 4, so all vanish. Range=2 splits exhaustively into (i) nonnegative: permutations of (2,2,0),(2,1,1), (ii) nonpositive negatives, and (iii) mixed: permutations of (-1,0,1). Mapping back gives exactly ±coordinate vectors, six permutations of (1,-1,0), and six mixed-sign ±1 triples, a total of 18 oriented/nine unoriented directions. Determinant of the edge matrix with diagonal 1 off-diagonal 1/2 is 1/2, volume 1/12; width=1 attains known sharp inequality. Independent integer shell enumeration confirmed 18 and independent range check scanned 4,912 nonzero u in [-8,8]^3; universal min lower bound is the congruence proof, not the scan.

## originality

PASS

Aliev's 2023 primary result establishes the volume-lattice-width equality and explicitly specifies this tetrahedron, but does not enumerate the complete attaining integer-functional set in its corollary and proof. Draisma–McAllister–Nill bound the number of minimum directions by 3^d-1, equality only at the regular lattice cross-polytope; at d=3, their 26 bound does not specify the exact 18 or directional identities for Aliev's simplex. This finite contact classification is a distinct result, with priority qualification for unindexed discussions of the sharpness example.

## value

PASS

The particular tetrahedron is a canonical sharpness witness for the exact three-dimensional volume-width inequality, so its active primitive dual width functionals are a natural finite invariant, not an arbitrary mesh enumeration. The complete nine unoriented contact directions sharpen knowledge of the equality witness and can serve in studies comparing extremal width contact geometry and equality/stability conditions. The number and full direction list were not supplied by the published universal bound. The calculation is elementary but a motivated exact classification of a canonical extremizer, with no claim of a new general inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
