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

Even sums of the original five consecutive generators are obtained using the two even generators x,x+1 and pairs of the three odd generators, reducing to x,x+1,2x−1,2x+3. For b=x+1,c=2x−1,d=2x+3, identities b+c=3x, c+d=2b+2x, and 3b=d+x reduce each Apéry factorization to either a pure c-power or d-powers plus at most two b, yielding the stated minimum formula in every residue. Subtracting branches gives x(2x−1−8q−3s) for residue r=3q+s, producing the exact cutoff R by x mod4. The standard Apéry partial order tests successors under b,c,d and yields maximal residues {R,R+1}, {R−1,R,R+1}, {R−2,R}, {R−2,R,R+1} for residues x mod4=0,1,2,3. Subtract x to obtain PF rows and type. The x=4 redundant-generator boundary is included. Fresh independent Dijkstra residue shortest-path computation, not the formula itself, verified all Apéry minima and PF maximal elements for x=4..250; finite checks do not replace the all-x normal-form proof.

## originality

PASS

Liu 2023 provides quotient formulas for almost-arithmetic progressions under divisor p|first generator, excluding the present denominator 2 and odd first generator; it primarily gives Frobenius/genus, not the whole PF set. Morales–Nguyen Thi Dung 2026 describes PF sets of generalized almost-arithmetic generating systems, with a required arithmetic generator block that these four reduced generators do not possess uniformly for x>=4. An older Adeniran quotient article was located indirectly but not obtained in full, leaving a specific implicit-coverage risk. No equivalent uniform Apéry and PF classification emerged in Resultary searches; this is only best-of-knowledge originality.

## value

PASS

The halved semigroup of five consecutive generators is a natural arithmetic quotient family, and its complete pseudo-Frobenius set is a natural invariant finer than Frobenius number or genus. The exact Apéry two-branch staircase, a tie-induced exception and mod-four type dichotomy classify all odd starts rather than a numerical list, so the result is a substantive arithmetic classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
