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

For Q5, a fort is a nonempty set F with no outside vertex having exactly one F-neighbor. The exact min-fort classification gives minimum size five and precisely the 32 open neighborhoods, reproduced by exhaustive evaluation of all 242,824 subsets of sizes 1–5. Open neighborhoods N(u),N(v) intersect iff centers are at Hamming distance two; same-parity centers must have distance four and at most two such centers per parity, hence rho^o(Q5)≤4, with centers 0,1,30,31 attaining four. An eight-vertex fort {6,7,10,11,20,21,24,25} disjoint from those neighborhoods gives five forts. Six forts require exactly four size-five neighborhoods plus two size-six forts and cover all 32 vertices. For two selected vertices of one parity, at least six opposite-parity vertices have unique adjacency, excluding mixed 6-fort parity counts 2,4; for three selected same-parity vertices a triple-intersection count leaves at least six opposite-parity vertices uniquely adjacent, excluding 3,3. Thus each size-six fort has parity profile (0,6),(1,5),(5,1),(6,0). Mixed profiles contain N(u), giving a forbidden fifth disjoint neighborhood. Every remaining six-vertex monochromatic residual set fails the fort test: an opposite-parity vertex at distance two from the two same-parity centers has exactly one residual neighbor. Independent exhaustive checks verified all 906,192 size-six subsets, 1,600 four-center open packings, residual obstructions, the witness, and Q1–Q4 boundary cases. Q1 is an exceptional opposite-direction inequality ft(Q1)=1<rho^o(Q1)=2; the FINAL repaired slogan correctly limits first strict POSITIVE gap to d≥2. No statement for d>5 or infinite dimension is implied by the finite checks.

## originality

PASS

Best-of-knowledge originality for the EXACT integer fort number ft(Q5)=5 and the strict positive gap with open packing 4. The complete 2025 hypercube paper proves minimum-fort classification and only 4≤ft(Q5)≤6, while the 2023 foundational fort paper establishes general hypergraph/zero-forcing equivalences rather than this integer value. The new size-eight witness and six-fort parity/residual obstruction are not implied by prior bounds. Published-result searches found no exact covering theorem; absence of a hit alone was not treated as proof of priority.

## value

PASS

The exact d=5 fort number resolves the first non-power-of-two integer gap left explicitly by 2025 bounds, 4≤ft(Q5)≤6, for a natural zero-forcing-related graph invariant. The result exhibits a meaningful structural separation: optimal fort packing needs a nonminimum fort, whereas packing minimum open-neighborhood forts reaches only four. The six-fort obstruction supplies reusable parity/tiling reasoning; this is a natural exact finite boundary, not a routine restatement, arbitrary sliced computation, or code-only novelty claim. The final statement correctly handles the d=1 boundary and makes no unsupported general asymptotic promises.

The dated certificate retains the supplied scientific assessment, sources and limitations.
