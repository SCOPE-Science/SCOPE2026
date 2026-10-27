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

# Verification of enumerative canonical-rotation theorem

Execute `python3 verify.py` in the same directory. The program requires only the standard Python library. It runs exhaustive direct cyclic-rotation comparisons for all binary words through length \(18\) (including all eligible necklaces), independently evaluates the binomial composition coefficients, and tests the general cyclic-\(00\) necessary condition on all primitive words through length \(14\).

Expected success marker: `GALOIS_LYNDON_UNIQUE_SHORTEST_PASS`. The finite executable checks do not prove the unrestricted infinite theorem: the parity, bijection, analytic estimates, and global density bounds are justified in `RESULT.md`. Independent audit has not been performed.
