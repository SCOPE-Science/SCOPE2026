---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For n>=3, overlap de Bruijn graph has edge set U_n and strongly connected vertices of admissible (n-1)-words. Supply-imbalance sources have differing first pair/equal final pair; any balancing path from s to sink must traverse at least d(s), first later equal-pair index. Appending opposite bits for exactly d(s) steps reaches a sink, and the last equal-pair position in the endpoint recovers s uniquely; this bijects all sources and sinks. An Euler circuit of the augmented graph gives an admissible cyclic cover with exactly sum d(s)=2F_(n-1)-2 extra edges; Fibonacci recurrence yields M_n. n=2 handled separately by 0011. Independent independent-overlap graph BFS plus exact assignment calculation for n=3..10 gave M_n=6,12,20,34,56,92,150,244 and matching extra counts, without using finite testing as the all-n proof.

## originality

PASS

The exact minimum repeated-edge cover length and optimal source-to-sink flow for the entire no-triple word family are not stated by accessible primary papers. Moreno-Matamala minimum means lexicographic ordering among exact-once cycles over circularly admissible dictionaries; Tan-Shallit study arbitrary factor-dictionary shortest witnesses with general bounds; Chee et al maximize nonrepeated constrained cycles. No compared theorem implies the exact Lucas formula for the *freely admissible* U_n. Residual older/unknown restricted-language postman special case possible.

## value

PASS

The full natural run-length-limited binary dictionary has a meaningful shortest universal cyclic covering length; the result gives exact all-n length, unavoidable duplication, constructive optimum and a sharp graph-theoretic flow classification, rather than a small example or trivial transfer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
