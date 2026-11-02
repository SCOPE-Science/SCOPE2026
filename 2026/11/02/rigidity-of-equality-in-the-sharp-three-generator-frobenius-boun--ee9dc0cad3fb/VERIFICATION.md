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

# Verification and scope

The complete theorem is established deductively in `RESULT.md`. Its core Kneser bound and the Apéry maximum argument apply to all ordered coprime triples. The two-generator equality examples use the Sylvester formula, and the unit-generator convention is explicit.

For a separate finite arithmetic diagnostic, run `python3 verify.py 95`. The script independently computes least representable sums in each residue class modulo the largest generator using Dijkstra's shortest-path algorithm, checks the newly published upper bound, and tests agreement with the claimed iff criterion. The observed output is:

`PASS: checked 116920 coprime triples, 92 equality cases, 3<=c<=95`

This finite diagnostic is not an exhaustive verification of the infinite theorem. The Kneser and Sylvester results are established classical mathematical inputs; their complete proofs are not bundled. Independent audit is not performed.
