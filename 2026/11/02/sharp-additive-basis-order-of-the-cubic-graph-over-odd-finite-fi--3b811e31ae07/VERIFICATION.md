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

# Mathematical and computational verification

Run `python3 verify_cubic_graph.py` to verify the finite experiments using only the Python standard library. It constructs field operations for the prime fields of sizes 3, 5, 7, 11, 13, 17, 19 and 23, and quadratic extensions of sizes 9, 25, 49 and 121 (with checked nonsquare parameters). It independently constructs complete twofold and threefold sumsets; for the two exceptional odd fields it also constructs fourfold sumsets. All 12 checks passed with final line `VERIFY_OK 12 fields, exact sumsets and sharp boundary cases`.

The cubic identity and the two affine derivative equations are symbolic deductions independent of computer output. The projective curve has exactly three rational points at infinity. The classical Hasse bound guarantees more than three points for all field orders at least eleven, giving a global proof beyond the enumerated fields. At field orders five and seven the explicit residue lists give the exact omitted pairs; scaling and an elementary cardinality argument complete those finite proofs.

No machine computation, source abstract, literature query, or prior unpublished statement independently certifies priority or the unrestricted mathematical claim. Independent mathematical audit remains not performed.
