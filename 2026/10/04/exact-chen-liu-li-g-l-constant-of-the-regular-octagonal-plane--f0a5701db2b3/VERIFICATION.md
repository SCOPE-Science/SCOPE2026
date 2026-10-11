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

The dihedral symmetry reduction to one reference facet is valid. For each active supporting facet of \(y\) and \(x-y\), the two support equalities determine an affine branch when nonparallel; the exact package verifier at blob 8c62c67a5cc5baed44a36c88c099f03d0090ffea checks all 64 active pairs, enforces every octagonal unit inequality, handles the parallel degeneracies, and deduplicates exactly six feasible branches. It then inserts every support-switch point for \(N(x+y)\) and \(N(2x-y)\); on each resulting cell the objective is a convex quadratic, so checking endpoints is exhaustive. The exact maximum is \(18-8\sqrt2\). The independently displayed witness \(x=(1,\sqrt2-1)\), \(y=(3-2\sqrt2,1)\) satisfies all three unit constraints and has both target norms \(2\sqrt2-1\), attaining the claimed value. The stored verifier output records six branches, ten piecewise cells and VERIFY_OK.

## originality

PASS

Chen, Liu and Li introduce the \(G_L\) constant and give universal bounds and standard-space examples, but the inspected complete article does not evaluate the regular octagonal plane. Current published findings do contain several exact invariants of the same octagonal norm, including \(T_G\), Ptolemy, the angle modulus and a parameterized von Neumann-Jordan profile. Their optimization functionals differ: a sharp product or weighted sum for another constant does not determine the sum of the two squared norms defining \(G_L\). Resultary search returns the assigned \(G_L\) record as the direct match and no earlier same-result theorem.

## value

PASS

The regular octagon is a canonical polyhedral Banach plane, and G_L is a named geometric constant introduced specifically to quantify equilateral configurations. An exact value with an exhaustive sharp upper proof is a natural reusable invariant, not an arbitrary coordinate sample. The calculation also distinguishes G_L from other nearby octagonal constants that happen to share related extremal geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
