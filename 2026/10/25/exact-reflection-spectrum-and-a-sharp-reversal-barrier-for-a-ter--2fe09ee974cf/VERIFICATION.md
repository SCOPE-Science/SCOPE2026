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

# Reproduction and limits

Execute `python3 verify.py`. The program uses only standard-library modules, visits each of the \(9840\) candidate ternary strings of lengths one through eight, and tests the seven forbidden factors in both orientations. It checks the complete reflection lists, builds a \(65\)-symbol prefix by seven morphism iterations, confirms all listed factors and their reversals occur there, and performs a separate longer-prefix comparison at lengths one through twenty-four.

The infinite theorem relies on the independently published global factor-complexity and avoidance theorems stated in References [1] of RESULT.md. The finite verifier does not purport to verify those published infinite assertions, and the length-twenty-four comparison is a sanity test rather than an infinite proof.

Independent audit has not been performed.
