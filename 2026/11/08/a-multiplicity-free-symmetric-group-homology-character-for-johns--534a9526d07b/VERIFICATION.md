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

Run `python3 verify_johnson_equivariant.py` with Python 3 using no third-party packages. The program constructs simplices directly from the two types of Johnson cliques, checks all conjugacy classes of the natural symmetric group action with explicit orientation signs, computes independent cycle-count characters and Murnaghan–Nakayama irreducible characters, and verifies full mod-two boundary ranks for the four smaller parameter cases. It reports `VERIFY_OK cases=6 class_trace_checks=130 mod2_full_chain_checks=4` on completion; see `VERIFIER_OUTPUT.txt`. The unbounded mathematical quantifiers are proven in `RESULT.md`, not inferred from these finite checks. This verification is a self-review and is not an independent audit.
