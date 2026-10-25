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

PASS. In H[K_s], adjacent vertices within each clique are true twins. If x,y take distinct colors a,b and A,B count their external common neighbors of those colors, strict unique plurality would require A>B+1 and B>A+1, contradiction. Consequently each clique has constant color, and each vertex sees (s-1)+s*t_own same-colored neighbors versus s*t_other of a competing color; for integers and s>=2, strict inequality iff t_own>=t_other, proving size-independent reduction to weak plurality on H. On base degree-one/two paths and cycles weak plurality iff every nonconstant color run length >=2, with endpoints constrained; compositions of n into r lengths>=2 give C(n-r-1,r-1) for paths, and marked cyclic boundaries give (n/r)C(n-r-1,r-1) for cycles; appropriate proper run color factors establish exact formulas, n=1 isolated case q and components product. Independent brute named-color enumeration on eight small path/cycle blowups, including s=3, agrees. General true-twin theorem and unbounded closed sums are deductive, not extrapolated from brute force.

## originality

PASS

Best-of-knowledge PASS after actual Git proof and independent bounded checks, Resultary semantic search, and comparisons of the precise claim against materially read primary texts and theorem scopes. No examined theorem/database supplies the same final formula or exact incidence certificate. Identified overlaps and access limits are credited; failed searches alone are not treated as a proof of novelty.

## value

PASS

PASS. True-twin rigidity changes strict neighborhood plurality on clique blowups into weak plurality on the quotient for every H, with a surprising exact independence from uniform clique size s>=2. This structural reduction has stand-alone use, and the full closed path/cycle/max-degree-two formulas give natural unbounded-degree graph classes explicitly. The result is not ordinary proper coloring or a direct restatement of the universal partition polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
