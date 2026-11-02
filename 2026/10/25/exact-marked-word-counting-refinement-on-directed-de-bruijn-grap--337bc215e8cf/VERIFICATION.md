---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS — For every q,k≥1 and each marked set M (including empty), collapsing all unused letters to * gives an equitable in/out-degree counting partition, so stable color cannot be finer than the coordinate pattern. Directly expanded F and B shift adjacency to establish B^(k−j)F^(k−1)B^(i−1)e_r=q^(i−1+k−j) 1_{v_j=r_i}. Since marked singleton indicators are present initially and F,B each advance one refinement round, all named-letter coordinate tests are visible by round ≤3k−3, forcing the reverse partition inclusion. Aut of directed de Bruijn graph acts by simultaneous S_q letter permutations; its marker stabilizer is S_u, and equality patterns of h unused positions give Σ_b Stirling(h,b) orbits per cell. Exactness iff k=1 or u≤1; q=1,k=1, M=∅ and loops covered. Independently enumerated 20 marked refinements and compared induced partitions, plus direct symbolic operator argument; finite checks do not prove all q,k.

## originality

PASS

PASS, qualified — Boutin–Goliber–Pelto Theorem 4.12 gives Aut(D(q,k))=S_q and determining number, which this result cites as known. General two-variable counting/colour-refinement frameworks of Kiefer–Schweitzer–Selman and Berkholz–Bonsma–Grohe do not in their inspected conclusions supply the complete individually marked coordinate-collapse partition and Stirling orbit census. The operator word-coordinate recovery theorem is an explicit structural refinement beyond a determining-set group statement. Full counting type with loop predicate is deliberately outside scope. Undiscovered symbolic-dynamics exact refinements remain possible.

## value

PASS

PASS — Relates intrinsically natural group orbits, determining sets, and coarsest stable in/out counting partitions for all directed de Bruijn shift graphs and marker sets. Complete formula, depth bound and explicit unused-letter equality obstruction explain exactly when color refinement captures automorphism orbits, not a mere restatement of determining-number theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
