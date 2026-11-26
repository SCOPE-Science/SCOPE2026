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

Cioabă–Mim Theorems 3.8 and 3.12 supply the required homology result for order at least five. A triangle not contained in a line uses all three edge directions and after translation has vertices (0,0),(u,0),(0,u) with u≠0. The only possible fourth vertex is (u,u), possible exactly for 2u=0; no fifth is possible. This gives n²(n−1) non-line triangles and (|A[2]|−1)n²/4 intercalates, hence the stated identity trace. For a translation of order d, q whole vertex orbits in an invariant simplex contribute sign (−1)^(q−1) to the Lefschetz sum. Outside the line directions, even a single orbit fails the clique test. In a line direction each of the n preserved lines contributes 1. An invariant triangle would require order 3 and would itself be a single orbit on a line, so there are no non-line invariant triangles. The only extra faces are the n²/4 intercalates stabilized by a given line involution, each with two swaps and contribution −1 in degree three. The augmentation contributes −1. These reduced Lefschetz numbers all equal the H₂ traces. Barycentric subdivision orders each simplex by its face dimensions and removes inversions; the quotient cellular chains are coinvariants, and rational averaging is exact. Averaging the four trace cases gives the h_i,e_i formula and n−|A[2]| for H=T. The supplied finite logs were inspected but not rerun; they do not attest to the universal formulas.

## originality

PASS

The nonequivariant dimension and concentration are covered by Cioabă–Mim after the intercalate count. A distinct same-day Paley-25 record is exactly the order-five specialization, with no priority inference in either direction. The supported distinct scope of the frozen contribution is the uniform all-abelian translation and geometric subgroup-quotient calculation, notably the correction at even orders. The later-dated cyclic odd, abelian odd and abelian even records must be credited as exact overlapping catalogue coverage, not treated as evidence that this earlier-dated scope is absent from today's catalogue.

## value

PASS

The result recovers a full rational representation rather than a single dimension and computes homology of every geometric translation quotient. Stabilized intercalates produce an explicit correction that distinguishes full quotients of groups of the same order, including an exact acyclicity criterion. It is not merely the known nonequivariant homology or a graph quotient calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
