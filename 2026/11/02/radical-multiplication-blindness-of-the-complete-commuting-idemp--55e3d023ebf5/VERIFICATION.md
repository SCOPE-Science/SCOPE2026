---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For any split basic finite-dimensional K algebra, explicit joint idempotents p_a from a commuting tuple lift the coloring projections E_a, and u=sum_a p_a E_a lies in 1+J, conjugating the full tuple. Stabilizer is exactly 1+oplus_{c(i)=c(j)} e_iJe_j; orbit-stabilizer gives q^{sum_{i<j}w_ij [c_i != c_j]} for each coloring. Surjection/Stirling inversion yields every distinct-idempotent clique count. All commuting families extend to a maximal Boolean family of size 2^n; conjugation gives q^{sum w_ij} such families. The two 6D quiver algebras have equal Peirce w and different J^2. Independently evaluated three-color sums at q=2,3, arity 0..3 to (1,26,340,3368) and (1,56,976,10592). The orbit proof, not finite checks, covers all q,n,k.

## originality

PASS

Best-of-knowledge acceptance for the stated narrowly quantified original contribution; known antecedents and overlapping results explicitly excluded. Published mathematical records were queried by equivalent statements; primary literature inspected to the material actually accessible, without implying that lack of a hit guarantees novelty.

## value

PASS

Shows precise information loss of a complete natural invariant of finite algebras: the full commuting-idempotent clique polynomial forgets radical products and arrow orientations, with explicit nonisomorphic same-dimensional witnesses differing in radical nilpotence class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
