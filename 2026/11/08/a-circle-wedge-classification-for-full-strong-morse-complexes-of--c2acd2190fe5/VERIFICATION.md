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

# Verification

The executable `verify.py` is self-contained and uses only Python's standard library. It checks the seven parameter pairs \((2,2),(2,3),(2,4),(3,3),(3,4),(4,4),(4,5)\). For each pair, the program enumerates every vertex ordering independently of the structural description, computes the filtration-gradient face set, reconstructs all star-and-flap faces, and verifies exact equality. It then executes all prescribed pairs as elementary collapses by checking **unique remaining cofaces** and proves the surviving face set consists exactly of full stars and one edge per flap. Finally, it checks the quotient graph has \(m+n\) vertices with exactly two edges for each bipartite pair and reports the predicted integral circle rank. The recorded standard output is in `verify_output.txt` and ends `ALL_VERIFY_OK`.

These experiments are finite corroboration, not proof for arbitrarily large \(m,n\). The mathematical proof is the complete total-order case split and symbolic free-face matching in `RESULT.md`. The data do not imply an equivariant statement, a pure-complex result, or an independent audit.
