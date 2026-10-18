---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For Cr_n=K_(n,n)-M, write selected index sets P⊆[n] on A and Q⊆[n] on B. If Q=∅ then all A must be in P (and vice versa). If |Q|=1, say Q={q}, domination of the unchosen a_q forces q∈P; analogous for singleton P. Mixed-size configurations with one selected on one side and ≥2 on the other fail minimality by deleting any noncorresponding vertex. If both sizes≥2, deleting any selected when a side has size≥3 preserves domination, so minimality requires |P|=|Q|=2. Deletion of each selected vertex then destroys domination exactly when P∩Q=∅. Thus exactly 2 whole sides, n matching NONEDGE pairs {a_i,b_i} and 6*binom(n,4) disjoint-index 2+2 quadruples are the minimal dominating sets for n≥3. Hence the full polynomial is n x²+6*binom(n,4)x⁴+2x^n; upper domination Γ=n, with 2 extrema for n=3 and n≥5 and 8 for n=4. Independently enumerated every vertex subset of the actual crown adjacency graph n=3..7, testing closed domination and deletion minimality; all coefficients agreed. Proof is exact case analysis for arbitrary n, not finite interpolation.

## originality

PASS

Crown graphs are precisely two-row rook-complement graphs, so checked that alias. OEIS A289121 (2017) gives the polynomial IN n for the total number of maximal irredundant sets; A384123 (2025) tabulates minimal dominating-set totals for n×m rook complements, with column 2 equal to those crown totals. Neither display the degree-resolved crown minimal-dominating-set polynomial. Crucially A384123’s detailed four-family classification and formula are explicitly restricted to BOTH row/column counts >2, so applying it uncritically at row count 2 is invalid. Source 2015 Jothi addresses scalar crown minimal domination size, not this exact profile in accessible material. Prior total and upper domination are acknowledged, not asserted new. Exact size profile remains best-of-knowledge new with risk of an earlier unindexed refinement.

## value

PASS

The known total n+2+6 binom(n,4) loses the minimum and maximum cardinality multiplicities and cannot alone reconstruct this three-term generating polynomial. The complete structural classification at the exceptional two-row boundary gives the exact inclusion-minimal family and sharp upper-domination multiplicities, a natural invariant of an important symmetric bipartite graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
