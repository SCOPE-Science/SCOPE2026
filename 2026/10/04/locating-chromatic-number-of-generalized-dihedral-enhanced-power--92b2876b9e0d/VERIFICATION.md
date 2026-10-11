---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Every element of the nontrivial generalized-dihedral coset is an involution. If such an element shared a cyclic subgroup with a nonidentity kernel element, the two would commute, forcing the kernel element to be an involution; a cyclic group cannot contain two distinct involutions, so every coset element is a leaf adjacent only to the identity. The only kernel leaves are exactly \(T(A)\), so \(At\cup T(A)\) is a false-twin class and forces distinct colors, while the universal identity forces one more. The proposed upper coloring injectively pairs every remaining kernel vertex with a distinct leaf; a nonidentity neighbor of the kernel vertex distinguishes the repeated-color pair. For non-2-groups any involution multiplied by a nontrivial odd-order element lies in a larger cyclic subgroup. For abelian 2-groups, \(T(A)=A[2]\setminus2A\), giving \(2^r-2^s\). The frozen group/graph verifier was read and independently checks twelve cyclic/noncyclic kernels.

## originality

PASS

The 2022 enhanced-power survey explicitly poses describing the locating chromatic number as an open problem. The closest 2021 nonabelian-family paper studies metric dimension, resolving polynomials, distance data and Laplacian spectra for related groups but not locating chromatic number. Resultary's exact generalized-dihedral query returned this audited record as the top matching locating-chromatic result; the other generalized-dihedral hits concern different graph invariants. No stronger theorem was found that implies the false-twin correction \(|T(A)|\) or its invariant-factor formula.

## value

PASS

This gives an exact solution of an explicit published graph-invariant problem on a natural infinite group family with arbitrary finite abelian kernel. The answer is structural: isolated involutions are precisely the correction term, and finite abelian 2-group structure converts that obstruction into a closed invariant-factor formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
