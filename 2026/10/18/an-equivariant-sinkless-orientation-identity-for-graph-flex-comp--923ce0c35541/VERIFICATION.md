---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Exact theorem: finite simple undirected graphs with no isolated vertices, every subgroup Γ≤Aut(G); ordinary unreduced rational H_k and equality of virtual representations, not degreewise modules or equivariant homotopy. Kozlov Definition 2.7 indexes a d-cell by independent D and an orientation of G\D; the equivalent unique all-sink-corner (θ,D) indexing holds because each non-isolated flex axis genuinely reverses incident edges. If automorphism g fixes a cell, it fixes its unique all-sink corner, maps θ to θ, permutes D without reversing sink-to-source coordinates. Its signed cellular trace is sgn(g|D). Summing (-1)^|D|sgn(g|D) over invariant subsets of the g-stable sink set yields det(I-P_{g,S}); this is 0 for S≠∅ (constant eigenvector) and 1 for S=∅. Finite Γ characters thus give the virtual Q[fixed sinkless orientations] representation by rational semisimplicity; averaging traces and rational transfer over H gives χ(|F|/H)=#(sinkless H-orbits). For orbit formula, a reversing undirected edge orbit forbids any g-fixed orientation; otherwise forcing a g-invariant independent sink set B fixes incident directions and leaves exactly one binary choice per g-edge orbit in G\B. Inclusion-exclusion by B-vertex orbits proves the displayed formula. Independent Python full-orientation/fixed-cell sign enumerator checked 84 automorphism instances across K2,P3,K3,C4,K4,2K2,C5,K1,4; identity and reversing automorphism boundaries included. No bounded check substitutes for the determinant/inclusion–exclusion proof.

## originality

PASS

Best-of-knowledge universal equivariant lift, compared in full against the founding Kozlov primary text and full relevant published same-object and different-complex results; earlier scalar and K_n restrictions are credited. Distinct arbitrary-G identity not found; structural possibility of an unindexed general equivariant consequence remains.

## value

PASS

A genuine motivated structural equivariant refinement of Kozlov’s core Euler identity: for all finite graphs and graph symmetry groups it computes an explicit nonnegative Lefschetz number at each element and an exact quotient Euler invariant with a reversing-edge obstruction. An ordinary Euler scalar cannot recover nonidentity virtual characters, and a K_n-only character does not cover arbitrary graphs. The orbitwise formula can be applied directly from vertex and edge orbit combinatorics without computing homology groups. This is a reusable natural graph-topology invariant, not an arbitrary numerical slice, while it appropriately claims neither graded representation modules nor homotopy equivalences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
