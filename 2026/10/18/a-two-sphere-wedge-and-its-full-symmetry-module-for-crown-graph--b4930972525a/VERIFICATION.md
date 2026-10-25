---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

PASS. For G_n=K_{n,n} minus the n matched edges, Ind_2 means induced connected components of vertex subsets have <=2 vertices. The mixed maximal simplices are T_ij on {a_i,a_j,b_i,b_j}, and the two all-one-side simplices ΔA,ΔB complete the facet list. Their intersections are simplices, so the simplicial nerve is the suspension of the complex P of common-endpoint edge families; P itself has a good cover by n simplices C_i whose pair intersections are single vertices and triple intersections empty, giving nerve K_n^(1). Consequently X_n~ΣK_n^(1)~wedge^(choose(n-1,2)) S2 for all n>=4, integrally and without torsion. Both covers are permutation invariant with connected contractible intersections; the natural Cech chain quasi-isomorphisms yield integral H2 module H1(K_n)⊗epsilon under Sn×C2. Over Q this is wedge² of Sn standard module U_n and trace (-1)^e([(f(sigma)-1)^2-(f(sigma²)-1)]/2). Independently enumerated all 2^(2n) vertex subsets and component sizes n=3,4,5,6, checked exact maximal facets, and signed Lefschetz traces for all 12, 48, 240 group elements n=3,4,5 and four n=6 samples. General proof is the two-stage nerve argument, not finite enumeration.

## originality

PASS

PASS (best of knowledge, not historical-priority certification): Independently compared mathematical statements and implications with the identified highly relevant literature and Resultary entries, distinguishing earlier counts/classifications from the newly assessed exact claim. Inaccessible/plausibly broader sources are disclosed rather than falsely excluded.

## value

PASS

PASS. Crown graphs are a canonical matching-deleted complete bipartite family; their higher-independence complexes and full integral symmetry modules are natural invariants not recovered by known complete multipartite/chordal classifications. The two good covers reveal a reusable graph-cycle homology mechanism, and the complete all-n character is a meaningful equivariant refinement rather than a tiny isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
