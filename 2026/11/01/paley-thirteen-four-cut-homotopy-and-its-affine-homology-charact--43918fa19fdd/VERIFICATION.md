---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

The 13-point graph uses nonzero quadratic residues {1,3,4,9,10,12} and is SRG(13,6,2,3). Independently counted all C(13,4)=715 induced 4-sets: 260 disconnected, 455 connected; their 9-point complements generate exactly 6994 nonempty faces, f=(13,78,286,715,1287,1716,1664,975,260). Explicit pivot-order vertex-toggle matching pairs 3484 faces, with precisely one critical 0-cell and 25 critical 6-cells. A complete topological sort of all 42393 oriented Hasse incidences visits all 6994 faces, proving acyclicity and hence the integral homotopy wedge^25 S6. The complex is pure dimension8 and has nonzero H6, so cannot be pure shellable. All 78 affine maps x↦ax+b with a a square were checked as graph symmetries; direct signed simplicial Lefschetz traces equal twice the number of fixed graph vertices minus one, yielding identity25, 12 nonidentity translations -1, and remaining 65 affine maps 1. Character equality proves rational H6=Q⊕2Aug(Q[F13]), invariants rank1; finite group quotient rational homology follows from barycentric subdivision and transfer. An independently coded complete Morse and character check corroborates source code; mod-two boundary-rank checker is separate and is not misused to prove integral wedge.

## originality

PASS

The standard cut-complex papers provide the definitions and powerful methods, but their actual hypotheses and treated graph families do not imply the P13 case, and a matching Paley-name directed-flag result is a different complex. PASS on a qualified searched basis, not claimed global priority.

## value

PASS

The 13-vertex Paley graph is a canonical symmetric strongly regular test case for graph cut topology. Its ordinary 4-cut complex is pure dimension8 but has all integral homotopy concentrated as 25 six-spheres, a motivated nonshellability witness, and the natural affine group action reduces to a simple nontrivial representation Q⊕2Aug. These exact topological and group-module invariants are not implied by the SRG parameters and distinguish ordinary from total cut constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
