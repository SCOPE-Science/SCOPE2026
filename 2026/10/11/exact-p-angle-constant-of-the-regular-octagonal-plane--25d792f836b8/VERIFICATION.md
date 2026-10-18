---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Octagonal P-angle reduces to Q(A,B)=A²+B²−(√2−1)AB−4≤0 for all unit boundary pairs. Dihedral symmetry fixes x on one edge. For all eight y edges, eight support choices for A and for B, the exact Q(√2) algorithm intersects supporting halfspaces, generates 126 nonempty active-support cells, checks 176 cell vertices and finds maximal Q=0; convexity on each cell supplies the continuum inequality. The independent reconstruction executed the inspected code algorithm and reproduced 126/176/max=0 and adjacent-vertex witness A=2,B=2(√2−1). The source code for the finite reduction was fully inspected; the local verifier reproduction is algorithmically equivalent, not byte-for-byte the frozen blob.

## originality

PASS

Best-of-knowledge no independently published same P-angle constant or dominating octagonal all-separation upper chord profile was found. The checked same-space complete modified-vNJ parameter profile and one-separation smoothness invariant have different admissibility/functional information; their statements do not entail this nonlinear P-angle supremum.

## value

PASS

The Yang–Li P-angle is a natural Banach-space geometric invariant, and the regular octagon is a canonical non-Hilbert polyhedral test space. The exact sharp value requires a genuine all-unit-pair optimization (126 active-support polyhedral cells), separates this invariant from previously known octagon vNJ/angle-modulus values, and includes a sharp geometric maximizing pair. The result is a useful exact benchmark not mechanically implied by checked constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
