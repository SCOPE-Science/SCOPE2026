---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The 4x4 Cartesian graph has 24 edges. Independent exhaustive matching enumeration gives face counts (1,24,224,1044,2593,3388,2150,552,36) including empty face, total 10012. The inspected integer certificate uses an explicit 5002-pair acyclic Hasse matching leaving 6 degree-4 and 2 degree-5 critical cells, constructs integral cycles and dual cocycles with identity pairings, and then evaluates all 8 signed induced D4 chain actions. The resulting traces on (H4,H5) by [identity,quarter turn,half turn,axis reflection,diagonal reflection] are (6,2,2,0,-2) and (2,0,-2,0,0). Independent signed fixed-face Lefschetz sums for all 8 elements are (4,2,4,2,0,-2,0,-2), exactly chi4-chi5. Inner products with stated D4 character table yield H4=A1+2A2+B1+E and H5=E. Inspected integral degree-5 basis verifier gives r=[[0,1],[-1,0]], h=[[-1,0],[0,1]] and checks the dihedral relations. No unproved homology-concentration inference from Euler traces: basis and the cited prior integral Morse result independently anchor degrees.

## originality

PASS

The exact same grid matching complex is previously classified nonequivariantly as six 4-spheres plus two 5-spheres, and this is explicitly credited. The full prior RESULT.md contains no D4-module, full character or integral degree-5 rotation/reflection matrices. Nearby published three-cut complexes are different face constructions; three-row grids and outerplanar results do not determine 4x4 matching homology characters. Novel contribution is finite but complete natural dihedral symmetry refinement, with residual risk from uninspected full three-row source.

## value

PASS

The 4x4 square is a natural smallest nonouterplanar square matching-complex benchmark with two different reduced homology degrees. The complete D4-module and integral H5 matrices identify invariant and orientation types absent from published wedge counts; a precise natural symmetry invariant could be useful for equivariant topology of larger grid families. Finite work is independently motivated by the canonical geometric D4 action.

The dated certificate retains the supplied scientific assessment, sources and limitations.
