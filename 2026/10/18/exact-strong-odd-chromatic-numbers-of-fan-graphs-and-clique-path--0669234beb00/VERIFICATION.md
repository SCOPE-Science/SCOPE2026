---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

At every clique vertex, all path color classes have odd global multiplicity, while path-neighbor parity forces unequal colors at distance two; properness forces distance one. Clique colors are distinct and disjoint from path colors. Thus a strong-odd coloring is exactly a path word with gaps ≥3 between identical symbols and every used class odd, plus r clique colors. For 1≤n≤6 a repeated class would require at least three occurrences spanning ≥7 positions, so all letters distinct. For n≥7, three colors force ABCABC… and are all odd precisely at n≡3(mod6); color-class oddness forces palette parity to agree with n. Explicit admissible seeds of lengths 3,4,5,7,8,12 and prefix block 012012 supply the sharp 3/4/5 upper bounds for every residue class. Independently checked parity-state minimal word palettes for path orders 1..36; finite checks corroborate the all-length combinatorial argument.

## originality

PASS

Best-of-knowledge PASS for the full exact K_r∨P_n spectrum, excluding the already published fan n=6 value χ_so(K1∨P6)=7. Prior bounds on outerplanar graph families and exact wheel coloring concern different statements and do not imply this nonmonotone six-periodic fan profile.

## value

PASS

Fan graphs are canonical outerplanar test cases and already contain a published sharp seven-color example. The complete infinite-family minimum and constructive parity profile reveal a nonmonotone drop 7→6→5→4 and a sharp six-periodic regime; these are natural chromatic invariants, not an arbitrary tiny table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
