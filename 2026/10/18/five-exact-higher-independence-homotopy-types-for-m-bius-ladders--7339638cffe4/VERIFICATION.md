---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For each n=4,5,6,7,8, M_{2n} has rim edges i~i+1 and spokes i~i+n. A face of Ind_2 is a vertex set containing no induced connected triple, equivalently each selected vertex has at most one selected neighbor. The explicitly listed stage-ordered vertex toggles give 38,111,339,1022,3023 matched pairs on 78,232,685,2046,6078 nonempty faces. An independent implementation rebuilt all faces by enumerating two-edge triples, generated every Hasse covering edge, reversed exactly the matched edges, and topologically sorted the complete gradient DAG: 192,720,2556,8946,30384 cover edges, every vertex visited, zero cycles. Critical-cell distributions are {0:1,2:1}, {0:1,3:9}, {0:1,3:6}, {0:1,4:1}, {0:1,5:31}. Forman discrete Morse theory therefore gives genuine integral wedges S^2, 9 S^3, 6 S^3, S^4, 31 S^5: only one critical vertex and d-cells for d>=2, hence no nontrivial attaching maps. For the natural D_{2n} action, I independently computed the signed fixed-simplex Lefschetz sum for each of the 4n group elements, then used homology concentration to obtain each top-degree rational character and invariant dimension; all tables match the final claim. The independent checker tests every face and edge in these finite cases, not a larger-n recurrence.

## originality

PASS

Best-of-knowledge PASS for these exact five integral two-independence homotopy types and all rational dihedral character arrays. Agarwal–Basak treat ordinary Ind and perfect matching on the identical Möbius ladders; Deshpande–Singh treat the same r-independence functor but other graph families; Carnero Bravo and a published Möbius-ladder total-cut theorem concern bounded independence by alpha(G[U]) rather than induced-component size. A Petersen Ind_2 computation is a different cubic graph. General discrete Morse and Lefschetz theory are antecedent methods, not graph-specific results. No inspected implication dominating the five exact values and characters was found. This is a bounded priority assessment with the explicitly listed primary-text access and unindexed-results risks.

## value

PASS

Möbius ladders are a natural symmetric cubic graph family, and higher-independence complexes are a standard topological refinement of ordinary independence. Five consecutive n values cover every modulo-4 class plus a first repetition, motivated by recent ordinary-independence periodic classification rather than an arbitrary numerical slice. Exact integral wedge decompositions and full D_{2n} rational homology characters are mathematically useful structural invariants not determined by face counts or ordinary independence; in particular M_10 has nine top spheres whereas the ten-vertex untwisted prism analogue was reported with a different rank. The finite complete classification is useful on its own, though no recurrence or all-n theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
