---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

A fresh compatibility graph on all 32 binary words joined pairs at cyclic pair distance at least four. Independent Bron–Kerbosch enumeration found 118 maximal cliques, maximum size eight, and exactly 20 size-eight cliques. Translating each maximum by one of its words produced an eight-element set containing zero and closed under XOR, so every maximum is an affine three-dimensional subspace. Exactly five direction subspaces occur, each with four cosets. These checks reconstruct the finite classification from the metric definition; the known Singleton bound independently confirms the maximum-size ceiling.

## originality

PASS

The classical symbol-pair literature already gives the Singleton upper bound and explicit binary MDS \((n,4)\) constructions for every \(n\ge4\), so neither existence nor the numerical maximum 8 is novel by itself. The inspected sources do not classify all nonlinear length-five binary maximizers. The audited census adds exactly that missing finite structure: all 20 labeled maxima are affine 3-flats, arranged as four cosets of five direction subspaces and one orbit under the stated pair-metric symmetry subgroup.

## value

PASS

The smallest binary distance-four MDS symbol-pair instance is a canonical boundary case where existence was known but nonlinear extremizers were not classified. Determining every optimum, its affine rigidity, and its symmetry orbit gives a natural complete finite classification useful as a benchmark for structural conjectures and enumeration methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
