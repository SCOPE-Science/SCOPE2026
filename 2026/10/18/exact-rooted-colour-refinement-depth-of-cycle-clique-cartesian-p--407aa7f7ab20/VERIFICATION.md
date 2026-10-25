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

Root-stabilizer automorphisms preserve clique-vs-cycle Cartesian directions by triangle counts for m>=3 and square counts for m=2, giving exactly A_d=(cycle distance d, clique coordinate 0), B_d=(distance d, remaining clique coords), d=0..floor(n/2). At refinement round t, the root-colour induced signatures determine rooted walk counts w_0..w_t by induction. A_k and B_(k-1) are the only competing orbit types at root distance k; their shortest-walk counts differ (k versus one, or even antipodal two), except the distance-one collision, which splits at t=2 if m>=3 from length-two counts and at t=3 if m=2 (length-three counts 6 vs 7). For n>=6, D>=3 is enough; n=5,m=2 needs t=3. All vertices beyond t hops of a singled-out root in the (m+1)-regular graph have the same color at round t, and B_D versus A_D remain unsplit at t=D-1, proving optimality. Independently rebuilt direct refinement on 65 parameter pairs n=5..17,m=2..6 and confirmed exact orbit cells and stabilization depth; source 392 vertex and 864 quotient finite tests corroborate rather than prove all n,m.

## originality

PASS

The exact mathematical conclusions compared to prior results were not identified as an implication of an inspected stronger result; best-of-knowledge, not exhaustive priority certification. Relevant full-text access limitations and aliases recorded.

## value

PASS

Gives a sharp, nontrivial exact time-to-stabilization and complete orbit partition for a natural two-parameter graph family, distinguishing cyclic radius from full marked-root eccentricity and identifying an exceptional pentagonal prism. This is a motivated structural invariant of standard graph-isomorphism refinement, not an unmotivated sample count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
