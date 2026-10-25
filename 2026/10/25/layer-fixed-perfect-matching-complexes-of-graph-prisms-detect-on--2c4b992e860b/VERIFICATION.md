---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

Proof-critical checks: (1) horizontal two-edge orbits are present together at a fixed point; they must project to disjoint base edges; (2) every resulting base matching and compatible rung subset extends by remaining rungs; (3) the midpoint map on invariant orbit simplices is a PL homeomorphism onto the geometric fixed locus; (4) the acyclic face pairing is exhaustive except for base perfect matchings, and a directed cycle cannot enlarge a base matching or reverse a pendant-edge pivot; (5) the remaining zero-cell and common-dimensional cells give the full integral homotopy type, including the zero-sphere case; (6) the reduced Lefschetz formula uses Euler characteristic of fixed geometric points.

Run `python3 verify.py` with standard-library Python 3. The script enumerates prism PMC facets and invariant simplices rather than assuming the theorem; it separately enumerates the fully whiskered graph's ordinary matching faces and tests their equality. Exhaustive labeled base graphs through five vertices and four larger cases total 1,103. Full augmented Hasse diagram topological sorts provide 79 direct acyclicity tests. The verification returned: `PASS: 1103 base graphs; 79 acyclic full matching certificates`. All 1,103 also satisfy the exact reduced Euler formula. The script is finite corroboration only; no finite experiment substitutes for the uniform mathematical proof. Independent audit and independent validation are not performed.
