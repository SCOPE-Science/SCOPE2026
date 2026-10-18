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

Inspected the exact Q(sqrt5) standalone enumeration and the full RESULT.md. At an edge-interior x the unique norming functional f_i forces y in the two unit directions ker(f_i). At a vertex x the norming functional interval gives x perpendicular_B y precisely when f_i(y)f_{i+1}(y)<=0; intersecting with decagon boundary yields 20 admissible subsegments. On every 1D case each norm is a maximum of ten affine terms, so the product is a quadratic on cells partitioned by all pairwise affine crossings. The exact checker checks endpoints and each interior stationary point using a rational quadratic-field arithmetic class, giving maximum P_edge=(63-5sqrt5)/16, P_vertex=(2+5sqrt5)/4, with strict difference (25sqrt5-55)/16>0. Independent numerical evaluation of the explicit pair and the respective edge/vertex maxima corroborated P_vertex~3.29508, P_edge~3.23873; finite exhaustive algorithm, not numeric sampling, is the claimed certificate. Birkhoff condition of witness verified using opposite signs of two norming functionals. The scope is precisely this affine-regular decagon and real scalars.

## originality

PASS

Bounded best-of-knowledge originality: the exact stated invariant and quantified result were compared by implication to the closest primary and published SCOPE sources; no decisive covering result found. Unread material and alternative nomenclature remain explicit, and source search is not proof of absolute novelty.

## value

PASS

The optimal Birkhoff-orthogonal geometric mean is a natural nonlinear invariant not determined by the decagon's separate James, Schäffer or Birkhoff chord-sum constants. The exact vertex-vs-edge competition, golden-ratio constant and equality witness supply a useful complete polygonal test case; the 1D cell classification is substantive, not merely a renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
