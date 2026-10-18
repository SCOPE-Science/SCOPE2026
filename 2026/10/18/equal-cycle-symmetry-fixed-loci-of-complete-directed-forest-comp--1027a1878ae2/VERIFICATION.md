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

The proof reduces the geometric fixed-point locus to an explicitly defined phase-colored rooted-forest complex and proves its shellability via the vertex-expansion shelling property. The weighted directed matrix–forest determinant gives the exact sphere count. These are all-parameter deductions; finite experiments are not used as substitutes for them.

Execute `python3 verify_equal_cycle_fixed.py`. The verifier uses the standard library, constructs finite forest faces by parent maps, checks signed face sums and exact mod-two boundary ranks, then separately enumerates original invariant forests for two parameter pairs. The archived output ends with `VERIFY_OK 12`.

The code checks ten colored-forest parameter pairs and two direct fixed-point cases, not arbitrary \(k,d\). It does not certify any equivariant collapse of the full strong matching complex. No independent audit has occurred.
